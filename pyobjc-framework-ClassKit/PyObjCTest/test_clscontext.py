from PyObjCTools.TestSupport import TestCase, min_os_level

import ClassKit


class TestCLSContext(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(ClassKit.CLSContextTopic, str)

    def test_enum_types(self):
        self.assertIsEnumType(ClassKit.CLSContextType)

    def test_constants(self):
        self.assertEqual(ClassKit.CLSContextTypeNone, 0)
        self.assertEqual(ClassKit.CLSContextTypeApp, 1)
        self.assertEqual(ClassKit.CLSContextTypeChapter, 2)
        self.assertEqual(ClassKit.CLSContextTypeSection, 3)
        self.assertEqual(ClassKit.CLSContextTypeLevel, 4)
        self.assertEqual(ClassKit.CLSContextTypePage, 5)
        self.assertEqual(ClassKit.CLSContextTypeTask, 6)
        self.assertEqual(ClassKit.CLSContextTypeChallenge, 7)
        self.assertEqual(ClassKit.CLSContextTypeQuiz, 8)
        self.assertEqual(ClassKit.CLSContextTypeExercise, 9)
        self.assertEqual(ClassKit.CLSContextTypeLesson, 10)
        self.assertEqual(ClassKit.CLSContextTypeBook, 11)
        self.assertEqual(ClassKit.CLSContextTypeGame, 12)
        self.assertEqual(ClassKit.CLSContextTypeDocument, 13)
        self.assertEqual(ClassKit.CLSContextTypeAudio, 14)
        self.assertEqual(ClassKit.CLSContextTypeVideo, 15)
        self.assertEqual(ClassKit.CLSContextTypeCourse, 16)
        self.assertEqual(ClassKit.CLSContextTypeCustom, 17)

    @min_os_level("11.0")
    def test_constants11_0(self):
        self.assertIsInstance(ClassKit.CLSContextTopicMath, str)
        self.assertIsInstance(ClassKit.CLSContextTopicScience, str)
        self.assertIsInstance(ClassKit.CLSContextTopicLiteracyAndWriting, str)
        self.assertIsInstance(ClassKit.CLSContextTopicWorldLanguage, str)
        self.assertIsInstance(ClassKit.CLSContextTopicSocialScience, str)
        self.assertIsInstance(
            ClassKit.CLSContextTopicComputerScienceAndEngineering, str
        )
        self.assertIsInstance(ClassKit.CLSContextTopicArtsAndMusic, str)
        self.assertIsInstance(ClassKit.CLSContextTopicHealthAndFitness, str)

    def test_methods(self):
        self.assertResultIsBOOL(ClassKit.CLSContext.isAssignable)
        self.assertArgIsBOOL(ClassKit.CLSContext.setAssignable_, 0)
        self.assertResultIsBOOL(ClassKit.CLSContext.isActive)

        self.assertArgIsBlock(
            ClassKit.CLSContext.descendantMatchingIdentifierPath_completion_, 1, b"v@@"
        )
