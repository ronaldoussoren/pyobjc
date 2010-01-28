__all__ = [ 'signature']

import os
import sys

def signature(signature, **kw):
    """
    A Python method decorator that allows easy specification
    of Objective-C selectors.

    Usage::
        
        @objc.signature('i@:if')
        def methodWithX_andY_(self, x, y):
            return 0
    """
    import warnings
    warnings.warn("Usage objc.typedSelector instead of objc.signature")
    from objc._objc import selector
    kw['signature'] = signature
    def makeSignature(func):
        return selector(func, **kw)
    return makeSignature
