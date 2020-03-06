import os

import CFNetwork
from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure

SCRIPT = """
function FindProxyForURL(url, host) {
   if (shExpMatch(host, "*.apple.com")) {
      return "PROXY proxy.apple.com:8080";
   }
   return "DIRECT";
}
"""


class TestCFProxySupport(TestCase):
    @min_os_level("10.5")
    def testFunctions(self):
        self.assertResultIsCFRetained(CFNetwork.CFNetworkCopyProxiesForURL)
        url = CFNetwork.CFURLCreateWithString(None, "http://www.apple.com/", None)
        v = CFNetwork.CFNetworkCopyProxiesForURL(url, None)
        self.assertIsInstance(v, CFNetwork.CFArrayRef)

        self.assertResultIsCFRetained(
            CFNetwork.CFNetworkCopyProxiesForAutoConfigurationScript
        )
        self.assertArgIsOut(CFNetwork.CFNetworkCopyProxiesForAutoConfigurationScript, 2)
        v, err = CFNetwork.CFNetworkCopyProxiesForAutoConfigurationScript(
            SCRIPT, url, None
        )
        self.assertTrue(err is None)
        self.assertIsInstance(v, CFNetwork.CFArrayRef)
        x = v[0]
        self.assertEqual(x[CFNetwork.kCFProxyTypeKey], CFNetwork.kCFProxyTypeHTTP)
        self.assertEqual(x[CFNetwork.kCFProxyHostNameKey], "proxy.apple.com")
        self.assertEqual(x[CFNetwork.kCFProxyPortNumberKey], 8080)

        self.assertResultIsCFRetained(CFNetwork.CFNetworkCopySystemProxySettings)
        v = CFNetwork.CFNetworkCopySystemProxySettings()
        self.assertIsInstance(v, CFNetwork.CFDictionaryRef)

    @min_os_level("10.5")
    def testManual(self):
        lst = []
        ctx = object()

        def callback(ctx, proxies, error):
            lst.append([ctx, proxies, error])

        url = CFNetwork.CFURLCreateWithString(None, "http://www.apple.com/", None)

        rls = CFNetwork.CFNetworkExecuteProxyAutoConfigurationScript(
            SCRIPT, url, callback, ctx
        )
        self.assertIsInstance(rls, CFNetwork.CFRunLoopSourceRef)

        rl = CFNetwork.CFRunLoopGetCurrent()
        CFNetwork.CFRunLoopAddSource(rl, rls, CFNetwork.kCFRunLoopCommonModes)

        CFNetwork.CFRunLoopRunInMode(CFNetwork.kCFRunLoopDefaultMode, 1.0, False)

        CFNetwork.CFRunLoopRemoveSource(rl, rls, CFNetwork.kCFRunLoopCommonModes)

        self.assertNotEqual(len(lst), 0)
        self.assertTrue(lst[0][0] is ctx)
        self.assertIsInstance(lst[0][1], CFNetwork.CFArrayRef)
        self.assertEqual(lst[0][2], None)

        lst[:] = []
        path = os.path.join(os.path.dirname(__file__), "proxy.pac")
        cwd = os.getcwd()
        if path.startswith(cwd):
            path = path[len(cwd) + 1 :]
        scriptURL = CFNetwork.CFURLCreateWithFileSystemPath(
            None, path, CFNetwork.kCFURLPOSIXPathStyle, False
        )

        rls = CFNetwork.CFNetworkExecuteProxyAutoConfigurationURL(
            scriptURL, url, callback, ctx
        )
        self.assertIsInstance(rls, CFNetwork.CFRunLoopSourceRef)

        CFNetwork.CFRunLoopAddSource(rl, rls, CFNetwork.kCFRunLoopCommonModes)

        CFNetwork.CFRunLoopRunInMode(CFNetwork.kCFRunLoopDefaultMode, 1.0, True)

        CFNetwork.CFRunLoopRemoveSource(rl, rls, CFNetwork.kCFRunLoopCommonModes)

        # print lst

        self.assertNotEqual(len(lst), 0)
        self.assertTrue(lst[0][0] is ctx)
        if lst[0][2] is None:
            self.assertIsInstance(lst[0][1], CFNetwork.CFArrayRef)
            self.assertEqual(lst[0][2], None)

        else:
            self.assertEqual(lst[0][1], None)
            self.assertIsInstance(lst[0][2], CFNetwork.CFErrorRef)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertIsInstance(CFNetwork.kCFProxyAutoConfigurationJavaScriptKey, str)
        self.assertIsInstance(CFNetwork.kCFProxyTypeAutoConfigurationJavaScript, str)

    @expectedFailure
    @min_os_level("10.7")
    def testConstants10_7_failure(self):
        self.assertIsInstance(CFNetwork.kCFNetworkProxiesProxyAutoConfigJavaScript, str)

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertIsInstance(CFNetwork.kCFProxyTypeKey, str)
        self.assertIsInstance(CFNetwork.kCFProxyHostNameKey, str)
        self.assertIsInstance(CFNetwork.kCFProxyPortNumberKey, str)
        self.assertIsInstance(CFNetwork.kCFProxyAutoConfigurationURLKey, str)
        self.assertIsInstance(CFNetwork.kCFProxyUsernameKey, str)
        self.assertIsInstance(CFNetwork.kCFProxyPasswordKey, str)
        self.assertIsInstance(CFNetwork.kCFProxyTypeNone, str)
        self.assertIsInstance(CFNetwork.kCFProxyTypeHTTP, str)
        self.assertIsInstance(CFNetwork.kCFProxyTypeHTTPS, str)
        self.assertIsInstance(CFNetwork.kCFProxyTypeSOCKS, str)
        self.assertIsInstance(CFNetwork.kCFProxyTypeFTP, str)
        self.assertIsInstance(CFNetwork.kCFProxyTypeAutoConfigurationURL, str)
        self.assertIsInstance(CFNetwork.kCFNetworkProxiesHTTPEnable, str)
        self.assertIsInstance(CFNetwork.kCFNetworkProxiesHTTPPort, str)
        self.assertIsInstance(CFNetwork.kCFNetworkProxiesHTTPProxy, str)

    @expectedFailure
    @min_os_level("10.5")
    def testConstants_fail(self):
        self.assertHasAttr(CFNetwork, "kCFProxyAutoConfigurationHTTPResponseKey")
        self.assertIsInstance(CFNetwork.kCFProxyAutoConfigurationHTTPResponseKey, str)

    @min_os_level("10.6")
    def testFunctions10_6(self):
        r = CFNetwork.CFNetworkCopySystemProxySettings()
        self.assertIsInstance(r, CFNetwork.CFDictionaryRef)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertIsInstance(CFNetwork.kCFNetworkProxiesExceptionsList, str)
        self.assertIsInstance(CFNetwork.kCFNetworkProxiesExcludeSimpleHostnames, str)
        self.assertIsInstance(CFNetwork.kCFNetworkProxiesFTPEnable, str)
        self.assertIsInstance(CFNetwork.kCFNetworkProxiesFTPPassive, str)
        self.assertIsInstance(CFNetwork.kCFNetworkProxiesFTPPort, str)
        self.assertIsInstance(CFNetwork.kCFNetworkProxiesFTPProxy, str)
        self.assertIsInstance(CFNetwork.kCFNetworkProxiesGopherEnable, str)
        self.assertIsInstance(CFNetwork.kCFNetworkProxiesGopherPort, str)
        self.assertIsInstance(CFNetwork.kCFNetworkProxiesGopherProxy, str)
        self.assertIsInstance(CFNetwork.kCFNetworkProxiesHTTPSEnable, str)
        self.assertIsInstance(CFNetwork.kCFNetworkProxiesHTTPSPort, str)
        self.assertIsInstance(CFNetwork.kCFNetworkProxiesHTTPSProxy, str)
        self.assertIsInstance(CFNetwork.kCFNetworkProxiesRTSPEnable, str)
        self.assertIsInstance(CFNetwork.kCFNetworkProxiesRTSPPort, str)
        self.assertIsInstance(CFNetwork.kCFNetworkProxiesRTSPProxy, str)
        self.assertIsInstance(CFNetwork.kCFNetworkProxiesSOCKSEnable, str)
        self.assertIsInstance(CFNetwork.kCFNetworkProxiesSOCKSPort, str)
        self.assertIsInstance(CFNetwork.kCFNetworkProxiesSOCKSProxy, str)
        self.assertIsInstance(CFNetwork.kCFNetworkProxiesProxyAutoConfigEnable, str)
        self.assertIsInstance(CFNetwork.kCFNetworkProxiesProxyAutoConfigURLString, str)
        self.assertIsInstance(CFNetwork.kCFNetworkProxiesProxyAutoDiscoveryEnable, str)
