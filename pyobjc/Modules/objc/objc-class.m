/*
 * Implementation of the class PyObjCClass_Type, that is the class representing
 * Objective-C classes.
 *
 */
#include "pyobjc.h"
#include "objc_support.h"
#include <stddef.h>

PyDoc_STRVAR(class_doc,
"objc_class(name, bases, dict) -> a new Objective-C class\n"
"\n"
"objc_class is the meta-type for Objective-C classes. It should not be\n"
"necessary to manually create instances of this type, those are \n"
"created by subclassing and existing Objective-C class.\n"
"\n"
"The list of bases must start with an existing Objective-C class, and \n"
"cannot contain other Objective-C classes. The list may contain\n"
"informal_interface objects, those are used during the calculation of\n"
"method signatures and will not be visible in the list of base-classes\n"
"of the created class."
);

static int add_class_fields(Class objc_class, PyObject* dict);

/*
 * Due to the way dynamicly created PyTypeObject's are processed it is not 
 * possible to add new fields to a type struct. For now we store the additional
 * information in a seperate data-structure. 
 *
 * The struct class_info contains the additional information for a class object,
 * and class_to_objc stores a mapping from a class object to its additional
 * information.
 *
 * In Python 2.3 we can, and do, store the additional information directly in
 * the type struct.
 */

#if PY_VERSION_HEX < 0x020300A2 /* Python 2.2 and early 2.3 alpha's */

typedef struct {
	Class	  class;
	PyObject* sel_to_py;
	int	  method_magic;
	int	  dictoffset;
	PyObject* delmethod;
	int       hasPythonImpl;
} PyObjC_class_info;

static NSMapTable* 	class_to_objc = NULL;


/*
 * Fetch the additional information for a class. If the information is
 * not yet available add it to the dictionary.
 */
static inline PyObjC_class_info*
get_class_info(PyObject* class)
{	
	PyObject*          item;
	PyObjC_class_info* info;

	if (class_to_objc == NULL) {
		class_to_objc = NSCreateMapTable(ObjC_PointerKeyCallBacks,
			ObjC_PointerValueCallBacks, 500);
	}

	item = NSMapGet(class_to_objc, class);
	if (item != NULL) {
		return (PyObjC_class_info*)item;
	}

	info = PyMem_Malloc(sizeof(*item));
	if (info == NULL) {
		PyErr_NoMemory();
		return NULL;
	}

	info->class     = nil;
	info->sel_to_py = NULL;
	info->method_magic = 0;

	Py_INCREF(class); 
	NSMapInsert(class_to_objc, class, info);
	return info;
}

#else /* Python >= 2.3 */

/* NOTE: This requires a version that more recent that 2.3a2 */

#define get_class_info(tp) ((PyObjCClassObject*)(tp))
#define PyObjC_class_info PyObjCClassObject


#endif /* Python >= 2.3 */


/* 
 * We keep references to all class objects we have created. This is needed
 * to correctly handle subclassing and avoids creating two python classes that
 * represent the same objective-C object.
 */
static NSMapTable*	class_registry = NULL;


	
static int 
objc_class_register(Class objc_class, PyObject* py_class)
{
	if (class_registry == NULL) {
		class_registry = NSCreateMapTable(ObjC_PointerKeyCallBacks,
			ObjC_PointerValueCallBacks, 500);
	}

	if (NSMapGet(class_registry, objc_class)) {
		PyErr_BadInternalCall();
		return -1;
	}

	Py_INCREF(py_class); 
	NSMapInsert(class_registry, objc_class, py_class);

	return 0;
}

static int 
objc_class_unregister(Class objc_class)
{
	if (class_registry == NULL) return 0;

	NSMapRemove(class_registry, objc_class);
	return 0;
}

static PyObject*
objc_class_locate(Class objc_class)
{
	PyObject* result;

	if (class_registry == NULL) return NULL;
	if (objc_class == NULL) return NULL;

	result = NSMapGet(class_registry, objc_class);
	return result;
}






