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
        self.assertResultIsCFRetained(CFNetworkCopyProxiesForURL)
        url = CFURLCreateWithString(None, "http://www.apple.com/", None)
        v = CFNetworkCopyProxiesForURL(url, None)
        self.assertIsInstance(v, CFArrayRef)

        self.assertResultIsCFRetained(CFNetworkCopyProxiesForAutoConfigurationScript)
        self.assertArgIsOut(CFNetworkCopyProxiesForAutoConfigurationScript, 2)
        v, err  = CFNetworkCopyProxiesForAutoConfigurationScript(
                SCRIPT, url, None)
        self.assertTrue(err is None)
        self.assertIsInstance(v, CFArrayRef)
        x = v[0]
        self.assertEqual(x[kCFProxyTypeKey], kCFProxyTypeHTTP)
        self.assertEqual(x[kCFProxyHostNameKey], "proxy.apple.com")
        self.assertEqual(x[kCFProxyPortNumberKey], 8080)

        self.assertResultIsCFRetained(CFNetworkCopySystemProxySettings)
        v = CFNetworkCopySystemProxySettings()
        self.assertIsInstance(v, CFDictionaryRef)


    @min_os_level('10.5')
    def testManual(self):
        lst = []
        ctx = object()
        def callback(ctx, proxies, error):
            lst.append([ctx, proxies, error])

        url = CFURLCreateWithString(None, "http://www.apple.com/", None)
        
        rls = CFNetworkExecuteProxyAutoConfigurationScript(
                SCRIPT, url, callback, ctx)
        self.assertIsInstance(rls, CFRunLoopSourceRef)

        rl = CFRunLoopGetCurrent()
        CFRunLoopAddSource(rl, rls,  kCFRunLoopCommonModes)

        CFRunLoopRunInMode(kCFRunLoopDefaultMode, 1.0, True)

        CFRunLoopRemoveSource(rl, rls,  kCFRunLoopCommonModes)

        self.assertNotEqual(len(lst), 0)
        self.assertTrue(lst[0][0] is ctx)
        self.assertIsInstance(lst[0][1], CFArrayRef)
        self.assertEqual(lst[0][2],  None)

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
        self.assertIsInstance(rls, CFRunLoopSourceRef)

        CFRunLoopAddSource(rl, rls,  kCFRunLoopCommonModes)

        CFRunLoopRunInMode(kCFRunLoopDefaultMode, 1.0, True)

        CFRunLoopRemoveSource(rl, rls,  kCFRunLoopCommonModes)

        #print lst

        self.assertNotEqual(len(lst), 0)
        self.assertTrue(lst[0][0] is ctx)
        if lst[0][2] is None:
            self.assertIsInstance(lst[0][1], CFArrayRef)
            self.assertEqual(lst[0][2],  None)

        else:
            self.assertEqual(lst[0][1],  None)
            self.assertIsInstance(lst[0][2], CFErrorRef)


        

    @min_os_level('10.5')
    def testConstants(self):
        self.assertIsInstance(kCFProxyTypeKey, unicode)
        self.assertIsInstance(kCFProxyHostNameKey, unicode)
        self.assertIsInstance(kCFProxyPortNumberKey, unicode)
        self.assertIsInstance(kCFProxyAutoConfigurationURLKey, unicode)
        self.assertIsInstance(kCFProxyUsernameKey, unicode)
        self.assertIsInstance(kCFProxyPasswordKey, unicode)
        self.assertIsInstance(kCFProxyTypeNone, unicode)
        self.assertIsInstance(kCFProxyTypeHTTP, unicode)
        self.assertIsInstance(kCFProxyTypeHTTPS, unicode)
        self.assertIsInstance(kCFProxyTypeSOCKS, unicode)
        self.assertIsInstance(kCFProxyTypeFTP, unicode)
        self.assertIsInstance(kCFProxyTypeAutoConfigurationURL, unicode)
        self.assertIsInstance(kCFNetworkProxiesHTTPEnable, unicode)
        self.assertIsInstance(kCFNetworkProxiesHTTPPort, unicode)
        self.assertIsInstance(kCFNetworkProxiesHTTPProxy, unicode)
        self.assertIsInstance(kCFNetworkProxiesProxyAutoConfigEnable, unicode)
        self.assertIsInstance(kCFNetworkProxiesProxyAutoConfigURLString, unicode)

    @expectedFailure
    @min_os_level('10.5')
    def testConstants_fail(self):
        self.assertIsIn('kCFProxyAutoConfigurationHTTPResponseKey', globals())
        self.assertIsInstance(kCFProxyAutoConfigurationHTTPResponseKey, unicode)

    @min_os_level('10.6')
    def testFunctions10_6(self):
        r = CFNetworkCopySystemProxySettings()
        self.assertIsInstance(r, CFDictionaryRef)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertIsInstance(kCFNetworkProxiesExceptionsList, unicode)
        self.assertIsInstance(kCFNetworkProxiesExcludeSimpleHostnames, unicode)
        self.assertIsInstance(kCFNetworkProxiesFTPEnable, unicode)
        self.assertIsInstance(kCFNetworkProxiesFTPPassive, unicode)
        self.assertIsInstance(kCFNetworkProxiesFTPPort, unicode)
        self.assertIsInstance(kCFNetworkProxiesFTPProxy, unicode)
        self.assertIsInstance(kCFNetworkProxiesGopherEnable, unicode)
        self.assertIsInstance(kCFNetworkProxiesGopherPort, unicode)
        self.assertIsInstance(kCFNetworkProxiesGopherProxy, unicode)
        self.assertIsInstance(kCFNetworkProxiesHTTPSEnable, unicode)
        self.assertIsInstance(kCFNetworkProxiesHTTPSPort, unicode)
        self.assertIsInstance(kCFNetworkProxiesHTTPSProxy, unicode)
        self.assertIsInstance(kCFNetworkProxiesRTSPEnable, unicode)
        self.assertIsInstance(kCFNetworkProxiesRTSPPort, unicode)
        self.assertIsInstance(kCFNetworkProxiesRTSPProxy, unicode)
        self.assertIsInstance(kCFNetworkProxiesSOCKSEnable, unicode)
        self.assertIsInstance(kCFNetworkProxiesSOCKSPort, unicode)
        self.assertIsInstance(kCFNetworkProxiesSOCKSProxy, unicode)



if __name__ == "__main__":
    main()
