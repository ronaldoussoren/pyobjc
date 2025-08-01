/*
 * Implementation of the class PyObjCClass_Type, that is the class representing
 * Objective-C classes.
 *
 */
#include "pyobjc.h"

#include <stddef.h>

NS_ASSUME_NONNULL_BEGIN

int
PyObjCClass_SetHidden(PyObject* tp, SEL sel, BOOL classMethod, PyObject* metadata)
{
    PyObject* hidden;
    PyObject* v;
    int       r;

    if (classMethod) {
        hidden = ((PyObjCClassObject*)tp)->hiddenClassSelectors;
        assert(hidden != NULL);

    } else {
        hidden = ((PyObjCClassObject*)tp)->hiddenSelectors;
        assert(hidden != NULL);
    }

    v = PyBytes_FromString(sel_getName(sel));
    if (v == NULL) { // LCOV_BR_EXCL_LINE
        return -1;   // LCOV_EXCL_LINE
    }
    r = PyDict_SetItem(hidden, v, metadata);
    Py_DECREF(v);
    return r;
}

PyObject* _Nullable PyObjCClass_HiddenSelector(PyObject* tp, SEL sel, BOOL classMethod)
{
    PyObject*  mro;
    Py_ssize_t i, n;
    if (tp == NULL) {
        return NULL;
    }

    mro = ((PyTypeObject*)tp)->tp_mro;
    if (mro == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;   // LCOV_EXCL_LINE
    }

    assert(PyTuple_Check(mro));
    n = PyTuple_GET_SIZE(mro);
    for (i = 0; i < n; i++) {
        PyObject* base = PyTuple_GET_ITEM(mro, i);
        if (PyObjCClass_Check(base)) {
            PyObject* hidden;

            if (classMethod) {
                hidden = ((PyObjCClassObject*)base)->hiddenClassSelectors;

            } else {
                hidden = ((PyObjCClassObject*)base)->hiddenSelectors;
            }

            if (hidden != NULL) {
                PyObject* v = PyBytes_FromString(sel_getName(sel));

                if (v == NULL) {   // LCOV_BR_EXCL_LINE
                    PyErr_Clear(); // LCOV_EXCL_LINE

                } else { // LCOV_EXCL_LINE
                    PyObject* result;
                    int       r = PyDict_GetItemRef(hidden, v, &result);
                    Py_CLEAR(v);
                    switch (r) { // LCOV_BR_EXCL_LINE
                    case -1:
                        return NULL; // LCOV_EXCL_LINE
                    /* case 0: pass */
                    case 1:
                        return result;
                    }
                }
            }
        }
    }

    return NULL;
}

/*
 * Support for NSData/NSMutableData to have buffer API
 *
 */

static int
nsdata_getbuffer(PyObject* obj, Py_buffer* view, int flags)
{
    NSMutableData* self = (NSMutableData*)PyObjCObject_GetObject(obj);
    if ([self respondsToSelector:@selector(mutableBytes)]) {
        return PyBuffer_FillInfo(view, obj, (void*)[self mutableBytes], [self length], 0,
                                 flags);
    } else {
        return PyBuffer_FillInfo(view, obj, (void*)[self bytes], [self length], 1, flags);
    }
}

static PyBufferProcs nsdata_as_buffer = {
    .bf_getbuffer = nsdata_getbuffer,
};

PyDoc_STRVAR(class_doc,
             "objc_class(name, bases, dict) -> a new Objective-C class\n" CLINIC_SEP "\n"
             "objc_class is the meta-type for Objective-C classes. It should not be\n"
             "necessary to manually create instances of this type, those are \n"
             "created by subclassing and existing Objective-C class.\n"
             "\n"
             "The list of bases must start with an existing Objective-C class, and \n"
             "cannot contain other Objective-C classes. The list may contain\n"
             "informal_interface objects, those are used during the calculation of\n"
             "method signatures and will not be visible in the list of base-classes\n"
             "of the created class.");

/*
 *
 *  Class Registry
 *
 */

/*!
 * @const class_registry
 * @discussion
 *    This structure is used to keep references to all class objects created
 *    by this module. This is necessary to be able to avoid creating two
 *    wrappers for an Objective-C class.
 *
 *    The key is the Objective-C class, the value is its wrapper.
 */
#ifdef Py_GIL_DISABLED
static PyMutex registry_lock = {0};
static PyMutex classmap_lock = {0};
#endif
static NSMapTable* _Nullable class_registry     = NULL;
static NSMapTable* _Nullable metaclass_to_class = NULL;

int
PyObjCClass_Setup(PyObject* module __attribute__((__unused__)))
{
    assert(class_registry == NULL);
    assert(metaclass_to_class == NULL);

    class_registry =
        NSCreateMapTable(PyObjCUtil_PointerKeyCallBacks, PyObjCUtil_PointerValueCallBacks,
                         PYOBJC_EXPECTED_CLASS_COUNT);
    if (class_registry == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_SetString(PyObjCExc_InternalError, "Cannot create class registry");
        return -1;
        // LCOV_EXCL_STOP
    }

    metaclass_to_class =
        NSCreateMapTable(PyObjCUtil_PointerKeyCallBacks, PyObjCUtil_PointerValueCallBacks,
                         PYOBJC_EXPECTED_CLASS_COUNT);
    if (metaclass_to_class == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_SetString(PyObjCExc_InternalError, "Cannot create metaclass registry");
        return -1;
        // LCOV_EXCL_STOP
    }

    return 0;
}

/*!
 * @function objc_class_register
 * @abstract Add a class to the class registry
 * @param objc_class An Objective-C class
 * @param py_class   The python wrapper for the Objective-C class
 *
 * Returns a new reference to the registered class,
 * which can be a
 */
static PyObject* __attribute__((warn_unused_result))
objc_class_register(Class objc_class, PyObject* py_class)
{
    assert(class_registry != NULL);

#ifdef Py_GIL_DISABLED
    PyMutex_Lock(&registry_lock);
#endif
    PyObject* existing = NSMapGet(class_registry, objc_class);
    if (existing) {
        Py_INCREF(existing);
#ifdef Py_GIL_DISABLED
        PyMutex_Unlock(&registry_lock);
#endif
        return existing;
    }

    Py_INCREF(py_class);
    NSMapInsert(class_registry, objc_class, py_class);

#ifdef Py_GIL_DISABLED
    PyMutex_Unlock(&registry_lock);
#endif

    Py_INCREF(py_class);
    return py_class;
}

/*
 * Register a meta_class with metaclass registry
 *
 * This also registers the metaclass in the regular registry.
 *
 * Note: objc_class_register is inlined in this function to
 *       get the locking right.
 */
static PyTypeObject* _Nullable __attribute__((warn_unused_result))
objc_metaclass_register(PyTypeObject* meta_class, Class objc_class, Class objc_meta_class)
{
    assert(metaclass_to_class != NULL);

#ifdef Py_GIL_DISABLED
    PyMutex_Lock(&classmap_lock);
    PyMutex_Lock(&registry_lock);
#endif

    PyObject* existing_class = NSMapGet(class_registry, objc_meta_class);
    if (existing_class) {
        meta_class = (PyTypeObject*)existing_class;
    } else {
        Py_INCREF(meta_class);
        NSMapInsert(class_registry, objc_meta_class, meta_class);
    }

    Class existing_meta = NSMapGet(metaclass_to_class, meta_class);
    if (existing_meta) {
        if (existing_class) {
            Py_INCREF(meta_class);
#ifdef Py_GIL_DISABLED
            PyMutex_Unlock(&registry_lock);
            PyMutex_Unlock(&classmap_lock);
#endif
            return meta_class;
        } else {
            PyErr_Format(PyObjCExc_InternalError, "Registering metaclass twice for '%s'",
                         class_getName(existing_meta));
#ifdef Py_GIL_DISABLED
            PyMutex_Unlock(&registry_lock);
            PyMutex_Unlock(&classmap_lock);
#endif
            return NULL;
        }
        // LCOV_EXCL_STOP
    }

    Py_INCREF(meta_class);
    NSMapInsert(metaclass_to_class, meta_class, objc_class);

    Py_INCREF(meta_class);
#ifdef Py_GIL_DISABLED
    PyMutex_Unlock(&registry_lock);
    PyMutex_Unlock(&classmap_lock);
#endif
    return meta_class;
}

static Class _Nullable objc_metaclass_locate(PyObject* meta_class)
{
    Class result;

    if (metaclass_to_class == NULL) // LCOV_BR_EXCL_LINE
        return NULL;                // LCOV_EXCL_LINE
    if (meta_class == NULL)         // LCOV_BR_EXCL_LINE
        return NULL;                // LCOV_EXCL_LINE

#ifdef Py_GIL_DISABLED
    PyMutex_Lock(&classmap_lock);
#endif
    result = NSMapGet(metaclass_to_class, meta_class);
#ifdef Py_GIL_DISABLED
    PyMutex_Unlock(&classmap_lock);
#endif
    return result;
}

/*!
 * @function objc_class_locate
 * @abstract Find the Python wrapper for an Objective-C class
 * @param objc_class An Objective-C class
 * @result Returns the Python wrapper for the class, or NULL
 * @discussion
 *     This function does not raise an Python exception when the
 *     wrapper cannot be found.
 *
 * XXX: Is this function needed? Why not use the same registry
 *      as used by objc-object?
 */
PyObject* _Nullable objc_class_locate(Class objc_class)
{
    PyObject* result;

    if (objc_class == NULL) // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE

#ifdef Py_GIL_DISABLED
    PyMutex_Lock(&registry_lock);
#endif
    result = NSMapGet(class_registry, objc_class);
    Py_XINCREF(result);
#ifdef Py_GIL_DISABLED
    PyMutex_Unlock(&registry_lock);
#endif
    return result;
}

/* Create a new objective-C metaclass proxy
 *
 * Returns a new reference.
 */
static PyTypeObject* _Nullable PyObjCClass_NewMetaClass(Class objc_class)
{
    PyTypeObject* result;
    Class         objc_meta_class = object_getClass(objc_class);

    if (unlikely(class_isMetaClass(objc_class))) {
        objc_meta_class = objc_class;
    }

    if (objc_meta_class == nil) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_INCREF(&PyObjCClass_Type);
        return &PyObjCClass_Type;
        // LCOV_EXCL_STOP
    }

    /* Create a metaclass proxy for the metaclass of the given class */
    result = (PyTypeObject*)objc_class_locate(objc_meta_class);
    if (result != NULL) {
        return result;
    }

    Class super_class = nil;

    if (unlikely(class_isMetaClass(objc_class))) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        super_class = class_getSuperclass(objc_meta_class);
        if (!class_isMetaClass(super_class)) {
            /* NSObject's metaclass inherits from NSObject, don't
             * model that in Python. */
            super_class = nil;
        }
        // LCOV_EXCL_STOP

    } else { // LCOV_EXCL_LINE
        super_class = class_getSuperclass(objc_class);
    }

    PyTypeObject* py_super_class;
    if (super_class == nil) {
        Py_INCREF(&PyObjCClass_Type);
        py_super_class = &PyObjCClass_Type;

    } else {
        py_super_class = PyObjCClass_NewMetaClass(super_class);
        if (py_super_class == NULL) { // LCOV_BR_EXCL_LINE
            return NULL;              // LCOV_EXCL_LINE
        }
    }

    /* We now know the superclass of our metaclass, build the actual
     * metaclass.
     */
    PyObject* dict  = PyDict_New();
    PyObject* bases = PyTuple_New(1);

    PyTuple_SET_ITEM(bases, 0, (PyObject*)py_super_class);

    PyObject* args = PyTuple_New(3);
    PyTuple_SET_ITEM(args, 0, PyUnicode_FromString(class_getName(objc_class)));
    PyTuple_SET_ITEM(args, 1, bases);
    PyTuple_SET_ITEM(args, 2, dict);

    result = (PyTypeObject*)PyType_Type.tp_new(&PyType_Type, args, NULL);
    Py_DECREF(args);
    if (result == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE
    }

    ((PyObjCClassObject*)result)->class = objc_meta_class;

    PyTypeObject* existing = objc_metaclass_register(result, objc_class, objc_meta_class);
    if (existing == NULL) { // LCOV_BR_EXCL_LINE
        // Can only happen with double registration, which would
        // be a bug.
        return NULL; // LCOV_EXCL_LINE
    }
    Py_DECREF(result);
    return existing;
}

static PyObject* _Nullable class_call(PyObject* self, PyObject* _Nullable args,
                                      PyObject* _Nullable kwds)
{
    PyTypeObject* type = (PyTypeObject*)self;
    PyObject*     result;

    if (type->tp_new == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_Format(PyExc_TypeError, "cannot create '%s' instances", type->tp_name);
        return NULL;
        // LCOV_EXCL_STOP
    }

    result = type->tp_new(type, args, kwds);
    if (result == NULL) {
        return result;
    }

    if (PyObject_TypeCheck(result, type) == 0) {
        return result;
    }

    PyObject* new = PyObject_GetAttr((PyObject*)type, PyObjCNM___new__);
    if (new == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(result);
        return NULL;
        // LCOV_EXCL_STOP
    }

    int r = PyObjC_IsGenericNew(new);
    if (r == -1) {
        Py_DECREF(new);
        Py_DECREF(result);
        return NULL;
    } else if (r) {
        /* the __new__ of the class is the default __new__,
         * don't call __init__.
         */
        return result;
    }

    type = Py_TYPE(result);
    if (type->tp_init != NULL) {
        int res = type->tp_init(result, args, kwds);
        if (res == -1) {
            Py_SETREF(result, NULL);
        }
    }
    return result;
}

static int
class_init(PyObject* cls, PyObject* args, PyObject* kwds)
{
    if (kwds != NULL) {
        if (PyDict_Check(kwds) && PyDict_Size(kwds) == 1) {

            PyObject* v;

            switch (
                PyDict_GetItemRef(kwds, PyObjCNM_protocols, &v)) { // LCOV_BR_EXCL_LINE
            case -1:
                return -1; // LCOV_EXCL_LINE
            /* case 0: pass */
            case 1:
                Py_DECREF(v);
                return PyType_Type.tp_init(cls, args, NULL);
            }
        }
    } // LCOV_EXCL_LINE
    return PyType_Type.tp_init(cls, args, kwds);
}

/*
 * class_new: Create a new objective-C class, as a subclass of 'type'. This is
 * PyObjCClass_Type.tp_new.
 *
 * Note: This function creates new _classes_
 */

