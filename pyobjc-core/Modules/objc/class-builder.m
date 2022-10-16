/*
 * This file contains the code that is used to create proxy-classes for Python
 * classes in the objective-C runtime.
 */
#include "pyobjc.h"

#import <Foundation/NSInvocation.h>

NS_ASSUME_NONNULL_BEGIN

/* XXX: See comment at definition */
static PyObject* _Nullable PyObjC_CallPython(id self, SEL selector, PyObject* arglist,
                                             BOOL* isAlloc, BOOL* isCFAlloc);

/* Special methods for Python subclasses of Objective-C objects */
static void object_method_dealloc(ffi_cif* cif, void* retval, void** args, void* userarg);
static void object_method_respondsToSelector(ffi_cif* cif, void* retval, void** args,
                                             void* userarg);
static void object_method_methodSignatureForSelector(ffi_cif* cif, void* retval,
                                                     void** args, void* userarg);
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
    BOOL use_intermediate;

} gMethods[] = {

    {0, "dealloc", "dealloc", "v@:", object_method_dealloc, NO, YES},
    {0, "storedValueForKey:", "storedValueForKey_", "@@:@", object_method_valueForKey_,
     NO, YES},
    {0, "valueForKey:", "valueForKey_", "@@:@", object_method_valueForKey_, NO, YES},
    {0, "takeStoredValue:forKey:", "takeStoredValue_forKey_", "v@:@@",
     object_method_setValue_forKey_, NO, YES},
    {0, "takeValue:forKey:", "takeValue_forKey_", "v@:@@", object_method_setValue_forKey_,
     NO, YES},
    {0, "setValue:forKey:", "setValue_forKey_", "v@:@@", object_method_setValue_forKey_,
     NO, YES},
    {0, "forwardInvocation:", "forwardInvocation_", "v@:@",
     object_method_forwardInvocation, NO, YES},
    {0, "methodSignatureForSelector:", "methodSignatureForSelector_",
     "@@::", object_method_methodSignatureForSelector, NO, YES},
    {0, "respondsToSelector:", "respondsToSelector_",
     "c@::", object_method_respondsToSelector, NO, YES},
    {0, "copyWithZone:", "copyWithZone_", "@@:^{_NSZone=}", object_method_copyWithZone_,
     YES, YES},
    {0, "mutableCopyWithZone:", "mutableCopyWithZone_", "@@:^{_NSZone=}",
     object_method_copyWithZone_, YES, YES},

    {0, 0, 0, 0, 0, 0, 0}};

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
 * The Python proxy for an object should not contain any state, even if
 * the class is defined in Python. Therefore transfer all slots to the
 * Objective-C class and add '__slots__ = ()' to the Python class.
 */
static int
do_slots(PyObject* super_class, PyObject* clsdict)
{
    PyObject*  slot_value;
    PyObject*  slots;
    Py_ssize_t len, i;

    slot_value = PyDict_GetItemStringWithError(clsdict, "__slots__");
    if (slot_value == NULL && PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return -1;                                // LCOV_EXCL_LINE
    }
    if (slot_value == NULL) {
        /*
         * No __slots__ found, add an empty one and
         * ensure that instances will have a __dict__.
         */
        PyObject* v;

        PyErr_Clear();

        slot_value = PyTuple_New(0);
        if (slot_value == NULL) { // LCOV_BR_EXCL_LINE
            return 0;             // LCOV_EXCL_LINE
        }

        if (PyDict_SetItemString( // LCOV_BR_EXCL_LINE
                clsdict, "__slots__", slot_value)
            < 0) {
            // LCOV_EXCL_START
            Py_DECREF(slot_value);
            return -1;
            // LCOV_EXCL_STOP
        }
        Py_DECREF(slot_value);

        if (PyObjCClass_DictOffset(super_class) != 0) {
            /* We already have an __dict__ */
            return 0;
        }

        v = PyObjCInstanceVariable_New("__dict__");
        if (v == NULL) { // LCOV_BR_EXCL_LINE
            return -1;   // LCOV_EXCL_LINE
        }
        ((PyObjCInstanceVariable*)v)->type   = PyObjCUtil_Strdup(@encode(PyObject*));
        ((PyObjCInstanceVariable*)v)->isSlot = 1;
        if (PyDict_SetItemString(clsdict, "__dict__", v) < 0) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(v);
            return -1;
            // LCOV_EXCL_STOP
        }
        Py_DECREF(v);

        return 0;
    }

    slots = PySequence_Fast(slot_value, "__slots__ must be a sequence");
    if (slots == NULL) {
        return -1;
    }

    len = PySequence_Fast_GET_SIZE(slots);
    for (i = 0; i < len; i++) {
        PyObjCInstanceVariable* var;

        slot_value = PySequence_Fast_GET_ITEM(slots, i);

        if (PyUnicode_Check(slot_value)) {
            const char* slot_name = PyUnicode_AsUTF8(slot_value);
            if (slot_name == NULL) {
                return -1;
            }

            var = (PyObjCInstanceVariable*)PyObjCInstanceVariable_New(slot_name);
            if (var == NULL) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                Py_DECREF(slots);
                return -1;
                // LCOV_EXCL_STOP
            }

        } else {
            PyErr_Format(PyExc_TypeError, "__slots__ entry %R is not a string, but %s",
                         slot_value, Py_TYPE(slot_value)->tp_name);
            Py_DECREF(slots);
            return -1;
        }

        ((PyObjCInstanceVariable*)var)->type   = PyObjCUtil_Strdup(@encode(PyObject*));
        ((PyObjCInstanceVariable*)var)->isSlot = 1;

        if (PyDict_SetItem( // LCOV_BR_EXCL_LINE
                clsdict, slot_value, (PyObject*)var)
            < 0) {
            // LCOV_EXCL_START
            Py_DECREF(slots);
            Py_DECREF(var);
            return -1;
            // LCOV_EXCL_STOP
        }
        Py_DECREF(var);
    }
    Py_DECREF(slots);

    slot_value = PyTuple_New(0);
    if (slot_value == NULL) { // LCOV_BR_EXCL_LINE
        return 0;             // LCOV_EXCL_LINE
    }

    if (PyDict_SetItemString( // LCOV_BR_EXCL_LINE
            clsdict, "__slots__", slot_value)
        < 0) {
        // LCOV_EXCL_START
        Py_DECREF(slot_value);
        return -1;
        // LCOV_EXCL_STOP
    }

    Py_DECREF(slot_value);
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

