"""
A number of usefull categories on AppKit classes
"""
__all__ = ()
import objc
from AppKit import  NSGraphicsContext

class _ctxHelper(object):
    def __enter__(self):
        NSGraphicsContext.saveGraphicsState()

    def __exit__(self, exc_type, exc_value, exc_tb):
        NSGraphicsContext.restoreGraphicsState()
        return False


class NSGraphicsContext (objc.Category(NSGraphicsContext)):
    @classmethod
    def savedGraphicsState(self):
        return _ctxHelper()

try:
    from AppKit import  NSAnimationContext

    class NSAnimationContext (objc.Category(NSAnimationContext)):
        @classmethod
        def __enter__(cls):
            cls.beginGrouping()

        @classmethod
        def __exit__(cls, exc_type, exc_value, exc_tb):
            cls.endGrouping()
            return False

except ImportError:
    pass
