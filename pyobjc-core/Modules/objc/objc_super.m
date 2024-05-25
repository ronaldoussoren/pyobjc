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

    PyTypeObject* _Nullable type;
    PyObject* _Nullable obj;
    PyTypeObject* _Nullable obj_type;
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
                dict = PyObjC_get_tp_dict(Py_TYPE(tmp));

            } else if (PyType_Check(tmp)) {
                dict = PyObjC_get_tp_dict((PyTypeObject*)tmp);

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

static PyType_Slot super_slots[] = {
    {.slot = Py_tp_getattro, .pfunc = (void*)&super_getattro},
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

    super_slots[1].pfunc = (void*)(PySuper_Type.tp_doc);

#if PY_VERSION_HEX < 0x030a0000
    PyObject* bases = PyTuple_New(1);
    if (bases == NULL) {
        return -1;
    }
    PyTuple_SET_ITEM(bases, 0, (PyObject*)&PySuper_Type);
    Py_INCREF(&PySuper_Type);
#endif

    PyObject* tmp = PyType_FromSpecWithBases(&super_spec,
#if PY_VERSION_HEX >= 0x030a0000
                                             (PyObject*)&PySuper_Type);
#else
                                             bases);
    Py_CLEAR(bases);
#endif
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
