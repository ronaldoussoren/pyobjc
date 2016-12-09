from PyObjCTools.TestSupport import *
import objc
import sys

if os_level_key(os_release()) < os_level_key('10.12') or sys.maxsize >= 2**32:
    import SceneKit

    class TestSCNJavascript (TestCase):
        @min_os_level('10.10')
        def testFunctions(self):
            SceneKit.SCNExportJavaScriptModule


if __name__ == "__main__":
    main()
