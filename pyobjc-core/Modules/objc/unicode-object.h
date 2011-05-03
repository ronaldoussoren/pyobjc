#ifndef PyObjC_UNICODE_H
#define PyObjC_UNICODE_H

extern PyTypeObject PyObjCUnicode_Type;
#define PyObjCUnicode_Check(obj) PyObject_TypeCheck(obj, &PyObjCUnicode_Type)
PyObject* PyObjCUnicode_New(NSString* value);
NSString* PyObjCUnicode_Extract(PyObject* value);

#endif /* PyObjC_UNICODE_H */
