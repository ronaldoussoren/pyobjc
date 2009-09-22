from Quartz import *
from PyObjCTools.TestSupport import *


class TestCAValueFunction (TestCase):
    @min_os_level('10.6')
    def testConstants10_6(self):
        self.failUnlessIsInstance(kCAValueFunctionRotateX, unicode)
        self.failUnlessIsInstance(kCAValueFunctionRotateY, unicode)
        self.failUnlessIsInstance(kCAValueFunctionRotateZ, unicode)
        self.failUnlessIsInstance(kCAValueFunctionScale, unicode)
        self.failUnlessIsInstance(kCAValueFunctionScaleX, unicode)
        self.failUnlessIsInstance(kCAValueFunctionScaleY, unicode)
        self.failUnlessIsInstance(kCAValueFunctionScaleZ, unicode)
        self.failUnlessIsInstance(kCAValueFunctionTranslate, unicode)
        self.failUnlessIsInstance(kCAValueFunctionTranslateX, unicode)
        self.failUnlessIsInstance(kCAValueFunctionTranslateY, unicode)
        self.failUnlessIsInstance(kCAValueFunctionTranslateZ, unicode)

if __name__ == "__main__":
    main()
