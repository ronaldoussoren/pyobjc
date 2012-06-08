
from PyObjCTools.TestSupport import *
from InputMethodKit import *
import InputMethodKit

try:
    unicode
except NameError:
    unicode = str

class TestIMKServer (TestCase):
    @min_os_level('10.6')
    @expectedFailure
    def testConstants(self):
        # The definitions below are defined on 10.5, but not actually
        # exported by the framework. That's why this test is only
        # enabled for 10.6 or later.
        # NOTE: I have no idea if the tests will pass there, this
        # is just to avoid false negatives on 10.5
        # See also: Radar #6783035
        self.assertTrue(hasattr(InputMethodKit, 'IMKDelegateClass'))
        self.assertIsInstance(IMKDelegateClass, unicode)
        self.assertTrue(hasattr(InputMethodKit, 'IMKControllerClass'))
        self.assertIsInstance(IMKControllerClass, unicode)


if __name__ == "__main__":
    main()