/*
 * Create a new objective-C class, as a subclass of 'type'. This is
 * PyObjCClass_Type.tp_new.
 *
 * Note: This function creates new _classes_
 *
 * TODO:
 * - Add support for Objective-C 'Protocol' instances in the list of bases
 */


static PyObject*
class_new(PyTypeObject* type, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "name", "bases", "dict", NULL };
	char* name;
	PyObject* bases;
	PyObject* dict;
	PyObject* res;
	PyObject* v;
	int       i;
	int       len;
	Class      objc_class = NULL;
	Class	   super_class = NULL;
	PyObjC_class_info* info;
	PyObject* protocols;
	PyObject* real_bases;
	PyObject* delmethod;
	IVAR var;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "sOO:__new__",
			keywords, &name, &bases, &dict)) {
		return NULL;
	}

	if (objc_lookUpClass(name) != NULL) {
		PyErr_SetString(ObjCExc_error, 
			"Class already exists in Objective-C runtime");
		return NULL;
	}

	if (!PyTuple_Check(bases)) {
		PyErr_SetString(PyExc_TypeError, "'bases' must be tuple");
		return NULL;
	}

	len  = PyTuple_Size(bases);
	if (len < 1) {
		PyErr_SetString(PyExc_TypeError, "'bases' must not be empty");
		return NULL;
	}

	v = PyTuple_GetItem(bases, 0);
	if (v == NULL) {
		return NULL;
	}

	if (!PyObjCClass_Check(v)) {
		PyErr_SetString(PyExc_TypeError, 
				"first base class must "
				"be objective-C based");
		return NULL;
	}
	super_class = PyObjCClass_GetClass(v);
	if (super_class) {
		PyObjCClass_CheckMethodList(v);
	}

	protocols = PyList_New(0);
	if (protocols == NULL) return NULL;
	real_bases = PyList_New(0);
	if (real_bases == NULL) {
		Py_DECREF(protocols);
		return NULL;
	}
	PyList_Append(real_bases, v);
	if (PyErr_Occurred()) {
		Py_DECREF(protocols);
		Py_DECREF(real_bases);
		return NULL;
	}
	
	for (i = 1; i < len; i++) {
		v = PyTuple_GetItem(bases, i);
		if (v == NULL) {
			return NULL;
		}
		if (PyObjCClass_Check(v)) {
			Py_DECREF(protocols);
			Py_DECREF(real_bases);
			PyErr_SetString(PyExc_TypeError, 
					"multiple objective-C bases");
			return NULL;
		} else if (PyObjCInformalProtocol_Check(v)) {
			PyList_Append(protocols, v);
		} else {
			PyList_Append(real_bases, v);
		}
	}

	v = PyList_AsTuple(real_bases);
	if (v == NULL) {
		Py_DECREF(protocols);
		Py_DECREF(real_bases);
		return NULL;
	}
	Py_DECREF(real_bases);
	real_bases = v;

	/* First generate the objective-C klass. This may change the
	 * class dict.
	 */
	objc_class = PyObjCClass_BuildClass(super_class, protocols, name, dict);
	if (objc_class == NULL) {
		Py_DECREF(protocols);
		Py_DECREF(real_bases);
		return NULL;
	}

	delmethod = PyDict_GetItemString(dict, "__del__");
	if (delmethod == NULL) {
		PyErr_Clear();
	} else {
		Py_INCREF(delmethod);
		if (PyDict_DelItemString(dict, "__del__") < 0) {
			PyObjCClass_UnbuildClass(objc_class);
			Py_DECREF(protocols);
			Py_DECREF(real_bases);
			return NULL;
		}
	}




	/* Add convenience methods like '__eq__'. Must do it before
	 * call to super-class implementation, because '__*' methods
	 * are treated specially there.
	 */
	if (ObjC_AddConvenienceMethods(objc_class, dict) < 0) {
		PyObjCClass_UnbuildClass(objc_class);
		Py_DECREF(protocols);
		Py_DECREF(real_bases);
		return NULL;
	}

	/* call super-class implementation */
	args = Py_BuildValue("(sOO)", name, real_bases, dict);
	res =  PyType_Type.tp_new(type, args, NULL);
	if (res == NULL) {
		Py_DECREF(args);
		Py_DECREF(real_bases);
		PyObjCClass_UnbuildClass(objc_class);
		return NULL;
	}
	Py_DECREF(args);
	Py_DECREF(real_bases);
	args = NULL;
	real_bases = NULL;

	/* Verify that the class conforms to all protocols it claims to 
	 * conform to.
	 */
	len = PyList_Size(protocols);
	for (i = 0; i < len; i++) {
		PyObject* p = PyList_GetItem(protocols, i);

		if (p == NULL) {
			PyErr_Clear();
			continue;
		}

		if (PyObjCInformalProtocol_Check(p)) {
			if (!PyObjCInformalProtocol_CheckClass(p, res)) {
				Py_DECREF(res);
				Py_DECREF(protocols);
				PyObjCClass_UnbuildClass(objc_class);
				return NULL;
			}
		}
	}
	
	Py_DECREF(protocols);
	protocols = NULL;

	if (objc_class_register(objc_class, res) < 0) {
		Py_DECREF(res);
		PyObjCClass_UnbuildClass(objc_class);
		return NULL;
	}

	info = get_class_info(res);
	if (info == NULL) {
		if (objc_class_unregister(objc_class) < 0) {
			/* Oops, cannot unregister */
			Py_FatalError(
				"PyObjC: Cannot unregister unbuild class");
		}
		Py_DECREF(res);
		PyObjCClass_UnbuildClass(objc_class);
		return NULL;
	}
	info->class = objc_class;
	info->sel_to_py = PyDict_New(); 
	info->method_magic = objc_methodlist_magic(objc_class);
	info->dictoffset = 0;
	info->delmethod = delmethod;
	info->hasPythonImpl = 1;


	// Initialize to parent version, not: this should not be necessary!
	info->dictoffset = PyObjCClass_DictOffset(PyTuple_GET_ITEM(bases, 0));

	PyObjCClass_SetClass(objc_class, res);

	var = class_getInstanceVariable(objc_class, "__dict__");
	if (var != NULL) {
		info->dictoffset = var->ivar_offset;
	}

	Py_INCREF(res);
	return res;
}


