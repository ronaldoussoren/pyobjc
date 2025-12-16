/*
 * This file implements the object/type used to implement
 *    anObject.pyobjc_classMethods.description()
 * and
 *    anObject.pyobjc_instanceMethods.description()
 */
#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

static PyObject* _Nullable find_selector(PyObject* self, const char* name,
                                         int class_method)
{
    SEL                    sel = PyObjCSelector_DefaultSelector(name);
    id                     objc_object;
    NSMethodSignature*     methsig;
    char                   buf[2048];
    int                    unbound_instance_method = 0;
    char*                  flattened               = NULL;
    PyObject*              class_object;
    PyObjCMethodSignature* methinfo = NULL;
    if (name[0] == '_' && name[1] == '_') {
        /* There are no public methods that start with a double underscore,
         * and some Cocoa classes crash hard when looking for them.
         */
        PyErr_Format(PyExc_AttributeError, "No selector %s", name);
        return NULL;
    }

    if (PyObjCClass_Check(self)) {
        objc_object  = (id)PyObjCClass_GetClass(self);
        class_object = self;

        if (!class_method) {
            unbound_instance_method = 1;
        }

        if (objc_object == nil) {
            PyErr_Format(PyExc_AttributeError, "<nil> doesn't have attribute %s", name);
            return NULL;
        }

    } else {
        assert(PyObjCObject_Check(self));

        /* Objective-C class methods cannot be accessed though the
         * instance, class_method will never be true
         */
        assert(!class_method);

        class_object = (PyObject*)Py_TYPE(self);

        objc_object = PyObjCObject_GetObject(self);
        assert(objc_object != nil);
    }

    if (unlikely(strcmp( // LCOV_BR_EXCL_LINE
                     object_getClassName(objc_object), "_NSZombie")
                 == 0)) {
        /* Impossible to hit in regular testing */
        // LCOV_EXCL_START
        PyErr_Format(PyExc_AttributeError, "Cannot access '%s' on deallocated object",
                     name);
        return NULL;
        // LCOV_EXCL_STOP
    }

    if (class_method && strcmp(class_getName((Class)objc_object), "NSProxy") == 0) {
        if (unlikely( // LCOV_BR_EXCL_LINE
                sel == @selector(methodSignatureForSelector:))) {
            // LCOV_EXCL_START
            PyErr_Format(PyExc_AttributeError, "Cannot access NSProxy.%s", name);
            return NULL;
            // LCOV_EXCL_STOP
        }
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (unbound_instance_method) {
                methsig = [objc_object                       // LCOV_BR_EXCL_LINE
                    instanceMethodSignatureForSelector:sel]; // LCOV_BR_EXCL_LINE
            } else {
                methsig =
                    [objc_object methodSignatureForSelector:sel]; // LCOV_BR_EXCL_LINE
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            /* This completely ignores exceptions in getting the signature,
             * but that's fine, Cocoa should never raise here.
             */
            methsig = nil; // LCOV_EXCL_LINE
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (methsig == NULL) {
        PyErr_Format(PyExc_AttributeError, "No selector %s", name);
        return NULL;
    }

    if (!class_method && !PyObjCClass_Check(self)) {
        objc_object = (id _Nonnull)object_getClass(objc_object);
    }

    /* Look for a hidden method, in practice the value (if present)
     * will be:
     * - None: Method is marked as hidden, no more information
     * - objc.selector: Hidden selector, implemented in Python
     * - method signature: Overridden method signature for a hidden method
     */
    PyObject* meta = PyObjCClass_HiddenSelector(class_object, sel, class_method);
    if (unlikely(meta == NULL && PyErr_Occurred())) { // LCOV_BR_EXCL_LINE
        return NULL;                                  // LCOV_EXCL_LINE
    }

    if (meta) {
        if (PyObjCSelector_Check(meta)) {
            /*
             * KVO complicates things, it will insert an intermediate
             * class that overrides KVO-related methods and those need
             * to be called to ensure KVO actually works.
             *
             * Because of this "meta" can only be used as-is when
             * it resolves to the same IMP as accessing the IMP through
             * the instance. If it doesn't we can only use the signature;
             *
             * XXX: The code is not 100% reliable and could be problematic
             *      when ObjC code replaces the method IMP. Fixing that
             *      is possible, but requires fairly invasive changes.
             */
            if (class_method) {
                /* AFAIK class methods cannot be used for KVO, ignore the
                 * issue here.
                 */
                return meta;
            } else {
                IMP sel_imp =
                    [PyObjCSelector_GetClass(meta) instanceMethodForSelector:sel];
                IMP cur_imp;

                /* XXX: The typecheck here is necessary because some callers pass a
                 *      class, I'm not yet sure this is correct. Found by stricter
                 *      checks in PyObjCObject_GetObject.
                 */
                if (PyObjCObject_Check(self)) {
                    cur_imp = [PyObjCObject_GetObject(self) methodForSelector:sel];
                } else if (likely(PyObjCClass_Check(self))) { // LCOV_BR_EXCL_LINE
                    cur_imp = [PyObjCClass_GetClass(self) methodForSelector:sel];
                } else {
                    // LCOV_EXCL_START
                    PyErr_SetString(PyObjCExc_Error,
                                    "Unsupported case for find_selector");
                    return NULL;
                    // LCOV_EXCL_STOP
                }

                if (sel_imp == cur_imp) {
                    return meta;
                } else {
                    methinfo = PyObjCSelector_GetMetadata(meta);
                    if (unlikely(methinfo == NULL)) { // LCOV_BR_EXCL_LINE
                        // LCOV_EXCL_START
                        Py_DECREF(meta);
                        return NULL;
                        // LCOV_EXCL_STOP
                    }
                    flattened = (char*)methinfo->signature;

                    /* Cannot decref 'methinfo' here because 'flattened'
                     * is used below.
                     */
                }
            }
        }
        Py_CLEAR(meta);
    }

    if (flattened == NULL) {
        flattened = PyObjC_NSMethodSignatureToTypeString(methsig, buf, sizeof(buf));
    }

    if (unlikely(flattened == NULL)) { // LCOV_BR_EXCL_LINE
        /* PyObjC_NSMethodSignatureToTypeString can only fail when
         * the NSMethodSignature is invalid, or if the encoded
         * signature would not fit buffer.
         */
        // LCOV_EXCL_START
        Py_CLEAR(methinfo);
        return NULL;
        // LCOV_EXCL_STOP
    }

    Py_CLEAR(methinfo);
    return PyObjCSelector_NewNative((Class)objc_object, sel, flattened, class_method);
}

static PyObject* _Nullable make_dict(PyObject* self, int class_method)
{
    Class        cls;
    PyObject*    res;
    Method*      methods;
    unsigned int i, method_count;
    Class        objc_class;

    if (PyObjCClass_Check(self)) {
        cls        = PyObjCClass_GetClass(self);
        objc_class = cls;

        if (class_method) {
            objc_class = object_getClass(cls);
        }

    } else {
        assert(PyObjCObject_Check(self));
        assert(!class_method);

        id obj = PyObjCObject_GetObject(self);
        assert(obj != nil);

        cls        = object_getClass(obj);
        objc_class = cls;
    }

    res = PyDict_New();
    if (unlikely(res == NULL)) { // LCOV_BR_EXCL_LINE
        return NULL;             // LCOV_EXCL_LINE
    }

    for (; objc_class != NULL && cls != NULL;
         objc_class = class_getSuperclass((Class)objc_class),
         cls        = class_getSuperclass((Class)cls)) {
        methods = class_copyMethodList(objc_class, &method_count);

        if (unlikely(methods == NULL)) { // LCOV_BR_EXCL_LINE
            continue;                    // LCOV_EXCL_LINE
        }

        for (i = 0; i < method_count; i++) {
            PyObject* v;
            PyObject* py_name;

            py_name = PyObjC_SELToPythonName(method_getName(methods[i]));
            if (unlikely(py_name == NULL)) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                free(methods);
                Py_DECREF(res);
                return NULL;
                // LCOV_EXCL_STOP
            }

            /* Check if py_name is already in the dict to avoid
             * replacing a more specific definition.
             */
            switch (PyDict_GetItemRef(res, py_name, &v)) { // LCOV_BR_EXCL_LINE
            case -1:
                // LCOV_EXCL_START
                Py_CLEAR(py_name);
                Py_CLEAR(res);
                return NULL;
                // LCOV_EXCL_STOP
            case 0:
                break;
            case 1:
                Py_CLEAR(v);
                Py_CLEAR(py_name);
                continue;
            }

            /* XXX: This needs some documentation. Basically resolve the method
             * through normal lookup first, that avoids replicating
             * objc_object.tp_getattro here.
             */
            v = PyObject_GetAttr(self, py_name);
            if (v == NULL) {
                PyErr_Clear();

            } else if (!PyObjCSelector_Check(v)) {
                Py_CLEAR(v);

            } else {
                int cm = ((PyObjCSelector*)v)->sel_flags & PyObjCSelector_kCLASS_METHOD;

                if (!cm != !class_method) {
                    Py_CLEAR(v);
                }
            }

            if (v == NULL) {
                const char* type_encoding = method_getTypeEncoding(methods[i]);
                if (unlikely(type_encoding == NULL)) { // LCOV_BR_EXCL_LINE
                    // LCOV_EXCL_START
                    PyErr_SetString(PyObjCExc_Error,
                                    "Native selector with Nil type encoding");
                    free(methods);
                    Py_CLEAR(py_name);
                    Py_DECREF(res);
                    return NULL;
                    // LCOV_EXCL_STOP
                }

                v = PyObjCSelector_NewNative(cls, method_getName(methods[i]),
                                             type_encoding, class_method);

                if (unlikely(v == NULL)) { // LCOV_BR_EXCL_LINE
                    /* This can fail for methods with an unknown encoding.
                     *
                     * Ignoring the error is more useful than raising.
                     */
                    // LCOV_EXCL_START
                    Py_CLEAR(py_name);
                    PyErr_Clear();
                    continue;
                    // LCOV_EXCL_STOP
                }
            } // LCOV_BR_EXCL_LINE

            if (unlikely(PyDict_SetItem(res, py_name, v) == -1)) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                Py_DECREF(v);
                Py_DECREF(res);
                Py_CLEAR(py_name);
                free(methods);
                return NULL;
                // LCOV_EXCL_STOP
            }

            Py_CLEAR(py_name);
            Py_CLEAR(v);
        } // LCOV_BR_EXCL_LINE

        free(methods);
    }

    return res;
}

