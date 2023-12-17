/*
 * The module entry point for ``_objc``. This file contains ``init_objc``
 * and the implementation of a number of exported functions.
 */
#include "pyobjc.h"
#include <objc/Protocol.h>
#include <objc/objc-sync.h>

#include <ctype.h>
#include <netinet/in.h>
#include <stddef.h>
#include <sys/socket.h>
#include <sys/un.h>

#import <Foundation/NSAutoreleasePool.h>
#import <Foundation/NSBundle.h>
#import <Foundation/NSProcessInfo.h>
#import <Foundation/NSString.h>

#import <mach-o/dyld.h>
#import <mach-o/getsect.h>
#import <mach-o/loader.h>
#import <objc/Protocol.h>

#include <dlfcn.h>

NS_ASSUME_NONNULL_BEGIN

static int PyObjC_Initialized = 0;

PyObject* _Nullable PyObjCClass_DefaultModule;

PyObject* _Nullable PyObjC_TypeStr2CFTypeID;

static NSAutoreleasePool* _Nullable global_release_pool;

/* Calculate the current version of macOS in a format that
 * can be compared with MAC_OS_VERSION_X_... constants
 */

#if PyObjC_BUILD_RELEASE < 1010
typedef struct {
    long majorVersion;
    long minorVersion;
    long patchVersion;
} NSOperatingSystemVersion;
#endif

static NSOperatingSystemVersion gSystemVersion = {0, 0, 0};

/*
 * XXX:
 * 1. Move function to a utility file and expose to ctests.m for testing.
 * 2. Split the legacy code path to a separate function for testing.
 * 3. Only enable the legacy code when the deployment target is 10.9
 */
static void
calc_current_version(void)
{
#if PyObjC_BUILD_RELEASE >= 1010
    if ([NSProcessInfo instancesRespondToSelector:@selector(operatingSystemVersion)]) {
        NSAutoreleasePool* pool;

        pool           = [[NSAutoreleasePool alloc] init];
        gSystemVersion = [[NSProcessInfo processInfo] operatingSystemVersion];
        [pool release];

    } else
#endif
    {
        /* Code path for macOS 10.9 or earlier. Don't use Gestalt because that's
         * deprecated. */
        NSAutoreleasePool* pool;
        NSDictionary*      plist;
        NSArray*           parts;

        pool = [[NSAutoreleasePool alloc] init];

        plist = [NSDictionary dictionaryWithContentsOfFile:
                                  @"/System/Library/CoreServices/SystemVersion.plist"];
        if (!plist) {
            NSLog(@"Cannot determine system version");
            return;
        }

        parts = [[plist valueForKey:@"ProductVersion"] componentsSeparatedByString:@"."];

        if (!parts || [parts count] < 2) {
            NSLog(@"Cannot determine system version");
            return;
        }

        gSystemVersion.majorVersion = [[parts objectAtIndex:0] intValue];
        gSystemVersion.minorVersion = [[parts objectAtIndex:1] intValue];

        if (parts.count >= 3) {
            gSystemVersion.patchVersion = [[parts objectAtIndex:2] intValue];
        }

        [pool release];
    }
}

PyObjC_FINAL_CLASS @interface OC_NSAutoreleasePoolCollector : NSObject
/*
 * This class is used to automatically reset the
 * global pool when an outer autorelease pool is
 * recycled. This avoids problems when a python
 * plugin is loaded in an Objective-C program.
 */
{
}
+ (void)newAutoreleasePool;
+ (void)targetForBecomingMultiThreaded:(id)sender;
@end

@implementation OC_NSAutoreleasePoolCollector
+ (void)newAutoreleasePool
{
    OC_NSAutoreleasePoolCollector* value = [[self alloc] init];
    global_release_pool                  = [[NSAutoreleasePool alloc] init];
    (void)[value autorelease];
}

- (void)dealloc
{
    global_release_pool = nil;
    [super dealloc];
}

/* XXX: This selector doesn't belong here... */
+ (void)targetForBecomingMultiThreaded:(id)sender
{
    [sender self];
}

@end

PyDoc_STRVAR(pyobjc_id_doc, "pyobjc_id(obj)\n" CLINIC_SEP "\n"
                            "Return the id of the underlying NSObject as an int.");

static PyObject* _Nullable pyobjc_id(PyObject* self __attribute__((__unused__)),
                                     PyObject* args, PyObject* kwds)
{
    static char* keywords[] = {"obj", NULL};
    PyObject*    o;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "O", keywords, &o)) {
        return NULL;
    }

    if (!PyObjCObject_Check(o)) {
        PyErr_SetString(PyExc_TypeError, "not an Objective-C object");
        return NULL;
    }
    return PyLong_FromVoidPtr((void*)PyObjCObject_GetObject(o));
}

PyDoc_STRVAR(repythonify_doc, "repythonify(obj, type='@')\n" CLINIC_SEP "\n"
                              "Put an object through the bridge by calling \n"
                              "depythonify_c_value then pythonify_c_value.\n"
                              "This is for internal use only.");

static PyObject* _Nullable repythonify(PyObject* self __attribute__((__unused__)),
                                       PyObject* _Nullable args, PyObject* _Nullable kwds)
{
    static char* keywords[] = {"obj", "type", NULL};
    const char*  type       = "@";
    PyObject*    rval;
    void*        datum;
    Py_ssize_t   size;
    PyObject*    o;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "O|y", keywords, &o, &type)) {
        return NULL;
    }

    size = PyObjCRT_SizeOfType(type);
    if (size == -1) {
        return NULL;
    }

    datum = PyMem_Malloc(size);
    if (datum == NULL) {         // LCOV_BR_EXCL_LINE
        return PyErr_NoMemory(); // LCOV_EXCL_LINE
    }

    if (depythonify_c_value(type, o, datum)) {
        PyMem_Free(datum);
        return NULL;
    }

    rval = pythonify_c_value(type, datum);
    PyMem_Free(datum);
    return rval;
}

static PyObject* _Nullable m_sizeoftype(PyObject* self __attribute__((__unused__)),
                                        PyObject* value)
{
    if (!PyBytes_Check(value)) {
        PyErr_SetString(PyExc_TypeError, "value must be a byte string");
        return NULL;
    }

    Py_ssize_t size = PyObjCRT_SizeOfType(PyBytes_AsString(value));
    if (size == -1) {
        return NULL;
    }

    return PyLong_FromSsize_t(size);
}

PyDoc_STRVAR(macos_available_doc,
             "macos_available(major, minor, patch=0)\n" CLINIC_SEP "\n"
             "Return true if the current macOS release is "
             "at least the provided version");

static PyObject* _Nullable macos_available(PyObject* self __attribute__((__unused__)),
                                           PyObject* _Nullable args,
                                           PyObject* _Nullable kwds)
{
    static char* keywords[] = {"major", "minor", "patch", NULL};
    long         major;
    long         minor;
    long         patch = 0;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "ll|l", keywords, &major, &minor,
                                     &patch)) {
        return NULL;
    }

    if (major > gSystemVersion.majorVersion) {
        Py_RETURN_FALSE;
    } else if (major == gSystemVersion.majorVersion) {
        if (minor > gSystemVersion.minorVersion) {
            Py_RETURN_FALSE;
        } else if (minor == gSystemVersion.minorVersion) {
            if (patch > gSystemVersion.patchVersion) {
                Py_RETURN_FALSE;
            } else {
                Py_RETURN_TRUE;
            }
        } else {
            Py_RETURN_TRUE;
        }

    } else {
        Py_RETURN_TRUE;
    }
}

PyDoc_STRVAR(lookUpClass_doc,
             "lookUpClass(class_name)\n" CLINIC_SEP "\n"
             "Search for the named classes in the Objective-C runtime and return it.\n"
             "Raises noclass_error when the class doesn't exist.");

static PyObject* _Nullable lookUpClass(PyObject* self __attribute__((__unused__)),
                                       PyObject* _Nullable args, PyObject* _Nullable kwds)
{
    static char* keywords[] = {"class_name", NULL};
    char*        class_name = NULL;
    Class        objc_class;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "s", keywords, &class_name)) {
        return NULL;
    }

    objc_class = objc_lookUpClass(class_name);
    if (objc_class == NULL) {
        PyErr_SetString(PyObjCExc_NoSuchClassError, class_name);
        return NULL;
    }
    return PyObjCClass_New(objc_class);
}

PyDoc_STRVAR(classAddMethods_doc,
             "classAddMethods(targetClass, methodsArray)\n" CLINIC_SEP "\n"
             "Adds methods in methodsArray to class. The effect is similar to how \n"
             "categories work. If class already implements a method as defined in \n"
             "methodsArray, the original implementation will be replaced by the \n"
             "implementation from methodsArray.");

static PyObject* _Nullable classAddMethods(PyObject* self __attribute__((__unused__)),
                                           PyObject* _Nullable args,
                                           PyObject* _Nullable keywds)
{
    static char* kwlist[]     = {"targetClass", "methodsArray", NULL};
    PyObject*    classObject  = NULL;
    PyObject*    methodsArray = NULL;

    if (!PyArg_ParseTupleAndKeywords(args, keywds, "OO:classAddMethods", kwlist,
                                     &classObject, &methodsArray)) {
        return NULL;
    }

    if (!PyObjCClass_Check(classObject)) {
        PyErr_SetString(PyExc_TypeError,
                        "Argument 'targetClass' (pos 1) is not an Objective-C class");
        return NULL;
    }

    methodsArray = PySequence_Fast(methodsArray,
                                   "Argument 'methodsArray' (pos 2) must be a sequence");
    if (methodsArray == NULL)
        return NULL;

    int r = PyObjCClass_AddMethods(classObject, PySequence_Fast_ITEMS(methodsArray),
                                   PySequence_Fast_GET_SIZE(methodsArray));
    Py_DECREF(methodsArray);

    if (r == -1) {
        return NULL;
    }

    Py_INCREF(Py_None);
    return Py_None;
}

PyDoc_STRVAR(have_autorelease_pool_doc,
             "_haveAutoreleasePool()\n" CLINIC_SEP "\n"
             "Return True iff the global release pool is present");
