/*
 * Support for converting "struct sockaddr" values to/from Python
 */
#ifndef PyObjC_STRUCT_SOCKADDR
#define PyObjC_STRUCT_SOCKADDR

extern int PyObjC_SockAddrFromPython(PyObject*, void*);
extern PyObject* PyObjC_SockAddrToPython(void*);

#endif /*PyObjC_STRUCT_SOCKADDR */