static PyObject*
class_repr(PyObject* obj)
{
	char buffer[256];
	Class cls;

	cls = PyObjCClass_GetClass(obj);

	if (cls) {
		snprintf(buffer, sizeof(buffer), 
			"<objective-c class %s at %p>", 
			cls->name, cls);
	} else {
		snprintf(buffer, sizeof(buffer),
			"%s", "<objective-c class NIL>");
	}

	return PyString_FromString(buffer);
}


static void
class_dealloc(PyObject* cls)
{
	char buf[1024];

	snprintf(buf, sizeof(buf), "Deallocating objective-C class %s", ((PyTypeObject*)cls)->tp_name);

	/* This should never happen */
	Py_FatalError(buf);
}

void 
PyObjCClass_CheckMethodList(PyObject* cls)
{
	PyObjC_class_info* info;
	int		   magic;

	info = get_class_info(cls);

	if (info->class == NULL) return;

	while (info->class != 0) {

		if (info->method_magic != 
				(magic = objc_methodlist_magic(info->class))) {

			int r;

			r = add_class_fields(
				info->class,
				((PyTypeObject*)cls)->tp_dict);
			if (r < 0) {
				PyErr_SetString(PyExc_RuntimeError,
					"Cannot rescan method table");
				return;
			}
			r =  ObjC_UpdateConvenienceMethods(cls);
			if (r < 0) {
				PyErr_SetString(PyExc_RuntimeError,
					"Cannot rescan method table");
				return;
			}
			info->method_magic = magic;
			if (info->sel_to_py) {
				Py_DECREF(info->sel_to_py);
				info->sel_to_py = PyDict_New();
			}
		}

		if (info->class->super_class == NULL) break;
		cls = PyObjCClass_New(info->class->super_class);
		info = get_class_info(cls);

	}
}

