import CFOpenDirectory
from PyObjCTools.TestSupport import TestCase


class TestCFOpenDirectory(TestCase):
    def test_classes(self):
        self.assertIsCFType(CFOpenDirectory.ODContextRef)
        self.assertIsCFType(CFOpenDirectory.ODNodeRef)
        self.assertIsCFType(CFOpenDirectory.ODQueryRef)
        self.assertIsCFType(CFOpenDirectory.ODRecordRef)
        self.assertIsCFType(CFOpenDirectory.ODSessionRef)

    def test_constants(self):
        self.assertIsInstance(CFOpenDirectory.kODErrorDomainFramework, str)
