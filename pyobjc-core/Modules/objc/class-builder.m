/*
 * This file contains the code that is used to create proxy-classes for Python
 * classes in the objective-C runtime.
 */
#include "pyobjc.h"

#import <Foundation/NSInvocation.h>

NS_ASSUME_NONNULL_BEGIN

/* Special methods for Python subclasses of Objective-C objects */
static void object_method_dealloc(ffi_cif* cif, void* retval, void** args, void* userarg);
static void object_method_forwardInvocation(ffi_cif* cif, void* retval, void** args,
                                            void* userarg);
static void object_method_valueForKey_(ffi_cif* cif, void* retval, void** args,
                                       void* userarg);
static void object_method_setValue_forKey_(ffi_cif* cif, void* retval, void** args,
                                           void* userarg);
static void object_method_copyWithZone_(ffi_cif* cif, void* resp, void** args,
                                        void* userdata);

struct method_info {
    SEL         selector;
    const char* sel_name;
    const char* method_name;
    const char* typestr;
    void (*func)(ffi_cif*, void*, void**, void*);
    BOOL override_only;

} gMethods[] = {
    /* Keep in sync with Lib/objc/_transform.py:HELPER_METHODS */

    {0, "dealloc", "dealloc", "v@:", object_method_dealloc, NO},
    {0, "storedValueForKey:", "storedValueForKey_", "@@:@", object_method_valueForKey_,
     NO},
    {0, "valueForKey:", "valueForKey_", "@@:@", object_method_valueForKey_, NO},
    {0, "takeStoredValue:forKey:", "takeStoredValue_forKey_", "v@:@@",
     object_method_setValue_forKey_, NO},
    {0, "takeValue:forKey:", "takeValue_forKey_", "v@:@@", object_method_setValue_forKey_,
     NO},
    {0, "setValue:forKey:", "setValue_forKey_", "v@:@@", object_method_setValue_forKey_,
     NO},
    {0, "forwardInvocation:", "forwardInvocation_", "v@:@",
     object_method_forwardInvocation, NO},
    {0, "copyWithZone:", "copyWithZone_", "@@:^{_NSZone=}", object_method_copyWithZone_,
     YES},
    {0, "mutableCopyWithZone:", "mutableCopyWithZone_", "@@:^{_NSZone=}",
     object_method_copyWithZone_, YES},

    {0, 0, 0, 0, 0, 0}};

#define IDENT_CHARS "ABCDEFGHIJKLMNOPQSRTUVWXYZabcdefghijklmnopqrstuvwxyz_0123456789"

/*
 * XXX: Move this to module setup
 */
static void
setup_gMethods_selectors(void)
{
    for (struct method_info* cur = gMethods; cur->method_name != NULL; cur++) {
        if (cur->selector == NULL) {
            cur->selector = sel_registerName(cur->sel_name);
        }
    }
}

/*
 * Last step of the construction a python subclass of an objective-C class.
 *
 * Set reference to the python half in the objective-C half of the class.
 *
 * Return 0 on success, -1 on failure.
 */
int
PyObjCClass_FinishClass(Class objc_class)
{
    PyObjC_Assert(objc_class != nil, -1);

    objc_registerClassPair(objc_class);
    return 0;
}

/*
 * Call this when the python half of the class could not be created.
 *
 * Due to technical restrictions it is not allowed to unbuild a class that
 * is already registered with the Objective-C runtime.
 */
int
PyObjCClass_UnbuildClass(Class objc_class __attribute__((__unused__)))
{
    PyObjC_Assert(objc_class != nil, -1);
    PyObjC_Assert(objc_lookUpClass(class_getName(objc_class)) == nil, -1);

    objc_disposeClassPair(objc_class);
    return 0;
}

/*
 * Built a (pure Objective-C) subclass of base_class that
 * inserts a number of special values. The intermediate class
 * is used when the Python subclasses overrides those
 * methods.
 */

static Class _Nullable build_intermediate_class(Class base_class, char* name)
{
    Class intermediate_class = nil;

    intermediate_class = objc_allocateClassPair(base_class, name, 0);
    if (intermediate_class == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_NoMemory();
        goto error_cleanup;
        // LCOV_EXCL_STOP
    }

    setup_gMethods_selectors();
    for (struct method_info* cur = gMethods; cur->method_name != NULL; cur++) {
        if (cur->override_only) {
            if (![base_class instancesRespondToSelector:cur->selector]) {
                continue;
            }
        }
        PyObjCMethodSignature* methinfo =
            PyObjCMethodSignature_WithMetaData(cur->typestr, NULL, NO);
        if (methinfo == NULL)   // LCOV_BR_EXCL_LINE
            goto error_cleanup; // LCOV_EXCL_LINE
        IMP closure = PyObjCFFI_MakeClosure(methinfo, cur->func, intermediate_class);
        Py_CLEAR(methinfo);
        if (closure == NULL)    // LCOV_BR_EXCL_LINE
            goto error_cleanup; // LCOV_EXCL_LINE

        class_addMethod(intermediate_class, cur->selector, (IMP)closure, cur->typestr);
        closure = NULL;
    }

    objc_registerClassPair(intermediate_class);
    return (Class)intermediate_class;

error_cleanup:
    // LCOV_EXCL_START
    if (intermediate_class) {
        objc_disposeClassPair(intermediate_class);
    }

    return Nil;
    // LCOV_EXCL_STOP
}

