import unittest
import objc

from Foundation import *

class TestNSDictionaryInteraction( unittest.TestCase ):
    def testRepeatedAllocInit( self ):
        for i in range(1,1000):
            d = NSDictionary.alloc().init()

    def testBasicInteraction( self ):
        d = NSMutableDictionary.dictionary()
        d['a'] = "foo"
        d['b'] = "bar"

        self.assertEqual(d['a'], "foo", "Failed to retrieve the same thing that was put into the dict.")
        try:
            d['c']
            self.fail("Should have raised...")
        except KeyError:
            pass

    def testIn( self ):
        d = NSMutableDictionary.dictionary()
        d['a'] = "foo"
        d['b'] = "bar"
        d[1] = "baz"
        d[0] = "bob"
        # d[-1] = None -- this fails because the bridge doesn't proxy py(None) to objc(NSNull)... not sure if it should

        self.assert_( 'a' in d )
        self.assert_( 1 in d )
        # self.assert_( -1 in d )
        # self.assert_( d[-1] is None )
        self.assert_( 'q' not in d )

        for k in d.allKeys():
            self.assertEqual( d.objectForKey_( k ), d[k] )

        for k in d:
            self.assertEqual( d.objectForKey_( k ), d[k] )
            
        del d['a']
        self.assert_( 'a' not in d )
        

def suite():
    suite = unittest.TestSuite()
    suite.addTest( unittest.makeSuite( TestNSDictionaryInteraction ) )
    return suite

if __name__ == '__main__':
    unittest.main( )
