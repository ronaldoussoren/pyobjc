/*
 * This file contains the code that is used to create proxy-classes for Python
 * classes in the objective-C runtime.
 */
#include "pyobjc.h"
#include "objc_support.h"
#include <Foundation/NSInvocation.h>


/* List of instance variables, methods and class-methods that should not
 * be overridden from python
 */
static char* dont_override_methods[] = {
	"alloc",
	"dealloc",
	"retain",
	"release",
	"autorelease",
	"retainCount",
	NULL
};

/* Special methods for Python subclasses of Objective-C objects */
static void object_method_dealloc(id self, SEL sel);
static BOOL object_method_respondsToSelector(id self, SEL selector, 
	SEL aSelector);
static NSMethodSignature*  object_method_methodSignatureForSelector(id self, 
	SEL selector, SEL aSelector);
static void object_method_forwardInvocation(id self, SEL selector, 
	NSInvocation* invocation);
static id object_method_storedValueForKey_(id self, SEL _meth, NSString* key);
static id object_method_valueForKey_(id self, SEL _meth, NSString* key);
static void object_method_takeStoredValue_forKey_(id self, SEL _meth, 
	id value, NSString* key);
static void object_method_takeValue_forKey_(id self, SEL _meth, 
	id vlaue, NSString* key);


/*
 * When we create a 'Class' we actually create the struct below. This allows
 * us to add some extra information to the class defintion.
 *
 * NOTE1: the meta_class field is first because poseAs: copies the class but
 *        not the meta class (on MacOS X <= 10.2)
 * NOTE2: That doesn't help, test_posing still crashes.
 */
#define MAGIC 0xDEADBEEF
#define CLASS_WRAPPER(cls) ((struct class_wrapper*)(cls))
#define CHECK_MAGIC(o) do { if (CLASS_WRAPPER(o)->magic != MAGIC) abort(); } while(0)
struct class_wrapper {
	struct objc_class class;
	struct objc_class meta_class;
	PyObject* python_class;
	unsigned int magic; 
};

#define IDENT_CHARS "ABCDEFGHIJKLMNOPQSRTUVWXYZabcdefghijklmnopqrstuvwxyz_0123456789"

/*
 * This function finds the superclass of the class where 'selector' is
 * overridden using 'currentImp'.
 *
 * This is needed to call the correct superclass implementation in case 
 * of multiple layers of subclassing in Python. If we don't find the 'real'
 * superclass, a call to 
 *   'objc_msgSendSuper({ self->isa->super_class, self }, ...)' will just 
 * transfer back to 'currentImp' if the method was called from a subclass (e.g.
 * if 'currentImp' is the IMP for the superclass of 'self->isa' instead of the
 * one from 'self'.
 *
 * The 'right' way to do this is by building closures (if done correctly it
 * would at least be faster), but that requires an external library or low-level
 * (assembly) trickery.
 */
static Class find_real_superclass(Class startAt, SEL selector, 
		METHOD (*find_method)(Class, SEL), IMP currentImp)
{
	METHOD m;
	Class  cur;

	cur = startAt;
	m = find_method(cur, selector);

	/* Skip to class containing this function */
	while (m == NULL || m->method_imp != currentImp) {
		cur = cur->super_class;
		if (!cur) {
			Py_FatalError("PyObjC: find_real_superclass "
				"cannot find SEL in class hierarchy");
		}
		m = find_method(cur, selector);
	}

	/* Skip all classes containing this function */
	while (m != NULL && m->method_imp == currentImp) {
		cur = cur->super_class;
		if (!cur) {
			Py_FatalError("PyObjC: find_real_superclass "
				"reached top of class hierarchy");
		}
		m = find_method(cur, selector);
	}

	/* We found the 'real' superclass */
	return cur;
}


/*
 * Last step of the construction a python subclass of an objective-C class.
 *
 * Set reference to the python half in the objective-C half of the class.
 *
 * Return 0 on success, -1 on failure.
 */
int PyObjCClass_SetClass(Class objc_class, PyObject* py_class)
{
	if (objc_class == nil) {
		ObjCErr_Set(ObjCExc_internal_error, 
			"Trying to set class of <nil>\n", objc_class->name);
		return -1;
	}
	if (py_class == NULL || !PyObjCClass_Check(py_class)) {
		ObjCErr_Set(ObjCExc_internal_error,
			"Trying to set class to of %s to invalid value "
			"(type %s instead of %s)",
			objc_class->name, py_class->ob_type->tp_name,
			PyObjCClass_Type.tp_name);
		return -1;
	}

	CHECK_MAGIC(objc_class);

	if (CLASS_WRAPPER(objc_class)->python_class != NULL) {
		ObjCErr_Set(ObjCExc_internal_error,
			"Trying to set update PythonClass of %s",
			objc_class->name);
		return -1;
	}


	CLASS_WRAPPER(objc_class)->python_class = py_class;
	Py_INCREF(py_class);

	objc_addClass(objc_class);
	return 0;
}

/*
 * Call this when the python half of the class could not be created. 
 *
 * Due to technical restrictions it is not allowed to unbuild a class that
 * is already registered with the Objective-C runtime.
 */
void PyObjCClass_UnbuildClass(Class objc_class)
{
	struct class_wrapper* wrapper = CLASS_WRAPPER(objc_class); 

	if (objc_class == nil) {
		ObjCErr_Set(ObjCExc_internal_error, 
		"Trying to unregister class <nil>");
		return;
	}

	CHECK_MAGIC(objc_class);

	if (wrapper->python_class != NULL) {
		ObjCErr_Set(ObjCExc_internal_error,
			"Trying to unregister objective-C class %s, but it "
			"is already registered with the runtime",
			objc_class->name);
		return;
	}


	objc_freeMethodList(wrapper->class.METHODLISTS);
	objc_freeMethodList(wrapper->meta_class.METHODLISTS);
	free((char*)(wrapper->class.name));
	free(objc_class);
}

/*
 * Find the signature of 'selector' in the list of protocols.
 */
