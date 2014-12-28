from PyObjCTools.TestSupport import *

import JavaScriptCore
import objc

class TestJSManagedValue (TestCase):
    @onlyOn64Bit
    @min_os_level('10.9')
    def test_classes(self):
        self.assertHasAttr(JavaScriptCore, 'JSManagedValue')

if __name__ == "__main__":
    main()
