import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import Intents

    class TestINParameter (TestCase):
        @min_os_level('10.14')
        def test_methods(self):
            self.assertResultIsBOOL(Intents.INParameter.isEqualToParameter_)


if __name__ == "__main__":
    main()
