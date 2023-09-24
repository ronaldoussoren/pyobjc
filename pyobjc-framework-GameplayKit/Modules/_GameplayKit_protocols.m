static void __attribute__((__used__)) use_protocols(void)
{
    PyObject* p __attribute__((__unused__));
    p = PyObjC_IdToPython(@protocol(GKAgentDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(GKGameModelUpdate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(GKGameModelPlayer));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(GKGameModel));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(GKRandom));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(GKStrategist));
    Py_XDECREF(p);
#if PyObjC_BUILD_RELEASE >= 1012
    p = PyObjC_IdToPython(@protocol(GKSceneRootNodeType));
    Py_XDECREF(p);
#endif
}
