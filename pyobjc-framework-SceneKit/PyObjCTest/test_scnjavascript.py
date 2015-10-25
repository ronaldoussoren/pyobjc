from PyObjCTools.TestSupport import *
import objc

import SceneKit

class TestSCNJavascript (TestCase):
    @min_os_level('10.10')
    def testFunctions(self):
        SceneKit.SCNExportJavaScriptModule


if __name__ == "__main__":
    main()