static PyObject*
have_autorelease_pool(PyObject* self __attribute__((__unused__)))
{
    PyObject* result = global_release_pool ? Py_True : Py_False;
    Py_INCREF(result);
    return result;
}

PyDoc_STRVAR(remove_autorelease_pool_doc,
             "removeAutoreleasePool()\n" CLINIC_SEP "\n"
             "This removes the global NSAutoreleasePool. You should do this\n"
             "at the end of a plugin's initialization script.\n");

static PyObject* _Nullable remove_autorelease_pool(PyObject* self
                                                   __attribute__((__unused__)))

{
    NSAutoreleasePool* pool;
    Py_BEGIN_ALLOW_THREADS
        @try {
            /* Unconditionally clear the global autorelease pool,
             * there's not much we can do if releasing raises.
             */
            pool                = global_release_pool;
            global_release_pool = nil;
            [pool release];

        } @catch (NSObject* localException) {
            PyObjCErr_FromObjC(localException);
        }

    Py_END_ALLOW_THREADS

    if (PyErr_Occurred())
        return NULL;

    Py_INCREF(Py_None);
    return Py_None;
}

PyDoc_STRVAR(recycle_autorelease_pool_doc,
             "recycleAutoreleasePool()\n" CLINIC_SEP "\n"
             "This 'releases' the global autorelease pool and creates a new one.\n"
             "This method is for system use only\n");
static PyObject* _Nullable recycle_autorelease_pool(PyObject* self
                                                    __attribute__((__unused__)))
{
    NSAutoreleasePool* pool;
    Py_BEGIN_ALLOW_THREADS
        @try {
            /* Unconditionally set global_release_pool to nil
             * before calling release. There's not much we can
             * do if draining fails with an exception.
             */
            pool                = global_release_pool;
            global_release_pool = nil;
            [pool release];

        } @catch (NSObject* localException) {
            PyObjCErr_FromObjC(localException);
        }

        /* No need to guard this with an @try, the API's we use
         * should never raise.
         */
        [OC_NSAutoreleasePoolCollector newAutoreleasePool];
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred())
        return NULL;

    Py_INCREF(Py_None);
    return Py_None;
}

PyDoc_STRVAR(getClassList_doc,
             "getClassList(ignore_invalid_identifiers=False)\n" CLINIC_SEP "\n"
             "Return a list with all Objective-C classes known to the runtime.\n");
static PyObject* _Nullable getClassList(PyObject* self __attribute__((__unused__)),
                                        PyObject* args)
{
    int ignore_invalid_identifiers = 0;
    if (!PyArg_ParseTuple(args, "|p", &ignore_invalid_identifiers)) {
        return NULL;
    }
    return PyObjC_GetClassList(ignore_invalid_identifiers);
}

PyDoc_STRVAR(currentBundle_doc, "currentBundle()\n" CLINIC_SEP "\n"
                                "Get the current bundle during module initialization.\n"
                                "Works for plug-ins and applications.\n"
                                "\n"
                                "Note that this is the default bundle used by\n"
                                "NibClassBuilder.extractClasses(...),\n"
                                "so calling it explicitly is rarely useful.\n"
                                "After module initialization, use\n"
                                "NSBundle.bundleForClass_(ClassInYourBundle).");
static PyObject* _Nullable currentBundle(PyObject* self __attribute__((__unused__)))
{
    char* bundle_address = getenv("PYOBJC_BUNDLE_ADDRESS");
    if (bundle_address) {
        char* endptr = NULL;
        long  rval   = strtol(bundle_address, &endptr, 16);

        /* Check that the entire string is consumed and that the
         * conversion didn't fail. The latter should also check
         * errno, but error return values from strtol aren't valid
         * pointers anyway.
         */
        if (endptr && *endptr == '\0') {
            if (rval != 0 && rval != LONG_MIN && rval != LONG_MAX) {
                return id_to_python((id)rval);
            }
        }
    }
    return id_to_python([NSBundle mainBundle]);
}

PyDoc_STRVAR(loadBundle_doc,
             "loadBundle(module_name, module_globals, bundle_path=None, "
             "bundle_identifier=None, scan_classes=True)\n" CLINIC_SEP "\n"
             "Load the bundle identified by 'bundle_path' or 'bundle_identifier' \n"
             "and add the classes in the bundle to the 'module_globals'.\n"
             "If 'scan_classes' is False the function won't add classes to "
             "'module_globals'"
             "\n"
             "If 'bundle_identifier' is specified the right bundle is located\n"
             "using NSBundle's +bundleWithIdentifier:.\n"
             "If 'bundle_path' is specified the right bundle is located using\n"
             "NSBundle's +bundleWithPath:. The path must be an absolute pathname\n");
static PyObject* _Nullable loadBundle(PyObject* self __attribute__((__unused__)),
                                      PyObject* _Nullable args, PyObject* _Nullable kwds)
{
    static char* keywords[] = {"module_name",       "module_globals", "bundle_path",
                               "bundle_identifier", "scan_classes",   NULL};
    NSBundle*    bundle     = nil;
    id           bundle_identifier = nil;
    id           bundle_path       = nil;
    PyObject*    module_name;
    PyObject*    module_globals;
    PyObject*    class_list;
    Py_ssize_t   len, i;
    PyObject*    scanClasses = NULL;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "UO|O&O&O", keywords, &module_name,
                                     &module_globals, PyObjCObject_Convert, &bundle_path,
                                     PyObjCObject_Convert, &bundle_identifier,
                                     &scanClasses)) {
        return NULL;
    }

    if (!bundle_path && !bundle_identifier) {
        PyErr_SetString(PyExc_ValueError, "Need to specify either bundle_path or "
                                          "bundle_identifier");
        return NULL;
    }
    if (bundle_path && bundle_identifier) {
        PyErr_SetString(PyExc_ValueError, "Need to specify either bundle_path or "
                                          "bundle_identifier");
        return NULL;
    }

    if (bundle_path) {
        if (![bundle_path isKindOfClass:[NSString class]]) {
            PyErr_SetString(PyExc_TypeError, "bundle_path is not a string");
            return NULL;
        }
        bundle = [NSBundle bundleWithPath:bundle_path];
    } else {
        if (![bundle_identifier isKindOfClass:[NSString class]]) {
            PyErr_SetString(PyExc_TypeError, "bundle_identifier is not a string");
            return NULL;
        }
        bundle = [NSBundle bundleWithIdentifier:bundle_identifier];
    }

    if (![bundle load]) {
        PyErr_SetString(PyExc_ImportError, "Bundle could not be loaded");
        return NULL;
    }

    /*
     * Scanning the class list is expensive and something to be avoided
     * when possible.
     */

    if (scanClasses != NULL && !PyObject_IsTrue(scanClasses)) {
        return pythonify_c_value(@encode(NSBundle*), &bundle);
    }

    class_list = PyObjC_GetClassList(1);
    if (class_list == NULL) {
        return NULL;
    }

    len = PyTuple_GET_SIZE(class_list);
    for (i = 0; i < len; i++) {
        PyObject*   item;
        const char* nm;

        item = PyTuple_GET_ITEM(class_list, i);
        if (item == NULL) {
            continue;
        }

        nm = ((PyTypeObject*)item)->tp_name;

        if (nm[0] == '%') {
            /* skip, posed-as type */
        } else if (strcmp(nm, "Object") == 0 || strcmp(nm, "List") == 0
                   || strcmp(nm, "Protocol") == 0) {
            /* skip, these have been deprecated since OpenStep! */
        } else if (PyDict_SetItemString(module_globals, ((PyTypeObject*)item)->tp_name,
                                        item)
                   == -1) {
            Py_DECREF(class_list);
            class_list = NULL;
            return NULL;
        }
    }
    Py_XDECREF(class_list);
    class_list = NULL;

    return pythonify_c_value(@encode(NSBundle*), &bundle);
}

PyDoc_STRVAR(objc_splitSignature_doc, "splitSignature(signature)\n" CLINIC_SEP "\n"
                                      "Split a signature string into a list of items.");
static PyObject* _Nullable objc_splitSignature(PyObject* self __attribute__((__unused__)),
                                               PyObject* _Nullable args,
                                               PyObject* _Nullable kwds)
{
    static char* keywords[] = {"signature", NULL};
    const char*  signature;
    const char*  end;
    PyObject*    result;
    PyObject*    tuple;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "y", keywords, &signature)) {
        return NULL;
    }

    result = PyList_New(0);
    if (result == NULL) // LCOV_BR_EXCL_LINE
        return NULL;    // LCOV_EXCL_LINE

    while (signature && *signature != 0) {
        PyObject*   str;
        const char* t;

        end = PyObjCRT_SkipTypeSpec(signature);
        if (end == NULL) {
            Py_DECREF(result);
            return NULL;
        }

        t = end - 1;
        while (t != signature && isdigit(*t)) {
            t--;
        }
        t++;

        str = PyBytes_FromStringAndSize(signature, t - signature);
        if (str == NULL) {     // LCOV_BR_EXCL_LINE
            Py_DECREF(result); // LCOV_EXCL_LINE
            return NULL;       // LCOV_EXCL_LINE
        }

        if (PyList_Append(result, str) == -1) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(str);
            Py_DECREF(result);
            return NULL;
            // LCOV_EXCL_STOP
        }
        Py_DECREF(str);

        signature = end;
    }

    tuple = PyList_AsTuple(result);
    Py_DECREF(result);
    return tuple;
}

PyDoc_STRVAR(objc_splitStructSignature_doc,
             "splitStructSignature(signature)\n" CLINIC_SEP "\n"
             "Split a struct signature string into a list of items.");