static PyObject* _Nullable class_new(PyTypeObject* type __attribute__((__unused__)),
                                     PyObject* _Nullable args, PyObject* _Nullable kwds)
{
    static char*       keywords[] = {"name", "bases", "dict", "protocols", "final", NULL};
    char*              name;
    PyObject*          bases;
    PyObject*          dict;
    PyObject*          old_dict;
    PyObject*          res;
    PyObject*          k;
    PyObject*          metadict;
    PyObject*          v;
    Py_ssize_t         i;
    Py_ssize_t         len;
    Class              objc_class = NULL;
    Class              super_class; /* XXX    = NULL; */
    PyObject*          py_super_class = NULL;
    PyObjCClassObject* info;
    PyObject*          keys;
    PyObject*          protocols;
    PyObject*          real_bases;
    PyObject*          delmethod;
    PyObject*          useKVOObj;
    Ivar               var;
    PyObject*          hiddenSelectors      = NULL;
    PyObject*          hiddenClassSelectors = NULL;
    PyObject*          arg_protocols        = NULL;
    BOOL               isCFProxyClass       = NO;
    int                r;
    int                final          = 0;
    int                has_dunder_new = 0;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "sOO|Op", keywords, &name, &bases, &dict,
                                     &arg_protocols, &final)) {
        return NULL;
    }
    assert(name != NULL);
    assert(bases != NULL);
    assert(dict != NULL);

    if (!PyTuple_Check(bases)) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_SetString(PyExc_TypeError, "'bases' must be tuple");
        return NULL;
        // LCOV_EXCL_STOP
    }

    len = PyTuple_Size(bases);
    if (len < 1) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_SetString(PyExc_TypeError, "'bases' must not be empty");
        return NULL;
        // LCOV_EXCL_STOP
    }

    py_super_class = PyTuple_GET_ITEM(bases, 0);
    assert(py_super_class != NULL);

    if (py_super_class == PyObjC_NSCFTypeClass) {
        /* A new subclass of NSCFType
         * -> a new proxy type for CoreFoundation classes
         */
        isCFProxyClass = YES;
    }

    if (!PyObjCClass_Check(py_super_class)) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_SetString(PyExc_TypeError, "first base class must "
                                         "be objective-C based");
        return NULL;
        // LCOV_EXCL_STOP
    }
    if (py_super_class == (PyObject*)&PyObjCObject_Type) {
        PyErr_SetString(PyExc_TypeError, "Cannot directly inherit from objc.objc_object");
        return NULL;
    }

    if (PyObjCClass_IsFinal((PyTypeObject*)py_super_class)) {
        PyErr_Format(PyExc_TypeError, "super class %s is final",
                     ((PyTypeObject*)py_super_class)->tp_name);
        return NULL;
    }

    super_class = PyObjCClass_GetClass(py_super_class);
    if (super_class == Nil) { // LCOV_BR_EXCL_LINE
        /* This will always set an exception, only the root has
         * a Nil class and that's excluded above.
         */
        // LCOV_EXCL_START
        assert(PyErr_Occurred());
        return NULL;
        // LCOV_EXCL_STOP
    }
    if (PyObjCClass_CheckMethodList(py_super_class, 1) < 0) {
        return NULL;
    }

    hiddenSelectors = PyDict_New();
    if (hiddenSelectors == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        return NULL;
        // LCOV_EXCL_STOP
    }

    hiddenClassSelectors = PyDict_New();
    if (hiddenClassSelectors == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(hiddenSelectors);
        return NULL;
        // LCOV_EXCL_STOP
    }

    /*
     * __pyobjc_protocols__ contains the list of protocols supported
     * by an existing class.
     */
    protocols = PyObject_GetAttrString(py_super_class, "__pyobjc_protocols__");
    if (protocols == NULL) {
        PyErr_Clear();
        protocols = PyList_New(0);
        if (protocols == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(hiddenSelectors);
            Py_DECREF(hiddenClassSelectors);
            return NULL;
            // LCOV_EXCL_STOP
        }

    } else {
        PyObject*  seq;
        Py_ssize_t protocols_len;

        seq = PyObjCSequence_Tuple(protocols, "__pyobjc_protocols__ not a sequence");
        if (seq == NULL) {
            Py_DECREF(hiddenSelectors);
            Py_DECREF(hiddenClassSelectors);
            Py_DECREF(protocols);
            return NULL;
        }

        Py_DECREF(protocols);

        protocols_len = PyTuple_GET_SIZE(seq);
        protocols     = PyList_New(0);
        if (protocols == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(hiddenSelectors);
            Py_DECREF(hiddenClassSelectors);
            return NULL;
            // LCOV_EXCL_STOP
        }

        for (i = 0; i < protocols_len; i++) {
            if (PyList_Append(protocols, PyTuple_GET_ITEM(seq, i))
                < 0) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                Py_DECREF(hiddenSelectors);
                Py_DECREF(hiddenClassSelectors);
                return NULL;
                // LCOV_EXCL_STOP
            }
        }

        Py_DECREF(seq);
    }

    real_bases = PyList_New(0);
    if (real_bases == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(protocols);
        Py_DECREF(hiddenSelectors);
        Py_DECREF(hiddenClassSelectors);
        return NULL;
        // LCOV_EXCL_STOP
    }

    if (PyList_Append(real_bases, py_super_class) == -1) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(hiddenSelectors);
        Py_DECREF(hiddenClassSelectors);
        Py_DECREF(protocols);
        Py_DECREF(real_bases);
        return NULL;
        // LCOV_EXCL_STOP
    }

    for (i = 1; i < len; i++) {
        v = PyTuple_GET_ITEM(bases, i);
        assert(v != NULL);

        if (PyObjCClass_Check(v)) {
            Py_DECREF(protocols);
            Py_DECREF(real_bases);
            Py_DECREF(hiddenSelectors);
            Py_DECREF(hiddenClassSelectors);
            PyErr_SetString(PyExc_TypeError, "multiple objective-C bases");
            return NULL;

        } else {
            r = PyList_Append(real_bases, v);

            if (r == -1) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                Py_DECREF(protocols);
                Py_DECREF(real_bases);
                Py_DECREF(hiddenSelectors);
                Py_DECREF(hiddenClassSelectors);
                // LCOV_EXCL_STOP
            } // LCOV_EXCL_LINE
        }
    }

    if (arg_protocols != NULL) {
        PyObject* args[] = {NULL, protocols, arg_protocols};

        PyObject* r = PyObject_VectorcallMethod(PyObjCNM_extend, args + 1,
                                                2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
        if (r == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(protocols);
            Py_DECREF(real_bases);
            Py_DECREF(hiddenSelectors);
            Py_DECREF(hiddenClassSelectors);
            return NULL;
            // LCOV_EXCL_STOP
        }
        Py_DECREF(r);
    }

    /* Also look for '__pyobjc_protocols__' in the class dictionary. */
    switch (PyDict_GetItemRef(dict, PyObjCNM___pyobjc_protocols__,
                              &arg_protocols)) { // LCOV_BR_EXCL_LINE
    case -1:
        // LCOV_EXCL_START
        Py_DECREF(protocols);
        Py_DECREF(real_bases);
        Py_DECREF(hiddenSelectors);
        Py_DECREF(hiddenClassSelectors);
        return NULL;
        // LCOV_EXCL_STOP
    /* case 0: pass */
    case 1: {
        PyObject* args[] = {NULL, protocols, arg_protocols};

        PyObject* r = PyObject_VectorcallMethod(PyObjCNM_extend, args + 1,
                                                2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
        if (r == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(arg_protocols);
            Py_DECREF(protocols);
            Py_DECREF(real_bases);
            Py_DECREF(hiddenSelectors);
            Py_DECREF(hiddenClassSelectors);
            return NULL;
            // LCOV_EXCL_STOP
        }
        Py_DECREF(r);
        Py_CLEAR(arg_protocols);
    }
    }

    metadict = PyDict_New();
    if (metadict == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(protocols);
        Py_DECREF(real_bases);
        Py_DECREF(hiddenSelectors);
        Py_DECREF(hiddenClassSelectors);
        return NULL;
        // LCOV_EXCL_STOP
    }

    /* Save the value of __slots__ to make it possible to restore
     * the original value after creating the Python class.
     *
     * PyObjCClass_BuildClass will reset __slots__ in the dict
     * to ensure that the Python proxy class will have no instance
     * variables.
     */
    PyObject* orig_slots;
    switch (
        PyDict_GetItemRef(dict, PyObjCNM___slots__, &orig_slots)) { // LCOV_BR_EXCL_LINE
    case -1:
        // LCOV_EXCL_START
        Py_DECREF(protocols);
        Py_DECREF(metadict);
        Py_DECREF(real_bases);
        Py_DECREF(hiddenSelectors);
        Py_DECREF(hiddenClassSelectors);
        return NULL;
        // LCOV_EXCL_STOP
        /* case 0: pass */
        /* case 1: pass */
    }

    if (isCFProxyClass) {
        objc_class = nil;

    } else {
        /* First generate the objective-C class. This may change the
         * class dict.
         */
        objc_class = PyObjCClass_BuildClass(super_class, protocols, name, dict, metadict,
                                            hiddenSelectors, hiddenClassSelectors,
                                            &has_dunder_new);
        if (objc_class == Nil) {
            Py_XDECREF(orig_slots);
            Py_DECREF(protocols);
            Py_DECREF(metadict);
            Py_DECREF(real_bases);
            Py_DECREF(hiddenSelectors);
            Py_DECREF(hiddenClassSelectors);
            return NULL;
        }

        /* PyObjCClass_BuildClass may have changed the super_class */
        /* This is a subclass of an existing class, the superclass will never be Nil */
        super_class    = (Class _Nonnull)class_getSuperclass(objc_class);
        py_super_class = PyObjCClass_New(super_class);
        if (py_super_class == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            assert(objc_class != Nil);
            (void)PyObjCClass_UnbuildClass(objc_class);
            Py_XDECREF(orig_slots);
            Py_DECREF(protocols);
            Py_DECREF(real_bases);
            Py_DECREF(metadict);
            Py_DECREF(hiddenSelectors);
            Py_DECREF(hiddenClassSelectors);
            return NULL;
            // LCOV_EXCL_STOP

        } else {
            if (PyObjCClass_CheckMethodList(py_super_class, 1) < 0) {
                assert(objc_class != Nil);
                (void)PyObjCClass_UnbuildClass(objc_class);
                Py_XDECREF(orig_slots);
                Py_DECREF(protocols);
                Py_DECREF(real_bases);
                Py_DECREF(metadict);
                Py_DECREF(hiddenSelectors);
                Py_DECREF(hiddenClassSelectors);
                return NULL;
            }
        }

        if (PyList_SetItem(real_bases, 0, py_super_class) < 0) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            assert(objc_class != Nil);
            (void)PyObjCClass_UnbuildClass(objc_class);
            Py_XDECREF(orig_slots);
            Py_DECREF(protocols);
            Py_DECREF(real_bases);
            Py_DECREF(metadict);
            Py_DECREF(hiddenSelectors);
            Py_DECREF(hiddenClassSelectors);
            return NULL;
            // LCOV_EXCL_STOP
        }
    }

    v = PyList_AsTuple(real_bases);
    if (v == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        if (objc_class != nil) {
            (void)PyObjCClass_UnbuildClass(objc_class);
        }
        Py_XDECREF(orig_slots);
        Py_DECREF(metadict);
        Py_DECREF(protocols);
        Py_DECREF(real_bases);
        Py_DECREF(hiddenSelectors);
        Py_DECREF(hiddenClassSelectors);
        return NULL;
        // LCOV_EXCL_STOP
    }
    Py_DECREF(real_bases);
    real_bases = v;

    /*
     * add __pyobjc_protocols__ to the class-dict.
     *
     * XXX: Move into python
     */
    v = PyList_AsTuple(protocols);
    if (v == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_XDECREF(orig_slots);
        Py_DECREF(real_bases);
        Py_DECREF(protocols);
        Py_DECREF(metadict);
        Py_DECREF(hiddenSelectors);
        Py_DECREF(hiddenClassSelectors);
        if (objc_class != Nil) {
            (void)PyObjCClass_UnbuildClass(objc_class);
        }
        return NULL;
        // LCOV_EXCL_STOP
    }

    if (PyDict_SetItem( // LCOV_BR_EXCL_LINE
            dict, PyObjCNM___pyobjc_protocols__, v)
        == -1) {
        // LCOV_EXCL_START
        Py_XDECREF(orig_slots);
        Py_DECREF(v);
        Py_DECREF(real_bases);
        Py_DECREF(protocols);
        Py_DECREF(metadict);
        Py_DECREF(hiddenSelectors);
        Py_DECREF(hiddenClassSelectors);
        if (objc_class != Nil) {
            (void)PyObjCClass_UnbuildClass(objc_class);
        }
        return NULL;
        // LCOV_EXCL_STOP
    }

    Py_DECREF(v);

    /*
     * Users can define a __del__ method. We special-case this to
     * avoid triggering the default mechanisms for this method: The
     * method should only be called when the Objective-C side of the
     * instance is deallocated, not whenever the Python proxy is.
     */
    switch (PyDict_GetItemRef(dict, PyObjCNM___del__, &delmethod)) { // LCOV_BR_EXCL_LINE
    case -1:
        // LCOV_EXCL_START
        Py_XDECREF(orig_slots);
        Py_DECREF(protocols);
        Py_DECREF(real_bases);
        Py_DECREF(metadict);
        Py_DECREF(hiddenSelectors);
        Py_DECREF(hiddenClassSelectors);
        return NULL;
        // LCOV_EXCL_STOP
    /* case 0: pass */
    case 1:
        if (isCFProxyClass) {
            /* XXX: Needs documentation on why this isn't possible */
            PyErr_SetString(PyObjCExc_Error,
                            "cannot define __del__ on subclasses of NSCFType");
            Py_XDECREF(delmethod);
            Py_XDECREF(orig_slots);
            Py_DECREF(protocols);
            Py_DECREF(real_bases);
            Py_DECREF(metadict);
            Py_DECREF(hiddenSelectors);
            Py_DECREF(hiddenClassSelectors);
            return NULL;

        } else {
            if (PyDict_DelItem(dict, PyObjCNM___del__) < 0) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                if (objc_class != nil) {
                    (void)PyObjCClass_UnbuildClass(objc_class);
                }
                Py_XDECREF(orig_slots);
                Py_DECREF(protocols);
                Py_DECREF(real_bases);
                Py_DECREF(metadict);
                Py_DECREF(hiddenSelectors);
                Py_DECREF(hiddenClassSelectors);
                Py_DECREF(delmethod);
                return NULL;
                // LCOV_EXCL_STOP
            }
        }
    }

    /* Add convenience methods like '__eq__'. Must do it before
     * call to super-class implementation, because '__*' methods
     * are treated specially there.
     */
    old_dict = PyDict_Copy(dict);
    if (old_dict == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        if (objc_class != nil) {
            (void)PyObjCClass_UnbuildClass(objc_class);
        }
        Py_XDECREF(orig_slots);
        Py_DECREF(protocols);
        Py_DECREF(real_bases);
        Py_DECREF(metadict);
        Py_DECREF(hiddenSelectors);
        Py_DECREF(hiddenClassSelectors);
        return NULL;
        // LCOV_EXCL_STOP
    }

    PyObject* bundleForClass = PyObjC_GetBundleForClassMethod();
    if (bundleForClass != NULL) {
        if (PyObjCPythonSelector_Check(bundleForClass)) {
            ((PyObjCSelector*)bundleForClass)->sel_class = objc_class;
        }

        r = PyDict_SetItem(dict, PyObjCNM_bundleForClass, bundleForClass);
        Py_CLEAR(bundleForClass);
        if (r == -1) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            if (objc_class != Nil) {
                (void)PyObjCClass_UnbuildClass(objc_class);
            }
            Py_XDECREF(orig_slots);
            Py_DECREF(old_dict);
            Py_DECREF(protocols);
            Py_DECREF(real_bases);
            Py_DECREF(metadict);
            Py_DECREF(hiddenSelectors);
            Py_DECREF(hiddenClassSelectors);
            return NULL;
            // LCOV_EXCL_STOP
        }

    } else if (PyErr_Occurred()) {
        if (objc_class != Nil) {
            (void)PyObjCClass_UnbuildClass(objc_class);
        }
        Py_XDECREF(orig_slots);
        Py_DECREF(old_dict);
        Py_DECREF(protocols);
        Py_DECREF(real_bases);
        Py_DECREF(metadict);
        Py_DECREF(hiddenSelectors);
        Py_DECREF(hiddenClassSelectors);
        return NULL;
    }

    PyTypeObject* metatype;
    if (objc_class != nil) {
        metatype = PyObjCClass_NewMetaClass(objc_class);
        if (metatype == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_XDECREF(orig_slots);
            Py_DECREF(old_dict);
            Py_DECREF(protocols);
            Py_DECREF(real_bases);
            Py_DECREF(metadict);
            Py_DECREF(hiddenSelectors);
            Py_DECREF(hiddenClassSelectors);
            return NULL;
            // LCOV_EXCL_STOP
        }

        if (PyDict_Update( // LCOV_BR_EXCL_LINE
                metatype->tp_dict, metadict)
            == -1) {
            // LCOV_EXCL_START
            Py_XDECREF(orig_slots);
            Py_DECREF(old_dict);
            Py_DECREF(protocols);
            Py_DECREF(real_bases);
            Py_DECREF(metadict);
            Py_DECREF(hiddenSelectors);
            Py_DECREF(hiddenClassSelectors);
            return NULL;
            // LCOV_EXCL_STOP
        }

    } else {
        metatype = Py_TYPE(PyObjC_NSCFTypeClass);
        Py_INCREF(metatype);
    }
    Py_DECREF(metadict);
    metadict = NULL;

    /* call super-class implementation */
    args = Py_BuildValue("(sOO)", name, real_bases, dict);
    if (args == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_XDECREF(orig_slots);
        Py_DECREF(metatype);
        Py_DECREF(real_bases);
        Py_DECREF(protocols);
        Py_DECREF(old_dict);
        Py_DECREF(hiddenSelectors);
        Py_DECREF(hiddenClassSelectors);
        return NULL;
        // LCOV_EXCL_STOP
    }

    /* The actual superclass might be different due to introduction
     * of magic intermediate classes, therefore explicitly refer to the
     * metatype we just created.
     */
    res = PyType_Type.tp_new(metatype, args, NULL);
    Py_DECREF(metatype);
    if (res == NULL) {
        Py_XDECREF(orig_slots);
        Py_DECREF(args);
        Py_DECREF(real_bases);
        Py_DECREF(protocols);
        Py_DECREF(old_dict);
        Py_DECREF(hiddenSelectors);
        Py_DECREF(hiddenClassSelectors);
        if (objc_class != Nil) {
            (void)PyObjCClass_UnbuildClass(objc_class);
        }
        return NULL;
    }
    Py_CLEAR(args);
    Py_CLEAR(real_bases);
    Py_CLEAR(protocols);

    if (orig_slots != NULL) {
        /* Restore the initial value of __slots__ */
        if (PyObject_SetAttrString( // LCOV_BR_EXCL_LINE
                res, "__slots__", orig_slots)
            == -1) {
            // LCOV_EXCL_START
            Py_XDECREF(orig_slots);
            Py_DECREF(old_dict);
            Py_DECREF(hiddenSelectors);
            Py_DECREF(hiddenClassSelectors);
            if (objc_class != Nil) {
                (void)PyObjCClass_UnbuildClass(objc_class);
            }
            return NULL;
            // LCOV_EXCL_STOP
        }
        Py_DECREF(orig_slots);
        orig_slots = NULL;
    }

    if (objc_class != nil) {
        /* Register the proxy as soon as possible, we can get
         * initialize calls very early on with the ObjC 2.0 runtime.
         */
        PyObject* actual = PyObjC_RegisterPythonProxy(objc_class, res);
        if (actual != res) { // LCOV_BR_EXCL_LINE
            /* This should never happen, *objc_class* was created by this
             * function.
             *
             * Note that *objc_registerClassPair* hasn't been called at
             * this point, which should avoid races with code introspecting
             * the available classes.
             */
            // LCOV_EXCL_START
            Py_DECREF(res);
            Py_DECREF(actual);
            return PyErr_Format(
                PyObjCExc_Error,
                "Race between creating and registering an ObjC class '%s'\n",
                class_getName(objc_class));
            // LCOV_EXCL_STOP
        }
        Py_DECREF(actual);

        PyObject* existing = objc_class_register(objc_class, res);
        assert(existing != NULL);
        if (existing != res) {
            /*
             * XXX: Can this happen?
             *
             * Possibly if a call of this function races objc.getClassList
             */
            Py_CLEAR(res);
            return existing;
        } else {
            Py_CLEAR(existing);
        }

        PyObjCClass_FinishClass(objc_class);
    }

    info        = (PyObjCClassObject*)res;
    info->class = objc_class;
    if (isCFProxyClass) {
        info->class = PyObjCClass_GetClass(PyObjC_NSCFTypeClass);
    }
    info->sel_to_py            = NULL;
    info->dictoffset           = 0;
    info->useKVO               = 0;
    info->delmethod            = delmethod;
    info->hasPythonImpl        = 1;
    info->isCFWrapper          = 0;
    info->isFinal              = final;
    info->hiddenSelectors      = hiddenSelectors;
    info->hiddenClassSelectors = hiddenClassSelectors;
