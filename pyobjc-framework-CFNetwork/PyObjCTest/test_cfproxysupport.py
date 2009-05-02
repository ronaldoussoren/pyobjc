from PyObjCTools.TestSupport import *
from CFNetwork import *
import os

SCRIPT="""
function FindProxyForURL(url, host) {
   if (shExpMatch(host, "*.apple.com")) {
      return "PROXY proxy.apple.com:8080";
   }
   return "DIRECT";
}
"""

class TestCFProxySupport (TestCase):

    @min_os_level('10.5')
    def testFunctions(self):
        self.failUnlessResultIsCFRetained(CFNetworkCopyProxiesForURL)
        url = CFURLCreateWithString(None, "http://www.apple.com/", None)
        v = CFNetworkCopyProxiesForURL(url, None)
        self.failUnlessIsInstance(v, CFArrayRef)

        self.failUnlessResultIsCFRetained(CFNetworkCopyProxiesForAutoConfigurationScript)
        self.failUnlessArgIsOut(CFNetworkCopyProxiesForAutoConfigurationScript, 2)
        v, err  = CFNetworkCopyProxiesForAutoConfigurationScript(
                SCRIPT, url, None)
        self.failUnless(err is None)
        self.failUnlessIsInstance(v, CFArrayRef)
        x = v[0]
        self.failUnlessEqual(x[kCFProxyTypeKey], kCFProxyTypeHTTP)
        self.failUnlessEqual(x[kCFProxyHostNameKey], "proxy.apple.com")
        self.failUnlessEqual(x[kCFProxyPortNumberKey], 8080)

        self.failUnlessResultIsCFRetained(CFNetworkCopySystemProxySettings)
        v = CFNetworkCopySystemProxySettings()
        self.failUnlessIsInstance(v, CFDictionaryRef)


    @min_os_level('10.5')
    def testManual(self):
        lst = []
        ctx = object()
        def callback(ctx, proxies, error):
            lst.append([ctx, proxies, error])

        url = CFURLCreateWithString(None, "http://www.apple.com/", None)
        
        rls = CFNetworkExecuteProxyAutoConfigurationScript(
                SCRIPT, url, callback, ctx)
        self.failUnlessIsInstance(rls, CFRunLoopSourceRef)

        rl = CFRunLoopGetCurrent()
        CFRunLoopAddSource(rl, rls,  kCFRunLoopCommonModes)

        CFRunLoopRunInMode(kCFRunLoopDefaultMode, 1.0, True)

        CFRunLoopRemoveSource(rl, rls,  kCFRunLoopCommonModes)

        self.failIfEqual(len(lst), 0)
        self.failUnless(lst[0][0] is ctx)
        self.failUnlessIsInstance(lst[0][1], CFArrayRef)
        self.failUnlessEqual(lst[0][2],  None)

        lst[:] = []
        path = os.path.join(os.path.dirname(__file__), "proxy.pac")
        cwd = os.getcwd()
        if path.startswith(cwd):
            path = path[len(cwd)+1:]
        scriptURL = CFURLCreateWithFileSystemPath(
                None,
                path,
                kCFURLPOSIXPathStyle,
                False)

        rls = CFNetworkExecuteProxyAutoConfigurationURL(
                scriptURL, url, callback, ctx)
        self.failUnlessIsInstance(rls, CFRunLoopSourceRef)

        CFRunLoopAddSource(rl, rls,  kCFRunLoopCommonModes)

        CFRunLoopRunInMode(kCFRunLoopDefaultMode, 1.0, True)

        CFRunLoopRemoveSource(rl, rls,  kCFRunLoopCommonModes)

        #print lst

        self.failIfEqual(len(lst), 0)
        self.failUnless(lst[0][0] is ctx)
        if lst[0][2] is None:
            self.failUnlessIsInstance(lst[0][1], CFArrayRef)
            self.failUnlessEqual(lst[0][2],  None)

        else:
            self.failUnlessEqual(lst[0][1],  None)
            self.failUnlessIsInstance(lst[0][2], CFErrorRef)


        

    @min_os_level('10.5')
    def testConstants(self):
        self.failUnlessIsInstance(kCFProxyTypeKey, unicode)
        self.failUnlessIsInstance(kCFProxyHostNameKey, unicode)
        self.failUnlessIsInstance(kCFProxyPortNumberKey, unicode)
        self.failUnlessIsInstance(kCFProxyAutoConfigurationURLKey, unicode)
        self.failUnlessIsInstance(kCFProxyUsernameKey, unicode)
        self.failUnlessIsInstance(kCFProxyPasswordKey, unicode)
        self.failUnlessIsInstance(kCFProxyTypeNone, unicode)
        self.failUnlessIsInstance(kCFProxyTypeHTTP, unicode)
        self.failUnlessIsInstance(kCFProxyTypeHTTPS, unicode)
        self.failUnlessIsInstance(kCFProxyTypeSOCKS, unicode)
        self.failUnlessIsInstance(kCFProxyTypeFTP, unicode)
        self.failUnlessIsInstance(kCFProxyTypeAutoConfigurationURL, unicode)
        self.failUnlessIsInstance(kCFNetworkProxiesHTTPEnable, unicode)
        self.failUnlessIsInstance(kCFNetworkProxiesHTTPPort, unicode)
        self.failUnlessIsInstance(kCFNetworkProxiesHTTPProxy, unicode)
        self.failUnlessIsInstance(kCFNetworkProxiesProxyAutoConfigEnable, unicode)
        self.failUnlessIsInstance(kCFNetworkProxiesProxyAutoConfigURLString, unicode)


if __name__ == "__main__":
    main()
