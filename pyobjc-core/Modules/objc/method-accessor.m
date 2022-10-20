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
    SEL                sel = PyObjCSelector_DefaultSelector(name);
    id                 objc_object;
    NSMethodSignature* methsig;
    char               buf[2048];
    int                unbound_instance_method = 0;
    char*              flattened               = NULL;
    PyObject*          class_object;

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

    } else {
        PyObjC_Assert(PyObjCObject_Check(self), NULL);

        /* Objective-C class methods cannot be accessed though the
         * instance, class_method will never be true
         */
        PyObjC_Assert(!class_method, NULL);

        class_object = (PyObject*)Py_TYPE(self);

        objc_object = PyObjCObject_GetObject(self);
    }

    if (objc_object == nil) {
        PyErr_Format(PyExc_AttributeError, "<nil> doesn't have attribute %s", name);
        return NULL;
    }

    if (strcmp(object_getClassName(objc_object), "_NSZombie") == 0) { // LCOV_BR_EXCL_LINE
        /* Impossible to hit in regular testing */
        // LCOV_EXCL_START
        PyErr_Format(PyExc_AttributeError, "Cannot access '%s' on deallocated object",
                     name);
        return NULL;
        // LCOV_EXCL_STOP
    }

    if (class_method && strcmp(class_getName((Class)objc_object), "NSProxy") == 0) {
        if (sel == @selector(methodSignatureForSelector:)) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            PyErr_Format(PyExc_AttributeError, "Cannot access NSProxy.%s", name);
            return NULL;
            // LCOV_EXCL_STOP
        }
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (unbound_instance_method) {
                methsig = [objc_object instanceMethodSignatureForSelector:sel];
            } else {
                methsig = [objc_object methodSignatureForSelector:sel];
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            /* This completely ignores exceptions in getting the signature,
             * but that's fine, Cocoa should never raise here.
             */
            methsig = nil; // LCOV_EXCL_LINE
        }                  // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (methsig == NULL) {
        PyErr_Format(PyExc_AttributeError, "No selector %s", name);
        return NULL;
    }

    if (!class_method) {
        objc_object = (id)object_getClass(objc_object);
    }

    /* XXX: This needs documentation */
    PyObject* meta = PyObjCClass_HiddenSelector(class_object, sel, class_method);
    if (meta == NULL && PyErr_Occurred()) {
        return NULL;
    }

    if (meta && meta != Py_None) {
        flattened = (char*)((PyObjCMethodSignature*)meta)->signature;
    }

    if (flattened == NULL) {
        flattened = PyObjC_NSMethodSignatureToTypeString(methsig, buf, sizeof(buf));
    }

    if (flattened == NULL) { // LCOV_BR_EXCL_LINE
        /* PyObjC_NSMethodSignatureToTypeString can only fail when
         * the NSMethodSignature is invalid, or if the encoded
         * signature would not fit buffer.
         */
        return NULL; // LCOV_EXCL_LINE
    }

    return PyObjCSelector_NewNative((Class)objc_object, sel, flattened, class_method);
}