#ifdef PyObjC_ENABLE_LOOKUP_CACHE
    info->lookup_cache = NULL;
#endif

    var = class_getInstanceVariable(objc_class, "__dict__");
    if (var != NULL) {
        info->dictoffset = ivar_getOffset(var);
    }

    switch (
        PyDict_GetItemRef(dict, PyObjCNM___useKVO__, &useKVOObj)) { // LCOV_BR_EXCL_LINE
    case -1:
        // LCOV_EXCL_START
        Py_DECREF(old_dict);
        return NULL;
        // LCOV_EXCL_STOP
    case 0:
        info->useKVO = PyObjC_UseKVO;
        break;
    case 1: {
        int useKVO = PyObject_IsTrue(useKVOObj);
        if (useKVO == -1) {
            return NULL;
        }
        info->useKVO = useKVO;
        Py_CLEAR(useKVOObj);
    }
    }

    if (isCFProxyClass) {
        /* Disable automatic KVO on pure CoreFoundation types */
        info->useKVO = 0;
    }
    keys = PyDict_Keys(dict);
    if (keys == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(old_dict);
        return NULL;
        // LCOV_EXCL_STOP
    }

    /* Merge the "difference" to pick up new selectors */
    for (i = 0; i < PyList_Size(keys); i++) {
        k = PyList_GetItemRef(keys, i);
        if (k == NULL) { // LCOV_BR_EXCL_LINE
            /* This failing requires changes to 'keys'
             * while iterating, while 'keys' is a new
             * list returned from 'PyDict_Keys'.
             */
            // LCOV_EXCL_START
            Py_DECREF(old_dict);
            Py_DECREF(keys);
            return NULL;
            // LCOV_EXCL_STOP
        }

        PyObject* old_v;
        switch (PyDict_GetItemRef(old_dict, k, &old_v)) { // LCOV_BR_EXCL_LINE
        case -1:
            // LCOV_EXCL_START
            /* XXX: Check refcounts, old_dict */
            return NULL;
            // LCOV_EXCL_STOP
        case 0:

            switch (PyDict_GetItemRef(dict, k, &v)) { // LCOV_BR_EXCL_LINE
            case -1:
                // LCOV_EXCL_START
                /* XXX: Check refcounts, old_dict */
                return NULL;
                // LCOV_EXCL_STOP
            /* case 0: pass */
            case 1:
                if (PyObject_SetAttr(res, k, v) == -1) {
                    PyErr_Clear();
                }
                Py_CLEAR(v);
            }
            break;

        case 1:
            Py_CLEAR(old_v);
        }

        Py_DECREF(k);
    }

    Py_DECREF(keys);
    Py_DECREF(old_dict);

    if (PyObjCClass_CheckMethodList(res, 1) < 0) {
        Py_DECREF(res);
        return NULL;
    }

    /* This is an "extra" ref */
    Py_INCREF(res);

    assert(info->hasPythonImpl);

    if (!has_dunder_new) {
        if (PyObjC_SetDunderNew(res) == -1) {
            Py_DECREF(res);
            return NULL;
        }
    }

    Py_INCREF(res);
    return res;
}

static PyObject* _Nullable class_repr(PyObject* obj)
{
    Class cls = PyObjCClass_GetClass(obj);
    if (cls) {
        const char* nm = class_getName(cls);
        if (strstr(nm, "NSCFType") != NULL) {
            return PyUnicode_FromFormat("<core-foundation class %s at %p>",
                                        ((PyTypeObject*)obj)->tp_name, (void*)cls);

        } else {
            return PyUnicode_FromFormat("<objective-c class %s at %p>", nm, (void*)cls);
        }
    } else {
        return PyUnicode_FromFormat("<class %s", ((PyTypeObject*)obj)->tp_name);
    }
}

static void
class_dealloc(PyObject* cls)
{
    PyObjCClassObject* self = (PyObjCClassObject*)cls;

    if (self->hasPythonImpl) { // LCOV_BR_EXCL_LINE
        /*
         * This is a class implemented in Python. These cannot be deallocated because
         * the state in the Objective-C runtime cannot be reverted. Deallocating the
         * Python state would therefore result in dangling pointers in the Objective-C
         * runtime.
         */
        // LCOV_EXCL_START
        char buf[1024];

        snprintf(buf, sizeof(buf), "Deallocating objective-C class %s %d %p\n",
                 ((PyTypeObject*)cls)->tp_name,
                 class_isMetaClass(((PyObjCClassObject*)cls)->class), cls);

        fputs(buf, stderr);
        Py_INCREF(cls);
        return;
        // LCOV_EXCL_STOP
    } // LCOV_EXCL_LINE

    /*
     * Proxies for "native" Objective-C classes can be deallocated when two threads race
     * to create a proxy for the class.
     */

    CLANG_SUPPRESS
    Py_CLEAR(self->sel_to_py);
    Py_CLEAR(self->delmethod);
    CLANG_SUPPRESS
    Py_CLEAR(self->hiddenSelectors);
    Py_CLEAR(self->hiddenClassSelectors);
#ifdef PyObjC_ENABLE_LOOKUP_CACHE
    Py_CLEAR(self->lookup_cache);
#endif
    PyType_Type.tp_dealloc(cls);

    /* Note: the class cannot be in the 'objc_class_locate' data structure
     * because that table owns a reference to the class.
     */
    return;
}

int
PyObjCClass_CheckMethodList(PyObject* start_cls, int recursive)
{
    PyObjCClassObject* info;
    PyObject* _Nullable cls = start_cls;

    assert(PyObjCClass_Check(start_cls));

    info = (PyObjCClassObject*)cls;

    if (info->class == NULL)
        return 0;

    while (info->class != NULL) {
        if (info->generation != PyObjC_MappingCount) {
            int r;
#ifdef Py_GIL_DISABLED
            /* XXX: The read above likely needs to be atomic,
             *      likewise for setting the value.
             *
             * XXX: Setting 'generation' in a critical section
             *      should be enough to avoid unnecessary duplicate
             *      updates.
             *
             */
            int should_call;

            Py_BEGIN_CRITICAL_SECTION(info);
            if (info->generation != PyObjC_MappingCount) {
                should_call = 1;
#endif

                // XXX: See below: due to a race we can only
                //      update the generation after calling the
                //      class extender.
                //
                //      This can cause races in the extender function
                //      itself, but that should be harmless other than
                //      doing unnecessary work.
                // info->generation = PyObjC_MappingCount;
#ifdef Py_GIL_DISABLED
            } else {
                should_call = 0;
            }
            Py_END_CRITICAL_SECTION();

            if (should_call) {
#endif
                /* XXX: This is annoying: the class extender should
                 *      be called in the critical section because
                 *      otherwise racing threads can see an incomplete
                 *      state...
                 *
                 *      Note that this is technically already a problem
                 *      with the regular build, although it is a lot easier
                 *      to hit with the GIL disabled.
                 */
                r = PyObjC_CallClassExtender(cls);
                if (r < 0) {
                    return -1;
                }

                PyObject* to_clear = NULL;
                Py_BEGIN_CRITICAL_SECTION(info);
                /* sel_to_py is a cache, interleaving
                 * two calls to this function in different
                 * threads is fine.
                 */

                to_clear = info->sel_to_py;
                if (info->sel_to_py) {
                    info->sel_to_py = PyDict_New();
                }

                info->generation = PyObjC_MappingCount;
                Py_END_CRITICAL_SECTION();
                Py_CLEAR(to_clear);
#ifdef Py_GIL_DISABLED
            }
#endif
        }

        if (!recursive)
            break;
        if (class_getSuperclass(info->class) == NULL)
            break;
        /* class_getSuperclass returns Nil only if its argument is Nil */
        cls = PyObjCClass_New((Class _Nonnull)class_getSuperclass(info->class));
        if (cls == NULL) { // LCOV_BR_EXCL_LINE
            /* Abort checking if the class object cannot be created. Should
             * never happen in practice...
             */
            // LCOV_EXCL_START
            PyErr_Clear();
            break;
            // LCOV_EXCL_STOP
        }

        /* We don't actually need the reference, convert to a borrowed one */

        /* This is safe because classes are never deallocated other than
         * to resolve a race condition between two threads creating a class
         * proxy for the same class.
         */
        Py_DECREF(cls);
        assert(PyObjCClass_Check(cls));
        info = (PyObjCClassObject*)cls;
    }
    return 0;
}

