/*
 * The module entry point for ``_objc``. This file contains ``init_objc``
 * and the implementation of a number of exported functions.
 */
#include "pyobjc.h"
#include "OC_NSBundleHack.h"
#include <objc/Protocol.h>
#include <objc/objc-sync.h>

#include <stddef.h>
#include <ctype.h>
#include <sys/socket.h>
#include <netinet/in.h>

#import <Foundation/NSAutoreleasePool.h>
#import <Foundation/NSBundle.h>
#import <Foundation/NSProcessInfo.h>
#import <Foundation/NSString.h>

#import <mach-o/dyld.h>
#import <mach-o/getsect.h>
#import <mach-o/loader.h>
#import <objc/Protocol.h>

#include <dlfcn.h>

static int PyObjC_Initialized = 0;

PyObject* PyObjCClass_DefaultModule = NULL;

PyObject* PyObjC_TypeStr2CFTypeID = NULL;

static NSAutoreleasePool* global_release_pool = nil;

@interface OC_NSAutoreleasePoolCollector: NSObject
  /*
   * This class is used to automaticly reset the
   * global pool when an outer autorelease pool is
   * recycled. This avoids problems when a python
   * plugin is loaded in an Objective-C program.
   */
{}
+(void)newAutoreleasePool;
+(void)targetForBecomingMultiThreaded:(id)sender;
@end

@implementation OC_NSAutoreleasePoolCollector
+(void)newAutoreleasePool
{
    self = [[self alloc] init];
    global_release_pool = [[NSAutoreleasePool alloc] init];
    (void)[self autorelease];
}

-(void)dealloc
{
    global_release_pool = nil;
    [super dealloc];
}

+(void)targetForBecomingMultiThreaded:(id)sender
{
    [sender self];
}

@end

PyDoc_STRVAR(pyobjc_id_doc,
  "pyobjc_id(obj)\n"
  CLINIC_SEP
  "\n"
  "Return the id of the underlying NSObject as an int."
);

static PyObject*
pyobjc_id(PyObject* self __attribute__((__unused__)), PyObject* args,
PyObject *kwds)
{
    static char* keywords[] = { "obj", NULL };
    PyObject *o;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "O", keywords, &o)) {
        return NULL;
    }

    if (!PyObjCObject_Check(o)) {
        PyErr_SetString(PyExc_TypeError, "not an Objective-C object");
        return NULL;
    }
    return PyLong_FromVoidPtr((void*)PyObjCObject_GetObject(o));
}


PyDoc_STRVAR(repythonify_doc,
  "repythonify(obj, type='@')\n"
  CLINIC_SEP
  "\n"
  "Put an object through the bridge by calling \n"
  "depythonify_c_value then pythonify_c_value.\n"
  "This is for internal use only."
);

static PyObject*
repythonify(PyObject* self __attribute__((__unused__)), PyObject* args,
PyObject *kwds)
{
    static char* keywords[] = { "obj", "type", NULL };
    const char *type = "@";
    PyObject *rval;
    void *datum;
    Py_ssize_t size;
    PyObject *o;

    if (!PyArg_ParseTupleAndKeywords(args, kwds,
                "O|"Py_ARG_BYTES,
        keywords, &o, &type)) {
        return NULL;
    }

    size = PyObjCRT_SizeOfType(type);
    if (size < 1) {
        PyErr_SetString(PyExc_ValueError, "Can not calculate size for type");
        return NULL;
    }

    datum = PyMem_Malloc(size);
    if (datum == NULL) {
        return PyErr_NoMemory();
    }

    if (depythonify_c_value(type, o, datum)) {
        PyMem_Free(datum);
        return NULL;
    }

    rval = pythonify_c_value(type, datum);
    PyMem_Free(datum);
    return rval;
}

#if PY_MAJOR_VERSION == 2

PyObject* PyObjCStrBridgeWarning = NULL;

#endif /* PY_VERSION_MAJOR == 2 */

PyDoc_STRVAR(lookUpClass_doc,
  "lookUpClass(class_name)\n"
  CLINIC_SEP
  "\n"
  "Search for the named classes in the Objective-C runtime and return it.\n"
  "Raises noclass_error when the class doesn't exist.");

static PyObject*
lookUpClass(PyObject* self __attribute__((__unused__)),
    PyObject* args, PyObject* kwds)
{
static char* keywords[] = { "class_name", NULL };
    char* class_name = NULL;
    Class objc_class;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "s",
            keywords, &class_name)) {
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
     "classAddMethods(targetClass, methodsArray)\n"
     CLINIC_SEP
     "\n"
     "Adds methods in methodsArray to class. The effect is similar to how \n"
     "categories work. If class already implements a method as defined in \n"
     "methodsArray, the original implementation will be replaced by the \n"
     "implementation from methodsArray.");

static PyObject*
classAddMethods(PyObject* self __attribute__((__unused__)),
    PyObject* args, PyObject* keywds)
{
    static char* kwlist[] = { "targetClass", "methodsArray", NULL };
    PyObject* classObject = NULL;
    PyObject* methodsArray = NULL;

    if (!PyArg_ParseTupleAndKeywords(args, keywds,
            "OO:classAddMethods", kwlist,
            &classObject, &methodsArray)) {
        return NULL;
    }

    if (!PyObjCClass_Check(classObject)) {
        PyErr_SetString(PyExc_TypeError, "base class is not an Objective-C class");
        return NULL;
    }

    methodsArray = PySequence_Fast(
            methodsArray, "methodsArray must be a sequence");
    if (methodsArray == NULL) return NULL;

    int r = PyObjCClass_AddMethods(classObject,
            PySequence_Fast_ITEMS(methodsArray),
            PySequence_Fast_GET_SIZE(methodsArray));
    Py_DECREF(methodsArray);

    if (r == -1) {
        return NULL;
    }

    Py_INCREF(Py_None);
    return Py_None;
}

PyDoc_STRVAR(remove_autorelease_pool_doc,
  "removeAutoreleasePool()\n"
  CLINIC_SEP
  "\n"
  "This removes the global NSAutoreleasePool. You should do this\n"
  "at the end of a plugin's initialization script.\n");

static PyObject*
remove_autorelease_pool(PyObject* self __attribute__((__unused__)),
    PyObject* args, PyObject* kwds)
{
    static char* keywords[] = { NULL };
    if (!PyArg_ParseTupleAndKeywords(args, kwds, "", keywords)) {
        return NULL;
    }

    PyObjC_DURING
        [global_release_pool release];
        global_release_pool = nil;

    PyObjC_HANDLER
        PyObjCErr_FromObjC(localException);
    PyObjC_ENDHANDLER

    if (PyErr_Occurred()) return NULL;

    Py_INCREF(Py_None);
    return Py_None;
}

PyDoc_STRVAR(recycle_autorelease_pool_doc,
  "recycleAutoreleasePool()\n"
  CLINIC_SEP
  "\n"
  "This 'releases' the global autorelease pool and creates a new one.\n"
  "This method is for system use only\n");
static PyObject*
recycle_autorelease_pool(PyObject* self __attribute__((__unused__)),
    PyObject* args, PyObject* kwds)
{
    static char* keywords[] = { NULL };

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "", keywords)) {
        return NULL;
    }

    if (global_release_pool != NULL) {

        PyObjC_DURING
            [global_release_pool release];
            [OC_NSAutoreleasePoolCollector newAutoreleasePool];

        PyObjC_HANDLER
            PyObjCErr_FromObjC(localException);

        PyObjC_ENDHANDLER

        if (PyErr_Occurred()) return NULL;
    }

    Py_INCREF(Py_None);
    return Py_None;
}

PyDoc_STRVAR(set_class_extender_doc,
    "_setClassExtender(func)\n"
    CLINIC_SEP
    "\n"
    "Register a function that will be called to update the class\n"
    "dict of new Objective-C classes and class-proxies. This will\n"
    "replace any existing callback.\n"
    "The function will be called like this:\n"
    "\tclass_extender(superclass, class_name, class_dict)\n"
    "superclass:\n"
    "  The superclass for the new class, or None if this is the top of\n"
    "  a class hierarchy.\n"
    "class_name:\n"
    "  Name of the new class\n"
    "class_dict:\n"
    "  The proposed class dictionary. The callback is supposed to update\n"
    "  this dictionary.\n"
    "");
static PyObject*
set_class_extender(PyObject* self __attribute__((__unused__)),
    PyObject* args, PyObject* kwds)
{
static char* keywords[] = { "callback", NULL };
    PyObject* callback;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "O:setClassExtender",
            keywords, &callback)) {
        return NULL;
    }

    if (!PyCallable_Check(callback)) {
        PyErr_SetString(PyExc_TypeError, "Expecting callable");
        return NULL;
    }

    SET_FIELD_INCREF(PyObjC_ClassExtender, callback);

    Py_INCREF(Py_None);
    return Py_None;
}


PyDoc_STRVAR(getClassList_doc,
  "getClassList()\n"
  CLINIC_SEP
  "\n"
  "Return a list with all Objective-C classes known to the runtime.\n"
);
static PyObject*
getClassList(PyObject* self __attribute__((__unused__)))
{
    return PyObjC_GetClassList();
}


PyDoc_STRVAR(allocateBuffer_doc,
         "allocateBuffer(size)\n"
         CLINIC_SEP
         "\n"
         "Allocate a buffer of memory of size. Buffer is \n"
         "read/write."
         );
static PyObject*
allocateBuffer(PyObject* self __attribute__((__unused__)), PyObject* args, PyObject* kwds)
{
    static char* keywords[] = { "length", 0 };
    Py_ssize_t length;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "n",
                keywords, &length)) {
        return NULL;
    }

    if (length <= 0 ) {
        PyErr_SetString(PyExc_ValueError,
            "Length must be greater than 0.");
        return NULL;
    }

#if PY_MAJOR_VERSION == 2 && PY_MINOR_VERSION < 6
    return PyBuffer_New(length);
#else
    return PyByteArray_FromStringAndSize(NULL, length);
#endif
}

PyDoc_STRVAR(currentBundle_doc,
    "currentBundle()\n"
    CLINIC_SEP
    "\n"
    "Get the current bundle during module initialization.\n"
    "Works for plug-ins and applications.\n"
    "\n"
    "Note that this is the default bundle used by\n"
    "NibClassBuilder.extractClasses(...),\n"
    "so calling it explicitly is rarely useful.\n"
    "After module initialization, use\n"
    "NSBundle.bundleForClass_(ClassInYourBundle)."
);
static PyObject*
currentBundle(PyObject* self __attribute__((__unused__)))
{
    id rval;
    char *bundle_address = getenv("PYOBJC_BUNDLE_ADDRESS");
    if (!(bundle_address && sscanf(bundle_address, "%p", &rval) == 1)) {
        rval = [NSBundle mainBundle];
    }
    return pythonify_c_value(@encode(id), &rval);
}


