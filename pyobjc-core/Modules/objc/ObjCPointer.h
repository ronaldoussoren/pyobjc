#ifndef PyObjC_OBJC_POINTER_H
#define PyObjC_OBJC_POINTER_H

NS_ASSUME_NONNULL_BEGIN

/* Python wrapper around C pointer
 *
 * NOTE: This class is almost never used, pointers in method interfaces are,
 * or should be, treated differently and I've yet to run into a Cocoa structure
 * that contains pointers.
 */

extern PyObject* PyObjCPointer_Type;
#define PyObjCPointer_Check(o) (Py_TYPE(o) == (PyTypeObject*)PyObjCPointer_Type)

extern PyObject* _Nullable PyObjCPointer_New(void* ptr, const char* type)
    __attribute__((__warn_unused_result__));

/* XXX: Nullable because of type checking */
extern void* _Nullable PyObjCPointer_Ptr(PyObject* object);

extern int PyObjCPointer_Setup(PyObject* module);

NS_ASSUME_NONNULL_END

#endif /* PyObjC_OBJC_POINTER_H */
