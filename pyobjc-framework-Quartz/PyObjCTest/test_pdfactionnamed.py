from PyObjCTools.TestSupport import TestCase
import Quartz


class TestPDFActionNamed(TestCase):
    def testConstants(self):
        self.assertEqual(Quartz.kPDFActionNamedNone, 0)
        self.assertEqual(Quartz.kPDFActionNamedNextPage, 1)
        self.assertEqual(Quartz.kPDFActionNamedPreviousPage, 2)
        self.assertEqual(Quartz.kPDFActionNamedFirstPage, 3)
        self.assertEqual(Quartz.kPDFActionNamedLastPage, 4)
        self.assertEqual(Quartz.kPDFActionNamedGoBack, 5)
        self.assertEqual(Quartz.kPDFActionNamedGoForward, 6)
        self.assertEqual(Quartz.kPDFActionNamedGoToPage, 7)
        self.assertEqual(Quartz.kPDFActionNamedFind, 8)
        self.assertEqual(Quartz.kPDFActionNamedPrint, 9)
        self.assertEqual(Quartz.kPDFActionNamedZoomIn, 10)
        self.assertEqual(Quartz.kPDFActionNamedZoomOut, 11)
