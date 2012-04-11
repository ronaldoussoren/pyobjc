#ifndef PyObjC_OBJC_POINTER_H
#define PyObjC_OBJC_POINTER_H

/* Python wrapper around C pointer 
 *
 * NOTE: This class is almost never used, pointers in method interfaces are,
 * or should be, treated differently and I've yet to run into a Cocoa structure 
 * that contains pointers.
 */

typedef struct
{
  PyObject_VAR_HEAD

  void *ptr;
  PyObject *type;
  char contents[1];
} PyObjCPointer;

extern int	PyObjCPointer_RaiseException;

extern PyTypeObject PyObjCPointer_Type;

#define PyObjCPointer_Check(o) (Py_TYPE(o) == &PyObjCPointer_Type)

extern PyObjCPointer *PyObjCPointer_New(void *ptr, const char *type);
#define PyObjCPointer_Ptr(obj) (((PyObjCPointer*)(obj))->ptr)

#endif /* PyObjC_OBJC_POINTER_H */