static PyObject*
class_getattro(PyObject* self, PyObject* name)
{
	PyObject* result;

	PyObjCClass_CheckMethodList(self);
	
	result = PyType_Type.tp_getattro(self, name);
	if (result != NULL) {
		return result;
	}

	/* Try to find the method anyway */
	PyErr_Clear();
	NS_DURING
		result = ObjCSelector_FindNative(self, PyString_AsString(name));
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		result = NULL;
	NS_ENDHANDLER

	if (result != 0) {
		int res = PyDict_SetItem(((PyTypeObject*)self)->tp_dict, name, result);
		ObjCNativeSelector* x = (ObjCNativeSelector*)result;

		if (x->sel_flags & ObjCSelector_kCLASS_METHOD) {
			x->sel_self = self;
			Py_INCREF(x->sel_self);
		}
		if (res < 0) {
			if (ObjC_VerboseLevel) {
				PySys_WriteStderr(
					"PyObjC[class_getattro]: Cannot "
					"add new method to dict:\n");
				PyErr_Print();
			}
			PyErr_Clear();
		}
	}
	return result;
}

static int
class_compare(PyObject* self, PyObject* other)
{
	Class self_class;
	Class other_class;
	int   v;

	if (!PyObjCClass_Check(other)) {
		PyErr_SetString(PyExc_NotImplementedError, "Cmp with other");
		return -1;
	}

	/* This is as arbitrary as the default tp_compare, but nicer for
	 * the user
	 */
	self_class = PyObjCClass_GetClass(self);
	other_class = PyObjCClass_GetClass(other);

	if (self_class == other_class) return 0;
	if (!self_class) return -1;
	if (!other_class) return 1;

	v = strcmp(
		self_class->name, 
		other_class->name);

	/* Python requires -1, 0 or 1, but strcmp on MacOS X returns
	 * 'negative', 0 or 'positive'
	 */
	if (v < 0) return -1;
	if (v == 0) return 0;
	return 1;
}

static long
class_hash(PyObject* self)
{
	return (long)self;
}

PyDoc_STRVAR(cls_get_classMethods_doc,
"The attributes of this field are the class methods of this object. This can\n"
"be used to force access to a class method."
);
static PyObject*
cls_get_classMethods(PyObject* self, void* closure)
{
	return ObjCMethodAccessor_New(self, 1);
}

PyDoc_STRVAR(cls_get_instanceMethods_doc,
"The attributes of this field are the instance methods of this object. This \n"
"can be used to force access to an instance method."
);
static PyObject*
cls_get_instanceMethods(PyObject* self, void* closure)
{
	return ObjCMethodAccessor_New(self, 0);
}

static PyObject*
cls_get__name__(PyObject* self, void* closure)
{
	Class cls = PyObjCClass_GetClass(self);
	if (cls == NULL) {
		return NULL;
	} else {
		return PyString_FromString(cls->name);
	}
}

static PyGetSetDef cls_getset[] = {
        {
                "pyobjc_classMethods",
                (getter)cls_get_classMethods,
                NULL,
                cls_get_classMethods_doc,
                0
        },
        {
                "pyobjc_instanceMethods",
                (getter)cls_get_instanceMethods,
                NULL,
                cls_get_instanceMethods_doc,
                0
        },
	{
		/* Access __name__ through a property: Objective-C name 
		 * might change due to posing.
		 */
		"__name__",
		(getter)cls_get__name__,
		NULL,
		NULL,
		0
	},
        { 0, 0, 0, 0, 0 }
};


