
from PyObjCTools.TestSupport import *
from Quartz.QuartzComposer import *

try:
    unicode
except NameError:
    unicode = str

class TestQCPlugIn (TestCase):
    @min_os_level('10.5')
    def testConstants10_5(self):
        self.assertIsInstance(QCPlugInAttributeNameKey, unicode)
        self.assertIsInstance(QCPlugInAttributeDescriptionKey, unicode)
        self.assertIsInstance(QCPlugInAttributeCopyrightKey, unicode)

        self.assertIsInstance(QCPortAttributeDefaultValueKey, unicode)
        self.assertIsInstance(QCPortAttributeMenuItemsKey, unicode)
        self.assertIsInstance(QCPlugInPixelFormatARGB8, unicode)
        self.assertIsInstance(QCPlugInPixelFormatBGRA8, unicode)
        self.assertIsInstance(QCPlugInPixelFormatRGBAf, unicode)
        self.assertIsInstance(QCPlugInPixelFormatI8, unicode)
        self.assertIsInstance(QCPlugInPixelFormatIf, unicode)
        self.assertIsInstance(QCPlugInExecutionArgumentEventKey, unicode)
        self.assertIsInstance(QCPlugInExecutionArgumentMouseLocationKey, unicode)

        self.assertEqual(kQCPlugInExecutionModeProvider, 1)
        self.assertEqual(kQCPlugInExecutionModeProcessor, 2)
        self.assertEqual(kQCPlugInExecutionModeConsumer, 3)

        self.assertEqual(kQCPlugInTimeModeNone, 0)
        self.assertEqual(kQCPlugInTimeModeIdle, 1)
        self.assertEqual(kQCPlugInTimeModeTimeBase, 2)

    @min_os_level('10.7')
    def testConstants10_7(self):
        self.assertIsInstance(QCPlugInAttributeCategoriesKey, unicode)
        self.assertIsInstance(QCPlugInAttributeExamplesKey, unicode)


    def testConstants(self):
        self.assertIsInstance(QCPortAttributeTypeKey, unicode)
        self.assertIsInstance(QCPortAttributeNameKey, unicode)
        self.assertIsInstance(QCPortAttributeMinimumValueKey, unicode)
        self.assertIsInstance(QCPortAttributeMaximumValueKey, unicode)
        self.assertIsInstance(QCPortTypeBoolean, unicode)
        self.assertIsInstance(QCPortTypeIndex, unicode)
        self.assertIsInstance(QCPortTypeNumber, unicode)
        self.assertIsInstance(QCPortTypeString, unicode)
        self.assertIsInstance(QCPortTypeColor, unicode)
        self.assertIsInstance(QCPortTypeImage, unicode)
        self.assertIsInstance(QCPortTypeStructure, unicode)


    @min_os_level('10.5')
    def testMethods(self):
        self.assertResultIsBOOL(QCPlugIn.startExecution_)
        self.assertResultIsBOOL(QCPlugIn.execute_atTime_withArguments_)
        self.assertResultIsBOOL(QCPlugIn.didValueForInputKeyChange_)
        self.assertResultIsBOOL(QCPlugIn.setValue_forOutputKey_)
        self.assertResultIsBOOL(QCPlugIn.loadPlugInAtPath_)

    @expectedFailure
    def testProtocols(self):
        self.fail("Test interface for QCPlugInContext")

if __name__ == "__main__":
    main()
