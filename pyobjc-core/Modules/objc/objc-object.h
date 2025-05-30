#ifndef PyObjC_OBJC_OBJECT_H
#define PyObjC_OBJC_OBJECT_H

NS_ASSUME_NONNULL_BEGIN

#define PyObjCObject_kDEFAULT 0x00
/* #define PyObjCObject_kUNINITIALIZED 0x01 */
#define PyObjCObject_kDEALLOC_HELPER 0x04
#define PyObjCObject_kSHOULD_NOT_RELEASE 0x08
#define PyObjCObject_kMAGIC_COOKIE 0x10
#define PyObjCObject_kCFOBJECT 0x20
#define PyObjCObject_kBLOCK 0x40
#define PyObjCObject_kNEW_WRAPPER 0x80

typedef struct {
    PyObject_HEAD

    __strong     id objc_object;
    unsigned int flags;
} PyObjCObject;

typedef struct {
    PyObjCObject base;
    PyObjCMethodSignature* _Nullable signature;
} PyObjCBlockObject;

extern PyObjCClassObject PyObjCObject_Type;
#define PyObjCObject_Check(obj) PyObject_TypeCheck(obj, (PyTypeObject*)&PyObjCObject_Type)

extern PyObject* _Nullable PyObjCObject_New(id objc_object, int flags, int retain);
extern PyObject* _Nullable PyObjCObject_FindSelector(PyObject* cls, SEL selector);
extern id PyObjCObject_GetObject(PyObject* object);
extern unsigned int PyObjCObject_GetFlags(PyObject* object);

extern void _PyObjCObject_FreeDeallocHelper(PyObject* obj);
extern PyObject* _Nullable _PyObjCObject_NewDeallocHelper(id objc_object);
extern bool PyObjCObject_IsBlock(PyObject* object);
extern bool PyObjCObject_IsMagic(PyObject* object);
extern PyObjCMethodSignature* _Nullable PyObjCObject_GetBlockSignature(PyObject* object);
extern PyObjCMethodSignature* _Nullable  PyObjCObject_SetBlockSignature(PyObject* object, PyObjCMethodSignature* methinfo);

/*
 * XXX: these defines should be in the .m file
 */
#define PyObjCObject_FLAGS(object) (((PyObjCObject*)(object))->flags)
#define PyObjCObject_OBJECT(object) (((PyObjCObject*)(object))->objc_object)

extern PyObject* _Nullable PyObjCObject_GetAttr(PyObject* object, PyObject* key);
extern PyObject* _Nullable PyObjCObject_GetAttrString(PyObject* object, char* key);
extern PyObject* _Nullable PyObjCObject_NewTransient(id objc_object, int* cookie);
extern void PyObjCObject_ReleaseTransient(PyObject* proxy, int cookie);

NS_ASSUME_NONNULL_END

#endif /* PyObjC_OBJC_OBJECT_H */
