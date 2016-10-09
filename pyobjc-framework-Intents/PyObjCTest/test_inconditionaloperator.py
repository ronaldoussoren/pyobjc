import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import Intents

    class TestINConditionalOperator (TestCase):
        @min_os_level('10.12')
        def testConstants(self):
            self.assertEqual(Intents.INConditionalOperatorAll, 0)
            self.assertEqual(Intents.INConditionalOperatorAny, 1)
            self.assertEqual(Intents.INConditionalOperatorNone, 2)


if __name__ == "__main__":
    main()