static PyObject* _Nullable metaclass_dir(PyObject* self)
{
    PyObject*    result;
    Class        cls;
    Method*      methods;
    unsigned int method_count, i;

    /* Start of with keys in __dict__ */
    result = PyDict_Keys(((PyTypeObject*)self)->tp_dict);
    if (result == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE
    }

    cls = objc_metaclass_locate(self);
    if (cls == NULL) {
        /* This happens for the root of the class tree */
        return result;
    }

    PyObject* self_class = PyObjCClass_ClassForMetaClass(self);
    if (self_class == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(result);
        return NULL;
        // LCOV_EXCL_STOP
    }

    while (cls != NULL) {
        /* Now add all method names */

        /* class_copyMethodList only returns NULL when it sets method_count
         * to 0
         */
        methods =
            (Method* _Nonnull)class_copyMethodList(object_getClass(cls), &method_count);
        for (i = 0; i < method_count; i++) {
            PyObject* item;
            SEL       meth_name = method_getName(methods[i]);
            if (meth_name == NULL) { // LCOV_BR_EXCL_LINE
                /* Ignore methods without a selector */
                continue; // LCOV_EXCL_LINE
            }

            /* Check if the selector should be hidden */
            PyObject* hidden = PyObjCClass_HiddenSelector(self_class, meth_name, YES);
            if (hidden == NULL && PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
                /* Assertion error */
                // LCOV_EXCL_START
                free(methods);
                Py_DECREF(result);
                return NULL;
                // LCOV_EXCL_STOP

            } else if (hidden) {
                Py_DECREF(hidden);
                continue;
            }

            item = PyObjC_SELToPythonName(meth_name);
            if (item == NULL) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                free(methods);
                Py_DECREF(self_class);
                Py_DECREF(result);
                return NULL;
                // LCOV_EXCL_STOP
            }

            if (PyList_Append(result, item) == -1) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                free(methods);
                Py_DECREF(self_class);
                Py_DECREF(result);
                Py_DECREF(item);
                return NULL;
                // LCOV_EXCL_STOP
            }
            Py_DECREF(item);
        }
        free(methods);

        cls = class_getSuperclass(cls);
    }
    Py_DECREF(self_class);
    return result;
}

/* FIXME: This is a lightly modified version of _type_lookup in objc-object.m, need to
 * merge these */
static inline PyObject* _Nullable _type_lookup(PyTypeObject* tp, PyObject* name)
{
    Py_ssize_t  i, n;
    PyObject *  mro, *base, *dict;
    PyObject*   descr    = NULL;
    const char* sel_name = PyUnicode_AsUTF8(name);
    if (sel_name == NULL) {
        return NULL;
    }
    SEL sel = PyObjCSelector_DefaultSelector(sel_name);

    /* TODO: if sel.startswith('__') and sel.endswith('__'): look_in_runtime = False */

    /* Look in tp_dict of types in MRO */
    Py_BEGIN_CRITICAL_SECTION(tp);
    mro = tp->tp_mro;
    Py_XINCREF(mro);
    Py_END_CRITICAL_SECTION();
    if (mro == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;   // LCOV_EXCL_LINE
    }
    assert(PyTuple_Check(mro));
    n = PyTuple_GET_SIZE(mro);
    for (i = 0; i < n; i++) {
        base = PyTuple_GET_ITEM(mro, i);
        if (PyObjCClass_Check(base)) {
            if (PyObjCClass_CheckMethodList(base, 0) < 0) {
                Py_CLEAR(mro);
                return NULL;
            }
            dict = PyType_GetDict((PyTypeObject*)base);
            if (dict == NULL) {
                continue;
            }

        } else if (PyType_Check(base)) { // LCOV_BR_EXCL_LINE
            dict = PyType_GetDict((PyTypeObject*)base);
            if (dict == NULL) {
                continue;
            }

        } else {
            /* Cannot happen: non-class on MRO  */
            Py_CLEAR(mro);
            return NULL; // LCOV_EXCL_LINE
        }

        assert(dict && PyDict_Check(dict));
        int r = PyDict_GetItemRef(dict, name, &descr);
        Py_CLEAR(dict);
        if (r == 1) { // LCOV_BR_EXCL_LINE
            break;    // LCOV_EXCL_LINE
        } else if (r == -1) {
            Py_CLEAR(mro);
            return NULL;
        }

        if (PyObject_IsSubclass(base, (PyObject*)&PyObjCMetaClass_Type)) {
            descr = PyObjCMetaClass_TryResolveSelector(base, name, sel);
            if (descr != NULL) {
                break;
            } else if (PyErr_Occurred()) {
                Py_CLEAR(mro);
                return NULL;
            }
        }
    }

    Py_CLEAR(mro);
    return descr;
}

static inline PyObject* _Nullable _type_lookup_harder(PyTypeObject* tp, PyObject* name)
/* See function of same name in objc-object.m for an explanation */
{
    Py_ssize_t  i, n;
    PyObject *  mro, *base;
    PyObject*   descr      = NULL;
    const char* name_bytes = PyUnicode_AsUTF8(name);
    if (name_bytes == NULL)
        return NULL;

    /* Look in tp_dict of types in MRO */
    Py_BEGIN_CRITICAL_SECTION(tp);
    mro = tp->tp_mro;
    Py_XINCREF(mro);
    Py_END_CRITICAL_SECTION();
    if (mro == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;   // LCOV_EXCL_LINE
    }
    assert(PyTuple_Check(mro));
    n = PyTuple_GET_SIZE(mro);
    for (i = 0; i < n; i++) {
        Class        cls;
        Method*      methods;
        unsigned int method_count, j;

        base = PyTuple_GET_ITEM(mro, i);
        assert(base != NULL);

        if (!PyObject_IsSubclass(base, (PyObject*)&PyObjCMetaClass_Type)) {
            continue;
        }
        if (base == (PyObject*)&PyObjCClass_Type
            || base == (PyObject*)&PyObjCMetaClass_Type) {
            /* Root of the PyObjC class tree, these do not refer to an ObjC class */
            continue;
        }

        cls = objc_metaclass_locate(base);
        assert(cls != Nil);

        PyObject* class_for_base = PyObjCClass_ClassForMetaClass(base);
        if (class_for_base == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_CLEAR(mro);
            return NULL;
            // LCOV_EXCL_STOP
        }

        /* class_copyMethodList only returns NULL when it sets method_count
         * to 0
         */
        methods =
            (Method* _Nonnull)class_copyMethodList(object_getClass(cls), &method_count);
        for (j = 0; j < method_count; j++) {
            Method m         = methods[j];
            SEL    meth_name = method_getName(m);
            if (meth_name == NULL) { // LCOV_BR_EXCL_LINE
                /* Method without a selector, ignore these */
                continue; // LCOV_EXCL_LINE
            }

            PyObject* hidden = PyObjCClass_HiddenSelector(class_for_base, meth_name, YES);
            if (hidden == NULL && PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                free(methods);
                Py_CLEAR(mro);
                return NULL;
                // LCOV_EXCL_STOP

            } else if (hidden) {
                Py_CLEAR(hidden);
                continue;
            }

            PyObject* sel_name = PyObjC_SELToPythonName(method_getName(m));
            if (sel_name == NULL) {
                /* Ignore selectors whose name cannot be converted to a python name */
                PyErr_Clear();
                continue;
            }
            int same = PyObject_RichCompareBool(sel_name, name, Py_EQ);
            Py_CLEAR(sel_name);
            if (same == -1) { // LCOV_BR_EXCL_START
                // LCOV_EXCL_START
                PyErr_Clear();
                continue;
                // LCOV_EXCL_STOP
            }
            if (same) {
                /* Create (unbound) selector */
                const char* encoding = method_getTypeEncoding(m);
                if (encoding == NULL) { // LCOV_BR_EXCL_LINE
                    // LCOV_EXCL_START
                    Py_DECREF(class_for_base);
                    free(methods);
                    Py_CLEAR(mro);
                    PyErr_SetString(PyObjCExc_Error,
                                    "Native selector with NULL type encoding");
                    return NULL;
                    // LCOV_EXCL_STOP
                }
                descr = PyObjCSelector_NewNative(cls, method_getName(m), encoding, 1);
                free(methods);
                Py_DECREF(class_for_base);
                if (descr == NULL) { // LCOV_BR_EXCL_LINE
                    // LCOV_EXCL_START
                    Py_CLEAR(mro);
                    return NULL;
                    // LCOV_EXCL_STOP
                }

                /* add to __dict__ 'cache' */
                if (PyDict_SetItem( // LCOV_BR_EXCL_LINE
                        ((PyTypeObject*)base)->tp_dict, name, descr)
                    == -1) {
                    // LCOV_EXCL_START
                    Py_DECREF(descr);
                    Py_CLEAR(mro);
                    return NULL;
                    // LCOV_EXCL_STOP
                }

                Py_CLEAR(mro);
                return descr;
            }
        }
        Py_DECREF(class_for_base);
        free(methods);
    }

    assert(descr == NULL);
    Py_CLEAR(mro);
    return NULL;
}

/* Returns a new reference */
PyObject* _Nullable PyObjCMetaClass_TryResolveSelector(PyObject* base, PyObject* name,
                                                       SEL sel)
{
    assert(PyObjCClass_Check(base) || PyObjCMetaClass_Check(base)
           || base == (PyObject*)&PyObjCMetaClass_Type);
    Class     cls;
    Method    m;
    PyObject* dict = ((PyTypeObject*)base)->tp_dict;
    PyObject* hidden;

    cls = objc_metaclass_locate(base);
    if (cls == Nil) {
        /* XXX: Fix for a sporadic crash when resolving methods */
        m = nil;
    } else {
        @try { /* XXX: Can this raise? */
            m = class_getClassMethod(cls, sel);

            // LCOV_EXCL_START
        } @catch (NSObject* localException) {
            PyObjCErr_FromObjC(localException);
            m = nil;
        }
        // LCOV_EXCL_STOP
    }
    if (m == nil && PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;                    // LCOV_EXCL_LINE
    }

    hidden = PyObjCClass_HiddenSelector(
        (PyObject* _Nonnull)PyObjCClass_ClassForMetaClass(base), sel, YES);
    if (hidden || PyErr_Occurred()) {
        Py_CLEAR(hidden);
        return NULL;
    }

    if (m) {
#ifndef PyObjC_FAST_BUT_INEXACT
        int   use = 1;
        Class sup = class_getSuperclass(cls);

        if (sup) {
            Method m_sup = class_getClassMethod(sup, sel);
            if (m_sup == m) {
                use = 0;
            }
        }

        if (!use) {
            return NULL;
        }
#endif

        /* Create (unbound) selector */
        /* XXX: Add check for method_getTypeEncoding */
        const char* encoding = method_getTypeEncoding(m);
        if (encoding == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            PyErr_SetString(PyObjCExc_Error, "Native selector with NIL encoding");
            return NULL;
            // LCOV_EXCL_STOP
        }

        PyObject* result = PyObjCSelector_NewNative(cls, sel, encoding, 1);
        if (result == NULL) { // LCOV_BR_EXCL_LINE
            return NULL;      // LCOV_EXCL_LINE
        }

        /* add to __dict__ 'cache' */
        if (PyDict_SetItem(dict, name, result) == -1) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(result);
            return NULL;
            // LCOV_EXCL_STOP
        }

        return result;
    }
    return NULL;
}

/* FIXME: version of _type_lookup that only looks for instance methods */
static inline PyObject* _Nullable _type_lookup_instance(PyObject*     class_dict,
                                                        PyTypeObject* tp, PyObject* name)
{
    Py_ssize_t  i, n;
    PyObject *  mro, *base, *dict;
    PyObject*   descr  = NULL;
    const char* c_name = PyUnicode_AsUTF8(name);
    if (c_name == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE
    }
    SEL sel = PyObjCSelector_DefaultSelector(c_name);

    /* TODO: if sel.startswith('__') and sel.endswith('__'): look_in_runtime = False */

    /* Look in tp_dict of types in MRO */
    Py_BEGIN_CRITICAL_SECTION(tp);
    mro = tp->tp_mro;
    Py_XINCREF(mro);
    Py_END_CRITICAL_SECTION();
    if (mro == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;   // LCOV_EXCL_LINE
    }
    assert(PyTuple_Check(mro));
    n = PyTuple_GET_SIZE(mro);
    for (i = 0; i < n; i++) {
        base = PyTuple_GET_ITEM(mro, i);
        if (PyType_Check(base)) { // LCOV_BR_EXCL_LINE
            dict = PyType_GetDict((PyTypeObject*)base);

        } else {
            /* Cannot happen: non-type in MRO */
            // LCOV_EXCL_START
            Py_CLEAR(mro);
            return NULL;
            // LCOV_EXCL_STOP
        }

        if (dict != NULL) {
            switch (PyDict_GetItemRef(dict, name, &descr)) { // LCOV_BR_EXCL_LINE
            case -1:
                // LCOV_EXCL_START
                Py_CLEAR(dict);
                Py_CLEAR(mro);
                return NULL;
                // LCOV_EXCL_STOP

            case 1:
                Py_CLEAR(dict);
                Py_CLEAR(mro);
                return descr;

            case 0:
                Py_CLEAR(dict);
            }
        }

        if (PyObjCClass_Check(base)) {
            /*Class cls = objc_metaclass_locate(base);*/
            Class  cls = PyObjCClass_GetClass(base);
            Method m;

            Py_BEGIN_ALLOW_THREADS
                @try {
                    m = class_getInstanceMethod(cls, sel);

                } @catch (NSObject* localException) {
                    /* Annoyingly enough this can result in callbacks to ObjC
                     * that can raise an exception.
                     */
                    m = NULL;
                }
            Py_END_ALLOW_THREADS

            if (m) {
#ifndef PyObjC_FAST_BUT_INEXACT
                int   use = 1;
                Class sup = class_getSuperclass(cls);
                if (sup) {
                    Method m_sup = class_getInstanceMethod(sup, sel);
                    if (m_sup == m) {
                        use = 0;
                    }
                }
                if (!use)
                    continue;
#endif

                /* Create (unbound) selector */
                const char* encoding = method_getTypeEncoding(m);
                if (encoding == NULL) { // LCOV_BR_EXCL_LINE
                    // LCOV_EXCL_START
                    PyErr_SetString(PyObjCExc_Error, "Native method with NIL selector");
                    return NULL;
                    // LCOV_EXCL_STOP
                }
                PyObject* result = PyObjCSelector_NewNative(cls, sel, encoding, 0);
                if (result == NULL) { // LCOV_BR_EXCL_LINE
                    // LCOV_EXCL_START
                    Py_CLEAR(mro);
                    return NULL;
                    // LCOV_EXCL_STOP
                }

                /* add to __dict__ 'cache' */
                if (PyDict_SetItem(class_dict, name, result) == -1) { // LCOV_BR_EXCL_LINE
                    // LCOV_EXCL_START
                    Py_DECREF(result);
                    Py_CLEAR(mro);
                    return NULL;
                    // LCOV_EXCL_STOP
                }

                Py_CLEAR(mro);
                return result;
            }
        }
    }

    Py_CLEAR(mro);
    return NULL;
}

