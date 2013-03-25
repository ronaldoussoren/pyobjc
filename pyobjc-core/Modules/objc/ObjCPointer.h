#ifndef PyObjC_OBJC_POINTER_H
#define PyObjC_OBJC_POINTER_H

/* Python wrapper around C pointer
 *
 * NOTE: This class is almost never used, pointers in method interfaces are,
 * or should be, treated differently and I've yet to run into a Cocoa structure
 * that contains pointers.
 */

extern PyTypeObject PyObjCPointer_Type;
#define PyObjCPointer_Check(o) (Py_TYPE(o) == &PyObjCPointer_Type)

extern PyObject* PyObjCPointer_New(void *ptr, const char *type) __attribute__((__nonnull__(2))) __attribute__((__warn_unused_result__));
extern void* PyObjCPointer_Ptr(PyObject* object) __attribute__((__nonnull__(1)));

#endif /* PyObjC_OBJC_POINTER_H */
