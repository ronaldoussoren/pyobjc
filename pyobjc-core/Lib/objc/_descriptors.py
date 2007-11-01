"""
Python <-> Objective-C bridge (PyObjC)

This module defines the core interfaces of the Python<->Objective-C bridge.
"""

__all__ = ['IBOutlet', 'IBAction', 'accessor', 'Accessor', 'typedAccessor', 'callbackFor', 'selectorFor', 'synthesize' ]

from _objc import ivar, selector, _makeClosure, selector, _C_SEL, _C_ID
import sys, textwrap

#
# Interface builder support.
#
def IBOutlet(name=None):
    """
    Create an instance variable that can be used as an outlet in
    Interface Builder.
    """
    if name is None:
        return ivar(isOutlet=1)
    else:
        return ivar(name, isOutlet=1)

def IBAction(func):
    """
    Return an Objective-C method object that can be used as an action
    in Interface Builder.
    """
    return selector(func, signature="v@:@")

def instancemethod(func):
    return selector(func, isClassMethod=False)

def accessor(func, typeSignature='@'):
    """
    Return an Objective-C method object that is conformant with key-value coding
    and key-value observing.
    """

    from inspect import getargspec
    args, varargs, varkw, defaults = getargspec(func)
    funcName = func.__name__
    maxArgs = len(args)
    minArgs = maxArgs - len(defaults or ())
    # implicit self
    selArgs = 1 + funcName.count('_')
    if varargs is not None or varkw is not None:
        raise TypeError('%s can not be an accessor because it accepts varargs or varkw' % (funcName,))

    if not (minArgs <= selArgs <= maxArgs):
        if selArgs == 3 and (minArgs <= 2 <= maxArgs) and funcName.startswith('validate') and funcName.endswith('_error_'):
            return selector(func, signature='c@:N^@o^@')
        elif minArgs == maxArgs:
            raise TypeError('%s expected to take %d args, but must accept %d from Objective-C (implicit self plus count of underscores)' % (funcName, maxArgs, selArgs))
        else:
            raise TypeError('%s expected to take between %d and %d args, but must accept %d from Objective-C (implicit self plus count of underscores)' % (funcName, minArgs, maxArgs, selArgs))
    
    if selArgs == 3:
        if funcName.startswith('insertObject_in') and funcName.endswith('AtIndex_'):
            return selector(func, signature='v@:@i')
        elif funcName.startswith('replaceObjectIn') and funcName.endswith('AtIndex_withObject_'):
            return selector(func, signature='v@:i@')
        
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

#
# Callback support
#
def callbackFor(callable, argIndex=-1):
    """
    Decorator for converting a function into an object that can be used
    as a callback function for (Objective-)C API's that take such a beast
    as one of their arguments.

    Note that using this decorator for methods is unsupported and that this
    decorator is optional when the callback isn't stored by the called function

    Usage::
        
        @objc.callbackFor(NSArray.sortedArrayUsingFunction_context_)
        def compare(left, right, context):
            return 1
    """
    def addClosure(function):
        closure = _makeClosure(function, callable, argIndex)
        function.pyobjc_closure = closure
        return function

    return addClosure

def selectorFor(callable, argIndex=-1):
    """
    Decorator that makes sure that the method has the right signature to be
    used as the selector argument to the specified method.

    Usage::
        
        @objc.selectorFor(NSApplication.beginSheet_modalForWindow_modalDelegate_didEndSelector_contextInfo_)
        def sheetDidEnd_returnCode_contextInfo_(self, sheet, returnCode, info):
            pass
    """
    if argIndex == -1:
        for arg in callable.__metadata__()['arguments']:
            if arg['type'] == _C_SEL and 'sel_of_type' in arg:
                signature = arg['sel_of_type']
                break
        else:
            raise ValueError("No selector argument with type information")

    else:
        signature = callable.__metadata__().arguments[idx]['type_of_sel']

    def addSignature(function): 
        return selector(function, signature=signature)

    return addSignature


def synthesize(name, copy=False, readwrite=True, type=_C_ID, ivarName=None):
    """
    Use this in a class dictionary to syntheze simple setting/setter methods.

    Note: this is only necessary to get propper behaviour when Key-Value coding
    is used and special features (like copying) are needed

    usage::
        
        class MyClass (NSObject):
            objc.synthesize('someTitle', copy=True)

    """
    if ivarName is None:
        ivarName = '_' + name

    classDict = sys._getframe(1).f_locals

    if copy:
        setter = textwrap.dedent('''
            def set%(name)s_(self, value):
                self.%(ivar)s = value.copy()
            ''' % dict(name=name.capitalize(), ivar=ivarName))

    else:
        setter = textwrap.dedent('''
            def set%(name)s_(self, value):
                self.%(ivar)s = value
            ''' % dict(name=name.capitalize(), ivar=ivarName))

    getter = textwrap.dedent('''
            def %(name)s(self):
                return self.%(ivar)s
            ''' % dict(name=name, ivar=ivarName))

    if readwrite:
        exec setter in classDict

    exec getter in classDict

    classDict[ivarName] = ivar(type=type)
