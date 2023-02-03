/*
 * A subclass of the builtin super type that works correctly when resolving
 * class methods.
 *
 * The problem is that the default ``super`` object walks the class an peeks
 * inside the class dict instead of using an API. That causes a problem because
 * the class methods of an ObjC class aren't stored in the class __dict__ but
 * in the __dict__ of the metaclass, which isn't advertised to Python code.
 */

#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

/*
 * NOTE: This is a minor tweak of Python 2.5's super_getattro and is a rather
 * crude hack.
 *
 * NOTE: updated for 3.2, and 2.7
 */
typedef struct {
    PyObject_HEAD

    PyTypeObject* type;
    PyObject*     obj;
    PyTypeObject* obj_type;
} superobject;

static PyObject* _Nullable super_getattro(PyObject* self, PyObject* name)
{
    superobject* su   = (superobject*)self;
    int          skip = su->obj_type == NULL;
    SEL          sel;

    if (!skip) {
        /* We want __class__ to return the class of the super object
         * (i.e. super, or a subclass), not the class of su->obj.
         */
        if (PyUnicode_Check(name)) {
            skip = PyObjC_is_ascii_string(name, "__class__");

        } else {
            skip = 0;
        }
    }

    if (PyUnicode_Check(name)) {
        const char* b = PyObjC_Unicode_Fast_Bytes(name);
        if (b == NULL) { // LCOV_BR_EXCL_LINE
            return NULL; // LCOV_EXCL_LINE
        }

        sel = PyObjCSelector_DefaultSelector(b);

    } else if (!skip) { // LCOV_BR_EXCL_LINE
        /* This should hever happen, Python's attribute machinery
         * rejects attribute names of the wrong type
         */
        // LCOV_EXCL_START
        PyErr_SetString(PyExc_TypeError, "attribute name is not a string");
        return NULL;
        // LCOV_EXCL_STOP
    }

    if (!skip) {
        PyObject *    mro, *res, *tmp, *dict;
        PyTypeObject* starttype;
        descrgetfunc  f;
        Py_ssize_t    i, n = 0;

        starttype = su->obj_type;
        mro       = starttype->tp_mro;

        if (mro != NULL) {
            PyObjC_Assert(PyTuple_Check(mro), NULL);
            n = PyTuple_GET_SIZE(mro);
        }

        for (i = 0; i < n; i++) {
            if ((PyObject*)(su->type) == PyTuple_GET_ITEM(mro, i))
                break;
        }

        i++;
        res = NULL;
        for (; i < n; i++) {
            tmp = PyTuple_GET_ITEM(mro, i);

            /* PyObjC PATCH: Treat PyObjC class objects specially to maintain
             * the proper illusion for users.
             * Also make sure that the method tables are up-to-date.
             */
            if (PyObjCClass_Check(tmp)) {
                if (PyObjCClass_CheckMethodList(tmp, NO) < 0) { // LCOV_BR_EXCL_LINE
                    return NULL;                                // LCOV_EXCL_LINE
                }
            }

            if (PyObjCClass_Check(tmp) && PyObjCClass_Check(su->obj)) {
                dict = Py_TYPE(tmp)->tp_dict;

            } else if (PyType_Check(tmp)) {
                dict = ((PyTypeObject*)tmp)->tp_dict;

            } else {
                continue;
            }

            res = PyDict_GetItemWithError(dict, name);
            if (res == NULL && PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
                return NULL;                       // LCOV_EXCL_LINE
            } else if (res != NULL) {
                Py_INCREF(res);
                f = Py_TYPE(res)->tp_descr_get;
                if (f != NULL) {
                    tmp = f(
                        res,
                        /* Only pass 'obj' param if
                           this is instance-mode super
                           (See SF ID #743627)
                        */
                        (su->obj == (PyObject*)su->obj_type ? (PyObject*)NULL : su->obj),
                        (PyObject*)starttype);
                    Py_DECREF(res);
                    res = tmp;
                }
                return res;
            }

            if (PyObjCClass_Check(tmp)) {
                if (!PyObjCClass_Check(su->obj)) {
                    res = PyObjCClass_TryResolveSelector(tmp, name, sel);
                } else {
                    res = PyObjCMetaClass_TryResolveSelector((PyObject*)Py_TYPE(tmp),
                                                             name, sel);
                }

                if (res) {
                    Py_INCREF(res);
                    f = Py_TYPE(res)->tp_descr_get;
                    if (f != NULL) {
                        tmp = f(res,
                                /* Only pass 'obj' param if
                                   this is instance-mode super
                                   (See SF ID #743627)
                                */
                                (su->obj == (PyObject*)su->obj_type ? (PyObject*)NULL
                                                                    : su->obj),
                                (PyObject*)starttype);
                        Py_DECREF(res);
                        res = tmp;
                    }

                    return res;

                } else if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
                    return NULL;               // LCOV_EXCL_LINE
                }
            }
        }
    }
    return PyObject_GenericGetAttr(self, name);
}

static void
super_dealloc(PyObject* obj)
{
    Py_CLEAR(((superobject*)obj)->type);
    Py_CLEAR(((superobject*)obj)->obj);
    Py_CLEAR(((superobject*)obj)->obj_type);

    PyTypeObject* tp = Py_TYPE(obj);
    tp->tp_free(obj);
#if PY_VERSION_HEX >= 0x030a0000
    Py_DECREF(tp);
#endif
}

static PyType_Slot super_slots[] = {
    {.slot = Py_tp_getattro, .pfunc = (void*)&super_getattro},
    {.slot = Py_tp_dealloc, .pfunc = (void*)&super_dealloc},
    {.slot = Py_tp_doc, .pfunc = NULL},
    {0, NULL} /* sentinel */
};

static PyType_Spec super_spec = {
    .name      = "objc.super",
    .basicsize = sizeof(superobject),
    .itemsize  = 0,
    .flags     = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE,
    .slots     = super_slots,
};

static PyObject* PyObjCSuper_Type;

int
PyObjCSuper_Setup(PyObject* module)
{
    PyObjC_Assert(sizeof(superobject) == PySuper_Type.tp_basicsize, -1);

    super_slots[2].pfunc = (void*)(PySuper_Type.tp_doc);

    PyObject* tmp = PyType_FromSpecWithBases(&super_spec, (PyObject*)&PySuper_Type);
    if (tmp == NULL) { // LCOV_BR_EXCL_LINE
        return -1;     // LCOV_EXCL_LINE
    }
    PyObjCSuper_Type = tmp;
    if (PyModule_AddObject( // LCOV_BR_EXCL_LINE
            module, "super", PyObjCSuper_Type)
        < 0) {
        return -1; // LCOV_EXCL_LINE
    }
    Py_INCREF(PyObjCSuper_Type);
    return 0;
}

NS_ASSUME_NONNULL_END