static inline PyObject* _Nullable _type_lookup_instance_harder(PyObject*     class_dict,
                                                               PyTypeObject* tp,
                                                               PyObject*     name)
{
    Py_ssize_t  i, n;
    PyObject *  mro, *base;
    const char* name_bytes = PyUnicode_AsUTF8(name);
    if (name_bytes == NULL) {
        return NULL;
    }
    SEL sel = PyObjCSelector_DefaultSelector(name_bytes);

    /* Look in tp_dict of types in MRO */
    Py_BEGIN_CRITICAL_SECTION(tp);
    mro = tp->tp_mro;
    Py_XINCREF(mro);
    Py_END_CRITICAL_SECTION();
    if (mro == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;   // LCOV_EXCL_LINE
    }
    assert(PyTuple_Check(mro));
    n = PyTuple_GET_SIZE(mro);
    for (i = 0; i < n; i++) {
        Class        cls;
        Method*      methods;
        unsigned int method_count, j;

        base = PyTuple_GET_ITEM(mro, i);
        if (!PyObjCClass_Check(base)) {
            continue;
        }

        cls = PyObjCClass_GetClass(base);

        /* if the result of class_copyMethodList is NULL the method_count
         * is set to 0. The code below will only use the result if method_count
         * is greater than 0.
         */
        methods = (Method* _Nonnull)class_copyMethodList(cls, &method_count);
        for (j = 0; j < method_count; j++) {
            Method m = methods[j];

            PyObject* sel_name = PyObjC_SELToPythonName(method_getName(m));
            if (sel_name == NULL) {
                /* Ignore methods whose selector cannot be converted */
                PyErr_Clear();
                continue;
            }

            int same = PyObject_RichCompareBool(sel_name, name, Py_EQ);
            Py_CLEAR(sel_name);
            if (same == -1) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                /* See above */
                PyErr_Clear();
                continue;
                // LCOV_EXCL_STOP
            }

            if (same) {
                /* Create (unbound) selector */
                const char* encoding = method_getTypeEncoding(m);
                if (encoding == NULL) { // LCOV_BR_EXCL_LINE
                    // LCOV_EXCL_START
                    PyErr_SetString(PyObjCExc_Error,
                                    "Native selector with Nil type encoding");
                    free(methods);
                    Py_DECREF(mro);
                    return NULL;
                    // LCOV_EXCL_STOP
                }
                PyObject* result = PyObjCSelector_NewNative(cls, sel, encoding, 0);
                free(methods);
                if (result == NULL) { // LCOV_BR_EXCL_LINE
                    // LCOV_EXCL_START
                    Py_DECREF(mro);
                    return NULL;
                    // LCOV_EXCL_STOP
                }

                /* add to __dict__ 'cache' */
                if (PyDict_SetItem(class_dict, name, result) == -1) { // LCOV_BR_EXCL_LINE
                    // LCOV_EXCL_START
                    Py_DECREF(result);
                    Py_DECREF(mro);
                    return NULL;
                    // LCOV_EXCL_STOP
                }

                return result;
            }
        }
        free(methods);
    }

    return NULL;
}

static PyObject* _Nullable class_getattro(PyObject* self, PyObject* name)
{
    PyObject*    descr  = NULL;
    PyObject*    result = NULL;
    descrgetfunc f      = NULL;

    /* Python will look for a number of "private" attributes during
     * normal operations, such as when building subclasses. Avoid a
     * method rescan when that happens.
     *
     * NOTE: This method should be rewritten, copy the version of type()
     *       and modify as needed, that would avoid unnecessary rescans
     *      of superclasses. The same strategy is used in object_getattro.
     *
     * NOTE2: That rewrite should also cause this method to prefer class
     *       methods over instance methods (and documentation should be
     *       added that you shouldn't look up instance methods through the
     *       class).
     *
     */
    if (PyUnicode_Check(name)) { // LCOV_BR_EXCL_LINE
        if (PyObjC_is_ascii_prefix(name, "__", 2)
            && !PyObjC_is_ascii_string(name, "__dict__")) {
            result = PyType_Type.tp_getattro(self, name);
            if (result != NULL) {
                return result;
            }
            PyErr_Clear();
        }

        if (PyUnicode_AsUTF8(name) == NULL)
            return NULL;

    } else {
        /* Never reached because the interpreter already performs
         * the typecheck on 'name'. Type check can only fail if
         * someone directly invokes the getattro slot.
         */
        // LCOV_EXCL_START
        PyErr_Format(PyExc_TypeError,
                     "Attribute name is not a string, but an instance of '%s'",
                     Py_TYPE(name)->tp_name);
        return NULL;
        // LCOV_EXCL_STOP
    }
    if (PyObjCClass_CheckMethodList(self, 1) < 0) {
        return NULL;
    }

    descr = _type_lookup(Py_TYPE(self), name);
    if (descr == NULL && PyErr_Occurred()) {
        return NULL;
    }

    if (descr != NULL) {
        f = Py_TYPE(descr)->tp_descr_get;
        if (f != NULL && PyDescr_IsData(descr)) {
            result = f(descr, self, (PyObject*)Py_TYPE(self));
            goto done;
        }
    }

    if (strcmp(PyUnicode_AsUTF8(name), "__dict__") == 0) {
        /* XXX: Is this correct */
        result = ((PyTypeObject*)self)->tp_dict;
        Py_INCREF(result);
        goto done;
    }

    if (descr == NULL) {
        descr = _type_lookup_instance(((PyTypeObject*)self)->tp_dict, (PyTypeObject*)self,
                                      name);
        if (descr != NULL) {
            f = Py_TYPE(descr)->tp_descr_get;
            if (f != NULL) {
                result = f(descr, NULL, self);
                goto done;
            }
        } else if (descr != NULL) {
            result = descr;
            descr  = NULL;
            goto done;
        } else if (PyErr_Occurred()) {
            result = NULL;
            goto done;
        }
    }

    if (descr == NULL) {
        descr = _type_lookup_harder(Py_TYPE(self), name);
        if (descr != NULL) {
            f = Py_TYPE(descr)->tp_descr_get;
        }
        if (PyErr_Occurred()) {
            result = NULL;
            goto done;
        }
    }

    if (descr == NULL) {
        descr = _type_lookup_instance_harder(((PyTypeObject*)self)->tp_dict,
                                             (PyTypeObject*)self, name);
        if (descr != NULL) {
            f = Py_TYPE(descr)->tp_descr_get;
        }
        if (PyErr_Occurred()) {
            /* XXX: can this happen without descr being NULL? */
            result = NULL;
            goto done;
        }
    }

    if (f != NULL) {
        result = f(descr, self, (PyObject*)Py_TYPE(self));
        goto done;
    }

    if (descr != NULL) {
        result = descr;
        descr  = NULL;
        goto done;
    }

    /* Try to find the method anyway */
    PyErr_Clear();
    const char* name_bytes = PyUnicode_AsUTF8(name);
    if (name_bytes == NULL) {
        return NULL;
    }
    PyObject* hidden = PyObjCClass_HiddenSelector(self, sel_getUid(name_bytes), YES);
    if (hidden == NULL && PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;                          // LCOV_EXCL_LINE
    } else if (hidden) {
        Py_CLEAR(hidden);
        PyErr_SetObject(PyExc_AttributeError, name);
        return NULL;
    }

    name_bytes = PyUnicode_AsUTF8(name);
    if (name_bytes == NULL) {
        return NULL;
    }
    result = PyObjCSelector_FindNative(self, name_bytes);

    if (result != NULL) {
        int res = PyDict_SetItem(((PyTypeObject*)self)->tp_dict, name, result);
        PyObjCNativeSelector* x = (PyObjCNativeSelector*)result;

        if (x->base.sel_flags & PyObjCSelector_kCLASS_METHOD) {
            x->base.sel_self = self;
            Py_INCREF(x->base.sel_self);
        }
        if (res < 0) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            if (PyObjC_Verbose) {
                PySys_WriteStderr("PyObjC[class_getattro]: Cannot "
                                  "add new method to dict:\n");
                PyErr_Print();
            }
            PyErr_Clear();
            // LCOV_EXCL_STOP
        }
    }
done:
    Py_CLEAR(descr);
    return result;
}

static int
class_setattro(PyObject* self, PyObject* name, PyObject* _Nullable value)
{
    int res;
    if (value == NULL) {
        /* delattr(), deny the operation when the name is bound
         * to a selector.
         */
        PyObject* old_value = class_getattro(self, name);
        if (old_value == NULL) {
            PyErr_Clear();
            return PyType_Type.tp_setattro(self, name, value);

        } else if (PyObjCSelector_Check(old_value)) {
            Py_DECREF(old_value);
            PyErr_Format(PyExc_AttributeError, "Cannot remove selector %R in '%s'", name,
                         Py_TYPE(self)->tp_name);

            return -1;
        }
    } else {
        /* XXX: Should store the protocols on the class object instead */
        PyObject* protocols = PyObject_GetAttrString(self, "__pyobjc_protocols__");
        if (protocols == NULL) {
            if (PyErr_ExceptionMatches(PyExc_AttributeError)) {
                PyErr_Clear();
                protocols = PyList_New(0);
                if (protocols == NULL) { // LCOV_BR_EXCL_LINE
                    return -1;           // LCOV_EXCL_LINE
                }
            } else {
                return -1;
            }
        }
        PyObject* old_value = value;
        value               = PyObjC_TransformAttribute(name, value, self, protocols);
        Py_DECREF(protocols);
        if (value == NULL) {
            return -1;
        }

        if (PyObjCNativeSelector_Check(value)) {
            /* XXX:
             *   The test for old_value is not ideal and is present
             *   to make it possible to use ``python_method(sel)`` to
             *   create an alias for ``sel``. Can't check for ``python_method``
             *   here because that type is python only.
             *
             *   Remove this once there is a good and documented way to
             *   accomplish this.
             */
            if (value == old_value) {
                Py_DECREF(value);
                PyErr_SetString(PyExc_TypeError,
                                "Assigning native selectors is not supported");
                return -1;
            }

        } else if (((PyObjCClassObject*)self)->isCFWrapper) {
            /* This is a wrapper class for a CoreFoundation type
             * that isn't tollfree bridged. Don't update the
             * Objective-C class because all CF types share the
             * same ObjC class (except for the toll-free bridged
             * ones).
             */

            /* XXX: Shouldn't this raise an exception instead of silently doing nothing
             *      when setting a selector?
             */

        } else if (PyObjCSelector_Check(value)) {
            /*
             * Assignment of a function: create a new method in the ObjC
             * runtime.
             */
            Method curMethod;
            Class  curClass;
            int    r;
            BOOL   b;

            if (PyObjCSelector_IsClassMethod(value)) {
                curMethod = class_getClassMethod(PyObjCClass_GetClass(self),
                                                 PyObjCSelector_GetSelector(value));
                curClass  = object_getClass(PyObjCClass_GetClass(self));
            } else {
                curMethod = class_getInstanceMethod(PyObjCClass_GetClass(self),
                                                    PyObjCSelector_GetSelector(value));
                curClass  = PyObjCClass_GetClass(self);
            }

            if (curMethod) {
                IMP newIMP = PyObjCFFI_MakeIMPForPyObjCSelector((PyObjCSelector*)value);
                if (newIMP == NULL) {
                    Py_DECREF(value);
                    return -1;
                }

                method_setImplementation(curMethod, newIMP);

            } else {
                /* XXX: Why use "strdup" here and not the pyobjc_util variant? */
                char* types = strdup(PyObjCSelector_Signature(value));

                if (types == NULL) { // LCOV_BR_EXCL_LINE
                    // LCOV_EXCL_START
                    Py_DECREF(value);
                    return -1;
                    // LCOV_EXCL_STOP
                }

                IMP newIMP = PyObjCFFI_MakeIMPForPyObjCSelector((PyObjCSelector*)value);
                if (newIMP == NULL) {
                    free(types);
                    Py_DECREF(value);
                    return -1;
                }
                b = class_addMethod(curClass, PyObjCSelector_GetSelector(value), newIMP,
                                    types);

                if (!b) { // LCOV_BR_EXCL_LINE
                    // LCOV_EXCL_START
                    free(types);
                    Py_DECREF(value);
                    return -1;
                    // LCOV_EXCL_STOP
                }
            }

            PyObject* hidden =
                PyObjCClass_HiddenSelector(self, PyObjCSelector_GetSelector(value),
                                           PyObjCSelector_IsClassMethod(value));
            if (hidden == NULL && PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                Py_DECREF(value);
                return -1;
                // LCOV_EXCL_STOP

            } else if (hidden) {
                Py_CLEAR(hidden);
                Py_DECREF(value);

            } else {
                if (PyObjCSelector_IsClassMethod(value)) {
                    r = PyDict_SetItem(Py_TYPE(self)->tp_dict, name, value);

                } else {
                    r = PyDict_SetItem(((PyTypeObject*)self)->tp_dict, name, value);
                }

                Py_DECREF(value);
                if (r == -1) { // LCOV_BR_EXCL_LINE
                    // LCOV_EXCL_START
                    PyErr_NoMemory();
                    return -1;
                    // LCOV_EXCL_STOP
                }
            }
            return 0;
        }
    }

#if 0 /* XXX: Disabled check due to #479 */
    /* Check if there is a current attribute with the same name that
     * is an unbound selector.
     */
    PyObject* old_value = class_getattro(self, name);
    if (old_value == NULL) {
        PyErr_Clear();
        res = PyType_Type.tp_setattro(self, name, value);
        Py_XDECREF(value);
        return res;

    } else if (PyObjCSelector_Check(old_value)) {
        Py_DECREF(old_value);
        PyErr_Format(PyExc_AttributeError,
                     "Cannot replace selector %R in '%s' by non-selector", name,
                     Py_TYPE(self)->tp_name);

        return -1;
    }
#endif

    res = PyType_Type.tp_setattro(self, name, value);
    Py_XDECREF(value);
    return res;
}

