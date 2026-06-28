import Foundation
from PyObjCTools.TestSupport import TestCase

NSUserScriptTaskCompletionHandler = b"v@"
NSUserUnixTaskCompletionHandler = b"v@"
NSUserAppleScriptTaskCompletionHandler = b"v@@"
NSUserAutomatorTaskCompletionHandler = b"@@"


class TestNSUserScriptTask(TestCase):
    def test_methods(self):
        self.assertArgIsOut(Foundation.NSUserScriptTask.initWithURL_error_, 1)
        self.assertArgIsBlock(
            Foundation.NSUserScriptTask.executeWithCompletionHandler_,
            0,
            NSUserScriptTaskCompletionHandler,
        )
        self.assertArgIsBlock(
            Foundation.NSUserUnixTask.executeWithArguments_completionHandler_,
            1,
            NSUserUnixTaskCompletionHandler,
        )
        self.assertArgIsBlock(
            Foundation.NSUserAppleScriptTask.executeWithAppleEvent_completionHandler_,
            1,
            NSUserAppleScriptTaskCompletionHandler,
        )
        self.assertArgIsBlock(
            Foundation.NSUserAutomatorTask.executeWithInput_completionHandler_,
            1,
            NSUserAutomatorTaskCompletionHandler,
        )