PyDoc_STRVAR(loadBundle_doc,
    "loadBundle(module_name, module_globals, bundle_path=None, "
    "bundle_identifier=None, scan_classes=True)\n"
    CLINIC_SEP
    "\n"
    "Load the bundle identified by 'bundle_path' or 'bundle_identifier' \n"
    "and add the classes in the bundle to the 'module_globals'.\n"
    "If 'scan_classes' is False the function won't add classes to 'module_globals'"
    "\n"
    "If 'bundle_identifier' is specified the right bundle is located\n"
    "using NSBundle's +bundleWithIdentifier:.\n"
    "If 'bundle_path' is specified the right bundle is located using\n"
    "NSBundle's +bundleWithPath:. The path must be an absolute pathname\n"
);
static PyObject*
loadBundle(PyObject* self __attribute__((__unused__)), PyObject* args, PyObject* kwds)
{
static char* keywords[] = { "module_name", "module_globals", "bundle_path", "bundle_identifier", "scan_classes", NULL };
static Py_ssize_t curClassCount = -1;
    NSBundle* bundle = nil;
    id bundle_identifier = nil;
    id bundle_path = nil;
    PyObject* module_name;
    PyObject* module_globals;
    PyObject* class_list;
    Py_ssize_t len, i;
    PyObject* scanClasses = NULL;

    if (!PyArg_ParseTupleAndKeywords(args, kwds,
#if PY_MAJOR_VERSION == 2
            "SO|O&O&O",
#else
            "UO|O&O&O",
#endif
            keywords, &module_name, &module_globals,
            PyObjCObject_Convert, &bundle_path, PyObjCObject_Convert, &bundle_identifier, &scanClasses)) {
        return NULL;
    }

    if (!bundle_path && !bundle_identifier) {
        PyErr_SetString(PyExc_ValueError,
            "Need to specify either bundle_path or "
            "bundle_identifier");
        return NULL;
    }
    if (bundle_path && bundle_identifier) {
        PyErr_SetString(PyExc_ValueError,
            "Need to specify either bundle_path or "
            "bundle_identifier");
        return NULL;
    }

    if (bundle_path) {
        if (![bundle_path isKindOfClass:[NSString class]]) {
            PyErr_SetString(PyExc_TypeError,
                    "bundle_path is not a string");
            return NULL;
        }
        bundle = [NSBundle bundleWithPath:bundle_path];
    } else {
        if (![bundle_identifier isKindOfClass:[NSString class]]) {
            PyErr_SetString(PyExc_TypeError,
                    "bundle_identifier is not a string");
            return NULL;
        }
        bundle = [NSBundle bundleWithIdentifier:bundle_identifier];
    }

    if (![bundle load]) {
        PyErr_SetString(PyExc_ImportError,
            "Bundle could not be loaded");
        return NULL;
    }

    /*
     * Scanning the class list is expensive and something to be avoided
     * when possible.
     */

    if (scanClasses != NULL && !PyObject_IsTrue(scanClasses)) {
        return pythonify_c_value(@encode(NSBundle*), &bundle);
    }

    class_list = PyObjC_GetClassList();
    if (class_list == NULL) {
        return NULL;
    }

    curClassCount = len = PyTuple_GET_SIZE(class_list);
    for (i = 0; i < len; i++) {
        PyObject* item;
        const char* nm;

        item = PyTuple_GET_ITEM(class_list, i);
        if (item == NULL) {
            continue;
        }

        nm = ((PyTypeObject*)item)->tp_name;

        if (nm[0] == '%') {
            /* skip, posed-as type */
        } else if (strcmp(nm, "Object") == 0
                || strcmp(nm, "List") == 0
                || strcmp(nm, "Protocol") == 0) {
            /* skip, these have been deprecated since OpenStep! */
        } else if (PyDict_SetItemString(module_globals,
                ((PyTypeObject*)item)->tp_name, item) == -1) {
            Py_DECREF(class_list); class_list = NULL;
            return NULL;
        }
    }
    Py_XDECREF(class_list); class_list = NULL;

    return pythonify_c_value(@encode(NSBundle*), &bundle);
}

PyDoc_STRVAR(objc_splitSignature_doc,
    "splitSignature(signature)\n"
    CLINIC_SEP
    "\n"
    "Split a signature string into a list of items."
);
static PyObject*
objc_splitSignature(PyObject* self __attribute__((__unused__)), PyObject* args, PyObject* kwds)
{
static char* keywords[] = { "signature", NULL };
    const char* signature;
    const char* end;
    PyObject* result;
    PyObject* tuple;

    if (!PyArg_ParseTupleAndKeywords(args, kwds,
            Py_ARG_BYTES,
            keywords, &signature)) {
        return NULL;
    }

    result = PyList_New(0);
    if (result == NULL) return NULL;

    while (signature && *signature != 0) {
        PyObject* str;
        const char* t;

        end = PyObjCRT_SkipTypeSpec(signature);
        if (end == NULL) {
            Py_DECREF(result);
            return NULL;
        }

        t = end-1;
        while (t != signature && isdigit(*t)) {
            t --;
        }
        t ++;

        str = PyBytes_FromStringAndSize(signature, t - signature);
        if (str == NULL) {
            Py_DECREF(result);
            return NULL;
        }

        if (PyList_Append(result, str) == -1) {
            Py_DECREF(str);
            Py_DECREF(result);
            return NULL;
        }
        Py_DECREF(str);

        signature = end;
    }

    tuple = PyList_AsTuple(result);
    Py_DECREF(result);
    return tuple;
}


PyDoc_STRVAR(objc_splitStructSignature_doc,
    "splitStructSignature(signature)\n"
    CLINIC_SEP
    "\n"
    "Split a struct signature string into a list of items."
);
static PyObject*
objc_splitStructSignature(PyObject* self __attribute__((__unused__)), PyObject* args, PyObject* kwds)
{
static char* keywords[] = { "signature", NULL };
    const char* signature;
    const char* end;
    PyObject* structname;
    PyObject* fields;

    if (!PyArg_ParseTupleAndKeywords(args, kwds,
            Py_ARG_BYTES,
            keywords, &signature)) {
        return NULL;
    }

    if (signature[0] != _C_STRUCT_B) {
        PyErr_SetString(PyExc_ValueError, "not a struct encoding");
        return NULL;
    }

    signature += 1;
    end = signature;
    while (*end && *end != _C_STRUCT_E && *end++ != '=');
    if (end == signature+1) {
        structname = Py_None;
        Py_INCREF(structname);

    } else {
        structname = PyText_FromStringAndSize(signature, end-signature-1);
        if (structname == NULL) {
            return NULL;
        }
    }

    if (*end == '=') {
        signature = end+1;
    } else {
        signature = end;
    }

    fields = PyList_New(0);
    if (fields == NULL) return NULL;

    while (signature && *signature != _C_STRUCT_E && *signature != 0) {
        PyObject* str;
        PyObject* item;
        PyObject* name;
        const char* t;

        if (*signature == '"') {
            signature ++;
            end = signature;
            while (*end && *end != '"') {
                end ++;
            }
            name = PyText_FromStringAndSize(signature, end-signature);
            if (name == NULL) {
                Py_DECREF(structname);
                Py_DECREF(fields);
                return NULL;
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

        t = end-1;
        while (t != signature && isdigit(*t)) {
            t --;
        }
        t ++;

        str = PyBytes_FromStringAndSize(signature, t - signature);
        if (str == NULL) {
            Py_DECREF(structname);
            Py_DECREF(name);
            Py_DECREF(fields);
            return NULL;
        }

        item = Py_BuildValue("NN", name, str);
        if (item == NULL) {
            Py_DECREF(fields);
            return NULL;
        }

        if (PyList_Append(fields, item) == -1) {
            Py_DECREF(fields);
            Py_DECREF(item);
            Py_DECREF(structname);
            return NULL;
        }
        Py_DECREF(item);

        signature = end;
    }

    if (signature && *signature != _C_STRUCT_E) {
        Py_DECREF(structname);
        Py_DECREF(fields);
        PyErr_SetString(PyExc_ValueError, "Value is not a complete struct signature");
        return NULL;
    }

    if (signature && signature[1]) {
        Py_DECREF(structname);
        Py_DECREF(fields);
        PyErr_SetString(PyExc_ValueError, "Additional text at end of signature");
        return NULL;
    }

    return Py_BuildValue("NN", structname, fields);
}

PyDoc_STRVAR(PyObjC_loadBundleVariables_doc,
    "loadBundleVariables(bundle, module_globals, variableInfo, "
    "skip_undefined=True)\n"
    CLINIC_SEP
    "\n"
    "Load the specified variables in the bundle. If skip_undefined is \n"
    "True, variables that are not present in the bundle are skipped, \n"
    "otherwise this method raises objc.error when a variable cannot be \n"
    "found.\n"
    "\n"
    "variableInfo is a list of (name, type) pairs. The type is the \n"
    "Objective-C type specifier for the variable type.");
PyDoc_STRVAR(PyObjC_loadBundleFunctions_doc,
    "loadBundleFunctions(bundle, module_globals, functionInfo, "
    "skip_undefined=True)\n"
    CLINIC_SEP
    "\n"
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
    "skip_undefined=True)\n"
    CLINIC_SEP
    "\n"
    "Load the specified functions. List should be a capsule object containing\n"
    "an array of { char*, funcion } structs.");
PyDoc_STRVAR(PyObjC_loadSpecialVar_doc,
    "loadSpecialVar(bundle, module_globals, typeid, name, skip_undefined=True)\n"
    CLINIC_SEP
    "\n"
    "Load a magic cookie object from a bundle. A magic cookie is a \n"
    "C pointer that represents a CoreFoundation or Objective-C object \n"
    "that cannot be deferenced.\n");




PyDoc_STRVAR(protocolsForProcess_doc,
    "protocolsForProcess()\n"
    CLINIC_SEP
    "\n"
    "Returns a list of Protocol objects that are present in the process"
);
static PyObject*
protocolsForProcess(PyObject* self __attribute__((__unused__)))
{
    PyObject *protocols;
    Protocol** protlist;
    unsigned int protCount;
    unsigned int i;

    protlist = objc_copyProtocolList(&protCount);
    if (protlist == NULL) {
        Py_INCREF(Py_None);
        return Py_None;
    }

    protocols = PyList_New(protCount);

    if (protocols == NULL) {
        return NULL;
    }

    for (i = 0; i < protCount; i++) {
        PyObject *p = PyObjCFormalProtocol_ForProtocol(protlist[i]);
        if (p == NULL) {
            Py_DECREF(protocols);
            free(protlist);
            return NULL;
        }

        PyList_SET_ITEM(protocols, i, p);
    }

    free(protlist);
    return protocols;
}

PyDoc_STRVAR(protocolNamed_doc,
    "_protocolNamed(name)\n"
    CLINIC_SEP
    "\n"
    "Returns an Objective-C protocol named *name*.\n"
    "Raises AttributeError when no such protocol can be found.\n"
    );
static PyObject*
protocolNamed(PyObject* self __attribute__((__unused__)), PyObject* args, PyObject* kwds)
{
static char* keywords[] = { "name", NULL };
    char* name;
    Protocol* p;

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
    "protocolsForClass(cls)\n"
    CLINIC_SEP
    "\n"
    "Returns a list of Protocol objects that the class claims\n"
    "to implement directly."
);
static PyObject*
protocolsForClass(PyObject* self __attribute__((__unused__)),
        PyObject* args,
        PyObject* kwds)
{
    static char* keywords[] = { "cls", NULL };
    Protocol** protocol_list;
    unsigned int protocol_count, i;
    PyObject *protocols;
    Class cls;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "O&:protocolsForClass", keywords,
            PyObjCClass_Convert, &cls)) {
        return NULL;
    }

    protocols = PyList_New(0);
    if (protocols == NULL) {
        return NULL;
    }

    protocol_list = class_copyProtocolList(cls, &protocol_count);
    for (i = 0; i < protocol_count; i++) {
        PyObject *protocol = PyObjCFormalProtocol_ForProtocol(protocol_list[i]);
        if (protocol == NULL) {
            free(protocol_list);
            Py_DECREF(protocols);
            return NULL;
        }
        PyList_Append(protocols, protocol);
        Py_DECREF(protocol);
    }

    free(protocol_list);
    return protocols;
}

