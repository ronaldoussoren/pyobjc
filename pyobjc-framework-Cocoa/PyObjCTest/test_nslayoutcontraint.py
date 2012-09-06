from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSLayoutContraintManual (TestCase):
    def testNSDictionaryOfVariableBindings(self):
        var1 = 'foo'
        var2 = 'bar'

        self.assertEqual(NSDictionaryOfVariableBindings('var1', 'var2'),
                {'var1': 'foo', 'var2': 'bar'})

        self.assertRaises(KeyError, NSDictionaryOfVariableBindings, 'var1', 'var3')
if __name__ == "__main__":
    main()
