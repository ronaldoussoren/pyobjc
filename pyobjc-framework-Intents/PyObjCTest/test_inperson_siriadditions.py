import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import Intents

    class TestINPersonSiriAdditions (TestCase):
        @min_os_level('10.14')
        def test_methods(self):
            self.assertArgIsBOOL(Intents.INPerson.initWithPersonHandle_nameComponents_displayName_image_contactIdentifier_customIdentifier_isMe_, 6)


if __name__ == "__main__":
    main()
