import unittest

from objc import *
from Foundation import *

class TestSearchPaths(unittest.TestCase):
    def testSearchPaths(self):
        self.assert_( NSSearchPathForDirectoriesInDomains( NSAllLibrariesDirectory, NSAllDomainsMask, NO ),
                      "NSSearchPathForDirectoriesInDomains() failed to return anything." )

    def testTrue(self):
        for boolVal in (1, 1==1, YES, -1):
            self.assert_(NSSearchPathForDirectoriesInDomains(NSLibraryDirectory,NSUserDomainMask, boolVal)[0][0] == '/', boolVal)

    def testFalse(self):
        for boolVal in (0, 1!=1, NO):
            self.assert_(NSSearchPathForDirectoriesInDomains(NSLibraryDirectory,NSUserDomainMask, boolVal)[0][0] != '/', boolVal)


if __name__ == '__main__':
    unittest.main( )
