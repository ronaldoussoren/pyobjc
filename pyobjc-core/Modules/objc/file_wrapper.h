#ifndef PyObjC_FILEWRAPPER_H
#define PyObjC_FILEWRAPPER_H

NS_ASSUME_NONNULL_BEGIN

/* A basic wrapper for C's "FILE*"
 * that implements a usable API.
 */
extern PyTypeObject FILE_Type;

#define FILE_Check(obj) PyObject_TypeCheck(obj, &FILE_Type)

extern PyObject* _Nullable FILE_create(FILE* fp);
extern FILE* _Nullable FILE_get(PyObject* fp);

NS_ASSUME_NONNULL_END

#endif /* PyObjC_FILEWRAPPER_H */