PyTypeObject PyObjCClass_Type = {
	PyObject_HEAD_INIT(&PyType_Type)
	0,					/* ob_size */
	"objc_class",				/* tp_name */
#if PY_VERSION_HEX >= 0x020300A2
	sizeof (PyObjCClassObject),		/* tp_basicsize */
#else /* Python 2.2 */
	0,					/* tp_basicsize */
#endif /* Python 2.2 */
	0,					/* tp_itemsize */
	/* methods */
	class_dealloc,	 			/* tp_dealloc */
	0,					/* tp_print */
	0,					/* tp_getattr */
	0,					/* tp_setattr */
	class_compare,				/* tp_compare */
	class_repr,				/* tp_repr */
	0,					/* tp_as_number */
	0,					/* tp_as_sequence */
	0,		       			/* tp_as_mapping */
	class_hash,				/* tp_hash */
	0,					/* tp_call */
	0,					/* tp_str */
	class_getattro,				/* tp_getattro */
	0,					/* tp_setattro */
	0,					/* tp_as_buffer */
	Py_TPFLAGS_DEFAULT,			/* tp_flags */
 	class_doc,				/* tp_doc */
 	0,					/* tp_traverse */
 	0,					/* tp_clear */
	0,					/* tp_richcompare */
	0,					/* tp_weaklistoffset */
	0,					/* tp_iter */
	0,					/* tp_iternext */
	0,					/* tp_methods */
	0,					/* tp_members */
	cls_getset,				/* tp_getset */
	&PyType_Type,				/* tp_base */
	0,					/* tp_dict */
	0,					/* tp_descr_get */
	0,					/* tp_descr_set */
	0,					/* tp_dictoffset */
	0,					/* tp_init */
	0,					/* tp_alloc */
	class_new,				/* tp_new */
	0,		        		/* tp_free */
};


/* FIXME: objc_support.[hm] also has version of this function! */
char*
PyObjC_SELToPythonName(SEL sel, char* buf, size_t buflen)
{
	size_t res = snprintf(buf, buflen, SELNAME(sel));
	char* cur;

	if (res != strlen(SELNAME(sel))) {
		return NULL;
	}
	cur = strchr(buf, ':');
	while (cur) {
		*cur = '_';
		cur = strchr(cur, ':');
	}
	return buf;
}

/*
 * Add methods and descriptors for the instance variables to the dict.
 *
 * Add only the items for this specific class, the items from the super-class
 * are found through inheritance.
 *
 * We add instance methods, class methods and instance variables in that 
 * order, methods always override variables (most classes provide accessor
 * methods with the same name as the variables and this order is the least
 * surprising)
 */
static int
add_class_fields(Class objc_class, PyObject* dict)
{
	Class     cls;
	METHOD    meth;
	struct objc_method_list* mlist;
	void*     iterator;
	PyObject* descr;
	char      selbuf[1024];

	if (objc_class == NULL) return 0;

	/*
	 * First add instance methods
	 */

	iterator = 0;
	mlist = class_nextMethodList(objc_class, &iterator);
	while (mlist != NULL) {
		int i;
		METHOD meth;

		for (i = 0; i < mlist->method_count; i++) {
			char* name;

			meth = mlist->method_list + i;

			name = (char*)PyObjC_SELToPythonName(
						meth->method_name, 
						selbuf, 
						sizeof(selbuf));

			/* FIXME: because we scan again later on, we should
			 * take care to avoid replacing Python methods with
			 * a custom selector ('selector' argument to function
			 * objc.selector)
			 *
			 * We're save for now because none of the example code 
			 * uses this feature.
			if (PyDict_GetItemString(dict, name) != NULL) {
				continue;
			} 
			 */

			descr = ObjCSelector_NewNative(
					objc_class,
					meth->method_name,
					meth->method_types,
					0);

			if (PyDict_SetItemString(
					dict, 
					name,
					descr) != 0) {

				Py_DECREF(descr); 
				return -1;
			}
			Py_DECREF(descr); 
		}
		mlist = class_nextMethodList(objc_class, &iterator);
	}



	/* 
	 * Then add class methods
	 */

	cls = GETISA(objc_class);
	iterator = 0;
	mlist = class_nextMethodList(cls, &iterator);
	while (mlist != NULL) {
		int i;
		for (i = 0; i < mlist->method_count; i++) {
			meth = mlist->method_list + i;

			PyObjC_SELToPythonName(
				meth->method_name, 
				selbuf, 
				sizeof(selbuf));

			if ((descr = PyDict_GetItemString(dict, selbuf))) {
				if (!ObjCSelector_Check(descr)) {
					continue;
				} else if (!(((ObjCSelector*)descr)->sel_flags & ObjCSelector_kCLASS_METHOD)) {
					continue;
				}
			}

			descr = ObjCSelector_NewNative(
				objc_class,
				meth->method_name,
				meth->method_types,
				1);

			if (PyDict_SetItemString(dict, 
					selbuf,
					descr) != 0) {
				Py_DECREF(descr);
				return -1;
			}
			Py_DECREF(descr);
		}
		mlist = class_nextMethodList(cls, &iterator);
	}

#if PyOBJC_ACCESS_INSTANCE_VARIABLES
	/*
	 * Finally add instance variables.
	 *
	 * This code is currently disabled to match the Objective-C
	 * semantics.
	 */
	if (objc_class->ivars) {
		for (i = 0; i < objc_class->ivars->ivar_count; i++) {
			var = objc_class->ivars->ivar_list + i;

			if (PyDict_GetItemString(dict, var->ivar_name)) {
				continue;
			}

			descr = PyObjCInstanceVariable_New(var->ivar_name);
			if (descr == NULL) {
				return -1;
			}
			if (PyDict_SetItemString(dict, 
					var->ivar_name, descr) != 0) {
				Py_DECREF(descr);
				return -1;
			}
			Py_DECREF(descr);
		}
	}
#endif

	return  0;
}

