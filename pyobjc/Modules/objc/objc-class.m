/*
 * Implementation of the class ObjCClass_Type, that is the class representing
 * Objective-C classes.
 *
 */
#include "pyobjc.h"
#include <stddef.h>
//#include <Foundation/Foundation.h>

/*
 * PyType_Type is has variable-sized information and I (ROU) haven't found a
 * way yet to stuff additional information in there. 
 *
 * XXX: the __slots__ mechanism could (and should) be used, implemention is 
 * left as an exercise for the reader.
 *
 * Because classes must live forever anyway (objective-C runtime cannot drop 
 * classes) storing the additinal information seperately is acceptable.
 *
 * The struct class_info contains the additional information for a class object,
 * and class_to_objc stores a mapping from a class object to its additional
 * information.
 */
struct class_info {
	Class	  class;
	PyObject* sel_to_py;
	int	  rescan_done;
};

static PyObject* 	class_to_objc = NULL;


/*
 * Fetch the additional information for a class. If the information is
 * not yet available add it to the dictionary.
 */
static struct class_info*
get_class_info(PyObject* class)
{	
	PyObject*          item;
	struct class_info* info;

	if (class_to_objc == NULL) {
		class_to_objc = PyDict_New();
		if (class_to_objc == NULL) return NULL;
	}

	item = PyDict_GetItem(class_to_objc, class);
	if (item != NULL) {
		return (struct class_info*)PyCObject_AsVoidPtr(item);
	}

	PyErr_Clear();
	info = PyMem_Malloc(sizeof(*item));

	if (info == NULL) {
		PyErr_NoMemory();
		return NULL;
	}

	info->class     = nil;
	info->sel_to_py = NULL;
	info->rescan_done = 0;
	item = PyCObject_FromVoidPtr(info, NULL);
	if (item == NULL) {
		PyMem_Free(info);
		PyErr_SetString(PyExc_MemoryError, 
			"allocating class_info");
		return NULL;
	}

	if (PyDict_SetItem(class_to_objc, class, item) < 0) {
		Py_DECREF(item);
		PyMem_Free(info);
		return NULL;
	}
	Py_INCREF(class);
	return info;
}


/* 
 * We keep references to all class objects we have created. This is needed
 * to correctly handle subclassing and avoids creating two python classes that
 * represent the same objective-C object.
 */
static PyObject*	class_registry = NULL;


static int 
objc_class_register(Class objc_class, PyObject* py_class)
{
	int res;
	
	if (class_registry == NULL) {
		class_registry = PyDict_New();
		if (class_registry == NULL) {
			return -1;
		}
	}

	if (PyDict_GetItemString(class_registry, (char*)objc_class->name)) {
		abort();
	}

	res = PyDict_SetItemString(class_registry, 
		(char*)objc_class->name, py_class);
	if (res == 0) {
		Py_INCREF(py_class);
	} else {
		abort();
	}
	return res;
}

static PyObject*
objc_class_locate(Class objc_class)
{
	PyObject* result;

	if (class_registry == NULL) return NULL;

	result = PyDict_GetItemString(class_registry, 
		(char*)objc_class->name);
	return result;
}






/*
 * convert a python class-name to an objective-C name.
 *
 * XXX: This function may not be necessary, I've never seen it called with
 *      names that contain dots.
 */
static char*
normalize_classname(char* classname, char* buf, size_t buflen)
{
	char* cur;

	snprintf(buf, buflen, "%s", classname);
	cur = strchr(buf, '.');
	while (cur != NULL) {
		*cur = '_';
		cur = strchr(cur, '.');
	}
	return buf;
}
	
static int
class_traverse(PyObject* ob, visitproc proc, void* opaque)
{
	int res = 0;

	/* If we are incomplete, don't traverse the type. */
	/* This seems to solve a problem on Python 2.2.0 */
	if (ObjCClass_GetClass(ob) != nil) {
		res =  ((PyTypeObject*)ob)->tp_base->tp_traverse(ob, proc, opaque);
	}

	return res;
}