static PyObject* _Nullable make_dict(PyObject* self, int class_method)
{
    Class        cls;
    PyObject*    res;
    Method*      methods;
    unsigned int i, method_count;
    char         buf[256];
    Class        objc_class;

    if (PyObjCClass_Check(self)) {
        cls        = PyObjCClass_GetClass(self);
        objc_class = cls;

        if (class_method) {
            objc_class = object_getClass(cls);
        }

    } else {
        PyObjC_Assert(PyObjCObject_Check(self), NULL);
        PyObjC_Assert(!class_method, NULL);

        id obj = PyObjCObject_GetObject(self);

        if (obj == NULL) {
            return PyDict_New();
        }

        cls        = object_getClass(obj);
        objc_class = cls;
    }

    res = PyDict_New();
    if (res == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;   // LCOV_EXCL_LINE
    }

    for (; objc_class != NULL && cls != NULL;
         objc_class = class_getSuperclass((Class)objc_class),
         cls        = class_getSuperclass((Class)cls)) {
        methods = class_copyMethodList(objc_class, &method_count);

        if (methods == NULL) { // LCOV_BR_EXCL_LINE
            continue;          // LCOV_EXCL_LINE
        }

        for (i = 0; i < method_count; i++) {
            PyObject* v;
            char*     name;

            name = PyObjC_SELToPythonName(method_getName(methods[i]), buf, sizeof(buf));
            if (name == NULL) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                free(methods);
                Py_DECREF(res);
                return NULL;
                // LCOV_EXCL_STOP
            }

            v = PyObject_GetAttrString(self, name);
            if (v == NULL) {
                PyErr_Clear();

            } else if (!PyObjCSelector_Check(v)) {
                Py_DECREF(v);
                v = NULL;

            } else {
                int cm = ((PyObjCSelector*)v)->sel_flags & PyObjCSelector_kCLASS_METHOD;

                if (!cm != !class_method) {
                    Py_DECREF(v);
                    v = NULL;
                }
            }

            if (v == NULL) {
                const char* type_encoding = method_getTypeEncoding(methods[i]);
                if (type_encoding == NULL) { // LCOV_BR_EXCL_LINE
                    // LCOV_EXCL_START
                    PyErr_SetString(PyObjCExc_Error,
                                    "Native selector with Nil type encoding");
                    free(methods);
                    Py_DECREF(res);
                    return NULL;
                    // LCOV_EXCL_STOP
                }

                v = PyObjCSelector_NewNative(cls, method_getName(methods[i]),
                                             type_encoding, class_method);

                if (v == NULL) { // LCOV_BR_EXCL_LINE
                    /* This can fail for methods with an unknown encoding.
                     *
                     * Ignoring the error is more useful than raising.
                     */
                    // LCOV_EXCL_START
                    PyErr_Clear();
                    continue;
#if 0
                    free(methods);
                    Py_DECREF(res);
                    return NULL;
#endif
                    // LCOV_EXCL_STOP
                }
            }

            if (PyDict_SetItemString(res, name, v) == -1) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                Py_DECREF(v);
                Py_DECREF(res);
                free(methods);
                return NULL;
                // LCOV_EXCL_STOP
            }

            Py_DECREF(v);
        }

        free(methods);
    }

    return res;
}

typedef struct {
    PyObject_HEAD
    PyObject* base;
    int       class_method;
} ObjCMethodAccessor;

static void
obj_dealloc(PyObject* _self)
{
    ObjCMethodAccessor* self = (ObjCMethodAccessor*)_self;

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

    PyObject_GC_Del(_self);
}

static int
obj_traverse(PyObject* _self, visitproc visit, void* _Nullable arg)
{
    ObjCMethodAccessor* self = (ObjCMethodAccessor*)_self;
    Py_VISIT(self->base);
    return 0;
}

static int
obj_clear(PyObject* _self)
{
    ObjCMethodAccessor* self = (ObjCMethodAccessor*)_self;

    /* Maintain the invariant that 'base' is not NULL */
    PyObject* tmp = self->base;
    self->base    = Py_None;
    Py_INCREF(Py_None);
    Py_CLEAR(tmp);

    return 0;
}

