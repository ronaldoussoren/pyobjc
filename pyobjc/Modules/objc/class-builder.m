/*
 * This file contains the code that is used to create proxy-classes for Python
 * classes in the objective-C runtime.
 */
#include "pyobjc.h"

#import <Foundation/NSInvocation.h>

#if defined(MACOSX) && MAC_OS_X_VERSION_MAX_ALLOWED >= MAC_OS_X_VERSION_10_3
#import <Foundation/NSKeyValueObserving.h>
#endif

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
static void object_method_dealloc(
		ffi_cif* cif,
		void* retval,
		void** args,
		void* userarg);
static void object_method_respondsToSelector(
		ffi_cif* cif,
		void* retval,
		void** args,
		void* userarg);
static void object_method_methodSignatureForSelector(
		ffi_cif* cif,
		void* retval,
		void** args,
		void* userarg);
static void object_method_forwardInvocation(
		ffi_cif* cif,
		void* retval,
		void** args,
		void* userarg);
static void object_method_storedValueForKey_(
		ffi_cif* cif,
		void* retval,
		void** args,
		void* userarg);
static void object_method_valueForKey_(
		ffi_cif* cif,
		void* retval,
		void** args,
		void* userarg);
static void object_method_takeStoredValue_forKey_(
		ffi_cif* cif,
		void* retval,
		void** args,
		void* userarg);
static void object_method_takeValue_forKey_(
		ffi_cif* cif,
		void* retval,
		void** args,
		void* userarg);

/*
 * When we create a 'Class' we actually create the struct below. This allows
 * us to add some extra information to the class defintion.
 *
 * NOTE1: the meta_class field is first because poseAs: copies the class but
 *        not the meta class (on MacOS X <= 10.2)
 * NOTE2: That doesn't help, test_posing still crashes.
 * XXX: Is this still relevant? The current code only refers to the struct
 *      during the construction of the class, which means poseAs: probably 
 *      works just fine (to be checked after 1.1)
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
 * Last step of the construction a python subclass of an objective-C class.
 *
 * Set reference to the python half in the objective-C half of the class.
 *
 * Return 0 on success, -1 on failure.
 */
