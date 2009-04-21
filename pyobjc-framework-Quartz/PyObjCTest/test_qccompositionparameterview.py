from PyObjCTools.TestSupport import *
from Quartz.QuartzComposer import *

class TestQCCompositionParameterViewHelper (NSObject):
    def compositionParameterView_shouldDisplayParameterWithKey_attributes_(self, pv, pk, pa): return 1

class TestQCCompositionParameterView (TestCase):
    @min_os_level('10.5')
    def testMethods(self):
        self.failUnlessResultIsBOOL(QCCompositionParameterView.hasParameters)

        self.failUnlessResultIsBOOL(QCCompositionParameterView.drawsBackground)
        self.failUnlessArgIsBOOL(QCCompositionParameterView.setDrawsBackground_, 0)

        self.failUnlessResultIsBOOL(TestQCCompositionParameterViewHelper.compositionParameterView_shouldDisplayParameterWithKey_attributes_)


if __name__ == "__main__":
    main()
