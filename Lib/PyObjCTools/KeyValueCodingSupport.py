from types import FunctionType
import objc
from Foundation import *

### BUG:  If accessing iVar directly and iVar is a callable type, it'll be invoked
# I don't think there is anything we can do about this because of the way python works
class BridgedKeyValueMethods(NSObject):
    def bridgedValueForKey_(self, aKey):
        try:
            v = getValueForKey_(self, aKey)
            return v
        except KeyError:
            zuper = super(self.__class__, self)
            if zuper.respondsToSelector_("valueForKey:"):
                return zuper.valueForKey_(aKey)

        raise KeyError, aKey
    bridgedValueForKey_ = objc.selector(bridgedValueForKey_,  argumentTypes="s", returnType="O")

def addKeyValueBridgeToClass(aClass):
    objc.classAddMethod(aClass, "valueForKey:", BridgedKeyValueMethods.bridgedValueForKey_)

def getValueForKey_(anObject, aKey):
    upperizedKey = aKey[0].upper() + aKey[1:]

    # Accessor methods
    possibleMethod = getattr(anObject, "get" + upperizedKey, None)
    if possibleMethod and type(possibleMethod) is FunctionType:
        return possibleMethod(anObject)
    aKeyPossibleMethod = getattr(anObject, aKey, None)
    if aKeyPossibleMethod and type(aKeyPossibleMethod) is FunctionType:
        return aKeyPossibleMethod(anObject)
    possibleIsMethod = getattr(anObject, "is" + upperizedKey, None)
    if possibleIsMethod and type(possibleIsMethod) is FunctionType:
        return possibleIsMethod(anObject)

    # direct access to ivar
    if anObject.accessInstanceVariablesDirectly():
        possibleValue = getattr(anObject, "_" + aKey, None)
        if possibleValue is not None: return possibleValue
        possibleValue = getattr(anObject, "_is" + upperizedKey, None)
        if possibleValue is not None: return possibleValue
        possibleValue = getattr(anObject, aKey, None)
        if possibleValue is not None: return possibleValue
        possibleValue = getattr(anObject, "is" + upperizedKey, None)
        if possibleValue is not None: return possibleValue

    raise KeyError, aKey

class KeyValueCoding:
    """A class that can be mixed into any python class to make it KV compatible on the ObjC side of the bridge."""
    def accessInstanceVariablesDirectly(self): return 1

    def valueForUndefinedKey_(self, aKey):
        raise KeyError, aKey
    
    def valueForKey_(self, aKey):
        try:
            return getValueForKey_(self, aKey)
        except KeyError:
            return valueForUndefinedKey_(self, aKey)
    
    def valueForKeyPath_(self, aPath):
        object = self
        for pathElement in aPath.split('.'):
            object = object.valueForKey_(pathElement)
        return object
