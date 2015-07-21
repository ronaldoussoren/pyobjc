from PyObjCTools.TestSupport import *
from AddressBook import *

class TestABPersonPickerDelegate (TestCase):
    def test_protocols(self):
        objc.protocolNamed('ABPersonPickerDelegate')

if __name__ == "__main__":
    main()