PyDoc_STRVAR(createOpaquePointerType_doc,
    "createOpaquePointerType(name, typestr, doc)\n"
    CLINIC_SEP
    "\n"
    "Return a wrapper type for opaque pointers of the given type. The type \n"
    "will be registered with PyObjC and will be used to wrap pointers of the \n"
    "given type."
);
static PyObject*
createOpaquePointerType(PyObject* self __attribute__((__unused__)),
        PyObject* args, PyObject* kwds)
{
static char* keywords[] = { "name", "typestr", "doc", NULL };
    char* name;
    char* typestr;
    char* docstr = NULL;

    if (!PyArg_ParseTupleAndKeywords(args, kwds,
                "s"Py_ARG_BYTES"|z",
                keywords,
                &name, &typestr, &docstr)) {
        return NULL;
    }

    return PyObjCCreateOpaquePointerType(name, typestr, docstr);
}

PyDoc_STRVAR(copyMetadataRegistry_doc,
    "_copyMetadataRegistry()\n"
    CLINIC_SEP
    "\n"
    "Return a copy of the metdata registry.");
static PyObject*
copyMetadataRegistry(PyObject* self __attribute__((__unused__)), PyObject* args, PyObject* kwds)
{
static char* keywords[] = { NULL };

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "", keywords)) {
        return NULL;
    }
    return PyObjC_copyMetadataRegistry();
}

PyDoc_STRVAR(registerMetaData_doc,
    "registerMetaDataForSelector(classObject, selector, metadata)\n"
    CLINIC_SEP
    "\n"
    "Registers a metadata dictionary for method *selector* in *class*");
static PyObject*
registerMetaData(PyObject* self __attribute__((__unused__)), PyObject* args, PyObject* kwds)
{
static char* keywords[] = { "class_", "selector", "metadata", NULL };

    PyObject* class_name;
    PyObject* selector;
    PyObject* metadata;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "SSO", keywords,
            &class_name, &selector, &metadata)) {
        return NULL;
    }

    if (PyObjC_registerMetaData(class_name, selector, metadata) < 0) {
        return NULL;

    } else {
        PyObjC_MappingCount ++;
        Py_INCREF(Py_None);
        return Py_None;
    }
}

PyDoc_STRVAR(registerStructAlias_doc,
    "registerStructAlias(typestr, structType)\n"
    CLINIC_SEP
    "\n"
    "Registers 'typestr' as a type that should be mapped onto 'structType'\n"
    "'structType' must be created using 'createStructType' (or through \n"
    "a metadata file."
);
static PyObject*
registerStructAlias(PyObject* self __attribute__((__unused__)),
                        PyObject* args, PyObject* kwds)
{
    static char* keywords[] = { "typestr", "structType", NULL };
    char* typestr;
    PyObject* structType;

    if (!PyArg_ParseTupleAndKeywords(args, kwds,
                Py_ARG_BYTES "O",
                keywords, &typestr, &structType)) {
        return NULL;
    }

    if (PyObjC_RegisterStructAlias(typestr, structType) == -1) {
        return NULL;
    }

    Py_INCREF(structType);
    return structType;
}


