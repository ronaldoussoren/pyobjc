/*
 * Opaque wrapper for the ``FSRef`` structure
 */
#ifndef PyObjC_FSREF_H
#define PyObjC_FSREF_H

#define IS_FSREF(typestr) \
	(strncmp(typestr, @encode(FSRef), sizeof(@encode(FSRef))-1) == 0)

extern int PyObjC_encode_fsref(PyObject*, void*);
extern PyObject* PyObjC_decode_fsref(void*);

extern PyTypeObject PyObjC_FSRefType;
#define PyObjC_FSRefCheck(value) \
	PyObject_TypeCheck(value, &PyObjC_FSRefType)

#endif /* PyObjC_FSREF_H */
