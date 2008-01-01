# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _pixel_format

def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "this"):
        if isinstance(value, class_type):
            self.__dict__[name] = value.this
            if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
            del value.thisown
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name) or (name == "thisown"):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


__version__ = _pixel_format.__version__
__date__ = _pixel_format.__date__
__api_version__ = _pixel_format.__api_version__
__author__ = _pixel_format.__author__
__doc__ = _pixel_format.__doc__

wglInitPixelFormatARB = _pixel_format.wglInitPixelFormatARB

__info = _pixel_format.__info

wglGetPixelFormatAttribivARB = _pixel_format.wglGetPixelFormatAttribivARB

wglGetPixelFormatAttribfvARB = _pixel_format.wglGetPixelFormatAttribfvARB
WGL_NUMBER_PIXEL_FORMATS_ARB = _pixel_format.WGL_NUMBER_PIXEL_FORMATS_ARB
WGL_DRAW_TO_WINDOW_ARB = _pixel_format.WGL_DRAW_TO_WINDOW_ARB
WGL_DRAW_TO_BITMAP_ARB = _pixel_format.WGL_DRAW_TO_BITMAP_ARB
WGL_ACCELERATION_ARB = _pixel_format.WGL_ACCELERATION_ARB
WGL_NEED_PALETTE_ARB = _pixel_format.WGL_NEED_PALETTE_ARB
WGL_NEED_SYSTEM_PALETTE_ARB = _pixel_format.WGL_NEED_SYSTEM_PALETTE_ARB
WGL_SWAP_LAYER_BUFFERS_ARB = _pixel_format.WGL_SWAP_LAYER_BUFFERS_ARB
WGL_SWAP_METHOD_ARB = _pixel_format.WGL_SWAP_METHOD_ARB
WGL_NUMBER_OVERLAYS_ARB = _pixel_format.WGL_NUMBER_OVERLAYS_ARB
WGL_NUMBER_UNDERLAYS_ARB = _pixel_format.WGL_NUMBER_UNDERLAYS_ARB
WGL_TRANSPARENT_ARB = _pixel_format.WGL_TRANSPARENT_ARB
WGL_TRANSPARENT_RED_VALUE_ARB = _pixel_format.WGL_TRANSPARENT_RED_VALUE_ARB
WGL_TRANSPARENT_GREEN_VALUE_ARB = _pixel_format.WGL_TRANSPARENT_GREEN_VALUE_ARB
WGL_TRANSPARENT_BLUE_VALUE_ARB = _pixel_format.WGL_TRANSPARENT_BLUE_VALUE_ARB
WGL_TRANSPARENT_ALPHA_VALUE_ARB = _pixel_format.WGL_TRANSPARENT_ALPHA_VALUE_ARB
WGL_TRANSPARENT_INDEX_VALUE_ARB = _pixel_format.WGL_TRANSPARENT_INDEX_VALUE_ARB
WGL_SHARE_DEPTH_ARB = _pixel_format.WGL_SHARE_DEPTH_ARB
WGL_SHARE_STENCIL_ARB = _pixel_format.WGL_SHARE_STENCIL_ARB
WGL_SHARE_ACCUM_ARB = _pixel_format.WGL_SHARE_ACCUM_ARB
WGL_SUPPORT_GDI_ARB = _pixel_format.WGL_SUPPORT_GDI_ARB
WGL_SUPPORT_OPENGL_ARB = _pixel_format.WGL_SUPPORT_OPENGL_ARB
WGL_DOUBLE_BUFFER_ARB = _pixel_format.WGL_DOUBLE_BUFFER_ARB
WGL_STEREO_ARB = _pixel_format.WGL_STEREO_ARB
WGL_PIXEL_TYPE_ARB = _pixel_format.WGL_PIXEL_TYPE_ARB
WGL_COLOR_BITS_ARB = _pixel_format.WGL_COLOR_BITS_ARB
WGL_RED_BITS_ARB = _pixel_format.WGL_RED_BITS_ARB
WGL_RED_SHIFT_ARB = _pixel_format.WGL_RED_SHIFT_ARB
WGL_GREEN_BITS_ARB = _pixel_format.WGL_GREEN_BITS_ARB
WGL_GREEN_SHIFT_ARB = _pixel_format.WGL_GREEN_SHIFT_ARB
WGL_BLUE_BITS_ARB = _pixel_format.WGL_BLUE_BITS_ARB
WGL_BLUE_SHIFT_ARB = _pixel_format.WGL_BLUE_SHIFT_ARB
WGL_ALPHA_BITS_ARB = _pixel_format.WGL_ALPHA_BITS_ARB
WGL_ALPHA_SHIFT_ARB = _pixel_format.WGL_ALPHA_SHIFT_ARB
WGL_ACCUM_BITS_ARB = _pixel_format.WGL_ACCUM_BITS_ARB
WGL_ACCUM_RED_BITS_ARB = _pixel_format.WGL_ACCUM_RED_BITS_ARB
WGL_ACCUM_GREEN_BITS_ARB = _pixel_format.WGL_ACCUM_GREEN_BITS_ARB
WGL_ACCUM_BLUE_BITS_ARB = _pixel_format.WGL_ACCUM_BLUE_BITS_ARB
WGL_ACCUM_ALPHA_BITS_ARB = _pixel_format.WGL_ACCUM_ALPHA_BITS_ARB
WGL_DEPTH_BITS_ARB = _pixel_format.WGL_DEPTH_BITS_ARB
WGL_STENCIL_BITS_ARB = _pixel_format.WGL_STENCIL_BITS_ARB
WGL_AUX_BUFFERS_ARB = _pixel_format.WGL_AUX_BUFFERS_ARB
WGL_NO_ACCELERATION_ARB = _pixel_format.WGL_NO_ACCELERATION_ARB
WGL_GENERIC_ACCELERATION_ARB = _pixel_format.WGL_GENERIC_ACCELERATION_ARB
WGL_FULL_ACCELERATION_ARB = _pixel_format.WGL_FULL_ACCELERATION_ARB
WGL_SWAP_EXCHANGE_ARB = _pixel_format.WGL_SWAP_EXCHANGE_ARB
WGL_SWAP_COPY_ARB = _pixel_format.WGL_SWAP_COPY_ARB
WGL_SWAP_UNDEFINED_ARB = _pixel_format.WGL_SWAP_UNDEFINED_ARB
WGL_TYPE_RGBA_ARB = _pixel_format.WGL_TYPE_RGBA_ARB
WGL_TYPE_COLORINDEX_ARB = _pixel_format.WGL_TYPE_COLORINDEX_ARB