PyDoc_STRVAR(createStructType_doc,
    "createStructType(name, typestr, fieldnames, doc, pack)\n"
    CLINIC_SEP
    "\n"
    "Return a wrapper type for structs of the given type. The wrapper will \n"
    "registered with PyObjC and will be used to wrap structs of the given type.\n"
    "The field names can be ``None`` iff the typestr contains field names."
);
static PyObject*
createStructType(PyObject* self __attribute__((__unused__)),
        PyObject* args, PyObject* kwds)
{
static char* keywords[] = { "name", "typestr", "fieldnames", "doc", "pack", NULL };
    char* name;
    char* typestr;
    PyObject* pyfieldnames;
    char* docstr = NULL;
    PyObject* retval;
    char** fieldnames = NULL;
    Py_ssize_t i;
    Py_ssize_t field_count;
    Py_ssize_t pack = -1;

    if (!PyArg_ParseTupleAndKeywords(args, kwds,
                "s"Py_ARG_BYTES"O|zn",
                keywords,
                &name, &typestr, &pyfieldnames, &docstr, &pack)) {
        return NULL;
    }

    name = PyObjCUtil_Strdup(name);
    typestr = PyObjCUtil_Strdup(typestr);
    if (docstr) {
        docstr = PyObjCUtil_Strdup(docstr);
    }

    if (pyfieldnames != Py_None) {
        pyfieldnames = PySequence_Fast(pyfieldnames,
            "fieldnames must be a sequence of strings");

        if (pyfieldnames == NULL) goto error_cleanup;
        if (name == NULL || typestr == NULL) {
            PyErr_NoMemory();
            goto error_cleanup;
        }

        fieldnames = PyMem_Malloc(sizeof(char*) * PySequence_Fast_GET_SIZE(pyfieldnames));
        if (fieldnames == NULL) {
            PyErr_NoMemory();
            goto error_cleanup;
        }
        memset(fieldnames, 0,
                sizeof(char*) * PySequence_Fast_GET_SIZE(pyfieldnames));
        for (i = 0; i < PySequence_Fast_GET_SIZE(pyfieldnames); i++) {
            PyObject* v = PySequence_Fast_GET_ITEM(pyfieldnames, i);
            if (PyUnicode_Check(v)) {
                PyObject* bytes = PyUnicode_AsEncodedString(v, NULL, NULL);
                if (bytes == NULL) {
                    goto error_cleanup;
                }
                fieldnames[i] = PyObjCUtil_Strdup(PyBytes_AsString(bytes));
                Py_DECREF(bytes);

#if PY_MAJOR_VERSION == 2
            } else if (PyString_Check(v)) {
                fieldnames[i] = PyObjCUtil_Strdup(PyString_AS_STRING(v));
#endif

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
        fieldnames = NULL;
    }

    retval = PyObjC_RegisterStructType(typestr, name, docstr, NULL,
            field_count, (const char**)fieldnames, pack);
    if (retval == NULL) goto error_cleanup;
    Py_DECREF(pyfieldnames);

    return retval;

error_cleanup:
    if (name) PyMem_Free(name);
    if (typestr) PyMem_Free(typestr);
    if (docstr) PyMem_Free(docstr);

    if (fieldnames) {
        for (i = 0; i < PySequence_Fast_GET_SIZE(pyfieldnames); i++) {
            if (fieldnames[i]) PyMem_Free(fieldnames[i]);
        }
        PyMem_Free(fieldnames);
    }

    Py_XDECREF(pyfieldnames);

    return NULL;
}

PyDoc_STRVAR(PyObjCIvar_Info_doc,
    "listInstanceVariables(classOrInstance)\n"
    CLINIC_SEP
    "\n"
    "Return information about all instance variables of an object or class\n"
);
PyDoc_STRVAR(PyObjCIvar_Get_doc,
    "getInstanceVariable(object, name)\n"
    CLINIC_SEP
    "\n"
    "Return the value of an instance variable\n"
);
PyDoc_STRVAR(PyObjCIvar_Set_doc,
    "setInstanceVariable(object, name, value, updateRefCount=False)\n"
    CLINIC_SEP
    "\n"
    "Modify an instance variable. If the instance variable is an object \n"
    "reference you must include the ``updateRefCount`` argument, otherwise it \n"
    "is ignored. If ``updateRefCount`` is true the reference counts of the \n"
    "old and new values are updated, otherwise they are not.\n"
    "\n"
    "NOTE: updating instance variables is dangerous, instance variables are \n"
    "private in Objective-C and classes might not expected that those values \n"
    "are changed by other code."
);

PyDoc_STRVAR(registerCFSignature_doc,
    "registerCFSignature(name, encoding, typeId, tollfreeName=None)\n"
    CLINIC_SEP
    "\n"
    "Register a CoreFoundation based type with the bridge. If \n"
    "tollFreeName is supplied the type is tollfree bridged to that class.");
static PyObject*
registerCFSignature(PyObject* self __attribute__((__unused__)),
        PyObject* args, PyObject* kwds)
{
    static char* keywords[] = { "name", "encoding", "typeId", "tollfreeName", NULL };
    char* name;
    char* encoding;
    PyObject* pTypeId;
    CFTypeID typeId;
    char* tollfreeName = NULL;

    if (!PyArg_ParseTupleAndKeywords(args, kwds,
        "s"Py_ARG_BYTES"O|s",
        keywords, &name, &encoding, &pTypeId, &tollfreeName)) {
        return NULL;
    }

    if (pTypeId == Py_None) {
        if (tollfreeName == NULL) {
            PyErr_SetString(PyExc_ValueError,
                "Must specify a typeid when not toll-free");
            return NULL;
        }
        typeId = (CFTypeID)-1;

    } else if (depythonify_c_value(@encode(CFTypeID), pTypeId, &typeId) == -1) {
        return NULL;

    } else {
        PyObject* v = PyInt_FromLong(typeId);
        int r;

        if (v == NULL) {
            return NULL;
        }

        r = PyDict_SetItemString(PyObjC_TypeStr2CFTypeID, encoding, v);
        Py_DECREF(v);
        if (r == -1) {
            return NULL;
        }
    }

    if (tollfreeName) {
        Class cls = objc_lookUpClass(tollfreeName);

        if (cls == nil) {
            PyErr_SetString(PyObjCExc_NoSuchClassError,
                    tollfreeName);
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

PyDoc_STRVAR(_updatingMetadata_doc,
    "_updatingMetadata(flag)\n"
    CLINIC_SEP
    "\n"
    "PRIVATE FUNCTION");
static PyObject*
_updatingMetadata(PyObject* self __attribute__((__unused__)),
        PyObject* args, PyObject* kwds)
{
    static char* keywords[] = { "flag", NULL };
    PyObject* flag;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "O", keywords, &flag)) {
        return NULL;
    }

    if (PyObject_IsTrue(flag)) {
        PyObjC_UpdatingMetaData = YES;

    } else {
        PyObjC_MappingCount ++;
        PyObjC_UpdatingMetaData = NO;

    }

    Py_INCREF(Py_None);
    return Py_None;
}

/* Support for locking */
static PyObject*
PyObjC_objc_sync_enter(PyObject* self __attribute__((__unused__)), PyObject* args)
{
    NSObject* object;
    int rv;

    if (!PyArg_ParseTuple(args, "O&",
            PyObjCObject_Convert, &object)) {
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

static PyObject*
PyObjC_objc_sync_exit(PyObject* self __attribute__((__unused__)), PyObject* args)
{
    NSObject* object;
    int rv;

    if (!PyArg_ParseTuple(args, "O&",
            PyObjCObject_Convert, &object)) {
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
  "_makeClosure(callable, closureFor, argIndex=0)\n"
  CLINIC_SEP
  "\n"
  "Returns a closure object that can be used to call the function from\n"
  "C. This object has no useable interface from Python.\n"
 );
#if PY_MAJOR_VERSION == 2 && PY_MINOR_VERSION < 7
static void _callback_cleanup(void* closure)
{
    PyObjCFFI_FreeIMP((IMP)closure);
}

#else /* Python >= 2.7 */

static void _callback_cleanup(PyObject* closure)
{
    PyObjCFFI_FreeIMP((IMP)PyCapsule_GetPointer(closure, "objc.__imp__"));
}
#endif /* Python >= 2.7 */

static PyObject*
_makeClosure(
    PyObject* self __attribute__((__unused__)),
    PyObject* args,
    PyObject* kwds)
{
static char* keywords[] = { "callable", "closureFor", "argIndex", NULL };
    PyObject* callable;
    PyObject* closureFor;
    PyObjCMethodSignature* methinfo;
    Py_ssize_t argIndex = 0;
    Py_ssize_t i;

    argIndex=-1;
    if (!PyArg_ParseTupleAndKeywords(args, kwds, "OO|n",
        keywords, &callable, &closureFor, &argIndex)) {
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
        PyErr_Format(PyExc_TypeError, "Don't know how to create closure for instance of %s",
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
            PyErr_SetString(PyExc_IndexError,
                "No such argument");
            return NULL;
        }

        if (methinfo->argtype[argIndex]->callable == NULL) {
            PyErr_Format(PyExc_ValueError,
                "Argument %" PY_FORMAT_SIZE_T "d is not callable", argIndex);
            return NULL;
        }
    }

    PyObjC_callback_function result;

    result = PyObjCFFI_MakeFunctionClosure(methinfo->argtype[argIndex]->callable, callable);
    if (result == NULL) {
        return NULL;
    }

    PyObject* retval = PyCapsule_New(
        result, "objc.__imp__", _callback_cleanup);
    if (retval == NULL) {
        PyObjCFFI_FreeIMP((IMP)result);
        return NULL;
    }

    return Py_BuildValue("NN", retval, PyObjCMethodSignature_AsDict(methinfo->argtype[argIndex]->callable));
}

PyDoc_STRVAR(_closurePointer_doc,
  "_closurePointer(closure)\n"
  CLINIC_SEP
  "\n"
  "Returns an integer that corresponds to the numeric value of the C pointer\n"
  "for the closure."
 );
static PyObject*
_closurePointer(
    PyObject* self __attribute__((__unused__)),
    PyObject* args,
    PyObject* kwds)
{
static char* keywords[] = { "closure", NULL };
    PyObject* closure;
    void*     pointer;


    if (!PyArg_ParseTupleAndKeywords(args, kwds, "O",
        keywords, &closure)) {
        return NULL;
    }

    pointer = PyCapsule_GetPointer(closure, "objc.__imp__");
    if (pointer == NULL && PyErr_Occurred()) {
        return NULL;
    }
    return PyLong_FromVoidPtr(pointer);
}

static PyObject*
ivar_dict(PyObject* self __attribute__((__unused__)))
{
    Py_INCREF(PyObjCInstanceVariable_Type.tp_dict);
    return PyObjCInstanceVariable_Type.tp_dict;
}

static PyObject*
mod_propertiesForClass(PyObject* mod __attribute__((__unused__)), PyObject* object)
{
    return PyObjCClass_ListProperties(object);
}

/*
 * Helper function for decoding XML metadata:
 *
 * This fixes an issue with metadata files: metadata files use
 * _C_BOOL to represent type 'BOOL', but that the string should
 * be used to represent 'bool' which has a different size on
 * PPC. Therefore swap usage of _C_BOOL and _C_NSBOOL in data
 * from metadata files.
 */
static void
typecode2typecode(char* buf)
{
    /* Skip pointer declarations and anotations */
    for (;;) {
        switch(*buf) {
        case _C_PTR:
        case _C_IN:
        case _C_OUT:
        case _C_INOUT:
        case _C_ONEWAY:
        case _C_CONST:
            buf++;
            break;
        default:
              goto exit;
        }
    }
exit:

    switch (*buf) {
    case _C_BOOL:
        *buf = _C_NSBOOL;
        break;
    case _C_NSBOOL:
        *buf = _C_BOOL;
        break;
        case _C_STRUCT_B:
        while (buf && *buf != _C_STRUCT_E && *buf && *buf++ != '=') {
        }
        while (buf && *buf && *buf != _C_STRUCT_E) {
            if (*buf == '"') {
                /* embedded field name */
                buf = strchr(buf+1, '"');
                if (buf == NULL) {
                    return;
                }
                buf++;
            }
            typecode2typecode(buf);
            buf = (char*)PyObjCRT_SkipTypeSpec(buf);
        }
        break;

    case _C_UNION_B:
        while (buf && *buf != _C_UNION_E && *buf && *buf++ != '=') {
        }
        while (buf && *buf && *buf != _C_UNION_E) {
            if (*buf == '"') {
                /* embedded field name */
                buf = strchr(buf+1, '"');
                if (buf == NULL) {
                    return;
                }
                buf++;
            }
            typecode2typecode(buf);
            buf = (char*)PyObjCRT_SkipTypeSpec(buf);
        }
        break;


    case _C_ARY_B:
        while (isdigit(*++buf));
        typecode2typecode(buf);
        break;
    }
}



static PyObject*
typestr2typestr(PyObject* args)
{
    char* s;
    char* buf;

    if (PyUnicode_Check(args)) {
        PyObject* bytes = PyUnicode_AsEncodedString(args, NULL, NULL);
        if (bytes == NULL) {
            return NULL;
        }
        buf = PyObjCUtil_Strdup(PyBytes_AsString(args));
        Py_DECREF(bytes);

    } else if (PyBytes_Check(args)) {
        buf = PyObjCUtil_Strdup(PyBytes_AsString(args));
    } else {
        PyErr_SetString(PyExc_TypeError, "expecing string");
        return NULL;
    }

    if (buf == NULL) {
        PyErr_NoMemory();
        return NULL;
    }

    s = buf;
    while (s && *s) {
        typecode2typecode(s);
        if (s && *s == '\"') {
            PyErr_Format(PyObjCExc_InternalError,
                "typecode2typecode: invalid typecode '%c' "
                "at \"%s\"", *s, s);
            *s = '\0';
            PyMem_Free(buf);
            return NULL;

        } else {
            s = (char*)PyObjCRT_SkipTypeSpec(s);
        }
    }

    PyObject* result = PyBytes_FromString(buf);
    PyMem_Free(buf);

    return result;
}

#if PyObjC_BUILD_RELEASE >= 1006
    /* Associated Object support. Functionality is available on OSX 10.6 or later. */

PyDoc_STRVAR(PyObjC_setAssociatedObject_doc,
    "setAssociatedObject(object, key, value, policy=objc.OBJC_ASSOCIATION_RETAIN)\n"
    CLINIC_SEP
    "\n"
    "Set the value for an object assiociation. Use 'None' as the\n"
    "value to clear an association.");
static PyObject*
PyObjC_setAssociatedObject(PyObject* self __attribute__((__unused__)),
    PyObject* args, PyObject* kwds)
{
static char* keywords[] = { "object", "key", "value", "policy", NULL };
    id object;
    PyObject* key;
    id value;
    long policy = OBJC_ASSOCIATION_RETAIN;

    if (&objc_setAssociatedObject == NULL) {
        PyErr_SetString(PyObjCExc_Error, "setAssociatedObject not available on this platform");
        return NULL;
    }

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "O&OO&|l",
        keywords,
        PyObjCObject_Convert, &object,
        &key,
        PyObjCObject_Convert, &value,
        &policy
        )) {

        return NULL;
    }

    PyObjC_DURING
        objc_setAssociatedObject(object, (void*)key, value, policy);

    PyObjC_HANDLER
        PyObjCErr_FromObjC(localException);

    PyObjC_ENDHANDLER

    if (PyErr_Occurred()) return NULL;

    Py_INCREF(Py_None);
    return Py_None;
}


PyDoc_STRVAR(PyObjC_getAssociatedObject_doc,
    "getAssociatedObject(object, key)\n"
    CLINIC_SEP
    "\n"
    "Get the value for an object assiociation. Returns None \n"
    "when they association doesn't exist.");
static PyObject*
PyObjC_getAssociatedObject(PyObject* self __attribute__((__unused__)),
    PyObject* args, PyObject* kwds)
{
static char* keywords[] = { "object", "key", NULL};
    id object;
    PyObject* key;
    id value;

    if (&objc_getAssociatedObject == NULL) {
        PyErr_SetString(PyObjCExc_Error, "setAssociatedObject not available on this platform");
        return NULL;
    }

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "O&O",
        keywords,
        PyObjCObject_Convert, &object,
        &key
        )) {

        return NULL;
    }

    PyObjC_DURING
        value = objc_getAssociatedObject(object, (void*)key);

    PyObjC_HANDLER
        value = nil;
        PyObjCErr_FromObjC(localException);
    PyObjC_ENDHANDLER

    if (PyErr_Occurred()) return NULL;

    return PyObjC_IdToPython(value);
}

PyDoc_STRVAR(PyObjC_removeAssociatedObjects_doc,
    "removeAssociatedObjects(object)\n"
    CLINIC_SEP
    "\n"
    "Remove all assocations from an object. This should in general not be used because\n"
    "it clear all references, including those made from unrelated code.\n");

static PyObject*
PyObjC_removeAssociatedObjects(PyObject* self __attribute__((__unused__)),
    PyObject* args, PyObject* kwds)
{
static char* keywords[] = { "object", NULL};
    id object;

    if (&objc_removeAssociatedObjects == NULL) {
        PyErr_SetString(PyObjCExc_Error, "removeAssociatedObjects not available on this platform");
        return NULL;
    }

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "O&",
        keywords,
        PyObjCObject_Convert, &object
        )) {

        return NULL;
    }

    PyObjC_DURING
        objc_removeAssociatedObjects(object);

    PyObjC_HANDLER
        PyObjCErr_FromObjC(localException);

    PyObjC_ENDHANDLER

    if (PyErr_Occurred()) return NULL;

    Py_INCREF(Py_None);
    return Py_None;
}
#endif

