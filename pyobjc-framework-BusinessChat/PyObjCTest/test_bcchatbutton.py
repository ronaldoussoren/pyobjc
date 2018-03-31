from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2 ** 32:
    import BusinessChat

    class TestBCChatButton (TestCase):
        def test_constants(self):
            self.assertEqual(BusinessChat.BCChatButtonStyleLight, 0)
            self.assertEqual(BusinessChat.BCChatButtonStyleDark, 1)

        def test_classes(self):
            BusinessChat.BCChatButton



if __name__ == "__main__":
    main()
