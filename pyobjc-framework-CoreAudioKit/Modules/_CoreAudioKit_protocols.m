static void __attribute__((__used__))
use_protocols(void)
{
    PyObject* p __attribute__((__unused__));
    p = PyObjC_IdToPython(@protocol(AUCustomViewPersistentData));
    Py_XDECREF(p);
}
