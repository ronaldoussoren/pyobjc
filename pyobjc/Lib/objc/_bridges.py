from _objc import *

__all__ = []

BRIDGED_STRUCTURES = {}
BRIDGED_TYPES = []

# XXX - these could let us remove code from OC_PythonObject
#NSNumber = lookUpClass('NSNumber')
#BRIDGED_TYPES.extend([
#    (bool, NSNumber.numberWithBool_),
#    (int, NSNumber.numberWithInt_),
#    (float, NSNumber.numberWithDouble_),
#    (long, NSNumber.numberWithLongLong_),
#])

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


class PyObjCData(lookUpClass('NSData')):
    def dataWithPyObject_(cls, anObject):
        self = cls.dataWithBytes_length_(anObject, len(anObject))
        self.__pyobjc_object__ = anObject
        return self
    dataWithPyObject_ = classmethod(dataWithPyObject_)

BRIDGED_TYPES.append((buffer, PyObjCData.dataWithPyObject_))


def _bridgePythonTypes():
    # python TO Obj-C
    OC_PythonObject = lookUpClass('OC_PythonObject')
    if BRIDGED_TYPES:
        OC_PythonObject.depythonifyTable().extend(BRIDGED_TYPES)
    if BRIDGED_STRUCTURES:
        OC_PythonObject.pythonifyStructTable().update(BRIDGED_STRUCTURES)
    
_bridgePythonTypes()
