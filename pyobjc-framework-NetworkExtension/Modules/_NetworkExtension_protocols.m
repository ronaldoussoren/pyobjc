/*
 * This file is generated by objective.metadata
 *
 * Last update: Wed Jan 16 13:10:52 2013
 */
static void __attribute__((__used__))
use_protocols(void)
{
    PyObject* p __attribute__((__unused__));
#if PyObjC_BUILD_RELEASE >= 1011
    p = PyObjC_IdToPython(@protocol(NWTCPConnectionAuthenticationDelegate));
    Py_XDECREF(p);
#endif
}
