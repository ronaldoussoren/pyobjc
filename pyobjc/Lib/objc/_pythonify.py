import _objc

__all__ = []

class OC_PythonFloat(float):
    def __new__(cls, obj, value):
        self = float.__new__(cls, value)
        self.__pyobjc_object__ = obj
        return self

    def __getattr__(self, attr):
        return getattr(self.__pyobjc_object__, attr)

class OC_PythonLong(long):
    def __new__(cls, obj, value):
        self = long.__new__(cls, value)
        self.__pyobjc_object__ = obj
        return self

    def __getattr__(self, attr):
        return getattr(self.__pyobjc_object__, attr)

class OC_PythonInt(int):
    def __new__(cls, obj, value):
        self = int.__new__(cls, value)
        self.__pyobjc_object__ = obj
        return self

    def __getattr__(self, attr):
        return getattr(self.__pyobjc_object__, attr)

NSNumber = _objc.lookUpClass('NSNumber')
NSDecimalNumber = _objc.lookUpClass('NSDecimalNumber')
def numberWrapper(obj):
    if isinstance(obj, NSDecimalNumber) or not hasattr(obj, 'objCType'):
        return obj
    tp = obj.objCType()
    if tp in 'qQLfd':
        if tp == 'q':
            return OC_PythonLong(obj, obj.longLongValue())
        elif tp in 'QL':
            return OC_PythonLong(obj, obj.unsignedLongLongValue())
        else:
            return OC_PythonFloat(obj, obj.doubleValue())
    else:
        return OC_PythonInt(obj, obj.longValue())

_objc.setNSNumberWrapper(numberWrapper)
