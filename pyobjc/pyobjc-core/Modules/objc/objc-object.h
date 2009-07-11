#ifndef PyObjC_OBJC_OBJECT_H
#define PyObjC_OBJC_OBJECT_H

#define PyObjCObject_kDEFAULT 0x00
#define PyObjCObject_kUNINITIALIZED 	0x01
#define PyObjCObject_kCLASSIC 		0x02
#define PyObjCObject_kDEALLOC_HELPER	0x04
#define PyObjCObject_kSHOULD_NOT_RELEASE      0x08
#define PyObjCObject_kMAGIC_COOKIE      0x10
#define PyObjCObject_kCFOBJECT      0x20
#define PyObjCObject_kBLOCK      0x40

typedef struct {
	PyObject_HEAD
	__strong id objc_object;
	int 	    flags;
} PyObjCObject;

typedef struct {
	PyObject_HEAD
	__strong id objc_object;
	int 	    flags;
	PyObjCMethodSignature* signature;
} PyObjCBlockObject;


extern PyObjCClassObject PyObjCObject_Type;
#define PyObjCObject_Check(obj) PyObject_TypeCheck(obj, (PyTypeObject*)&PyObjCObject_Type)

PyObject* PyObjCObject_New(id objc_object, int flags, int retain);
PyObject* PyObjCObject_FindSelector(PyObject* cls, SEL selector);
id 	  PyObjCObject_GetObject(PyObject* object);
void 	  PyObjCObject_ClearObject(PyObject* object);
#define   PyObjCObject_GetObject(object) (((PyObjCObject*)(object))->objc_object)
void _PyObjCObject_FreeDeallocHelper(PyObject* obj);
PyObject* _PyObjCObject_NewDeallocHelper(id objc_object);
#define PyObjCObject_GetFlags(object) (((PyObjCObject*)(object))->flags)
#define PyObjCObject_IsClassic(object) (PyObjCObject_GetFlags(object) & PyObjCObject_kCLASSIC)
#define PyObjCObject_IsBlock(object) (PyObjCObject_GetFlags(object) & PyObjCObject_kBLOCK)
#define PyObjCObject_GetBlock(object) (((PyObjCBlockObject*)(object))->signature)
#define PyObjCObject_SET_BLOCK(object, value) (((PyObjCBlockObject*)(object))->signature = (value))

PyObject* PyObjCObject_GetAttr(PyObject* object, PyObject* key);
PyObject* PyObjCObject_GetAttrString(PyObject* object, char* key);


PyObject* PyObjCObject_NewTransient(id objc_object, int* cookie);
void PyObjCObject_ReleaseTransient(PyObject* proxy, int cookie);

#endif /* PyObjC_OBJC_OBJECT_H */
