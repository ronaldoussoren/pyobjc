/*
 * This file is generated by objective.metadata
 *
 * Last update: Wed Jan 16 13:10:52 2013
 */

static void __attribute__((__used__))
use_protocols(void)
{
    PyObject* p __attribute__((__unused__));
#if PyObjC_BUILD_RELEASE >= 1016
    p = PyObjC_IdToPython(@protocol(VZVirtioSocketListenerDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(VZVirtualMachineDelegate));
    Py_XDECREF(p);
#endif
#if PyObjC_BUILD_RELEASE >= 1300
    p = PyObjC_IdToPython(@protocol(VZVirtioConsoleDeviceDelegate));
    Py_XDECREF(p);
#endif
#if PyObjC_BUILD_RELEASE >= 1400
    p = PyObjC_IdToPython(@protocol(VZGraphicsDisplayObserver));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(VZNetworkBlockDeviceStorageDeviceAttachmentDelegate));
    Py_XDECREF(p);
#endif
#if PyObjC_BUILD_RELEASE >= 1500
    p = PyObjC_IdToPython(@protocol(VZUSBDeviceConfiguration));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(VZUSBDevice));
    Py_XDECREF(p);
#endif
}