/*
 * First step of creating a python subclass of an objective-C class
 *
 * Returns NULL or the newly created objective-C class. 'class_dict' may
 * be modified by this function.
 *
 * TODO:
 * - Set 'sel_class' of PyObjCPythonSelector instances
 * - This function complete ignores other base-classes, even though they
 *   might override methods. Need to check the MRO documentation to check
 *   if this is a problem.
 * - It is a problem when the user tries to use mixins to define common
 *   methods (like a NSTableViewDataSource mixin), this works but slowly
 *   because this calls will always be resolved through forwardInvocation:
 * - Add an 'override' flag that makes it possible to replace an existing
 *   PyObjC class, feature request for the Python-IDE  (write class, run,
 *   oops this doesn't work, rewrite class, reload and continue testing in
 *   the running app)
 */

static int
is_ivar(PyObject* value)
{
    return PyObjCInstanceVariable_Check(value);
}

static int
is_instance_method(PyObject* value)
{
    if (PyBytes_Check(value)) {
        return 1;
    }
    if (!PyObjCSelector_Check(value)) {
        return 0;
    }
    if (PyObjCNativeSelector_Check(value)) {
        return 0;
    }
    return !PyObjCSelector_IsClassMethod(value);
}

static int
is_class_method(PyObject* value)
{
    if (PyBytes_Check(value)) {
        return 1;
    }
    if (!PyObjCSelector_Check(value)) {
        return 0;
    }
    if (PyObjCNativeSelector_Check(value)) {
        return 0;
    }
    return PyObjCSelector_IsClassMethod(value);
}

static int
validate_tuple(PyObject* value, int (*validate)(PyObject*), const char* message)
{
    Py_ssize_t i, len;
    if (!PyTuple_Check(value)) {
        PyErr_SetString(PyObjCExc_InternalError, message);
        return -1;
    }
    len = PyTuple_GET_SIZE(value);
    for (i = 0; i < len; i++) {
        PyObject* item = PyTuple_GET_ITEM(value, i);
        if (!validate(item)) {
            PyErr_SetString(PyObjCExc_InternalError, message);
            return -1;
        }
    }
    return 0;
}

