import unittest

from objc import *
from Foundation import *

class TestSearchPaths( unittest.TestCase ):
    def testSearchPaths( self ):
        self.assert_( NSSearchPathForDirectoriesInDomains( NSAllLibrariesDirectory, NSAllDomainsMask, NO ),
                      "NSSearchPathForDirectoriesInDomains() failed to return anything." )
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest( unittest.makeSuite( TestSearchPaths ) )
    return suite

if __name__ == '__main__':
    unittest.main( )

