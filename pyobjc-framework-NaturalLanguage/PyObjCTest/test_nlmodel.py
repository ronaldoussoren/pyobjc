from PyObjCTools.TestSupport import TestCase
import NaturalLanguage


class TestNLModel(TestCase):
    def test_enums(self):
        self.assertIsEnumType(NaturalLanguage.NLModelType)
        self.assertEqual(NaturalLanguage.NLModelTypeClassifier, 0)
        self.assertEqual(NaturalLanguage.NLModelTypeSequence, 1)

    def test_methods(self):
        self.assertArgIsOut(NaturalLanguage.NLModel.modelWithContentsOfURL_error_, 1)
        self.assertArgIsOut(NaturalLanguage.NLModel.modelWithMLModel_error_, 1)