static PyObject* _Nullable objc_splitStructSignature(PyObject* self
                                                     __attribute__((__unused__)),
                                                     PyObject* _Nullable args,
                                                     PyObject* _Nullable kwds)
{
    static char* keywords[] = {"signature", NULL};
    const char*  signature;
    const char*  end;
    PyObject*    structname;
    PyObject*    fields;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "y", keywords, &signature)) {
        return NULL;
    }

    if (signature[0] != _C_STRUCT_B) {
        PyErr_SetString(PyExc_ValueError, "not a struct encoding");
        return NULL;
    }

    signature += 1;
    end = signature;
    while (*end && *end != _C_STRUCT_E && *end++ != '=')
        ;
    if (end == signature + 1) {
        structname = Py_None;
        Py_INCREF(structname);

    } else {
        structname = PyUnicode_FromStringAndSize(signature, end - signature - 1);
        if (structname == NULL) {
            return NULL;
        }
    }

    if (*end == '=') {
        signature = end + 1;
    } else {
        signature = end;
    }

    fields = PyList_New(0);
    if (fields == NULL) // LCOV_BR_EXCL_LINE
        return NULL;    // LCOV_EXCL_LINE

    while (signature && *signature != _C_STRUCT_E && *signature != 0) {
        PyObject*   str;
        PyObject*   item;
        PyObject*   name;
        const char* t;

        if (*signature == '"') {
            signature++;
            end = signature;
            while (*end && *end != '"') {
                end++;
            }
            name = PyUnicode_FromStringAndSize(signature, end - signature);
            if (name == NULL) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                Py_DECREF(structname);
                Py_DECREF(fields);
                return NULL;
                // LCOV_EXCL_STOP
            }

            signature = end + 1;

        } else {
            name = Py_None;
            Py_INCREF(name);
        }

        end = PyObjCRT_SkipTypeSpec(signature);
        if (end == NULL) {
            Py_DECREF(structname);
            Py_DECREF(name);
            Py_DECREF(fields);
            return NULL;
        }

        t = end - 1;
        while (t != signature && isdigit(*t)) {
            t--;
        }
        t++;

        str = PyBytes_FromStringAndSize(signature, t - signature);
        if (str == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(structname);
            Py_DECREF(name);
            Py_DECREF(fields);
            return NULL;
            // LCOV_EXCL_STOP
        }

        item = Py_BuildValue("NN", name, str);
        if (item == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(fields);
            return NULL;
            // LCOV_EXCL_STOP
        }

        if (PyList_Append(fields, item) == -1) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(fields);
            Py_DECREF(item);
            Py_DECREF(structname);
            // LCOV_EXCL_STOP
            return NULL;
        }
        Py_DECREF(item);

        signature = end;
    }

    if (signature && *signature != _C_STRUCT_E) {
        Py_DECREF(structname);
        Py_DECREF(fields);
        PyErr_SetString(PyExc_ValueError, "value is not a complete struct signature");
        return NULL;
    }

    if (signature && signature[1]) {
        Py_DECREF(structname);
        Py_DECREF(fields);
        PyErr_SetString(PyExc_ValueError, "additional text at end of signature");
        return NULL;
    }

    return Py_BuildValue("NN", structname, fields);
}

PyDoc_STRVAR(PyObjC_loadBundleVariables_doc,
             "loadBundleVariables(bundle, module_globals, variableInfo, "
             "skip_undefined=True)\n" CLINIC_SEP "\n"
             "Load the specified variables in the bundle. If skip_undefined is \n"
             "True, variables that are not present in the bundle are skipped, \n"
             "otherwise this method raises objc.error when a variable cannot be \n"
             "found.\n"
             "\n"
             "variableInfo is a list of (name, type) pairs. The type is the \n"
             "Objective-C type specifier for the variable type.");
PyDoc_STRVAR(PyObjC_loadBundleFunctions_doc,
             "loadBundleFunctions(bundle, module_globals, functionInfo, "
             "skip_undefined=True)\n" CLINIC_SEP "\n"
             "Load the specified functions in the bundle. If skip_undefined is \n"
             "True, variables that are not present in the bundle are skipped, \n"
             "otherwise this method raises objc.error when a variable cannot be \n"
             "found.\n"
             "\n"
             "functionInfo is a list of (name, signature, doc [, methinfo]) triples. \n"
             "The signature is the Objective-C type specifier for the function \n"
             "signature.");
PyDoc_STRVAR(PyObjC_loadFunctionList_doc,
             "loadFunctionList(list, module_globals, functionInfo, "
             "skip_undefined=True)\n" CLINIC_SEP "\n"
             "Load the specified functions. List should be a capsule object containing\n"
             "an array of { char*, function } structs.");
PyDoc_STRVAR(PyObjC_loadSpecialVar_doc,
             "loadSpecialVar(bundle, module_globals, typeid, name, "
             "skip_undefined=True)\n" CLINIC_SEP "\n"
             "Load a magic cookie object from a bundle. A magic cookie is a \n"
             "C pointer that represents a CoreFoundation or Objective-C object \n"
             "that cannot be deferenced.\n");

PyDoc_STRVAR(protocolsForProcess_doc,
             "protocolsForProcess()\n" CLINIC_SEP "\n"
             "Returns a list of Protocol objects that are present in the process");
static PyObject* _Nullable protocolsForProcess(PyObject* self __attribute__((__unused__)))
{
    PyObject*    protocols;
    Protocol**   protlist;
    unsigned int protCount;
    unsigned int i;

    protlist = objc_copyProtocolList(&protCount);
    if (protlist == NULL) {
        Py_INCREF(Py_None);
        return Py_None;
    }

    protocols = PyList_New(protCount);

    if (protocols == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;         // LCOV_EXCL_LINE
    }

    for (i = 0; i < protCount; i++) {
        PyObject* p = PyObjCFormalProtocol_ForProtocol(protlist[i]);
        if (p == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(protocols);
            free(protlist);
            return NULL;
            // LCOV_EXCL_STOP
        }

        PyList_SET_ITEM(protocols, i, p);
    }

    free(protlist);
    return protocols;
}

PyDoc_STRVAR(idSignatures_doc,
             "_idSignatures()\n" CLINIC_SEP "\n"
             "Returns a list of type encodings that refer to 'id' or 'CFTypeRef'\n");
static PyObject* _Nullable idSignatures(PyObject* self __attribute__((__unused__)))
{
    return PyObjCPointer_GetIDEncodings();
}

PyDoc_STRVAR(protocolNamed_doc,
             "_protocolNamed(name)\n" CLINIC_SEP "\n"
             "Returns an Objective-C protocol named *name*.\n"
             "Raises AttributeError when no such protocol can be found.\n");
static PyObject* _Nullable protocolNamed(PyObject* self __attribute__((__unused__)),
                                         PyObject* _Nullable args,
                                         PyObject* _Nullable kwds)
{
    static char* keywords[] = {"name", NULL};
    char*        name;
    Protocol*    p;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "s", keywords, &name)) {
        return NULL;
    }

    p = objc_getProtocol(name);

    if (p == NULL) {
        PyErr_SetString(PyExc_AttributeError, name);
        return NULL;
    }

    return PyObjCFormalProtocol_ForProtocol(p);
}

PyDoc_STRVAR(protocolsForClass_doc,
             "protocolsForClass(cls)\n" CLINIC_SEP "\n"
             "Returns a list of Protocol objects that the class claims\n"
             "to implement directly.");
static PyObject* _Nullable protocolsForClass(PyObject* self __attribute__((__unused__)),
                                             PyObject* _Nullable args,
                                             PyObject* _Nullable kwds)
{
    static char* keywords[] = {"cls", NULL};
    Protocol**   protocol_list;
    unsigned int protocol_count, i;
    PyObject*    protocols;
    Class        cls;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "O&:protocolsForClass", keywords,
                                     PyObjCClass_Convert, &cls)) {
        return NULL;
    }

    protocols = PyList_New(0);
    if (protocols == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;         // LCOV_EXCL_LINE
    }

    protocol_list = class_copyProtocolList(cls, &protocol_count);

    /* Documented API: the list will only be NULL if the count is 0 */
    PyObjC_Assert(protocol_count == 0 || protocol_list != NULL, NULL);

    for (i = 0; i < protocol_count; i++) {
        PyObject* protocol = PyObjCFormalProtocol_ForProtocol(protocol_list[i]);
        if (protocol == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            free(protocol_list);
            Py_DECREF(protocols);
            return NULL;
            // LCOV_EXCL_STOP
        }
        if (PyList_Append(protocols, protocol) == -1) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(protocol);
            Py_DECREF(protocols);
            free(protocol_list);
            return NULL;
            // LCOV_EXCL_STOP
        }
        Py_DECREF(protocol);
    }

    free(protocol_list);
    return protocols;
}

PyDoc_STRVAR(createOpaquePointerType_doc,
             "createOpaquePointerType(name, typestr, doc)\n" CLINIC_SEP "\n"
             "Return a wrapper type for opaque pointers of the given type. The type \n"
             "will be registered with PyObjC and will be used to wrap pointers of the \n"
             "given type.");
static PyObject* _Nullable createOpaquePointerType(PyObject* self
                                                   __attribute__((__unused__)),
                                                   PyObject* _Nullable args,
                                                   PyObject* _Nullable kwds)
{
    static char* keywords[] = {"name", "typestr", "doc", NULL};
    char*        name;
    char*        typestr;
    char*        docstr = NULL;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "sy|z", keywords, &name, &typestr,
                                     &docstr)) {
        return NULL;
    }

    return PyObjCCreateOpaquePointerType(name, typestr, docstr);
}

PyDoc_STRVAR(copyMetadataRegistry_doc, "_copyMetadataRegistry()\n" CLINIC_SEP "\n"
                                       "Return a copy of the metadata registry.");
static PyObject* _Nullable copyMetadataRegistry(PyObject* self
                                                __attribute__((__unused__)))
{
    return PyObjC_copyMetadataRegistry();
}

PyDoc_STRVAR(registerMetaData_doc,
             "registerMetaDataForSelector(classObject, selector, metadata)\n" CLINIC_SEP
             "\n"
             "Registers a metadata dictionary for method *selector* in *class*");
static PyObject* _Nullable registerMetaData(PyObject* self __attribute__((__unused__)),
                                            PyObject* _Nullable args,
                                            PyObject* _Nullable kwds)
{
    static char* keywords[] = {"class_", "selector", "metadata", NULL};

    PyObject* class_name;
    PyObject* selector;
    PyObject* metadata;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "SSO", keywords, &class_name, &selector,
                                     &metadata)) {
        return NULL;
    }
    PyObjC_Assert(PyBytes_Check(class_name), NULL);
    PyObjC_Assert(PyBytes_Check(selector), NULL);

    if (PyObjC_registerMetaData(class_name, selector, metadata) < 0) {
        return NULL;

    } else {
        PyObjC_MappingCount++;
        Py_INCREF(Py_None);
        return Py_None;
    }
}

