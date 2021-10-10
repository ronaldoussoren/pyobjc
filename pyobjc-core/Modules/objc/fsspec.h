/*
 * Opaque wrapper for the ``FSSpec`` structure
 */
#ifndef PyObjC_FSSPEC_H
#define PyObjC_FSSPEC_H

NS_ASSUME_NONNULL_BEGIN

#define IS_FSSPEC(typestr)                                                               \
    (strncmp(typestr, @encode(FSSpec), sizeof(@encode(FSSpec)) - 1) == 0)

extern int PyObjC_encode_fsspec(PyObject*, void*);
extern PyObject* _Nullable PyObjC_decode_fsspec(void*);

extern PyTypeObject PyObjC_FSSpecType;
#define PyObjC_FSSpecCheck(value) PyObject_TypeCheck(value, &PyObjC_FSSpecType)

NS_ASSUME_NONNULL_END

#endif /* PyObjC_FSSPEC_H */