static char*
find_protocol_signature(PyObject* protocols, SEL selector)
{
	int len;
	int i;
	PyObject* proto;
	PyObject* info;

	if (!PyList_Check(protocols)) {
		ObjCErr_Set(ObjCExc_internal_error,
			"Protocol-list is not a list");
		return NULL;
	}

	/* First try the explicit protocol definitions */
	len = PyList_GET_SIZE(protocols);
	for (i = 0; i < len; i++) {
		proto = PyList_GET_ITEM(protocols, i);
		if (proto == NULL) {
			PyErr_Clear();
			continue;
		}
		if (!PyObjCInformalProtocol_Check(proto)) continue;

		info = PyObjCInformalProtocol_FindSelector(proto, selector);
		if (info != NULL) {
			return PyObjCSelector_Signature(info);
		}
	}

	/* Then check if another protocol users this selector */
	proto = PyObjCInformalProtocol_FindProtocol(selector);
	if (proto == NULL) {
		PyErr_Clear();
		return NULL;
	}

	info = PyObjCInformalProtocol_FindSelector(proto, selector);
	if (info != NULL) {
		if (PyList_Append(protocols, proto) < 0) {
			return NULL;
		}
		Py_INCREF(proto);
		return PyObjCSelector_Signature(info);
	}
	
	return NULL;
}

/*
 * Be smart about slots: Push them into Objective-C and leave an empty
 * __slots__ attribute.
 */
static int 
do_slots(PyObject* super_class, PyObject* clsdict)
{
	PyObject* slot_value;
	PyObject* slots;
	int       len, i;

	slot_value = PyDict_GetItemString(clsdict, "__slots__");
	if (slot_value == NULL) {
		PyObject* v;

		/* Add an __dict__ unless it is already there */
		PyErr_Clear();

		if (PyObjCClass_DictOffset(super_class) != 0) {
			/* We already have an __dict__ */
			return 0;
		}

		v = PyObjCInstanceVariable_New("__dict__");
		if (v == NULL) {
			return -1;
		}
		((PyObjCInstanceVariable*)v)->type[0] = '\0';
		((PyObjCInstanceVariable*)v)->isSlot = 1;
		if (PyDict_SetItemString(clsdict, "__dict__", v) < 0) {
			Py_DECREF(v);
			return -1;
		}
		Py_DECREF(v);

		slot_value = PyTuple_New(0);
		if (slot_value == NULL) {
			return NULL;
		}

		if (PyDict_SetItemString(clsdict, "__slots__", slot_value) < 0){
			Py_DECREF(slot_value);
			return -1;
		}
		Py_DECREF(slot_value);
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

		if (!PyString_Check(slot_value)) {
			ObjCErr_Set(PyExc_TypeError, 
				"__slots__ entry %d is not a string", i);
			Py_DECREF(slots);
			return -1;
		}

		var = (PyObjCInstanceVariable*)PyObjCInstanceVariable_New(
				PyString_AS_STRING(slot_value));
		if (var == NULL) {
			Py_DECREF(slots);
			return -1;
		}
		var->type[0] = '\0';
		((PyObjCInstanceVariable*)var)->isSlot = 1;
	
		if (PyDict_SetItem(clsdict, slot_value, (PyObject*)var) < 0) {
			Py_DECREF(slots);
			Py_DECREF(var);
			return -1;
		}
		Py_DECREF(var);
	}
	Py_DECREF(slots);

	slot_value = PyTuple_New(0);
	if (slot_value == NULL) {
		return NULL;
	}
	if (PyDict_SetItemString(clsdict, "__slots__", slot_value) < 0) {
		Py_DECREF(slot_value);
		return -1;
	}
	Py_DECREF(slot_value);
	return 0;
}

/*
 * First step of creating a python subclass of an objective-C class
 *
 * Returns NULL or the newly created objective-C klass. 'class_dict' may
 * be modified by this function.
 *
 * TODO:
 * - Set 'sel_class' of ObjCPythonSelector instances
 * - This function complete ignores other base-classes, even though they
 *   might override methods. Need to check the MRO documentation to check
 *   if this is a problem. 
 * - It is a problem when the user tries to use mixins to define common
 *   methods (like a NSTableViewDataSource mixin).
 */