/* PyObjC uses a number of typecode descriptors that aren't available in
 * the objc runtime. Remove these from the type string (inline).
 *
 */
static int
tc2tc(char* buf)
{
    /* Skip pointer declarations and annotations */
    for (;;) {
        switch (*buf) {
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
    case _C_NSBOOL:
#ifdef __arm64__
        *buf = _C_BOOL;
#else
        *buf = _C_CHR;
#endif
        break;

    case _C_CHAR_AS_INT:
    case _C_CHAR_AS_TEXT:
        *buf = _C_CHR;
        break;

    case _C_UNICHAR:
        *buf = _C_SHT;
        break;

    case _C_STRUCT_B:
        while (*buf != _C_STRUCT_E && *buf && *buf++ != '=') {
        }
        while (buf && *buf && *buf != _C_STRUCT_E) {
            if (*buf == '"') {
                /* embedded field name */
                buf = strchr(buf + 1, '"');
                if (buf == NULL) {
                    return -1;
                }
                buf++;
            }
            tc2tc(buf);
            char* new_buf = (char*)PyObjCRT_SkipTypeSpec(buf);
            if (new_buf == NULL) {
                return -1;
            }
            buf = new_buf;
        }
        break;

    case _C_UNION_B:
        while (*buf != _C_UNION_E && *buf && *buf++ != '=') {
        }
        while (buf && *buf && *buf != _C_UNION_E) {
            if (*buf == '"') {
                /* embedded field name */
                buf = strchr(buf + 1, '"');
                if (buf == NULL) {
                    return -1;
                }
                buf++;
            }
            tc2tc(buf);
            char* new_buf = (char*)PyObjCRT_SkipTypeSpec(buf);
            if (new_buf == NULL) {
                return -1;
            }
            buf = new_buf;
        }
        break;

    case _C_ARY_B:
        while (isdigit(*++buf))
            ;
        tc2tc(buf);
        break;
    }
    return 0;
}

/* XXX: This function and tc2tc should be in objc_support.m
 * XXX: _C_VECTOR... requires completely removing part of the buffer
 */
int
PyObjC_RemoveInternalTypeCodes(char* buf)
{
    char* _Nullable cur = buf;

    while (*cur) {
        if (tc2tc(cur) == -1) {
            PyErr_SetString(PyObjCExc_Error, "invalid type encoding");
            return -1;
        }
        cur = (char*)PyObjCRT_SkipTypeSpec(cur);
        if (cur == NULL) {
            return -1;
        }
    }
    return 0;
}

static BOOL
need_intermediate(PyObject* class_dict)
{
    struct method_info* cur;

    for (cur = gMethods; cur->method_name != NULL; cur++) {
        /* XXX: Should look for a selector, not necessarily using the
         * method name.
         *
         * XXX: Use PyDict_GetItemStringWithError, but that requires an
         * API change for this function as well.
         */
        if (PyDict_GetItemString(class_dict, cur->method_name) != NULL) {
            return YES;
        }
    }
    return NO;
}

Class _Nullable PyObjCClass_BuildClass(Class super_class, PyObject* protocols, char* name,
                                       PyObject* class_dict, PyObject* meta_dict,
                                       PyObject* hiddenSelectors,
                                       PyObject* hiddenClassSelectors)
{
    PyObject*  seq;
    PyObject*  key_list = NULL;
    PyObject*  key      = NULL;
    PyObject*  value    = NULL;
    Py_ssize_t i;
    Py_ssize_t key_count;
    Py_ssize_t protocol_count     = 0;
    int        first_python_gen   = 0;
    Class      new_class          = NULL;
    Class      new_meta_class     = NULL;
    PyObject*  py_superclass      = NULL;
    int        have_intermediate  = 0;
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

    if (PyDict_SetItemString( // LCOV_BR_EXCL_LINE
            class_dict, "__objc_python_subclass__", Py_True)
        == -1) {
        return Nil; // LCOV_EXCL_LINE
    }

    py_superclass = PyObjCClass_New(super_class);
    if (py_superclass == NULL) { // LCOV_BR_EXCL_LINE
        return Nil;              // LCOV_EXCL_LINE
    }

    instance_variables = PySet_New(NULL);
    if (instance_variables == NULL) { // LCOV_BR_EXCL_LINE
        goto error_cleanup;           // LCOV_EXCL_LINE
    }

    instance_methods = PySet_New(NULL);
    if (instance_methods == NULL) { // LCOV_BR_EXCL_LINE
        goto error_cleanup;         // LCOV_EXCL_LINE
    }

    class_methods = PySet_New(NULL);
    if (class_methods == NULL) { // LCOV_BR_EXCL_LINE
        goto error_cleanup;      // LCOV_EXCL_LINE
    }

    /* We must override copyWithZone: for python classes because the
     * refcounts of python slots might be off otherwise. Yet it should
     * be possible to override copyWithZone: in those classes.
     *
     * The solution: introduce an intermediate class that contains our
     * implementation of copyWithZone:. This intermediate class is only
     * needed when (1) the superclass implements copyWithZone: and (2)
     * the python subclass overrides that method.
     *
     * The same issue is present with a number of other methods.
     */

    if (!PyObjCClass_HasPythonImplementation(py_superclass)
        && need_intermediate(class_dict)) {
        Class intermediate_class;
        char  buf[256];
        int   r;

        have_intermediate = 1;

        r = snprintf(buf, sizeof(buf), "_PyObjCCopying_%s", class_getName(super_class));
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

    if (do_slots(py_superclass, class_dict) < 0) {
        goto error_cleanup;
    }

    if (!PyObjCClass_HasPythonImplementation(py_superclass)) {
        /*
         * This class has a super_class that is pure objective-C
         * We'll add some instance variables and methods that are
         * needed for the correct functioning of the class.
         *
         * See the code below the next loop.
         */
        first_python_gen = 1;
    }

    /* The code uses PyDict_Keys instead of PyDict_Next because
     * we change the class_dict on the second iteration. The first
     * iteration could use PyDict_Next, but is kept like this to
     * keep the code style consistent.
     */
    key_list = PyDict_Keys(class_dict);
    if (key_list == NULL) { // LCOV_BR_EXCL_LINE
        goto error_cleanup; // LCOV_EXCL_LINE
    }

    key_count = PyList_Size(key_list);
    if (key_count == -1) {  // LCOV_BR_EXCL_LINE
        goto error_cleanup; // LCOV_EXCL_LINE
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

    /* First step: call class setup hooks of entries in the class dict */
    for (i = 0; i < key_count; i++) {
        key = PyList_GET_ITEM(key_list, i);

        value = PyDict_GetItemWithError(class_dict, key);
        if (value == NULL) {
            if (PyErr_Occurred())   // LCOV_BR_EXCL_LINE
                goto error_cleanup; // LCOV_EXCL_LINE
            PyErr_SetString(PyObjCExc_InternalError,
                            "PyObjCClass_BuildClass: Cannot fetch item in keylist");
            goto error_cleanup;
        }

        /*
         * Check if the value has a class-setup hook, and if it does
         * call said hook.
         * XXX: Create utility function for "call optional method"
         *      or use VectorcallMethod and handle AttributeError.
         */
        PyObject* m = PyObject_GetAttrString(value, "__pyobjc_class_setup__");
        if (m == NULL) {
            PyErr_Clear();

        } else {
            PyObject* args[5] = {NULL, key, class_dict, instance_methods, class_methods};
            PyObject* rv      = PyObject_Vectorcall(m, args + 1,
                                                    4 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
            Py_DECREF(m);
            if (rv == NULL) {
                goto error_cleanup;
            }
            Py_DECREF(rv);
        }
    }

    /* The class_setup_hooks may have changed the class dictionary, hence
     * we need to recalculate the key list.
     */
    Py_CLEAR(key_list);

    key_list = PyDict_Keys(class_dict);
    if (key_list == NULL) { // LCOV_BR_EXCL_LINE
        goto error_cleanup; // LCOV_EXCL_LINE
    }

    key_count = PyList_Size(key_list);
    if (key_count == -1) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(key_list);
        goto error_cleanup;
        // LCOV_EXCL_STOP
    }

    /* Step 2b: Collect methods and instance variables in the class dict
     *          into the 3 sets.
     *
     * XXX: This work should be done by the class setup hook instead.
     */
    for (i = 0; i < key_count; i++) {
        key = PyList_GET_ITEM(key_list, i);

        value = PyDict_GetItemWithError(class_dict, key);
        if (value == NULL) { // LCOV_BR_EXCL_LINE
            /* I'm pretty sure that keys can't disappear from
             * the class_dict at this point.
             */
            // LCOV_EXCL_START
            if (PyErr_Occurred())   // LCOV_BR_EXCL_LINE
                goto error_cleanup; // LCOV_EXCL_LINE
            PyErr_SetString(PyObjCExc_InternalError,
                            "PyObjCClass_BuildClass: Cannot fetch item in keylist");
            goto error_cleanup;
            // LCOV_EXCL_STOP
        }

        if (PyObjCInstanceVariable_Check(value)) {
            if (PySet_Add(instance_variables, value) == -1) {
                goto error_cleanup;
            }

        } else if (PyObjCSelector_Check(value)) {
            int r;

            /* Check if the 'key' is the name as the python
             * representation of our selector. If not: add the
             * python representation of our selector to the
             * dict as well to ensure that the ObjC interface works
             * from Python as well.
             *
             * NOTE: This also allows one to add both a class
             * and instance method for the same selector in one
             * generation.
             */
            char        buf[1024];
            const char* py_meth_name = PyObjC_SELToPythonName(
                PyObjCSelector_GetSelector(value), buf, sizeof(buf));
            if (py_meth_name == NULL) { // LCOV_BR_EXCL_LINE
                /* Can only happen when the selector name is huge */
                goto error_cleanup; // LCOV_EXCL_LINE
            }

            PyObject* pyname = PyUnicode_FromString(py_meth_name);
            if (pyname == NULL) {   // LCOV_BR_EXCL_LINE
                goto error_cleanup; // LCOV_EXCL_LINE
            }

            int shouldCopy = PyObject_RichCompareBool(pyname, key, Py_EQ);
            if (shouldCopy == -1) {
                goto error_cleanup;
            } else if (!shouldCopy) {
                Py_DECREF(pyname);
                pyname = NULL;
            }

            if (PyObjCSelector_GetClass(value) != NULL) {
                PyObject* new_value;
                new_value = PyObjCSelector_Copy(value);
                if (new_value == NULL) { // LCOV_BR_EXCL_LINE
                    goto error_cleanup;  // LCOV_EXCL_LINE
                }

                if (PyDict_SetItem( // LCOV_BR_EXCL_LINE
                        class_dict, key, new_value)
                    == -1) {
                    // LCOV_EXCL_START
                    Py_DECREF(new_value);
                    goto error_cleanup;
                    // LCOV_EXCL_STOP
                }

                value = new_value;
                Py_DECREF(new_value); /* The value is still in the dict, and hence safe to
                                         use */
            }

            if (PyObjCSelector_IsClassMethod(value)) {
                r = PySet_Add(class_methods, value);
                if (r == -1) {          // LCOV_BR_EXCL_LINE
                    goto error_cleanup; // LCOV_EXCL_LINE
                }

                if (!PyObjCSelector_IsHidden(value)) {
                    if (PyDict_SetItem( // LCOV_BR_EXCL_LINE
                            meta_dict, key, value)
                        == -1) {
                        goto error_cleanup; // LCOV_EXCL_LINE
                    }
                } else {
                    shouldCopy = NO;
                }

                if (shouldCopy) {
                    r = PyDict_SetItem(meta_dict, pyname, value);
                    Py_DECREF(pyname);
                    if (r == -1) {          // LCOV_BR_EXCL_LINE
                        goto error_cleanup; // LCOV_EXCL_LINE
                    }
                }

                if (PyDict_DelItem(class_dict, key) == -1) { // LCOV_BR_EXCL_LINE
                    goto error_cleanup;                      // LCOV_EXCL_LINE
                }

            } else {
                r = PySet_Add(instance_methods, value);
                if (r == -1) {          // LCOV_BR_EXCL_LINE
                    goto error_cleanup; // LCOV_EXCL_LINE
                }

                if (PyObjCSelector_IsHidden(value)) {
                    r = PyDict_DelItem(class_dict, key);
                    if (r == -1) {          // LCOV_BR_EXCL_LINE
                        goto error_cleanup; // LCOV_EXCL_LINE
                    }
                    shouldCopy = NO;
                }
                if (shouldCopy) {
                    r = PyDict_SetItem(class_dict, pyname, value);
                    Py_DECREF(pyname);
                    if (r == -1) {          // LCOV_BR_EXCL_LINE
                        goto error_cleanup; // LCOV_EXCL_LINE
                    }
                }
            }

        } else if (PyMethod_Check(value) || PyFunction_Check(value)
                   || PyObject_TypeCheck(value, &PyClassMethod_Type)) {

            const char* ocname;
            PyObject*   pyname = key;

            if (PyUnicode_Check(pyname)) {
                ocname = PyObjC_Unicode_Fast_Bytes(pyname);
                if (ocname == NULL) {
                    goto error_cleanup;
                }

            } else {
                PyErr_Format(PyExc_TypeError, "method name is of type %s, not a string",
                             Py_TYPE(pyname)->tp_name);
                goto error_cleanup;
            }

            if (ocname[0] != '_' || ocname[1] != '_') {
                /* Skip special methods (like __getattr__) to
                 * avoid confusing type().
                 */
                PyObject* new_value;

                new_value =
                    PyObjCSelector_FromFunction(pyname, value, py_superclass, protocols);
                if (new_value == NULL) {
                    goto error_cleanup;
                }
                value = new_value;

                if (PyObjCSelector_Check(value)) {
                    int r;

                    if (PyObjCSelector_IsClassMethod(value)) {
                        if (!PyObjCSelector_IsHidden(value)) {
                            if (PyDict_SetItem( // LCOV_BR_EXCL_LINE
                                    meta_dict, key, value)
                                == -1) {
                                goto error_cleanup; // LCOV_EXCL_LINE
                            }
                        }
                        if (PyDict_DelItem(class_dict, key) == -1) { // LCOV_BR_EXCL_LINE
                            goto error_cleanup;                      // LCOV_EXCL_LINE
                        }

                        r = PySet_Add(class_methods, value);
                        if (r == -1) {          // LCOV_BR_EXCL_LINE
                            goto error_cleanup; // LCOV_EXCL_LINE
                        }

                    } else {
                        if (PyObjCSelector_IsHidden(value)) {
                            if (PyDict_DelItem( // LCOV_BR_EXCL_LINE
                                    class_dict, key)
                                == -1) {
                                goto error_cleanup; // LCOV_EXCL_LINE
                            }

                        } else {
                            if (PyDict_SetItem( // LCOV_BR_EXCL_LINE
                                    class_dict, key, value)
                                < 0) {
                                // LCOV_EXCL_START
                                Py_CLEAR(value);
                                goto error_cleanup;
                                // LCOV_EXCL_STOP
                            }
                        }

                        r = PySet_Add(instance_methods, value);
                        if (r == -1) {          // LCOV_BR_EXCL_LINE
                            goto error_cleanup; // LCOV_EXCL_LINE
                        }
                    }
                }
            }
        }
    }

    /* Keylist is not needed anymore */
    Py_CLEAR(key_list);

    /* Step 3: Check instance variables */

    /*    convert to 'fast sequence' to ensure stable order when accessing */
    seq = PySequence_Fast(instance_variables,
                          "converting instance variable set to sequence");
    if (seq == NULL) {
        goto error_cleanup;
    }
    Py_DECREF(instance_variables);
    instance_variables = seq;
    for (i = 0; i < PySequence_Fast_GET_SIZE(instance_variables); i++) {
        value = PySequence_Fast_GET_ITEM(instance_variables, i);

        if (!PyObjCInstanceVariable_Check(value)) {
            /* XXX: Why is this needed? */
            continue;
        }

        /* Our only check for now is that instance variable names must be unique */
        /* XXX: Is this really necessary? */
        /* XXX: This doesn't check that the new class has unique instance variables!
         *      Add test before fixing this
         */
        if (class_getInstanceVariable(super_class, PyObjCInstanceVariable_GetName(value))
            != NULL) {
            PyErr_Format(PyObjCExc_Error,
                         "a superclass already has an instance "
                         "variable with this name: %s",
                         PyObjCInstanceVariable_GetName(value));
            goto error_cleanup;
        }
    }

    /* Step 4: Verify instance and class methods sets */

    /*   first convert then to 'Fast' sequences for easier access */
    seq = PySequence_Fast(instance_methods, "converting instance method set to sequence");
    if (seq == NULL) {
        goto error_cleanup;
    }
    Py_DECREF(instance_methods);
    instance_methods = seq;

    seq = PySequence_Fast(class_methods, "converting class method set to sequence");
    if (seq == NULL) {
        goto error_cleanup;
    }
    Py_DECREF(class_methods);
    class_methods = seq;

    for (i = 0; i < PySequence_Fast_GET_SIZE(instance_methods); i++) {
        value = PySequence_Fast_GET_ITEM(instance_methods, i);

        if (PyBytes_Check(value)) {
            int r = PyDict_SetItem(hiddenSelectors, value, Py_None);
            if (r == -1) {          // LCOV_BR_EXCL_LINE
                goto error_cleanup; // LCOV_EXCL_LINE
            }
        }

        if (!PyObjCSelector_Check(value)) {
            continue;
        }

        if (PyObjCSelector_IsClassMethod(value)) { // LCOV_BR_EXCL_LINE
            /* Assertion failure: this can only happen when the code
             * in this file is buggy.
             */

            // LCOV_EXCL_START
            PyErr_Format(PyExc_TypeError, "class method in instance method set: -%s",
                         sel_getName(PyObjCSelector_GetSelector(value)));
            goto error_cleanup;
            // LCOV_EXCL_STOP
        }

        if (PyObjCNativeSelector_Check(value)) { // LCOV_BR_EXCL_LINE
            /* Assertion failure: this can only happen when the code
             * in this file is buggy.
             */

            // LCOV_EXCL_START
            PyErr_Format(PyExc_TypeError, "native selector -%s of %s",
                         sel_getName(PyObjCSelector_GetSelector(value)),
                         class_getName(PyObjCSelector_GetClass(value)));
            goto error_cleanup;
            // LCOV_EXCL_STOP
            //
        } else if (PyObjCSelector_Check(value)) {
            PyObjCSelector* sel = (PyObjCSelector*)value;

            /* Set sel_class */
            sel->sel_class = new_class;

            if (sel->sel_flags & PyObjCSelector_kHIDDEN) {
                PyObject* v = PyObjCBytes_InternFromString(
                    sel_getName(PyObjCSelector_GetSelector(value)));
                if (v == NULL) {        // LCOV_BR_EXCL_LINE
                    goto error_cleanup; // LCOV_EXCL_LINE
                }
                int r = PyDict_SetItem(hiddenSelectors, v,
                                       (PyObject*)PyObjCSelector_GetMetadata(value));
                Py_DECREF(v);
                if (r == -1) {          // LCOV_BR_EXCL_LINE
                    goto error_cleanup; // LCOV_EXCL_LINE
                }
            }
        }
    }
    for (i = 0; i < PySequence_Fast_GET_SIZE(class_methods); i++) {
        value = PySequence_Fast_GET_ITEM(class_methods, i);

        if (PyBytes_Check(value)) {
            /* XXX: This needs documentation */
            int r = PyDict_SetItem(hiddenClassSelectors, value, Py_None);
            if (r == -1) {          // LCOV_BR_EXCL_LINE
                goto error_cleanup; // LCOV_EXCL_LINE
            }
        }

        if (!PyObjCSelector_Check(value)) {
            continue;
        }

        if (!PyObjCSelector_IsClassMethod(value)) { // LCOV_BR_EXCL_LINE
            /* Assertion failure: this can only happen when the code
             * in this file is buggy.
             */

            // LCOV_EXCL_START
            PyErr_Format(PyExc_TypeError, "instance method in class method set: -%s",
                         sel_getName(PyObjCSelector_GetSelector(value)));
            goto error_cleanup;
            // LCOV_EXCL_STOP
        }

        if (PyObjCNativeSelector_Check(value)) {
            /* Assertion failure: this can only happen when the code
             * in this file is buggy.
             */

            // LCOV_EXCL_START
            PyErr_Format(PyExc_TypeError, "native selector +%s of %s",
                         sel_getName(PyObjCSelector_GetSelector(value)),
                         class_getName(PyObjCSelector_GetClass(value)));
            goto error_cleanup;
            // LCOV_EXCL_STOP

        } else if (PyObjCSelector_Check(value)) {
            PyObjCSelector* sel = (PyObjCSelector*)value;

            /* Set sel_class */
            sel->sel_class = new_class;

            if (sel->sel_flags & PyObjCSelector_kHIDDEN) {
                PyObject* v = PyObjCBytes_InternFromString(
                    sel_getName(PyObjCSelector_GetSelector(value)));
                if (v == NULL) {        // LCOV_BR_EXCL_LINE
                    goto error_cleanup; // LCOV_EXCL_LINE
                }
                int r = PyDict_SetItem(hiddenClassSelectors, v,
                                       (PyObject*)PyObjCSelector_GetMetadata(value));
                Py_DECREF(v);
                if (r == -1) {          // LCOV_BR_EXCL_LINE
                    goto error_cleanup; // LCOV_EXCL_LINE
                }
            }
        }
    }

    /* Allocate space for the new instance variables and methods */
    if (first_python_gen) {
        /* Our parent is a pure Objective-C class, add our magic
         * methods and variables
         */

        if (!have_intermediate) {
            /* XXX: This loop is also in the function that builds the
             *      intermediate class, refactor this.
             */
            setup_gMethods_selectors();
            for (struct method_info* cur = gMethods; cur->method_name != NULL; cur++) {
                if (cur->override_only) {
                    if (![super_class instancesRespondToSelector:cur->selector]) {
                        continue;
                    }
                }

                PyObjCMethodSignature* methinfo =
                    PyObjCMethodSignature_WithMetaData(cur->typestr, NULL, NO);
                if (methinfo == NULL)   // LCOV_BR_EXCL_LINE
                    goto error_cleanup; // LCOV_EXCL_LINE

                IMP closure = PyObjCFFI_MakeClosure(methinfo, cur->func, new_class);
                Py_CLEAR(methinfo);
                if (closure == NULL)    // LCOV_BR_EXCL_LINE
                    goto error_cleanup; // LCOV_EXCL_LINE

                class_addMethod(new_class, cur->selector, closure, cur->typestr);
                PyObject* sel =
                    PyObjCSelector_NewNative(new_class, cur->selector, cur->typestr, 0);
                if (sel == NULL) // LCOV_BR_EXCL_LINE
                    /* The call can only fail when running out of memory */
                    goto error_cleanup; // LCOV_EXCL_LINE

                int r = PyDict_SetItemString(class_dict, cur->method_name, sel);
                Py_DECREF(sel);

                if (r == -1)            // LCOV_BR_EXCL_LINE
                    goto error_cleanup; // LCOV_EXCL_LINE
            }
        }
    }

    /* add instance variables */
    for (i = 0; i < PySequence_Fast_GET_SIZE(instance_variables); i++) {
        value = PySequence_Fast_GET_ITEM(instance_variables, i);

        if (!PyObjCInstanceVariable_Check(value)) {
            continue;
        }

        char*  type;
        size_t size;
        size_t align;

        if (PyObjCInstanceVariable_IsSlot(value)) {
            type = @encode(PyObject*);
            size = sizeof(PyObject*);
        } else {
            type = PyObjCInstanceVariable_GetType(value);
            if (type == NULL) {
                goto error_cleanup;
            }
            size = PyObjCRT_SizeOfType(type);
        }
        align = PyObjCRT_AlignOfType(type);

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
    for (i = 0; i < PySequence_Fast_GET_SIZE(instance_methods); i++) {
        value = PySequence_Fast_GET_ITEM(instance_methods, i);

        if (!PyObjCSelector_Check(value)) {
            continue;
        }

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
    for (i = 0; i < PySequence_Fast_GET_SIZE(class_methods); i++) {
        value = PySequence_Fast_GET_ITEM(class_methods, i);

        if (!PyObjCSelector_Check(value)) {
            continue;
        }

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

    if (PyDict_DelItemString(class_dict, "__dict__") < 0) {
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

    if (key_list) {
        Py_DECREF(key_list);
        key_list = NULL;
    }

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
                if (s != NULL) {
                    /* XXX: Why not use Vectorcall uncondationally (through compat layer
                     * on py3.8 and earlier)? */
#if PY_VERSION_HEX >= 0x03090000
                    PyObject* args[2] = {NULL, s};
                    obj               = PyObject_Vectorcall(delmethod, args + 1,
                                                            1 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
#else
                    obj = PyObject_CallFunctionObjArgs(delmethod, s, NULL);
#endif
                    _PyObjCObject_FreeDeallocHelper(s);
                    if (obj == NULL) {
                        PyErr_WriteUnraisable(delmethod);
                    } else {
                        Py_DECREF(obj);
                    }
                    Py_DECREF(delmethod);
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

/* -respondsToSelector: */
static void
object_method_respondsToSelector(ffi_cif* cif __attribute__((__unused__)), void* retval,
                                 void** args, void* userdata)
{
    id   self      = *(id*)args[0];
    SEL  _meth     = *(SEL*)args[1];
    SEL  aSelector = *(SEL*)args[2];
    int* p_result  = (int*)retval; /* Actually BOOL. */

    struct objc_super spr;
    PyObject*         pyself;
    PyObject*         pymeth;

    PyObjC_BEGIN_WITH_GIL
        /* First check if this class respond */

        /* XXX: Shouldn't this use id_to_python? */
        pyself = PyObjCObject_New(self, PyObjCObject_kDEFAULT, YES);
        if (pyself == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            *p_result = NO;
            PyObjC_GIL_RETURNVOID;
            // LCOV_EXCL_STOP
        }
        pymeth = PyObjCObject_FindSelector(pyself, aSelector);
        Py_DECREF(pyself);
        if (pymeth) {
            *p_result = YES;

            if (PyObjCSelector_Check(pymeth)
                && (((PyObjCSelector*)pymeth)->sel_flags
                    & PyObjCSelector_kCLASS_METHOD)) {
                *p_result = NO;
            }

            Py_DECREF(pymeth);
            PyObjC_GIL_RETURNVOID;
        }
        PyErr_Clear();

    PyObjC_END_WITH_GIL

    /* Check superclass */
    spr.super_class = (Class _Nonnull)class_getSuperclass((Class)userdata);
    spr.receiver    = self;

    *p_result = ((int (*)(struct objc_super*, SEL, SEL))objc_msgSendSuper)(&spr, _meth,
                                                                           aSelector);
    return;
}

/* -methodSignatureForSelector */
static void
object_method_methodSignatureForSelector(ffi_cif* cif __attribute__((__unused__)),
                                         void* retval, void** args, void* userdata)
{
    id  self      = *(id*)args[0];
    SEL _meth     = *(SEL*)args[1];
    SEL aSelector = *(SEL*)args[2];

    struct objc_super   spr;
    PyObject*           pyself;
    PyObject*           pymeth;
    NSMethodSignature** p_result = (NSMethodSignature**)retval;

    *p_result = nil;

    spr.super_class = class_getSuperclass((Class)userdata);
    spr.receiver    = self;

    /*
     * XXX: This checks self and super in a different order than the
     *      previous function, without a clear reason. Note that either
     *      order should work because we check that Python methods overriding
     *      an existing method have a compatible signature.
     */
    @try {
        *p_result = ((NSMethodSignature * (*)(struct objc_super*, SEL, SEL))
                         objc_msgSendSuper)(&spr, _meth, aSelector);

    } @catch (NSObject* localException) {
        *p_result = nil;
    }

    if (*p_result != nil) {
        return;
    }

    PyObjC_BEGIN_WITH_GIL
        /* XXX: Shouldn't this use id_to_python? */
        pyself = PyObjCObject_New(self, PyObjCObject_kDEFAULT, YES);
        if (pyself == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            PyErr_Clear();
            PyObjC_GIL_RETURNVOID;
            // LCOV_EXCL_STOP
        }

        pymeth = PyObjCObject_FindSelector(pyself, aSelector);
        if (!pymeth) {
            Py_DECREF(pyself);
            PyErr_Clear();
            PyObjC_GIL_RETURNVOID;
        }

    PyObjC_END_WITH_GIL

    @try {
        /* XXX: Shouldn't this be sel_native_signature? */
        *p_result = [NSMethodSignature
            signatureWithObjCTypes:((PyObjCSelector*)pymeth)->sel_python_signature];
    } @catch (NSObject* localException) {
        PyObjC_BEGIN_WITH_GIL
            Py_DECREF(pymeth);
            Py_DECREF(pyself);

        PyObjC_END_WITH_GIL
        @throw;
    }

    PyObjC_BEGIN_WITH_GIL
        Py_DECREF(pymeth);
        Py_DECREF(pyself);

    PyObjC_END_WITH_GIL
}

/* -forwardInvocation: */
static void
object_method_forwardInvocation(ffi_cif* cif __attribute__((__unused__)),
                                void* retval __attribute__((__unused__)), void** args,
                                void* userdata)
{
    id            self       = *(id*)args[0];
    SEL           _meth      = *(SEL*)args[1];
    NSInvocation* invocation = *(NSInvocation**)args[2];
    SEL           theSelector;

    PyObject*              arglist;
    PyObject*              result;
    PyObject*              v;
    BOOL                   isAlloc;
    BOOL                   isCFAlloc;
    Py_ssize_t             i;
    Py_ssize_t             len;
    PyObjCMethodSignature* signature;
    const char*            type;
    void*                  argbuf = NULL;
    int                    err;
    Py_ssize_t             arglen;
    PyObject*              pymeth;
    PyObject*              pyself;
    int                    have_output = 0;
    PyGILState_STATE       state       = PyGILState_Ensure();

    /* XXX: Shouldn't this use id_to_python? */
    pyself = PyObjCObject_New(self, PyObjCObject_kDEFAULT, YES);
    if (pyself == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyObjCErr_ToObjCWithGILState(&state);
        return;
        // LCOV_EXCL_STOP
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            theSelector = [invocation selector];
        } @catch (NSObject* localException) {
            PyGILState_Release(state);
            @throw;
        }
    Py_END_ALLOW_THREADS

    pymeth = PyObjCObject_FindSelector(pyself, theSelector);

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

    signature =
        PyObjCMethodSignature_WithMetaData(PyObjCSelector_Signature(pymeth), NULL, NO);
    len = Py_SIZE(signature);

    Py_XDECREF(pymeth);
    pymeth = NULL;

    arglist = PyList_New(1);
    if (arglist == NULL) {
        Py_DECREF(signature);
        PyObjCErr_ToObjCWithGILState(&state);
        return;
    }

    PyList_SET_ITEM(arglist, 0, pyself);
    pyself = NULL;

    for (i = 2; i < len; i++) {
        type = signature->argtype[i]->type;
        if (type == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            PyErr_SetString(PyObjCExc_InternalError, "corrupt metadata");
            Py_DECREF(arglist);
            Py_DECREF(signature);
            PyObjCErr_ToObjCWithGILState(&state);
            return;
            // LCOV_EXCL_STOP
        }

        arglen = PyObjCRT_SizeOfType(type);

        if (arglen == -1) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(arglist);
            Py_DECREF(signature);
            PyObjCErr_ToObjCWithGILState(&state);
            return;
            // LCOV_EXCL_STOP
        }

        argbuf = PyMem_Malloc(arglen + 64);

        [invocation getArgument:argbuf atIndex:i];

        /* XXX: this needs a lot of work to adapt to the new metadata!!! */

        switch (*type) {
        case _C_INOUT:
            if (type[1] == _C_PTR) {
                have_output++;
            }
            /* FALL THROUGH */
        case _C_IN:
        case _C_CONST:
            if (type[1] == _C_PTR) {
                v = pythonify_c_value(type + 2, *(void**)argbuf);
            } else {
                v = pythonify_c_value(type + 1, argbuf);
            }
            break;
        case _C_OUT:
            if (type[1] == _C_PTR) {
                have_output++;
            }
            PyMem_Free(argbuf);
            argbuf = NULL;
            v      = Py_None;
            Py_INCREF(Py_None);
            break;
        default:
            v = pythonify_c_value(type, argbuf);
        }
        PyMem_Free(argbuf);
        argbuf = NULL;

        if (v == NULL) {
            Py_DECREF(arglist);
            Py_DECREF(signature);
            PyObjCErr_ToObjCWithGILState(&state);
            return;
        }

        if (PyList_Append(arglist, v) < 0) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(arglist);
            Py_DECREF(signature);
            PyObjCErr_ToObjCWithGILState(&state);
            return;
            // LCOV_EXCL_STOP
        }
    }

    v = PyList_AsTuple(arglist);
    if (v == NULL) {
        Py_DECREF(arglist);
        Py_DECREF(signature);
        PyObjCErr_ToObjCWithGILState(&state);
        return;
    }
    Py_DECREF(arglist);
    arglist = v;
    v       = NULL;

    result = PyObjC_CallPython(self, theSelector, arglist, &isAlloc, &isCFAlloc);
    Py_DECREF(arglist);
    if (result == NULL) {
        Py_DECREF(signature);
        PyObjCErr_ToObjCWithGILState(&state);
        return;
    }

    type   = signature->rettype->type;
    arglen = PyObjCRT_SizeOfType(type);

    if (arglen == -1) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(signature);
        PyObjCErr_ToObjCWithGILState(&state);
        return;
        // LCOV_EXCL_STOP
    }

    if (!have_output) {
        if (*type != _C_VOID && *type != _C_ONEWAY) {
            argbuf = PyMem_Malloc(arglen + 64);

            err = depythonify_c_value(type, result, argbuf);
            if (err == -1) {
                PyMem_Free(argbuf);
                Py_DECREF(signature);
                PyObjCErr_ToObjCWithGILState(&state);
                return;
            }
            if (isAlloc) {
                [(*(id*)argbuf) retain];
            } else if (isCFAlloc) {
                if (*(id*)argbuf != nil) {
                    CFRetain((*(id*)argbuf));
                }
            }
            [invocation setReturnValue:argbuf];
            PyMem_Free(argbuf);
        }
        Py_DECREF(result);

    } else {
        Py_ssize_t idx;
        PyObject*  real_res;

        if (*type == _C_VOID && have_output == 1) {
            /* One output argument, and a 'void' return value,
             * the python method returned just the output
             * argument
             */
            /* XXX: This should be cleaned up, unnecessary code
             * duplication
             */

            for (i = 2; i < len; i++) {
                void* ptr;
                type = signature->argtype[i]->type;

                if (arglen == -1) { // LCOV_BR_EXCL_LINE
                    // LCOV_EXCL_START
                    Py_DECREF(signature);
                    PyObjCErr_ToObjCWithGILState(&state);
                    return;
                    // LCOV_EXCL_STOP
                }

                switch (*type) {
                case _C_INOUT:
                case _C_OUT:
                    if (type[1] != _C_PTR) {
                        continue;
                    }
                    type += 2;
                    break;
                default:
                    continue;
                }

                [invocation getArgument:&ptr atIndex:i];
                err = depythonify_c_value(type, result, ptr);
                if (err == -1) {
                    Py_DECREF(signature);
                    PyObjCErr_ToObjCWithGILState(&state);
                    return;
                }
                if (Py_REFCNT(result) == 1 && type[0] == _C_ID) {
                    /* make sure return value doesn't die before
                     * the caller can get its hands on it.
                     */
                    [[*(id*)ptr retain] autorelease];
                }

                /* We have exactly 1 output argument */
                break;
            }

            Py_DECREF(signature);
            Py_DECREF(result);
            PyGILState_Release(state);
            return;
        }

        if (*type != _C_VOID) {
            if (!PyTuple_Check(result) || PyTuple_Size(result) != have_output + 1) {
                PyErr_Format(PyExc_TypeError, "%s: Need tuple of %d arguments as result",
                             sel_getName(theSelector), have_output + 1);
                Py_DECREF(result);
                Py_DECREF(signature);
                PyObjCErr_ToObjCWithGILState(&state);
                return;
            }
            idx      = 1;
            real_res = PyTuple_GET_ITEM(result, 0);

            argbuf = PyMem_Malloc(arglen + 64);
            if (argbuf == NULL) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                PyErr_NoMemory();
                Py_DECREF(signature);
                PyObjCErr_ToObjCWithGILState(&state);
                PyMem_Free(argbuf);
                return;
                // LCOV_EXCL_STOP
            }

            err = depythonify_c_value(type, real_res, argbuf);
            if (err == -1) {
                Py_DECREF(signature);
                PyObjCErr_ToObjCWithGILState(&state);
                PyMem_Free(argbuf);
                return;
            }

            if (isAlloc) {
                [(*(id*)argbuf) retain];

            } else if (isCFAlloc) {
                CFRetain(*(id*)argbuf);
            }

            [invocation setReturnValue:argbuf];
            PyMem_Free(argbuf);

        } else {
            if (!PyTuple_Check(result) || PyTuple_Size(result) != have_output) {
                PyErr_Format(PyExc_TypeError, "%s: Need tuple of %d arguments as result",
                             sel_getName(theSelector), have_output);
                Py_DECREF(signature);
                Py_DECREF(result);
                PyObjCErr_ToObjCWithGILState(&state);
                return;
            }
            idx = 0;
        }

        for (i = 2; i < len; i++) {
            void* ptr;
            type = signature->argtype[i]->type;

            if (arglen == -1) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                Py_DECREF(signature);
                PyObjCErr_ToObjCWithGILState(&state);
                return;
                // LCOV_EXCL_STOP
            }

            switch (*type) {
            case _C_INOUT:
            case _C_OUT:
                if (type[1] != _C_PTR) {
                    continue;
                }
                type += 2;
                break;
            default:
                continue;
            }

            [invocation getArgument:&ptr atIndex:i];
            v   = PyTuple_GET_ITEM(result, idx++);
            err = depythonify_c_value(type, v, ptr);
            if (err == -1) {
                Py_DECREF(signature);
                PyObjCErr_ToObjCWithGILState(&state);
                return;
            }
            if (Py_REFCNT(v) == 1 && type[0] == _C_ID) {
                /* make sure return value doesn't die before
                 * the caller can get its hands on it.
                 */
                [[*(id*)ptr retain] autorelease];
            }
        }
        Py_DECREF(result);
    }
    Py_DECREF(signature);
    PyGILState_Release(state);
}

/*
 * XXX: Function PyObjC_CallPython should be moved
 *
 * XXX: Move API to vectorcall convention, and possibly inline in
 * its sole caller.
 */
static PyObject* _Nullable PyObjC_CallPython(id self, SEL selector, PyObject* arglist,
                                             BOOL* isAlloc, BOOL* isCFAlloc)
{
    PyObject* pyself = NULL;
    PyObject* pymeth = NULL;
    PyObject* result;

    pyself = id_to_python(self);
    if (pyself == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE
    }

    if (PyObjCClass_Check(pyself)) {
        pymeth = PyObjCClass_FindSelector(pyself, selector, YES);
    } else {
        pymeth = PyObjCObject_FindSelector(pyself, selector);
    }

    if (pymeth == NULL) {
        Py_DECREF(pyself);
        return NULL;
    }

    if (NULL != ((PyObjCSelector*)pymeth)->sel_self) {
        /* The selector is a bound selector, we didn't expect that...*/
        PyObject* arg_self;

        arg_self = PyTuple_GET_ITEM(arglist, 0);
        if (arg_self == NULL) {
            return NULL;
        }
        if (arg_self != ((PyObjCSelector*)pymeth)->sel_self) {

            PyErr_SetString(PyExc_TypeError, "PyObjC_CallPython called with 'self' and "
                                             "a method bound to another object");
            return NULL;
        }

        arglist = PyTuple_GetSlice(arglist, 1, PyTuple_Size(arglist));
        if (arglist == NULL) {
            return NULL;
        }
    } else {
        Py_INCREF(arglist);
    }

    if (isAlloc != NULL) {
        PyObjCMethodSignature* methinfo = PyObjCSelector_GetMetadata(pymeth);
        if (methinfo == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(arglist);
            Py_DECREF(pymeth);
            Py_DECREF(pyself);
            return NULL;
            // LCOV_EXCL_STOP

        } else {
            *isAlloc = methinfo->rettype->alreadyRetained;
        }
    }

    if (isCFAlloc != NULL) {
        PyObjCMethodSignature* methinfo = PyObjCSelector_GetMetadata(pymeth);
        if (methinfo == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(arglist);
            Py_DECREF(pymeth);
            Py_DECREF(pyself);
            return NULL;
            // LCOV_EXCL_STOP
        } else {
            *isCFAlloc = methinfo->rettype->alreadyCFRetained;
        }
    }

    result = PyObject_Call(pymeth, arglist, NULL);
    Py_DECREF(arglist);
    Py_DECREF(pymeth);
    Py_DECREF(pyself);

    /* XXX: This test is spurious, remove once test coverage is ok */
    if (result == NULL) {
        return NULL;
    }

    return result;
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
         * NOTE: We have to be extermely careful in here, some classes,
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
