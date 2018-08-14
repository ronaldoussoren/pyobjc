from PyObjCTools.TestSupport import *
import decimal
import Cocoa
from PyObjCTools import Conversion

class TestConversion (TestCase):
    def test_toPythonDecimal(self):
        v = Cocoa.NSDecimalNumber.decimalNumberWithString_(u"42.5")
        d = Conversion.toPythonDecimal(v)
        self.assertIsInstance(d, decimal.Decimal)
        self.assertEqual(str(d), "42.5")

    def test_fromPythonDecimal(self):
        d = decimal.Decimal("42.5")
        self.assertIsInstance(d, decimal.Decimal)

        v = Conversion.fromPythonDecimal(d)
        self.assertIsInstance(v, Cocoa.NSDecimalNumber)
        self.assertEqual(str(v), "42.5")

    def test_serializePropertyList(self):
        self.assertRaises(ValueError, Conversion.serializePropertyList, {}, 'invalid')

        v = Conversion.serializePropertyList({'a': 42}, 'xml')
        self.assertTrue(bytes(v).startswith(b'<?xml'))

        v = Conversion.serializePropertyList({'a': 42}, 'binary')
        self.assertTrue(bytes(v).startswith(b'bplist'))

        self.assertRaises(ValueError, Conversion.serializePropertyList, {'a': 42}, 'ascii')

        self.assertRaises(ValueError, Conversion.serializePropertyList, Cocoa.NSObject.alloc().init(), 'xml')

    def test_deserializePropertyList(self):
        in_val =  {'a': 42}

        for fmt in ('xml', 'binary'):
             data = Conversion.serializePropertyList(in_val, fmt)

             out_val = Conversion.deserializePropertyList(data)

             self.assertEqual(in_val, out_val)


             self.assertRaises(ValueError, Conversion.deserializePropertyList, data[:-2])

if __name__ == "__main__":
    main()
