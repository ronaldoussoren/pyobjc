"""
This adds some usefull conveniences to NSManagedObject and subclasses thereof
"""
__all__ = ()
from objc import addConvenienceForClass
from Foundation import NSObject

def NSMOsetValue_ForKey_(self, name, value):
    try:
        if '__objc_python_subclass__' in self.__class__.__dict__:
            super(self.__class__, self).setValue_forKey_(value, name)
        else:
            self.setValue_forKey_(value, name)

    except KeyError, msg:
        NSObject.__setattr__(self, name, value)

def NSMOgetValueForKey_(self, name):
    try:
        if '__objc_python_subclass__' in self.__class__.__dict__:
            return super(self.__class__, self).valueForKey_(name)
        else:
            return self.valueForKey_(name)
        
    except KeyError, msg:
        raise AttributeError(name)

addConvenienceForClass('NSManagedObject', (
    ('__setattr__', NSMOsetValue_ForKey_),
    ('__getattr__', NSMOgetValueForKey_),
))
