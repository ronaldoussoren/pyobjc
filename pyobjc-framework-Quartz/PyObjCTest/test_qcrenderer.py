
from PyObjCTools.TestSupport import *
from Quartz.QuartzComposer import *

try:
    unicode
except NameError:
    unicode = str

class TestQCRendererHelper (NSObject):
    def setValue_forInputKey_(self, v, k): return 1

class TestQCRenderer (TestCase):
    def testConstants(self):
        self.assertIsInstance(QCRendererEventKey, unicode)
        self.assertIsInstance(QCRendererMouseLocationKey, unicode)

    def testMethods(self):
        self.assertResultIsBOOL(TestQCRendererHelper.setValue_forInputKey_)

        self.assertResultIsBOOL(QCRenderer.renderAtTime_arguments_)


if __name__ == "__main__":
    main()
