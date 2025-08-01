/*
 * This file is generated by objective.metadata
 *
 * Last update: Thu Aug 22 22:15:16 2024
 */

static void __attribute__((__used__))
use_protocols(void)
{
    PyObject* p __attribute__((__unused__));
#if PyObjC_BUILD_RELEASE >= 1504
    p = PyObjC_IdToPython(@protocol(FSFileSystemBase));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(FSManageableResourceMaintenanceOperations));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(FSUnaryFileSystemOperations));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(FSVolumePathConfOperations));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(FSVolumeOperations));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(FSVolumeXattrOperations));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(FSVolumeOpenCloseOperations));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(FSVolumeReadWriteOperations));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(FSVolumeAccessCheckOperations));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(FSVolumeRenameOperations));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(FSVolumePreallocateOperations));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(FSVolumeItemDeactivation));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(FSVolumeKernelOffloadedIOOperations));
    Py_XDECREF(p);
#endif /* PyObjC_BUILD_RELEASE >= 1501 */
}