typedef struct {
    PyObject_HEAD
    PyObject* base;
    int       class_method;
} PyObjCMethodAccessor;

static void
methacc_dealloc(PyObject* _self)
{
    PyObjCMethodAccessor* self = (PyObjCMethodAccessor*)_self;

    PyObject_GC_UnTrack(_self);

    /* Don't use CLEAR because the invariant
     * is that 'base' is not NULL.
     *
     * Setting the field to NULL anyway
     * is safe because we deallocate right
     * afterwards.
     */
    Py_DECREF(self->base);
    self->base = (PyObject* _Nonnull)NULL;

    PyTypeObject* tp = Py_TYPE(self);
    PyObject_GC_Del(_self);
    Py_DECREF(tp);
}

static int
methacc_traverse(PyObject* _self, visitproc visit, void* _Nullable arg)
{
    PyObjCMethodAccessor* self = (PyObjCMethodAccessor*)_self;
    Py_VISIT(self->base);
    return 0;
}

// LCOV_EXCL_START
// Instances of this type cannot be part of a loop: This type has
// references to an ObjC type of instance. Instances only have
// references to their type, and ObjC types are immortal.
//
// Even when an ObjC class has (Python) attributes those are stored
// on the actual ObjC object, not on the ``PyObjCObject*`` value.
static int
methacc_clear(PyObject* _self)
{
    PyObjCMethodAccessor* self = (PyObjCMethodAccessor*)_self;

    /* Maintain the invariant that 'base' is not NULL */
    PyObject* tmp = self->base;
    self->base    = Py_None;
    Py_INCREF(Py_None);
    Py_CLEAR(tmp);

    return 0;
}
// LCOV_EXCL_STOP

