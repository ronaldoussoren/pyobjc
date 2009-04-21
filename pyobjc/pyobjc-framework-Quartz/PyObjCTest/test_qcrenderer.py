
from PyObjCTools.TestSupport import *
from Quartz.QuartzComposer import *

class TestQCRendererHelper (NSObject):
    def setValue_forInputKey_(self, v, k): return 1

class TestQCRenderer (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(QCRendererEventKey, unicode)
        self.failUnlessIsInstance(QCRendererMouseLocationKey, unicode)

    def testMethods(self):
        self.failUnlessResultIsBOOL(TestQCRendererHelper.setValue_forInputKey_)

        self.failUnlessResultIsBOOL(QCRenderer.renderAtTime_arguments_)


if __name__ == "__main__":
    main()