static PyObject* _Nullable obj_getattro(PyObject* _self, PyObject* name)
{
    ObjCMethodAccessor* self   = (ObjCMethodAccessor*)_self;
    PyObject*           result = NULL;

    if (PyUnicode_Check(name)) {
        if (PyObjC_Unicode_Fast_Bytes(name) == NULL) {
            return NULL;
        }

    } else {
        PyErr_Format(PyExc_TypeError, "Expecting string, got %s", Py_TYPE(name)->tp_name);
        return NULL;
    }

    if (PyObjC_is_ascii_string(name, "__dict__")) {

        PyObject* dict;
        dict = make_dict(self->base, self->class_method);
        if (dict == NULL) {
            return NULL;
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
        PyObjC_Assert(PyObjCClass_Check(self->base), NULL);
        result = PyObject_GetAttr(self->base, name);

    } else {
        if (PyObjCClass_Check(self->base) || PyObjCObject_Check(self->base)) {
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

                PyObject* dict = ((PyTypeObject*)c)->tp_dict;
                PyObject* v    = PyDict_GetItemWithError(dict, name);
                if (v == NULL && PyErr_Occurred()) {
                    return NULL;

                } else if (v != NULL) {
                    if (PyObjCSelector_Check(v)) {
                        /* Found it, use the
                         * descriptor mechanism to
                         * fetch the actual result
                         */
                        v = Py_TYPE(v)->tp_descr_get(v, descr_arg, (PyObject*)Py_TYPE(v));
                        if (v == NULL) {
                            return NULL;
                        }
                        result = v;
                        Py_INCREF(result);
                    }
                    /* Found an item with the specified
                     * name, abort the search.
                     */
                    break;
                }
            }

        } else {
            result = PyObject_GetAttr(self->base, name);
        }
    }

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
    const char* name_bytes = PyObjC_Unicode_Fast_Bytes(name);
    if (name_bytes == NULL) {
        return NULL;
    }
    result = find_selector(self->base, name_bytes, self->class_method);
    if (result == NULL) {
        return result;
    }

    if (!self->class_method && PyObjCClass_Check(self->base)) {
        /* Unbound instance method */
        ((PyObjCSelector*)result)->sel_self = NULL;
    } else {
        /* Bound instance or class method */
        ((PyObjCSelector*)result)->sel_self = self->base;
        Py_INCREF(self->base);
    }

    return result;
}

static PyObject* _Nullable obj_repr(PyObject* _self)
{
    ObjCMethodAccessor* self = (ObjCMethodAccessor*)_self;
    PyObject*           rval;

    rval = PyUnicode_FromFormat("<%s method-accessor for %R>",
                                self->class_method ? "class" : "instance", self->base);

    return rval;
}

static PyObject* _Nullable obj_dir(PyObject* self)
{
    PyObject* dict = make_dict(((ObjCMethodAccessor*)self)->base,
                               ((ObjCMethodAccessor*)self)->class_method);
    PyObject* result;

    if (dict == NULL) {
        return NULL;
    }

    result = PyMapping_Keys(dict);
    Py_DECREF(dict);

    return result;
}

static PyMethodDef obj_methods[] = {{
                                        .ml_name  = "__dir__",
                                        .ml_meth  = (PyCFunction)obj_dir,
                                        .ml_flags = METH_NOARGS,
                                    },
                                    {
                                        .ml_name = NULL /* SENTINEL */
                                    }};

PyTypeObject PyObjCMethodAccessor_Type = {
    PyVarObject_HEAD_INIT(&PyType_Type, 0).tp_name = "objc.method_acces",
    .tp_basicsize                                  = sizeof(ObjCMethodAccessor),
    .tp_itemsize                                   = 0,
    .tp_dealloc                                    = obj_dealloc,
    .tp_clear                                      = obj_clear,
    .tp_traverse                                   = obj_traverse,
    .tp_repr                                       = obj_repr,
    .tp_getattro                                   = obj_getattro,
    .tp_flags   = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HAVE_GC,
    .tp_methods = obj_methods,
};

PyObject* _Nullable PyObjCMethodAccessor_New(PyObject* base, int class_method)
{
    ObjCMethodAccessor* result;
    PyObjC_Assert(PyObjCObject_Check(base) || PyObjCClass_Check(base), NULL);
    if (class_method) {
        PyObjC_Assert(PyObjCClass_Check(base), NULL);
    }

    result = PyObject_GC_New(ObjCMethodAccessor, &PyObjCMethodAccessor_Type);
    if (result == NULL) // LCOV_BR_EXCL_LINE
        return NULL;    // LCOV_EXCL_LINE

    result->base = base;
    Py_XINCREF(base);
    result->class_method = class_method;

    PyObject_GC_Track((PyObject*)result);

    return (PyObject*)result;
}

NS_ASSUME_NONNULL_END
