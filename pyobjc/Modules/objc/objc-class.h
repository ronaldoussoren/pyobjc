#ifndef  PyObjC_OBJC_CLASS_H 
#define  PyObjC_OBJC_CLASS_H 

extern PyTypeObject PyObjCClass_Type;
#define PyObjCClass_Check(obj) PyObject_TypeCheck(obj, &PyObjCClass_Type)

#if PY_VERSION_HEX >= 0x020300A2 

#define PyObjC_CLASS_INFO_IN_TYPE 1

typedef struct {
	PyHeapTypeObject        base;
	Class     class;
	PyObject* sel_to_py;
	int       method_magic;
	int	  dictoffset;
	PyObject* delmethod;
	int	  hasPythonImpl;
} PyObjCClassObject;

#else

typedef struct {
	PyTypeObject		base;
} PyObjCClassObject;

#endif

extern PyObject* PyObjCClass_DefaultModule;
PyObject* PyObjCClass_New(Class objc_class);
Class     PyObjCClass_GetClass(PyObject* object);
PyObject* PyObjCClass_FindSelector(PyObject* cls, SEL selector);
void 	  PyObjCClass_MaybeRescan(PyObject* class);
int 	  PyObjCClass_IsSubClass(Class child, Class parent);
int 	  ObjC_RegisterClassProxy(Class cls, PyObject* classProxy);
void PyObjCClass_CheckMethodList(PyObject* cls, int recursive);
int PyObjCClass_DictOffset(PyObject* cls);
PyObject* PyObjCClass_GetDelMethod(PyObject* cls);
void PyObjCClass_SetDelMethod(PyObject* cls, PyObject* newval);
int  PyObjCClass_HasPythonImplementation(PyObject* cls);

#endif /* PyObjC_OBJC_CLASS_H */
