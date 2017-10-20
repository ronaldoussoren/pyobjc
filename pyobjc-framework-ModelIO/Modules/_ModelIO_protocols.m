static void __attribute__((__used__)) use_protocols(void)
{
    PyObject* p __attribute__((__unused__));
    p = PyObjC_IdToPython(@protocol(MDLComponent)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MDLLightProbeIrradianceDataSource)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MDLMeshBuffer)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MDLMeshBufferAllocator)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MDLMeshBufferZone)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MDLNamed)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MDLObjectContainerComponent)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MDLTransformComponent)); Py_XDECREF(p);
#if PyObjC_BUILD_RELEASE >= 1013
    p = PyObjC_IdToPython(@protocol(MDLAssetResolver)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MDLJointAnimation)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MDLTransformOp)); Py_XDECREF(p);
#endif
}
