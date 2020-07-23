from PyObjCTools.TestSupport import TestCase, min_os_level
import CoreML


class TestMLModelCollection(TestCase):
    @min_os_level("10.16")
    def test_constants(self):
        self.assertIsInstance(CoreML.MLModelCollectionDidChangeNotification, str)

    @min_os_level("10.16")
    def test_methods(self):
        self.assertResultIsBOOL(CoreML.MLModelCollection.isSynchronizationEnabled)
        self.assertArgIsBOOL(CoreML.MLModelCollection.setIsSynchronizationEnabled_, 0)

        self.assertArgIsBlock(
            CoreML.MLModelCollection.beginAccessingModelCollectionWithIdentifier_completionHandler_,
            1,
            b"v@@",
        )

        self.assertArgIsBlock(
            CoreML.MLModelCollection.endAccessingModelCollectionWithIdentifier_completionHandler_,
            1,
            b"vZ@",
        )
