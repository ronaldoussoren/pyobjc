from PyObjCTools.TestSupport import *
from AppKit import *

# Would like some tests for NSRunAlertPanel and friends as well, but those
# require user interaction :-(

class TestAlertFormat (TestCase):
    def testSimple(self):
        alert = NSAlert.alertWithMessageText_defaultButton_alternateButton_otherButton_informativeTextWithFormat_(
                "message text", "ok", "cancel", "help", "foobar is the sucks")
        self.assertEqual(alert.messageText(), "message text")
        self.assertEqual(alert.informativeText(), "foobar is the sucks")

    def testWithFormat(self):
        alert = NSAlert.alertWithMessageText_defaultButton_alternateButton_otherButton_informativeTextWithFormat_(
                "message text", "ok", "cancel", "help", "%d * %d = %d", 9, 7, 9*7)
        self.assertEqual(alert.messageText(), "message text")
        self.assertEqual(alert.informativeText(), "9 * 7 = 63")

if __name__ == "__main__":
    main()