static PyObject*
PyObjC_LoadConstant(PyObject* self __attribute__((__unused__)),
    PyObject* args, PyObject* kwds)
{
static char* keywords[] = { "name", "type", "magic", NULL };
    char* name;
    char* type;
    int magic;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "ssi",
        keywords, &name, &type, &magic)) {

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
            v = PyObjCCF_NewSpecial(type, *(void**)buf);
        } else {
            v = PyObjCCF_NewSpecial(type, buf);
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


PyObject* PyObjC_callable_docstr_get(PyObject* callable, void* closure __attribute__((__unused__)))

{
    if (PyObjC_CallableDocFunction == NULL) {
        Py_INCREF(Py_None);
        return Py_None;
    }
    return PyObject_CallFunction(PyObjC_CallableDocFunction, "O", callable);
}

#if PY_VERSION_HEX >= 0x03030000
PyObject* PyObjC_callable_signature_get(PyObject* callable, void* closure __attribute__((__unused__)))

{
    if (PyObjC_CallableSignatureFunction == NULL) {
        Py_INCREF(Py_None);
        return Py_None;
    }
    return PyObject_CallFunction(PyObjC_CallableSignatureFunction, "O", callable);
}
#endif /* PY_VERSION_HEX >= 0x03030000 */

static PyObject*
name_for_signature(PyObject* mod __attribute__((__unused__)), PyObject* signature)
{
    char* typestr;
    if (!PyBytes_Check(signature)) {
        PyErr_Format(PyExc_TypeError, "type encoding must be a bytes string, not a '%s' object",
                Py_TYPE(signature)->tp_name);
        return NULL;
    }
    typestr = PyBytes_AS_STRING(signature);
    if (typestr[0] == _C_STRUCT_B) {
        PyTypeObject* type = (PyTypeObject*)PyObjC_FindRegisteredStruct(typestr, PyBytes_GET_SIZE(signature));
        if (type == NULL) {
            Py_INCREF(Py_None);
            return Py_None;
        } else {
#if PY_MAJOR_VERSION == 2
            return PyString_FromString(type->tp_name);
#else
            return PyUnicode_FromString(type->tp_name);
#endif
        }
    }
    if (typestr[0] == _C_PTR) {
        const char* name = PyObjCPointerWrapper_Describe(typestr);
        if (name != NULL) {
#if PY_MAJOR_VERSION == 2
            return PyString_FromString(name);
#else
            return PyUnicode_FromString(name);
#endif
        }
    }
    Py_INCREF(Py_None);
    return Py_None;
}

static PyObject*
block_signature(PyObject* mod __attribute__((__unused__)), PyObject* block)
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

static PyObject*
force_rescan(PyObject* mod __attribute__((__unused__)), PyObject* args, PyObject* kwds)
{
static char* keywords[] = { "name", NULL };
    const char* class_name;
    PyObject* py_cls;
    Class cls;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "s", keywords, &class_name)) {
        return NULL;
    }

    cls = objc_lookUpClass(class_name);
    if (cls == Nil) goto done;

    py_cls = objc_class_locate(cls);
    if (py_cls == NULL) goto done;

    if (PyObjCClass_CheckMethodList(py_cls, NO) < 0) {
        return NULL;
    }

done:
    Py_INCREF(Py_None);
    return Py_None;
}


static PyMethodDef mod_methods[] = {
    {
        .ml_name    = "propertiesForClass",
        .ml_meth    = (PyCFunction)mod_propertiesForClass,
        .ml_flags   = METH_O,
        .ml_doc     =
            "propertiesForClass(classObject)\n"
            CLINIC_SEP
            "\n"
            "Return information about properties from the runtime",
    },
    {
        .ml_name    = "splitSignature",
        .ml_meth    = (PyCFunction)objc_splitSignature,
        .ml_flags   = METH_VARARGS|METH_KEYWORDS,
        .ml_doc     = objc_splitSignature_doc
    },
    {
        .ml_name    = "splitStructSignature",
        .ml_meth    = (PyCFunction)objc_splitStructSignature,
        .ml_flags   = METH_VARARGS|METH_KEYWORDS,
        .ml_doc     = objc_splitStructSignature_doc,
    },
    {
        .ml_name    = "lookUpClass",
        .ml_meth    = (PyCFunction)lookUpClass,
        .ml_flags   = METH_VARARGS|METH_KEYWORDS,
        .ml_doc     = lookUpClass_doc
    },
    {
        .ml_name    = "classAddMethods",
        .ml_meth    = (PyCFunction)classAddMethods,
        .ml_flags   = METH_VARARGS|METH_KEYWORDS,
        .ml_doc     = classAddMethods_doc
    },
    {
        .ml_name    = "currentBundle",
        .ml_meth    = (PyCFunction)currentBundle,
        .ml_flags   = METH_NOARGS,
        .ml_doc     = currentBundle_doc
    },
    {
        .ml_name    = "getClassList",
        .ml_meth    = (PyCFunction)getClassList,
        .ml_flags   = METH_NOARGS,
        .ml_doc     = getClassList_doc
    },
    {
        .ml_name    = "_setClassExtender",
        .ml_meth    = (PyCFunction)set_class_extender,
        .ml_flags   = METH_VARARGS|METH_KEYWORDS,
        .ml_doc     = set_class_extender_doc
    },
    {
        .ml_name    = "recycleAutoreleasePool",
        .ml_meth    = (PyCFunction)recycle_autorelease_pool,
        .ml_flags   = METH_VARARGS|METH_KEYWORDS,
        .ml_doc     = recycle_autorelease_pool_doc
    },
    {
        .ml_name    = "removeAutoreleasePool",
        .ml_meth    = (PyCFunction)remove_autorelease_pool,
        .ml_flags   = METH_VARARGS|METH_KEYWORDS,
        .ml_doc     = remove_autorelease_pool_doc
    },
    {
        .ml_name    = "pyobjc_id",
        .ml_meth    = (PyCFunction)pyobjc_id,
        .ml_flags   = METH_VARARGS|METH_KEYWORDS,
        .ml_doc     = pyobjc_id_doc
    },
    {
        .ml_name    = "repythonify",
        .ml_meth    = (PyCFunction)repythonify,
        .ml_flags   = METH_VARARGS|METH_KEYWORDS,
        .ml_doc     = repythonify_doc
    },
    {
        .ml_name    = "loadBundle",
        .ml_meth    = (PyCFunction)loadBundle,
        .ml_flags   = METH_VARARGS|METH_KEYWORDS,
        .ml_doc     = loadBundle_doc
    },
    {
        .ml_name    = "allocateBuffer",
        .ml_meth    = (PyCFunction)allocateBuffer,
        .ml_flags   = METH_VARARGS|METH_KEYWORDS,
        .ml_doc     = allocateBuffer_doc
    },
    {
        .ml_name    = "protocolsForClass",
        .ml_meth    = (PyCFunction)protocolsForClass,
        .ml_flags   = METH_VARARGS|METH_KEYWORDS,
        .ml_doc     = protocolsForClass_doc
    },
    {
        .ml_name    = "protocolsForProcess",
        .ml_meth    = (PyCFunction)protocolsForProcess,
        .ml_flags   = METH_NOARGS,
        .ml_doc     = protocolsForProcess_doc
    },
    {
        .ml_name    = "_protocolNamed",
        .ml_meth    = (PyCFunction)protocolNamed,
        .ml_flags   = METH_VARARGS|METH_KEYWORDS,
        .ml_doc     = protocolNamed_doc
    },
    {
        .ml_name    = "registerCFSignature",
        .ml_meth    = (PyCFunction)registerCFSignature,
        .ml_flags   = METH_VARARGS|METH_KEYWORDS,
        .ml_doc     = registerCFSignature_doc
    },
    {
        .ml_name    = "loadBundleVariables",
        .ml_meth    = (PyCFunction)PyObjC_loadBundleVariables,
        .ml_flags   = METH_VARARGS|METH_KEYWORDS,
        .ml_doc     = PyObjC_loadBundleVariables_doc
    },
    {
        .ml_name    = "loadSpecialVar",
        .ml_meth    = (PyCFunction)PyObjC_loadSpecialVar,
        .ml_flags   = METH_VARARGS|METH_KEYWORDS,
        .ml_doc     = PyObjC_loadSpecialVar_doc
    },
    {
        .ml_name    = "loadBundleFunctions",
        .ml_meth    = (PyCFunction)PyObjC_loadBundleFunctions,
        .ml_flags   = METH_VARARGS|METH_KEYWORDS,
        .ml_doc     = PyObjC_loadBundleFunctions_doc
    },
    {
        .ml_name    = "loadFunctionList",
        .ml_meth    = (PyCFunction)PyObjC_loadFunctionList,
        .ml_flags   = METH_VARARGS|METH_KEYWORDS,
        .ml_doc     = PyObjC_loadFunctionList_doc
    },
    {
        .ml_name    = "listInstanceVariables",
        .ml_meth    = (PyCFunction)PyObjCIvar_Info,
        .ml_flags   = METH_O,
        .ml_doc     = PyObjCIvar_Info_doc
    },
    {
        .ml_name    = "getInstanceVariable",
        .ml_meth    = (PyCFunction)PyObjCIvar_Get,
        .ml_flags   = METH_VARARGS|METH_KEYWORDS,
        .ml_doc     = PyObjCIvar_Get_doc
    },
    {
        .ml_name    = "setInstanceVariable",
        .ml_meth    = (PyCFunction)PyObjCIvar_Set,
        .ml_flags   = METH_VARARGS|METH_KEYWORDS,
        .ml_doc     = PyObjCIvar_Set_doc
    },
    {
        .ml_name    = "createOpaquePointerType",
        .ml_meth    = (PyCFunction)createOpaquePointerType,
        .ml_flags   = METH_VARARGS|METH_KEYWORDS,
        .ml_doc     = createOpaquePointerType_doc
    },
    {
        .ml_name    = "createStructType",
        .ml_meth    = (PyCFunction)createStructType,
        .ml_flags   = METH_VARARGS|METH_KEYWORDS,
        .ml_doc     = createStructType_doc
    },
    {
        .ml_name    = "registerStructAlias",
        .ml_meth    = (PyCFunction)registerStructAlias,
        .ml_flags   = METH_VARARGS|METH_KEYWORDS,
        .ml_doc     = registerStructAlias_doc
    },
    {
        .ml_name    = "registerMetaDataForSelector",
        .ml_meth    = (PyCFunction)registerMetaData,
        .ml_flags   = METH_VARARGS|METH_KEYWORDS,
        .ml_doc     = registerMetaData_doc
    },
    {
        .ml_name    = "_copyMetadataRegistry",
        .ml_meth    = (PyCFunction)copyMetadataRegistry,
        .ml_flags   = METH_VARARGS|METH_KEYWORDS,
        .ml_doc     = copyMetadataRegistry_doc
    },
    {
        .ml_name    = "_updatingMetadata",
        .ml_meth    = (PyCFunction)_updatingMetadata,
        .ml_flags   = METH_VARARGS|METH_KEYWORDS,
        .ml_doc     = _updatingMetadata_doc
    },
    {
        .ml_name    = "_makeClosure",
        .ml_meth    = (PyCFunction)_makeClosure,
        .ml_flags   = METH_VARARGS|METH_KEYWORDS,
        .ml_doc     = _makeClosure_doc
    },
    {
        .ml_name    = "_closurePointer",
        .ml_meth    = (PyCFunction)_closurePointer,
        .ml_flags   = METH_VARARGS|METH_KEYWORDS,
        .ml_doc     = _closurePointer_doc
    },
    {
        .ml_name    = "_ivar_dict",
        .ml_meth    = (PyCFunction)ivar_dict,
        .ml_flags   = METH_NOARGS,
        .ml_doc     = "_ivar_dict()\n" CLINIC_SEP "\nPRIVATE FUNCTION\n"
    },
    {
        .ml_name    = "_objc_sync_enter",
        .ml_meth    = (PyCFunction)PyObjC_objc_sync_enter,
        .ml_flags   = METH_VARARGS,
        .ml_doc     = "_objc_sync_enter(object)\n" CLINIC_SEP "\nacquire mutex for an object"
    },
    {
        .ml_name    = "_objc_sync_exit",
        .ml_meth    = (PyCFunction)PyObjC_objc_sync_exit,
        .ml_flags   = METH_VARARGS,
        .ml_doc     = "_objc_sync_exit(object)\n" CLINIC_SEP "\nrelease mutex for an object"
    },
    {
        .ml_name    = "_block_call",
        .ml_meth    = (PyCFunction)PyObjCBlock_Call,
        .ml_flags   = METH_VARARGS,
        "_block_call(block, signature, args, kwds)\n" CLINIC_SEP "\nCall an Objective-C block"
    },
    {
        .ml_name    = "_block_signature",
        .ml_meth    = (PyCFunction)block_signature,
        .ml_flags   = METH_O,
        "_block_signature(block)\n" CLINIC_SEP "\nreturn signature string for a block, or None"
    },
    {
        .ml_name    = "_typestr2typestr",
        .ml_meth    = (PyCFunction)typestr2typestr,
        .ml_flags   = METH_O,
        .ml_doc     = "_typestr2typestr(value)\n" CLINIC_SEP "\nReturns the standard Objective-C version for a PyObjC typestr"
    },

#if    PyObjC_BUILD_RELEASE >= 1006

    {
        .ml_name    = "setAssociatedObject",
        .ml_meth    = (PyCFunction)PyObjC_setAssociatedObject,
        .ml_flags   = METH_VARARGS|METH_KEYWORDS,
        .ml_doc     = PyObjC_setAssociatedObject_doc
    },
    {
        .ml_name    = "getAssociatedObject",
        .ml_meth    = (PyCFunction)PyObjC_getAssociatedObject,
        .ml_flags   = METH_VARARGS|METH_KEYWORDS,
        .ml_doc     = PyObjC_getAssociatedObject_doc
    },
    {
        .ml_name    = "removeAssociatedObjects",
        .ml_meth    = (PyCFunction)PyObjC_removeAssociatedObjects,
        .ml_flags   = METH_VARARGS|METH_KEYWORDS,
        .ml_doc     = PyObjC_removeAssociatedObjects_doc
    },

#endif /* PyObjC_BUILD_RELEASE >= 1006 */

    {
        .ml_name    = "_loadConstant",
        .ml_meth    = (PyCFunction)PyObjC_LoadConstant,
        .ml_flags   = METH_VARARGS|METH_KEYWORDS,
        .ml_doc     = "_loadConstant(name, type, magic)\n" CLINIC_SEP "\nLoad a single C constant and return its value"
    },
    {
        .ml_name    = "_nameForSignature",
        .ml_meth    = (PyCFunction)name_for_signature,
        .ml_flags   = METH_O,
        .ml_doc     = "_nameForSignature(typestr)\n" CLINIC_SEP "\nReturn a pretty name for a PyObjC type string"
    },
    {
        .ml_name    = "_rescanClass",
        .ml_meth    = (PyCFunction)force_rescan,
        .ml_flags   = METH_VARARGS|METH_KEYWORDS,
        .ml_doc     = "_rescanClass(classObject)\n" CLINIC_SEP "\nForce a rescan of the method table of a class",
    },
    {
        .ml_name    = NULL /* SENTINEL */
    }
};

