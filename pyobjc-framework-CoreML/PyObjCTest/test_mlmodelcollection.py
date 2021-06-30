from PyObjCTools.TestSupport import TestCase, min_os_level
import CoreML


class TestMLModelCollection(TestCase):
    @min_os_level("11.0")
    def test_constants11_0(self):
        self.assertIsInstance(CoreML.MLModelCollectionDidChangeNotification, str)

    @min_os_level("11.0")
    def test_methods11_0(self):
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
