/*
 * This file contains the code that is used to create proxy-classes for Python
 * classes in the objective-C runtime.
 */
#include <Python.h>
#include "pyobjc.h"
#include "objc_support.h"
#include <Foundation/NSInvocation.h>


/* We add 1 instance variable to hybrid objective-C/Python classes, this 
 * contains the reference to the python half of the class. Name should be 
 * not be used by Objective-C classes that are not managed by PyObjC... 
 */
static char pyobj_ivar[] = "__pyobjc_obj__";

/* List of instance variables, methods and class-methods that should not
 * be overridden from python
 */
static char* dont_override_methods[] = {
        pyobj_ivar,
	"alloc",
	"dealloc",
	"retain",
	"release",
	"autorelease",
	"retainCount",
	NULL
};

/* Special methods for Python subclasses of Objective-C objects */
static id class_method_alloc(id self, SEL sel);
static id class_method_allocWithZone(id self, SEL sel, NSZone* zone);

static id object_method_retain(id self, SEL sel);
static void object_method_release(id self, SEL sel);
static unsigned object_method_retainCount(id self, SEL sel);
static BOOL object_method_respondsToSelector(id self, SEL selector, 
	SEL aSelector);
static NSMethodSignature*  object_method_methodSignatureForSelector(id self, 
	SEL selector, SEL aSelector);
static void object_method_forwardInvocation(id self, SEL selector, 
	NSInvocation* invocation);
static PyObject* object_method__pyobjc_PythonObject__(id self, SEL selector);


/*
 * When we create a 'Class' we actually create the struct below. This allows
 * us to add some extra information to the class defintion.
 */
