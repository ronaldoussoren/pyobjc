static void __attribute__((__used__)) use_protocols(void)
{
    PyObject* p __attribute__((__unused__));
    #if 0
    p = PyObjC_IdToPython(@protocol(MTKViewDelegate));
    Py_XDECREF(p);
    #endif
}
