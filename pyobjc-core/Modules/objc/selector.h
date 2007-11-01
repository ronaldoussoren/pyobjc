#ifndef PyObjC_SELECTOR_H
#define PyObjC_SELECTOR_H

/* We have a small class-tree for selector/objective-C methods: A base type
 * and two subtypes (one for methods implemented in python and one for methods
 * implemented in Objective-C)
 */

#define PyObjCSelector_kCLASS_METHOD          0x000001
#define PyObjCSelector_kREQUIRED              0x000004
#define PyObjCSelector_kRETURNS_UNINITIALIZED 0x000010

#define PyObjCSelector_HEAD \
	PyObject_HEAD 			\
	char*		sel_python_signature;  \
	char* 		sel_native_signature; \
	SEL		sel_selector;	\
	PyObject*	sel_self;	\
	Class		sel_class;	\
	int		sel_flags;	\
	PyObjCMethodSignature* sel_methinfo;


/*!
 * @typedef PyObjC_CallFunc
 * @param meth A selector object
 * @param self The self argument
 * @param args The other arguments
 * @result Returns the return value, or NULL if an exception occurred
 */
typedef PyObject* (*PyObjC_CallFunc)(
	PyObject* meth, PyObject* self, PyObject* args);

typedef struct {
	PyObjCSelector_HEAD
} PyObjCSelector;

typedef struct {
	PyObjCSelector_HEAD
	PyObjC_CallFunc sel_call_func; 
} PyObjCNativeSelector;

typedef struct {
	PyObjCSelector_HEAD
	PyObject*	callable;
	Py_ssize_t	argcount;
	Py_ssize_t	numoutput;
} PyObjCPythonSelector;

extern PyTypeObject PyObjCSelector_Type;
extern PyTypeObject PyObjCNativeSelector_Type;
extern PyTypeObject PyObjCPythonSelector_Type;
#define PyObjCSelector_Check(obj) PyObject_TypeCheck(obj, &PyObjCSelector_Type)
#define PyObjCNativeSelector_Check(obj) PyObject_TypeCheck(obj, &PyObjCNativeSelector_Type)
#define PyObjCPythonSelector_Check(obj) PyObject_TypeCheck(obj, &PyObjCPythonSelector_Type)

PyObject* PyObjCSelector_Copy(PyObject* obj);
char* PyObjCSelector_Signature(PyObject* obj);
SEL   PyObjCSelector_GetSelector(PyObject* obj);
int   PyObjCSelector_GetFlags(PyObject* obj);
Class PyObjCSelector_GetClass(PyObject* obj);
int   PyObjCSelector_Required(PyObject* obj);
int   PyObjCSelector_IsClassMethod(PyObject* obj);
int ObjC_SignatureForSelector(char* class_name, SEL selector, char* signature);
PyObjCMethodSignature* PyObjCSelector_GetMetadata(PyObject* _self);



PyObject* PyObjCSelector_NewNative(Class class, SEL selector, const char* signature, int class_method) ;
PyObject* PyObjCSelector_FindNative(PyObject* self, const char* name);

#define PyObjCSelector_GET_CLASS(obj) (((PyObjCSelector*)(obj))->sel_class)
#define PyObjCSelector_GET_SELECTOR(obj) (((PyObjCSelector*)(obj))->sel_selector)

PyObject* PyObjCSelector_New(PyObject* callable, SEL selector, char* signature, int class_method, Class class) ;
SEL PyObjCSelector_DefaultSelector(const char* methname);

PyObject* 
PyObjCSelector_FromFunction(
	PyObject* pyname,
	PyObject* callable,
	PyObject* template_class,
	PyObject* protocols);


#endif /* PyObjC_SELECTOR_H */