/*
 * Create a new objective-C class  proxy.
 *
 * NOTES:
 * - proxies are subclasses of PyObjCClass_Type
 * - subclass relations in objetive-C are retained in python
 * - this looks a lot like PyObjCClass_Type.tp_new, but it is _not_ the
 *   same!
 */
PyObject* 
PyObjCClass_New(Class objc_class)
{
	PyObject* args;
	PyObject* dict;
	PyObject* result;
	PyObject* bases;
	PyObjC_class_info* info;
	IVAR var;

	result = objc_class_locate(objc_class);
	if (result != NULL) {
		Py_INCREF(result);
		return result;
	}
	PyErr_Clear();

	dict = PyDict_New();
	PyDict_SetItemString(dict, "__slots__", PyTuple_New(0));

	bases = PyTuple_New(1);

	if (objc_class->super_class == NULL) {
		PyTuple_SetItem(bases, 0, (PyObject*)&PyObjCObject_Type);
		Py_INCREF(((PyObject*)&PyObjCObject_Type));
	} else {
		PyTuple_SetItem(bases, 0, 
			PyObjCClass_New(objc_class->super_class));
	} 
	args = PyTuple_New(3);
	PyTuple_SetItem(args, 0, PyString_FromString(objc_class->name));
	PyTuple_SetItem(args, 1, bases);
	PyTuple_SetItem(args, 2, dict);

	result = PyType_Type.tp_new(&PyObjCClass_Type, args, NULL);
	if (result == NULL) {
		Py_DECREF(args);
		return NULL;
	}
	Py_DECREF(args); 

	info = get_class_info(result);
	if (info == NULL) {
		Py_DECREF(result);
		PyErr_SetString(PyExc_RuntimeError,
			"PyObjC: Cannot build class information");
		return NULL;
	}

	info->class = objc_class;
	info->sel_to_py = PyDict_New(); 
	info->method_magic = 0;
	info->dictoffset = 0;
	info->delmethod = 0;
	info->hasPythonImpl = 0;

	var = class_getInstanceVariable(objc_class, "__dict__");
	if (var != NULL) {
		info->dictoffset = var->ivar_offset;
	}

	if (PyObject_SetAttrString(result, 
			"__module__", PyObjCClass_DefaultModule) < 0) {
		PyErr_Clear();
	}


	objc_class_register(objc_class, result);

	return result;
}


Class 
PyObjCClass_GetClass(PyObject* cls)
{
	PyObjC_class_info* info;

	if (!PyObjCClass_Check(cls)) {
		ObjCErr_Set(ObjCExc_internal_error,
			"PyObjCClass_GetClass called for non-class");
		return nil;
	}
	
	info = get_class_info(cls);
	return info->class;
}

