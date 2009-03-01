"""
This module defines a number of context managers. These are meant to be used
in the context of the with statement (introduced in Python 2.5).
"""
from Quartz.CoreGraphics import *

__all__ = ('CGSavedGState', 'CGTransparencyLayer',  'CGContextPage')


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
    Context manager for working in a transparancylayer.

    Usage::

        with CGTransparencyLayer(context, info [, rect]):
            statement

    This is equivalent to:
        CGContextBeginTransparencyLayer(context, info)
        try:
            statement

        finally:
            CGContextEndTransparencyLayer(context)
    """
    def __init__(self, context, info, rect = None):
        self.context = context
        self.info = info
        self.rect = rect

    def __enter__(self):
        if self.rect is None:
            result = CGContextBeginTransparencyLayer(self.context, self.info)
        else:
            result = CGContextBeginTransparencyLayerWithRect(self.context, self.rect, self.info)
        return result

    def __exit__(self, exc_type, exc_value, exc_tp):
        CGContextEndTransparencyLayer(self.context)
        return False

class CGContextPage (object):
    """
    Context manager for saving and restoring the graphics state.

    Usage::

        with CGContextPage(context):
            statement

    This is equivalent to:
        CGContextBeginPage(context, None)
        try:
            statement

        finally:
            CGContextEndPage(context)
    """
    def __init__(self, context, mediaBox = None):
        self.context = context
        self.mediaBox = mediaBox

    def __enter__(self):
        mediaRect = CGContextBeginPage(self.context, self.mediaBox)

    def __exit__(self, exc_type, exc_value, exc_tp):
        CGContextEndPage(self.context)
        return False


