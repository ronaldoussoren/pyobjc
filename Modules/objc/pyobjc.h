#ifndef META_H
#define META_H

#include "objc_util.h"

#include <Python.h>
#include <objc/objc-runtime.h>
#include "OC_PythonObject.h"
#include "super-call.h"

#define PYOBJC_VERSION "0.7.1"

#ifdef MACOSX

/* On MacOS X, +signatureWithObjCTypes: is a method of NSMethodSignature,
 * but that method is not present in the header files. We add the definition
 * here to avoid warnings.
 * 
 * XXX: We use an undocumented API, but we also don't have much choice: we
 * must create the things and this is the only way to do it...
 */
@interface NSMethodSignature (WarningKiller)
	+signatureWithObjCTypes:(const char*)types;
	@end
#endif


extern PyTypeObject ObjCClass_Type;
#define ObjCClass_Check(obj) PyObject_TypeCheck(obj, &ObjCClass_Type)


typedef struct {
	PyObject_HEAD
	PyObject* weak_refs;
	id        objc_object;
	int 	  is_paired;
} ObjCObject;

extern PyTypeObject ObjCObject_Type;
#define ObjCObject_Check(obj) PyObject_TypeCheck(obj, &ObjCObject_Type)

PyObject* ObjCClass_New(Class objc_class);
Class     ObjCClass_GetClass(PyObject* object);
PyObject* ObjCClass_FindSelector(PyObject* cls, SEL selector);
void 	  ObjCClass_MaybeRescan(PyObject* class);
int 	  ObjCClass_IsSubClass(Class child, Class parent);


PyObject* ObjCObject_New(id objc_object);
PyObject* ObjCObject_FindSelector(PyObject* cls, SEL selector);
id 	  ObjCObject_GetObject(PyObject* object);
#define   ObjCObject_GetObject(object) (((ObjCObject*)(object))->objc_object)


/* in class-descriptor.m */
PyObject* objcclass_descr_get(PyObject* obj, void* closure);
extern char objcclass_descr_doc[];

#define OBJCCLASS_SLOT \
	{ 						\
	"__objc_class__",		/* name */	\
	objcclass_descr_get,		/* get */	\
	0,				/* set */	\
	objcclass_descr_doc,		/* doc */	\
	0,				/* closure */	\
	}


/* in selector.m */
/* We have a small class-tree for selector/objective-C methods: A base type
 * and two subtypes (one for methods implemented in python and one for methods
 * implemented in Objective-C)
 */

extern PyObject* allocator_dict;

#define ObjCSelector_HEAD \
	PyObject_HEAD 			\
	char*		sel_signature;  \
	SEL		sel_selector;	\
	PyObject*	sel_self;	\
	int		sel_class_method;  \
	int		sel_allocator;



typedef struct {
	ObjCSelector_HEAD
} ObjCSelector;

typedef struct {
	ObjCSelector_HEAD
	Class		class;
	ObjC_CallFunc_t sel_call_self; 
	ObjC_CallFunc_t sel_call_super;
} ObjCNativeSelector;

typedef struct {
	ObjCSelector_HEAD
	PyObject*	callable;

	/* Protocol support: */
	unsigned int	is_required:1;
} ObjCPythonSelector;

extern PyTypeObject ObjCSelector_Type;
extern PyTypeObject ObjCNativeSelector_Type;
extern PyTypeObject ObjCPythonSelector_Type;
#define ObjCSelector_Check(obj) PyObject_TypeCheck(obj, &ObjCSelector_Type)
#define ObjCNativeSelector_Check(obj) PyObject_TypeCheck(obj, &ObjCNativeSelector_Type)
#define ObjCPythonSelector_Check(obj) PyObject_TypeCheck(obj, &ObjCPythonSelector_Type)

char* ObjCSelector_Signature(PyObject* obj);
SEL   ObjCSelector_Selector(PyObject* obj);
int   ObjCSelector_Required(PyObject* obj);
int ObjC_SignatureForSelector(char* class_name, SEL selector, char* signature);

PyObject* ObjCSelect_NewFromPython(char* selector, char* signature, PyObject* callable);
PyObject* ObjCSelect_NewWithSelector(Class objc_class, SEL selector);

PyObject*
ObjCSelector_NewNative(Class class, SEL selector, char* signature, int class_method) ;
PyObject* ObjCSelector_FindNative(PyObject* self, char* name);
PyObject*
ObjCSelector_New(PyObject* callable, SEL selector, char* signature, int class_method) ;
SEL ObjCSelector_DefaultSelector(char* methname);



/* From 'instance-var.m' */
#include "instance-var.h"

/* From class-builder.m */
#include "class-builder.h" 

/* From ObjCPointer.m */
#include "ObjCPointer.h"

/* From 'class-list.m' */
PyObject* ObjC_GetClassList(void);


int ObjC_register_methods(void);

int ObjCAPI_Register(PyObject* module_dict);
#define PYOBJC_BUILD
#include "pyobjc-api.h"


extern PyTypeObject ObjCInformalProtocol_Type;
#define ObjCInformalProtocol_Check(obj) PyObject_TypeCheck(obj, &ObjCInformalProtocol_Type)

int     ObjCIPVerify(PyObject* obj, PyObject* cls);
PyObject* ObjCIPFindInfo(PyObject* obj, SEL selector);



#endif /* META_H */