PyDoc_STRVAR(registerStructAlias_doc,
             "registerStructAlias(typestr, structType)\n" CLINIC_SEP "\n"
             "Registers 'typestr' as a type that should be mapped onto 'structType'\n"
             "'structType' must be created using 'createStructType' (or through \n"
             "a metadata file.");
static PyObject* _Nullable registerStructAlias(PyObject* self __attribute__((__unused__)),
                                               PyObject* _Nullable args,
                                               PyObject* _Nullable kwds)
{
    static char* keywords[] = {"typestr", "structType", NULL};
    char*        typestr;
    PyObject*    structType;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "yO", keywords, &typestr, &structType)) {
        return NULL;
    }

    if (PyObjC_RegisterStructAlias(typestr, structType) == -1) {
        return NULL;
    }

    Py_INCREF(structType);
    return structType;
}

PyDoc_STRVAR(createStructType_doc,
             "createStructType(name, typestr, fieldnames, doc, pack)\n" CLINIC_SEP "\n"
             "Return a wrapper type for structs of the given type. The wrapper will \n"
             "registered with PyObjC and will be used to wrap structs of the given "
             "type.\n"
             "The field names can be ``None`` iff the typestr contains field names.");
static PyObject* _Nullable createStructType(PyObject* self __attribute__((__unused__)),
                                            PyObject* _Nullable args,
                                            PyObject* _Nullable kwds)
{
    static char* keywords[] = {"name", "typestr", "fieldnames", "doc", "pack", NULL};
    char*        name;
    char*        typestr;
    PyObject*    pyfieldnames;
    char*        docstr = NULL;
    PyObject*    retval;
    char**       fieldnames = NULL;
    Py_ssize_t   i;
    Py_ssize_t   field_count;
    Py_ssize_t   pack = -1;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "syO|zn", keywords, &name, &typestr,
                                     &pyfieldnames, &docstr, &pack)) {
        return NULL;
    }

    name = PyObjCUtil_Strdup(name);
    if (name == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_NoMemory();
        return NULL;
        // LCOV_EXCL_STOP
    }
    typestr = PyObjCUtil_Strdup(typestr);
    if (typestr == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyMem_Free(name);
        PyErr_NoMemory();
        return NULL;
        // LCOV_EXCL_STOP
    }
    if (docstr) {
        docstr = PyObjCUtil_Strdup(docstr);
        if (docstr == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            PyMem_Free(name);
            PyMem_Free(typestr);
            PyErr_NoMemory();
            return NULL;
            // LCOV_EXCL_STOP
        }
    }

    if (pyfieldnames != Py_None) {
        pyfieldnames =
            PySequence_Fast(pyfieldnames, "fieldnames must be a sequence of strings");

        if (pyfieldnames == NULL)
            goto error_cleanup;

        fieldnames = PyMem_Malloc(sizeof(char*) * PySequence_Fast_GET_SIZE(pyfieldnames));
        if (fieldnames == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            PyErr_NoMemory();
            goto error_cleanup;
            // LCOV_EXCL_STOP
        }
        memset(fieldnames, 0, sizeof(char*) * PySequence_Fast_GET_SIZE(pyfieldnames));
        for (i = 0; i < PySequence_Fast_GET_SIZE(pyfieldnames); i++) {
            PyObject* v = PySequence_Fast_GET_ITEM(pyfieldnames, i);
            if (PyUnicode_Check(v)) {
                PyObject* bytes = PyUnicode_AsEncodedString(v, NULL, NULL);
                if (bytes == NULL) {
                    goto error_cleanup;
                }
                fieldnames[i] = PyObjCUtil_Strdup(PyBytes_AsString(bytes));
                Py_DECREF(bytes);

            } else {
                PyErr_SetString(PyExc_TypeError,
                                "fieldnames must be a sequence of strings");
                goto error_cleanup;
            }

            if (fieldnames[i] == NULL) {
                PyErr_NoMemory();
                goto error_cleanup;
            }
        }
        field_count = PySequence_Fast_GET_SIZE(pyfieldnames);

    } else {
        field_count = -1;
        fieldnames  = NULL;
    }

    retval = PyObjC_RegisterStructType(typestr, name, docstr, NULL, field_count,
                                       (const char**)fieldnames, pack);
    if (retval == NULL)
        goto error_cleanup;
    Py_DECREF(pyfieldnames);

    return retval;

error_cleanup:
    if (name)
        PyMem_Free(name);
    if (typestr)
        PyMem_Free(typestr);
    if (docstr)
        PyMem_Free(docstr);

    if (fieldnames) {
        for (i = 0; i < PySequence_Fast_GET_SIZE(pyfieldnames); i++) {
            if (fieldnames[i])
                PyMem_Free(fieldnames[i]);
        }
        PyMem_Free(fieldnames);
    }

    Py_XDECREF(pyfieldnames);

    return NULL;
}

PyDoc_STRVAR(PyObjCIvar_Info_doc,
             "listInstanceVariables(classOrInstance)\n" CLINIC_SEP "\n"
             "Return information about all instance variables of an object or class\n");
PyDoc_STRVAR(PyObjCIvar_Get_doc, "getInstanceVariable(object, name)\n" CLINIC_SEP "\n"
                                 "Return the value of an instance variable\n");
PyDoc_STRVAR(PyObjCIvar_Set_doc,
             "setInstanceVariable(object, name, value, "
             "updateRefCount=False)\n" CLINIC_SEP "\n"
             "Modify an instance variable. If the instance variable is an object \n"
             "reference you must include the ``updateRefCount`` argument, otherwise it "
             "\n"
             "is ignored. If ``updateRefCount`` is true the reference counts of the \n"
             "old and new values are updated, otherwise they are not.\n"
             "\n"
             "NOTE: updating instance variables is dangerous, instance variables are \n"
             "private in Objective-C and classes might not expected that those values \n"
             "are changed by other code.");

PyDoc_STRVAR(registerCFSignature_doc,
             "registerCFSignature(name, encoding, typeId, "
             "tollfreeName=None)\n" CLINIC_SEP "\n"
             "Register a CoreFoundation based type with the bridge. If \n"
             "tollFreeName is supplied the type is tollfree bridged to that class.");
static PyObject* _Nullable registerCFSignature(PyObject* self __attribute__((__unused__)),
                                               PyObject* _Nullable args,
                                               PyObject* _Nullable kwds)
{
    static char* keywords[] = {"name", "encoding", "typeId", "tollfreeName", NULL};
    char*        name;
    char*        encoding;
    PyObject*    pTypeId;
    CFTypeID     typeId;
    char*        tollfreeName = NULL;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "syO|s", keywords, &name, &encoding,
                                     &pTypeId, &tollfreeName)) {
        return NULL;
    }

    if (pTypeId == Py_None) {
        if (tollfreeName == NULL) {
            PyErr_SetString(PyExc_ValueError, "Must specify a typeid when not toll-free");
            return NULL;
        }
        typeId = (CFTypeID)-1;

    } else if (depythonify_c_value(@encode(CFTypeID), pTypeId, &typeId) == -1) {
        return NULL;

    } else {
        PyObject* v = PyLong_FromLong(typeId);
        if (v == NULL) { // LCOV_BR_EXCL_LINE
            return NULL; // LCOV_EXCL_LINE
        }

        int r = PyDict_SetItemString(PyObjC_TypeStr2CFTypeID, encoding, v);
        Py_DECREF(v);
        if (r == -1) {   // LCOV_BR_EXCL_LINE
            return NULL; // LCOV_EXCL_LINE
        }
    }

    if (tollfreeName) {
        Class cls = objc_lookUpClass(tollfreeName);

        if (cls == nil) {
            PyErr_SetString(PyObjCExc_NoSuchClassError, tollfreeName);
            return NULL;
        }

        if (PyObjCPointerWrapper_RegisterID(name, encoding) == -1) {
            return NULL;
        }

        /* Don't have to do anything with the cfTypeId: because
         * the type is toll-free bridged automatic conversion will
         * do the right thing.
         */

        return PyObjCClass_New(cls);
    } else {
        return PyObjCCFType_New(name, encoding, typeId);
    }
}

PyDoc_STRVAR(_updatingMetadata_doc, "_updatingMetadata(flag)\n" CLINIC_SEP "\n"
                                    "PRIVATE FUNCTION");
static PyObject* _Nullable _updatingMetadata(PyObject* self __attribute__((__unused__)),
                                             PyObject* _Nullable args,
                                             PyObject* _Nullable kwds)
{
    static char* keywords[] = {"flag", NULL};
    PyObject*    flag;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "O", keywords, &flag)) {
        return NULL;
    }

    if (PyObject_IsTrue(flag)) {
        PyObjC_UpdatingMetaData = YES;

    } else {
        PyObjC_MappingCount++;
        PyObjC_UpdatingMetaData = NO;
    }

    Py_INCREF(Py_None);
    return Py_None;
}