struct objc_typestr_values {
    char*    name;
    char    value;
} objc_typestr_values [] = {
    { "_C_ID", _C_ID },
    { "_C_CLASS", _C_CLASS },
    { "_C_SEL", _C_SEL },
    { "_C_CHR", _C_CHR },
    { "_C_UCHR", _C_UCHR },
    { "_C_SHT", _C_SHT },
    { "_C_USHT", _C_USHT },
#ifdef _C_BOOL
    { "_C_BOOL", _C_BOOL },
#endif
    { "_C_INT", _C_INT },
    { "_C_UINT", _C_UINT },
    { "_C_LNG", _C_LNG },
    { "_C_ULNG", _C_ULNG },
    { "_C_LNG_LNG", _C_LNG_LNG },
    { "_C_ULNG_LNG", _C_ULNG_LNG },
    { "_C_FLT", _C_FLT },
    { "_C_DBL", _C_DBL },
    { "_C_BFLD", _C_BFLD },
    { "_C_VOID", _C_VOID },
    { "_C_UNDEF", _C_UNDEF },
    { "_C_PTR", _C_PTR },
    { "_C_CHARPTR", _C_CHARPTR },
    { "_C_ARY_B", _C_ARY_B },
    { "_C_ARY_E", _C_ARY_E },
    { "_C_UNION_B", _C_UNION_B },
    { "_C_UNION_E", _C_UNION_E },
    { "_C_STRUCT_B", _C_STRUCT_B },
    { "_C_STRUCT_E", _C_STRUCT_E },
    { "_C_CONST", _C_CONST },
    { "_C_IN", _C_IN },
    { "_C_INOUT", _C_INOUT },
    { "_C_OUT", _C_OUT },
    { "_C_BYCOPY", _C_BYCOPY },
    { "_C_ONEWAY", _C_ONEWAY },

    /* Compatibility: */
    { "_C_LNGLNG", _C_LNG_LNG },
    { "_C_ULNGLNG", _C_ULNG_LNG },

    /* PyObjC specific */
    { "_C_NSBOOL",    _C_NSBOOL },
    { "_C_UNICHAR", _C_UNICHAR },
    { "_C_CHAR_AS_TEXT", _C_CHAR_AS_TEXT },
    { "_C_CHAR_AS_INT", _C_CHAR_AS_INT },

    { NULL, 0 }
};

#if PyObjC_BUILD_RELEASE < 1010
typedef struct {
    NSInteger majorVersion;
    NSInteger minorVersion;
    NSInteger patchVersion;
} NSOperatingSystemVersion;
#endif

static NSOperatingSystemVersion version_from_plist(void)
{
    NSOperatingSystemVersion result = { 0, 0, 0 };

    NSString *plistPath = @"/System/Library/CoreServices/SystemVersion.plist";
    NSDictionary* info = [NSDictionary dictionaryWithContentsOfFile:plistPath];

    NSString *versionString = [info objectForKey:@"ProductVersion"];
    if (versionString == NULL) {
        /* For some reason there is no version info key */
        return result;
    }

    NSArray *components = [versionString componentsSeparatedByString:@"."];
    NSUInteger cnt = [components count];

    result.majorVersion = [[components objectAtIndex:0] integerValue];
    result.minorVersion = (cnt > 1) ? [[components objectAtIndex:1] integerValue] : 0;
    result.patchVersion = (cnt > 2) ? [[components objectAtIndex:2] integerValue] : 0;

    return result;
}

static long get_macos_release(void)
{
    NSOperatingSystemVersion version;

    if ([NSProcessInfo instancesRespondToSelector:@selector(operatingSystemVersion)]) {
        version = (NSOperatingSystemVersion)[[NSProcessInfo processInfo] operatingSystemVersion];
    } else {
        version  = version_from_plist();
    }

    if (version.majorVersion == 10 && version.minorVersion <= 9) {
        return version.majorVersion * 100 + version.minorVersion;
    } else {
        return version.majorVersion * 10000 + version.minorVersion * 100 + version.patchVersion;
    }
}

