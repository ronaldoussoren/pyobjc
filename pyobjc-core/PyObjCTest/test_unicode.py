from PyObjCTools.TestSupport import *
import objc

class TestUnicodeProxy (TestCase):

    def test_regr1(self):
        o = objc.lookUpClass('NSString').stringWithString_("hello")
        self.assertIsInstance(o.stringByAppendingFormat_, objc.selector)
        self.assertIsInstance(o.nsstring().stringByAppendingFormat_, objc.selector)

        # XXX: Can only test this one when Foundation wrappers are loaded:
        #self.assertEqual(o.stringByAppendingFormat_('foo %d', 42), 'hellofoo 42')

    def test_regr2(self):
        o = objc.lookUpClass('NSString').stringWithString_("hello")
        self.assertIsInstance(o.stringByAppendingString_, objc.selector)
        self.assertIsInstance(o.nsstring().stringByAppendingString_, objc.selector)

        self.assertEqual(o.stringByAppendingString_('foo %d'), 'hellofoo %d')

if __name__ == "__main__":
    main()
