#ifndef META_H
#define META_H

#include "objc_util.h"

#include <Python.h>
#ifdef GNU_RUNTIME
#include <objc/runtime.h>
#else
#include <objc/objc-runtime.h>
#endif
#include "OC_PythonObject.h"
#include "OC_PythonArray.h"
#include "OC_PythonDictionary.h"
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

#if PY_VERSION_HEX < 0x0203000A /* Python < 2.3.0a */

/* PyBool_Type was introduced in Python 2.3 */
#define PyBool_Check(_x_) (0)
#define PyBool_FromLong(_x_) PyInt_FromLong(_x_)

#endif /* Python < 2.3.0a */

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
int 	  ObjC_RegisterClassProxy(Class cls, PyObject* classProxy);
void ObjCClass_CheckMethodList(PyObject* cls);




PyObject* ObjCObject_New(id objc_object);
PyObject* ObjCObject_FindSelector(PyObject* cls, SEL selector);
id 	  ObjCObject_GetObject(PyObject* object);
void 	  ObjCObject_ClearObject(PyObject* object);
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

#define ObjCSelector_kCLASS_METHOD    0x1
#define ObjCSelector_kDONATE_REF      0x2
#define ObjCSelector_kREQUIRED        0x4

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
#ifdef OBJC_PARANOIA_MODE

#define OC_CheckRevive(obj)     \
        do {  \
                if ((obj)->ob_refcnt == 0) {                            \
                        PySys_WriteStderr("%s:%d %s revives %p\n",      \
                                      __FILE__, __LINE__, __FUNCTION__, \
                                      (obj)); \
                        abort(); \
                } \
	} while (0)

#else /* !OBJC_PARANOIA_MODE */

#define OC_CheckRevive(obj)

#endif /* !OBJC_PARANOIA_MODE */

/* See alloc_hack.m */
int ObjC_InstallAllocHack(void);

#ifdef OC_WITH_LIBFFI

IMP ObjC_MakeIMPForSignature(char* signature);
PyObject *ObjC_FFICaller(PyObject *aMeth, PyObject* self, PyObject *args);

#endif /* OC_WITH_LIBFFI */

#endif /* META_H */
