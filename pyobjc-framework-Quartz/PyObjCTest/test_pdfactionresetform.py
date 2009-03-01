
from PyObjCTools.TestSupport import *
from Quartz.PDFKit import *

class TestPDFActionResetForm (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(PDFActionResetForm.fieldsIncludedAreCleared)
        self.failUnlessArgIsBOOL(PDFActionResetForm.setFieldsIncludedAreCleared_, 0)

if __name__ == "__main__":
    main()