static PyObject* _Nullable methacc_getattro(PyObject* _self, PyObject* name)
{
    PyObjCMethodAccessor* self   = (PyObjCMethodAccessor*)_self;
    PyObject*             result = NULL;

    assert(PyObjCObject_Check(self->base) || PyObjCClass_Check(self->base));

    if (likely(PyUnicode_Check(name))) {                // LCOV_BR_EXCL_LINE
        if (unlikely(PyUnicode_AsUTF8(name) == NULL)) { // LCOV_BR_EXCL_LINE
            return NULL;                                // LCOV_EXCL_LINE
        }

    } else { // LCOV_BR_EXCL_LINE
        /* This should never happen, CPython checks for the type of 'name'
         * before calling this slot.
         */
        // LCOV_EXCL_START
        PyErr_Format(PyExc_TypeError, "Expecting string, got %s", Py_TYPE(name)->tp_name);
        return NULL;
        // LCOV_EXCL_STOP
    }

    if (PyObjC_is_ascii_string(name, "__dict__")) {

        PyObject* dict;
        dict = make_dict(self->base, self->class_method);
        if (unlikely(dict == NULL)) { // LCOV_BR_EXCL_LINE
            return NULL;              // LCOV_EXCL_LINE
        }

        result = PyDictProxy_New(dict);
        Py_DECREF(dict);
        return result;
    }

    if (PyObjC_is_ascii_string(name, "__methods__")) {

        PyErr_SetString(PyExc_AttributeError, "No such attribute: __methods__");
        return NULL;
    }

    if (PyObjC_is_ascii_string(name, "__members__")) {

        PyErr_SetString(PyExc_AttributeError, "No such attribute: __members__");
        return NULL;
    }

    if (self->class_method) {
        assert(PyObjCClass_Check(self->base));
        result = PyObject_GetAttr(self->base, name);

    } else {
        assert(PyObjCClass_Check(self->base) || PyObjCObject_Check(self->base));
        /* Walk the mro and look in the class dict */
        PyObject* mro;
        PyObject* descr_arg;

        if (PyObjCClass_Check(self->base)) {
            mro       = ((PyTypeObject*)self->base)->tp_mro;
            descr_arg = NULL;
        } else {
            mro       = (Py_TYPE(self->base))->tp_mro;
            descr_arg = self->base;
        }
        Py_ssize_t i, len;

        len = PyTuple_GET_SIZE(mro);
        for (i = 0; i < len && result == NULL; i++) {
            PyObject* c = PyTuple_GET_ITEM(mro, i);
            if (!PyObjCClass_Check(c))
                continue;

            PyObject* dict = PyType_GetDict((PyTypeObject*)c);
            PyObject* v;

            int r = PyDict_GetItemRef(dict, name, &v);
            if (unlikely(r == -1)) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                Py_CLEAR(dict);
                return NULL;
                // LCOV_EXCL_STOP
            } else if (r == 1) {
                if (PyObjCSelector_Check(v)) {
                    /* Found it, use the
                     * descriptor mechanism to
                     * fetch the actual result
                     */
                    v = Py_TYPE(v)->tp_descr_get(v, descr_arg, (PyObject*)Py_TYPE(v));
                    if (unlikely(v == NULL)) { // LCOV_BR_EXCL_LINE
                        Py_CLEAR(dict);        // LCOV_EXCL_LINE
                        return NULL;           // LCOV_EXCL_LINE
                    }
                    result = v;
                } else {
                    Py_DECREF(v);
                }
                /* Found an item with the specified
                 * name, abort the search.
                 */
                Py_CLEAR(dict);
                break;
            }
        } // LCOV_BR_EXCL_LINE
    } // LCOV_BR_EXCL_LINE

    if (result != NULL) {
        if (!PyObjCSelector_Check(result)) {
            Py_DECREF(result);
            result = NULL;
        }
    } else {
        /* PyObject_GetAttr failed, ignore the exception
         * because we'll search in a different way below.
         */
        PyErr_Clear();
    }

    if (result) {
        if (self->class_method) {
            if (!PyObjCSelector_IsClassMethod(result)) {
                Py_DECREF(result);
                result = NULL;
            }
        } else {
            if (PyObjCSelector_IsClassMethod(result)) {
                Py_DECREF(result);
                result = NULL;
            }
        }
    }

    if (result != NULL) {
        return result;
    }

    /* Didn't find the selector the first trip around, try harder. */
    const char* name_bytes = PyUnicode_AsUTF8(name);
    if (unlikely(name_bytes == NULL)) { // LCOV_BR_EXCL_LINE
        return NULL;                    // LCOV_EXCL_LINE
    }

    @autoreleasepool {
        result = find_selector(self->base, name_bytes, self->class_method);
    }
    if (result == NULL) {
        return result;
    }

    if (!self->class_method && PyObjCClass_Check(self->base)) {
        /* Unbound instance method */
        assert(((PyObjCSelector*)result)->sel_self == NULL);
        return result;
    } else {
        /* Bound instance or class method
         *
         * This needs to create a new selector because the value
         * might be a "hidden" selector.
         */
        PyObject* tmp =
            PyObject_CallMethod(result, "__get__", "OO", self->base, Py_TYPE(self->base));
        Py_DECREF(result);
        return tmp;
    }
}

