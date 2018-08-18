from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2 ** 32:
    import NaturalLanguage

    class TestNLLanguageRecognizer (TestCase):
        def test_classes(self):
            NaturalLanguage.NLLanguageRecognizer

if __name__ == "__main__":
    main()