Class _Nullable PyObjCClass_BuildClass(Class super_class, PyObject* protocols, char* name,
                                       PyObject* class_dict, PyObject* meta_dict,
                                       PyObject* hiddenSelectors,
                                       PyObject* hiddenClassSelectors,
                                       int* has_dunder_new)
{
    PyObject*  value = NULL;
    Py_ssize_t i;
    Py_ssize_t protocol_count     = 0;
    Class      new_class          = NULL;
    Class      new_meta_class     = NULL;
    PyObject*  py_superclass      = NULL;
    PyObject*  instance_variables = NULL;
    PyObject*  instance_methods   = NULL;
    PyObject*  class_methods      = NULL;

    PyObjC_Assert(super_class != Nil, Nil);
    PyObjC_Assert(PyList_Check(protocols), Nil);
    PyObjC_Assert(PyDict_Check(class_dict), Nil);

    if (objc_lookUpClass(name) != NULL) {
        PyErr_Format(PyObjCExc_Error, "%s is overriding existing Objective-C class",
                     name);
        return Nil;
    }

    if (strspn(name, IDENT_CHARS) != strlen(name)) {
        PyErr_Format(PyObjCExc_Error, "'%s' not a valid Objective-C class name", name);
        return Nil;
    }

    py_superclass = PyObjCClass_New(super_class);
    if (py_superclass == NULL) { // LCOV_BR_EXCL_LINE
        return Nil;              // LCOV_EXCL_LINE
    }

    if (PyObjC_processClassDict == NULL || PyObjC_processClassDict == Py_None) {
        PyErr_SetString(
            PyObjCExc_InternalError,
            "Cannot create class because 'objc.options._processClassDict' is not set");
        goto error_cleanup;
    }
    PyObject* py_name = PyUnicode_FromString(name);
    if (py_name == NULL) {
        goto error_cleanup;
    }
    PyObject* args[] = {NULL,      py_name, class_dict,      meta_dict,           py_superclass,
                        protocols, hiddenSelectors, hiddenClassSelectors};
    PyObject* rv     = PyObject_Vectorcall(PyObjC_processClassDict, args + 1,
                                           7 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
    Py_DECREF(py_name);
    if (rv == NULL) {
        goto error_cleanup;
    }
    if (!PyTuple_Check(rv) || PyTuple_GET_SIZE(rv) != 4) {
        Py_DECREF(rv);
        PyErr_SetString(
            PyObjCExc_InternalError,
            "'objc.options._processClassDict' did not return a tuple of 3 items");
        goto error_cleanup;
    }
    instance_variables = PyTuple_GET_ITEM(rv, 0);
    Py_INCREF(instance_variables);
    instance_methods = PyTuple_GET_ITEM(rv, 1);
    Py_INCREF(instance_methods);
    class_methods = PyTuple_GET_ITEM(rv, 2);
    Py_INCREF(class_methods);
    *has_dunder_new = PyObject_IsTrue(PyTuple_GET_ITEM(rv, 3));
    Py_DECREF(rv);
    PyObjC_Assert(instance_variables != NULL, Nil);
    PyObjC_Assert(instance_methods != NULL, Nil);
    PyObjC_Assert(class_methods != NULL, Nil);
    if (validate_tuple(instance_variables, is_ivar,
                       "invalid instance_variables in result of class dict transformer")
        == -1) {
        goto error_cleanup;
    }
    if (validate_tuple(instance_methods, is_instance_method,
                       "invalid instance_methods in result of class dict transformer")
        == -1) {
        goto error_cleanup;
    }
    if (validate_tuple(class_methods, is_class_method,
                       "invalid class_methods in result of class dict transformer")
        == -1) {
        goto error_cleanup;
    }

    /*
     * A number of methods need to be implemented by PyObjC, but it should
     * also be possible to implement these in Python. Because of this
     * the bridge always introduces an intermediate class between the
     * Objective-C class and the first generation Python class.
     */
    if (!PyObjCClass_HasPythonImplementation(py_superclass)) {
        Class intermediate_class;
        char  buf[256];
        int   r;

        r = snprintf(buf, sizeof(buf), "_PyObjCIntermediate_%s",
                     class_getName(super_class));
        if (r < 0 || r >= (int)sizeof(buf)) { // LCOV_BR_EXCL_LINE
            /* Formatting the name failed, which is unlikely to happen */
            // LCOV_EXCL_START
            PyErr_SetString(PyObjCExc_InternalError,
                            "Cannot calculate name of intermediate class");
            goto error_cleanup;
            // LCOV_EXCL_STOP
        }

        intermediate_class = objc_lookUpClass(buf);
        if (intermediate_class == NULL) {
            intermediate_class = build_intermediate_class(super_class, buf);
            if (intermediate_class == Nil) { // LCOV_BR_EXCL_LINE
                /* build_intermediate_class can only fail when
                 * running out of resources.
                 */
                goto error_cleanup; // LCOV_EXCL_LINE
            }
        }
        Py_DECREF(py_superclass);

        super_class   = intermediate_class;
        py_superclass = PyObjCClass_New(super_class);
        if (py_superclass == Nil) { // LCOV_BR_EXCL_LINE
            goto error_cleanup;     // LCOV_EXCL_LINE
        }
    }

    /* Allocate the class as soon as possible, for new selector objects */
    new_class = objc_allocateClassPair(super_class, name, 0);
    if (new_class == Nil) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_Format(PyObjCExc_Error, "Cannot allocateClassPair for %s", name);
        goto error_cleanup;
        // LCOV_EXCL_STOP
    }

    /* Class is only Nil if new_class is nil */
    new_meta_class = (Class _Nonnull)object_getClass(new_class);

    /* 0th round: protocols */
    protocol_count = PyList_Size(protocols);
    if (protocol_count == -1) { // LCOV_BR_EXCL_LINE
        goto error_cleanup;     // LCOV_EXCL_LINE
    }
    for (i = 0; i < protocol_count; i++) {
        PyObject* wrapped_protocol;
        wrapped_protocol = PyList_GET_ITEM(protocols, i);
        if (!PyObjCFormalProtocol_Check(wrapped_protocol)) {
            continue;
        }

        /* PyObjCFormalProtocol_GetProtocol() is nonnull because we've already type
         * checked */
        if (!class_addProtocol( // LCOV_BR_EXCL_LINE
                new_class,
                (Protocol* _Nonnull)PyObjCFormalProtocol_GetProtocol(wrapped_protocol))) {
            goto error_cleanup; // LCOV_EXCL_LINE
        }
    }

    /* add instance variables */
    for (i = 0; i < PyTuple_GET_SIZE(instance_variables); i++) {
        value = PyTuple_GET_ITEM(instance_variables, i);

        if (!PyObjCInstanceVariable_Check(value)) { // LCOV_BR_EXCL_LINE
            continue;                               // LCOV_EXCL_LINE
        }

        char*      type;
        Py_ssize_t size;
        Py_ssize_t align;

        if (PyObjCInstanceVariable_IsSlot(value)) {
            type = @encode(PyObject*);
            size = sizeof(PyObject*);
        } else {
            type = PyObjCInstanceVariable_GetType(value);
            if (type == NULL) { // LCOV_BR_EXCL_LINE
                /* XXX: check if this can happen */
                // LCOV_EXCL_START
                PyErr_SetString(PyObjCExc_InternalError,
                                "got instance variable without a type");
                goto error_cleanup;
                // LCOV_EXCL_STOP
            }
            size = PyObjCRT_SizeOfType(type);
            if (size == -1) { // LCOV_BR_EXCL_LINE
                /* This cannot happen, the ivar.__init__ method
                 * checks that the encoding is valid.
                 */
                goto error_cleanup; // LCOV_EXCL_LINE
            }
        }
        align = PyObjCRT_AlignOfType(type);
        if (align == -1) {      // LCOV_BR_EXCL_LINE
            goto error_cleanup; // LCOV_EXCL_LINE
        }

        if (PyObjCInstanceVariable_GetName(value) == NULL) {
            PyErr_SetString(PyObjCExc_Error, "instance variable without a name");
            goto error_cleanup;
        }

        if (!class_addIvar( // LCOV_BR_EXCL_LINE
                new_class, PyObjCInstanceVariable_GetName(value), size, align, type)) {
            /* class_addIvar should never fail with the checks we've done
             * earlier.
             */
            goto error_cleanup; // LCOV_EXCL_LINE
        }
    }

    /* instance methods */
    for (i = 0; i < PyTuple_GET_SIZE(instance_methods); i++) {
        value = PyTuple_GET_ITEM(instance_methods, i);

        if (!PyObjCSelector_Check(value)) {
            continue;
        }

        /* Make sure that the selector is bound to the newly created class */
        ((PyObjCSelector*)value)->sel_class = new_class;

        Method meth;
        int    is_override = 0;
        IMP    imp;

        meth = class_getInstanceMethod(super_class, PyObjCSelector_GetSelector(value));
        if (meth) {
            is_override               = 1;
            const char* meth_encoding = method_getTypeEncoding(meth);
            if (meth_encoding == NULL) { // LCOV_BR_EXCL_LINE
                /* method_getTypeEncoding should only return NULL when
                 * meth is NULL.
                 */
                // LCOV_EXCL_START
                PyErr_Format(PyObjCExc_BadPrototypeError,
                             "%R cannot determine super_class type encoding", value);
                goto error_cleanup;
                // LCOV_EXCL_STOP
            }

            if (!PyObjCRT_SignaturesEqual(meth_encoding,
                                          PyObjCSelector_GetNativeSignature(value))) {

                PyErr_Format(
                    PyObjCExc_BadPrototypeError,
                    "%R has signature that is not compatible with super-class: %s != %s",
                    value, meth_encoding, PyObjCSelector_GetNativeSignature(value));
                goto error_cleanup;
            }
        }

        if (is_override) {
            imp = PyObjC_MakeIMP(new_class, super_class, value, value);

        } else {
            imp = PyObjC_MakeIMP(new_class, nil, value, value);
        }

        if (imp == NULL) {
            goto error_cleanup;
        }

        if (!class_addMethod( // LCOV_BR_EXCL_LINE
                new_class, PyObjCSelector_GetSelector(value), imp,
                PyObjCSelector_GetNativeSignature(value))) {
            /* should never fail */
            goto error_cleanup; // LCOV_EXCL_LINE
        }
    }

    /* class methods */
    for (i = 0; i < PyTuple_GET_SIZE(class_methods); i++) {
        value = PyTuple_GET_ITEM(class_methods, i);

        if (!PyObjCSelector_Check(value)) { // LCOV_BR_EXCL_LINE
            /* Cannot happen, sequence items were validated earlier */
            continue; // LCOV_EXCL_LINE
        }

        /* Make sure that the selector is bound to the newly created class */
        ((PyObjCSelector*)value)->sel_class = new_class;

        Method meth;
        int    is_override = 0;
        IMP    imp;

        meth = class_getClassMethod(super_class, PyObjCSelector_GetSelector(value));
        if (meth) {
            is_override               = 1;
            const char* meth_encoding = method_getTypeEncoding(meth);
            if (meth_encoding == NULL) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                PyErr_Format(PyObjCExc_BadPrototypeError,
                             "%R: Cannot determine superclass type encoding", value);
                goto error_cleanup;
                // LCOV_EXCL_STOP
            }

            if (!PyObjCRT_SignaturesEqual(meth_encoding,
                                          PyObjCSelector_GetNativeSignature(value))) {

                PyErr_Format(
                    PyObjCExc_BadPrototypeError,
                    "%R has signature that is not compatible with super-class: %s != %s",
                    value, meth_encoding, PyObjCSelector_GetNativeSignature(value));
                goto error_cleanup;
            }
        }

        if (is_override) {
            imp = PyObjC_MakeIMP(new_meta_class, super_class, value, value);
        } else {
            imp = PyObjC_MakeIMP(new_meta_class, nil, value, value);
        }

        if (imp == NULL) {
            goto error_cleanup;
        }

        if (!class_addMethod( // LCOV_BR_EXCL_LINE
                new_meta_class, PyObjCSelector_GetSelector(value), imp,
                PyObjCSelector_GetNativeSignature(value))) {
            goto error_cleanup; // LCOV_EXCL_LINE
        }
    }

    Py_CLEAR(py_superclass);

    /* XXX: Can __dict__ ever be in the class_dict? */
    if (PyDict_DelItemString(class_dict, "__dict__") == -1) {
        PyErr_Clear();
    }
    Py_CLEAR(instance_variables);
    Py_CLEAR(instance_methods);
    Py_CLEAR(class_methods);

    /*
     * NOTE: Class is not registered yet, we do that as lately as possible
     * because it is impossible to remove the registration from the
     * objective-C runtime.
     */
    return new_class;