static PyObject* _Nullable class_richcompare(PyObject* self, PyObject* other, int op)
{
    Class self_class;
    Class other_class;
    int   v;

    if (!PyObjCClass_Check(other)) {
        if (op == Py_EQ) {
            Py_RETURN_FALSE;

        } else if (op == Py_NE) {
            Py_RETURN_TRUE;

        } else {
            Py_RETURN_NOTIMPLEMENTED;
        }
    }

    /* This is as arbitrary as the default tp_compare, but nicer for
     * the user
     */
    self_class  = PyObjCClass_GetClass(self);
    other_class = PyObjCClass_GetClass(other);

    if (self_class == other_class) {
        v = 0; // LCOV_EXCL_LINE

    } else if (!self_class) {
        v = -1;

    } else if (!other_class) {
        v = 1;

    } else {
        switch (op) {
        case Py_EQ:
            /* Classes should only compare equal
             * if they are the same class.
             */
            if (self_class == other_class) {
                Py_RETURN_TRUE; // LCOV_EXCL_LINE
            } else {
                Py_RETURN_FALSE;
            }

        case Py_NE:
            if (self_class == other_class) {
                Py_RETURN_FALSE;
            } else {
                Py_RETURN_TRUE; // LCOV_EXCL_LINE
            }
        }

        v = strcmp(class_getName(self_class), class_getName(other_class));
    }

    switch (op) { // LCOV_BR_EXCL_LINE
    case Py_EQ:
        if (v == 0) {
            Py_RETURN_TRUE;
        } else {
            Py_RETURN_FALSE;
        }
        break;

    case Py_NE:
        if (v != 0) {
            Py_RETURN_TRUE;
        } else {
            Py_RETURN_FALSE;
        }
        break;

    case Py_LE:
        if (v <= 0) {
            Py_RETURN_TRUE;
        } else {
            Py_RETURN_FALSE;
        }
        break;

    case Py_LT:
        if (v < 0) {
            Py_RETURN_TRUE;
        } else {
            Py_RETURN_FALSE;
        }
        break;

    case Py_GE:
        if (v >= 0) {
            Py_RETURN_TRUE;
        } else {
            Py_RETURN_FALSE;
        }
        break;

    case Py_GT:
        if (v > 0) {
            Py_RETURN_TRUE;
        } else {
            Py_RETURN_FALSE;
        }
        break;

    default:
        // LCOV_EXCL_START
        PyErr_Format(PyExc_TypeError, "Unexpected op=%d in class_richcompare", op);
        return NULL;
        // LCOV_EXCL_STOP
    }
}

static Py_hash_t
class_hash(PyObject* self)
{
    /* Class equality requires that two classes are the same,
     * using self for the hash is therefore safe.
     */
    return (Py_hash_t)self;
}

PyDoc_STRVAR(
    cls_get_classMethods_doc,
    "The attributes of this field are the class methods of this object. This can\n"
    "be used to force access to a class method.");
static PyObject* _Nullable cls_get_classMethods(PyObject* self, void* _Nullable closure
                                                __attribute__((__unused__)))
{
    return PyObjCMethodAccessor_New(self, 1);
}

PyDoc_STRVAR(
    cls_get_instanceMethods_doc,
    "The attributes of this field are the instance methods of this object. This \n"
    "can be used to force access to an instance method.");
static PyObject* _Nullable cls_get_instanceMethods(PyObject* self, void* _Nullable closure
                                                   __attribute__((__unused__)))
{
    return PyObjCMethodAccessor_New(self, 0);
}

static PyObject* _Nullable cls_get__name__(PyObject* self, void* _Nullable closure
                                           __attribute__((__unused__)))
{
    Class cls = PyObjCClass_GetClass(self);
    if (cls == NULL) {
        return PyUnicode_FromString(((PyTypeObject*)self)->tp_name);

    } else {
        const char* nm = class_getName(cls);
        if (strstr(nm, "NSCFType") != NULL) {
            return PyUnicode_FromString(((PyTypeObject*)self)->tp_name);
        } else {
            return PyUnicode_FromString(nm);
        }
    }
}

PyDoc_STRVAR(cls_version_doc, "get/set the version of a class");
static PyObject* _Nullable cls_get_version(PyObject* self, void* _Nullable closure
                                           __attribute__((__unused__)))
{
    Class cls = PyObjCClass_GetClass(self);
    if (cls == NULL) {
        Py_RETURN_NONE;
    } else {
        return PyLong_FromLong(class_getVersion(cls));
    }
}

static int
cls_set_version(PyObject* self, PyObject* _Nullable newVal,
                void* _Nullable closure __attribute__((__unused__)))
{
    Class cls = PyObjCClass_GetClass(self);
    int   val;
    int   r;

    if (newVal == NULL) {
        PyErr_SetString(PyExc_TypeError, "Cannot delete __version__ attribute");
        return -1;
    }

    r = depythonify_c_value(@encode(int), newVal, &val);
    if (r == -1) {
        return -1;
    }

    class_setVersion(cls, val);
    return 0;
}

static PyObject*
cls_get_useKVO(PyObject* self, void* _Nullable closure __attribute__((__unused__)))
{
    if (((PyObjCClassObject*)self)->useKVO) {
        Py_RETURN_TRUE;
    } else {
        Py_RETURN_FALSE;
    }
}

static int
cls_set_useKVO(PyObject* self, PyObject* _Nullable newVal,
               void* _Nullable closure __attribute__((__unused__)))
{
    if (newVal == NULL) {
        PyErr_SetString(PyExc_TypeError, "Cannot delete __useKVO__ attribute");
        return -1;
    }

    int useKVO = PyObject_IsTrue(newVal);
    if (useKVO == -1) {
        return -1;
    }
    /* XXX: Need to use atomic operations accessing the value */
    ((PyObjCClassObject*)self)->useKVO = useKVO;
    return 0;
}

static PyObject* _Nullable cls_get_final(PyObject* self, void* _Nullable closure
                                         __attribute__((__unused__)))
{
    if (((PyObjCClassObject*)self)->isFinal) {
        Py_RETURN_TRUE;
    } else {
        Py_RETURN_FALSE;
    }
}

static int
cls_set_final(PyObject* self, PyObject* _Nullable newVal,
              void* _Nullable closure __attribute__((__unused__)))
{
    if (newVal == NULL) {
        PyErr_SetString(PyExc_TypeError, "Cannot delete __objc_final__ attribute");
        return -1;
    }

    int isFinal = PyObject_IsTrue(newVal);
    if (isFinal == -1) {
        return -1;
    }
    /* XXX: Need to use atomic operations accessing the value */
    ((PyObjCClassObject*)self)->isFinal = isFinal;
    return 0;
}

static PyObject* _Nullable cls_get_hasdict(PyObject* self, void* _Nullable closure
                                           __attribute__((__unused__)))
{
    if (((PyObjCClassObject*)self)->dictoffset != 0) {
        Py_RETURN_TRUE;
    } else {
        Py_RETURN_FALSE;
    }
}

static PyObject* _Nullable cls_get_haspythonimplementation(PyObject* self,
                                                           void* _Nullable closure
                                                           __attribute__((__unused__)))
{
    if (((PyObjCClassObject*)self)->hasPythonImpl != 0) {
        Py_RETURN_TRUE;
    } else {
        Py_RETURN_FALSE;
    }
}

static PyGetSetDef class_getset[] = {
    {
        .name = "pyobjc_classMethods",
        .get  = cls_get_classMethods,
        .doc  = cls_get_classMethods_doc,
    },
    {
        .name = "pyobjc_instanceMethods",
        .get  = cls_get_instanceMethods,
        .doc  = cls_get_instanceMethods_doc,
    },
    {
        .name = "__version__",
        .get  = cls_get_version,
        .set  = cls_set_version,
        .doc  = cls_version_doc,
    },
    {
        .name = "__useKVO__",
        .get  = cls_get_useKVO,
        .set  = cls_set_useKVO,
        .doc  = "Use KVO notifications when setting attributes from Python",
    },
    {
        .name = "__objc_final__",
        .get  = cls_get_final,
        .set  = cls_set_final,
        .doc  = "True if the class cannot be subclassed",
    },
    {
        .name = "__hasdict__",
        .get  = cls_get_hasdict,
        .doc  = "True if the class has an __dict__",
    },
    {
        .name = "__has_python_implementation__",
        .get  = cls_get_haspythonimplementation,
        .doc  = "True if the class has a Python implementation",
    },
    {
        /* Access __name__ through a property: Objective-C name
         * might change due to posing.
         */
        .name = "__name__",
        .get  = cls_get__name__,
    },
    {
        .name = NULL /* SENTINEL */
    }};

static PyObject* _Nullable meth_dir(PyObject* self)
{
    PyObject*    result;
    Class        cls;
    Method*      methods;
    unsigned int method_count, i;

    /* Start of with keys in __dict__ */
    result = PyDict_Keys(((PyTypeObject*)self)->tp_dict);
    if (result == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE
    }

    cls = PyObjCClass_GetClass(self);

    while (cls != NULL) {
        /* Now add all method names */

        /* class_copyMethodList only returns NULL when it sets method_count
         * to 0
         */
        methods = (Method* _Nonnull)class_copyMethodList(cls, &method_count);
        for (i = 0; i < method_count; i++) {
            PyObject* item;

            /* Check if the selector should be hidden */
            PyObject* hidden = PyObjCClass_HiddenSelector((PyObject*)Py_TYPE(self),
                                                          method_getName(methods[i]), NO);
            if (hidden == NULL && PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                free(methods);
                Py_DECREF(result);
                return NULL;
                // LCOV_EXCL_STOP
            } else if (hidden) {
                Py_CLEAR(hidden);
                continue;
            }

            item = PyObjC_SELToPythonName(method_getName(methods[i]));
            if (item == NULL) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                free(methods);
                Py_DECREF(result);
                return NULL;
                // LCOV_EXCL_STOP
            }

            if (PyList_Append(result, item) == -1) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                free(methods);
                Py_DECREF(result);
                Py_DECREF(item);
                return NULL;
                // LCOV_EXCL_STOP
            }
            Py_DECREF(item);
        }
        free(methods);

        cls = class_getSuperclass(cls);
    }
    return result;
}

static PyObject* _Nullable class_get_hidden(PyObject* _self, PyObject* classMethod)
{
    PyObjCClassObject* self = ((PyObjCClassObject*)_self);
    PyObject*          hidden;
    int                isClassMethod;

    isClassMethod = PyObject_IsTrue(classMethod);
    if (isClassMethod == -1) {
        return NULL;
    }
    if (isClassMethod) {
        hidden = self->hiddenClassSelectors;
        if (hidden == NULL) {
            return PyDict_New();
        }

    } else {
        hidden = self->hiddenSelectors;
        if (hidden == NULL) {
            return PyDict_New();
        }
    }

    assert(PyDict_Check(hidden));
    return PyDict_Copy(hidden);
}

static PyMethodDef metaclass_methods[] = {{.ml_name  = "__dir__",
                                           .ml_meth  = (PyCFunction)metaclass_dir,
                                           .ml_flags = METH_NOARGS,
                                           .ml_doc   = "dir() hook, don't call directly"},
                                          {
                                              .ml_name = NULL /* SENTINEL */
                                          }};

static PyMethodDef class_methods[] = {
    {.ml_name  = "__dir__",
     .ml_meth  = (PyCFunction)meth_dir,
     .ml_flags = METH_NOARGS,
     .ml_doc   = "dir() hook, don't call directly"},
    {.ml_name  = "pyobjc_hiddenSelectors",
     .ml_meth  = class_get_hidden,
     .ml_flags = METH_O,
     .ml_doc   = "pyobjc_hiddenSelectors(classMethod)" CLINIC_SEP
               "Return copy of hidden selectors"},
    {.ml_name = "__class_getitem__",
     .ml_meth = (PyCFunction)Py_GenericAlias,
     // This is not a METH_CLASS due the the parallel class tree
     // for instance and class methods.
     .ml_flags = METH_O,
     .ml_doc   = "See PEP 585"},

    {
        .ml_name = NULL /* SENTINEL */
    }};

/*
 * This is the class for type(NSObject), and is a subclass of type()
 * with an overridden tp_getattro that is used to dynamically look up
 * class methods.
 */
PyTypeObject PyObjCMetaClass_Type = {
    PyVarObject_HEAD_INIT(&PyType_Type, 0).tp_name = "objc.objc_meta_class",
    .tp_basicsize                                  = sizeof(PyHeapTypeObject),
    .tp_itemsize                                   = sizeof(PyMemberDef),
    .tp_flags                                      = Py_TPFLAGS_DEFAULT,
    .tp_methods                                    = metaclass_methods,
    .tp_base                                       = &PyType_Type,
    .tp_dictoffset                                 = offsetof(PyTypeObject, tp_dict),
};

PyTypeObject PyObjCClass_Type = {
    PyVarObject_HEAD_INIT(&PyObjCMetaClass_Type, 0).tp_name = "objc.objc_class",
    .tp_basicsize                                           = sizeof(PyObjCClassObject),
    .tp_itemsize                                            = 0,
    .tp_dealloc                                             = class_dealloc,
    .tp_repr                                                = class_repr,
    .tp_hash                                                = class_hash,
    .tp_getattro                                            = class_getattro,
    .tp_setattro                                            = class_setattro,
    .tp_flags       = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
    .tp_doc         = class_doc,
    .tp_richcompare = class_richcompare,
    .tp_methods     = class_methods,
    .tp_getset      = class_getset,
    .tp_base        = &PyObjCMetaClass_Type,
    .tp_init        = class_init,
    .tp_new         = class_new,
    .tp_call        = class_call,
};

/*
 * Create a new objective-C class  proxy.
 *
 * NOTES:
 * - proxies are subclasses of PyObjCClass_Type
 * - subclass relations in objetive-C are retained in python
 * - this looks a lot like PyObjCClass_Type.tp_new, but it is _not_ the
 *   same!
 *
 * Returns a new reference.
 */
