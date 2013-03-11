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

extern PyObject* PyObjCPointer_New(void *ptr, const char *type);
extern void* PyObjCPointer_Ptr(PyObject* object);

#endif /* PyObjC_OBJC_POINTER_H */
