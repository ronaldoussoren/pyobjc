/*
 * This file is generated by objective.metadata
 *
 * Last update: Wed Jan 16 13:10:52 2013
 */

static void __attribute__((__used__)) use_protocols(void)
{
    PyObject* p __attribute__((__unused__));
#if PyObjC_BUILD_RELEASE >= 1016
    p = PyObjC_IdToPython(@protocol(PKPaymentAuthorizationControllerDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(PKPaymentAuthorizationViewControllerDelegate));
    Py_XDECREF(p);

    // XXX: Investigate
    // p = PyObjC_IdToPython(@protocol(PKDisbursementAuthorizationControllerDelegate));
    // Py_XDECREF(p);
#endif
}
