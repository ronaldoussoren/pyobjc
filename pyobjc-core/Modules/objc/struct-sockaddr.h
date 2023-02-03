/*
 * Support for converting "struct sockaddr" values to/from Python
 */
#ifndef PyObjC_STRUCT_SOCKADDR
#define PyObjC_STRUCT_SOCKADDR

NS_ASSUME_NONNULL_BEGIN

extern int PyObjC_SockAddr_Setup(PyObject*);
extern int PyObjC_SockAddrFromPython(PyObject*, void*);
extern PyObject* _Nullable PyObjC_SockAddrToPython(const void*);

NS_ASSUME_NONNULL_END

#endif /*PyObjC_STRUCT_SOCKADDR */
