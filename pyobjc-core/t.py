import objc


class OC_Compared(objc.lookUpClass("NSObject")):
    def initWithValue_(self, value):
        self = super(OC_Compared, self).init()
        if self is None:
            return None

        self._value = value
        return self

    @objc.typedSelector(objc._C_NSBOOL + b"@:@")
    def isEqualTo_(self, other):
        return self.compare_(other) == 0

    @objc.typedSelector(objc._C_NSBOOL + b"@:@")
    def isNotEqualTo_(self, other):
        return self.compare_(other) != 0

    @objc.typedSelector(objc._C_NSInteger + b"@:@")
    def compare_(self, other):
        if isinstance(other, OC_Compared):
            other = other._value

        if self._value < other:
            return -1

        elif self._value > other:
            return 1

        else:
            return 0