/* Support for locking */
static PyObject* _Nullable PyObjC_objc_sync_enter(PyObject* self
                                                  __attribute__((__unused__)),
                                                  PyObject* _Nullable args)
{
    NSObject* object;
    int       rv;

    if (!PyArg_ParseTuple(args, "O&", PyObjCObject_Convert, &object)) {
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        rv = objc_sync_enter(object);

    Py_END_ALLOW_THREADS

    if (rv == OBJC_SYNC_SUCCESS) {
        Py_INCREF(Py_None);
        return Py_None;
    }

    PyErr_Format(PyObjCExc_LockError, "objc_sync_enter failed: %d", rv);
    return NULL;
}

static PyObject* _Nullable PyObjC_objc_sync_exit(PyObject* self
                                                 __attribute__((__unused__)),
                                                 PyObject* _Nullable args)
{
    NSObject* object;
    int       rv;

    if (!PyArg_ParseTuple(args, "O&", PyObjCObject_Convert, &object)) {
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        rv = objc_sync_exit(object);
    Py_END_ALLOW_THREADS
    if (rv == OBJC_SYNC_SUCCESS) {
        Py_INCREF(Py_None);
        return Py_None;
    }

    PyErr_Format(PyObjCExc_LockError, "objc_sync_exit failed: %d", rv);
    return NULL;
}

PyDoc_STRVAR(_makeClosure_doc,
             "_makeClosure(callable, closureFor, argIndex=0)\n" CLINIC_SEP "\n"
             "Returns a closure object that can be used to call the function from\n"
             "C. This object has no usable interface from Python.\n");

static void
_callback_cleanup(PyObject* closure)
{
    PyObjCFFI_FreeIMP((IMP)PyCapsule_GetPointer(closure, "objc.__imp__"));
}

static PyObject* _Nullable _makeClosure(PyObject* self __attribute__((__unused__)),
                                        PyObject* _Nullable args,
                                        PyObject* _Nullable kwds)
{
    static char*           keywords[] = {"callable", "closureFor", "argIndex", NULL};
    PyObject*              callable;
    PyObject*              closureFor;
    PyObjCMethodSignature* methinfo;
    Py_ssize_t             argIndex = 0;
    Py_ssize_t             i;

    argIndex = -1;
    if (!PyArg_ParseTupleAndKeywords(args, kwds, "OO|n", keywords, &callable, &closureFor,
                                     &argIndex)) {
        return NULL;
    }

    if (!PyCallable_Check(callable)) {
        PyErr_SetString(PyExc_TypeError, "Callable isn't callable");
        return NULL;
    }

    if (PyObjCFunction_Check(closureFor)) {
        methinfo = (PyObjCMethodSignature*)PyObjCFunc_GetMethodSignature(closureFor);
        if (methinfo == NULL) {
            return NULL;
        }

    } else if (PyObjCSelector_Check(closureFor)) {
        methinfo = PyObjCSelector_GetMetadata(closureFor);
        if (methinfo == NULL) {
            PyObjC_Assert(PyErr_Occurred(), NULL);
            return NULL;
        }

    } else {
        PyErr_Format(PyExc_TypeError,
                     "Don't know how to create closure for instance of %s",
                     Py_TYPE(closureFor)->tp_name);
        return NULL;
    }

    if (argIndex == -1) {
        for (i = 0; i < Py_SIZE(methinfo); i++) {
            if (methinfo->argtype[i]->callable != NULL) {
                argIndex = i;
                break;
            }
        }

        if (argIndex == -1) {
            PyErr_SetString(PyExc_ValueError,
                            "No callback argument in the specified object");
            return NULL;
        }

    } else {
        if (argIndex < 0 || argIndex >= Py_SIZE(methinfo)) {
            PyErr_SetString(PyExc_IndexError, "No such argument");
            return NULL;
        }

        if (methinfo->argtype[argIndex]->callable == NULL) {
            PyErr_Format(PyExc_ValueError,
                         "Argument %" PY_FORMAT_SIZE_T "d is not callable", argIndex);
            return NULL;
        }
    }

    PyObjC_callback_function result;

    result =
        PyObjCFFI_MakeFunctionClosure(methinfo->argtype[argIndex]->callable, callable);
    if (result == NULL) {
        return NULL;
    }

    PyObject* retval = PyCapsule_New((void*)result, "objc.__imp__", _callback_cleanup);
    if (retval == NULL) {
        PyObjCFFI_FreeIMP((IMP)result);
        return NULL;
    }

    return Py_BuildValue(
        "NN", retval,
        PyObjCMethodSignature_AsDict(methinfo->argtype[argIndex]->callable));
}

PyDoc_STRVAR(_closurePointer_doc, "_closurePointer(closure)\n" CLINIC_SEP "\n"
                                  "Returns an integer that corresponds to the "
                                  "numeric value of the C pointer\n"
                                  "for the closure.");
static PyObject* _Nullable _closurePointer(PyObject* self __attribute__((__unused__)),
                                           PyObject* _Nullable args,
                                           PyObject* _Nullable kwds)
{
    static char* keywords[] = {"closure", NULL};
    PyObject*    closure;
    void*        pointer;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "O", keywords, &closure)) {
        return NULL;
    }

    pointer = PyCapsule_GetPointer(closure, "objc.__imp__");
    if (pointer == NULL && PyErr_Occurred()) {
        return NULL;
    }
    return PyLong_FromVoidPtr(pointer);
}

static PyObject* _Nullable mod_propertiesForClass(PyObject* mod
                                                  __attribute__((__unused__)),
                                                  PyObject* object)
{
    return PyObjCClass_ListProperties(object);
}

PyDoc_STRVAR(PyObjC_setAssociatedObject_doc,
             "setAssociatedObject(object, key, value, "
             "policy=objc.OBJC_ASSOCIATION_RETAIN)\n" CLINIC_SEP "\n"
             "Set the value for an object association. Use 'None' as the\n"
             "value to clear an association.");
static PyObject* _Nullable PyObjC_setAssociatedObject(PyObject* self
                                                      __attribute__((__unused__)),
                                                      PyObject* _Nullable args,
                                                      PyObject* _Nullable kwds)
{
    static char* keywords[] = {"object", "key", "value", "policy", NULL};
    id           object;
    PyObject*    key;
    id           value;
    long         policy = OBJC_ASSOCIATION_RETAIN;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "O&OO&|l", keywords,
                                     PyObjCObject_Convert, &object, &key,
                                     PyObjCObject_Convert, &value, &policy)) {

        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            objc_setAssociatedObject(object, (void*)key, value, policy);

        } @catch (NSObject* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred())
        return NULL;

    Py_INCREF(Py_None);
    return Py_None;
}

PyDoc_STRVAR(PyObjC_getAssociatedObject_doc,
             "getAssociatedObject(object, key)\n" CLINIC_SEP "\n"
             "Get the value for an object association. Returns None \n"
             "when they association doesn't exist.");
static PyObject* _Nullable PyObjC_getAssociatedObject(PyObject* self
                                                      __attribute__((__unused__)),
                                                      PyObject* _Nullable args,
                                                      PyObject* _Nullable kwds)
{
    static char* keywords[] = {"object", "key", NULL};
    id           object;
    PyObject*    key;
    id           value;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "O&O", keywords, PyObjCObject_Convert,
                                     &object, &key)) {

        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            value = objc_getAssociatedObject(object, (void*)key);

        } @catch (NSObject* localException) {
            value = nil;
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred())
        return NULL;

    return id_to_python(value);
}

PyDoc_STRVAR(PyObjC_removeAssociatedObjects_doc,
             "removeAssociatedObjects(object)\n" CLINIC_SEP "\n"
             "Remove all associations from an object. This should in general not be used "
             "because\n"
             "it clear all references, including those made from unrelated code.\n");

static PyObject* _Nullable PyObjC_removeAssociatedObjects(PyObject* self
                                                          __attribute__((__unused__)),
                                                          PyObject* _Nullable args,
                                                          PyObject* _Nullable kwds)
{
    static char* keywords[] = {"object", NULL};
    id           object;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "O&", keywords, PyObjCObject_Convert,
                                     &object)) {

        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            objc_removeAssociatedObjects(object);

        } @catch (NSObject* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred())
        return NULL;

    Py_INCREF(Py_None);
    return Py_None;
}

static PyObject* _Nullable PyObjC_LoadConstant(PyObject* self __attribute__((__unused__)),
                                               PyObject* _Nullable args,
                                               PyObject* _Nullable kwds)
{
    static char* keywords[] = {"name", "type", "magic", NULL};
    char*        name;
    char*        type;
    int          magic;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "ssi", keywords, &name, &type, &magic)) {

        return NULL;
    }

    void* buf = dlsym(RTLD_DEFAULT, name);
    if (buf == NULL) {
        PyErr_SetString(PyExc_AttributeError, name);
        return NULL;
    }

    PyObject* v;

    if (magic) {
        if (magic == 2) {
            v = PyObjCCF_NewSpecialFromTypeEncoding(type, *(void**)buf);
        } else {
            v = PyObjCCF_NewSpecialFromTypeEncoding(type, buf);
        }
    } else {
        if (*type == _C_CHARPTR) {
            v = pythonify_c_value(type, &buf);
        } else {
            v = pythonify_c_value(type, buf);
        }
    }

    return v;
}

/* XXX: Move to utility file */
PyObject* _Nullable PyObjC_callable_docstr_get(PyObject* callable, void* _Nullable closure
                                               __attribute__((__unused__)))

{
    if (PyObjC_CallableDocFunction == NULL || PyObjC_CallableDocFunction == Py_None) {
        Py_INCREF(Py_None);
        return Py_None;
    }
    PyObject* args[2] = {NULL, callable};
    return PyObject_Vectorcall(PyObjC_CallableDocFunction, args + 1,
                               1 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
}

/* XXX: Move to utility file */
PyObject* _Nullable PyObjC_callable_signature_get(PyObject* callable,
                                                  void* _Nullable closure
                                                  __attribute__((__unused__)))

{
    if (PyObjC_CallableSignatureFunction == NULL
        || PyObjC_CallableSignatureFunction == Py_None) {
        Py_INCREF(Py_None);
        return Py_None;
    }
    PyObject* args[2] = {NULL, callable};
    return PyObject_Vectorcall(PyObjC_CallableSignatureFunction, args + 1,
                               1 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
}

static PyObject* _Nullable name_for_signature(PyObject* mod __attribute__((__unused__)),
                                              PyObject* signature)
{
    char* typestr;
    if (!PyBytes_Check(signature)) {
        PyErr_Format(PyExc_TypeError,
                     "type encoding must be a bytes string, not a '%s' object",
                     Py_TYPE(signature)->tp_name);
        return NULL;
    }
    typestr = PyBytes_AS_STRING(signature);
    if (typestr[0] == _C_STRUCT_B) {
        PyTypeObject* type = (PyTypeObject*)PyObjC_FindRegisteredStruct(
            typestr, PyBytes_GET_SIZE(signature));
        if (type == NULL) {
            if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
                return NULL;        // LCOV_EXCL_LINE
            } else {
                Py_INCREF(Py_None);
                return Py_None;
            }
        } else {
            return PyUnicode_FromString(type->tp_name);
        }
    }
    if (typestr[0] == _C_PTR) {
        const char* name = PyObjCPointerWrapper_Describe(typestr);
        if (name != NULL) {
            return PyUnicode_FromString(name);
        }
    }
    Py_INCREF(Py_None);
    return Py_None;
}

static PyObject* _Nullable block_signature(PyObject* mod __attribute__((__unused__)),
                                           PyObject* block)
{
    if (!PyObjCObject_Check(block) || !PyObjCObject_IsBlock(block)) {
        PyErr_SetString(PyExc_ValueError, "Not a block");
        return NULL;
    }

    const char* sig = PyObjCBlock_GetSignature(PyObjCObject_GetObject(block));
    if (sig == NULL) {
        Py_INCREF(Py_None);
        return Py_None;
    }

    return PyBytes_FromString(sig);
}

static PyObject* _Nullable force_rescan(PyObject* mod __attribute__((__unused__)),
                                        PyObject* _Nullable args,
                                        PyObject* _Nullable kwds)
{
    static char* keywords[] = {"name", NULL};
    const char*  class_name;
    PyObject*    py_cls;
    Class        cls;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "s", keywords, &class_name)) {
        return NULL;
    }

    cls = objc_lookUpClass(class_name);
    if (cls == Nil)
        goto done;

    py_cls = objc_class_locate(cls);
    if (py_cls == NULL)
        goto done;

    if (PyObjCClass_CheckMethodList(py_cls, NO) < 0) {
        return NULL;
    }

