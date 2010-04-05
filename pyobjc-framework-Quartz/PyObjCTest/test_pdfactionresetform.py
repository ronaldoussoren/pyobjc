
from PyObjCTools.TestSupport import *
from Quartz.PDFKit import *

class TestPDFActionResetForm (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(PDFActionResetForm.fieldsIncludedAreCleared)
        self.assertArgIsBOOL(PDFActionResetForm.setFieldsIncludedAreCleared_, 0)

if __name__ == "__main__":
    main()
