import objc
from PyObjCTools import Debugging

NSArray = objc.lookUpClass('NSArray')
a = NSArray.arrayWithArray_(['a', 'b', 'c'])
print(list(iter(a)))

Debugging.installVerboseExceptionHandler()
print(list(iter(a)))

print(a.__iter__)
