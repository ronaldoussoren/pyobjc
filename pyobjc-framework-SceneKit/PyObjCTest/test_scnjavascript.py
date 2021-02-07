from PyObjCTools.TestSupport import TestCase, min_os_level

import SceneKit


class TestSCNJavascript(TestCase):
    @min_os_level("10.10")
    def testFunctions(self):
        SceneKit.SCNExportJavaScriptModule
