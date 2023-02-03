/*
 * Opaque wrapper for the ``FSRef`` structure
 */
#ifndef PyObjC_FSREF_H
#define PyObjC_FSREF_H

NS_ASSUME_NONNULL_BEGIN

#define IS_FSREF(typestr)                                                                \
    (strncmp(typestr, @encode(FSRef), sizeof(@encode(FSRef)) - 1) == 0)

extern int PyObjC_encode_fsref(PyObject*, void*);
extern PyObject* _Nullable PyObjC_decode_fsref(const void*);

extern PyObject* PyObjCFSRef_Type;
#define PyObjCFSRef_Check(value)                                                         \
    PyObject_TypeCheck(value, (PyTypeObject*)PyObjCFSRef_Type)

extern int PyObjCFSRef_Setup(PyObject*);

NS_ASSUME_NONNULL_END

#endif /* PyObjC_FSREF_H */