int 
PyObjCClass_SetClass(Class objc_class, PyObject* py_class)
{
	if (objc_class == nil) {
		PyErr_SetString(PyObjCExc_InternalError, 
			"Trying to set class of <nil>\n");
		return -1;
	}
	if (py_class == NULL || !PyObjCClass_Check(py_class)) {
		PyErr_Format(PyObjCExc_InternalError,
			"Trying to set class to of %s to invalid value "
			"(type %s instead of %s)",
			objc_class->name, py_class->ob_type->tp_name,
			PyObjCClass_Type.tp_name);
		return -1;
	}

	CHECK_MAGIC(objc_class);

	if (CLASS_WRAPPER(objc_class)->python_class != NULL) {
		PyErr_Format(PyObjCExc_InternalError,
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
void 
PyObjCClass_UnbuildClass(Class objc_class)
{
	struct class_wrapper* wrapper = CLASS_WRAPPER(objc_class); 

	if (objc_class == nil) {
		PyErr_SetString(PyObjCExc_InternalError, 
		"Trying to unregister class <nil>");
		return;
	}

	CHECK_MAGIC(objc_class);

	if (wrapper->python_class != NULL) {
		PyErr_Format(PyObjCExc_InternalError,
			"Trying to unregister objective-C class %s, but it "
			"is already registered with the runtime",
			objc_class->name);
		return;
	}


	PyObjCRT_ClearClass(&(wrapper->class));
	PyObjCRT_ClearClass(&(wrapper->meta_class));
	free(objc_class);
}

/*
 * Be smart about slots: Push them into Objective-C and leave an empty
 * __slots__ attribute, that way we don't store object-state in the python
 * proxy.
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
			return 0;
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
			PyErr_Format(PyExc_TypeError, 
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
		return 0;
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
 * Returns NULL or the newly created objective-C class. 'class_dict' may
 * be modified by this function.
 *
 * TODO:
 * - Set 'sel_class' of PyObjCPythonSelector instances
 * - This function complete ignores other base-classes, even though they
 *   might override methods. Need to check the MRO documentation to check
 *   if this is a problem. 
 * - It is a problem when the user tries to use mixins to define common
 *   methods (like a NSTableViewDataSource mixin), this works but slowly
 *   because this calls will always be resolved through forwardInvocation:
 * - Add an 'override' flag that makes it possible to replace an existing
 *   PyObjC class, feature request for the Python-IDE  (write class, run,
 *   oops this doesn't work, rewrite class, reload and continue testing in
 *   the running app)
 */
Class 
PyObjCClass_BuildClass(Class super_class,  PyObject* protocols,
				char* name, PyObject* class_dict)
{
	PyObject*                key_list = NULL;
	PyObject*                key = NULL;
	PyObject*                value = NULL;
	int                      i, key_count;
	int                      ivar_count = 0;
	int                      ivar_size  = 0;
	int                      meta_method_count = 0;
	int                      method_count = 0;
	int                      first_python_gen = 0;
	struct objc_ivar_list*   ivar_list = NULL;
	struct objc_method_list* method_list = NULL;
	struct objc_method_list* meta_method_list = NULL;
	struct class_wrapper*    new_class = NULL;
	Class                    root_class;
	Class			 cur_class;
	char**                   curname;
	PyObject*                py_superclass;
	int                      item_size;

	if (!PyList_Check(protocols)) {
		PyErr_Format(PyObjCExc_InternalError,  
			"protocol list not a python 'list' but '%s'",
			protocols->ob_type->tp_name);
		goto error_cleanup;
	}
	if (!PyDict_Check(class_dict)) {
		PyErr_Format(PyObjCExc_InternalError, 
			"class dict not a python 'dict', but '%s'",
			class_dict->ob_type->tp_name);
		goto error_cleanup;
	}
	if (super_class == NULL) {
		PyErr_SetString(PyObjCExc_InternalError, 
			"must have super_class");
		goto error_cleanup;
	}

	if ((cur_class = PyObjCRT_LookUpClass(name)) != NULL) {
		/*
		 * Only allow redefinition of classes that are defined in
		 * python and are in the same module.
		 * This allows using reload() without hiding erroneous
		 * redefinition (e.g. someone forgetting that classnames
		 * must be globally unique.
		 */

		PyObject* tmp = PyObjCClass_New(cur_class);
		PyObject* m1;
		PyObject* m2;

		if (!PyObjCClass_HasPythonImplementation(tmp)) {
			PyErr_Format(PyObjCExc_Error, 
				"%s is overriding existing Objective-C class", 
				name);
			goto error_cleanup;
		} 

		m1 = PyObject_GetAttrString(tmp, "__module__");
		if (m1 == NULL) {
			PyErr_Clear();
		}

		m2 = PyDict_GetItemString(class_dict, "__module__");
		if (m2 == NULL) {
			PyErr_Clear();
		}

		if (m1 == NULL || m2 == NULL || 
				PyObject_RichCompareBool(m1, m2, Py_EQ) != 1) {
			Py_XDECREF(m1);
			Py_XDECREF(m2);
			if (PyErr_Occurred()) {
				goto error_cleanup;
			}
			PyErr_Format(PyObjCExc_Error, 
				"%s is overriding existing Objective-C class", 
				name);
			goto error_cleanup;
		}
		Py_DECREF(m1);
		Py_DECREF(m2);
	}
	if (strspn(name, IDENT_CHARS) != strlen(name)) {
		PyErr_Format(PyObjCExc_Error, "'%s' not a valid name", name);
		goto error_cleanup;
	}

	py_superclass = PyObjCClass_New(super_class);
	if (py_superclass == NULL) return NULL;

	if (do_slots(py_superclass, class_dict) < 0) {
		goto error_cleanup;
	}


	/* 
	 * Check for methods/variables that must not be overridden in python.
	 */
	for (curname = dont_override_methods; *curname != NULL; curname++) {
		key = PyDict_GetItemString(class_dict, *curname);
		if (key != NULL) {
			PyErr_Format(PyObjCExc_Error,
				"Cannot override method '%s' from python", 
				*curname);
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
	new_class = malloc(sizeof(struct class_wrapper));
	if (new_class == NULL) {
		goto error_cleanup;
	}
	memset(new_class, 0, sizeof(*new_class));

	/* First round, count new instance-vars and check for overridden 
	 * methods.
	 */
	for (i = 0; i < key_count; i++) {
		key = PyList_GET_ITEM(key_list, i);
		if (PyErr_Occurred()) {
			PyErr_SetString(PyObjCExc_InternalError,
				"PyObjCClass_BuildClass: "
				"Cannot fetch key in keylist");
			goto error_cleanup;
		}

		value = PyDict_GetItem(class_dict, key);
		if (value == NULL) {
			PyErr_SetString(PyObjCExc_InternalError,
				"PyObjCClass_BuildClass: "
				"Cannot fetch item in keylist");
			goto error_cleanup;
		}

		if (PyObjCInstanceVariable_Check(value)) {
			if (class_getInstanceVariable(super_class, 
			    ((PyObjCInstanceVariable*)value)->name) != NULL) {
				PyErr_Format(PyObjCExc_Error,
					"a superclass already has an instance "
					"variable with this name: %s",
					((PyObjCInstanceVariable*)value)->name);
				goto error_cleanup;
			}

			ivar_count ++;

			if (((PyObjCInstanceVariable*)value)->isSlot) {
				item_size = sizeof(PyObject**);
			} else {
				item_size = PyObjCRT_SizeOfType(
					((PyObjCInstanceVariable*)value)->type);
			}
			if (item_size == -1) goto error_cleanup;
			ivar_size += item_size;

		} else if (PyObjCSelector_Check(value)) {
			PyObjCSelector* sel = (PyObjCSelector*)value;
			PyObjCRT_Method_t        meth;

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

		} else if (
				PyMethod_Check(value) 
			     || PyFunction_Check(value) 
			     || PyObject_TypeCheck(value, &PyClassMethod_Type)){

			PyObject* pyname;
			char*     ocname;
			pyname = key;
			if (pyname == NULL) continue;

			ocname = PyString_AS_STRING(pyname);
			if (ocname[0] == '_' && ocname[1] == '_') {
				/* Skip special methods */
				continue;
			}

			value = PyObjCSelector_FromFunction(
					pyname,
					value,
					py_superclass,
					protocols);
			if (value == NULL) goto error_cleanup;

			if (!PyObjCSelector_Check(value)) {
				Py_DECREF(value);
				continue;
			}

			((PyObjCSelector*)value)->sel_class = &new_class->class;

			if (PyDict_SetItem(class_dict, key, value) < 0) {
				Py_DECREF(value); value = NULL;
				goto error_cleanup;
			}
			if (PyObjCSelector_IsClassMethod(value)) {
				meta_method_count++;
			} else {
				method_count++;
			}
			Py_DECREF(value); value = NULL;
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
		method_list = PyObjCRT_AllocMethodList(method_count);

		if (method_list == NULL) {
			PyErr_NoMemory();
			goto error_cleanup;
		}
	}

	if (meta_method_count == 0) {
		meta_method_list = NULL;
		
	} else {
		meta_method_list = PyObjCRT_AllocMethodList(meta_method_count);

		if (meta_method_list == NULL) {
			PyErr_NoMemory();
			goto error_cleanup;
		}
	}


	/* And fill the method_lists and ivar_list */
	ivar_size = super_class->instance_size;

	if (first_python_gen) {
		/* Our parent is a pure Objective-C class, add our magic
		 * methods and variables 
		 */
		 
		PyObjCRT_Method_t meth;
		PyObject* sel;
		IMP closure;
		PyObjCMethodSignature* methinfo;

#		define METH(pyname, selector, types, imp) 		\
		        methinfo = PyObjCMethodSignature_FromSignature(types); \
			if (methinfo == NULL) goto error_cleanup; \
			closure = PyObjCFFI_MakeClosure(methinfo, imp, \
					super_class); \
			PyObjCMethodSignature_Free(methinfo); \
			if (closure == NULL) goto error_cleanup; \
			meth = method_list->method_list + 		\
				method_list->method_count++;		\
			PyObjCRT_InitMethod(meth, selector, types, (IMP)closure); \
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
			"v@:@@",
			object_method_takeStoredValue_forKey_);
		METH(
			"takeValue_forKey_",
			@selector(takeValue:forKey:),
			"v@:@@",
			object_method_takeValue_forKey_);
		METH(
			"setValue_forKey_",
			@selector(setValue:forKey:),
			"v@:@@",
			object_method_takeValue_forKey_);
#undef		METH
	}

	for (i = 0; i < key_count; i++) {
		key = PyList_GetItem(key_list, i);
		if (key == NULL) {
			PyErr_SetString(PyObjCExc_InternalError,
				"PyObjCClass_BuildClass: "
				"Cannot fetch key in keylist");
			goto error_cleanup;
		}

		value = PyDict_GetItem(class_dict, key);
		if (value == NULL)  {
			PyErr_SetString(PyObjCExc_InternalError,
				"PyObjCClass_BuildClass: "
				"Cannot fetch item in keylist");
			goto error_cleanup;
		}

		if (PyObjCInstanceVariable_Check(value)) {
			PyObjCRT_Ivar_t var;

			var = ivar_list->ivar_list + ivar_list->ivar_count;
			ivar_list->ivar_count++;

			var->ivar_name = PyObjCUtil_Strdup(
				((PyObjCInstanceVariable*)value)->name);
			if (var->ivar_name == NULL) goto error_cleanup;
			var->ivar_offset = ivar_size;

			/* XXX: Add alignment! */

			if (((PyObjCInstanceVariable*)value)->isSlot) {
				var->ivar_type = "^v";
				item_size = sizeof(PyObject**);
			} else {
				var->ivar_type = PyObjCUtil_Strdup(((PyObjCInstanceVariable*)value)->type);
				if (var->ivar_type == NULL) goto error_cleanup;
				item_size = PyObjCRT_SizeOfType(var->ivar_type);
			}

			if (item_size == -1) goto error_cleanup;
			ivar_size += item_size;

		} else if (PyObjCSelector_Check(value)) {
			PyObjCSelector* sel = (PyObjCSelector*)value;
			PyObjCRT_Method_t        meth;
			int           is_override = 0;
			struct objc_method_list* lst;

			if (sel->sel_flags & PyObjCSelector_kCLASS_METHOD) {
				meth = class_getClassMethod(super_class,
					sel->sel_selector);
				if (meth) is_override = 1;
				lst = meta_method_list;
			} else {
				meth = class_getInstanceMethod(super_class,
					sel->sel_selector);
				if (meth) is_override = 1;
				lst = method_list;
			}

			meth = lst->method_list + lst->method_count;
		
			if (is_override) {
				PyObjCRT_InitMethod(
					meth, 
					sel->sel_selector, 
					sel->sel_signature,
					PyObjC_MakeIMP(super_class, value, value)
				);
			} else {
				PyObjCRT_InitMethod(
					meth, 
					sel->sel_selector, 
					sel->sel_signature,
					PyObjC_MakeIMP(nil, value, value)
				);
			}

			if (meth->method_imp == NULL) {
				goto error_cleanup;
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

	i = PyObjCRT_SetupClass(
		&new_class->class, 
		&new_class->meta_class, 
		name,
		super_class,
		root_class,
		ivar_size, ivar_list
		);
	if (i < 0) {
		goto error_cleanup;
	}

	if (method_list) {
		PyObjCRT_ClassAddMethodList(
			&(new_class->class), 
			method_list);
		method_list = NULL;
	}
	if (meta_method_list) {
		PyObjCRT_ClassAddMethodList(
			&(new_class->meta_class), 
			meta_method_list);
		meta_method_list = NULL;
	}

	Py_XDECREF(py_superclass); py_superclass = NULL;

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
		PyObjCRT_ClearClass(&(new_class->class));
		PyObjCRT_ClearClass(&(new_class->meta_class));
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
free_ivars(id self, PyObject* volatile cls )
{
	/* Free all instance variables introduced through python */
	volatile PyObjCRT_Ivar_t var;

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
		volatile int       i;
		int len;

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
				NS_DURING
					[*(id*)(((char*)self) + var->ivar_offset) release];

				NS_HANDLER
					// FIXME: I don't like this but we must
					// do something...
					NSLog(@"ignoring exception %@ in destructor",
						localException);

				NS_ENDHANDLER
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
static void 
object_method_dealloc(
		ffi_cif* cif __attribute__((__unused__)),
		void* retval __attribute__((__unused__)),
		void** args,
		void* userdata)
{
	id self = *(id*)(args[0]);
	SEL _meth = *(SEL*)(args[1]);

	struct objc_super super;
	PyObject* obj;
	PyObject* delmethod;
	PyObject* cls;
	PyObject* ptype, *pvalue, *ptraceback;

	PyObjC_BEGIN_WITH_GIL

		PyErr_Fetch(&ptype, &pvalue, &ptraceback);

		CHECK_MAGIC(GETISA(self));
		cls = PyObjCClass_New(GETISA(self));
		if (!PyObjCClass_HasPythonImplementation(cls)) {
			printf("-dealloc substitute called for pure ObjC "
			       "class\n");
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

	PyObjC_END_WITH_GIL

	super.class = (Class)userdata;
	RECEIVER(super) = self;

	objc_msgSendSuper(&super, _meth);
}

/* -respondsToSelector: */
static void 
object_method_respondsToSelector(
		ffi_cif* cif __attribute__((__unused__)),
		void* retval,
		void** args,
		void* userdata)
{
	id self = *(id*)args[0];
	SEL _meth = *(SEL*)args[1];
	SEL aSelector = *(SEL*)args[2];
	int* pres = (int*)retval; // Actually BOOL.

	struct objc_super super;
        PyObject* pyself;
	PyObject* pymeth;

	PyObjC_BEGIN_WITH_GIL
		/* First check if we respond */
		pyself = PyObjCObject_New(self);
		if (pyself == NULL) {
			*pres = NO;
			PyObjC_GIL_RETURNVOID;
		}
		pymeth = PyObjCObject_FindSelector(pyself, aSelector);
		Py_DECREF(pyself);
		if (pymeth) {
			*pres = YES;

			if (PyObjCSelector_Check(pymeth) && (((PyObjCSelector*)pymeth)->sel_flags & PyObjCSelector_kCLASS_METHOD)) {
				*pres = NO;	
			}
			
			Py_DECREF(pymeth);
			PyObjC_GIL_RETURNVOID;
		}
		PyErr_Clear();
	
	PyObjC_END_WITH_GIL

	/* Check superclass */
	super.class = (Class)userdata;
	RECEIVER(super) = self;

	*pres = (int)objc_msgSendSuper(&super, _meth, aSelector);
	return;
}

/* -methodSignatureForSelector */
static void
object_method_methodSignatureForSelector(
		ffi_cif* cif __attribute__((__unused__)),
		void* retval,
		void** args,
		void* userdata)
{
	id self = *(id*)args[0];
	SEL _meth = *(SEL*)args[1];
	SEL aSelector = *(SEL*)args[2];

	struct objc_super  super;
        PyObject*          pyself;
	PyObject*          pymeth;
	NSMethodSignature** presult = (NSMethodSignature**)retval;

	*presult = nil;

	super.class = (Class)userdata;
	RECEIVER(super) = self;

	NS_DURING
		*presult = objc_msgSendSuper(&super, _meth, aSelector);
	NS_HANDLER
		*presult = nil;
	NS_ENDHANDLER

	if (*presult != nil) {
		return;
	}

	PyObjC_BEGIN_WITH_GIL
		pyself = PyObjCObject_New(self);
		if (pyself == NULL) {
			PyErr_Clear();
			PyObjC_GIL_RETURNVOID;
		}

		pymeth = PyObjCObject_FindSelector(pyself, aSelector);
		if (!pymeth) {
			Py_DECREF(pyself);
			PyErr_Clear();
			PyObjC_GIL_RETURNVOID;
		}
	
	PyObjC_END_WITH_GIL

	NS_DURING
		*presult =  [NSMethodSignature signatureWithObjCTypes:(
				(PyObjCSelector*)pymeth)->sel_signature];
	NS_HANDLER
		PyObjC_BEGIN_WITH_GIL
			Py_DECREF(pymeth);
			Py_DECREF(pyself);

		PyObjC_END_WITH_GIL
		[localException raise];
	NS_ENDHANDLER

	PyObjC_BEGIN_WITH_GIL
		Py_DECREF(pymeth);
		Py_DECREF(pyself);

	PyObjC_END_WITH_GIL

}

/* -forwardInvocation: */
static void
object_method_forwardInvocation(
		ffi_cif* cif __attribute__((__unused__)),
		void* retval __attribute__((__unused__)),
		void** args,
		void* userdata)
{
	id self = *(id*)args[0];
	SEL _meth = *(SEL*)args[1];
	NSInvocation* invocation = *(NSInvocation**)args[2];
	SEL theSelector;

	PyObject*	arglist;
	PyObject* 	result;
	PyObject*       v;
	int		isAlloc;
	int             i;
	int 		len;
	PyObjCMethodSignature* signature;
	/*char		   argbuf[1024]; */
	const char* 		type;
	void* argbuf = NULL;
	int  err;
	int   arglen;
	PyObject* pymeth;
	PyObject* pyself;
	volatile int have_output = 0;
	PyGILState_STATE state = PyGILState_Ensure();

	pyself = PyObjCObject_New(self);
	if (pyself == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}


	NS_DURING
		theSelector = [invocation selector];
	NS_HANDLER
		PyGILState_Release(state);
		[localException raise];

		/* Avoid compiler warnings */
		theSelector = @selector(init);

	NS_ENDHANDLER

	pymeth = PyObjCObject_FindSelector(pyself, theSelector);

	if ((pymeth == NULL) || PyObjCNativeSelector_Check(pymeth)) {
		struct objc_super super;

		if (pymeth == NULL) {
			PyErr_Clear();
		}

		Py_XDECREF(pymeth);
		Py_XDECREF(pyself);

		super.class = (Class)userdata;
		RECEIVER(super) = self;
		PyGILState_Release(state);
		objc_msgSendSuper(&super, _meth, invocation);
		return;
	}


	signature = PyObjCMethodSignature_FromSignature(
		PyObjCSelector_Signature(pymeth));
	len = signature->nargs;

	Py_XDECREF(pymeth); pymeth = NULL;

	arglist = PyList_New(1);
	if (arglist == NULL) {
		PyObjCMethodSignature_Free(signature);
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}

	PyList_SET_ITEM(arglist, 0, pyself);
	pyself = NULL;

	for (i = 2; i < len; i++) {
		type = signature->argtype[i];
		arglen = PyObjCRT_SizeOfType(type);

		if (arglen == -1) {
			Py_DECREF(arglist);
			PyObjCMethodSignature_Free(signature);
			PyObjCErr_ToObjCWithGILState(&state);
			return;
		}

		argbuf = PyMem_Malloc(arglen+64);
		
		[invocation getArgument:argbuf atIndex:i];

		switch (*type) {
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
			PyMem_Free(argbuf); argbuf = NULL;
			continue;
		default:
			v = pythonify_c_value(type, argbuf);
		}
		PyMem_Free(argbuf); argbuf = NULL;

		if (v == NULL) {
			Py_DECREF(arglist);
			PyObjCMethodSignature_Free(signature);
			PyObjCErr_ToObjCWithGILState(&state);
			return;
		}

		if (PyList_Append(arglist, v) < 0) {
			Py_DECREF(arglist);
			PyObjCMethodSignature_Free(signature);
			PyObjCErr_ToObjCWithGILState(&state);
			return;
		}
	}

	v = PyList_AsTuple(arglist);
	if (v == NULL) {
		Py_DECREF(arglist);
		PyObjCMethodSignature_Free(signature);
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}
	Py_DECREF(arglist);
	arglist = v; v = NULL;

	result = PyObjC_CallPython(self, theSelector, arglist, &isAlloc);
	Py_DECREF(arglist);
	if (result == NULL) {
		PyObjCMethodSignature_Free(signature);
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}

	type = signature->rettype;
	arglen = PyObjCRT_SizeOfType(type);

	if (arglen == -1) {
		PyObjCMethodSignature_Free(signature);
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}

	if (!have_output) {
		if (*type  != _C_VOID && *type != _C_ONEWAY) {
			argbuf = PyMem_Malloc(arglen+64);

			err = depythonify_c_value(type, result, argbuf);
			if (err == -1) {
				PyMem_Free(argbuf);
				PyObjCMethodSignature_Free(signature);
				PyObjCErr_ToObjCWithGILState(&state);
				return;
			}
			if (isAlloc && *type == _C_ID) {
				[(*(id*)argbuf) retain];
			}
			[invocation setReturnValue:argbuf];
			PyMem_Free(argbuf);
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
				type = signature->argtype[i];

				if (arglen == -1) {
					PyObjCMethodSignature_Free(signature);
					PyObjCErr_ToObjCWithGILState(&state);
					return;
				}

				switch (*type) {
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
					PyObjCMethodSignature_Free(signature);
					PyObjCErr_ToObjCWithGILState(&state);
					return;
				}
				if (result->ob_refcnt == 1 && type[0] == _C_ID) {
					/* make sure return value doesn't die before
					 * the caller can get its hands on it.
					 */
					[[*(id*)ptr retain] autorelease];
				}

				/* We have exactly 1 output argument */
				break;

			}

			PyObjCMethodSignature_Free(signature);
			Py_DECREF(result);
			PyGILState_Release(state);
			return;
		}

		if (*type != _C_VOID) {
			if (!PyTuple_Check(result) 
			     || PyTuple_Size(result) != have_output+1) {
				PyErr_Format(PyExc_TypeError,
					"%s: Need tuple of %d arguments as result",
					PyObjCRT_SELName(theSelector),
					have_output+1);
				Py_DECREF(result);
				PyObjCMethodSignature_Free(signature);
				PyObjCErr_ToObjCWithGILState(&state);
				return;
			}
			idx = 1;
			real_res = PyTuple_GET_ITEM(result, 0);

			argbuf = PyMem_Malloc(arglen+64);

			err = depythonify_c_value(type, real_res, argbuf);
			if (err == -1) {
				PyObjCMethodSignature_Free(signature);
				PyObjCErr_ToObjCWithGILState(&state);
				PyMem_Free(argbuf);
				return;
			}
			if (isAlloc && *type == _C_ID) {
				[(*(id*)argbuf) retain];
			}
			[invocation setReturnValue:argbuf];
			PyMem_Free(argbuf);

		} else {
			if (!PyTuple_Check(result) 
			     || PyTuple_Size(result) != have_output) {
				PyErr_Format(PyExc_TypeError,
					"%s: Need tuple of %d arguments as result",
					PyObjCRT_SELName(theSelector),
					have_output);
				PyObjCMethodSignature_Free(signature);
				Py_DECREF(result);
				PyObjCErr_ToObjCWithGILState(&state);
				return;
			}
			idx = 0;
		}


		for (i = 2; i < len;i++) {
			void* ptr;
			type = signature->argtype[i];

			if (arglen == -1) {
				PyObjCMethodSignature_Free(signature);
				PyObjCErr_ToObjCWithGILState(&state);
				return;
			}

			switch (*type) {
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
				PyObjCMethodSignature_Free(signature);
				PyObjCErr_ToObjCWithGILState(&state);
				return;
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
	PyObjCMethodSignature_Free(signature);
	PyGILState_Release(state);
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

	pyself = pythonify_c_value(@encode(id), &self);
	if (pyself == NULL) {
		return NULL;
	}
	
	if (PyObjCClass_Check(pyself)) {
		pymeth = PyObjCClass_FindSelector(pyself, selector);
	} else {
		pymeth = PyObjCObject_FindSelector(pyself, selector);
	}
	if (pymeth == NULL) {
		Py_DECREF(pyself);
		return NULL;
	}

	if (NULL != ((PyObjCSelector*)pymeth)->sel_self) {
		/* The selector is a bound selector, we didn't expect that...*/
		PyObject* arg_self;

		arg_self = PyTuple_GET_ITEM(arglist, 0);
		if (arg_self == NULL) {
			return NULL;
		}
		if (arg_self != ((PyObjCSelector*)pymeth)->sel_self) {
			PyErr_SetString(PyExc_TypeError,
				"PyObjC_CallPython called with 'self' and "
				"a method bound to another object");
			return NULL;
		}

		arglist = PyTuple_GetSlice(arglist, 1, PyTuple_Size(arglist));
		if (arglist == NULL) {
			return NULL;
		}
	} else {
		Py_INCREF(arglist);
	}

	if (isAlloc != NULL) {
		*isAlloc = PyObjCSelector_DonatesRef(pymeth);
	}


	result = PyObject_Call(pymeth, arglist, NULL);
	Py_DECREF(arglist);
	Py_DECREF(pymeth);
	Py_DECREF(pyself);

	if (result == NULL) {
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
	PyObject* cls = PyObjCClass_New(GETISA(self));
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
			PyObject* ps;

			Py_DECREF(att);

			ps = PyObjCObject_New(self);
			if (ps == NULL) {
				PyErr_Clear();
				return -1;
			}

			val = PyObject_GetAttrString(
				ps,
				(char*)[key cString]);
			Py_DECREF(ps);
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
			PyObject* ps = PyObjCObject_New(self);
			if (ps == NULL) {
				PyErr_Clear();
				return -1;
			}
			val = PyObject_GetAttrString(
				ps,
				(char*)[key cString]);
			Py_DECREF(ps);
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
	PyObject* cls = PyObjCClass_New(GETISA(self));
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
			PyObject* ps;

			Py_DECREF(att);

			ps = PyObjCObject_New(self);
			if (ps == NULL) {
				PyErr_Clear();
				return -1;
			}

			val = PyObject_CallMethod(
				ps,
				(char*)[key cString],
				NULL);
			Py_DECREF(ps);
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

/* 
 * Support for NSKeyValueObserving on MacOS X 10.3 and later.
 *
 * XXX: It's probably better to detect this at runtime.
 * XXX2: This is not correct, should also call 'willChangeValueForKey:'!
 */
#if defined(MACOSX) && MAC_OS_X_VERSION_MAX_ALLOWED >= MAC_OS_X_VERSION_10_3
#   define WILL_CHANGE(self, key) [(NSObject*)(self) willChangeValueForKey:(key)]	
#   define DID_CHANGE(self, key) [(NSObject*)(self) didChangeValueForKey:(key)]	
#else
#   define WILL_CHANGE(self, key) ((void)0)
#   define DID_CHANGE(self, key) ((void)0)
#endif


static int
setAttribute(id self, NSString* key, id value)
{
	PyObject* cls = PyObjCClass_New(GETISA(self));
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
				return 0;
			}


			WILL_CHANGE(self, key);
			r = PyDict_SetItemString(*dictptr, 
				(char*)[key cString], val);
			DID_CHANGE(self, key);

			Py_DECREF(val);
			return 0;
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
				return 0;
			}

			WILL_CHANGE(self, key);
			r = PyObject_SetAttrString(
				PyObjCObject_New(self),
				(char*)[key cString], val);
			DID_CHANGE(self, key);
			Py_DECREF(val);
			return 0;
		}
		Py_DECREF(att);
	}

	return -1;
}

static int
setAccessor(id self, NSString* key, id value)
{
	PyObject* cls = PyObjCClass_New(GETISA(self));
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
				return 0;
			}

			WILL_CHANGE(self, key);
			att = PyObject_CallMethod(
				PyObjCObject_New(self),
				(char*)[key cString], "O", val);
			DID_CHANGE(self, key);
			Py_XDECREF(att);
			Py_DECREF(val);
			return 0;
		}
		Py_DECREF(att);
	}

	return -1;
}

static void
object_method_storedValueForKey_(
		ffi_cif* cif __attribute__((__unused__)),
		void* retval,
		void** args,
		void* userdata)
{
	id self = *(id*)args[0];
	SEL _meth = *(SEL*)args[1];
	NSString* key = *(NSString**)args[2];

	id* presult = (id*)retval;
	int r;
	struct objc_super super;

	PyGILState_STATE state = PyGILState_Ensure();

#define TRY_GETMETHOD(method, format, keyexp) { \
	r = method(self, \
			[NSString stringWithFormat: format, keyexp], presult); \
	if (r == 0) { \
		PyGILState_Release(state); \
		return; \
	} \
}

	TRY_GETMETHOD(getAccessor, @"get_%@", key);
	TRY_GETMETHOD(getAttribute, @"%@", key);
	TRY_GETMETHOD(getAccessor, @"_get_%@", key);
	TRY_GETMETHOD(getAttribute, @"_%@", key);

#undef TRY_GETMETHOD

	PyGILState_Release(state);

	/* Call super */
	super.class = (Class)userdata;
	RECEIVER(super) = self;
	*presult = objc_msgSendSuper(&super, _meth, key);
}

static void
object_method_valueForKey_(
		ffi_cif* cif __attribute__((__unused__)),
		void* retval,
		void** args,
		void* userdata)
{
	int r;
	id self = *(id*)args[0];
	SEL _meth = *(SEL*)args[1];
	NSString* key = *(NSString**)args[2];

	id* presult = (id*)retval;
	struct objc_super super;
	PyGILState_STATE state = PyGILState_Ensure();

#define TRY_GETMETHOD(method, format, keyexp) { \
	r = method(self, \
			[NSString stringWithFormat: format, keyexp], presult); \
	if (r == 0) { \
		PyGILState_Release(state); \
		return; \
	} \
}

	TRY_GETMETHOD(getAccessor, @"get_%@", key);
	TRY_GETMETHOD(getAccessor, @"get%@", [key capitalizedString]);
	TRY_GETMETHOD(getAttribute, @"%@", key);
	TRY_GETMETHOD(getAccessor, @"_get_%@", key);
	TRY_GETMETHOD(getAccessor, @"_get%@", [key capitalizedString]);
	TRY_GETMETHOD(getAccessor, @"%@", key);
	TRY_GETMETHOD(getAccessor, @"_%@", key);
	TRY_GETMETHOD(getAttribute, @"_%@", key);

#undef TRY_GETMETHOD
	
	/* Call super */
	PyGILState_Release(state);
	super.class = (Class)userdata;
	RECEIVER(super) = self;
	*presult = objc_msgSendSuper(&super, _meth, key);
}


static void
object_method_takeStoredValue_forKey_(
		ffi_cif* cif __attribute__((__unused__)),
		void* retval __attribute__((__unused__)),
		void** args,
		void* userdata)
{
	id self = *(id*)args[0];
	SEL _meth = *(SEL*)args[1];
	id value = *(id*)args[2];
	NSString* key = *(NSString**)args[3];

	struct objc_super super;
	int r;
	PyGILState_STATE state = PyGILState_Ensure();


#define TRY_SETMETHOD(method, format, keyexp) { \
	r = method(self, \
		[NSString stringWithFormat:format, keyexp], value); \
	if (r == 0) { \
		if (PyErr_Occurred()) { \
			PyErr_Clear(); \
			PyGILState_Release(state); \
			[[NSException \
				exceptionWithName:@"NSUnknownKeyException" \
				reason:key userInfo:nil] raise]; \
			return; \
		} \
		PyGILState_Release(state); \
		return; \
	} \
}

	TRY_SETMETHOD(setAccessor, @"set_%@", key);
	TRY_SETMETHOD(setAccessor, @"set%@", [key capitalizedString]);
	TRY_SETMETHOD(setAttribute, @"%@", key);
	TRY_SETMETHOD(setAccessor, @"_set_%@", key);
	TRY_SETMETHOD(setAccessor, @"_set%@", [key capitalizedString]);
	TRY_SETMETHOD(setAttribute, @"_%@", key);

#undef TRY_SETMETHOD

	/* Call super */
	PyGILState_Release(state);
	NS_DURING
		super.class = (Class)userdata;
		RECEIVER(super) = self;
		(void)objc_msgSendSuper(&super, _meth, value, key);
	NS_HANDLER
		/* Parent doesn't know the key, try to create in the 
		 * python side, just like for plain python objects.
		 */
		if ([[localException name] isEqual:@"NSUnknownKeyException"]
#ifndef MACOSX
			/* This test is necessary on GNUstep */
			|| [[localException name] isEqual:@"NSInvalidArgumentException"]
#endif
			) {

			PyObject* selfObj;
			PyObject* val;

			state = PyGILState_Ensure();
			selfObj = PyObjCObject_New(self);
			val = pythonify_c_value(@encode(id), &value);
			if (val == NULL) {
				PyErr_Clear();
				PyGILState_Release(state);
				[localException raise];
			}

			r = PyObject_SetAttrString(selfObj, 
				(char*)[key cString],
				val);
			Py_DECREF(val);
			Py_DECREF(selfObj);
			if (r == -1) {
				PyErr_Clear();
				PyGILState_Release(state);
				[localException raise];
			}
			PyGILState_Release(state);
				
		} else {
			[localException raise];
		}
	NS_ENDHANDLER
}

static void
object_method_takeValue_forKey_(
		ffi_cif* cif __attribute__((__unused__)),
		void* retval __attribute__((__unused__)),
		void** args,
		void* userdata)
{
	id self = *(id*)args[0];
	SEL _meth = *(SEL*)args[1];
	id value = *(id*)args[2];
	NSString* key = *(NSString**)args[3];

	struct objc_super super;
	int r;
	PyGILState_STATE state = PyGILState_Ensure();

#define TRY_SETMETHOD(method, format, keyexp) { \
	r = method(self, \
		[NSString stringWithFormat:format, keyexp], value); \
	if (r == 0) { \
		if (PyErr_Occurred()) { \
			PyErr_Clear(); \
			PyGILState_Release(state); \
			[[NSException \
				exceptionWithName:@"NSUnknownKeyException" \
				reason:key userInfo:nil] raise]; \
			return; \
		} \
		PyGILState_Release(state); \
		return; \
	} \
}

	TRY_SETMETHOD(setAccessor, @"set_%@", key);
	TRY_SETMETHOD(setAccessor, @"set%@", [key capitalizedString]);
	TRY_SETMETHOD(setAttribute, @"%@", key);
	TRY_SETMETHOD(setAccessor, @"_set_%@", key);
	TRY_SETMETHOD(setAccessor, @"_set%@", [key capitalizedString]);
	TRY_SETMETHOD(setAttribute, @"_%@", key);

#undef TRY_SETMETHOD

	/* Call super */
	PyGILState_Release(state);
	NS_DURING
		super.class = (Class)userdata;
		RECEIVER(super) = self;
		(void)objc_msgSendSuper(&super, _meth, value, key);
	NS_HANDLER
		/* Parent doesn't know the key, try to create in the 
		 * python side, just like for plain python objects.
		 */
		if ([[localException name] isEqual:@"NSUnknownKeyException"] 
#ifndef MACOSX
				/* This test is necessary on GNUstep */
				|| [[localException name] isEqual:@"NSInvalidArgumentException"]
#endif
				) {
			PyObject* selfObj;
			PyObject* val;
			state = PyGILState_Ensure();
			selfObj = PyObjCObject_New(self);
			val = pythonify_c_value(@encode(id), &value);
			if (val == NULL) {
				PyErr_Clear();
				PyGILState_Release(state);
				[localException raise];
			}

			r = PyObject_SetAttrString(selfObj, 
				(char*)[key cString],
				val);
			Py_DECREF(val);
			Py_DECREF(selfObj);
			if (r == -1) {
				PyErr_Clear();
				PyGILState_Release(state);
				[localException raise];
			}
			PyGILState_Release(state);
				
		} else {
			[localException raise];
		}
	NS_ENDHANDLER
}

#if 0
 /* This will one day be the copyWithZone: for subclasses of classes that define
  * copyWithZone:. There's just one problem: how can we allow the user to
  * hook into this (e.g. the user must be able to override copyWithZone:
  * without introducing problems). 
  *
  * Luckily we can break existing code, that code is broken anyway :-)
  *
  * Why is this needed? In many cases the default copyWithZone: either doesn't
  * copy python slots, or it copies them without updating the reference count.
  * For __dict__ and values in __slots__ the second option is a serious 
  * problem: there is nothing the user can do to fix this (those values are 
  * PyObject*-s and there is no interface for changing their refcount from 
  * Python).  The only workaround: have '__slots__ = ()' in the class (e.g.
  * do NOT have additional instance variables).
  */

static void
object_method_copyWithZone_(
		ffi_cif* cif __attribute__((__unused__)),
		void* resp,
		void** args,
		void* userdata)
{
	id self = *(id*)args[0];
	id copy;
	SEL _meth = *(SEL*)args[1];
	NSZone* zone = *(NSZone**)args[2];
	struct copyWithZoneData* data = (PyObject*)userdata;

	struct objc_super super;
	int r;
	PyGILState_STATE state;
	PyObjCRT_Ivar_t var;

	/* Ask super to create a copy */

	super.class = data->class;
	RECEIVER(super) = self;
	copy = objc_msgSendSuper(&super, _meth, zone);

	if (copy == nil) {
		*(id*)resp = nil;
	}

	state = PyGILState_Ensure();

	/* Update the reference counts for slots/outlets */

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
				Py_XINCREF(*(PyObject**)(((char*)self) + 
					var->ivar_offset));
				*(PyObject**)(((char*)copy) + var->ivar_offset) =
					*(PyObject**)(((char*)self) + var->ivar_offset);
			} else {
				[*(id*)(((char*)self) + var->ivar_offset) retain];
				*(id*)(((char*)copy) + var->ivar_offset) = *(id*)(((char*)self) + var->ivar_offset);
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

	/* And at the end copy the dict */
	var = class_getInstanceVariable(PyObjCClass_GetClass(cls), "__dict__");
	if (var != NULL) {
		*(PyObject**)(((char*)copy) + var->ivar_offset) = 
			PyDict_Copy(
			    *(PyObject**)(((char*)self) + var->ivar_offset));

		if (*(PyObject**)(((char*)copy) + var->ivar_offset) == NULL) {
			[copy release];
			*(id*)resp = nil;
			PyObjCErr_ToObjCWithGILState(&state);
			return;
		}
	}
	
	PyGILState_Release(state);
	*(id*)resp = copy;
}

#endif