PyObject* _Nullable PyObjCClass_New(Class objc_class)
{
    PyObject*          args;
    PyObject*          dict;
    PyObject*          result;
    PyObject*          bases;
    PyObjCClassObject* info;
    Ivar               var;
    PyObject*          hiddenSelectors;
    PyObject*          hiddenClassSelectors;
    PyTypeObject*      metaclass;
    const char*        className;

    assert(objc_class != Nil);

    result = objc_class_locate(objc_class);
    if (result != NULL) {
        return result;
    }

    if (class_isMetaClass(objc_class)) {
        result = (PyObject*)PyObjCClass_NewMetaClass(objc_class);
        return result;
    }

    hiddenSelectors = PyDict_New();
    if (hiddenSelectors == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;               // LCOV_EXCL_LINE
    }

    hiddenClassSelectors = PyDict_New();
    if (hiddenClassSelectors == NULL) { // LCOV_BR_EXCL_LINE
        Py_DECREF(hiddenSelectors);     // LCOV_EXCL_LINE
        return NULL;                    // LCOV_EXCL_LINE
    }

    metaclass = PyObjCClass_NewMetaClass(objc_class);
    if (metaclass == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(hiddenSelectors);
        Py_DECREF(hiddenClassSelectors);
        return NULL;
        // LCOV_EXCL_STOP
    }

    dict = PyDict_New();
    if (dict == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(hiddenSelectors);
        Py_DECREF(hiddenClassSelectors);
        Py_DECREF(metaclass);
        return NULL;
        // LCOV_EXCL_STOP
    }

    {
        PyObject* slots = PyTuple_New(0);
        if (slots == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(hiddenSelectors);
            Py_DECREF(hiddenClassSelectors);
            Py_DECREF(metaclass);
            Py_DECREF(dict);
            return NULL;
            // LCOV_EXCL_STOP
        }
        if (PyDict_SetItem(dict, PyObjCNM___slots__, slots) == -1) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(hiddenSelectors);
            Py_DECREF(hiddenClassSelectors);
            Py_DECREF(metaclass);
            Py_DECREF(dict);
            Py_DECREF(slots);
            return NULL;
            // LCOV_EXCL_STOP
        }
        Py_DECREF(slots);
    }

    bases = PyTuple_New(1);
    if (bases == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(hiddenSelectors);
        Py_DECREF(hiddenClassSelectors);
        Py_DECREF(metaclass);
        Py_DECREF(dict);
        return NULL;
        // LCOV_EXCL_STOP
    }

    if (class_getSuperclass(objc_class) == NULL) {
        PyTuple_SET_ITEM(bases, 0, (PyObject*)&PyObjCObject_Type);
        Py_INCREF(((PyObject*)&PyObjCObject_Type));
    } else {
        PyObject* super_class =
            PyObjCClass_New((Class _Nonnull)class_getSuperclass(objc_class));
        if (super_class == NULL) { // LCOV_BR_ECXL_START
            // LCOV_EXCL_START
            Py_DECREF(hiddenSelectors);
            Py_DECREF(hiddenClassSelectors);
            Py_DECREF(metaclass);
            Py_DECREF(dict);
            Py_DECREF(bases);
            return NULL;
            // LCOV_EXCL_STOP
        }
        PyTuple_SET_ITEM(bases, 0, super_class);
    }
    args      = PyTuple_New(3);
    className = class_getName(objc_class);
    PyTuple_SET_ITEM(args, 0, PyUnicode_FromString(className));
    if (PyTuple_GET_ITEM(args, 0) == NULL) { // LCOV_BR_EXLC_LINE
        // LCOV_EXCL_START
        Py_DECREF(hiddenSelectors);
        Py_DECREF(hiddenClassSelectors);
        Py_DECREF(metaclass);
        Py_DECREF(dict);
        Py_DECREF(bases);
        Py_DECREF(args);
        return NULL;
        // LCOV_EXCL_STOP
    }
    PyTuple_SET_ITEM(args, 1, bases);
    PyTuple_SET_ITEM(args, 2, dict);
    bases = NULL;
    dict  = NULL;

    result = PyType_Type.tp_new(metaclass, args, NULL);
    Py_DECREF(args);
    Py_DECREF(metaclass);
    if (result == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(hiddenSelectors);
        Py_DECREF(hiddenClassSelectors);
        return NULL;
        // LCOV_EXCL_STOP
    }

    info                       = (PyObjCClassObject*)result;
    info->class                = objc_class;
    info->sel_to_py            = NULL;
    info->dictoffset           = 0;
    info->useKVO               = 1;
    info->delmethod            = NULL;
    info->hasPythonImpl        = 0;
    info->isCFWrapper          = 0;
    info->isFinal              = 0;
    info->hiddenSelectors      = hiddenSelectors;
    info->hiddenClassSelectors = hiddenClassSelectors;
#ifdef PyObjC_ENABLE_LOOKUP_CACHE
    info->lookup_cache = NULL;
#endif

    /*
     * Support the buffer protocol in the wrappers for NSData and
     * NSMutableData, the only two classes where this makes sense.
     *
     * XXX: This changes the 'result' class after it is 'ready', which
     *      could be problematic.
     */
    if (PyObjC_class_isSubclassOf(objc_class, [NSData class])) {
        ((PyTypeObject*)result)->tp_as_buffer = &nsdata_as_buffer;
        PyType_Modified((PyTypeObject*)result);
        if (PyType_Ready((PyTypeObject*)result) == -1) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(result);
            return NULL;
            // LCOV_EXCL_STOP
        }

    } else if (strcmp(className, "NSBlock") == 0) {
        ((PyTypeObject*)result)->tp_basicsize = sizeof(PyObjCBlockObject);
        PyType_Modified((PyTypeObject*)result);
        if (PyType_Ready((PyTypeObject*)result) == -1) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(result);
            return NULL;
            // LCOV_EXCL_STOP
        }
    }

    if (strncmp(className, "_NSPlaceholder", sizeof("_NSPlaceholder") - 1) == 0) {
        /* Workaround for an issue on macOS 10.15: For some
         * reason the call to class_getInstanceVariable crashes
         * when called early in the process, likely due to an
         * incompletely initialized class.
         *
         * The issue is more widespread in later versions of the OS,
         * and seems to be related to rewriting Foundation in Swift.
         *
         * Issues: #271, #625
         */
        [objc_class class];
    }

    var = class_getInstanceVariable(objc_class, "__dict__");
    if (var != NULL) {
        info->dictoffset = ivar_getOffset(var);
    }

    /*
     * Note: Setting the __module__ attribute is directly invoking the superclass
     * implementation because class_setattro will do the same, and the implementation of
     * class_setattro is dependent on the class being registered using
     * objc_class_register.
     */
    if (PyType_Type.tp_setattro(result, PyObjCNM___module__, PyObjCClass_DefaultModule)
        == -1) {
        PyErr_Clear(); // LCOV_EXCL_LINE
    } // LCOV_EXCL_LINE

    PyObject* existing = objc_class_register(objc_class, result);
    Py_CLEAR(result);
    return existing;
}

PyObject* _Nullable PyObjCClass_ListProperties(PyObject* aClass)
{
    Class     cls   = Nil;
    Protocol* proto = nil;

    if (PyObjCClass_Check(aClass)) {
        cls = PyObjCClass_GetClass(aClass);
        if (cls == Nil) {
            return NULL;
        }

    } else if (PyObjCFormalProtocol_Check(aClass)) {
        proto = PyObjCFormalProtocol_GetProtocol(aClass);

    } else {
        PyErr_SetString(PyExc_TypeError,
                        "class must be an Objective-C class or formal protocol");
        return NULL;
    }

    objc_property_t* props;
    unsigned int     propcount, i;
    char             buf[128];

    if (cls == Nil) {
        return NULL;
    }

    PyObject* result = PyList_New(0);
    if (result == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE
    }

    if (cls) {
        props = class_copyPropertyList(cls, &propcount);

    } else {
        props = protocol_copyPropertyList(proto, &propcount);
    }

    if (props == NULL) {
        return result;
    }

    for (i = 0; i < propcount; i++) {
        PyObject*   item;
        PyObject*   v;
        const char* name = property_getName(props[i]);
        const char* attr = property_getAttributes(props[i]);
        const char* e;

        if (!attr)
            continue;

        item = Py_BuildValue("{sssy}", "name", name, "raw_attr", attr);
        if (item == NULL) { // LCOV_BR_EXCL_LINE
            goto error;     // LCOV_EXCL_LINE
        }
        if (PyList_Append(result, item) == -1) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(item);
            goto error;
            // LCOV_EXCL_STOP
        }
        Py_DECREF(item);

        if (*attr != 'T') {
            /* Attribute string doesn't conform to the
             * 2.0 protocol, don't try to process it.
             */
            continue;
        }

        e = PyObjCRT_SkipTypeSpec(attr + 1);
        if (e == NULL) {
            goto error;
        }
        if (e - (attr + 1) > 127) { /* XXX: What does this do??? */
            v = PyBytes_FromStringAndSize(attr + 1, e - (attr + 1));
        } else {
            PyObjCRT_RemoveFieldNames(buf, attr + 1);
            v = PyBytes_FromString(buf);
        }
        if (v == NULL) { // LCOV_BR_EXCL_LINE
            goto error;  // LCOV_EXCL_LINE
        }

        if (PyDict_SetItem(item, PyObjCNM_typestr, v) == -1) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(v);
            goto error;
            // LCOV_EXCL_STOP
        }
        Py_DECREF(v);
        v = NULL;

        attr = e;
        if (*attr == '"') {
            e = strchr(attr + 1, '"');
            v = PyUnicode_FromStringAndSize(attr + 1, e - (attr + 1));
            if (v == NULL) { // LCOV_BR_EXCL_LINE
                goto error;  // LCOV_EXCL_LINE
            }
            if (PyDict_SetItem(item, PyObjCNM_classname, v) == -1) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                Py_DECREF(v);
                goto error;
                // LCOV_EXCL_STOP
            }
            Py_DECREF(v);
            v    = NULL;
            attr = e + 1;
        }

        if (*attr++ != ',') {
            /* Value doesn't conform to 2.0 protocol */
            continue;
        }

        while (attr && *attr != '\0') {
            switch (*attr++) {
            case 'R':
                if (PyDict_SetItem( // LCOV_BR_EXCL_LINE
                        item, PyObjCNM_readonly, Py_True)
                    == -1) {
                    goto error; // LCOV_EXCL_LINE
                }
                break;

            case 'C':
                if (PyDict_SetItem( // LCOV_BR_EXCL_LINE
                        item, PyObjCNM_copy, Py_True)
                    == -1) {
                    goto error; // LCOV_EXCL_LINE
                }
                break;

            case '&':
                if (PyDict_SetItem( // LCOV_BR_EXCL_LINE
                        item, PyObjCNM_retain, Py_True)
                    == -1) {
                    goto error; // LCOV_EXCL_LINE
                }
                break;

            case 'N':
                if (PyDict_SetItem( // LCOV_BR_EXCL_LINE
                        item, PyObjCNM_nonatomic, Py_True)
                    == -1) {
                    goto error; // LCOV_EXCL_LINE
                }
                break;

            case 'D':
                if (PyDict_SetItem( // LCOV_BR_EXCL_LINE
                        item, PyObjCNM_dynamic, Py_True)
                    == -1) {
                    goto error; // LCOV_EXCL_LINE
                }
                break;

            case 'W':
                if (PyDict_SetItem( // LCOV_BR_EXCL_LINE
                        item, PyObjCNM_weak, Py_True)
                    == -1) {
                    goto error; // LCOV_EXCL_LINE
                }
                break;

            case 'P':
                if (PyDict_SetItem( // LCOV_BR_EXCL_LINE
                        item, PyObjCNM_collectable, Py_True)
                    == -1) {
                    goto error; // LCOV_EXCL_LINE
                }
                break;

            case 'G':
                e = strchr(attr, ',');
                if (e == NULL) {
                    v    = PyBytes_FromString(attr);
                    attr = e;

                } else {
                    v    = PyBytes_FromStringAndSize(attr, e - attr);
                    attr = e;
                }

                if (v == NULL) { // LCOV_BR_EXCL_LINE
                    goto error;  // LCOV_EXCL_LINE
                }

                if (PyDict_SetItem(item, PyObjCNM_getter, v) == -1) { // LCOV_BR_EXCL_LINE
                    // LCOV_EXCL_START
                    Py_DECREF(v);
                    goto error;
                    // LCOV_EXCL_STOP
                }
                break;

            case 'S':
                e = strchr(attr, ',');
                if (e == NULL) {
                    v    = PyBytes_FromString(attr);
                    attr = e;

                } else {
                    v    = PyBytes_FromStringAndSize(attr, e - attr);
                    attr = e;
                }

                if (v == NULL) { // LCOV_BR_EXCL_LINE
                    goto error;  // LCOV_EXCL_LINE
                }

                if (PyDict_SetItem(item, PyObjCNM_setter, v) == -1) { // LCOV_BR_EXCL_LINE
                    // LCOV_EXCL_START
                    Py_DECREF(v);
                    goto error;
                    // LCOV_EXCL_STOP
                }

                break;
            case 'V':
                attr = NULL;
                break;
            }
        }
    }

    free(props);
    props = NULL;

    return result;
error:
    // LCOV_EXCL_START
    if (props) {
        free(props);
    }
    Py_XDECREF(result);
    return NULL;
    // LCOV_EXCL_STOP
}

Class _Nullable PyObjCClass_GetClass(PyObject* cls)
{
    if (PyObjCClass_Check(cls)) {
        Class result = Nil;

        result = ((PyObjCClassObject*)cls)->class;

        if (result == Nil) {
            /* XXX: Audit callers, the field can be Nil */
            // PyErr_SetString(PyObjCExc_Error, "Class object has Nil class");
            return NULL;
        }

        return result;

    } else if (PyObjCMetaClass_Check(cls)) {
        Class result = objc_metaclass_locate(cls);
        if (result == Nil) {
            PyErr_Format(PyObjCExc_InternalError, "Cannot find class for meta class %R",
                         cls);
            return Nil;
        }
        return result;

    } else {
        PyErr_Format(PyObjCExc_InternalError,
                     "PyObjCClass_GetClass called for non-class (%s)",
                     Py_TYPE(cls)->tp_name);
        return Nil;
    }
}

