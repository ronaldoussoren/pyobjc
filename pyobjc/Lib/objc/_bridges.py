from _objc import *
import warnings

__all__ = ['PyObjCStrBridgeWarning']

class PyObjCStrBridgeWarning(DeprecationWarning):
    pass

BRIDGED_STRUCTURES = {}
BRIDGED_TYPES = []

def str_to_unicode(s):
    if not getStrBridgeEnabled():
        warnings.warn("use unicode(str, encoding) for NSString", PyObjCStrBridgeWarning, stacklevel=2)
    return unicode(s)

BRIDGED_TYPES.append((str, str_to_unicode))

try:
    from array import array
    from Carbon.File import FSRef
except ImportError:
    pass
else:
    def struct_to_FSRef(s):
        return FSRef(rawdata=array('B', s[0]).tostring())
    BRIDGED_STRUCTURES['{FSRef=[80C]}'] = struct_to_FSRef

    def FSRef_to_struct(fsRef):
        return (tuple(array('B').fromstring(fsRef.data)),)
    BRIDGED_TYPES.append((FSRef, FSRef_to_struct))

#try:
#    import decimal
#except ImportError:
#    pass
#else:
#    NSDecimalNumber = lookUpClass('NSDecimalNumber')
#    def Decimal_to_NSDecimalNumber(d):
#        # XXX - this doesn't take into account the locale setting
#        #       however I don't know what the heck NSDecimalNumber
#        #       expects..
#        return NSDecimalNumber.decimalNumberWithString_(unicode(d))
#    BRIDGED_TYPES.append((decimal.Decimal, Decimal_to_NSDecimalNumber))

def _bridgePythonTypes():
    # python TO Obj-C
    OC_PythonObject = lookUpClass('OC_PythonObject')
    if BRIDGED_TYPES:
        OC_PythonObject.depythonifyTable().extend(BRIDGED_TYPES)
    if BRIDGED_STRUCTURES:
        OC_PythonObject.pythonifyStructTable().update(BRIDGED_STRUCTURES)
    
_bridgePythonTypes()