done:
    Py_INCREF(Py_None);
    return Py_None;
}

#if PyObjC_BUILD_RELEASE >= 1100
static PyObject* _Nullable mod_dyld_shared_cache_contains_path(
    PyObject* _Nullable mod __attribute__((__unused__)), PyObject* object)
{
    if (!PyUnicode_Check(object)) {
        PyErr_SetString(PyExc_TypeError, "Expecting a string");
        return NULL;
    }

    /* This uses an availability check for 10.16 just in case
     * we're loaded in a Python that was compiled with an old SDK.
     */
    if (@available(macOS 10.16, *)) {
        const char* path = PyUnicode_AsUTF8(object);
        if (path == NULL) {
            return NULL;
        }

        int result = _dyld_shared_cache_contains_path(path);
        return PyBool_FromLong(result);
    } else {
        Py_INCREF(Py_False);
        return Py_False;
    }
}

#else

/* Variant to be used when buildin on macOS 10.15 or earlier:
 * use dlsym(3) APIs to look for the function.
 */

static PyObject* _Nullable mod_dyld_shared_cache_contains_path(
    PyObject* _Nullable mod __attribute__((__unused__)), PyObject* object)
{
    static bool (*contains_func)(const char*) = NULL;
    static bool resolved_func                 = 0;

    if (!resolved_func) {
        contains_func = dlsym(RTLD_DEFAULT, "_dyld_shared_cache_contains_path");
        resolved_func = 1;
    }

    if (!PyUnicode_Check(object)) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_SetString(PyExc_TypeError, "Expecting a string");
        return NULL;
        // LCOV_EXCL_STOP
    }

    /* Always fetch the C string to get consistent
     * behaviour in error cases, even on systems
     * without this system API.
     */
    const char* path = PyUnicode_AsUTF8(object);
    if (path == NULL) {
        return NULL;
    }

    if (contains_func) {
        int result = contains_func(path);
        return PyBool_FromLong(result);
    } else {

        Py_INCREF(Py_False);
        return Py_False;
    }
}

#endif

static PyObject* _Nullable mod_registerVectorType(PyObject* _Nullable mod
                                                  __attribute__((__unused__)),
                                                  PyObject* object)
{
    PyObject* typestr = PyObject_GetAttrString(object, "__typestr__");
    if (typestr == NULL) {
        return NULL;
    }
    if (!PyBytes_CheckExact(typestr)) {
        PyErr_SetString(PyExc_TypeError, "__typstr__ must be bytes");
        Py_DECREF(typestr);
        return NULL;
    }
    int r = PyObjCRT_RegisterVectorType(PyBytes_AsString(typestr), object);
    Py_DECREF(typestr);
    if (r == -1) {
        PyObjC_Assert(PyErr_Occurred(), NULL);
        return NULL;
    } else {
        Py_INCREF(Py_None);
        return Py_None;
    }
}

static PyObject* _Nullable mod_registeredMetadataForSelector(PyObject* _Nullable mod
                                                             __attribute__((__unused__)),
                                                             PyObject* args)
{
    PyObject* class;
    char* pysel;
    SEL   sel;

    if (!PyArg_ParseTuple(args, "Oy", &class, &pysel)) {
        return NULL;
    }
    if (!PyObjCClass_Check(class)) {
        PyErr_SetString(PyExc_TypeError, "Expecting a class");
        return NULL;
    }

    sel = sel_registerName(pysel);

    Class cls = PyObjCClass_GetClass(class);
    if (cls == Nil) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyObjC_Assert(PyErr_Occurred(), NULL);
        return NULL;
        // LCOV_EXCL_STOP
    }

    PyObjCMethodSignature* sig = PyObjCMethodSignature_GetRegistered(cls, sel);
    if (sig == NULL) {
        PyErr_Clear();
        Py_INCREF(Py_None);
        return Py_None;
    }
    return PyObjCMethodSignature_AsDict(sig);
}

