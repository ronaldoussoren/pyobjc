from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2 ** 32:
    import NaturalLanguage

    class TestNLModel (TestCase):
        def test_constants(self):
            self.assertEqual(NaturalLanguage.NLModelTypeClassifier, 0)
            self.assertEqual(NaturalLanguage.NLModelTypeSequence, 1)

if __name__ == "__main__":
    main()
