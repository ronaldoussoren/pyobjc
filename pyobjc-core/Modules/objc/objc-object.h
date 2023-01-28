#ifndef PyObjC_OBJC_OBJECT_H
#define PyObjC_OBJC_OBJECT_H

NS_ASSUME_NONNULL_BEGIN

#define PyObjCObject_kDEFAULT 0x00
#define PyObjCObject_kUNINITIALIZED 0x01
#define PyObjCObject_kDEALLOC_HELPER 0x04
#define PyObjCObject_kSHOULD_NOT_RELEASE 0x08
#define PyObjCObject_kMAGIC_COOKIE 0x10
#define PyObjCObject_kCFOBJECT 0x20
#define PyObjCObject_kBLOCK 0x40
#define PyObjCObject_kNEW_WRAPPER 0x80

typedef struct {
    PyObject_HEAD

    __strong     id _Nullable objc_object;
    unsigned int flags;
} PyObjCObject;

typedef struct {
    PyObjCObject base;
    PyObjCMethodSignature* _Nullable signature;
} PyObjCBlockObject;

extern PyObjCClassObject PyObjCObject_Type;
#define PyObjCObject_Check(obj) PyObject_TypeCheck(obj, (PyTypeObject*)&PyObjCObject_Type)

PyObject* _Nullable PyObjCObject_New(id objc_object, int flags, int retain);
PyObject* _Nullable PyObjCObject_FindSelector(PyObject* cls, SEL selector);
id _Nullable PyObjCObject_GetObject(PyObject* object);
void PyObjCObject_ClearObject(PyObject* object);

/* XXX: Is the macro still needed with LTO? */
#define PyObjCObject_GetObject(object) (((PyObjCObject*)(object))->objc_object)

void _PyObjCObject_FreeDeallocHelper(PyObject* obj);
PyObject* _Nullable _PyObjCObject_NewDeallocHelper(id objc_object);

#define PyObjCObject_GetFlags(object) (((PyObjCObject*)(object))->flags)
#define PyObjCObject_IsBlock(object) (PyObjCObject_GetFlags(object) & PyObjCObject_kBLOCK)
#define PyObjCObject_IsMagic(object)                                                     \
    (PyObjCObject_GetFlags(object) & PyObjCObject_kMAGIC_COOKIE)
#define PyObjCObject_GetBlock(object) (((PyObjCBlockObject*)(object))->signature)
#define PyObjCObject_SET_BLOCK(object, value)                                            \
    (((PyObjCBlockObject*)(object))->signature = (value))

PyObject* _Nullable PyObjCObject_GetAttr(PyObject* object, PyObject* key);
PyObject* _Nullable PyObjCObject_GetAttrString(PyObject* object, char* key);
PyObject* _Nullable PyObjCObject_NewTransient(id objc_object, int* cookie);
void PyObjCObject_ReleaseTransient(PyObject* proxy, int cookie);

/* XXX: Move to different file */
PyObject* _Nullable PyObjC_get_c_void_p(void);

NS_ASSUME_NONNULL_END

#endif /* PyObjC_OBJC_OBJECT_H */
