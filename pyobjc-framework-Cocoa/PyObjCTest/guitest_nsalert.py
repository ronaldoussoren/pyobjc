import Cocoa
from PyObjCTools.TestSupport import TestCase, os_level_key, os_release, skipUnless

# Would like some tests for NSRunAlertPanel and friends as well, but those
# require user interaction :-(


class TestAlertFormat(TestCase):
    @skipUnless(
        not (os_level_key("10.13") <= os_level_key(os_release()) < os_level_key("10.15")),
        "Crash on 10.13, 10.14??",
    )
    @skipUnless(
        not (os_level_key("15.0") <= os_level_key(os_release()) < os_level_key("15.1")),
        "Crash on macOS 15 beta",
    )
    def testSimple(self):
        alert = Cocoa.NSAlert.alertWithMessageText_defaultButton_alternateButton_otherButton_informativeTextWithFormat_(  # noqa: B950
            "message text", "ok", "cancel", "help", "foobar is the sucks"
        )
        self.assertEqual(alert.messageText(), "message text")
        self.assertEqual(alert.informativeText(), "foobar is the sucks")

    @skipUnless(
        not (os_level_key("10.13") <= os_level_key(os_release()) < os_level_key("10.15")),
        "Crash on 10.13, 10.14??",
    )
    @skipUnless(
        not (os_level_key("15.0") <= os_level_key(os_release()) < os_level_key("15.1")),
        "Crash on macOS 15 beta",
    )
    def testWithFormat(self):
        alert = Cocoa.NSAlert.alertWithMessageText_defaultButton_alternateButton_otherButton_informativeTextWithFormat_(  # noqa: B950
            "message text", "ok", "cancel", "help", "%d * %d = %d", 9, 7, 9 * 7
        )
        self.assertEqual(alert.messageText(), "message text")
        self.assertEqual(alert.informativeText(), "9 * 7 = 63")