Class PyObjCClass_BuildClass(Class super_class,  PyObject* protocols,
				char* name, PyObject* class_dict)
{
	PyObject*                key_list = NULL;
	PyObject*                key = NULL;
	PyObject*                value = NULL;
	int                      i, key_count;
	int	                 ivar_count = 0;
	int                      ivar_size  = 0;
	int                      meta_method_count = 0;
	int                      method_count = 0;
	int                      first_python_gen = 0;
	struct objc_ivar_list*   ivar_list = NULL;
	struct objc_method_list* method_list = NULL;
	struct objc_method_list* meta_method_list = NULL;
	struct class_wrapper*    new_class = NULL;
	Class                    root_class;
	char**                   curname;
	PyObject*		 py_superclass;
	int			 item_size;


	/* XXX: May as well directly pass this in... */
	py_superclass = PyObjCClass_New(super_class);
	if (py_superclass == NULL) return NULL;

	if (do_slots(py_superclass, class_dict) < 0) {
		goto error_cleanup;
	}

	if (!PyList_Check(protocols)) {
		ObjCErr_Set(ObjCExc_internal_error, "%s", 
			"protocol list not a PyList");
		goto error_cleanup;
	}
	if (!PyDict_Check(class_dict)) {
		ObjCErr_Set(ObjCExc_internal_error, "%s", 
			"class dict not a PyDict");
		goto error_cleanup;
	}
	if (super_class == NULL) {
		ObjCErr_Set(ObjCExc_internal_error, "%s", 
			"must have super_class");
		goto error_cleanup;
	}

	if (objc_lookUpClass(name) != NULL) {
		ObjCErr_Set(ObjCExc_error, "class '%s' exists", name);
		goto error_cleanup;
	}
	if (strspn(name, IDENT_CHARS) != strlen(name)) {
		ObjCErr_Set(ObjCExc_error, "'%s' not a valid name", name);
		goto error_cleanup;
	}

	/* 
	 * Check for methods/variables that must not be overridden in python.
	 */
	for (curname = dont_override_methods; *curname != NULL; curname++) {
		key = PyDict_GetItemString(class_dict, *curname);
		if (key != NULL) {
			ObjCErr_Set(ObjCExc_error,
				"Cannot override %s from python", *curname);
			goto error_cleanup;
		}
	}

	key_list = PyDict_Keys(class_dict);
	if (key_list == NULL) {
		goto error_cleanup;
	}

	key_count = PyList_Size(key_list);
	if (PyErr_Occurred()) {
		Py_DECREF(key_list);
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

		ivar_count        += 0;
		meta_method_count += 0; 
		method_count      += 8;
	}

	/* Allocate the class as soon as possible, for new selector objects */
	new_class = calloc(1, sizeof(struct class_wrapper));
	if (new_class == NULL) {
		goto error_cleanup;
	}

	/* First round, count new instance-vars and check for overridden 
	 * methods.
	 */
	for (i = 0; i < key_count; i++) {
		key = PyList_GetItem(key_list, i);
		if (PyErr_Occurred()) {
			PyErr_Clear();
			ObjCErr_Set(ObjCExc_internal_error,
				"Cannot fetch key in keylist");
			goto error_cleanup;
		}

		value = PyDict_GetItem(class_dict, key);
		if (value == NULL) {
			PyErr_Clear();
			ObjCErr_Set(ObjCExc_internal_error,
				"Cannot fetch item in keylist");
			goto error_cleanup;
		}

		if (PyObjCInstanceVariable_Check(value)) {
			if (class_getInstanceVariable(super_class, 
			    ((PyObjCInstanceVariable*)value)->name) != NULL) {
				ObjCErr_Set(ObjCExc_error,
					"Cannot replace instance variable %s",
					((PyObjCInstanceVariable*)value)->name);
				goto error_cleanup;
			}

			ivar_count ++;

			if (((PyObjCInstanceVariable*)value)->isSlot) {
				item_size = sizeof(PyObject**);
			} else {
				item_size = objc_sizeof_type(
					((PyObjCInstanceVariable*)value)->type);
			}
			if (item_size == -1) goto error_cleanup;
			ivar_size += item_size;

		} else if (PyObjCSelector_Check(value)) {
			PyObjCSelector* sel = (PyObjCSelector*)value;
			METHOD        meth;

			if (sel->sel_flags & PyObjCSelector_kCLASS_METHOD) {
				meth = class_getClassMethod(super_class,
					sel->sel_selector);
				meta_method_count ++;


			} else {
				meth = class_getInstanceMethod(super_class,
					sel->sel_selector);
				method_count ++;
			}

			/* TODO: If it already has a sel_class, create a copy */
			((PyObjCSelector*)value)->sel_class =
				&new_class->class;

		} else if (PyMethod_Check(value) || PyFunction_Check(value)) {
			PyObject* pyname;
			char*     ocname;
			SEL	  selector;
			METHOD    meth;
			int       is_class_method = 0;

			pyname = key;
			if (pyname == NULL) continue;

			ocname = PyString_AS_STRING(pyname);
			if (ocname[0] == '_' && ocname[1] == '_') {
				/* Skip special methods */
				continue;
			}

			selector = PyObjCSelector_DefaultSelector(ocname);

			meth = class_getInstanceMethod(super_class, selector);
			if (!meth) {
				meth = class_getClassMethod(
						super_class, selector);
				if (meth) {
					is_class_method = 1;
				}
			}

			if (meth) {
				/* The function overrides a method in the 
				 * objective-C class, replace by a selector 
				 * object.
				 *
				 * Get the signature through the python wrapper,
				 * the user may have specified a more exact
				 * signature!
				 */
				PyObject* super_sel = PyObjCClass_FindSelector(
					py_superclass, selector);
				if (!super_sel) goto error_cleanup;

				value = PyObjCSelector_New(
					value, 
					selector, 
					PyObjCSelector_Signature(super_sel),
					is_class_method,
					&new_class->class);
				new_class->class.name = "TempValue";
				Py_DECREF(super_sel);
			} else {
				char* signature;

				signature = find_protocol_signature(
					protocols, selector);
				value = PyObjCSelector_New(
					value, 
					selector, 
					signature,
					0,
					&new_class->class);
			}
			if (value == NULL) goto error_cleanup;
				
			if (PyDict_SetItem(class_dict, key, value) < 0) {
				Py_DECREF(value); value = NULL;
				goto error_cleanup;
			}
			Py_DECREF(value); value = NULL;
			if (is_class_method) {
				meta_method_count++;
			} else {
				method_count++;
			}
#if 0
		} else if ((value)->ob_type == PyClassMethod_Type) {
			/* Make a new selector object */
#endif
		}
	}

	/* Allocate space for the new instance variables and methods */

	if (ivar_count == 0)  {
		ivar_list = NULL;
	} else {
		ivar_list = malloc(sizeof(struct objc_ivar_list) +
			(ivar_count)*sizeof(struct objc_ivar));
		if (ivar_list == NULL) {
			PyErr_NoMemory();
			goto error_cleanup;
		}
		ivar_list->ivar_count = 0;
	}

	if (method_count == 0) {
		method_list = NULL;
	} else {
		method_list = objc_allocMethodList(method_count);

		if (method_list == NULL) {
			PyErr_NoMemory();
			goto error_cleanup;
		}
	}

	if (meta_method_count == 0) {
		meta_method_list = NULL;
		
	} else {
		meta_method_list = objc_allocMethodList(meta_method_count);

		if (meta_method_list == NULL) {
			PyErr_NoMemory();
			goto error_cleanup;
		}
	}


	/* And fill the method_lists and ivar_list */

#if 0
	/* Create new_class here, just in case we are the first python
	 * generation, in which case we need to use new_class (it must just
	 * be there, it doesn't have to be initialized)
	 */
	new_class = calloc(1, sizeof(struct class_wrapper));
	if (new_class == NULL) {
		goto error_cleanup;
	}
#endif


	ivar_size = super_class->instance_size;

	if (first_python_gen) {
		/* Our parent is a pure Objective-C class, add our magic
		 * methods and variables 
		 */
		 
		METHOD meth;
		PyObject* sel;

#		define METH(pyname, selector, types, imp) 		\
			meth = method_list->method_list + 		\
				method_list->method_count++;		\
			meth->method_name = selector;			\
			meth->method_types = types;			\
			meth->method_imp = (IMP)imp;			\
			sel = PyObjCSelector_NewNative(&new_class->class, \
				selector,  types, 0);			\
			if (sel == NULL) goto error_cleanup;		\
			PyDict_SetItemString(class_dict, pyname, sel);	\
			Py_DECREF(sel)


		METH(
			"dealloc", 
			@selector(dealloc), 
			"v@:", 
			object_method_dealloc);
		METH(
			"respondsToSelector_", 
			@selector(respondsToSelector:), 
			"c@::", 
			object_method_respondsToSelector);
		METH(
			"methodSignatureForSelector_", 
			@selector(methodSignatureForSelector:), 
			"@@::", 
			object_method_methodSignatureForSelector);
		METH(
			"forwardInvocation_", 
			@selector(forwardInvocation:), 
			"v@:@", 
			object_method_forwardInvocation);
		METH(
			"storedValueForKey_",
			@selector(storedValueForKey:),
			"@@:@",
			object_method_storedValueForKey_);
		METH(
			"valueForKey_",
			@selector(valueForKey:),
			"@@:@",
			object_method_valueForKey_);
		METH(
			"takeStoredValue_forKey_",
			@selector(takeStoredValue:forKey:),
			"@@:@@",
			object_method_takeStoredValue_forKey_);
		METH(
			"takeValue_forKey_",
			@selector(takeValue:forKey:),
			"@@:@@",
			object_method_takeValue_forKey_);
#undef		METH
	}

	for (i = 0; i < key_count; i++) {
		key = PyList_GetItem(key_list, i);
		if (key == NULL) {
			ObjCErr_Set(ObjCExc_internal_error,
				"Cannot fetch key in keylist");
			goto error_cleanup;
		}

		value = PyDict_GetItem(class_dict, key);
		if (value == NULL)  {
			ObjCErr_Set(ObjCExc_internal_error,
				"Cannot fetch item in keylist");
			goto error_cleanup;
		}

		if (PyObjCInstanceVariable_Check(value)) {
			IVAR var;

			var = ivar_list->ivar_list + ivar_list->ivar_count;
			ivar_list->ivar_count++;

			var->ivar_name = strdup(
				((PyObjCInstanceVariable*)value)->name);
			var->ivar_offset = ivar_size;

			/* XXX: Add alignment! */

			if (((PyObjCInstanceVariable*)value)->isSlot) {
				var->ivar_type = "^v";
				item_size = sizeof(PyObject**);
			} else {
				var->ivar_type = strdup(((PyObjCInstanceVariable*)value)->type);
				item_size = objc_sizeof_type(var->ivar_type);
			}

			if (item_size == -1) goto error_cleanup;
			ivar_size += item_size;

		} else if (PyObjCSelector_Check(value)) {
			PyObjCSelector* sel = (PyObjCSelector*)value;
			METHOD        meth;
			int           is_override = 0;
			struct objc_method_list* lst;

			if (sel->sel_flags & PyObjCSelector_kCLASS_METHOD) {
				meth = class_getClassMethod(super_class,
					sel->sel_selector);
				is_override = 1;
				lst = meta_method_list;
			} else {
				meth = class_getInstanceMethod(super_class,
					sel->sel_selector);
				if (meth) is_override = 1;
				lst = method_list;
			}

			meth = lst->method_list + lst->method_count;
			meth->method_name = sel->sel_selector;
			meth->method_types = sel->sel_signature;
		
			if (is_override) {
				meth->method_imp = 
					ObjC_FindIMP(super_class, 
						sel->sel_selector);
			} else {
				meth->method_imp = 
					ObjC_FindIMPForSignature(
						sel->sel_signature);

			}

			if (sel->sel_class == NULL) {
				sel->sel_class = &new_class->class;
			}

			if (meth->method_imp == NULL) {
				goto error_cleanup;
			}
			lst->method_count++;
		}
	}
	Py_DECREF(key_list);
	key_list = NULL;

	/* And now initialize the actual class... */

	root_class = super_class;
	while (root_class->super_class != NULL) {
		root_class = root_class->super_class;
	}

	new_class->magic = MAGIC;
	new_class->python_class = NULL;
	new_class->class.METHODLISTS = NULL;
	new_class->meta_class.METHODLISTS = NULL;
	GETISA(&new_class->class) = &new_class->meta_class;
	new_class->class.info = CLS_CLASS|CLS_METHOD_ARRAY;
	new_class->meta_class.info = CLS_META|CLS_METHOD_ARRAY;

	new_class->class.name = strdup(name);
	new_class->meta_class.name = new_class->class.name;

#ifndef GNU_RUNTIME
	new_class->class.METHODLISTS = 
		calloc(1, sizeof(struct objc_method_list*));
	if (new_class->class.METHODLISTS == NULL) goto error_cleanup;

	new_class->meta_class.METHODLISTS = 
		calloc(1, sizeof(struct objc_method_list*));
	if (new_class->meta_class.METHODLISTS == NULL) goto error_cleanup;

	/* 
	 * This is MacOS X specific, and an undocumented feature (long live
	 * Open Source!). 
	 *
	 * The code in the objc runtime assumes that the method lists are 
	 * terminated by '-1', and will happily overwite existing data if
	 * they aren't.
	 *
	 * Ronald filed a bugreport for this: Radar #3317376
	 */
	new_class->class.METHODLISTS[0] = (struct objc_method_list*)-1;
	new_class->meta_class.METHODLISTS[0] = (struct objc_method_list*)-1;

#endif

	new_class->class.super_class = super_class;
	new_class->meta_class.super_class = GETISA(super_class);
	GETISA(&new_class->meta_class) = GETISA(root_class);

	new_class->class.instance_size = ivar_size;
	new_class->class.ivars = ivar_list;

	new_class->class.protocols = NULL;
	new_class->meta_class.protocols = NULL;

	if (method_list) {
		class_addMethods(&(new_class->class), method_list);
	}
	if (meta_method_list) {
		class_addMethods(&(new_class->meta_class), meta_method_list);
	}

	Py_XDECREF(py_superclass);

	if (PyDict_DelItemString(class_dict, "__dict__") < 0) {
		PyErr_Clear();
	}

	/* 
	 * NOTE: Class is not registered yet, we do that as lately as possible
	 * because it is impossible to remove the registration from the
	 * objective-C runtime (at least on MacOS X).
	 */
	return &new_class->class;

error_cleanup:
	Py_XDECREF(py_superclass);

	if (key_list != NULL) {
		Py_DECREF(key_list);
		key_list = NULL;
	}

	if (ivar_list) {
		free(ivar_list);
	}
	if (method_list) {
		free(method_list);
	}
	if (meta_method_list) {
		free(meta_method_list);
	}

	if (new_class != NULL) {
		if(new_class->class.METHODLISTS) {
			objc_freeMethodList(new_class->class.METHODLISTS);
		}
		if (new_class->meta_class.METHODLISTS) {
			objc_freeMethodList(new_class->meta_class.METHODLISTS);
		}

		if (new_class->class.name) {
			free((char*)(new_class->class.name));
		}
		free(new_class);
	}

	return NULL;
}