/*
 * Create a new objective-C class, as a subclass of 'type'. This is
 * ObjCClass_Type.tp_new.
 *
 * Note: This function creates new _classes_
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
	char normalized_name[1024];
	Class      objc_class = NULL;
	Class	   super_class = NULL;
	struct class_info* info;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "sOO:meta_new",
			keywords, &name, &bases, &dict)) {
		return NULL;
	}

	name = normalize_classname(name, 
		normalized_name, sizeof(normalized_name));

	if (objc_lookUpClass(name) != NULL) {
		PyErr_SetString(objc_error, 
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

	if (!ObjCClass_Check(v)) {
		PyErr_SetString(PyExc_TypeError, 
				"first base class must "
				"be objective-C based");
		return NULL;
	}
	super_class = ObjCClass_GetClass(v);
	
	for (i = 1; i < len; i++) {
		v = PyTuple_GetItem(bases, 0);
		if (v == NULL) {
			return NULL;
		}
		if (ObjCClass_Check(v)) {
			PyErr_SetString(PyExc_TypeError, 
					"multiple objective-C bases");
			return NULL;
		}
	}

	/* First generate the objective-C klass. This may change the
	 * class dict.
	 */
	objc_class = ObjCClass_BuildClass(super_class, name, dict);
	if (objc_class == NULL) {
		if (!PyErr_Occurred()) {
			abort();
		}
		return NULL;
	}

	/* Add convenience methods like '__eq__'. Must do it before
	 * call to super-class implementation, because '__*' methods
	 * are treated specially there.
	 */
	if (ObjC_AddConvenienceMethods(objc_class, dict) < 0) {
		ObjCClass_UnbuildClass(objc_class);
		return NULL;
	}

	/* call super-class implementation */
	res =  PyType_Type.tp_new(type, args, kwds);
	if (res == NULL) {
		ObjCClass_UnbuildClass(objc_class);
		return NULL;
	}

	/* FIXME: handle errors in next 4 lines */
	objc_class_register(objc_class, res);
	info = get_class_info(res);
	info->class = objc_class;
	info->sel_to_py = NULL; /* FIX ME */
	info->rescan_done = 0;

	ObjCClass_SetClass(objc_class, res);

	Py_INCREF(res);
	return res;
}


static PyObject*
class_repr(PyObject* obj)
{
	char buffer[256];
	Class cls;

	cls = ObjCClass_GetClass(obj);

	if (cls) {
		snprintf(buffer, sizeof(buffer), 
			"<objective-c class %s at %p>", 
			cls->name, obj);
	} else {
		snprintf(buffer, sizeof(buffer),
			"%s", "<objective-c class NIL>");
	}

	return PyString_FromString(buffer);
}

static void
class_dealloc(PyObject* cls)
{
	/* This should never happen */
	PySys_WriteStderr("Deallocating objective-C class %s\n", 
		((PyTypeObject*)cls)->tp_name);
	abort();
}

