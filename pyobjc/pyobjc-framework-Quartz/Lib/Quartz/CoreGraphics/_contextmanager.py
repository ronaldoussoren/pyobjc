"""
This module defines a number of context managers. These are meant to be used
in the context of the with statement (introduced in Python 2.5).
"""
class CGSavedGState (object):
    """
    Context manager for saving and restoring the graphics state.

    Usage::

        with  CGSavedGState(context):
            statement

    This is equivalent to:
        CGContextSaveGState(context)
        try:
            statement

        finally:
            CGContextRestoreGState(context)
    """
    def __init__(self, context):
        self.context = context

    def __enter__(self):
        CGContextSaveGState(self.context)
        return self

    def __exit__(self, exc_type, exc_value, exc_tp):
        CGContextRestoreGState(self.context)
        return False

class CGTransparencyLayer (object):
    """
    Context manager for saving and restoring the graphics state.

    Usage::

        with GTransparancyLayer(context):
            statement

    This is equivalent to:
        CGContextBeginTransparencyLayer(context)
        try:
            statement

        finally:
            CGContextEndTransparencyLayer(context)
    """
    def __init__(self, context):
        self.context = context

    def __enter__(self):
        CGContextBeginTransparencyLayer(self.context)
        return self

    def __exit__(self, exc_type, exc_value, exc_tp):
        CGContextEndTransparencyLayer(self.context)
        return False

class CGContextPage (object):
    """
    Context manager for saving and restoring the graphics state.

    Usage::

        with CGContextPage(context) as mediaRect:
            statement

    This is equivalent to:
        mediaRect = CGContextBeginPage(context, None)
        try:
            statement

        finally:
            CGContextEndPage(context)
    """
    def __init__(self, context):
        self.context = context

    def __enter__(self):
        mediaRect = CGContextBeginPage(self.context, None)
        return mediaRect

    def __exit__(self, exc_type, exc_value, exc_tp):
        CGContextEndPage(self.context)
        return False
