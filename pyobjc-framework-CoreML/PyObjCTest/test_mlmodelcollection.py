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
