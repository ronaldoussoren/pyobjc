from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestQCPlugIn(TestCase):
    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertIsInstance(Quartz.QCPlugInAttributeNameKey, str)
        self.assertIsInstance(Quartz.QCPlugInAttributeDescriptionKey, str)
        self.assertIsInstance(Quartz.QCPlugInAttributeCopyrightKey, str)

        self.assertIsInstance(Quartz.QCPortAttributeDefaultValueKey, str)
        self.assertIsInstance(Quartz.QCPortAttributeMenuItemsKey, str)
        self.assertIsInstance(Quartz.QCPlugInPixelFormatARGB8, str)
        self.assertIsInstance(Quartz.QCPlugInPixelFormatBGRA8, str)
        self.assertIsInstance(Quartz.QCPlugInPixelFormatRGBAf, str)
        self.assertIsInstance(Quartz.QCPlugInPixelFormatI8, str)
        self.assertIsInstance(Quartz.QCPlugInPixelFormatIf, str)
        self.assertIsInstance(Quartz.QCPlugInExecutionArgumentEventKey, str)
        self.assertIsInstance(Quartz.QCPlugInExecutionArgumentMouseLocationKey, str)

        self.assertEqual(Quartz.kQCPlugInExecutionModeProvider, 1)
        self.assertEqual(Quartz.kQCPlugInExecutionModeProcessor, 2)
        self.assertEqual(Quartz.kQCPlugInExecutionModeConsumer, 3)

        self.assertEqual(Quartz.kQCPlugInTimeModeNone, 0)
        self.assertEqual(Quartz.kQCPlugInTimeModeIdle, 1)
        self.assertEqual(Quartz.kQCPlugInTimeModeTimeBase, 2)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertIsInstance(Quartz.QCPlugInAttributeCategoriesKey, str)
        self.assertIsInstance(Quartz.QCPlugInAttributeExamplesKey, str)

    def testConstants(self):
        self.assertIsInstance(Quartz.QCPortAttributeTypeKey, str)
        self.assertIsInstance(Quartz.QCPortAttributeNameKey, str)
        self.assertIsInstance(Quartz.QCPortAttributeMinimumValueKey, str)
        self.assertIsInstance(Quartz.QCPortAttributeMaximumValueKey, str)
        self.assertIsInstance(Quartz.QCPortTypeBoolean, str)
        self.assertIsInstance(Quartz.QCPortTypeIndex, str)
        self.assertIsInstance(Quartz.QCPortTypeNumber, str)
        self.assertIsInstance(Quartz.QCPortTypeString, str)
        self.assertIsInstance(Quartz.QCPortTypeColor, str)
        self.assertIsInstance(Quartz.QCPortTypeImage, str)
        self.assertIsInstance(Quartz.QCPortTypeStructure, str)

    @min_os_level("10.5")
    def testMethods(self):
        self.assertResultIsBOOL(Quartz.QCPlugIn.startExecution_)
        self.assertResultIsBOOL(Quartz.QCPlugIn.execute_atTime_withArguments_)
        self.assertResultIsBOOL(Quartz.QCPlugIn.didValueForInputKeyChange_)
        self.assertResultIsBOOL(Quartz.QCPlugIn.setValue_forOutputKey_)
        self.assertResultIsBOOL(Quartz.QCPlugIn.loadPlugInAtPath_)

    def testProtocols(self):
        self.assertProtocolExists("QCPlugInContext")
        self.assertProtocolExists("QCPlugInInputImageSource")
        self.assertProtocolExists("QCPlugInOutputImageProvider")
