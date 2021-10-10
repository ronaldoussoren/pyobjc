static void __attribute__((__used__)) use_protocols(void)
{
    PyObject* p __attribute__((__unused__));

    p = PyObjC_IdToPython(@protocol(UNUserNotificationCenterDelegate));
    Py_XDECREF(p);

#if PyObjC_BUILD_RELEASE >= 1200
    p = PyObjC_IdToPython(@protocol(UNNotificationContentProviding));
    Py_XDECREF(p);
#endif
}
