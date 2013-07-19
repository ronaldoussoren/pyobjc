"""
Support for NSDecimalNumber.

The actual class is defined in Foundation, but having the wrapper
here is much more convenient.
"""
from objc._convenience import addConvenienceForClass
from objc._objc import lookUpClass

addConvenienceForClass('NSDecimalNumber', (
    ('__add__',         lambda self, other: _makeD(self.decimalValue() + other)),
    ('__radd__',        lambda self, other: _makeD(other + self.decimalValue())),
    ('__sub__',         lambda self, other: _makeD(self.decimalValue() - other)),
    ('__rsub__',        lambda self, other: _makeD(other - self.decimalValue())),
    ('__mul__',         lambda self, other: _makeD(self.decimalValue() * other)),
    ('__rmul__',        lambda self, other: _makeD(other * self.decimalValue())),
    ('__div__',         lambda self, other: _makeD(self.decimalValue() / other)),
    ('__rdiv__',        lambda self, other: _makeD(other / self.decimalValue())),
    ('__truediv__',     lambda self, other: _makeD(self.decimalValue() / other)),
    ('__rtruediv__',    lambda self, other: _makeD(other / self.decimalValue())),
    ('__floordiv__',    lambda self, other: _makeD(self.decimalValue() // other)),
    ('__rfloordiv__',   lambda self, other: _makeD(other // self.decimalValue())),
    ('__mod__',         lambda self, other: _makeD(self.decimalValue() % other)),
    ('__rmod__',        lambda self, other: _makeD(other % self.decimalValue())),
    ('__neg__',         lambda self: _makeD(-(self.decimalValue()))),
    ('__pos__',         lambda self: _makeD(+(self.decimalValue()))),
    ('__abs__',         lambda self: _makeD(abs(self.decimalValue()))),
    ('__round__',       lambda self, n=0 : _makeD(round(self.decimalValue(), n))),
))

NSDecimalNumber = lookUpClass('NSDecimalNumber')
def _makeD(v):
    if isinstance(v, NSDecimalNumber):
        return v

    return NSDecimalNumber.decimalNumberWithDecimal_(v)
