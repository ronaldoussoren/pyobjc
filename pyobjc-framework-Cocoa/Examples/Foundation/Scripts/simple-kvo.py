#!/usr/bin/python
"""
This script is a basic example of how to use Key Value Observation
in Python
"""

import objc
from Foundation import NSKeyValueChangeNewKey, NSKeyValueObservingOptionNew, NSObject


class MyClass(NSObject):
    base = objc.ivar("base", objc._C_INT)
    power = objc.ivar("power", objc._C_INT)

    def result(self):
        return self.base**self.power


MyClass.setKeys_triggerChangeNotificationsForDependentKey_(["base", "power"], "result")


class Observer(NSObject):
    def observeValueForKeyPath_ofObject_change_context_(
        self, path, an_object, changeDescription, context
    ):
        print(
            'path "%s" was changed to "%s".'
            % (path, changeDescription[NSKeyValueChangeNewKey])
        )


myInstance = MyClass.new()
observer = Observer.new()

myInstance.addObserver_forKeyPath_options_context_(
    observer, "result", NSKeyValueObservingOptionNew, 0
)
myInstance.addObserver_forKeyPath_options_context_(
    observer, "base", NSKeyValueObservingOptionNew, 0
)
myInstance.addObserver_forKeyPath_options_context_(
    observer, "power", NSKeyValueObservingOptionNew, 0
)

myInstance.setValue_forKey_(2, "base")
myInstance.power = 4

print(
    "%d ** %d == %d"
    % (myInstance.base, myInstance.valueForKey_("power"), myInstance.result())
)
