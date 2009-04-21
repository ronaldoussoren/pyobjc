
from PyObjCTools.TestSupport import *
from Quartz.QuartzComposer import *


class TestQCPlugIn (TestCase):
    @min_os_level('10.5')
    def testConstants10_5(self):
        self.failUnlessIsInstance(QCPlugInAttributeNameKey, unicode)
        self.failUnlessIsInstance(QCPlugInAttributeDescriptionKey, unicode)
        self.failUnlessIsInstance(QCPlugInAttributeCopyrightKey, unicode)

        self.failUnlessIsInstance(QCPortAttributeDefaultValueKey, unicode)
        self.failUnlessIsInstance(QCPortAttributeMenuItemsKey, unicode)
        self.failUnlessIsInstance(QCPlugInPixelFormatARGB8, unicode)
        self.failUnlessIsInstance(QCPlugInPixelFormatBGRA8, unicode)
        self.failUnlessIsInstance(QCPlugInPixelFormatRGBAf, unicode)
        self.failUnlessIsInstance(QCPlugInPixelFormatI8, unicode)
        self.failUnlessIsInstance(QCPlugInPixelFormatIf, unicode)
        self.failUnlessIsInstance(QCPlugInExecutionArgumentEventKey, unicode)
        self.failUnlessIsInstance(QCPlugInExecutionArgumentMouseLocationKey, unicode)

        self.failUnlessEqual(kQCPlugInExecutionModeProvider, 1)
        self.failUnlessEqual(kQCPlugInExecutionModeProcessor, 2)
        self.failUnlessEqual(kQCPlugInExecutionModeConsumer, 3)

        self.failUnlessEqual(kQCPlugInTimeModeNone, 0)
        self.failUnlessEqual(kQCPlugInTimeModeIdle, 1)
        self.failUnlessEqual(kQCPlugInTimeModeTimeBase, 2)



    def testConstants(self):
        self.failUnlessIsInstance(QCPortAttributeTypeKey, unicode)
        self.failUnlessIsInstance(QCPortAttributeNameKey, unicode)
        self.failUnlessIsInstance(QCPortAttributeMinimumValueKey, unicode)
        self.failUnlessIsInstance(QCPortAttributeMaximumValueKey, unicode)
        self.failUnlessIsInstance(QCPortTypeBoolean, unicode)
        self.failUnlessIsInstance(QCPortTypeIndex, unicode)
        self.failUnlessIsInstance(QCPortTypeNumber, unicode)
        self.failUnlessIsInstance(QCPortTypeString, unicode)
        self.failUnlessIsInstance(QCPortTypeColor, unicode)
        self.failUnlessIsInstance(QCPortTypeImage, unicode)
        self.failUnlessIsInstance(QCPortTypeStructure, unicode)


    def testMethods(self):
        self.failUnlessResultIsBOOL(QCPlugIn.startExecution_)
        self.failUnlessResultIsBOOL(QCPlugIn.execute_atTime_withArguments_)
        self.failUnlessResultIsBOOL(QCPlugIn.didValueForInputKeyChange_)
        self.failUnlessResultIsBOOL(QCPlugIn.setValue_forOutputKey_)
        self.failUnlessResultIsBOOL(QCPlugIn.loadPlugInAtPath_)

    def testProtocols(self):
        self.fail("Test interface for QCPlugInContext")

if __name__ == "__main__":
    main()

