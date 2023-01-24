#ifndef PyObjC_FILEWRAPPER_H
#define PyObjC_FILEWRAPPER_H

NS_ASSUME_NONNULL_BEGIN

extern PyObject* _Nullable FILE_create(FILE* fp);
extern FILE* _Nullable FILE_get(PyObject* fp);

extern int FILE_Setup(PyObject* module);

NS_ASSUME_NONNULL_END

#endif /* PyObjC_FILEWRAPPER_H */
