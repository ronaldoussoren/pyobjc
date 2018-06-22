from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2 ** 32:
    import NaturalLanguage

    class TestNLTokenizer (TestCase):
        def test_constants(self):
            self.assertEqual(NaturalLanguage.NLTokenUnitWord, 0)
            self.assertEqual(NaturalLanguage.NLTokenUnitSentence, 1)
            self.assertEqual(NaturalLanguage.NLTokenUnitParagraph, 2)
            self.assertEqual(NaturalLanguage.NLTokenUnitDocument, 3)

            self.assertEqual(NaturalLanguage.NLTokenizerAttributeNumeric, 1 << 0)
            self.assertEqual(NaturalLanguage.NLTokenizerAttributeSymbolic, 1 << 1)
            self.assertEqual(NaturalLanguage.NLTokenizerAttributeEmoji, 1 << 2)

        def test_methods(self):
            self.assertArgIsBlock(NaturalLanguage.NLTokenizer.enumerateTokensInRange_usingBlock_, 1,
                    objc._C_VOID + NaturalLanguage.NSRange.__typestr__ +  objc._C_NSUInteger + objc._C_OUT + objc._C_PTR + objc._C_NSBOOL)

if __name__ == "__main__":
    main()
