from PyObjCTools.TestSupport import TestCase, expectedFailure

import FSKit


class TestFSClient(TestCase):
    def test_constants(self):
        self.assertIsInstance(FSKit.FSCheckOptionSyntaxKey, str)
        self.assertIsInstance(FSKit.FSFormatOptionSyntaxKey, str)
        self.assertIsInstance(FSKit.FSActivateOptionSyntaxKey, str)

    def test_methods(self):
        self.assertArgIsBlock(
            FSKit.FSTaskOptionsBundle.bundleForArguments_count_extension_operationType_errorHandler_,
            4,
            b"v@@",
        )
        self.assertArgIsBlock(
            FSKit.FSTaskOptionsBundle.enumerateOptionsWithBlock_, 0, b"vi@Qo^Z"
        )

    @expectedFailure
    def test_methods_unsupported(self):
        self.fail("argv support!")