static PyObject* _Nullable methacc_repr(PyObject* _self)
{
    PyObjCMethodAccessor* self = (PyObjCMethodAccessor*)_self;
    PyObject*             rval;

    rval = PyUnicode_FromFormat("<%s method-accessor for %R>",
                                self->class_method ? "class" : "instance", self->base);

    return rval;
}

static PyObject* _Nullable methacc_dir(PyObject* self)
{
    PyObject* dict = make_dict(((PyObjCMethodAccessor*)self)->base,
                               ((PyObjCMethodAccessor*)self)->class_method);
    PyObject* result;

    if (unlikely(dict == NULL)) { // LCOV_BR_EXCL_LINE
        return NULL;              // LCOV_EXCL_LINE
    }

    result = PyMapping_Keys(dict);
    Py_DECREF(dict);

    return result;
}

static PyMethodDef methacc_methods[] = {{
                                            .ml_name  = "__dir__",
                                            .ml_meth  = (PyCFunction)methacc_dir,
                                            .ml_flags = METH_NOARGS,
                                        },
                                        {
                                            .ml_name = NULL /* SENTINEL */
                                        }};

static PyType_Slot methacc_slots[] = {
    {.slot = Py_tp_dealloc, .pfunc = (void*)&methacc_dealloc},
    {.slot = Py_tp_clear, .pfunc = (void*)&methacc_clear},
    {.slot = Py_tp_traverse, .pfunc = (void*)&methacc_traverse},
    {.slot = Py_tp_repr, .pfunc = (void*)&methacc_repr},
    {.slot = Py_tp_getattro, .pfunc = (void*)&methacc_getattro},
    {.slot = Py_tp_methods, .pfunc = (void*)&methacc_methods},
    {0, NULL} /* sentinel */
};

