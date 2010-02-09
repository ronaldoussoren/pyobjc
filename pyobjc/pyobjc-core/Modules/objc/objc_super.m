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
 *
 * FIXME: This will require further work when I remove
 * "PyObjCClass_CheckMethodList".
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



	if (!skip) {
		/* We want __class__ to return the class of the super object
		   (i.e. super, or a subclass), not the class of su->obj. */
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

	if (!skip) {
		PyObject *mro, *res, *tmp, *dict;
		PyTypeObject *starttype;
		descrgetfunc f;
		Py_ssize_t i, n;

		starttype = su->obj_type;
		mro = starttype->tp_mro;

		if (mro == NULL)
			n = 0;
		else {
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
				
			} else if (PyType_Check(tmp))
				dict = ((PyTypeObject *)tmp)->tp_dict;
#if PY_MAJOR_VERSION == 2
			else if (PyClass_Check(tmp))
				dict = ((PyClassObject *)tmp)->cl_dict;
#endif
			else
				continue;

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
		}
	}
	return PyObject_GenericGetAttr(self, name);
}

PyTypeObject PyObjCSuper_Type = {
	PyVarObject_HEAD_INIT(&PyType_Type, 0)
	"objc.super",
	sizeof(superobject),
	0,
	/* methods */
	0,		 			/* tp_dealloc */
	0,					/* tp_print */
	0,					/* tp_getattr */
	0,					/* tp_setattr */
	0,					/* tp_compare */
	0,					/* tp_repr */
	0,					/* tp_as_number */
	0,					/* tp_as_sequence */
	0,		       			/* tp_as_mapping */
	0,					/* tp_hash */
	0,					/* tp_call */
	0,					/* tp_str */
	super_getattro,				/* tp_getattro */
	0,					/* tp_setattro */
	0,					/* tp_as_buffer */
	Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HAVE_GC |
		Py_TPFLAGS_BASETYPE,		/* tp_flags */
 	0,					/* tp_doc */
 	0,					/* tp_traverse */
 	0,					/* tp_clear */
	0,					/* tp_richcompare */
	0,					/* tp_weaklistoffset */
	0,					/* tp_iter */
	0,					/* tp_iternext */
	0,					/* tp_methods */
	0,					/* tp_members */
	0,					/* tp_getset */
	0,					/* tp_base */
	0,					/* tp_dict */
	0,					/* tp_descr_get */
	0,					/* tp_descr_set */
	0,					/* tp_dictoffset */
	0,					/* tp_init */
	PyType_GenericAlloc,			/* tp_alloc */
	PyType_GenericNew,			/* tp_new */
	PyObject_GC_Del,        		/* tp_free */
	0,					/* tp_is_gc */
	0,					/* tp_bases */
	0,					/* tp_mro */
	0,					/* tp_cache */
	0,					/* tp_mro */
	0,					/* tp_weaklist */
	0					/* tp_del */
#if PY_VERSION_HEX >= 0x02060000
	, 0                                     /* tp_version_tag */
#endif

};
