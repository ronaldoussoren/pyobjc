from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2 ** 32:
    import BusinessChat

    class TestBCChatAction (TestCase):
        def test_constants(self):
            self.assertIsInstance(BusinessChat.BCParameterNameIntent, unicode)
            self.assertIsInstance(BusinessChat.BCParameterNameGroup, unicode)
            self.assertIsInstance(BusinessChat.BCParameterNameBody, unicode)

        def test_classes(self):
            BusinessChat.BCChatAction



if __name__ == "__main__":
    main()