PyObjC_MODULE_INIT(_objc)
{
    PyObject *m, *d, *v;

    if (PyObjC_Initialized) {
        PyErr_SetString(PyExc_RuntimeError,
            "Reload of objc._objc detected, this is not supported");
        PyObjC_INITERROR();
    }

    PyObjC_SetupRuntimeCompat();
    if (PyErr_Occurred()) {
        PyObjC_INITERROR();
    }

    NSAutoreleasePool *initReleasePool = [[NSAutoreleasePool alloc] init];
    [OC_NSBundleHack installBundleHack];

    PyObjCClass_DefaultModule = PyText_FromString("objc");

    if (PyObjC_InitProxyRegistry() < 0) {
        PyObjC_INITERROR();
    }

    PyObjC_TypeStr2CFTypeID = PyDict_New();
    if (PyObjC_TypeStr2CFTypeID == NULL) {
        PyObjC_INITERROR();
    }

    if (PyObjCBlock_Setup() == -1) {
        PyObjC_INITERROR();
    }

    if (PyType_Ready(&PyObjCFunc_Type) < 0) {
        PyObjC_INITERROR();
    }
    if (PyType_Ready(&PyObjCPointer_Type) < 0) {
        PyObjC_INITERROR();
    }
    if (PyType_Ready(&PyObjCMetaClass_Type) < 0) {
        PyObjC_INITERROR();
    }
    if (PyType_Ready(&PyObjCClass_Type) < 0) {
        PyObjC_INITERROR();
    }
    if (PyType_Ready((PyTypeObject*)&PyObjCObject_Type) < 0) {
        PyObjC_INITERROR();
    }
    if (PyType_Ready(&PyObjCSelector_Type) < 0) {
        PyObjC_INITERROR();
    }
    if (PyType_Ready(&PyObjCNativeSelector_Type) < 0) {
        PyObjC_INITERROR();
    }
    if (PyType_Ready(&PyObjCPythonSelector_Type) < 0) {
        PyObjC_INITERROR();
    }
    if (PyType_Ready(&PyObjCInstanceVariable_Type) < 0) {
        PyObjC_INITERROR();
    }
    if (PyType_Ready(&PyObjCInformalProtocol_Type) < 0) {
        PyObjC_INITERROR();
    }
    if (PyType_Ready(&PyObjCFormalProtocol_Type) < 0) {
        PyObjC_INITERROR();
    }
    if (PyType_Ready(&PyObjCUnicode_Type) < 0) {
        PyObjC_INITERROR();
    }
    if (PyType_Ready(&PyObjCIMP_Type) < 0) {
        PyObjC_INITERROR();
    }
    if (PyType_Ready(&PyObjCMethodAccessor_Type) < 0) {
        PyObjC_INITERROR();
    }
    if (PyType_Ready(&PyObjCMethodSignature_Type) < 0) {
        PyObjC_INITERROR();
    }
    if (PyType_Ready(&PyObjC_VarList_Type) < 0) {
        PyObjC_INITERROR();
    }
    if (PyType_Ready(&PyObjC_FSRefType) < 0) {
        PyObjC_INITERROR();
    }
    if (PyType_Ready(&PyObjC_FSSpecType) < 0) {
        PyObjC_INITERROR();
    }
    if (PyType_Ready(&PyObjCPythonMethod_Type) < 0) {
        PyObjC_INITERROR();
    }
    if (PyType_Ready(&StructBase_Type) < 0) {
        PyObjC_INITERROR();
    }

#ifndef Py_HAVE_LOCAL_LOOKUP
    PyObjCSuper_Type.tp_doc = PySuper_Type.tp_doc;
    PyObjCSuper_Type.tp_init = PySuper_Type.tp_init;
    PyObjCSuper_Type.tp_alloc = PySuper_Type.tp_alloc;
    PyObjCSuper_Type.tp_new = PySuper_Type.tp_new;
    PyObjCSuper_Type.tp_dealloc = PySuper_Type.tp_dealloc;
    PyObjCSuper_Type.tp_free = PySuper_Type.tp_free;
    PyObjCSuper_Type.tp_traverse = PySuper_Type.tp_traverse;
    if (PyType_Ready(&PyObjCSuper_Type) < 0) {
        PyObjC_INITERROR();
    }
#endif /* !Py_HAVE_LOCAL_LOOKUP */

#if PyObjC_BUILD_RELEASE >= 1007
    if (PyType_Ready(&PyObjCWeakRef_Type) < 0) {
        PyObjC_INITERROR();
    }
#endif /* PyObjC_BUILD_RELEASE >= 1007 */

    if (PyObjC_setup_nsdata() < 0) {
        PyObjC_INITERROR();
    }
    if (PyObjC_setup_nscoder() < 0) {
        PyObjC_INITERROR();
    }
    if (PyObjC_setup_nsobject() < 0) {
        PyObjC_INITERROR();
    }

    if (PyObjCCFType_Setup() == -1) {
        PyObjC_INITERROR();
    }

    m = PyObjC_MODULE_CREATE(_objc);
    if (m == 0) {
        PyObjC_INITERROR();
    }

    if (PyObjC_SetupOptions(m) < 0) {
        PyObjC_INITERROR();
    }

    if (PyObjC_setup_nsdecimal(m) < 0) {
        PyObjC_INITERROR();
    }


    d = PyModule_GetDict(m);
    if (d == 0) {
        PyObjC_INITERROR();
    }

    if (PyDict_SetItemString(d, "ObjCPointer", (PyObject*)&PyObjCPointer_Type) < 0) {
        PyObjC_INITERROR();
    }
    if (PyDict_SetItemString(d, "objc_meta_class", (PyObject*)&PyObjCMetaClass_Type) < 0) {
        PyObjC_INITERROR();
    }
    if (PyDict_SetItemString(d, "objc_class", (PyObject*)&PyObjCClass_Type) < 0) {
        PyObjC_INITERROR();
    }
    if (PyDict_SetItemString(d, "objc_object", (PyObject*)&PyObjCObject_Type) < 0) {
        PyObjC_INITERROR();
    }
    if (PyDict_SetItemString(d, "pyobjc_unicode", (PyObject*)&PyObjCUnicode_Type) < 0) {
        PyObjC_INITERROR();
    }
    if (PyDict_SetItemString(d, "selector", (PyObject*)&PyObjCSelector_Type) < 0) {
        PyObjC_INITERROR();
    }
    if (PyDict_SetItemString(d, "FSRef", (PyObject*)&PyObjC_FSRefType) < 0) {
        PyObjC_INITERROR();
    }
    if (PyDict_SetItemString(d, "FSSpec", (PyObject*)&PyObjC_FSSpecType) < 0) {
        PyObjC_INITERROR();
    }
    if (PyDict_SetItemString(d, "ivar", (PyObject*)&PyObjCInstanceVariable_Type) < 0) {
        PyObjC_INITERROR();
    }
    if (PyDict_SetItemString(d, "informal_protocol", (PyObject*)&PyObjCInformalProtocol_Type) < 0) {
        PyObjC_INITERROR();
    }
    if (PyDict_SetItemString(d, "formal_protocol", (PyObject*)&PyObjCFormalProtocol_Type) < 0) {
        PyObjC_INITERROR();
    }
    if (PyDict_SetItemString(d, "varlist", (PyObject*)&PyObjC_VarList_Type) < 0) {
        PyObjC_INITERROR();
    }
    if (PyDict_SetItemString(d, "function", (PyObject*)&PyObjCFunc_Type) < 0) {
        PyObjC_INITERROR();
    }
    if (PyDict_SetItemString(d, "IMP", (PyObject*)&PyObjCIMP_Type) < 0) {
        PyObjC_INITERROR();
    }
    if (PyDict_SetItemString(d, "python_method", (PyObject*)&PyObjCPythonMethod_Type) < 0) {
        PyObjC_INITERROR();
    }
    if (PyDict_SetItemString(d, "_structwrapper", (PyObject*)&StructBase_Type) < 0) {
        PyObjC_INITERROR();
    }

#ifndef Py_HAVE_LOCAL_LOOKUP
    if (PyDict_SetItemString(d, "super", (PyObject*)&PyObjCSuper_Type) < 0) {
        PyObjC_INITERROR();
    }
    if (PyDict_SetItemString(d, "_pep447", Py_False) < 0) {
        PyObjC_INITERROR();
    }
#else /* Py_HAVE_LOCAL_LOOKUP */
    if (PyDict_SetItemString(d, "super", (PyObject*)&PySuper_Type) < 0) {
        PyObjC_INITERROR();
    }
    if (PyDict_SetItemString(d, "_pep447", Py_True) < 0) {
        PyObjC_INITERROR();
    }
#endif /* Py_HAVE_LOCAL_LOOKUP */


#if PyObjC_BUILD_RELEASE >= 1007
    if (&objc_loadWeak != NULL) {
        if (PyDict_SetItemString(d, "WeakRef", (PyObject*)&PyObjCWeakRef_Type) < 0) {
            PyObjC_INITERROR();
        }
    }
#endif /* PyObjC_BUILD_RELEASE >= 1007 */

    v = PyObjCInitNULL();
    if (v == NULL) {
        PyObjC_INITERROR();
    }

    if (PyDict_SetItemString(d, "NULL", v) < 0) {
        Py_DECREF(v);
        PyObjC_INITERROR();
    }
    Py_DECREF(v);

    if (PyObjCUtil_Init(m) < 0) {
        PyObjC_INITERROR();
    }
    if (PyObjCAPI_Register(m) < 0) {
        PyObjC_INITERROR();
    }
    if (PyObjCIMP_SetUpMethodWrappers() < 0) {
        PyObjC_INITERROR();
    }
    if (PyObjC_init_ctests(m) < 0) {
        PyObjC_INITERROR();
    }


#if PY_MAJOR_VERSION == 2
    PyObjCStrBridgeWarning = PyErr_NewException("objc.PyObjCStrBridgeWarning", PyExc_DeprecationWarning, NULL);
    PyModule_AddObject(m, "PyObjCStrBridgeWarning", PyObjCStrBridgeWarning);
#endif

    {
        struct objc_typestr_values* cur = objc_typestr_values;

        for (; cur->name != NULL; cur ++) {
            PyObject* t = PyBytes_FromStringAndSize(&cur->value, 1);
            if (t == NULL) {
                PyObjC_INITERROR();
            }
            if (PyModule_AddObject(m, cur->name, t)) {
                PyObjC_INITERROR();
            }
        }
    }

    /* Add _C_CFTYPEID to avoid hardcoding this in our python code */
    if (PyModule_AddObject(m, "_C_CFTYPEID", PyBytes_FromString(@encode(CFTypeID))) < 0) {
        PyObjC_INITERROR();
    }

    /* Likewise for _C_NSInteger and _C_NSUInteger */
    if (PyModule_AddObject(m, "_C_NSInteger", PyBytes_FromString(@encode(NSInteger))) < 0) {
        PyObjC_INITERROR();
    }
    if (PyModule_AddObject(m, "_C_NSUInteger", PyBytes_FromString(@encode(NSUInteger))) < 0) {
        PyObjC_INITERROR();
    }
    if (PyModule_AddObject(m, "_C_CFIndex", PyBytes_FromString(@encode(CFIndex))) < 0) {
        PyObjC_INITERROR();
    }
    if (PyModule_AddObject(m, "_C_CGFloat", PyBytes_FromString(@encode(CGFloat))) < 0) {
        PyObjC_INITERROR();
    }
    if (PyModule_AddObject(m, "_C_FSRef", PyBytes_FromString(@encode(FSRef))) < 0) {
        PyObjC_INITERROR();
    }
    if (PyModule_AddIntConstant(m, "_size_sockaddr_ip4", sizeof(struct sockaddr_in)) < 0) {
        PyObjC_INITERROR();
    }
    if (PyModule_AddIntConstant(m, "_size_sockaddr_ip6", sizeof(struct sockaddr_in6)) < 0) {
        PyObjC_INITERROR();
    }
    if (PyModule_AddStringConstant(m, "__version__", OBJC_VERSION) < 0) {
        PyObjC_INITERROR();
    }

    if (PyModule_AddObject(m, "_sockaddr_type", PyBytes_FromString(@encode(struct sockaddr))) < 0) {
        PyObjC_INITERROR();
    }

    PyObjCPointerWrapper_Init();

#if PyObjC_BUILD_RELEASE >= 1006
#if MAC_OS_X_VERSION_MIN_REQUIRED < MAC_OS_X_VERSION_10_6
    if (objc_setAssociatedObject != NULL) {
#endif /* MAC_OS_X_VERSION_MIN_REQUIRED < MAC_OS_X_VERSION_10_6 */
        if (PyModule_AddIntConstant(m, "OBJC_ASSOCIATION_ASSIGN", OBJC_ASSOCIATION_ASSIGN) < 0) {
            PyObjC_INITERROR();
        }
        if (PyModule_AddIntConstant(m, "OBJC_ASSOCIATION_RETAIN_NONATOMIC", OBJC_ASSOCIATION_RETAIN_NONATOMIC) < 0) {
            PyObjC_INITERROR();
        }
        if (PyModule_AddIntConstant(m, "OBJC_ASSOCIATION_COPY_NONATOMIC", OBJC_ASSOCIATION_COPY_NONATOMIC) < 0) {
            PyObjC_INITERROR();
        }
        if (PyModule_AddIntConstant(m, "OBJC_ASSOCIATION_RETAIN", OBJC_ASSOCIATION_RETAIN) < 0) {
            PyObjC_INITERROR();
        }
        if (PyModule_AddIntConstant(m, "OBJC_ASSOCIATION_COPY", OBJC_ASSOCIATION_COPY) < 0) {
            PyObjC_INITERROR();
        }
#if MAC_OS_X_VERSION_MIN_REQUIRED < MAC_OS_X_VERSION_10_6
    } else {
        /* Build on a system where object associations are available, running on a platform where they aren't.
         * Disable the wrappers.
         */
        if (PyDict_DelItemString(d, "setAssociatedObject") < 0) {
            PyErr_Clear();
        }
        if (PyDict_DelItemString(d, "getAssociatedObject") < 0) {
            PyErr_Clear();
        }
        if (PyDict_DelItemString(d, "removeAssociatedObjects") < 0) {
            PyErr_Clear();
        }

    }
#endif /* MAC_OS_X_VERSION_MIN_REQUIRED < MAC_OS_X_VERSION_10_6 */
#endif /* PyObjC_BUILD_RELEASE >= 1006 */



#ifdef MAC_OS_X_VERSION_MAX_ALLOWED
    /* An easy way to check for the MacOS X version we did build for */
    if (PyModule_AddIntConstant(m, "MAC_OS_X_VERSION_MAX_ALLOWED", MAC_OS_X_VERSION_MAX_ALLOWED) < 0) {
        PyObjC_INITERROR();
    }
#endif /* MAC_OS_X_VERSION_MAX_ALLOWED */

#ifdef MAC_OS_X_VERSION_MIN_REQUIRED
    if (PyModule_AddIntConstant(m, "MAC_OS_X_VERSION_MIN_REQUIRED", MAC_OS_X_VERSION_MAX_ALLOWED) < 0) {
        PyObjC_INITERROR();
    }
#endif /* MAC_OS_X_VERSION_MIN_REQUIRED */

#ifdef MAC_OS_X_VERSION_10_0
    if (PyModule_AddIntConstant(m, "MAC_OS_X_VERSION_10_0", MAC_OS_X_VERSION_10_0) < 0) {
        PyObjC_INITERROR();
    }
#endif /* MAC_OS_X_VERSION_10_0 */

#ifdef MAC_OS_X_VERSION_10_1
    if (PyModule_AddIntConstant(m, "MAC_OS_X_VERSION_10_1", MAC_OS_X_VERSION_10_1) < 0) {
        PyObjC_INITERROR();
    }
#endif /* MAC_OS_X_VERSION_10_1 */

#ifdef MAC_OS_X_VERSION_10_2
    if (PyModule_AddIntConstant(m, "MAC_OS_X_VERSION_10_2", MAC_OS_X_VERSION_10_2) < 0) {
        PyObjC_INITERROR();
    }
#endif /* MAC_OS_X_VERSION_10_2 */

#ifdef MAC_OS_X_VERSION_10_3
    if (PyModule_AddIntConstant(m, "MAC_OS_X_VERSION_10_3", MAC_OS_X_VERSION_10_3) < 0) {
        PyObjC_INITERROR();
    }
#endif /* MAC_OS_X_VERSION_10_3 */

#ifdef MAC_OS_X_VERSION_10_4
    if (PyModule_AddIntConstant(m, "MAC_OS_X_VERSION_10_4", MAC_OS_X_VERSION_10_4) < 0) {
        PyObjC_INITERROR();
    }
#endif /* MAC_OS_X_VERSION_10_4 */

#ifdef MAC_OS_X_VERSION_10_5
    if (PyModule_AddIntConstant(m, "MAC_OS_X_VERSION_10_5", MAC_OS_X_VERSION_10_5) < 0) {
        PyObjC_INITERROR();
    }
#endif /* MAC_OS_X_VERSION_10_5 */

#ifdef MAC_OS_X_VERSION_10_6
    if (PyModule_AddIntConstant(m, "MAC_OS_X_VERSION_10_6", MAC_OS_X_VERSION_10_6) < 0) {
        PyObjC_INITERROR();
    }
#endif /* MAC_OS_X_VERSION_10_6 */

#ifdef MAC_OS_X_VERSION_10_7
    if (PyModule_AddIntConstant(m, "MAC_OS_X_VERSION_10_7", MAC_OS_X_VERSION_10_7) < 0) {
        PyObjC_INITERROR();
    }
#endif /* MAC_OS_X_VERSION_10_7 */

#ifdef MAC_OS_X_VERSION_10_8
    if (PyModule_AddIntConstant(m, "MAC_OS_X_VERSION_10_8", MAC_OS_X_VERSION_10_8) < 0) {
        PyObjC_INITERROR();
    }
#endif /* MAC_OS_X_VERSION_10_8 */

#ifdef MAC_OS_X_VERSION_10_9
    if (PyModule_AddIntConstant(m, "MAC_OS_X_VERSION_10_9", MAC_OS_X_VERSION_10_9) < 0) {
        PyObjC_INITERROR();
    }
#endif /* MAC_OS_X_VERSION_10_9 */

#ifdef MAC_OS_X_VERSION_10_10
    if (PyModule_AddIntConstant(m, "MAC_OS_X_VERSION_10_10", MAC_OS_X_VERSION_10_10) < 0) {
        PyObjC_INITERROR();
    }
#endif /* MAC_OS_X_VERSION_10_10 */

#ifdef MAC_OS_X_VERSION_10_10_2
    if (PyModule_AddIntConstant(m, "MAC_OS_X_VERSION_10_10_2", MAC_OS_X_VERSION_10_10_2) < 0) {
        PyObjC_INITERROR();
    }
#endif /* MAC_OS_X_VERSION_10_10_2 */

#ifdef MAC_OS_X_VERSION_10_10_3
    if (PyModule_AddIntConstant(m, "MAC_OS_X_VERSION_10_10_3", MAC_OS_X_VERSION_10_10_3) < 0) {
        PyObjC_INITERROR();
    }
#endif /* MAC_OS_X_VERSION_10_10_3 */

#ifdef MAC_OS_X_VERSION_10_11
    if (PyModule_AddIntConstant(m, "MAC_OS_X_VERSION_10_11", MAC_OS_X_VERSION_10_11) < 0) {
        PyObjC_INITERROR();
    }
#endif /* MAC_OS_X_VERSION_10_11 */

#ifdef MAC_OS_X_VERSION_10_11_2
    if (PyModule_AddIntConstant(m, "MAC_OS_X_VERSION_10_11_2", MAC_OS_X_VERSION_10_11_2) < 0) {
        PyObjC_INITERROR();
    }
#endif /* MAC_OS_X_VERSION_10_11_2 */

#ifdef MAC_OS_X_VERSION_10_11_3
    if (PyModule_AddIntConstant(m, "MAC_OS_X_VERSION_10_11_3", MAC_OS_X_VERSION_10_11_3) < 0) {
        PyObjC_INITERROR();
    }
#endif /* MAC_OS_X_VERSION_10_11_3 */

#ifdef MAC_OS_X_VERSION_10_11_4
    if (PyModule_AddIntConstant(m, "MAC_OS_X_VERSION_10_11_4", MAC_OS_X_VERSION_10_11_4) < 0) {
        PyObjC_INITERROR();
    }
#endif /* MAC_OS_X_VERSION_10_11_4 */

#ifdef MAC_OS_X_VERSION_10_12
    if (PyModule_AddIntConstant(m, "MAC_OS_X_VERSION_10_12", MAC_OS_X_VERSION_10_12) < 0) {
        PyObjC_INITERROR();
    }
#endif /* MAC_OS_X_VERSION_10_12 */

#ifdef MAC_OS_X_VERSION_10_12_1
    if (PyModule_AddIntConstant(m, "MAC_OS_X_VERSION_10_12_1", MAC_OS_X_VERSION_10_12_1) < 0) {
        PyObjC_INITERROR();
    }
#endif /* MAC_OS_X_VERSION_10_12_1 */

#ifdef MAC_OS_X_VERSION_10_12_2
    if (PyModule_AddIntConstant(m, "MAC_OS_X_VERSION_10_12_2", MAC_OS_X_VERSION_10_12_2) < 0) {
        PyObjC_INITERROR();
    }
#endif /* MAC_OS_X_VERSION_10_12_2 */

#ifdef MAC_OS_X_VERSION_10_12_4
    if (PyModule_AddIntConstant(m, "MAC_OS_X_VERSION_10_12_4", MAC_OS_X_VERSION_10_12_4) < 0) {
        PyObjC_INITERROR();
    }
#endif /* MAC_OS_X_VERSION_10_12_4 */

#ifdef MAC_OS_X_VERSION_10_13
    if (PyModule_AddIntConstant(m, "MAC_OS_X_VERSION_10_13", MAC_OS_X_VERSION_10_13) < 0) {
        PyObjC_INITERROR();
    }
#endif /* MAC_OS_X_VERSION_10_13 */

#ifdef MAC_OS_X_VERSION_10_13_1
    if (PyModule_AddIntConstant(m, "MAC_OS_X_VERSION_10_13_1", MAC_OS_X_VERSION_10_13_1) < 0) {
        PyObjC_INITERROR();
    }
#endif /* MAC_OS_X_VERSION_10_13_1 */

#ifdef MAC_OS_X_VERSION_10_13_2
    if (PyModule_AddIntConstant(m, "MAC_OS_X_VERSION_10_13_2", MAC_OS_X_VERSION_10_13_2) < 0) {
        PyObjC_INITERROR();
    }
#endif /* MAC_OS_X_VERSION_10_13_2 */

#ifdef MAC_OS_X_VERSION_10_13_3
    if (PyModule_AddIntConstant(m, "MAC_OS_X_VERSION_10_13_3", MAC_OS_X_VERSION_10_13_3) < 0) {
        PyObjC_INITERROR();
    }
#endif /* MAC_OS_X_VERSION_10_13_3 */

#ifdef MAC_OS_X_VERSION_10_13_4
    if (PyModule_AddIntConstant(m, "MAC_OS_X_VERSION_10_13_4", MAC_OS_X_VERSION_10_13_4) < 0) {
        PyObjC_INITERROR();
    }
#endif /* MAC_OS_X_VERSION_10_13_4 */

#ifdef MAC_OS_X_VERSION_10_13_5
    if (PyModule_AddIntConstant(m, "MAC_OS_X_VERSION_10_13_5", MAC_OS_X_VERSION_10_13_5) < 0) {
        PyObjC_INITERROR();
    }
#endif /* MAC_OS_X_VERSION_10_13_5 */

#ifdef MAC_OS_X_VERSION_10_13_6
    if (PyModule_AddIntConstant(m, "MAC_OS_X_VERSION_10_13_6", MAC_OS_X_VERSION_10_13_6) < 0) {
        PyObjC_INITERROR();
    }
#endif /* MAC_OS_X_VERSION_10_13_6 */

#ifdef MAC_OS_X_VERSION_10_14
    if (PyModule_AddIntConstant(m, "MAC_OS_X_VERSION_10_14", MAC_OS_X_VERSION_10_14) < 0) {
        PyObjC_INITERROR();
    }
#endif /* MAC_OS_X_VERSION_10_14 */

    if (PyModule_AddIntConstant(m, "MAC_OS_X_VERSION_CURRENT", get_macos_release()) < 0) {
        PyObjC_INITERROR();
    }

    if (PyModule_AddIntConstant(m, "PyObjC_BUILD_RELEASE", PyObjC_BUILD_RELEASE) < 0) {
        PyObjC_INITERROR();
    }

    if (PyModule_AddIntConstant(m, "_NSNotFound", NSNotFound) < 0) {
        PyObjC_INITERROR();
    }


    if ((v = PyFloat_FromDouble(FLT_MIN)) == NULL) {
        PyObjC_INITERROR();
    }
    if (PyModule_AddObject(m, "_FLT_MIN", v) < 0) {
        PyObjC_INITERROR();
    }

    if ((v = PyFloat_FromDouble(FLT_MAX)) == NULL) {
        PyObjC_INITERROR();
    }
    if (PyModule_AddObject(m, "_FLT_MAX", v) < 0) {
        PyObjC_INITERROR();
    }

    if (PyModule_AddStringConstant(m, "platform", "MACOSX") < 0) {
        PyObjC_INITERROR();
    }

    PyEval_InitThreads();
    if (![NSThread isMultiThreaded]) {
        [NSThread detachNewThreadSelector:@selector(targetForBecomingMultiThreaded:) toTarget:[OC_NSAutoreleasePoolCollector class] withObject:nil];
    }

    [initReleasePool release];
    /* Allocate an auto-release pool for our own use, this avoids numerous
     * warnings during startup of a python script.
     */
    global_release_pool = [[NSAutoreleasePool alloc] init];
    [OC_NSAutoreleasePoolCollector newAutoreleasePool];

#ifndef Py_ARG_BYTES
#error "No Py_ARG_BYTES"
#endif

#ifndef Py_ARG_NSInteger
#error "No Py_ARG_NSInteger"
#endif

#ifndef Py_ARG_NSUInteger
#error "No Py_ARG_NSUInteger"
#endif

#if PY_MAJOR_VERSION == 3
    /*
     * Archives created with Python 2.x can contain instances of OC_PythonString,
     * use OC_PythonUnicode to decode.
     */
    [NSUnarchiver decodeClassName:@"OC_PythonString" asClassName:@"OC_PythonUnicode"];
#endif /* PY_MAJOR_VERSION == 3 */

    PyObjC_Initialized = 1;
    PyObjC_INITDONE();
}
