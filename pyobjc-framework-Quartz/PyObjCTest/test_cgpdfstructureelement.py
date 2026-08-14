from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestCGPDFStructureElement(TestCase):
    @min_os_level("27.0")
    def test_types(self):
        self.assertIsCFType(Quartz.CGPDFStructureElementRef, unique=False)

    @min_os_level("27.0")
    def test_functions(self):
        self.assertResultIsCFRetained(Quartz.CGPDFStructureElementCreate)
        Quartz.CGPDFStructureElementRetain
        Quartz.CGPDFStructureElementRelease
        Quartz.CGPDFStructureElementSetTitle
        Quartz.CGPDFStructureElementSetLanguageIdentifier
        Quartz.CGPDFStructureElementSetAlternativeText
        Quartz.CGPDFStructureElementSetExpansionText
        Quartz.CGPDFStructureElementSetActualText
        Quartz.CGPDFStructureElementAddStructureElement
        Quartz.CGPDFStructureElementAddMarkedContentItem