error_cleanup:
    Py_XDECREF(instance_variables);
    Py_XDECREF(instance_methods);
    Py_XDECREF(class_methods);
    Py_XDECREF(py_superclass);

    if (new_class) {
        objc_disposeClassPair(new_class);
    }

    return NULL;
}

/*
 * Below here are implementations of various methods needed to correctly
 * subclass Objective-C classes from Python.
 *
 * These are added to the new Objective-C class by PyObjCClass_BuildClass (but
 * only if the super_class is a 'pure' objective-C class)
 *
 * NOTE:
 * - These functions will be used as methods, but as far as the compiler
 *   knows these are normal functions. You cannot use [super call]s here.
 */

static void
free_ivars(id self, PyObject* cls)
{
    /* Free all instance variables introduced through python */
    Ivar var;

    var = class_getInstanceVariable(PyObjCClass_GetClass(cls), "__dict__");
    if (var != NULL) {
        ptrdiff_t offset                      = ivar_getOffset(var);
        PyObject* tmp                         = *(PyObject**)(((char*)self) + offset);
        *(PyObject**)(((char*)self) + offset) = NULL;
        Py_XDECREF(tmp);
    }

    while (cls != NULL) {
        Class     objcClass = PyObjCClass_GetClass(cls);
        PyObject* clsDict;
        PyObject* clsValues;
        PyObject* o;

        if (objcClass == nil) {
            break;
        }

        /* XXX: Why does this not access the dict slot directly? */
        clsDict = PyObject_GetAttrString(cls, "__dict__");
        if (clsDict == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            PyErr_Clear();
            break;
            // LCOV_EXCL_STOP
        }

        /* Class.__dict__ is a dictproxy, which is not a dict and
         * therefore PyDict_Values doesn't work.
         *
         * XXX: PyMapping_Values?
         */
        PyObject* args[2] = {NULL, clsDict};
        clsValues         = PyObject_VectorcallMethod(PyObjCNM_values, args + 1,
                                                      1 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
        Py_DECREF(clsDict);
        if (clsValues == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            PyErr_Clear();
            break;
            // LCOV_EXCL_STOP
        }

        PyObject* iter = PyObject_GetIter(clsValues);
        Py_DECREF(clsValues);
        if (iter == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            PyErr_Clear();
            continue;
            // LCOV_EXCL_STOP
        }

        /* Check type */
        while ((o = PyIter_Next(iter)) != NULL) {
            PyObjCInstanceVariable* iv;

            if (!PyObjCInstanceVariable_Check(o)) {
                Py_DECREF(o);
                continue;
            }

            iv = ((PyObjCInstanceVariable*)o);

            if (iv->isOutlet) {
                Py_DECREF(o);
                continue;
            }

            if (strcmp(iv->type, "@") != 0 && strcmp(iv->type, @encode(PyObject*)) != 0) {
                Py_DECREF(o);
                continue;
            }

            var = class_getInstanceVariable(objcClass, iv->name);
            if (var == NULL) { // LCOV_BR_EXCL_LINE
                /* This should never fail, we're walking the instance variables
                 * of a class we created earlier.
                 */
                // LCOV_EXCL_START
                Py_DECREF(o);
                continue;
                // LCOV_EXCL_STOP
            }

            if (iv->isSlot) {
                PyObject* tmp = *(PyObject**)(((char*)self) + ivar_getOffset(var));
                (*(PyObject**)(((char*)self) + ivar_getOffset(var))) = NULL;
                Py_XDECREF(tmp);
            } else {
                Py_BEGIN_ALLOW_THREADS
                    @try {
                        [*(id*)(((char*)self) + ivar_getOffset(var)) autorelease];

                    } @catch (NSObject* localException) {
                        NSLog(@"ignoring exception %@ in destructor", localException);
                    }
                Py_END_ALLOW_THREADS
                *(id*)(((char*)self) + ivar_getOffset(var)) = nil;
            }
            Py_DECREF(o);
        }
        Py_DECREF(iter);

        /* XXX: Why does this use cls.__bases__()[0] instead of
         *      the type slot with the primary superclass?
         */
        o = PyObject_GetAttrString(cls, "__bases__");
        if (o == NULL) {
            PyErr_Clear();
            cls = NULL;

        } else if (PyTuple_Size(o) == 0) {
            PyErr_Clear();
            cls = NULL;
            Py_DECREF(o);

        } else {
            cls = PyTuple_GET_ITEM(o, 0);
            if (cls == (PyObject*)&PyObjCClass_Type) {
                cls = NULL;
            }
            Py_DECREF(o);
        }
    }
}

/* -dealloc */
static void
object_method_dealloc(ffi_cif* cif __attribute__((__unused__)),
                      void* retval __attribute__((__unused__)), void** args,
                      void* userdata)
{
    id  self  = *(id*)(args[0]);
    SEL _meth = *(SEL*)(args[1]);

    struct objc_super spr;
    PyObject*         obj;
    PyObject*         delmethod;
    PyObject*         cls;
    PyObject *        ptype, *pvalue, *ptraceback;

    PyObjC_BEGIN_WITH_GIL
        PyErr_Fetch(&ptype, &pvalue, &ptraceback);

        /* object_getClass will only return Nil if its argument is nil */
        cls = PyObjCClass_New((Class _Nonnull)object_getClass(self));
        /* Note: In practice 'cls' will never be null */
        if (cls != NULL) { // LCOV_BR_EXCL_LINE
            delmethod = PyObjCClass_GetDelMethod(cls);
            if (delmethod != NULL) {
                PyObject* s = _PyObjCObject_NewDeallocHelper(self);
                if (s != NULL) { // LCOV_BR_EXCL_LINE
                    PyObject* args[2] = {NULL, s};
                    obj               = PyObject_Vectorcall(delmethod, args + 1,
                                                            1 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
                    if (obj == NULL) {
                        PyErr_WriteUnraisable(delmethod);
                    } else {
                        Py_DECREF(obj);
                    }
                    Py_DECREF(delmethod);
                    _PyObjCObject_FreeDeallocHelper(s);
                }
            }

            free_ivars(self, cls);

            PyErr_Restore(ptype, pvalue, ptraceback);
        }

    PyObjC_END_WITH_GIL

    spr.super_class = (Class _Nonnull)class_getSuperclass((Class)userdata);
    spr.receiver    = self;

    ((void (*)(struct objc_super*, SEL))objc_msgSendSuper)(&spr, _meth);
}

/* -copyWithZone:(NSZone*)zone */
static void
object_method_copyWithZone_(ffi_cif* cif __attribute__((__unused__)), void* resp,
                            void** args, void* userdata)
{
    id      self = *(id*)args[0];
    id      copy;
    SEL     _meth = *(SEL*)args[1];
    NSZone* zone  = *(NSZone**)args[2];
    Class   cls;
    Class   super_cls;

    struct objc_super spr;
    PyGILState_STATE  state;

    /* Ask super to create a copy */

    spr.super_class = super_cls = (Class _Nonnull)class_getSuperclass((Class)userdata);
    spr.receiver                = self;
    copy =
        ((id(*)(struct objc_super*, SEL, NSZone*))objc_msgSendSuper)(&spr, _meth, zone);

    if (copy == nil) {
        *(id*)resp = nil;
        return;
    }
    if (!PyObjC_class_isSubclassOf((Class _Nonnull)object_getClass(copy), userdata)) {
        /* The copy is not a subclass of the defining class, this
         * can happen in (for example) class clusters.
         *
         * XXX: Need explicit test case for this!
         */
        // NSLog(@"not a subclass %@ %@", object_getClass(copy), userdata);
        *(id*)resp = copy;
        return;
    }

    state = PyGILState_Ensure();

    cls = object_getClass(self);
    while (cls != super_cls) {
        unsigned ivarCount, i;
        /* Returns NULL only when setting ivarCount to 0 */
        Ivar* ivarList = (Ivar* _Nonnull)class_copyIvarList(cls, &ivarCount);

        /* XXX: This code is not 100% consistent with the code freeing slots,
         *      in particular for ObjC variables, and the 'isSlot' attribute.
         *      Document why this is (both here, and if necessary in user docs).
         *      It might be possible to make the two consistent, but that could
         *      break backward compatibility.
         *      This code also needs tests!
         */
        for (i = 0; i < ivarCount; i++) {
            Ivar        v = ivarList[i];
            const char* typestr;
            ptrdiff_t   offset;
            PyObject**  p;

            typestr = ivar_getTypeEncoding(v);
            offset  = ivar_getOffset(v);

            if (strcmp(typestr, @encode(PyObject*)) != 0)
                continue;

            /* A PyObject, increase it's refcount */
            p = (PyObject**)(((char*)copy) + offset);
            if (*p == NULL)
                continue;
            if (strcmp(ivar_getName(v), "__dict__") == 0) {
                /* copy __dict__ */
                *p = PyDict_Copy(*p);
                if (*p == NULL) {
                    [copy release];
                    PyObjCErr_ToObjCWithGILState(&state);
                    return;
                }
            } else {
                Py_INCREF(*p);
            }
        }

        free(ivarList);
        cls = class_getSuperclass(cls);
    }

    PyGILState_Release(state);
    *(id*)resp = copy;
}

/* -forwardInvocation: */
/*
 * XXX: Consider dropping this method, even it is a
 *      backward compatibility break: NSObject's
 *      forwardInvocation always raises an exception,
 *      this implementation does a lot more than that...
 *
 *      The implementation is large, but still incomplete
 *      because it reimplements the logic in the regular
 *      path, and only does so when upcalling doesn't require
 *      a manual implementation.
 *
 *      This implementation is also fairly large at over
 *      460 lines of code.
 */
static void
object_method_forwardInvocation(ffi_cif* cif __attribute__((__unused__)),
                                void* retval __attribute__((__unused__)), void** args,
                                void* userdata)
{
    id            self       = *(id*)args[0];
    SEL           _meth      = *(SEL*)args[1];
    NSInvocation* invocation = *(NSInvocation**)args[2];
    SEL           theSelector;

    PyGILState_STATE state = PyGILState_Ensure();

    /* XXX: Shouldn't this use id_to_python? */
    PyObject* pyself = PyObjCObject_New(self, PyObjCObject_kDEFAULT, YES);
    if (pyself == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyObjCErr_ToObjCWithGILState(&state);
        return;
        // LCOV_EXCL_STOP
    }

    /*
     * First check if this is a method that's implemented in Python,
     * if not just call super. This avoids problems when super's
     * methodForSelector returns an IMP that invokes forwardInvocation
     * again.
     */

    Py_BEGIN_ALLOW_THREADS
        @try {
            theSelector = [invocation selector];
        } @catch (NSObject* localException) {
            /* XXX: This is wrong, releasing the GIL while we don't hold it */
            Py_DECREF(pyself);
            PyGILState_Release(state);
            @throw;
        }
    Py_END_ALLOW_THREADS

    PyObject* pymeth = PyObjCObject_FindSelector(pyself, theSelector);

    if ((pymeth == NULL) || PyObjCNativeSelector_Check(pymeth)) {
        struct objc_super spr;

        if (pymeth == NULL) {
            PyErr_Clear();
        }

        Py_XDECREF(pymeth);
        Py_XDECREF(pyself);

        spr.super_class = class_getSuperclass((Class)userdata);
        spr.receiver    = self;
        PyGILState_Release(state);
        ((void (*)(struct objc_super*, SEL, NSInvocation*))objc_msgSendSuper)(&spr, _meth,
                                                                              invocation);
        return;
    }
    Py_CLEAR(pymeth);
    Py_CLEAR(pyself);

    /*
     * The method is implemented in Python. Fetch the IMP and call it through
     * libffi (to avoid having to reproduce the method stub implementation
     * in this function).
     */

    IMP method;
    @try {
        method = [self methodForSelector:theSelector];
    } @catch (NSObject* localException) { // LCOV_EXCL_LINE
        // LCOV_EXCL_START
        PyGILState_Release(state);
        @throw;
        // LCOV_EXCL_STOP
    }
    if (method == NULL) {
        PyGILState_Release(state);
        @throw [NSException exceptionWithName:NSInternalInconsistencyException
                                       reason:@"cannot resolve selector"
                                     userInfo:nil];
    }

    if (PyObjCFFI_CallUsingInvocation(method, invocation) == -1) {
        PyObjCErr_ToObjCWithGILState(&state);
        return;
    }
    PyGILState_Release(state);
}

static void
object_method_valueForKey_(ffi_cif* cif __attribute__((__unused__)), void* retval,
                           void** args, void* userdata)
{
    /*
     * This method does the following:
     * - Checks super implementation
     * - if [[self class] accessInstanceVariablesDirectly]
     * - Checks for attribute key
     * - Checks for attribute _key
     */
    int       r;
    id        self  = *(id*)args[0];
    SEL       _meth = *(SEL*)args[1];
    NSString* key   = *(NSString**)args[2];

    struct objc_super spr;

    /* First check super */
    @try {
        spr.super_class = class_getSuperclass((Class)userdata);
        spr.receiver    = self;
        *((id*)retval)  = ((id(*)(struct objc_super*, SEL, NSString*))objc_msgSendSuper)(
            &spr, _meth, key);
    } @catch (NSObject* localException) {

        /* Parent doesn't know the key, try to create in the
         * python side, just like for plain python objects.
         *
         * NOTE: We have to be extremely careful in here, some classes,
         * like NSManagedContext convert __getattr__ into a -valueForKey:,
         * and that can cause infinite loops.
         *
         * This is why attribute access is hardcoded using PyObjCObject_GetAttrString
         * rather than PyObject_GetAttrString.
         */
        if (([localException isKindOfClass:[NSException class]])
            && ([[(NSException*)localException name] isEqual:@"NSUnknownKeyException"]) &&
            [[self class] accessInstanceVariablesDirectly]) {

            PyGILState_STATE state   = PyGILState_Ensure();
            PyObject*        selfObj = PyObjCObject_New(self, PyObjCObject_kDEFAULT, YES);
            PyObject*        res     = NULL;
            r                        = -1;
            do {
                res = PyObjCObject_GetAttrString(selfObj, (char*)[key UTF8String]);
                if (res == NULL) {
                    PyErr_Clear();
                    res = PyObjCObject_GetAttrString(
                        selfObj, (char*)[[@"_" stringByAppendingString:key] UTF8String]);
                    if (res == NULL) {
                        break;
                    }
                }

                /* Check that we don't accidentally return
                 * an accessor method.
                 */
                if (PyObjCSelector_Check(res)
                    && ((PyObjCSelector*)res)->sel_self == selfObj) {
                    Py_DECREF(res);
                    res = NULL;
                    break;
                }
                r = depythonify_c_value(@encode(id), res, retval);
            } while (0);
            Py_DECREF(selfObj);
            Py_XDECREF(res);
            if (r == -1) {
                PyErr_Clear();
                PyGILState_Release(state);
                @throw;
            }
            PyGILState_Release(state);
        } else {
            @throw;
        }
    }
}

static void
object_method_setValue_forKey_(ffi_cif* cif __attribute__((__unused__)),
                               void* retval __attribute__((__unused__)), void** args,
                               void* userdata)
{
    /*
     * This method does the following:
     * - Checks super implementation
     * - if [[self class] accessInstanceVariablesDirectly]
     * - Checks for attribute _key and sets if present
     * - Sets attribute key
     */
    int               r;
    struct objc_super spr;
    id                self  = *(id*)args[0];
    SEL               _meth = *(SEL*)args[1];
    id                value = *(id*)args[2];
    NSString*         key   = *(NSString**)args[3];

    @try {
        /* First check super */
        spr.super_class = class_getSuperclass((Class)userdata);
        spr.receiver    = self;
        ((void (*)(struct objc_super*, SEL, id, id))objc_msgSendSuper)(&spr, _meth, value,
                                                                       key);
    } @catch (NSObject* localException) {
        /* Parent doesn't know the key, try to create in the
         * python side, just like for plain python objects.
         */
        if (([localException isKindOfClass:[NSException class]])
            && ([[(NSException*)localException name] isEqual:@"NSUnknownKeyException"]) &&
            [[self class] accessInstanceVariablesDirectly]) {

            PyGILState_STATE state = PyGILState_Ensure();
            PyObject*        val   = id_to_python(value);
            if (val == NULL) {
                PyErr_Clear();
                PyGILState_Release(state);

                @throw;
            }
            PyObject* res     = NULL;
            PyObject* selfObj = PyObjCObject_New(self, PyObjCObject_kDEFAULT, YES);
            r                 = -1;
            do {
                char* rawkey = (char*)[[@"_" stringByAppendingString:key] UTF8String];
                res          = PyObject_GetAttrString(selfObj, rawkey);
                if (res != NULL) {
                    r = PyObject_SetAttrString(selfObj, rawkey, val);
                    if (r != -1) {
                        break;
                    }
                }
                PyErr_Clear();
                rawkey = (char*)[key UTF8String];
                r      = PyObject_SetAttrString(selfObj, rawkey, val);
            } while (0);
            Py_DECREF(selfObj);
            Py_DECREF(val);
            Py_XDECREF(res);
            if (r == -1) {
                PyErr_Clear();
                PyGILState_Release(state);
                @throw;
            }
            PyGILState_Release(state);
        } else {
            @throw;
        }
    }
}

NS_ASSUME_NONNULL_END
