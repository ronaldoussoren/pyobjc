import _objc

__all__ = []


class OC_PythonFloat(float):
    __slots__=('__pyobjc_object__',)


    def __new__(cls, obj, value):
        self = float.__new__(cls, value)
        self.__pyobjc_object__ = obj
        return self

    __class__ = property(lambda self: self.__pyobjc_object__.__class__)

    def __getattr__(self, attr):
        return getattr(self.__pyobjc_object__, attr)

    def __reduce__(self):
        return (float, (float(self),))

class OC_PythonLong(long):

    def __new__(cls, obj, value):
        self = long.__new__(cls, value)
        self.__pyobjc_object__ = obj
        return self

    __class__ = property(lambda self: self.__pyobjc_object__.__class__)

    def __getattr__(self, attr):
        return getattr(self.__pyobjc_object__, attr)

    # The long type doesn't support __slots__ on subclasses, fake
    # one part of the effect of __slots__: don't allow setting of attributes.
    def __setattr__(self, attr, value):
        if attr != '__pyobjc_object__':
            raise AttributeError, "'%s' object has no attribute '%s')"%(self.__class__.__name__, attr)
        self.__dict__['__pyobjc_object__'] = value

    def __reduce__(self):
        return (long, (long(self),))

class OC_PythonInt(int):
    __slots__=('__pyobjc_object__',)

    def __new__(cls, obj, value):
        self = int.__new__(cls, value)
        self.__pyobjc_object__ = obj
        return self

    __class__ = property(lambda self: self.__pyobjc_object__.__class__)

    def __getattr__(self, attr):
        return getattr(self.__pyobjc_object__, attr)

    def __reduce__(self):
        return (int, (int(self),))

NSNumber = _objc.lookUpClass('NSNumber')
NSDecimalNumber = _objc.lookUpClass('NSDecimalNumber')
Foundation = None

def numberWrapper(obj):
    if isinstance(obj, NSDecimalNumber):
        return obj
        # ensure that NSDecimal is around
        global Foundation
        if Foundation is None:
            import Foundation
        # return NSDecimal
        return Foundation.NSDecimal(obj)
    try:
        tp = obj.objCType()
    except AttributeError:
        import warnings
        warnings.warn(RuntimeWarning, "NSNumber instance doesn't implement objCType? %r" % (obj,))
        return obj
    if tp in 'qQLfd':
        if tp == 'q':
            return OC_PythonLong(obj, obj.longLongValue())
        elif tp in 'QL':
            return OC_PythonLong(obj, obj.unsignedLongLongValue())
        else:
            return OC_PythonFloat(obj, obj.doubleValue())
    else:
        return OC_PythonInt(obj, obj.longValue())

_objc._setNSNumberWrapper(numberWrapper)
