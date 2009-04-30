/*
 * Opaque wrapper for the ``FSSpec`` structure
 */
#ifndef PyObjC_FSSPEC_H
#define PyObjC_FSSPEC_H

#define IS_FSSPEC(typestr) \
	(strncmp(typestr, @encode(FSSpec), sizeof(@encode(FSSpec))-1) == 0)

extern int PyObjC_encode_fsspec(PyObject*, void*);
extern PyObject* PyObjC_decode_fsspec(void*);

extern PyTypeObject PyObjC_FSSpecType;
#define PyObjC_FSSpecCheck(value) \
	PyObject_TypeCheck(value, &PyObjC_FSSpecType)

#endif PyObjC_FSSPEC_H