static PyMethodDef mod_methods[] = {
    {
        .ml_name  = "propertiesForClass",
        .ml_meth  = (PyCFunction)mod_propertiesForClass,
        .ml_flags = METH_O,
        .ml_doc   = "propertiesForClass(classObject)\n" CLINIC_SEP "\n"
                    "Return information about properties from the runtime",
    },
    {.ml_name  = "splitSignature",
     .ml_meth  = (PyCFunction)objc_splitSignature,
     .ml_flags = METH_VARARGS | METH_KEYWORDS,
     .ml_doc   = objc_splitSignature_doc},
    {
        .ml_name  = "splitStructSignature",
        .ml_meth  = (PyCFunction)objc_splitStructSignature,
        .ml_flags = METH_VARARGS | METH_KEYWORDS,
        .ml_doc   = objc_splitStructSignature_doc,
    },
    {
        .ml_name  = "_sizeOfType",
        .ml_meth  = m_sizeoftype,
        .ml_flags = METH_O,
        .ml_doc   = "_sizeOfType(typestr, /)\n" CLINIC_SEP "\n"
                    "Return the size of the type described by 'typestr'",
    },
    {.ml_name  = "macos_available",
     .ml_meth  = (PyCFunction)macos_available,
     .ml_flags = METH_VARARGS | METH_KEYWORDS,
     .ml_doc   = macos_available_doc},
    {.ml_name  = "lookUpClass",
     .ml_meth  = (PyCFunction)lookUpClass,
     .ml_flags = METH_VARARGS | METH_KEYWORDS,
     .ml_doc   = lookUpClass_doc},
    {.ml_name  = "classAddMethods",
     .ml_meth  = (PyCFunction)classAddMethods,
     .ml_flags = METH_VARARGS | METH_KEYWORDS,
     .ml_doc   = classAddMethods_doc},
    {.ml_name  = "currentBundle",
     .ml_meth  = (PyCFunction)currentBundle,
     .ml_flags = METH_NOARGS,
     .ml_doc   = currentBundle_doc},
    {.ml_name  = "getClassList",
     .ml_meth  = (PyCFunction)getClassList,
     .ml_flags = METH_VARARGS,
     .ml_doc   = getClassList_doc},
    {.ml_name  = "recycleAutoreleasePool",
     .ml_meth  = (PyCFunction)recycle_autorelease_pool,
     .ml_flags = METH_NOARGS,
     .ml_doc   = recycle_autorelease_pool_doc},
    {.ml_name  = "removeAutoreleasePool",
     .ml_meth  = (PyCFunction)remove_autorelease_pool,
     .ml_flags = METH_NOARGS,
     .ml_doc   = remove_autorelease_pool_doc},
    {.ml_name  = "_haveAutoreleasePool",
     .ml_meth  = (PyCFunction)have_autorelease_pool,
     .ml_flags = METH_NOARGS,
     .ml_doc   = have_autorelease_pool_doc},
    {.ml_name  = "pyobjc_id",
     .ml_meth  = (PyCFunction)pyobjc_id,
     .ml_flags = METH_VARARGS | METH_KEYWORDS,
     .ml_doc   = pyobjc_id_doc},
    {.ml_name  = "repythonify",
     .ml_meth  = (PyCFunction)repythonify,
     .ml_flags = METH_VARARGS | METH_KEYWORDS,
     .ml_doc   = repythonify_doc},
    {.ml_name  = "loadBundle",
     .ml_meth  = (PyCFunction)loadBundle,
     .ml_flags = METH_VARARGS | METH_KEYWORDS,
     .ml_doc   = loadBundle_doc},
    {.ml_name  = "protocolsForClass",
     .ml_meth  = (PyCFunction)protocolsForClass,
     .ml_flags = METH_VARARGS | METH_KEYWORDS,
     .ml_doc   = protocolsForClass_doc},
    {.ml_name  = "protocolsForProcess",
     .ml_meth  = (PyCFunction)protocolsForProcess,
     .ml_flags = METH_NOARGS,
     .ml_doc   = protocolsForProcess_doc},
    {.ml_name  = "_protocolNamed",
     .ml_meth  = (PyCFunction)protocolNamed,
     .ml_flags = METH_VARARGS | METH_KEYWORDS,
     .ml_doc   = protocolNamed_doc},
    {.ml_name  = "registerCFSignature",
     .ml_meth  = (PyCFunction)registerCFSignature,
     .ml_flags = METH_VARARGS | METH_KEYWORDS,
     .ml_doc   = registerCFSignature_doc},
    {.ml_name  = "loadBundleVariables",
     .ml_meth  = (PyCFunction)PyObjC_loadBundleVariables,
     .ml_flags = METH_VARARGS | METH_KEYWORDS,
     .ml_doc   = PyObjC_loadBundleVariables_doc},
    {.ml_name  = "loadSpecialVar",
     .ml_meth  = (PyCFunction)PyObjC_loadSpecialVar,
     .ml_flags = METH_VARARGS | METH_KEYWORDS,
     .ml_doc   = PyObjC_loadSpecialVar_doc},
    {.ml_name  = "loadBundleFunctions",
     .ml_meth  = (PyCFunction)PyObjC_loadBundleFunctions,
     .ml_flags = METH_VARARGS | METH_KEYWORDS,
     .ml_doc   = PyObjC_loadBundleFunctions_doc},
    {.ml_name  = "loadFunctionList",
     .ml_meth  = (PyCFunction)PyObjC_loadFunctionList,
     .ml_flags = METH_VARARGS | METH_KEYWORDS,
     .ml_doc   = PyObjC_loadFunctionList_doc},
    {.ml_name  = "listInstanceVariables",
     .ml_meth  = (PyCFunction)PyObjCIvar_Info,
     .ml_flags = METH_O,
     .ml_doc   = PyObjCIvar_Info_doc},
    {.ml_name  = "getInstanceVariable",
     .ml_meth  = (PyCFunction)PyObjCIvar_Get,
     .ml_flags = METH_VARARGS | METH_KEYWORDS,
     .ml_doc   = PyObjCIvar_Get_doc},
    {.ml_name  = "setInstanceVariable",
     .ml_meth  = (PyCFunction)PyObjCIvar_Set,
     .ml_flags = METH_VARARGS | METH_KEYWORDS,
     .ml_doc   = PyObjCIvar_Set_doc},
    {.ml_name  = "createOpaquePointerType",
     .ml_meth  = (PyCFunction)createOpaquePointerType,
     .ml_flags = METH_VARARGS | METH_KEYWORDS,
     .ml_doc   = createOpaquePointerType_doc},
    {.ml_name  = "createStructType",
     .ml_meth  = (PyCFunction)createStructType,
     .ml_flags = METH_VARARGS | METH_KEYWORDS,
     .ml_doc   = createStructType_doc},
    {.ml_name  = "registerStructAlias",
     .ml_meth  = (PyCFunction)registerStructAlias,
     .ml_flags = METH_VARARGS | METH_KEYWORDS,
     .ml_doc   = registerStructAlias_doc},
    {.ml_name  = "registerMetaDataForSelector",
     .ml_meth  = (PyCFunction)registerMetaData,
     .ml_flags = METH_VARARGS | METH_KEYWORDS,
     .ml_doc   = registerMetaData_doc},
    {.ml_name  = "_copyMetadataRegistry",
     .ml_meth  = (PyCFunction)copyMetadataRegistry,
     .ml_flags = METH_NOARGS,
     .ml_doc   = copyMetadataRegistry_doc},
    {.ml_name  = "_idSignatures",
     .ml_meth  = (PyCFunction)idSignatures,
     .ml_flags = METH_NOARGS,
     .ml_doc   = idSignatures_doc},
    {.ml_name  = "_updatingMetadata",
     .ml_meth  = (PyCFunction)_updatingMetadata,
     .ml_flags = METH_VARARGS | METH_KEYWORDS,
     .ml_doc   = _updatingMetadata_doc},
    {.ml_name  = "_makeClosure",
     .ml_meth  = (PyCFunction)_makeClosure,
     .ml_flags = METH_VARARGS | METH_KEYWORDS,
     .ml_doc   = _makeClosure_doc},
    {.ml_name  = "_closurePointer",
     .ml_meth  = (PyCFunction)_closurePointer,
     .ml_flags = METH_VARARGS | METH_KEYWORDS,
     .ml_doc   = _closurePointer_doc},
    {.ml_name  = "_objc_sync_enter",
     .ml_meth  = (PyCFunction)PyObjC_objc_sync_enter,
     .ml_flags = METH_VARARGS,
     .ml_doc   = "_objc_sync_enter(object)\n" CLINIC_SEP "\nacquire mutex for an object"},
    {.ml_name  = "_objc_sync_exit",
     .ml_meth  = (PyCFunction)PyObjC_objc_sync_exit,
     .ml_flags = METH_VARARGS,
     .ml_doc   = "_objc_sync_exit(object)\n" CLINIC_SEP "\nrelease mutex for an object"},
    {.ml_name  = "_block_call",
     .ml_meth  = (PyCFunction)PyObjCBlock_Call,
     .ml_flags = METH_VARARGS,
     "_block_call(block, signature, args, kwds)\n" CLINIC_SEP
     "\nCall an Objective-C block"},
    {.ml_name  = "_block_signature",
     .ml_meth  = (PyCFunction)block_signature,
     .ml_flags = METH_O,
     "_block_signature(block)\n" CLINIC_SEP
     "\nreturn signature string for a block, or None"},
    {.ml_name  = "setAssociatedObject",
     .ml_meth  = (PyCFunction)PyObjC_setAssociatedObject,
     .ml_flags = METH_VARARGS | METH_KEYWORDS,
     .ml_doc   = PyObjC_setAssociatedObject_doc},
    {.ml_name  = "getAssociatedObject",
     .ml_meth  = (PyCFunction)PyObjC_getAssociatedObject,
     .ml_flags = METH_VARARGS | METH_KEYWORDS,
     .ml_doc   = PyObjC_getAssociatedObject_doc},
    {.ml_name  = "removeAssociatedObjects",
     .ml_meth  = (PyCFunction)PyObjC_removeAssociatedObjects,
     .ml_flags = METH_VARARGS | METH_KEYWORDS,
     .ml_doc   = PyObjC_removeAssociatedObjects_doc},
    {.ml_name  = "_loadConstant",
     .ml_meth  = (PyCFunction)PyObjC_LoadConstant,
     .ml_flags = METH_VARARGS | METH_KEYWORDS,
     .ml_doc   = "_loadConstant(name, type, magic)\n" CLINIC_SEP
               "\nLoad a single C constant and return its value"},
    {.ml_name  = "_nameForSignature",
     .ml_meth  = (PyCFunction)name_for_signature,
     .ml_flags = METH_O,
     .ml_doc   = "_nameForSignature(typestr)\n" CLINIC_SEP
               "\nReturn a pretty name for a PyObjC type string"},
    {
        .ml_name  = "_rescanClass",
        .ml_meth  = (PyCFunction)force_rescan,
        .ml_flags = METH_VARARGS | METH_KEYWORDS,
        .ml_doc   = "_rescanClass(classObject)\n" CLINIC_SEP
                  "\nForce a rescan of the method table of a class",
    },
    {
        .ml_name  = "_rescanClass",
        .ml_meth  = (PyCFunction)force_rescan,
        .ml_flags = METH_VARARGS | METH_KEYWORDS,
        .ml_doc   = "_rescanClass(classObject)\n" CLINIC_SEP
                  "\nForce a rescan of the method table of a class",
    },
    {
        .ml_name  = "_dyld_shared_cache_contains_path",
        .ml_meth  = (PyCFunction)mod_dyld_shared_cache_contains_path,
        .ml_flags = METH_O,
        .ml_doc   = "_dyld_shared_cache_contains_path(path)\n" CLINIC_SEP
                  "\nForce a rescan of the method table of a class",
    },
    {
        .ml_name  = "_registerVectorType",
        .ml_meth  = (PyCFunction)mod_registerVectorType,
        .ml_flags = METH_O,
        .ml_doc   = "_registerVectorType(type)\n" CLINIC_SEP
                  "\nRegister SIMD type with the bridge.",
    },
    {
        .ml_name  = "_registeredMetadataForSelector",
        .ml_meth  = (PyCFunction)mod_registeredMetadataForSelector,
        .ml_flags = METH_VARARGS,
        .ml_doc   = "_registeredMetadataForSelector(cls, selname)\n" CLINIC_SEP
                  "\nLook up registered metadata info for a selector.",
    },
    {
        .ml_name = NULL /* SENTINEL */
    }};

struct objc_typestr_values {
    char* name;
    char  value;
} objc_typestr_values[] = {{"_C_ID", _C_ID},
                           {"_C_CLASS", _C_CLASS},
                           {"_C_SEL", _C_SEL},
                           {"_C_CHR", _C_CHR},
                           {"_C_UCHR", _C_UCHR},
                           {"_C_SHT", _C_SHT},
                           {"_C_USHT", _C_USHT},
#ifdef _C_BOOL
                           {"_C_BOOL", _C_BOOL},
#endif
                           {"_C_INT", _C_INT},
                           {"_C_UINT", _C_UINT},
                           {"_C_LNG", _C_LNG},
                           {"_C_ULNG", _C_ULNG},
                           {"_C_LNG_LNG", _C_LNG_LNG},
                           {"_C_ULNG_LNG", _C_ULNG_LNG},
                           {"_C_FLT", _C_FLT},
                           {"_C_DBL", _C_DBL},
                           {"_C_BFLD", _C_BFLD},
                           {"_C_VOID", _C_VOID},
                           {"_C_UNDEF", _C_UNDEF},
                           {"_C_PTR", _C_PTR},
                           {"_C_CHARPTR", _C_CHARPTR},
                           {"_C_ARY_B", _C_ARY_B},
                           {"_C_ARY_E", _C_ARY_E},
                           {"_C_UNION_B", _C_UNION_B},
                           {"_C_UNION_E", _C_UNION_E},
                           {"_C_STRUCT_B", _C_STRUCT_B},
                           {"_C_STRUCT_E", _C_STRUCT_E},
                           {"_C_VECTOR_B", _C_VECTOR_B},
                           {"_C_VECTOR_E", _C_VECTOR_E},
                           {"_C_CONST", _C_CONST},
                           {"_C_COMPLEX", _C_COMPLEX},
                           {"_C_ATOMIC", _C_ATOMIC},
                           {"_C_IN", _C_IN},
                           {"_C_INOUT", _C_INOUT},
                           {"_C_OUT", _C_OUT},
                           {"_C_BYCOPY", _C_BYCOPY},
                           {"_C_BYREF", _C_BYREF},
                           {"_C_ONEWAY", _C_ONEWAY},

                           /* Compatibility: */
                           {"_C_LNGLNG", _C_LNG_LNG},
                           {"_C_ULNGLNG", _C_ULNG_LNG},

                           /* PyObjC specific */
                           {"_C_NSBOOL", _C_NSBOOL},
                           {"_C_UNICHAR", _C_UNICHAR},
                           {"_C_CHAR_AS_TEXT", _C_CHAR_AS_TEXT},
                           {"_C_CHAR_AS_INT", _C_CHAR_AS_INT},

                           {NULL, 0}};