/*
 * Below here are implementations of various methods needed to correctly
 * subclass Objective-C classes from Python. 
 *
 * These are added to the new Objective-C class by  PyObjCClass_BuildClass (but
 * only if the super_class is a 'pure' objective-C klass)
 *
 * NOTE:
 * - These functions will be used as methods, but as far as the compiler
 *   knows these are normal functions. You cannot use [super call]s here.
 */


static void
free_ivars(id self, PyObject* cls)
{
	/* Free all instance variables introduced through python */
	IVAR var;

	var = class_getInstanceVariable(PyObjCClass_GetClass(cls), "__dict__");
	if (var != NULL) {
		Py_XDECREF(*(PyObject**)(((char*)self) + var->ivar_offset));
		*(PyObject**)(((char*)self) + var->ivar_offset) = NULL;
	}

	while (cls != NULL) {
		Class     objcClass = PyObjCClass_GetClass(cls);
		PyObject* clsDict; 
		PyObject* clsValues;
		PyObject* o;
		int       len, i;

		if (objcClass == nil) break;


		clsDict = PyObject_GetAttrString(cls, "__dict__");
		if (clsDict == NULL) {
			PyErr_Clear();
			break;
		}
		
		/* Class.__dict__ is a dictproxy, which is not a dict and
		 * therefore PyDict_Values doesn't work.
		 */
		clsValues = PyObject_CallMethod(clsDict, "values", NULL);
		Py_DECREF(clsDict);
		if (clsValues == NULL) {
			PyErr_Clear();
			break;
		}

		len = PyList_Size(clsValues);
		/* Check type */
		for (i = 0; i < len; i++) {
			PyObjCInstanceVariable* iv;

			o = PyList_GET_ITEM(clsValues, i);

			if (o == NULL) continue;
			if (!PyObjCInstanceVariable_Check(o)) continue;
		
			iv = ((PyObjCInstanceVariable*)o);

			if (iv->type[0] != '@') continue;
			if (iv->isOutlet) continue;

			var = class_getInstanceVariable(objcClass, iv->name);
			if (var == NULL) continue;

			if (iv->isSlot) {
				Py_XDECREF(*(PyObject**)(((char*)self) + 
					var->ivar_offset));
			} else {
				[*(id*)(((char*)self) + var->ivar_offset) release];
				*(id*)(((char*)self) + var->ivar_offset) = NULL;
			}
		}

		Py_DECREF(clsValues);

		o = PyObject_GetAttrString(cls, "__bases__");
		if (o == NULL) {
			PyErr_Clear();
			cls = NULL;
		}  else if (PyTuple_Size(o) == 0) {
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
static void object_method_dealloc(id self, SEL sel __attribute__((__unused__)))
{
	struct objc_super super;
	PyObject* obj;
	PyObject* delmethod;
	PyObject* cls;

	PyObject* ptype, *pvalue, *ptraceback;

	PyErr_Fetch(&ptype, &pvalue, &ptraceback);

	CHECK_MAGIC(self->isa);
	cls = PyObjCClass_New(self->isa);
	if (!PyObjCClass_HasPythonImplementation(cls)) {
		printf("-dealloc substitute called for pure ObjC class\n");
		abort();
	}

	delmethod = PyObjCClass_GetDelMethod(cls);
	if (delmethod != NULL) {
		PyObject* s = _PyObjCObject_NewDeallocHelper(self);
		obj = PyObject_CallFunction(delmethod, "O", s);
		_PyObjCObject_FreeDeallocHelper(s);
		if (obj == NULL) {
			PyErr_WriteUnraisable(delmethod);
		} else {
			Py_DECREF(obj);
		}
		Py_DECREF(delmethod);
	}

	free_ivars(self, cls);

	PyErr_Restore(ptype, pvalue, ptraceback);

	super.class = find_real_superclass(GETISA(self),
		@selector(dealloc), class_getInstanceMethod, 
		(IMP)object_method_dealloc);
	RECEIVER(super) = self;
	
	objc_msgSendSuper(&super, @selector(dealloc)); 
}

/* -respondsToSelector: */
static BOOL 
object_method_respondsToSelector(id self, SEL selector, SEL aSelector)
{
	struct objc_super super;
	BOOL              res;
        PyObject*         pyself;
	PyObject*         pymeth;

	/* First check if we respond */
	pyself = PyObjCObject_New(self);
	if (pyself == NULL) {
		return NO;
	}
	pymeth = PyObjCObject_FindSelector(pyself, aSelector);
	Py_DECREF(pyself);
	if (pymeth) {
		Py_DECREF(pymeth);
		return YES;
	}
	PyErr_Clear();

	/* Check superclass */
	super.class = find_real_superclass(GETISA(self),
			selector, class_getInstanceMethod, 
			(IMP)object_method_respondsToSelector);
	RECEIVER(super) = self;

	res = (int)objc_msgSendSuper(&super, selector, aSelector);
	return res;
}

/* -methodSignatureForSelector */
static NSMethodSignature*  
object_method_methodSignatureForSelector(id self, SEL selector, SEL aSelector)
{
	NSMethodSignature* result = nil;
	struct objc_super  super;
        PyObject*          pyself;
	PyObject*          pymeth;

	super.class = find_real_superclass(
			GETISA(self), 
			selector, class_getInstanceMethod, 
			(IMP)object_method_methodSignatureForSelector);
	RECEIVER(super) = self;

	NS_DURING
		result = objc_msgSendSuper(&super, selector, aSelector);
	NS_HANDLER
		result = nil;
	NS_ENDHANDLER

	if (result != nil) {
		return result;
	}

	pyself = PyObjCObject_New(self);
	if (pyself == NULL) {
		PyErr_Clear();
		return nil;
	}

	pymeth = PyObjCObject_FindSelector(pyself, aSelector);
	if (!pymeth) {
		Py_DECREF(pyself);
		PyErr_Clear();
		return nil;
	}

	result =  [NSMethodSignature signatureWithObjCTypes:(
		  	(PyObjCSelector*)pymeth)->sel_signature];
	Py_DECREF(pymeth);
	Py_DECREF(pyself);
	return result;
}

/* -forwardInvocation: */
static void
object_method_forwardInvocation(id self, SEL selector, NSInvocation* invocation)
{
	PyObject*	args;
	PyObject* 	result;
	PyObject*       v;
	int		isAlloc;
	int             i;
	int 		len;
	NSMethodSignature* signature;
	char		   argbuf[1024];
	const char* 		type;
	void* arg = NULL;
	int  err;
	int   arglen;
	PyObject* pymeth;
	PyObject* pyself;
	int have_output = 0;

	pyself = PyObjCObject_New(self);
	if (pyself == NULL) {
		PyObjCErr_ToObjC();
		return;
	}
	pymeth = PyObjCObject_FindSelector(pyself, [invocation selector]);
	if ((pymeth == NULL) || ObjCNativeSelector_Check(pymeth)) {
		struct objc_super super;

		if (pymeth == NULL) PyErr_Clear();

		Py_XDECREF(pymeth);
		Py_XDECREF(pyself);

		super.class = find_real_superclass(
				GETISA(self), 
				selector, class_getInstanceMethod, 
				(IMP)object_method_forwardInvocation);
		super.receiver = self;
		objc_msgSendSuper(&super, selector, invocation);
		return;
	}

	Py_XDECREF(pymeth);
	Py_XDECREF(pyself);

	signature = [invocation methodSignature];
	len = [signature numberOfArguments];

	args = PyList_New(1);
	if (args == NULL) {
		PyObjCErr_ToObjC();
	}

	i = PyList_SetItem(args, 0, pythonify_c_value(
					[signature getArgumentTypeAtIndex:0],
					(void*)&self));
	if (i < 0) {
		Py_DECREF(args);
		PyObjCErr_ToObjC();
		return;
	}

	for (i = 2; i < len; i++) {
		type = [signature getArgumentTypeAtIndex:i];
		arglen = objc_sizeof_type(type);

		if (arglen == -1) {
			Py_DECREF(args);
			PyObjCErr_ToObjC();
			return;
		}

		arg = alloca(arglen);
		
		[invocation getArgument:argbuf atIndex:i];

		switch (*type) {
		case _C_PTR:
			have_output ++;
			v = pythonify_c_value(type+1, *(void**)argbuf);
			break;
		case _C_INOUT:
			if (type[1] == _C_PTR) {
				have_output ++;
			}
			/* FALL THROUGH */
		case _C_IN: case _C_CONST:
			if (type[1] == _C_PTR) {
				v = pythonify_c_value(type+2, *(void**)argbuf);
			} else {
				v = pythonify_c_value(type+1, argbuf);
			}
			break;
		case _C_OUT:
			if (type[1] == _C_PTR) {
				have_output ++;
			}
			continue;
		default:
			v = pythonify_c_value(type, argbuf);
		}

		if (v == NULL) {
			Py_DECREF(args);
			PyObjCErr_ToObjC();
			return;
		}

		if (PyList_Append(args, v) < 0) {
			Py_DECREF(args);
			PyObjCErr_ToObjC();
			return;
		}
	}

	v = PyList_AsTuple(args);
	if (v == NULL) {
		Py_DECREF(args);
		PyObjCErr_ToObjC();
		return;
	}
	Py_DECREF(args);
	args = v;

	result = PyObjC_CallPython(self, [invocation selector], args, &isAlloc);
	Py_DECREF(args);
	if (result == NULL) {
		PyObjCErr_ToObjC();
		return;
	}

	type = [signature methodReturnType];
	arglen = objc_sizeof_type(type);

	if (arglen == -1) {
		PyObjCErr_ToObjC();
		return;
	}

	if (!have_output) {
		if (*type  != _C_VOID && *type != _C_ONEWAY) {
			arg = alloca(arglen+1);

			err = depythonify_c_value(type, result, arg);
			if (err == -1) {
				PyObjCErr_ToObjC();
				return;
			}
			if (isAlloc && *type == _C_ID) {
				[(*(id*)arg) retain];
			}
			[invocation setReturnValue:arg];
		}
		Py_DECREF(result);
	} else {
		int idx;
		PyObject* real_res;

		if (*type == _C_VOID && have_output == 1) {
			/* One output argument, and a 'void' return value,
			 * the python method returned just the output
			 * argument
			 */
			/* This should be cleaned up, unnecessary code
			 * duplication
			 */

			for (i = 2; i < len;i++) {
				void* ptr;
				type = [signature getArgumentTypeAtIndex:i];

				if (arglen == -1) {
					PyObjCErr_ToObjC();
					return;
				}

				switch (*type) {
				case _C_PTR:
					type ++;
					break;
				case _C_INOUT: case _C_OUT:
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
					PyObjCErr_ToObjC();
				}
				if (v->ob_refcnt == 1 && type[0] == _C_ID) {
					/* make sure return value doesn't die before
					 * the caller can get its hands on it.
					 */
					[[*(id*)ptr retain] autorelease];
				}

				/* We have exactly 1 output argument */
				break;

			}

			Py_DECREF(result);
			return;
		}

		if (*type != _C_VOID) {
			if (!PyTuple_Check(result) 
			     || PyTuple_Size(result) != have_output+1) {
				ObjCErr_Set(PyExc_TypeError,
					"%s: Need tuple of %d arguments as result",
					SELNAME([invocation selector]),
					have_output+1);
				Py_DECREF(result);
				PyObjCErr_ToObjC();
				return;
			}
			idx = 1;
			real_res = PyTuple_GET_ITEM(result, 0);

			arg = alloca(arglen+1);

			err = depythonify_c_value(type, real_res, arg);
			if (err == -1) {
				PyObjCErr_ToObjC();
				return;
			}
			if (isAlloc && *type == _C_ID) {
				[(*(id*)arg) retain];
			}
			[invocation setReturnValue:arg];

		} else {
			if (!PyTuple_Check(result) 
			     || PyTuple_Size(result) != have_output) {
				ObjCErr_Set(PyExc_TypeError,
					"%s: Need tuple of %d arguments as result",
					SELNAME([invocation selector]),
					have_output);
				Py_DECREF(result);
				PyObjCErr_ToObjC();
				return;
			}
			idx = 0;
		}


		for (i = 2; i < len;i++) {
			void* ptr;
			type = [signature getArgumentTypeAtIndex:i];

			if (arglen == -1) {
				PyObjCErr_ToObjC();
				return;
			}

			switch (*type) {
			case _C_PTR:
				type ++;
				break;
			case _C_INOUT: case _C_OUT:
				if (type[1] != _C_PTR) {
					continue;
				}
				type += 2;
				break;
			default:
				continue;
			}

			[invocation getArgument:&ptr atIndex:i];
			v = PyTuple_GET_ITEM(result, idx++);
			err = depythonify_c_value(type, v, ptr);
			if (err == -1) {
				PyObjCErr_ToObjC();
			}
			if (v->ob_refcnt == 1 && type[0] == _C_ID) {
				/* make sure return value doesn't die before
				 * the caller can get its hands on it.
			   	 */
				[[*(id*)ptr retain] autorelease];
			}

		}
		Py_DECREF(result);
	}
}

/*
 * XXX: Function PyObjC_CallPython should be moved
 */

PyObject*
PyObjC_CallPython(id self, SEL selector, PyObject* arglist, int* isAlloc)
{
	PyObject* pyself = NULL;
	PyObject* pymeth = NULL;
	PyObject* result;


	pyself = pythonify_c_value("@", &self);
	if (pyself == NULL) {
		PyObjCErr_ToObjC();
		return NULL;
	}
	
	if (PyObjCClass_Check(pyself)) {
		pymeth = PyObjCClass_FindSelector(pyself, selector);
	} else {
		pymeth = PyObjCObject_FindSelector(pyself, selector);
	}
	if (pymeth == NULL) {
		Py_DECREF(pyself);
		PyObjCErr_ToObjC();
		return NULL;
	}

	if (isAlloc != NULL) {
		*isAlloc = ((PyObjCSelector*)pymeth)->sel_flags;
		*isAlloc = (*isAlloc & PyObjCSelector_kDONATE_REF) != 0;
	}

	result = PyObject_Call(pymeth, arglist, NULL);
	Py_DECREF(pymeth);
	Py_DECREF(pyself);

	if (result == NULL) {
		PyObjCErr_ToObjC();
		return NULL;
	}

	return result;
}

/*
 * Suppport for key-value encoding for Python/ObjC hybrids.
 * 
 * NOTE: This implementation is likely to change, which probably will have
 * user-visible effects.
 *
 * We check python-specific ways to read/write attributes, and then defer
 * to the super-class implementation. This seems to be the best way to 
 * play nice with when subclassing arbitrary Objective-C classes.
 */

static int
getAttribute(id self, NSString* key, id* result)
{
	PyObject* cls = PyObjCClass_New(self->isa);
	PyObject* val;
	PyObject* att;
	PyObject* dict;
	int dictoffset;
	int r;
	id  tmpVal;

	dictoffset = PyObjCClass_DictOffset(cls);
	if (dictoffset != 0) {
		PyObject** dictptr = (PyObject**)(((char*)self) + dictoffset);
		if (*dictptr != NULL) {
			val = PyDict_GetItemString(*dictptr, 
				(char*)[key cString]);
			if (val == NULL) {
				PyErr_Clear();
			} else {
				tmpVal = nil;
				r = depythonify_c_value(
					@encode(id), val, (void*)&tmpVal);
				if (r == -1) {
					PyErr_Clear();
				}
				*result = tmpVal;
				return r;
			}
		}
	}

	/* 
	 * Maybe this is a descriptor object, check if there is a
	 * non-method attribute in the class
	 */
	att = PyObject_GetAttrString(cls, (char*)[key cString]);
	if (att == NULL) {
		PyErr_Clear();
	} else {
		if (!PyObjCSelector_Check(att)) {
			Py_DECREF(att);
			val = PyObject_GetAttrString(
				PyObjCObject_New(self),
				(char*)[key cString]);
			if (val == NULL) {
				PyErr_Clear();
				return -1;
			} else {
				r = depythonify_c_value(@encode(id),
					val, result);
				Py_DECREF(val);
				if (r == -1) {
					PyErr_Clear();
				}
				return r;
			}
		} 
		Py_DECREF(att);
	}

	/* Check for properties, data properties won't be found using
	 * getattr(cls, propname).
	 */
	dict = PyObject_GetAttrString(cls, "__dict__");
	if (dict == NULL) {
		PyErr_Clear();
	} else {
		/* Class __dict__ need not be an actual dict! */
		att = PyMapping_GetItemString(dict, (char*)[key cString]);
		if (att == NULL) {
			PyErr_Clear();
		} else if (!PyObjCSelector_Check(att)) {
			val = PyObject_GetAttrString(
				PyObjCObject_New(self),
				(char*)[key cString]);
			if (val == NULL) {
				PyErr_Clear();
				return -1;
			} else {
				r = depythonify_c_value(@encode(id),
					val, result);
				Py_DECREF(val);
				if (r == -1) {
					PyErr_Clear();
				}
				return r;
			}
		} 
	}
	return -1;
}

static int
getAccessor(id self, NSString* key, id* result)
{
	PyObject* cls = PyObjCClass_New(self->isa);
	PyObject* val;
	PyObject* att;
	int r;

	att = PyObject_GetAttrString(cls, (char*)[key cString]);
	if (att == NULL) {
		PyErr_Clear();
	} else {
		if (PyObjCSelector_Check(att) 
				|| PyFunction_Check(att) 
				|| PyMethod_Check(att)) {
			Py_DECREF(att);
			val = PyObject_CallMethod(
				PyObjCObject_New(self),
				(char*)[key cString],
				NULL);
			if (val == NULL) {
				PyErr_Clear();
				return -1;
			} else {
				r = depythonify_c_value(@encode(id),
					val, result);
				if (r == -1) {
					PyErr_Clear();
				}
				return r;
			}
		} 
		Py_DECREF(att);
	}

	return -1;
}

static int
setAttribute(id self, NSString* key, id value)
{
	PyObject* cls = PyObjCClass_New(self->isa);
	PyObject* val;
	PyObject* att;
	int dictoffset;
	int r;

	dictoffset = PyObjCClass_DictOffset(cls);
	if (dictoffset != 0) {
		PyObject** dictptr = (PyObject**)(((char*)self) + dictoffset);
		if (*dictptr != NULL && PyDict_GetItemString(
				*dictptr, (char*)[key cString]) != NULL) {

			val = pythonify_c_value(@encode(id), &value);
			if (val == NULL) {
				PyErr_Clear();
				return -1;
			}

			r = PyDict_SetItemString(*dictptr, 
				(char*)[key cString], val);
			if (r == -1) {
				PyErr_Clear();
			}
			Py_DECREF(val);
			return r;
		}
	}

	/* 
	 * Maybe this is a descriptor object, check if there is a
	 * non-method attribute in the class
	 */
	att = PyObject_GetAttrString(cls, (char*)[key cString]);
	if (att == NULL) {
		PyErr_Clear();
	} else {
		if (!PyObjCSelector_Check(att)) {
			Py_DECREF(att);

			val = pythonify_c_value(@encode(id), &value);
			if (val == NULL) {
				PyErr_Clear();
				return -1;
			}

			r = PyObject_SetAttrString(
				PyObjCObject_New(self),
				(char*)[key cString], val);
			if (r == -1) {
				PyErr_Clear();
			}
			Py_DECREF(val);
			return r;
		}
		Py_DECREF(att);
	}

	return -1;
}

static int
setAccessor(id self, NSString* key, id value)
{
	PyObject* cls = PyObjCClass_New(self->isa);
	PyObject* val;
	PyObject* att;

	att = PyObject_GetAttrString(cls, (char*)[key cString]);
	if (att == NULL) {
		PyErr_Clear();
	} else {
		if (PyObjCSelector_Check(att) 
				|| PyFunction_Check(att) 
				|| PyMethod_Check(att)) {

			Py_DECREF(att);

			val = pythonify_c_value(@encode(id), &value);
			if (val == NULL) {
				PyErr_Clear();
				return -1;
			}

			att = PyObject_CallMethod(
				PyObjCObject_New(self),
				(char*)[key cString], "O", val);
			if (att == NULL) {
				PyErr_Print();
				PyErr_Clear();
			}
			Py_XDECREF(att);
			Py_DECREF(val);
			return (att == NULL) ? -1 : 0;
		}
		Py_DECREF(att);
	}

	return -1;
}

static id
object_method_storedValueForKey_(id self, SEL _meth, NSString* key)
{
	id result;
	int r;
	struct objc_super super;

	r = getAccessor(self, [NSString stringWithFormat: @"get_%@", key], 
		&result);
	if (r == 0) {
		return result;
	}

	r = getAttribute(self, key, &result);
	if (r == 0) {
		return result;
	}


	r = getAccessor(self, [NSString stringWithFormat: @"_get_%@", key], 
		&result);
	if (r == 0) {
		return result;
	}

	r = getAttribute(self, [NSString stringWithFormat: @"_%@", key], 
		&result);
	if (r == 0) {
		return result;
	}

	/* Call super */
	super.class = find_real_superclass(
		GETISA(self),
		_meth,
		class_getInstanceMethod,
		(IMP)object_method_storedValueForKey_);
	super.receiver = self;
	return objc_msgSendSuper(&super, _meth, key);
}

static id
object_method_valueForKey_(id self, SEL _meth, NSString* key)
{
	id result;
	int r;
	struct objc_super super;

	r = getAccessor(self, [NSString stringWithFormat: @"get_%@", key], 
		&result);
	if (r == 0) {
		return result;
	}

	r = getAttribute(self, key, &result);
	if (r == 0) {
		return result;
	}


	r = getAccessor(self, [NSString stringWithFormat: @"_get_%@", key], 
		&result);
	if (r == 0) {
		return result;
	}

	r = getAttribute(self, [NSString stringWithFormat: @"_%@", key], 
		&result);
	if (r == 0) {
		return result;
	}


	/* Call super */
	super.class = find_real_superclass(
		GETISA(self),
		_meth,
		class_getInstanceMethod,
		(IMP)object_method_valueForKey_);
	super.receiver = self;
	return objc_msgSendSuper(&super, _meth, key);
}

static void
object_method_takeStoredValue_forKey_(id self, SEL _meth, id value, NSString* key)
{
	struct objc_super super;
	int r;

	r = setAccessor(self, 
		[NSString stringWithFormat:@"set_%@", key], value);
	if (r == 0) {
		return;
	}

	r = setAccessor(self, 
		[NSString stringWithFormat:@"set%@", [key capitalizedString]], 
		value);
	if (r == 0) {
		return;
	}

	r = setAttribute(self, key, value);
	if (r == 0) {
		return;
	}

	r = setAccessor(self, 
		[NSString stringWithFormat:@"_set_%@", key], value);
	if (r == 0) {
		return;
	}

	r = setAccessor(self, 
		[NSString stringWithFormat:@"_set%@", [key capitalizedString]], 
		value);
	if (r == 0) {
		return;
	}

	r = setAttribute(self, [NSString stringWithFormat:@"_%@", key], value);
	if (r == 0) {
		return;
	}

	/* Call super */
	NS_DURING
		super.class = find_real_superclass(
			GETISA(self),
			_meth,
			class_getInstanceMethod,
			(IMP)object_method_takeStoredValue_forKey_);
		super.receiver = self;
		(void)objc_msgSendSuper(&super, _meth, value, key);
	NS_HANDLER
		/* Parent doesn't know the key, try to create in the 
		 * python side, just like for plain python objects.
		 */
		if ([[localException name] isEqual:@"NSUnknownKeyException"]) {
			PyObject* selfObj = PyObjCObject_New(self);
			PyObject* val;

			val = pythonify_c_value(@encode(id), &value);
			if (val == NULL) {
				PyErr_Clear();
				[localException raise];
			}

			r = PyObject_SetAttrString(selfObj, 
				(char*)[key cString],
				val);
			Py_DECREF(val);
			if (r == -1) {
				PyErr_Clear();
				[localException raise];
			}
				
		} else {
			[localException raise];
		}
	NS_ENDHANDLER
}

static void
object_method_takeValue_forKey_(id self, SEL _meth, id value, NSString* key)
{
	struct objc_super super;
	int r;

	r = setAccessor(self, 
		[NSString stringWithFormat:@"set_%@", key], value);
	if (r == 0) {
		return;
	}

	r = setAccessor(self, 
		[NSString stringWithFormat:@"set%@", [key capitalizedString]], 
		value);
	if (r == 0) {
		return;
	}

	r = setAttribute(self, key, value);
	if (r == 0) {
		return;
	}

	r = setAccessor(self, 
		[NSString stringWithFormat:@"_set_%@", key], value);
	if (r == 0) {
		return;
	}

	r = setAccessor(self, 
		[NSString stringWithFormat:@"_set%@", [key capitalizedString]], 
		value);
	if (r == 0) {
		return;
	}

	r = setAttribute(self, [NSString stringWithFormat:@"_%@", key], value);
	if (r == 0) {
		return;
	}


	/* Call super */
	NS_DURING
		super.class = find_real_superclass(
			GETISA(self),
			_meth,
			class_getInstanceMethod,
			(IMP)object_method_takeValue_forKey_);
		super.receiver = self;
		(void)objc_msgSendSuper(&super, _meth, value, key);
	NS_HANDLER
		/* Parent doesn't know the key, try to create in the 
		 * python side, just like for plain python objects.
		 */
		if ([[localException name] isEqual:@"NSUnknownKeyException"]) {
			PyObject* selfObj = PyObjCObject_New(self);
			PyObject* val;

			val = pythonify_c_value(@encode(id), &value);
			if (val == NULL) {
				PyErr_Clear();
				[localException raise];
			}

			r = PyObject_SetAttrString(selfObj, 
				(char*)[key cString],
				val);
			Py_DECREF(val);
			if (r == -1) {
				PyErr_Clear();
				[localException raise];
			}
				
		} else {
			[localException raise];
		}
	NS_ENDHANDLER
}