struct class_wrapper {
	struct objc_class  class;
	struct objc_class  meta_class;
	PyObject*          python_class;
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
 * Return wether the object is (partially) implemented in python
 */
int ObjC_HasPythonImplementation(id obj)
{
	if (obj == nil) return 0;
	
	return (class_getInstanceVariable(GETISA(obj), pyobj_ivar) != NULL);
}

/*
 * Get the python half of the implementation.
 *
 * Returns a borrowed reference.
 */
PyObject* ObjC_GetPythonImplementation(id obj)
{
	PyObject* pyobj = NULL;
	IVAR      var   = NULL;

	if (obj == nil) {
		ObjCErr_Set(ObjCExc_internal_error,
			"ObjC_GetPythonImplementation called for <nil>");
		return NULL;
	}

	var = object_getInstanceVariable(obj, pyobj_ivar, (void**)&pyobj);
	if (var == NULL) {
		ObjCErr_Set(ObjCExc_internal_error,
			"ObjC_GetPythonImplementation called for "
			"normal object of class %s",
			    GETISA(obj)->name);
		return NULL;
	}
	if (pyobj == NULL) {
		return Py_None;
	}

	return pyobj;
}

static int
ObjC_SetPythonImplementation(id obj, PyObject* newval)
{
	IVAR      var   = NULL;

	if (obj == nil) {
		ObjCErr_Set(ObjCExc_internal_error,
			"ObjC_GetPythonImplementation called for <nil>");
		return -1;
	}

	var = class_getInstanceVariable(GETISA(obj), pyobj_ivar);
	if (var == NULL) {
		ObjCErr_Set(ObjCExc_internal_error,
			"ObjC_SetPythonImplementation called for "
			"normal object of class %s",
			    GETISA(obj)->name);
		return -1;
	}
	*(PyObject**)(((char*)obj)+var->ivar_offset) = newval;
	return 0;
}

/*
 * Last step of the construction a python subclass of an objective-C class.
 *
 * Set reference to the python half in the objective-C half of the class.
 *
 * Return 0 on success, -1 on failure.
 */
int ObjCClass_SetClass(Class objc_class, PyObject* py_class)
{
	if (objc_class == nil) {
		ObjCErr_Set(ObjCExc_internal_error, 
			"Trying to set class of <nil>\n", objc_class->name);
		return -1;
	}
	if (class_getInstanceVariable(objc_class, pyobj_ivar) == NULL) {
		ObjCErr_Set(ObjCExc_internal_error, 
			"Trying to set class of non-python %s", 
			objc_class->name);
		return -1;
	}
	if (py_class == NULL || !ObjCClass_Check(py_class)) {
		ObjCErr_Set(ObjCExc_internal_error,
			"Trying to set class to of %s to invalid value "
			"(type %s instead of %s)",
			objc_class->name, py_class->ob_type->tp_name,
			ObjCClass_Type.tp_name);
		return -1;
	}
	if (((struct class_wrapper*)objc_class)->python_class != NULL) {
		ObjCErr_Set(ObjCExc_internal_error,
			"Trying to set update PythonClass of %s",
			objc_class->name);
		return -1;
	}


	((struct class_wrapper*)objc_class)->python_class = py_class;
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
void ObjCClass_UnbuildClass(Class objc_class)
{
	struct class_wrapper* wrapper = (struct class_wrapper*)objc_class;

	if (objc_class == nil) {
		ObjCErr_Set(ObjCExc_internal_error, 
		"Trying to unregister class <nil>");
		return;
	}
	if (class_getInstanceVariable(objc_class, pyobj_ivar) == NULL) {
		ObjCErr_Set(ObjCExc_internal_error, 
			"Trying to unregister class %s, but it is not "
			"python based", 
			objc_class->name);
		return;
	}
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

	if (!PyList_Check(protocols)) {
		ObjCErr_Set(ObjCExc_internal_error,
			"Protocol-list is not a list");
		return NULL;
	}

	len = PyList_Size(protocols);
	for (i = 0; i < len; i++) {
		PyObject* p;
		PyObject* info;
	
		p = PyList_GetItem(protocols, i);
		if (p == NULL) {
			PyErr_Clear();
			continue;
		}
		if (!ObjCInformalProtocol_Check(p)) continue;

		info = ObjCIPFindInfo(p, selector);
		if (info != NULL) {
			return ObjCSelector_Signature(info);
		}
	}
	return NULL;
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
Class ObjCClass_BuildClass(Class super_class,  PyObject* protocols,
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
	py_superclass = ObjCClass_New(super_class);
	if (py_superclass == NULL) return NULL;


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


	if (class_getInstanceVariable(super_class, pyobj_ivar) == 0) {
		first_python_gen = 1;

		/* 
		 * This class has a super_class that is pure objective-C
		 * We'll add some instance variables and methods that are
		 * needed for the correct functioning of the class. 
		 *
		 * See the code below the next loop.
		 */
		ivar_count        += 1;
		meta_method_count += 2; 
		method_count      += 8;
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

		if (ObjCIvar_Check(value)) {
			if (class_getInstanceVariable(super_class, 
					((ObjCIvar*)value)->name) != NULL) {
				ObjCErr_Set(ObjCExc_error,
					"Cannot replace instance variable %s",
					((ObjCIvar*)value)->name);
				goto error_cleanup;
			}

			ivar_count ++;
			item_size = objc_sizeof_type(((ObjCIvar*)value)->type);
			if (item_size == -1) goto error_cleanup;
			ivar_size += item_size;

		} else if (ObjCSelector_Check(value)) {
			ObjCSelector* sel = (ObjCSelector*)value;
			METHOD        meth;

			if (sel->sel_flags & ObjCSelector_kCLASS_METHOD) {
				meth = class_getClassMethod(super_class,
					sel->sel_selector);
				if (meth) {
					meta_method_count ++;
				}


			} else {
				meth = class_getInstanceMethod(super_class,
					sel->sel_selector);
				method_count ++;
			}

		} else if (PyMethod_Check(value) || PyFunction_Check(value)) {
			PyObject* pyname;
			char*     name;
			SEL	  selector;
			METHOD    meth;
			int       is_class_method = 0;

			pyname = key;
			if (pyname == NULL) continue;

			name = PyString_AS_STRING(pyname);
			if (name[0] == '_' && name[1] == '_') {
				/* Skip special methods */
				continue;
			}

			selector = ObjCSelector_DefaultSelector(name);

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
				PyObject* super_sel = ObjCClass_FindSelector(
					py_superclass, selector);
				if (!super_sel) goto error_cleanup;

				value = ObjCSelector_New(
					value, 
					selector, 
					ObjCSelector_Signature(super_sel),
					is_class_method);
				Py_DECREF(super_sel);
			} else {
				char* signature;

				signature = find_protocol_signature(
					protocols, selector);
				value = ObjCSelector_New(
					value, 
					selector, 
					signature,
					0);
			}
			if (value == NULL) goto error_cleanup;
				
			if (PyDict_SetItem(class_dict, key, value) < 0) {
				goto error_cleanup;
			}
			Py_DECREF(value); value = NULL;
			method_count++;
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

	/* Create new_class here, just in case we are the first python
	 * generation, in which case we need to use new_class (it must just
	 * be there, it doesn't have to be initialized)
	 */
	new_class = calloc(1, sizeof(struct class_wrapper));
	if (new_class == NULL) {
		goto error_cleanup;
	}

	ivar_size = super_class->instance_size;

	if (first_python_gen) {
		/* Our parent is a pure Objective-C class, add our magic
		 * methods and variables 
		 */
		 
		IVAR var = ivar_list->ivar_list;
		METHOD meth;
		PyObject* sel;
		ivar_list->ivar_count++;

		var->ivar_name = pyobj_ivar;
		var->ivar_type = "^v";
		var->ivar_offset = ivar_size;
		ivar_size += sizeof(void*);

		/* XXX: Make these global lists instead of macros */

#		define META_METH(pyname, selector, types, imp) 		\
			meth = meta_method_list->method_list + 		\
				meta_method_list->method_count++;	\
			meth->method_name = selector;			\
			meth->method_types = types;			\
			meth->method_imp = (IMP)imp;			\
			sel = ObjCSelector_NewNative(&new_class->class, \
				selector,  types, 1);			\
			if (sel == NULL) goto error_cleanup;		\
			PyDict_SetItemString(class_dict, pyname, sel);	\
			Py_DECREF(sel)

#		define METH(pyname, selector, types, imp) 		\
			meth = method_list->method_list + 		\
				method_list->method_count++;		\
			meth->method_name = selector;			\
			meth->method_types = types;			\
			meth->method_imp = (IMP)imp;			\
			sel = ObjCSelector_NewNative(&new_class->class, \
				selector,  types, 0);			\
			if (sel == NULL) goto error_cleanup;		\
			PyDict_SetItemString(class_dict, pyname, sel);	\
			Py_DECREF(sel)


		META_METH("alloc", @selector(alloc), "@@:", class_method_alloc);
		META_METH("allocWithZone_", @selector(allocWithZone:), "@@:^{_NSZone=}", class_method_allocWithZone);

		METH("retain", @selector(retain), "@@:", object_method_retain);
		METH("release", @selector(release), "v@:", object_method_release);
		METH("retainCount", @selector(retainCount), "I@:", object_method_retainCount);
		METH("respondsToSelector_", @selector(respondsToSelector:), "c@::", 
			object_method_respondsToSelector);
		METH("methodSignatureForSelector_", @selector(methodSignatureForSelector:), "@@::", 
			object_method_methodSignatureForSelector);
		METH("forwardInvocation_", @selector(forwardInvocation:), "v@:@", 
			object_method_forwardInvocation);
		METH("__pyobjc_PythonObject__", @selector(__pyobjc_PythonObject__), "^{PythonObject}@:", object_method__pyobjc_PythonObject__);
#undef		METH
#undef		META_METH
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

		if (ObjCIvar_Check(value)) {
			IVAR var;

			var = ivar_list->ivar_list + ivar_list->ivar_count;
			ivar_list->ivar_count++;

			var->ivar_name = ((ObjCIvar*)value)->name;
			var->ivar_type = ((ObjCIvar*)value)->type;
			var->ivar_offset = ivar_size;

			item_size = objc_sizeof_type(var->ivar_type);
			if (item_size == -1) goto error_cleanup;
			ivar_size += item_size;

		} else if (ObjCSelector_Check(value)) {
			ObjCSelector* sel = (ObjCSelector*)value;
			METHOD        meth;
			int           is_override = 0;
			struct objc_method_list* lst;

			if (sel->sel_flags & ObjCSelector_kCLASS_METHOD) {
				meth = class_getClassMethod(super_class,
					sel->sel_selector);
				if (!meth) continue;
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
					ObjC_FindIMPForSignature(sel->sel_signature);

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

	new_class->python_class = NULL;
	new_class->class.METHODLISTS = NULL;
	new_class->meta_class.METHODLISTS = NULL;
	GETISA(&new_class->class) = &new_class->meta_class;
	new_class->class.info = CLS_CLASS;
	new_class->meta_class.info = CLS_META;

	new_class->class.name = strdup(name);
	new_class->meta_class.name = new_class->class.name;

#ifndef GNU_RUNTIME
	new_class->class.METHODLISTS = 
		calloc(1, sizeof(struct objc_method_list*));
	if (new_class->class.METHODLISTS == NULL) goto error_cleanup;
	
	new_class->class.METHODLISTS[0] = NULL;

	new_class->meta_class.METHODLISTS = 
		calloc(1, sizeof(struct objc_method_list*));
	if (new_class->meta_class.METHODLISTS == NULL) goto error_cleanup;
	new_class->meta_class.METHODLISTS[0] = NULL;
#endif

	new_class->class.super_class = super_class;
	new_class->meta_class.super_class = GETISA(super_class);
	GETISA(&new_class->meta_class) = GETISA(root_class);

	new_class->class.instance_size = ivar_size;
	new_class->class.ivars = ivar_list;

	/* Be explicit about clearing data, should not be necessary with
	 * 'calloc'
	 */
#ifndef GNU_RUNTIME
	new_class->class.cache = NULL;
	new_class->meta_class.cache = NULL;
#endif

	new_class->class.protocols = NULL;
	new_class->meta_class.protocols = NULL;

	if (method_list) {
		class_addMethods(&(new_class->class), method_list);
	}
	if (meta_method_list) {
		class_addMethods(&(new_class->meta_class), meta_method_list);
	}

	Py_XDECREF(py_superclass);

	/* 
	 * NOTE: Class is not registered yet, we do that as lately as possible
	 * because it is impossible to remove the registration from the
	 * objective-C runtime (at least on MacOS X).
	 */
	return (Class)new_class;

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
 * These are added to the new Objective-C class by  ObjCClass_BuildClass (but
 * only if the super_class is a 'pure' objective-C klass)
 *
 * The protocol for objc-python object-clusters is:
 * - +alloc calls [super alloc], then creates a new Python 'wrapper' for it
 *   (ObjCObject_New) and sets a pointer to that wrapper object in the 
 *   correct instance variable of the new object
 * - +allocWithZone: is implemented in a simular manner.
 * - the references from the python-side to the objective-c side and back
 *   do _not_ count in the reference-count of the cluster
 * - the reference-count is stored in the python-side
 * - deallocactie doen we eerst in python en dan in objective-C
 *
 * NOTE:
 * - These functions will be used as methods, but as far as the compiler
 *   knows these are normal functions. You cannot use [super call]s here.
 */

/*
 * +alloc
 */
static id class_method_alloc(id self, SEL sel)
{  
   /* NSObject documentation defines +alloc as 'allocWithZone:nil' */
   return class_method_allocWithZone(self, sel, NULL);
}


/* +allocWithZone: */
static id class_method_allocWithZone(id self, SEL sel, NSZone* zone)
{
   PyObject* pyclass;
   ObjCObject* pyobject;
   id          obj;
   struct objc_super super;

   pyclass = ((struct class_wrapper*)self)->python_class;

   super.class = GETISA(find_real_superclass((Class)self, 
   			@selector(allocWithZone:),
			class_getClassMethod, 
			(IMP)class_method_allocWithZone));
   RECEIVER(super) = self;

   obj = objc_msgSendSuper(&super, @selector(allocWithZone:), zone); 
   if (obj == nil) {
	   return nil;	
   }

   pyobject = (ObjCObject*)ObjCObject_New(obj);
   if (pyobject == NULL) {
       ObjCErr_ToObjC();
       return nil;
   }

   /* obj->__pyobjc_obj__ = pyobjct */ 
   if (ObjC_SetPythonImplementation(obj, (PyObject*)pyobject) == -1) {
       Py_DECREF(pyobject);
       ObjCErr_ToObjC();
       return nil;
   }
   return obj;
}

/* -__pyobjc_PythonObject__ */
static PyObject* object_method__pyobjc_PythonObject__(id self, SEL sel)
{
	PyObject* pyself;
	pyself = ObjC_GetPythonImplementation(self);
	Py_XINCREF(pyself);
	return pyself;
}

/* -retain */
static id object_method_retain(id self, SEL sel)
{
	PyObject* pyself;

	pyself = ObjC_GetPythonImplementation(self);

	if (pyself == Py_None) {
		struct objc_super super;
		
   		super.class = find_real_superclass(GETISA(self),
			@selector(retain), class_getInstanceMethod, 
			(IMP)object_method_retain);
		RECEIVER(super) = self;

		self = objc_msgSendSuper(&super, @selector(retain)); 
	} else if (pyself) {
		Py_INCREF(pyself);
	} else {
		PyErr_Clear();
	}

	return self;
}

/* -release */
static void object_method_release(id self, SEL sel)
{
	struct objc_super super;
	PyObject* obj;

	
	obj = ObjC_GetPythonImplementation(self);

	if (obj == NULL) {
		PyErr_Clear();
		return;
	} else if (obj == Py_None) {
	  super.class = find_real_superclass(GETISA(self),
			@selector(release), class_getInstanceMethod, 
			(IMP)object_method_release);
		RECEIVER(super) = self;

		self = objc_msgSendSuper(&super, @selector(release)); 
		return;
	}

	if (obj->ob_refcnt <= 0) {
		
		/* Remove reference to the Python object. We don't need it
		 * any more (because the ObjCObject code will remove it 
		 * when this function returns) and [super release] may 
		 * call back to us some time later on ([NSWindow release] in
		 * a seperator thread).
		 */
		if (ObjC_SetPythonImplementation(self, 0) == -1) {
		       ObjCErr_ToObjC();
		       return;
		}

		/* [super release] */
   		super.class = find_real_superclass(GETISA(self),
			@selector(release), class_getInstanceMethod, 
			(IMP)object_method_release);
		RECEIVER(super) = self;

		self = objc_msgSendSuper(&super, @selector(release)); 
		return;

	} else {
		/* If the reference count is 1, Py_DECREF causes a call
		 * to object_dealloc, which in turn calls back to us
		 * with a reference-count of 0.
		 */
		Py_DECREF(obj);
		return;
	} 

	return;
}

/* -retainCount */
static unsigned object_method_retainCount(id self, SEL sel)
{
	PyObject* obj = ObjC_GetPythonImplementation(self);

	if (obj == Py_None) {
		struct objc_super super;
		
   		super.class = find_real_superclass(GETISA(self),
			@selector(retainCount), class_getInstanceMethod, 
			(IMP)object_method_retainCount);
		RECEIVER(super) = self;

		return (int)objc_msgSendSuper(&super, @selector(retainCount)); 
	}
	return obj->ob_refcnt;
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
	pyself = ObjC_GetPythonImplementation(self);
	if (pyself == NULL) {
		return NO;
	}
	pymeth = ObjCObject_FindSelector(pyself, aSelector);
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

	pyself = ObjC_GetPythonImplementation(self);
	if (pyself == NULL) {
		PyErr_Clear();
		return nil;
	}

	pymeth = ObjCObject_FindSelector(pyself, aSelector);
	if (!pymeth) {
		PyErr_Clear();
		return nil;
	}

	result =  [NSMethodSignature signatureWithObjCTypes:(
		  	(ObjCSelector*)pymeth)->sel_signature];
	[result autorelease];
	Py_DECREF(pymeth);
	return result;
}

/* -forwardInvocation: */
static void
object_method_forwardInvocation(id self, SEL selector, NSInvocation* invocation)
{
	PyObject*	args;
	PyObject* 	result;
	PyObject*       v;
	int             i;
	int 		len;
	NSMethodSignature* signature;
	char		   argbuf[1024];
	const char* 		type;
	void* arg = NULL;
	const char* err;
	int   arglen;
	PyObject* pymeth;
	PyObject* pyself;

	pyself = ObjC_GetPythonImplementation(self);
	if (pyself == NULL) {
		ObjCErr_ToObjC();
		return;
	}
	pymeth = ObjCObject_FindSelector(pyself, selector);
	if (pymeth && ObjCNativeSelector_Check(pymeth)) {
		struct objc_super super;

		Py_DECREF(pymeth);

		super.class = find_real_superclass(
				GETISA(self), 
				selector, class_getInstanceMethod, 
				(IMP)object_method_forwardInvocation);
		super.receiver = self;
		objc_msgSendSuper(&super, selector, invocation);
		return;
	}
	Py_XDECREF(pymeth);

	signature = [invocation methodSignature];
	len = [signature numberOfArguments];

	args = PyTuple_New(len - 1);
	if (args == NULL) {
		ObjCErr_ToObjC();
	}

	i = PyTuple_SetItem(args, 0, pythonify_c_value(
					[signature getArgumentTypeAtIndex:0],
					(void*)&self));
	if (i < 0) {
		Py_DECREF(args);
		ObjCErr_ToObjC();
		return;
	}

	for (i = 2; i < len; i++) {
		type = [signature getArgumentTypeAtIndex:i];
		arglen = objc_sizeof_type(type);

		if (arglen == -1) {
			Py_DECREF(args);
			ObjCErr_ToObjC();
			return;
		}

		arg = alloca(arglen);
		
		[invocation getArgument:argbuf atIndex:i];
		v = pythonify_c_value(type, argbuf);
		if (v == NULL) {
			Py_DECREF(args);
			ObjCErr_ToObjC();
			return;
		}

		if (PyTuple_SetItem(args, i-1, v) < 0) {
			Py_DECREF(args);
			ObjCErr_ToObjC();
			return;
		}
	}

	result = ObjC_call_to_python(self, [invocation selector], args);
	Py_DECREF(args);
	if (result == NULL) {
		ObjCErr_ToObjC();
		return;
	}

	type = [signature methodReturnType];
	arglen = objc_sizeof_type(type);

	if (arglen == -1) {
		ObjCErr_ToObjC();
		return;
	}

	arg = alloca(arglen+1);

	err = depythonify_c_value(type, result, arg);
	if (err != NULL) {
		ObjCErr_Set(ObjCExc_error,
			"Cannot depythonify result: %s", err);
		ObjCErr_ToObjC();
		return;
	}
}

/*
 * XXX: Function ObjC_call_to_python should be moved
 */

PyObject*
ObjC_call_to_python(id self, SEL selector, PyObject* arglist)
{
	PyObject* pyself = NULL;
	PyObject* pymeth = NULL;
	PyObject* result;


	pyself = ObjC_GetPythonImplementation(self);
	if (pyself == NULL) {
		ObjCErr_ToObjC();
		return NULL;
	}
	pymeth = ObjCObject_FindSelector(pyself, selector);
	if (pymeth == NULL) {
		ObjCErr_ToObjC();
		return NULL;
	}

	result = PyObject_Call(pymeth, arglist, NULL);
	Py_DECREF(pymeth);

	if (result == NULL) {
		ObjCErr_ToObjC();
		return NULL;
	}

	return result;
}
