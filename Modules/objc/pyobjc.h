#ifndef META_H
#define META_H

#include "objc_util.h"

#include <Python.h>
#include "py2.2bool.h"
#ifdef GNU_RUNTIME
#include <objc/runtime.h>
#else
#include <objc/objc-runtime.h>
#endif
#include "OC_PythonObject.h"
#include "OC_PythonArray.h"
#include "OC_PythonDictionary.h"
//#include "OC_PythonString.h"
#include "super-call.h"

/*
 * Python compatibility definitions
 */

/* Earlier versions of Python don't define PyDoc_STRVAR */
#ifndef PyDoc_STR
#define PyDoc_VAR(name)	        static char name[]
#define PyDoc_STR(str)	        (str)
#define PyDoc_STRVAR(name, str) PyDoc_VAR(name) = PyDoc_STR(str)
#endif

#define OBJC_VERSION "0.8CVS"

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
@end // interface NSMethodSignature
#endif

extern int ObjC_VerboseLevel;

extern PyTypeObject PyObjCClass_Type;
#define PyObjCClass_Check(obj) PyObject_TypeCheck(obj, &PyObjCClass_Type)

#if PY_VERSION_HEX >= 0x020300A2

typedef struct {
	PyHeapTypeObject        base;
	Class     class;
	PyObject* sel_to_py;
	int       method_magic;
} PyObjCClassObject;

#else

typedef struct {
	PyTypeObject		base;
} PyObjCClassObject;

#endif



#define PyObjCObject_kUNINITIALIZED 	0x01
typedef struct {
	PyObject_HEAD
	PyObject* weak_refs;
	id        objc_object;
	int 	  flags;
} PyObjCObject;

extern PyObjCClassObject PyObjCObject_Type;
#define PyObjCObject_Check(obj) PyObject_TypeCheck(obj, (PyTypeObject*)&PyObjCObject_Type)

extern PyObject* PyObjCClass_DefaultModule;
PyObject* PyObjCClass_New(Class objc_class);
Class     PyObjCClass_GetClass(PyObject* object);
PyObject* PyObjCClass_FindSelector(PyObject* cls, SEL selector);
void 	  PyObjCClass_MaybeRescan(PyObject* class);
int 	  PyObjCClass_IsSubClass(Class child, Class parent);
int 	  ObjC_RegisterClassProxy(Class cls, PyObject* classProxy);
void PyObjCClass_CheckMethodList(PyObject* cls);




PyObject* PyObjCObject_New(id objc_object);
PyObject* PyObjCObject_FindSelector(PyObject* cls, SEL selector);
id 	  PyObjCObject_GetObject(PyObject* object);
void 	  PyObjCObject_ClearObject(PyObject* object);
#define   PyObjCObject_GetObject(object) (((PyObjCObject*)(object))->objc_object)


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

#define ObjCSelector_kCLASS_METHOD          0x000001
#define ObjCSelector_kDONATE_REF            0x000002
#define ObjCSelector_kREQUIRED              0x000004
#define ObjCSelector_kRETURNS_SELF          0x000008
#define ObjCSelector_kRETURNS_UNINITIALIZED 0x000010
#define ObjCSelector_kINITIALIZER    	    0x000020

#define ObjCSelector_HEAD \
	PyObject_HEAD 			\
	char*		sel_signature;  \
	SEL		sel_selector;	\
	PyObject*	sel_self;	\
	Class		sel_class;	\
	int		sel_flags;


typedef struct {
	ObjCSelector_HEAD
} ObjCSelector;

typedef struct {
	ObjCSelector_HEAD
	NSMethodSignature* sel_oc_signature;
	ObjC_CallFunc_t sel_call_self; 
	ObjC_CallFunc_t sel_call_super;
} ObjCNativeSelector;

typedef struct {
	ObjCSelector_HEAD
	PyObject*	callable;
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

/* See alloc_hack.m */
int PyObjC_InstallAllocHack(void);

#ifdef OC_WITH_LIBFFI

IMP ObjC_MakeIMPForSignature(char* signature, PyObject* callable);
IMP ObjC_MakeIMPForObjCSelector(ObjCSelector *aSelector);
PyObject *ObjC_FFICaller(PyObject *aMeth, PyObject* self, PyObject *args);

#endif /* OC_WITH_LIBFFI */

extern PyObject* ObjCMethodAccessor_New(PyObject* base, int class_method);

/* Needed by method-accessor, name will be changed soon */
char* pythonify_selector(SEL, char*, size_t);

/* unicode-object.m */
extern PyTypeObject ObjCUnicode_Type;
#define ObjCUnicode_Check(obj) PyObject_TypeCheck(obj, &ObjCUnicode_Type)
PyObject* ObjCUnicode_New(NSString* value);
NSString* ObjCUnicode_Extract(PyObject* value);

#endif /* META_H */
