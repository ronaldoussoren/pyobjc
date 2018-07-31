import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import Intents

    class TestINPerson (TestCase):
        @min_os_level('10.12')
        def testConstants(self):
            self.assertEqual(Intents.INPersonSuggestionTypeNone, 0)
            self.assertEqual(Intents.INPersonSuggestionTypeSocialProfile, 1)
            self.assertEqual(Intents.INPersonSuggestionTypeInstantMessageAddress, 2)


if __name__ == "__main__":
    main()
