from PyObjCTools.TestSupport import TestCase
import Quartz


class TestPDFActionResetForm(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(Quartz.PDFActionResetForm.fieldsIncludedAreCleared)
        self.assertArgIsBOOL(Quartz.PDFActionResetForm.setFieldsIncludedAreCleared_, 0)