static PyObject*
class_getattro(PyObject* self, PyObject* name)
{
	PyObject* result = PyType_Type.tp_getattro(self, name);

	if (result != NULL) {
		return result;
	}

	/* Try to find the method anyway */
	PyErr_Clear();
	result = ObjCSelector_FindNative(self, PyString_AsString(name));
	if (result != 0) {
		int res = PyDict_SetItem(self, name, result);
		ObjCNativeSelector* x = (ObjCNativeSelector*)result;

		if (x->sel_class_method) {
			x->sel_self = self;
			Py_INCREF(x->sel_self);
		}
		if (res >= 0) {
			Py_INCREF(result);
		} else {
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

	if (!ObjCClass_Check(other)) {
		PyErr_SetString(PyExc_NotImplementedError, "Cmp with other");
		return -1;
	}

	/* This is as arbitrary as the default tp_compare, but nicer for
	 * the user
	 */
	self_class = ObjCClass_GetClass(self);
	other_class = ObjCClass_GetClass(other);

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

PyTypeObject ObjCClass_Type = {
	PyObject_HEAD_INIT(&PyType_Type)
	0,					/* ob_size */
	"objc_class",				/* tp_name */
	0,					/* tp_basicsize */
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
 	0,					/* tp_doc */
 	class_traverse,				/* tp_traverse */
 	0,					/* tp_clear */
	0,					/* tp_richcompare */
	0,					/* tp_weaklistoffset */
	0,					/* tp_iter */
	0,					/* tp_iternext */
	0,					/* tp_methods */
	0,					/* tp_members */
	0,					/* tp_getset */
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
static char*
pythonify_selector(SEL sel, char* buf, size_t buflen)
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
	Method    meth;
	struct objc_method_list* mlist;
	void*     iterator;
	PyObject* descr;
	char      selbuf[1024];

	/*
	 * First add instance methods
	 */

	iterator = 0;
	mlist = class_nextMethodList(objc_class, &iterator);
	while (mlist != NULL) {
		int i;
		Method meth;

		for (i = 0; i < mlist->method_count; i++) {
			char* name;

			meth = mlist->method_list + i;

			name = (char*)pythonify_selector(
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
			 */
			if (PyDict_GetItemString(dict, name) != NULL) {
				//printf("Skipped %s in wrapper for %s\n", SELNAME(meth->method_name), objc_class->name);
				continue;
			} 
			//printf("Found %s in wrapper for %s\n", SELNAME(meth->method_name), objc_class->name);

			descr = ObjCSelector_NewNative(
					objc_class,
					meth->method_name,
					meth->method_types,
					0);

			if (PyDict_SetItemString(
					dict, 
					name,
					descr) != 0) {

				return -1;
			}
		}
		mlist = class_nextMethodList(objc_class, &iterator);
	}



	/* 
	 * Then add class methods
	 */

	cls = objc_class->isa;
	iterator = 0;
	mlist = class_nextMethodList(cls, &iterator);
	while (mlist != NULL) {
		int i;
		for (i = 0; i < mlist->method_count; i++) {
			meth = mlist->method_list + i;

			if (PyDict_GetItemString(dict, 
					(char*)SELNAME(meth->method_name))) {
				continue;
			}

			descr = ObjCSelector_NewNative(
				objc_class,
				meth->method_name,
				meth->method_types,
				1);

			if (PyDict_SetItemString(dict, 
					pythonify_selector(
						meth->method_name, 
						selbuf, 
						sizeof(selbuf)), 
					descr) != 0) {
				return -1;
			}
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

			descr = ObjCInstanceVar_New(var->ivar_name);
			if (descr == NULL) {
				return -1;
			}
			if (PyDict_SetItemString(dict, 
					var->ivar_name, descr) != 0) {
				return -1;
			}
		}
	}
#endif

	return  0;
}

/*
 * Create a new objective-C class  proxy.
 *
 * NOTES:
 * - proxies are subclasses of ObjCClass_Type
 * - subclass relations in objetive-C are retained in python
 * - this looks a lot like ObjCClass_Type.tp_new, but it is _not_ the
 *   same!
 */
PyObject* ObjCClass_New(Class objc_class)
{
	PyObject* args;
	PyObject* dict;
	PyObject* result;
	PyObject* bases;
	struct class_info* info;

	result = objc_class_locate(objc_class);
	if (result != NULL) {
		Py_INCREF(result);
		return result;
	}

	dict = PyDict_New();
	if (add_class_fields(objc_class, dict) < 0)  {
		Py_DECREF(dict);
		return NULL;
	}
	if (ObjC_AddConvenienceMethods(objc_class, dict) < 0) {
		Py_DECREF(dict);
		return NULL;
	}

	bases = PyTuple_New(1);
	PyTuple_SET_ITEM(bases, 0, NULL);

	if (objc_class->super_class == NULL) {
		PyTuple_SetItem(bases, 0, (PyObject*)&ObjCObject_Type);
		Py_INCREF((&ObjCObject_Type));
	} else {
		PyTuple_SetItem(bases, 0, 
			ObjCClass_New(objc_class->super_class));
	} 
	args = PyTuple_New(3);
	PyTuple_SET_ITEM(args, 0, PyString_FromString(objc_class->name));
	PyTuple_SET_ITEM(args, 1, bases);
	PyTuple_SET_ITEM(args, 2, dict);

	result = PyType_Type.tp_new(&ObjCClass_Type, args, NULL);
	if (result == NULL) {
		Py_DECREF(args);
		return NULL;
	}
	Py_DECREF(args); /* XXX: Seems to be needed */

	info = get_class_info(result);
	if (info == NULL) abort();

	info->class = objc_class;
	info->sel_to_py = NULL; /* FIX ME */
	info->rescan_done = 0;

	objc_class_register(objc_class, result);
	Py_INCREF(result);

	return result;
}


Class ObjCClass_GetClass(PyObject* cls)
{
	struct class_info* info;

	if (!ObjCClass_Check(cls)) {
		ObjCErr_Set(objc_internal_error,
			"ObjCClass_GetClass called for non-class");
		return nil;
	}
	
	info = get_class_info(cls);
	return info->class;
}

PyObject* ObjCClass_FindSelector(PyObject* cls, SEL selector)
{
	struct class_info* info;
	PyObject*          result;
	PyObject*          attributes;
	PyObject*          key;
	PyObject*          v;
	int                i;
	int                len;

	if (!ObjCClass_Check(cls)) {
		ObjCErr_Set(objc_internal_error,
			"ObjCClass_GetClass called for non-class");
		return nil;
	}
	
	info = get_class_info(cls);
	if (info->sel_to_py == NULL) {
		info->sel_to_py = PyDict_New();
		if (info->sel_to_py == NULL) return NULL;
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
		if (key == NULL) abort();

		v = PyObject_GetAttr(cls, key);
		Py_DECREF(key);
		if (v == NULL) {
			PyErr_Clear();
			continue;
		}

		if (ObjCSelector_Check(v)) {
			if (((ObjCSelector*)v)->sel_selector == selector) {
				Py_DECREF(attributes);
				if (PyDict_SetItemString(info->sel_to_py,
					(char*)SELNAME(selector), v) == 0) {

					Py_INCREF(v);
				}
				return v;
			}
		} 
		Py_DECREF(v);
	}

	Py_DECREF(attributes);

	ObjCErr_Set(PyExc_AttributeError,
		"No selector %s", SELNAME(selector));
	if (PyDict_SetItemString(info->sel_to_py, 
			(char*)SELNAME(selector), Py_None) == 0) {
		Py_INCREF(Py_None);
	}
	return NULL;
}

/*
 * This should be a temporary function, need to find a better soluation for
 * the problem described in 'add_class_fields'
 *
 * Wanted: efficient way to detect if the method-table has changed, maybe cache
 * value of 'methodLists'...
 */
void 
ObjCClass_MaybeRescan(PyObject* class)
{
	struct class_info* info;
	int   r;

	if (!ObjCClass_Check(class)) {
		abort();	/* FIXME */
	}

	info = get_class_info(class);
	if (info == NULL) {
		abort(); 	/* FIXME */
	}

	if (info->rescan_done) return;

	r = add_class_fields(ObjCClass_GetClass(class), ((PyTypeObject*)class)->tp_dict);
	if (r < 0) abort();

	info->rescan_done = 1;
	if (info->sel_to_py) {
		Py_DECREF(info->sel_to_py);
		info->sel_to_py = NULL;
	}
}


int 
ObjCClass_IsSubClass(Class child, Class parent)
{
	if (parent == nil) return 1;

	while (child != nil) {
		if (child == parent) return 1;
		child = child->super_class;	
	}
	return 0;
}