PyObject* 
PyObjCClass_FindSelector(PyObject* cls, SEL selector)
{
	PyObjC_class_info* info;
	PyObject*          result;
	PyObject*          attributes;
	PyObject*          key;
	PyObject*          v;
	int                i;
	int                len;

	if (!PyObjCClass_Check(cls)) {
		ObjCErr_Set(ObjCExc_internal_error,
			"PyObjCClass_GetClass called for non-class");
		return NULL;
	}

	PyObjCClass_CheckMethodList(cls);
	
	info = get_class_info(cls);
	if (info->sel_to_py == NULL) {
		info->sel_to_py = PyDict_New();
		if (info->sel_to_py == NULL) {
			return NULL;
		}
	}

	/* First check the cache */

	result = PyDict_GetItemString(info->sel_to_py, 
				(char*)SELNAME(selector));	
	if (result != NULL) {
		if (result == Py_None) {
			/* negative cache entry */
			ObjCErr_Set(PyExc_AttributeError,
				"No selector %s (cached)",
				SELNAME(selector));
			return NULL;
		}
		Py_INCREF(result);
		return result;
	}

	/* Not in the cache, walk the attribute list */

	attributes = PyObject_Dir(cls);
	if (attributes == NULL) {
		return NULL;
	}

	len = PySequence_Size(attributes);
	for (i = 0; i < len; i++) {
		key = PySequence_GetItem(attributes, i);
		if (key == NULL) {
			return NULL;
		}

#ifdef  PyObjC_COMPILING_ON_MACOSX_10_1
	/* On MacOSX we get hard crashes for the method signature of this
         * method. This seems to be a problem with the Objective-C runtime 
  	 * and/or Cocoa because a simple ObjC program gives the same error.
 	 * 
 	 * As this method should never be forwarded to Python anyway we can
	 * safely ignore it here.
  	 */
		if (PyString_Check(key) && 
				strcmp(PyString_AS_STRING(key), "__pyobjc_PythonObject__") == 0) {
			Py_DECREF(key);
			continue;

		}
#endif

		v = PyObject_GetAttr(cls, key);
		Py_DECREF(key);
		if (v == NULL) {
			PyErr_Clear();
			continue;
		}

		if (ObjCSelector_Check(v)) {
			if (((ObjCSelector*)v)->sel_selector == selector) {
				Py_DECREF(attributes);
				PyDict_SetItemString(info->sel_to_py,
					(char*)SELNAME(selector), v);
				return v;
			}
		} 
		Py_DECREF(v);
	}

	Py_DECREF(attributes);

	ObjCErr_Set(PyExc_AttributeError,
		"No selector %s", SELNAME(selector));
	PyDict_SetItemString(info->sel_to_py, 
			(char*)SELNAME(selector), Py_None);
	return NULL;
}

int 
PyObjCClass_IsSubClass(Class child, Class parent)
{
	if (parent == nil) return 1;

	while (child != nil) {
		if (child == parent) return 1;
		child = child->super_class;	
	}
	return 0;
}

int
PyObjCClass_DictOffset(PyObject* cls)
{
	PyObjC_class_info* info;
	info = get_class_info(cls);
	return info->dictoffset;
}

PyObject*
PyObjCClass_GetDelMethod(PyObject* cls)
{
	PyObjC_class_info* info;
	info = get_class_info(cls);
	Py_XINCREF(info->delmethod);
	return info->delmethod;
}

void
PyObjCClass_SetDelMethod(PyObject* cls, PyObject* m)
{
	PyObjC_class_info* info;
	info = get_class_info(cls);
	Py_XINCREF(m);
	Py_XDECREF(info->delmethod);
	info->delmethod = m;
}

int
PyObjCClass_HasPythonImplementation(PyObject* cls)
{
	PyObjC_class_info* info;
	info = get_class_info(cls);
	return info->hasPythonImpl;
}
