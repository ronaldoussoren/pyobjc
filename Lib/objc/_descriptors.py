"""
Python <-> Objective-C bridge (PyObjC)

This module defines the core interfaces of the Python<->Objective-C bridge.
"""

__all__ = ['IBOutlet', 'IBAction', 'accessor', 'Accessor', 'typedAccessor']

from _objc import ivar, selector
import inspect

#
# Interface builder support.
#
def IBOutlet(name):
    """
    Create an instance variable that can be used as an outlet in
    Interface Builder.
    """
    return ivar(name, isOutlet=1)

def IBAction(func):
    """
    Return an Objective-C method object that can be used as an action
    in Interface Builder.
    """
    return selector(func, signature="v@:@")

def accessor(func, typeSignature='@'):
    """
    Return an Objective-C method object that is conformant with key-value coding
    and key-value observing.
    """

    args, varargs, varkw, defaults = inspect.getargspec(func)
    funcName = func.__name__
    maxArgs = len(args)
    minArgs = maxArgs - len(defaults or ())
    # implicit self
    selArgs = 1 + funcName.count('_')
    if varargs is not None or varkw is not None:
        raise TypeError('%s can not be an accessor because it accepts varargs or varkw' % (funcName,))

    if not (minArgs <= selArgs <= maxArgs):
        if minArgs == maxArgs:
            raise TypeError('%s expected to take %d args, but must accept %d from Objective-C (implicit self plus count of underscores)' % (funcName, maxArgs, selArgs))
        else:
            raise TypeError('%s expected to take between %d and %d args, but must accept %d from Objective-C (implicit self plus count of underscores)' % (funcName, minArgs, maxArgs, selArgs))
    
    if selArgs == 3:
        if funcName.startswith('insertObject_in') and funcName.endswith('AtIndex_'):
            return selector(func, signature='v@:@i')
        elif funcName.startswith('replaceObjectIn') and funcName.endswith('AtIndex_withObject_'):
            return selector(func, signature='v@:i@')
        elif funcName.startswith('validate') and funcName.endswith('_error_'):
            return selector(func, signature='c@:N^@o^@')
        
        # pass through to "too many arguments"

    elif selArgs == 2:
        if funcName.startswith('objectIn') and funcName.endswith('AtIndex_'):
            return selector(func, signature='@@:i')
        elif funcName.startswith('removeObjectFrom') and funcName.endswith('AtIndex_'):
            return selector(func, signature='v@:i')
        elif funcName.startswith('get') and funcName.endswith('_range_'):
            return selector(func, signature='@@:{_NSRange=ii}')

        return selector(func, signature="v@:" + typeSignature)

    elif selArgs == 1:
        if typeSignature == '@' and func.func_name.startswith('countOf'):
            typeSignature = 'i'

        return selector(func, signature=typeSignature + "@:")

    elif selArgs == 0:
        raise TypeError("%s must take at least one argument to be an accessor" % (funcName,))

    raise TypeError("%s takes too many arguments to be an accessor" % (funcName,))

def typedAccessor(typeSignature):
    """
    Python 2.4 decorator for creating a typed accessor, usage:
        
        @typedAccessor('i')
        def someIntegerAccessor(self):
            return self.someInteger

        @typedAccessor('i')
        def setSomeIntegerAccessor_(self, anInteger):
            self.someInteger = anInteger
    """
    def _typedAccessor(func):
        return accessor(func, typeSignature)
    return _typedAccessor

def Accessor(func):
    import warnings
    warnings.warn(
        "Use objc.accessor instead of objc.Accessor", DeprecationWarning)
    return accessor(func)