static PyType_Spec methacc_spec = {
    .name      = "objc._method_access",
    .basicsize = sizeof(PyObjCMethodAccessor),
    .itemsize  = 0,
    .flags     = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE | Py_TPFLAGS_IMMUTABLETYPE
             | Py_TPFLAGS_DISALLOW_INSTANTIATION | Py_TPFLAGS_HAVE_GC,
    .slots = methacc_slots,
};

static PyObject* PyObjCMethodAccessor_Type;

PyObject* _Nullable PyObjCMethodAccessor_New(PyObject* base, int class_method)
{
    PyObjCMethodAccessor* result;
    assert(PyObjCObject_Check(base) || PyObjCClass_Check(base));
    if (class_method) {
        assert(PyObjCClass_Check(base));
    }

    result =
        PyObject_GC_New(PyObjCMethodAccessor, (PyTypeObject*)PyObjCMethodAccessor_Type);
    if (unlikely(result == NULL)) // LCOV_BR_EXCL_LINE
        return NULL;              // LCOV_EXCL_LINE

    result->base = base;
    Py_XINCREF(base);
    result->class_method = class_method;

    PyObject_GC_Track((PyObject*)result);

    return (PyObject*)result;
}

int
PyObjCMethodAccessor_Setup(PyObject* module __attribute__((__unused__)))
{
    PyObject* tmp = PyType_FromSpec(&methacc_spec);
    if (unlikely(tmp == NULL)) { // LCOV_BR_EXCL_LINE
        return -1;               // LCOV_EXCL_LINE
    }
    PyObjCMethodAccessor_Type = tmp;
    return 0;
}

NS_ASSUME_NONNULL_END