PyObject* _Nullable PyObjCClass_FindSelector(PyObject* cls, SEL selector,
                                             BOOL class_method)
{
    PyObjCClassObject* info;
    PyObject*          result;

    if (!PyObjCClass_Check(cls)) { // LCOV_BR_EXCL_LINE
        /* All callers ensure 'cls' is an actual class */
        // LCOV_EXCL_START
        PyErr_Format(PyObjCExc_InternalError,
                     "PyObjCClass_FindSelector called for non-class (%s)",
                     Py_TYPE(cls)->tp_name);
        return NULL;
        // LCIV_EXCL_STOP
    }

    if (PyObjCClass_CheckMethodList(cls, 1) < 0) {
        return NULL;
    }

    info = (PyObjCClassObject*)cls;
    if (info->sel_to_py == NULL) {
        info->sel_to_py = PyDict_New();
        if (info->sel_to_py == NULL) { // LCOV_BR_EXCL_LINE
            return NULL;               // LCOV_EXCL_LINE
        }
    }

    PyObject* hidden = PyObjCClass_HiddenSelector(cls, selector, class_method);

    if (hidden == NULL && PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;                          // LCOV_EXCL_LINE
    } else if (hidden) {
        Py_CLEAR(hidden);
        PyObject* py_name = PyUnicode_FromString((char*)sel_getName(selector));
        if (py_name == NULL) {
            PyErr_Clear();
        } else {
            int r = PyDict_SetItem(info->sel_to_py, py_name, Py_None);
            if (r == -1) {     // LCOV_BR_EXCL_LINE
                PyErr_Clear(); // LCOV_EXCL_LINE
            }
            Py_DECREF(py_name);
        }
        PyErr_Format(PyExc_AttributeError, "No selector %s", sel_getName(selector));
        return NULL;
    }

    /* First check the cache */

    PyObject* k = PyUnicode_FromString(sel_getName(selector));
    if (k == NULL) { // LCOV_BR_EXCL_LINE
        return NULL; // LCOV_EXCL_LINE
    }

    switch (PyDict_GetItemRef(info->sel_to_py, k, &result)) { // LCOV_BR_EXCL_LINE
    case -1:
        // LCOV_EXCL_START
        Py_DECREF(k);
        return NULL;
        // LCOV_EXCL_STOP
    case 0:
        Py_DECREF(k);
        break;
    case 1:
        Py_DECREF(k);
        if (result == Py_None) {
            /* negative cache entry */
            /* XXX: This is buggy: first looking for a class method where
             *      there's only an instance method will fail and add a negative
             *      entry to the cache, later looking for a class method will
             *      then fail.
             *
             *      Therefore ignore negative cache entries for now...
             */
#if 0
            PyErr_Format(PyExc_AttributeError, "No selector %s", sel_getName(selector));
            return NULL;
#endif
            Py_CLEAR(result);
        } else {
            return result;
        }
    }

    /* Not in the cache. Walk the MRO to check
     * every method object.
     *
     * (We could also generate the most likely
     * python name and check that, but the most
     * likely reason we're called is that this
     * method doesn't exist or isn't good enough)
     */

    PyObject*  mro = ((PyTypeObject*)cls)->tp_mro;
    Py_ssize_t i, n;
    /* XXX: Can MRO be NULL? */

    n = PyTuple_GET_SIZE(mro);
    for (i = 0; i < n; i++) {
        PyObject* c = PyTuple_GET_ITEM(mro, i);

        if (!PyObjCClass_Check(c)) {
            continue;
        }

        PyObject* dict;

        if (class_method) {
            dict = Py_TYPE(c)->tp_dict;
        } else {
            dict = ((PyTypeObject*)c)->tp_dict;
        }

        PyObject*  value = NULL;
        Py_ssize_t pos   = 0;

        while (PyDict_Next(dict, &pos, NULL, &value)) {
            if (!PyObjCSelector_Check(value))
                continue;

            if (sel_isEqual(PyObjCSelector_GetSelector(value), selector)) {
                PyObject* py_name = PyUnicode_FromString((char*)sel_getName(selector));
                if (py_name == NULL) {
                    return NULL;
                }
                if (PyDict_SetItem( // LCOV_BR_EXCL_LINE
                        info->sel_to_py, py_name, value)
                    == -1) {
                    Py_DECREF(py_name);
                    return NULL; // LCOV_EXCL_LINE
                }
                Py_DECREF(py_name);
                Py_INCREF(value);
                return value;
            }
        }
        {
            PyObject* py_name = PyObjC_SELToPythonName(selector);
            if (!py_name) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                PyErr_Clear();
                continue;
                // LCOV_EXCL_STOP
            }

            if (class_method) {
                value = PyObjCMetaClass_TryResolveSelector((PyObject*)Py_TYPE(c), py_name,
                                                           selector);
            } else {
                value = PyObjCClass_TryResolveSelector(c, py_name, selector);
            }
            Py_CLEAR(py_name);
            if (value != NULL) {
                return value;
            } else if (PyErr_Occurred()) {
                return NULL;
            }
        }
    }

    /* If all else fails, ask the actual class (getattro also does this) */
    result = PyObjCSelector_FindNative(cls, sel_getName(selector));
    if (result) {
        return result;
    }

    PyObject* py_name = PyUnicode_FromString((char*)sel_getName(selector));
    if (py_name == NULL) {
        PyErr_Clear();
    } else if (PyDict_SetItem(info->sel_to_py, py_name, Py_None)
               == -1) { // LCOV_BR_EXCL_LINE
        PyErr_Clear();  // LCOV_EXCL_LINE
    }
    PyErr_Format(PyExc_AttributeError, "No selector %s", sel_getName(selector));
    return NULL;
}

Py_ssize_t
PyObjCClass_DictOffset(PyObject* cls)
{
    return ((PyObjCClassObject*)cls)->dictoffset;
}

PyObject* _Nullable PyObjCClass_GetDelMethod(PyObject* cls)
{
    PyObjCClassObject* info;
    info = (PyObjCClassObject*)cls;
    Py_XINCREF(info->delmethod);
    return info->delmethod;
}

int
PyObjCClass_HasPythonImplementation(PyObject* cls)
{
    PyObjCClassObject* info;
    info = (PyObjCClassObject*)cls;
    return info->hasPythonImpl;
}

PyObject* _Nullable PyObjCClass_ClassForMetaClass(PyObject* meta)
{
    if (meta == NULL)
        return NULL;

    Class real_class = objc_metaclass_locate(meta);
    if (real_class == Nil) {
        return NULL;
    }
    return PyObjCClass_New(real_class);
}

int
PyObjCClass_AddMethods(PyObject* classObject, PyObject** methods, Py_ssize_t methodCount)
{
    Class                 targetClass;
    Py_ssize_t            methodIndex;
    int                   r;
    struct PyObjC_method* methodsToAdd;
    size_t                curMethodIndex;
    struct PyObjC_method* classMethodsToAdd;
    size_t                curClassMethodIndex;
    PyObject*             extraDict = NULL;
    PyObject*             metaDict  = NULL;
    PyObject*             protocols = NULL;

    targetClass = PyObjCClass_GetClass(classObject);
    if (targetClass == NULL) {
        return -1;
    }

    if (methodCount == 0) {
        return 0;
    }

    protocols = PyObject_GetAttrString(classObject, "__pyobjc_protocols__");
    if (protocols == NULL) {
        PyErr_Clear();
        protocols = PyList_New(0);
        if (protocols == NULL) {
            return -1;
        }
    }

    extraDict = PyDict_New();
    if (extraDict == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(protocols);
        return -1;
        // LCOV_EXCL_STOP
    }

    metaDict = PyDict_New();
    if (metaDict == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(protocols);
        Py_DECREF(extraDict);
        return -1;
        // LCOV_EXCL_STOP
    }

    methodsToAdd = PyMem_Malloc(sizeof(*methodsToAdd) * methodCount);
    if (methodsToAdd == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(protocols);
        Py_DECREF(extraDict);
        Py_DECREF(metaDict);
        PyErr_NoMemory();
        return -1;
        // LCOV_EXCL_STOP
    }

    classMethodsToAdd = PyMem_Malloc(sizeof(*methodsToAdd) * methodCount);
    if (classMethodsToAdd == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(protocols);
        Py_DECREF(extraDict);
        Py_DECREF(metaDict);
        PyMem_Free(methodsToAdd);
        PyErr_NoMemory();
        return -1;
        // LCOV_EXCL_STOP
    }

    curMethodIndex      = 0;
    curClassMethodIndex = 0;

    for (methodIndex = 0; methodIndex < methodCount; methodIndex++) {
        PyObject*             aMethod = methods[methodIndex];
        PyObject*             name;
        struct PyObjC_method* objcMethod;

        if (PyObjCNativeSelector_Check(aMethod)) {
            PyErr_SetString(PyExc_TypeError, "Cannot add a native selector to other "
                                             "classes");
            goto cleanup_and_return_error;
        }

#if PY_VERSION_HEX < 0x030a0000
        if (PyObject_TypeCheck(aMethod, &PyClassMethod_Type)) {
            PyObject* func = PyObject_GetAttrString(aMethod, "__func__");
            if (func == NULL) {
                goto cleanup_and_return_error;
            }
            name = PyObject_GetAttrString(func, "__name__");
            Py_DECREF(func);
        } else
#endif
            name = PyObject_GetAttrString(aMethod, "__name__");
        if (name == NULL) {
            goto cleanup_and_return_error;
        }

        aMethod = PyObjC_TransformAttribute(name, aMethod, classObject, protocols);
        Py_CLEAR(name);
        if (aMethod == NULL) {
            PyErr_Format(PyExc_TypeError, "All objects in methodArray must be of "
                                          "type <objc.selector>, <function>, "
                                          " <method> or <classmethod>");
            goto cleanup_and_return_error;
        }

        /* install in methods to add */
        if (PyObjCSelector_IsClassMethod(aMethod)) {
            objcMethod = classMethodsToAdd + curClassMethodIndex++;

        } else {
            objcMethod = methodsToAdd + curMethodIndex++;
        }

        objcMethod->name = PyObjCSelector_GetSelector(aMethod);
        objcMethod->type = strdup(PyObjCSelector_Signature(aMethod));

        if (PyObjC_RemoveInternalTypeCodes((char*)(objcMethod->type)) == -1) {
            goto cleanup_and_return_error;
        }
        if (objcMethod->type == NULL) {
            goto cleanup_and_return_error;
        }

        IMP imp = PyObjCFFI_MakeIMPForPyObjCSelector((PyObjCSelector*)aMethod);
        if (imp == NULL) {
            goto cleanup_and_return_error;
        }
        objcMethod->imp = imp;

        name = PyObject_GetAttrString(aMethod, "__name__");

        if (PyBytes_Check(name)) {
            /* XXX: Why support bytes here? */
            PyObject* t =
                PyUnicode_Decode(PyBytes_AsString(name), PyBytes_Size(name), NULL, NULL);
            if (t == NULL) {
                Py_DECREF(name);
                name = NULL;
                Py_DECREF(aMethod);
                aMethod = NULL;
                goto cleanup_and_return_error;
            }
            Py_DECREF(name);
            name = t;
        }

        if (PyObjCSelector_IsHidden(aMethod)) {
            r = PyObjCClass_SetHidden(classObject, objcMethod->name,
                                      PyObjCSelector_IsClassMethod(aMethod), aMethod);
            if (r == -1) {
                goto cleanup_and_return_error;
            }
        }

        r                = 0;
        PyObject* hidden = PyObjCClass_HiddenSelector(
            classObject, objcMethod->name, PyObjCSelector_IsClassMethod(aMethod));
        if (!hidden) {
            if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
                r = -1;             // LCOV_EXCL_LINE
            } else if (PyObjCSelector_IsClassMethod(aMethod)) {
                r = PyDict_SetItem(metaDict, name, aMethod);

            } else {
                r = PyDict_SetItem(extraDict, name, aMethod);
            }
        }
        Py_CLEAR(hidden);

        ((PyObjCSelector*)aMethod)->sel_class = targetClass;

        Py_DECREF(name);
        name = NULL;
        Py_DECREF(aMethod);
        aMethod = NULL;

        if (r == -1) {                     // LCOV_BR_EXCL_LINE
            goto cleanup_and_return_error; // LCOV_EXCL_LINE
        }
    }

    /* add the methods */
    if (curMethodIndex != 0) {
        PyObjC_class_addMethodList(targetClass, methodsToAdd, (unsigned)curMethodIndex);
    }

    PyMem_Free(methodsToAdd);
    methodsToAdd = NULL;
    if (curClassMethodIndex != 0) {
        /* object_getClass will only return Nil if its argument is nil */
        PyObjC_class_addMethodList((Class _Nonnull)object_getClass(targetClass),
                                   classMethodsToAdd, (unsigned)curClassMethodIndex);
    }

    PyMem_Free(classMethodsToAdd);
    classMethodsToAdd = NULL;

    r = PyDict_Merge(((PyTypeObject*)classObject)->tp_dict, extraDict, 1);
    if (r == -1)                       // LCOV_BR_EXCL_LINE
        goto cleanup_and_return_error; // LCOV_EXCL_LINE

    r = PyDict_Merge(Py_TYPE(classObject)->tp_dict, metaDict, 1);
    if (r == -1)                       // LCOV_BR_EXCL_LINE
        goto cleanup_and_return_error; // LCOV_EXCL_LINE

    Py_DECREF(protocols);
    Py_DECREF(extraDict);
    extraDict = NULL;
    Py_DECREF(metaDict);
    metaDict = NULL;

    return 0;

cleanup_and_return_error:
    Py_XDECREF(protocols);
    Py_XDECREF(metaDict);
    Py_XDECREF(extraDict);
    if (methodsToAdd) {
        /* XXX: This should also clear entries */
        PyMem_Free(methodsToAdd);
    }
    if (classMethodsToAdd) {
        /* XXX: This should also clear entries */
        PyMem_Free(classMethodsToAdd);
    }
    return -1;
}

/* Return a new reference */
PyObject* _Nullable PyObjCClass_TryResolveSelector(PyObject* base, PyObject* name,
                                                   SEL sel)
{
    assert(PyObjCClass_Check(base));
    Class cls = PyObjCClass_GetClass(base);
    if (cls == NULL) {
        return NULL;
    }
    /* 'base' is a PyObjCClass instance, using tp_dict is safe */
    PyObject* dict = ((PyTypeObject*)base)->tp_dict;
    Method    m    = class_getInstanceMethod(cls, sel);
    if (m) {
#ifndef PyObjC_FAST_BUT_INEXACT
        int   use = 1;
        Class sup = class_getSuperclass(cls);
        if (sup) {
            Method m_sup = class_getInstanceMethod(sup, sel);
            if (m_sup == m) {
                use = 0;
            }
        }
        if (!use)
            return NULL;
#endif

        /* Create (unbound) selector */
        const char* encoding = method_getTypeEncoding(m);
        if (encoding == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            PyErr_SetString(PyObjCExc_Error, "Native selector with Nil type encoding");
            return NULL;
            // LCOV_EXCL_STOP
        }
        PyObject* result = PyObjCSelector_NewNative(cls, sel, encoding, 0);
        if (result == NULL) { // LCOV_BR_EXCL_LINE
            /* Can only fail if the encoding in the ObjC runtime is
             * invalid.
             */
            return NULL; // LCOV_EXCL_LINE
        }

        /* add to __dict__ 'cache' */
        if (PyDict_SetItem(dict, name, result) == -1) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(result);
            return NULL;
            // LCOV_EXCL_STOP
        }

        return result;
    }
    return NULL;
}

NS_ASSUME_NONNULL_END
