#ifndef PyObjC_OBJC_OBJECT_H
#define PyObjC_OBJC_OBJECT_H

#define PyObjCObject_kUNINITIALIZED 	0x01
#define PyObjCObject_kCLASSIC 		0x02
typedef struct {
	PyObject_HEAD
	id        objc_object;
	int 	  flags;
} PyObjCObject;

extern PyObjCClassObject PyObjCObject_Type;
#define PyObjCObject_Check(obj) PyObject_TypeCheck(obj, (PyTypeObject*)&PyObjCObject_Type)

PyObject* PyObjCObject_New(id objc_object);
PyObject* PyObjCObject_NewClassic(id objc_object);
PyObject* PyObjCObject_NewUnitialized(id objc_object);
PyObject* PyObjCObject_FindSelector(PyObject* cls, SEL selector);
id 	  PyObjCObject_GetObject(PyObject* object);
void 	  PyObjCObject_ClearObject(PyObject* object);
#define   PyObjCObject_GetObject(object) (((PyObjCObject*)(object))->objc_object)
void _PyObjCObject_FreeDeallocHelper(PyObject* obj);
PyObject* _PyObjCObject_NewDeallocHelper(id objc_object);
#define PyObjCObject_Flags(object) (((PyObjCObject*)(object))->flags)
#define PyObjCObject_IsClassic(object) (PyObjCObject_Flags(object) & PyObjCObject_kCLASSIC)

#endif /* PyObjC_OBJC_OBJECT_H */
