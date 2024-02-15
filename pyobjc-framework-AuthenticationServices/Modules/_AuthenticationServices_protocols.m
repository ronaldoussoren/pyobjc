static void __attribute__((__used__)) use_protocols(void)
{
    PyObject* p __attribute__((__unused__));
#if PyObjC_BUILD_RELEASE >= 1015
    p = PyObjC_IdToPython(@protocol(ASAuthorizationControllerDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(
        @protocol(ASAuthorizationControllerPresentationContextProviding));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(ASAuthorizationCredential));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(ASAuthorizationProvider));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(ASWebAuthenticationPresentationContextProviding));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(ASWebAuthenticationSessionRequestDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(ASWebAuthenticationSessionWebBrowserSessionHandling));
    Py_XDECREF(p);
#endif
#if PyObjC_BUILD_RELEASE >= 1300
    p = PyObjC_IdToPython(@protocol(ASAuthorizationProviderExtensionRegistrationHandler));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(
        @protocol(ASAuthorizationWebBrowserPlatformPublicKeyCredentialProvider));
    Py_XDECREF(p);
#endif
#if PyObjC_BUILD_RELEASE >= 1400
    p = PyObjC_IdToPython(
        @protocol(ASAuthorizationWebBrowserPlatformPublicKeyCredentialAssertionRequest));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(
        ASAuthorizationWebBrowserPlatformPublicKeyCredentialRegistrationRequest));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(ASCredentialRequest));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(ASCredentialIdentity));
    Py_XDECREF(p);
#endif
#if PyObjC_BUILD_RELEASE >= 1404
    p = PyObjC_IdToPython(
        @protocol(ASAuthorizationWebBrowserSecurityKeyPublicKeyCredentialAssertionRequest));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(
        @protocol(ASAuthorizationWebBrowserSecurityKeyPublicKeyCredentialProvider));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(
        @protocol(ASAuthorizationWebBrowserSecurityKeyPublicKeyCredentialRegistrationRequest));
    Py_XDECREF(p);
#endif
}