struct objc_typestr_long_values {
    char* name;
    char* value;
} objc_typestr_long_values[] = {{"_C_CFTYPEID", @encode(CFTypeID)},
                                {"_C_NSInteger", @encode(NSInteger)},
                                {"_C_NSUInteger", @encode(NSUInteger)},
                                {"_C_CFIndex", @encode(CFIndex)},
                                {"_C_CGFloat", @encode(CGFloat)},
                                {"_C_FSRef", @encode(FSRef)},
                                {"_C_NSRange", @encode(NSRange)},
                                {"_C_CFRange", @encode(CFRange)},
                                {"_C_PythonObject", @encode(PyObject*)},
                                {"_sockaddr_type", @encode(struct sockaddr)},
                                {NULL, 0}};

struct objc_int_values {
    char* name;
    long  value;
} objc_int_values[] = {
    // { "NAME", value },
    {"PyObjC_BUILD_RELEASE", PyObjC_BUILD_RELEASE},
    {"_NSNotFound", NSNotFound},
    {"OBJC_ASSOCIATION_ASSIGN", OBJC_ASSOCIATION_ASSIGN},
    {"OBJC_ASSOCIATION_RETAIN_NONATOMIC", OBJC_ASSOCIATION_RETAIN_NONATOMIC},
    {"OBJC_ASSOCIATION_COPY_NONATOMIC", OBJC_ASSOCIATION_COPY_NONATOMIC},
    {"OBJC_ASSOCIATION_RETAIN", OBJC_ASSOCIATION_RETAIN},
    {"OBJC_ASSOCIATION_COPY", OBJC_ASSOCIATION_COPY},
    {"_size_sockaddr_ip4", sizeof(struct sockaddr_in)},
    {"_size_sockaddr_ip6", sizeof(struct sockaddr_in6)},
    {"_size_sockaddr_un", sizeof(struct sockaddr_un)},
    {"_size_sockaddr", sizeof(struct sockaddr)},
    {NULL, 0}};

struct objc_float_values {
    char*  name;
    double value;
} objc_float_values[] = {{"_FLT_MIN", FLT_MIN}, {"_FLT_MAX", FLT_MAX}, {NULL, 0}};

struct objc_string_values {
    char* name;
    char* value;
} objc_string_values[] = {{"__version__", OBJC_VERSION},
                          {"platform", "MACOSX"},

#if defined(__x86_64__)
                          {"arch", "x86_64"},
#elif defined(__arm64__)
                          {"arch", "arm64"},
#else
#error "Unsupported CPU architecture"
#endif

                          {NULL, 0}};

typedef int (*setup_function)(PyObject*);

/* XXX: Consider generating this table with a helper script:
 * - Naming convention (e.g. all function names ending with _Setup)
 * - Encode dependencies somehow
 * - Script that extracts function names and dependencies,
 *   using topsort to generate this array.
 */
static setup_function _Nullable setup_functions[] = {
    PyObjC_InitProxyRegistry, /* Must be first */

    PyObjCUtil_Init,
    PyObjCPointerWrapper_Init,
    PyObjC_SetupOptions,
    PyObjC_setup_nsdecimal,
    PyObjCPointer_Setup,
    FILE_Setup,
    PyObjCFormalProtocol_Setup,
    PyObjCFunc_Setup,
    PyObjCVarList_Setup,
    PyObjCSuper_Setup,
    PyObjCMethodSignature_Setup,
    PyObjCUnicode_Setup,
    PyObjCInitNULL,
    PyObjCInstanceVariable_Setup,
    PyObjCMemView_Setup,
    PyObjCWeakRef_Setup,
    PyObjCMethodAccessor_Setup,
    PyObjCIMP_SetUp,
    PyObjC_init_ctests,
    PyObjCSelector_Setup,
    PyObjC_setup_nsdata,
    PyObjC_setup_nscoder,
    PyObjC_setup_nsobject,
    PyObjC_setup_simd,
    PyObjC_setup_nsinvocation,
    PyObjCCFType_Setup,
    PyObjCBlock_Setup,
    PyObjCFSRef_Setup,
    PyObjC_SockAddr_Setup,

    PyObjCAPI_Register, /* Must be last */
    NULL};

#define ADD_CONSTANT_TABLE(module, var_name, item_creator)                               \
    do {                                                                                 \
        __typeof__((var_name)[0])* cur = (var_name);                                     \
                                                                                         \
        for (; cur->name != NULL; cur++) {                                               \
            PyObject* t = item_creator(cur->value);                                      \
            if (t == NULL) { /* LCOV_BR_EXCL_LINE */                                     \
                return NULL; /* LCOV_EXCL_LINE */                                        \
            }                                                                            \
            if (PyModule_AddObject((module), cur->name, t)) { /* LCOV_BR_EXCL_LINE */    \
                Py_DECREF(t);                                 /* LCOV_EXCL_LINE */       \
                return NULL;                                  /* LCOV_EXCL_LINE */       \
            }                                                                            \
        }                                                                                \
    } while (0)

static PyObject*
bytes_from_char(char ch)
{
    return PyBytes_FromStringAndSize(&ch, 1);
}

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "_objc", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* _Nullable __attribute__((__visibility__("default"))) PyInit__objc(void)
{
    _Static_assert(sizeof(BOOL) == sizeof(bool), "BOOL and bool should have same size");
    PyObject* m;

    if (PyObjC_Initialized) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_SetString(PyExc_RuntimeError,
                        "Reload of objc._objc detected, this is not supported");
        return NULL;
        // LCOV_EXCL_STOP
    }

    calc_current_version();

    m = PyModule_Create(&mod_module);
    if (m == 0) {    // LCOV_BR_EXCL_LINE
        return NULL; // LCOV_EXCL_LINE // LCOV_EXCL_LINE
    }

    if (PyObjC_InitSuperCallRegistry() == -1) { // LCOV_BR_EXCL_LINE
        return NULL;                            // LCOV_EXCL_LINE
    }

    /* Create a temporary release pool for handling values autoreleased during
     * the setup function.
     */
    NSAutoreleasePool* initReleasePool = [[NSAutoreleasePool alloc] init];

    /* XXX: See earlier, unclear if this is still needed */
    [OC_NSBundleHack installBundleHack];

    PyObjCClass_DefaultModule = PyUnicode_FromString("objc");
    if (PyObjCClass_DefaultModule == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;                         // LCOV_EXCL_LINE
    }

    PyObjC_TypeStr2CFTypeID = PyDict_New();
    if (PyObjC_TypeStr2CFTypeID == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;                       // LCOV_EXCL_LINE
    }

    /* XXX: Move these to setup functions as well */
    if (PyType_Ready(&PyObjCMetaClass_Type) < 0) { // LCOV_BR_EXCL_LINE
        return NULL;                               // LCOV_EXCL_LINE
    }
    if (PyType_Ready(&PyObjCClass_Type) < 0) { // LCOV_BR_EXCL_LINE
        return NULL;                           // LCOV_EXCL_LINE
    }
    if (PyType_Ready((PyTypeObject*)&PyObjCObject_Type) < 0) { // LCOV_BR_EXCL_LINE
        return NULL;                                           // LCOV_EXCL_LINE
    }

    if (PyType_Ready(&StructBase_Type) < 0) { // LCOV_BR_EXCL_LINE
        return NULL;                          // LCOV_EXCL_LINE
    }

    for (setup_function* cur = setup_functions; *cur != NULL; cur++) {
        if ((*cur)(m) < 0) { // LCOV_BR_EXCL_LINE
            return NULL;     // LCOV_EXCL_LINE
        }
        if (PyErr_Occurred()) {
            return NULL;
        }
    }

    /* XXX: Move these to setup functions as well */
    if ( // LCOV_BR_EXCL_LINE
        PyModule_AddObject(m, "objc_meta_class", (PyObject*)&PyObjCMetaClass_Type) < 0) {
        return NULL; // LCOV_EXCL_LINE
    }
    Py_INCREF((PyObject*)&PyObjCMetaClass_Type);

    if (PyModule_AddObject( // LCOV_BR_EXCL_LINE
            m, "objc_class", (PyObject*)&PyObjCClass_Type)
        < 0) {
        return NULL; // LCOV_EXCL_LINE
    }
    Py_INCREF((PyObject*)&PyObjCClass_Type);

    if (PyModule_AddObject( // LCOV_BR_EXCL_LINE
            m, "objc_object", (PyObject*)&PyObjCObject_Type)
        < 0) {
        return NULL; // LCOV_EXCL_LINE
    }
    Py_INCREF((PyObject*)&PyObjCObject_Type);

    if (PyModule_AddObject( // LCOV_BR_EXCL_LINE
            m, "_structwrapper", (PyObject*)&StructBase_Type)
        < 0) {
        return NULL; // LCOV_EXCL_LINE
    }
    Py_INCREF((PyObject*)&StructBase_Type);

    ADD_CONSTANT_TABLE(m, objc_int_values, PyLong_FromLong);
    ADD_CONSTANT_TABLE(m, objc_float_values, PyFloat_FromDouble);
    ADD_CONSTANT_TABLE(m, objc_string_values, PyUnicode_FromString);
    ADD_CONSTANT_TABLE(m, objc_typestr_values, bytes_from_char);
    ADD_CONSTANT_TABLE(m, objc_typestr_long_values, PyBytes_FromString);

    /* XXX: Why is this needed? */
    if (![NSThread isMultiThreaded]) {
        [NSThread detachNewThreadSelector:@selector(targetForBecomingMultiThreaded:)
                                 toTarget:[OC_NSAutoreleasePoolCollector class]
                               withObject:nil];
    }

    [initReleasePool release];

    /* Allocate an auto-release pool for our own use, this avoids numerous
     * warnings during startup of a python script.
     */
    global_release_pool = nil;
    [OC_NSAutoreleasePoolCollector newAutoreleasePool];

    /*
     * Archives created with Python 2.x can contain instances of
     * OC_PythonString, use OC_PythonUnicode to decode.
     */
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"

    [NSUnarchiver decodeClassName:@"OC_PythonString" asClassName:@"OC_PythonUnicode"];

#pragma clang diagnostic pop

    PyObjC_Initialized = 1;
    return m;
}

NS_ASSUME_NONNULL_END
