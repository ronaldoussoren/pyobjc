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


/*
 * NOTE: This is a minor tweak of Python 2.5's super_getattro and is a rather
 * crude hack.
 *
 * NOTE: updated for 3.2, and 2.7
 */
typedef struct {
    PyObject_HEAD

    PyTypeObject *type;
    PyObject *obj;
    PyTypeObject *obj_type;
} superobject;

static PyObject *
super_getattro(PyObject *self, PyObject *name)
{
    superobject *su = (superobject *)self;
    int skip = su->obj_type == NULL;
    SEL sel;

    if (!skip) {
        /* We want __class__ to return the class of the super object
         *  (i.e. super, or a subclass), not the class of su->obj.
         */
        if (PyUnicode_Check(name)) {
            skip = (PyUnicode_GET_SIZE(name) && PyObjC_is_ascii_string(name, "__class__"));
#if PY_MAJOR_VERSION == 2
        } else if (PyString_Check(name)) {
            skip = (
                PyString_GET_SIZE(name) == 9 &&
                strcmp(PyString_AS_STRING(name), "__class__") == 0);
#endif
        } else {
            skip = 0;
        }

    }

    if (PyUnicode_Check(name)) {
#ifdef PyObjC_FAST_UNICODE_ASCII
        const char* b = PyObjC_Unicode_Fast_Bytes(name);
        if (name == NULL) {
            return NULL;
        }
        sel = PyObjCSelector_DefaultSelector(b);

#else /* !PyObjC_FAST_UNICODE_ASCII */

        PyObject* bytes = PyUnicode_AsEncodedString(name, NULL, NULL);
        if (bytes == NULL) {
            return NULL;
        }
        sel = PyObjCSelector_DefaultSelector(PyBytes_AsString(bytes));
#endif /* !PyObjC_FAST_UNICODE_ASCII */

#if PY_MAJOR_VERSION == 2
    } else if (PyBytes_Check(name)) {
        sel = PyObjCSelector_DefaultSelector(PyBytes_AsString(name));
#endif

    } else if (!skip) {
        PyErr_SetString(PyExc_TypeError, "attribute name is not a string");
        return NULL;
    }

    if (!skip) {
        PyObject *mro, *res, *tmp, *dict;
        PyTypeObject *starttype;
        descrgetfunc f;
        Py_ssize_t i, n;

        starttype = su->obj_type;
        mro = starttype->tp_mro;

        if (mro == NULL) {
            n = 0;
        } else {
            assert(PyTuple_Check(mro));
            n = PyTuple_GET_SIZE(mro);
        }

        for (i = 0; i < n; i++) {
            if ((PyObject *)(su->type) == PyTuple_GET_ITEM(mro, i))
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
                PyObjCClass_CheckMethodList(tmp, NO);
            }

            if (PyObjCClass_Check(tmp) && PyObjCClass_Check(su->obj))  {
                dict = Py_TYPE(tmp)->tp_dict;

            } else if (PyType_Check(tmp)) {
                dict = ((PyTypeObject *)tmp)->tp_dict;
#if PY_MAJOR_VERSION == 2
            } else if (PyClass_Check(tmp)) {
                dict = ((PyClassObject *)tmp)->cl_dict;
#endif
            } else {
                continue;
            }

            res = PyDict_GetItem(dict, name);
            if (res != NULL) {
                Py_INCREF(res);
                f = Py_TYPE(res)->tp_descr_get;
                if (f != NULL) {
                    tmp = f(res,
                        /* Only pass 'obj' param if
                           this is instance-mode super
                           (See SF ID #743627)
                        */
                        (su->obj == (PyObject *)
                                su->obj_type
                            ? (PyObject *)NULL
                            : su->obj),
                        (PyObject *)starttype);
                    Py_DECREF(res);
                    res = tmp;
                }
                return res;
            }


            if (PyObjCClass_Check(tmp)) {
                if (!PyObjCClass_Check(su->obj)) {
                    res = PyObjCClass_TryResolveSelector(tmp, name, sel);
                } else {
                    res = PyObjCMetaClass_TryResolveSelector((PyObject*)Py_TYPE(tmp), name, sel);
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
                            (su->obj == (PyObject *)
                                    su->obj_type
                                ? (PyObject *)NULL
                                : su->obj),
                            (PyObject *)starttype);
                        Py_DECREF(res);
                        res = tmp;
                    }

                    return res;

                } else if (PyErr_Occurred()) {
                    return NULL;
                }
            }
        }
    }
    return PyObject_GenericGetAttr(self, name);
}

PyTypeObject PyObjCSuper_Type = {
    PyVarObject_HEAD_INIT(&PyType_Type, 0)
    .tp_name        = "objc.super",
    .tp_basicsize   = sizeof(superobject),
    .tp_itemsize    = 0,
    .tp_getattro    = super_getattro,
    .tp_flags       = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HAVE_GC,
    .tp_alloc       = PyType_GenericAlloc,
    .tp_new         = PyType_GenericNew,
    .tp_free        = PyObject_GC_Del,
};
