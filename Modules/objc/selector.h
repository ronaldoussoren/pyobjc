#ifndef PyObjC_SELECTOR_H
#define PyObjC_SELECTOR_H

/* We have a small class-tree for selector/objective-C methods: A base type
 * and two subtypes (one for methods implemented in python and one for methods
 * implemented in Objective-C)
 */

#define PyObjCSelector_kCLASS_METHOD          0x000001
#define PyObjCSelector_kDONATE_REF            0x000002
#define PyObjCSelector_kREQUIRED              0x000004
#define PyObjCSelector_kRETURNS_SELF          0x000008
#define PyObjCSelector_kRETURNS_UNINITIALIZED 0x000010
#define PyObjCSelector_kINITIALIZER    	    0x000020

#define PyObjCSelector_HEAD \
	PyObject_HEAD 			\
	char*		sel_signature;  \
	SEL		sel_selector;	\
	PyObject*	sel_self;	\
	Class		sel_class;	\
	int		sel_flags;


typedef struct {
	PyObjCSelector_HEAD
} PyObjCSelector;

typedef struct {
	PyObjCSelector_HEAD
	PyObjCMethodSignature* sel_oc_signature;
	ObjC_CallFunc_t sel_call_func; 
} ObjCNativeSelector;

typedef struct {
	PyObjCSelector_HEAD
	PyObject*	callable;
} ObjCPythonSelector;

extern PyTypeObject PyObjCSelector_Type;
extern PyTypeObject ObjCNativeSelector_Type;
extern PyTypeObject ObjCPythonSelector_Type;
#define PyObjCSelector_Check(obj) PyObject_TypeCheck(obj, &PyObjCSelector_Type)
#define ObjCNativeSelector_Check(obj) PyObject_TypeCheck(obj, &ObjCNativeSelector_Type)
#define ObjCPythonSelector_Check(obj) PyObject_TypeCheck(obj, &ObjCPythonSelector_Type)

char* PyObjCSelector_Signature(PyObject* obj);
SEL   PyObjCSelector_GetSelector(PyObject* obj);
Class PyObjCSelector_GetClass(PyObject* obj);
int   PyObjCSelector_Required(PyObject* obj);
int ObjC_SignatureForSelector(char* class_name, SEL selector, char* signature);

PyObject* ObjCSelect_NewFromPython(char* selector, char* signature, PyObject* callable);
PyObject* ObjCSelect_NewWithSelector(Class objc_class, SEL selector);

PyObject*
PyObjCSelector_NewNative(Class class, SEL selector, const char* signature, int class_method) ;
PyObject* PyObjCSelector_FindNative(PyObject* self, const char* name);

PyObject*
PyObjCSelector_New(PyObject* callable, SEL selector, char* signature, int class_method, Class class) ;
SEL PyObjCSelector_DefaultSelector(const char* methname);

#endif /* PyObjC_SELECTOR_H */
