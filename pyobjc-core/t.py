
from Foundation import NSObject
from objc import python_method


class MyObject (NSObject):
    @python_method
    def my_method(self):
        return 42


print(MyObject.my_method)
print(MyObject.alloc().init().my_method)
print(MyObject.alloc().init().my_method())
