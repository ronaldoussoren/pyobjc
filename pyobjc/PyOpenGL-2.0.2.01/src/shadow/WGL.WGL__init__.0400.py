# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _WGL__init__

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


__version__ = _WGL__init__.__version__
__date__ = _WGL__init__.__date__
__api_version__ = _WGL__init__.__api_version__
__author__ = _WGL__init__.__author__
__doc__ = _WGL__init__.__doc__
class PIXELFORMATDESCRIPTOR(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PIXELFORMATDESCRIPTOR, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PIXELFORMATDESCRIPTOR, name)
    def __repr__(self):
        return "<%s.%s; proxy of C PIXELFORMATDESCRIPTOR instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    __swig_setmethods__["nSize"] = _WGL__init__.PIXELFORMATDESCRIPTOR_nSize_set
    __swig_getmethods__["nSize"] = _WGL__init__.PIXELFORMATDESCRIPTOR_nSize_get
    if _newclass:nSize = property(_WGL__init__.PIXELFORMATDESCRIPTOR_nSize_get, _WGL__init__.PIXELFORMATDESCRIPTOR_nSize_set)
    __swig_setmethods__["nVersion"] = _WGL__init__.PIXELFORMATDESCRIPTOR_nVersion_set
    __swig_getmethods__["nVersion"] = _WGL__init__.PIXELFORMATDESCRIPTOR_nVersion_get
    if _newclass:nVersion = property(_WGL__init__.PIXELFORMATDESCRIPTOR_nVersion_get, _WGL__init__.PIXELFORMATDESCRIPTOR_nVersion_set)
    __swig_setmethods__["dwFlags"] = _WGL__init__.PIXELFORMATDESCRIPTOR_dwFlags_set
    __swig_getmethods__["dwFlags"] = _WGL__init__.PIXELFORMATDESCRIPTOR_dwFlags_get
    if _newclass:dwFlags = property(_WGL__init__.PIXELFORMATDESCRIPTOR_dwFlags_get, _WGL__init__.PIXELFORMATDESCRIPTOR_dwFlags_set)
    __swig_setmethods__["iPixelType"] = _WGL__init__.PIXELFORMATDESCRIPTOR_iPixelType_set
    __swig_getmethods__["iPixelType"] = _WGL__init__.PIXELFORMATDESCRIPTOR_iPixelType_get
    if _newclass:iPixelType = property(_WGL__init__.PIXELFORMATDESCRIPTOR_iPixelType_get, _WGL__init__.PIXELFORMATDESCRIPTOR_iPixelType_set)
    __swig_setmethods__["cColorBits"] = _WGL__init__.PIXELFORMATDESCRIPTOR_cColorBits_set
    __swig_getmethods__["cColorBits"] = _WGL__init__.PIXELFORMATDESCRIPTOR_cColorBits_get
    if _newclass:cColorBits = property(_WGL__init__.PIXELFORMATDESCRIPTOR_cColorBits_get, _WGL__init__.PIXELFORMATDESCRIPTOR_cColorBits_set)
    __swig_setmethods__["cRedBits"] = _WGL__init__.PIXELFORMATDESCRIPTOR_cRedBits_set
    __swig_getmethods__["cRedBits"] = _WGL__init__.PIXELFORMATDESCRIPTOR_cRedBits_get
    if _newclass:cRedBits = property(_WGL__init__.PIXELFORMATDESCRIPTOR_cRedBits_get, _WGL__init__.PIXELFORMATDESCRIPTOR_cRedBits_set)
    __swig_setmethods__["cRedShift"] = _WGL__init__.PIXELFORMATDESCRIPTOR_cRedShift_set
    __swig_getmethods__["cRedShift"] = _WGL__init__.PIXELFORMATDESCRIPTOR_cRedShift_get
    if _newclass:cRedShift = property(_WGL__init__.PIXELFORMATDESCRIPTOR_cRedShift_get, _WGL__init__.PIXELFORMATDESCRIPTOR_cRedShift_set)
    __swig_setmethods__["cGreenBits"] = _WGL__init__.PIXELFORMATDESCRIPTOR_cGreenBits_set
    __swig_getmethods__["cGreenBits"] = _WGL__init__.PIXELFORMATDESCRIPTOR_cGreenBits_get
    if _newclass:cGreenBits = property(_WGL__init__.PIXELFORMATDESCRIPTOR_cGreenBits_get, _WGL__init__.PIXELFORMATDESCRIPTOR_cGreenBits_set)
    __swig_setmethods__["cGreenShift"] = _WGL__init__.PIXELFORMATDESCRIPTOR_cGreenShift_set
    __swig_getmethods__["cGreenShift"] = _WGL__init__.PIXELFORMATDESCRIPTOR_cGreenShift_get
    if _newclass:cGreenShift = property(_WGL__init__.PIXELFORMATDESCRIPTOR_cGreenShift_get, _WGL__init__.PIXELFORMATDESCRIPTOR_cGreenShift_set)
    __swig_setmethods__["cBlueBits"] = _WGL__init__.PIXELFORMATDESCRIPTOR_cBlueBits_set
    __swig_getmethods__["cBlueBits"] = _WGL__init__.PIXELFORMATDESCRIPTOR_cBlueBits_get
    if _newclass:cBlueBits = property(_WGL__init__.PIXELFORMATDESCRIPTOR_cBlueBits_get, _WGL__init__.PIXELFORMATDESCRIPTOR_cBlueBits_set)
    __swig_setmethods__["cBlueShift"] = _WGL__init__.PIXELFORMATDESCRIPTOR_cBlueShift_set
    __swig_getmethods__["cBlueShift"] = _WGL__init__.PIXELFORMATDESCRIPTOR_cBlueShift_get
    if _newclass:cBlueShift = property(_WGL__init__.PIXELFORMATDESCRIPTOR_cBlueShift_get, _WGL__init__.PIXELFORMATDESCRIPTOR_cBlueShift_set)
    __swig_setmethods__["cAlphaBits"] = _WGL__init__.PIXELFORMATDESCRIPTOR_cAlphaBits_set
    __swig_getmethods__["cAlphaBits"] = _WGL__init__.PIXELFORMATDESCRIPTOR_cAlphaBits_get
    if _newclass:cAlphaBits = property(_WGL__init__.PIXELFORMATDESCRIPTOR_cAlphaBits_get, _WGL__init__.PIXELFORMATDESCRIPTOR_cAlphaBits_set)
    __swig_setmethods__["cAlphaShift"] = _WGL__init__.PIXELFORMATDESCRIPTOR_cAlphaShift_set
    __swig_getmethods__["cAlphaShift"] = _WGL__init__.PIXELFORMATDESCRIPTOR_cAlphaShift_get
    if _newclass:cAlphaShift = property(_WGL__init__.PIXELFORMATDESCRIPTOR_cAlphaShift_get, _WGL__init__.PIXELFORMATDESCRIPTOR_cAlphaShift_set)
    __swig_setmethods__["cAccumBits"] = _WGL__init__.PIXELFORMATDESCRIPTOR_cAccumBits_set
    __swig_getmethods__["cAccumBits"] = _WGL__init__.PIXELFORMATDESCRIPTOR_cAccumBits_get
    if _newclass:cAccumBits = property(_WGL__init__.PIXELFORMATDESCRIPTOR_cAccumBits_get, _WGL__init__.PIXELFORMATDESCRIPTOR_cAccumBits_set)
    __swig_setmethods__["cAccumRedBits"] = _WGL__init__.PIXELFORMATDESCRIPTOR_cAccumRedBits_set
    __swig_getmethods__["cAccumRedBits"] = _WGL__init__.PIXELFORMATDESCRIPTOR_cAccumRedBits_get
    if _newclass:cAccumRedBits = property(_WGL__init__.PIXELFORMATDESCRIPTOR_cAccumRedBits_get, _WGL__init__.PIXELFORMATDESCRIPTOR_cAccumRedBits_set)
    __swig_setmethods__["cAccumGreenBits"] = _WGL__init__.PIXELFORMATDESCRIPTOR_cAccumGreenBits_set
    __swig_getmethods__["cAccumGreenBits"] = _WGL__init__.PIXELFORMATDESCRIPTOR_cAccumGreenBits_get
    if _newclass:cAccumGreenBits = property(_WGL__init__.PIXELFORMATDESCRIPTOR_cAccumGreenBits_get, _WGL__init__.PIXELFORMATDESCRIPTOR_cAccumGreenBits_set)
    __swig_setmethods__["cAccumBlueBits"] = _WGL__init__.PIXELFORMATDESCRIPTOR_cAccumBlueBits_set
    __swig_getmethods__["cAccumBlueBits"] = _WGL__init__.PIXELFORMATDESCRIPTOR_cAccumBlueBits_get
    if _newclass:cAccumBlueBits = property(_WGL__init__.PIXELFORMATDESCRIPTOR_cAccumBlueBits_get, _WGL__init__.PIXELFORMATDESCRIPTOR_cAccumBlueBits_set)
    __swig_setmethods__["cAccumAlphaBits"] = _WGL__init__.PIXELFORMATDESCRIPTOR_cAccumAlphaBits_set
    __swig_getmethods__["cAccumAlphaBits"] = _WGL__init__.PIXELFORMATDESCRIPTOR_cAccumAlphaBits_get
    if _newclass:cAccumAlphaBits = property(_WGL__init__.PIXELFORMATDESCRIPTOR_cAccumAlphaBits_get, _WGL__init__.PIXELFORMATDESCRIPTOR_cAccumAlphaBits_set)
    __swig_setmethods__["cDepthBits"] = _WGL__init__.PIXELFORMATDESCRIPTOR_cDepthBits_set
    __swig_getmethods__["cDepthBits"] = _WGL__init__.PIXELFORMATDESCRIPTOR_cDepthBits_get
    if _newclass:cDepthBits = property(_WGL__init__.PIXELFORMATDESCRIPTOR_cDepthBits_get, _WGL__init__.PIXELFORMATDESCRIPTOR_cDepthBits_set)
    __swig_setmethods__["cStencilBits"] = _WGL__init__.PIXELFORMATDESCRIPTOR_cStencilBits_set
    __swig_getmethods__["cStencilBits"] = _WGL__init__.PIXELFORMATDESCRIPTOR_cStencilBits_get
    if _newclass:cStencilBits = property(_WGL__init__.PIXELFORMATDESCRIPTOR_cStencilBits_get, _WGL__init__.PIXELFORMATDESCRIPTOR_cStencilBits_set)
    __swig_setmethods__["cAuxBuffers"] = _WGL__init__.PIXELFORMATDESCRIPTOR_cAuxBuffers_set
    __swig_getmethods__["cAuxBuffers"] = _WGL__init__.PIXELFORMATDESCRIPTOR_cAuxBuffers_get
    if _newclass:cAuxBuffers = property(_WGL__init__.PIXELFORMATDESCRIPTOR_cAuxBuffers_get, _WGL__init__.PIXELFORMATDESCRIPTOR_cAuxBuffers_set)
    __swig_setmethods__["iLayerType"] = _WGL__init__.PIXELFORMATDESCRIPTOR_iLayerType_set
    __swig_getmethods__["iLayerType"] = _WGL__init__.PIXELFORMATDESCRIPTOR_iLayerType_get
    if _newclass:iLayerType = property(_WGL__init__.PIXELFORMATDESCRIPTOR_iLayerType_get, _WGL__init__.PIXELFORMATDESCRIPTOR_iLayerType_set)
    __swig_setmethods__["bReserved"] = _WGL__init__.PIXELFORMATDESCRIPTOR_bReserved_set
    __swig_getmethods__["bReserved"] = _WGL__init__.PIXELFORMATDESCRIPTOR_bReserved_get
    if _newclass:bReserved = property(_WGL__init__.PIXELFORMATDESCRIPTOR_bReserved_get, _WGL__init__.PIXELFORMATDESCRIPTOR_bReserved_set)
    __swig_setmethods__["dwLayerMask"] = _WGL__init__.PIXELFORMATDESCRIPTOR_dwLayerMask_set
    __swig_getmethods__["dwLayerMask"] = _WGL__init__.PIXELFORMATDESCRIPTOR_dwLayerMask_get
    if _newclass:dwLayerMask = property(_WGL__init__.PIXELFORMATDESCRIPTOR_dwLayerMask_get, _WGL__init__.PIXELFORMATDESCRIPTOR_dwLayerMask_set)
    __swig_setmethods__["dwVisibleMask"] = _WGL__init__.PIXELFORMATDESCRIPTOR_dwVisibleMask_set
    __swig_getmethods__["dwVisibleMask"] = _WGL__init__.PIXELFORMATDESCRIPTOR_dwVisibleMask_get
    if _newclass:dwVisibleMask = property(_WGL__init__.PIXELFORMATDESCRIPTOR_dwVisibleMask_get, _WGL__init__.PIXELFORMATDESCRIPTOR_dwVisibleMask_set)
    __swig_setmethods__["dwDamageMask"] = _WGL__init__.PIXELFORMATDESCRIPTOR_dwDamageMask_set
    __swig_getmethods__["dwDamageMask"] = _WGL__init__.PIXELFORMATDESCRIPTOR_dwDamageMask_get
    if _newclass:dwDamageMask = property(_WGL__init__.PIXELFORMATDESCRIPTOR_dwDamageMask_get, _WGL__init__.PIXELFORMATDESCRIPTOR_dwDamageMask_set)
    def __init__(self, *args):
        _swig_setattr(self, PIXELFORMATDESCRIPTOR, 'this', _WGL__init__.new_PIXELFORMATDESCRIPTOR(*args))
        _swig_setattr(self, PIXELFORMATDESCRIPTOR, 'thisown', 1)
    def __del__(self, destroy=_WGL__init__.delete_PIXELFORMATDESCRIPTOR):
        try:
            if self.thisown: destroy(self)
        except: pass


class PIXELFORMATDESCRIPTORPtr(PIXELFORMATDESCRIPTOR):
    def __init__(self, this):
        _swig_setattr(self, PIXELFORMATDESCRIPTOR, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, PIXELFORMATDESCRIPTOR, 'thisown', 0)
        _swig_setattr(self, PIXELFORMATDESCRIPTOR,self.__class__,PIXELFORMATDESCRIPTOR)
_WGL__init__.PIXELFORMATDESCRIPTOR_swigregister(PIXELFORMATDESCRIPTORPtr)

PFD_TYPE_RGBA = _WGL__init__.PFD_TYPE_RGBA
PFD_TYPE_COLORINDEX = _WGL__init__.PFD_TYPE_COLORINDEX
PFD_MAIN_PLANE = _WGL__init__.PFD_MAIN_PLANE
PFD_OVERLAY_PLANE = _WGL__init__.PFD_OVERLAY_PLANE
PFD_UNDERLAY_PLANE = _WGL__init__.PFD_UNDERLAY_PLANE
PFD_DOUBLEBUFFER = _WGL__init__.PFD_DOUBLEBUFFER
PFD_STEREO = _WGL__init__.PFD_STEREO
PFD_DRAW_TO_WINDOW = _WGL__init__.PFD_DRAW_TO_WINDOW
PFD_DRAW_TO_BITMAP = _WGL__init__.PFD_DRAW_TO_BITMAP
PFD_SUPPORT_GDI = _WGL__init__.PFD_SUPPORT_GDI
PFD_SUPPORT_OPENGL = _WGL__init__.PFD_SUPPORT_OPENGL
PFD_GENERIC_FORMAT = _WGL__init__.PFD_GENERIC_FORMAT
PFD_NEED_PALETTE = _WGL__init__.PFD_NEED_PALETTE
PFD_NEED_SYSTEM_PALETTE = _WGL__init__.PFD_NEED_SYSTEM_PALETTE
PFD_SWAP_EXCHANGE = _WGL__init__.PFD_SWAP_EXCHANGE
PFD_SWAP_COPY = _WGL__init__.PFD_SWAP_COPY
PFD_SWAP_LAYER_BUFFERS = _WGL__init__.PFD_SWAP_LAYER_BUFFERS
PFD_GENERIC_ACCELERATED = _WGL__init__.PFD_GENERIC_ACCELERATED
PFD_SUPPORT_DIRECTDRAW = _WGL__init__.PFD_SUPPORT_DIRECTDRAW
PFD_DEPTH_DONTCARE = _WGL__init__.PFD_DEPTH_DONTCARE
PFD_DOUBLEBUFFER_DONTCARE = _WGL__init__.PFD_DOUBLEBUFFER_DONTCARE
PFD_STEREO_DONTCARE = _WGL__init__.PFD_STEREO_DONTCARE
class POINTFLOAT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, POINTFLOAT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, POINTFLOAT, name)
    def __repr__(self):
        return "<%s.%s; proxy of C POINTFLOAT instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    __swig_setmethods__["x"] = _WGL__init__.POINTFLOAT_x_set
    __swig_getmethods__["x"] = _WGL__init__.POINTFLOAT_x_get
    if _newclass:x = property(_WGL__init__.POINTFLOAT_x_get, _WGL__init__.POINTFLOAT_x_set)
    __swig_setmethods__["y"] = _WGL__init__.POINTFLOAT_y_set
    __swig_getmethods__["y"] = _WGL__init__.POINTFLOAT_y_get
    if _newclass:y = property(_WGL__init__.POINTFLOAT_y_get, _WGL__init__.POINTFLOAT_y_set)
    def __init__(self, *args):
        _swig_setattr(self, POINTFLOAT, 'this', _WGL__init__.new_POINTFLOAT(*args))
        _swig_setattr(self, POINTFLOAT, 'thisown', 1)
    def __del__(self, destroy=_WGL__init__.delete_POINTFLOAT):
        try:
            if self.thisown: destroy(self)
        except: pass


class POINTFLOATPtr(POINTFLOAT):
    def __init__(self, this):
        _swig_setattr(self, POINTFLOAT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, POINTFLOAT, 'thisown', 0)
        _swig_setattr(self, POINTFLOAT,self.__class__,POINTFLOAT)
_WGL__init__.POINTFLOAT_swigregister(POINTFLOATPtr)

class GLYPHMETRICSFLOAT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, GLYPHMETRICSFLOAT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, GLYPHMETRICSFLOAT, name)
    def __repr__(self):
        return "<%s.%s; proxy of C GLYPHMETRICSFLOAT instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    __swig_setmethods__["gmfBlackBoxX"] = _WGL__init__.GLYPHMETRICSFLOAT_gmfBlackBoxX_set
    __swig_getmethods__["gmfBlackBoxX"] = _WGL__init__.GLYPHMETRICSFLOAT_gmfBlackBoxX_get
    if _newclass:gmfBlackBoxX = property(_WGL__init__.GLYPHMETRICSFLOAT_gmfBlackBoxX_get, _WGL__init__.GLYPHMETRICSFLOAT_gmfBlackBoxX_set)
    __swig_setmethods__["gmfBlackBoxY"] = _WGL__init__.GLYPHMETRICSFLOAT_gmfBlackBoxY_set
    __swig_getmethods__["gmfBlackBoxY"] = _WGL__init__.GLYPHMETRICSFLOAT_gmfBlackBoxY_get
    if _newclass:gmfBlackBoxY = property(_WGL__init__.GLYPHMETRICSFLOAT_gmfBlackBoxY_get, _WGL__init__.GLYPHMETRICSFLOAT_gmfBlackBoxY_set)
    __swig_setmethods__["gmfptGlyphOrigin"] = _WGL__init__.GLYPHMETRICSFLOAT_gmfptGlyphOrigin_set
    __swig_getmethods__["gmfptGlyphOrigin"] = _WGL__init__.GLYPHMETRICSFLOAT_gmfptGlyphOrigin_get
    if _newclass:gmfptGlyphOrigin = property(_WGL__init__.GLYPHMETRICSFLOAT_gmfptGlyphOrigin_get, _WGL__init__.GLYPHMETRICSFLOAT_gmfptGlyphOrigin_set)
    __swig_setmethods__["gmfCellIncX"] = _WGL__init__.GLYPHMETRICSFLOAT_gmfCellIncX_set
    __swig_getmethods__["gmfCellIncX"] = _WGL__init__.GLYPHMETRICSFLOAT_gmfCellIncX_get
    if _newclass:gmfCellIncX = property(_WGL__init__.GLYPHMETRICSFLOAT_gmfCellIncX_get, _WGL__init__.GLYPHMETRICSFLOAT_gmfCellIncX_set)
    __swig_setmethods__["gmfCellIncY"] = _WGL__init__.GLYPHMETRICSFLOAT_gmfCellIncY_set
    __swig_getmethods__["gmfCellIncY"] = _WGL__init__.GLYPHMETRICSFLOAT_gmfCellIncY_get
    if _newclass:gmfCellIncY = property(_WGL__init__.GLYPHMETRICSFLOAT_gmfCellIncY_get, _WGL__init__.GLYPHMETRICSFLOAT_gmfCellIncY_set)
    def __init__(self, *args):
        _swig_setattr(self, GLYPHMETRICSFLOAT, 'this', _WGL__init__.new_GLYPHMETRICSFLOAT(*args))
        _swig_setattr(self, GLYPHMETRICSFLOAT, 'thisown', 1)
    def __del__(self, destroy=_WGL__init__.delete_GLYPHMETRICSFLOAT):
        try:
            if self.thisown: destroy(self)
        except: pass


class GLYPHMETRICSFLOATPtr(GLYPHMETRICSFLOAT):
    def __init__(self, this):
        _swig_setattr(self, GLYPHMETRICSFLOAT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, GLYPHMETRICSFLOAT, 'thisown', 0)
        _swig_setattr(self, GLYPHMETRICSFLOAT,self.__class__,GLYPHMETRICSFLOAT)
_WGL__init__.GLYPHMETRICSFLOAT_swigregister(GLYPHMETRICSFLOATPtr)

WGL_FONT_LINES = _WGL__init__.WGL_FONT_LINES
WGL_FONT_POLYGONS = _WGL__init__.WGL_FONT_POLYGONS
class LAYERPLANEDESCRIPTOR(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, LAYERPLANEDESCRIPTOR, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, LAYERPLANEDESCRIPTOR, name)
    def __repr__(self):
        return "<%s.%s; proxy of C LAYERPLANEDESCRIPTOR instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    __swig_setmethods__["nSize"] = _WGL__init__.LAYERPLANEDESCRIPTOR_nSize_set
    __swig_getmethods__["nSize"] = _WGL__init__.LAYERPLANEDESCRIPTOR_nSize_get
    if _newclass:nSize = property(_WGL__init__.LAYERPLANEDESCRIPTOR_nSize_get, _WGL__init__.LAYERPLANEDESCRIPTOR_nSize_set)
    __swig_setmethods__["nVersion"] = _WGL__init__.LAYERPLANEDESCRIPTOR_nVersion_set
    __swig_getmethods__["nVersion"] = _WGL__init__.LAYERPLANEDESCRIPTOR_nVersion_get
    if _newclass:nVersion = property(_WGL__init__.LAYERPLANEDESCRIPTOR_nVersion_get, _WGL__init__.LAYERPLANEDESCRIPTOR_nVersion_set)
    __swig_setmethods__["dwFlags"] = _WGL__init__.LAYERPLANEDESCRIPTOR_dwFlags_set
    __swig_getmethods__["dwFlags"] = _WGL__init__.LAYERPLANEDESCRIPTOR_dwFlags_get
    if _newclass:dwFlags = property(_WGL__init__.LAYERPLANEDESCRIPTOR_dwFlags_get, _WGL__init__.LAYERPLANEDESCRIPTOR_dwFlags_set)
    __swig_setmethods__["iPixelType"] = _WGL__init__.LAYERPLANEDESCRIPTOR_iPixelType_set
    __swig_getmethods__["iPixelType"] = _WGL__init__.LAYERPLANEDESCRIPTOR_iPixelType_get
    if _newclass:iPixelType = property(_WGL__init__.LAYERPLANEDESCRIPTOR_iPixelType_get, _WGL__init__.LAYERPLANEDESCRIPTOR_iPixelType_set)
    __swig_setmethods__["cColorBits"] = _WGL__init__.LAYERPLANEDESCRIPTOR_cColorBits_set
    __swig_getmethods__["cColorBits"] = _WGL__init__.LAYERPLANEDESCRIPTOR_cColorBits_get
    if _newclass:cColorBits = property(_WGL__init__.LAYERPLANEDESCRIPTOR_cColorBits_get, _WGL__init__.LAYERPLANEDESCRIPTOR_cColorBits_set)
    __swig_setmethods__["cRedBits"] = _WGL__init__.LAYERPLANEDESCRIPTOR_cRedBits_set
    __swig_getmethods__["cRedBits"] = _WGL__init__.LAYERPLANEDESCRIPTOR_cRedBits_get
    if _newclass:cRedBits = property(_WGL__init__.LAYERPLANEDESCRIPTOR_cRedBits_get, _WGL__init__.LAYERPLANEDESCRIPTOR_cRedBits_set)
    __swig_setmethods__["cRedShift"] = _WGL__init__.LAYERPLANEDESCRIPTOR_cRedShift_set
    __swig_getmethods__["cRedShift"] = _WGL__init__.LAYERPLANEDESCRIPTOR_cRedShift_get
    if _newclass:cRedShift = property(_WGL__init__.LAYERPLANEDESCRIPTOR_cRedShift_get, _WGL__init__.LAYERPLANEDESCRIPTOR_cRedShift_set)
    __swig_setmethods__["cGreenBits"] = _WGL__init__.LAYERPLANEDESCRIPTOR_cGreenBits_set
    __swig_getmethods__["cGreenBits"] = _WGL__init__.LAYERPLANEDESCRIPTOR_cGreenBits_get
    if _newclass:cGreenBits = property(_WGL__init__.LAYERPLANEDESCRIPTOR_cGreenBits_get, _WGL__init__.LAYERPLANEDESCRIPTOR_cGreenBits_set)
    __swig_setmethods__["cGreenShift"] = _WGL__init__.LAYERPLANEDESCRIPTOR_cGreenShift_set
    __swig_getmethods__["cGreenShift"] = _WGL__init__.LAYERPLANEDESCRIPTOR_cGreenShift_get
    if _newclass:cGreenShift = property(_WGL__init__.LAYERPLANEDESCRIPTOR_cGreenShift_get, _WGL__init__.LAYERPLANEDESCRIPTOR_cGreenShift_set)
    __swig_setmethods__["cBlueBits"] = _WGL__init__.LAYERPLANEDESCRIPTOR_cBlueBits_set
    __swig_getmethods__["cBlueBits"] = _WGL__init__.LAYERPLANEDESCRIPTOR_cBlueBits_get
    if _newclass:cBlueBits = property(_WGL__init__.LAYERPLANEDESCRIPTOR_cBlueBits_get, _WGL__init__.LAYERPLANEDESCRIPTOR_cBlueBits_set)
    __swig_setmethods__["cBlueShift"] = _WGL__init__.LAYERPLANEDESCRIPTOR_cBlueShift_set
    __swig_getmethods__["cBlueShift"] = _WGL__init__.LAYERPLANEDESCRIPTOR_cBlueShift_get
    if _newclass:cBlueShift = property(_WGL__init__.LAYERPLANEDESCRIPTOR_cBlueShift_get, _WGL__init__.LAYERPLANEDESCRIPTOR_cBlueShift_set)
    __swig_setmethods__["cAlphaBits"] = _WGL__init__.LAYERPLANEDESCRIPTOR_cAlphaBits_set
    __swig_getmethods__["cAlphaBits"] = _WGL__init__.LAYERPLANEDESCRIPTOR_cAlphaBits_get
    if _newclass:cAlphaBits = property(_WGL__init__.LAYERPLANEDESCRIPTOR_cAlphaBits_get, _WGL__init__.LAYERPLANEDESCRIPTOR_cAlphaBits_set)
    __swig_setmethods__["cAlphaShift"] = _WGL__init__.LAYERPLANEDESCRIPTOR_cAlphaShift_set
    __swig_getmethods__["cAlphaShift"] = _WGL__init__.LAYERPLANEDESCRIPTOR_cAlphaShift_get
    if _newclass:cAlphaShift = property(_WGL__init__.LAYERPLANEDESCRIPTOR_cAlphaShift_get, _WGL__init__.LAYERPLANEDESCRIPTOR_cAlphaShift_set)
    __swig_setmethods__["cAccumBits"] = _WGL__init__.LAYERPLANEDESCRIPTOR_cAccumBits_set
    __swig_getmethods__["cAccumBits"] = _WGL__init__.LAYERPLANEDESCRIPTOR_cAccumBits_get
    if _newclass:cAccumBits = property(_WGL__init__.LAYERPLANEDESCRIPTOR_cAccumBits_get, _WGL__init__.LAYERPLANEDESCRIPTOR_cAccumBits_set)
    __swig_setmethods__["cAccumRedBits"] = _WGL__init__.LAYERPLANEDESCRIPTOR_cAccumRedBits_set
    __swig_getmethods__["cAccumRedBits"] = _WGL__init__.LAYERPLANEDESCRIPTOR_cAccumRedBits_get
    if _newclass:cAccumRedBits = property(_WGL__init__.LAYERPLANEDESCRIPTOR_cAccumRedBits_get, _WGL__init__.LAYERPLANEDESCRIPTOR_cAccumRedBits_set)
    __swig_setmethods__["cAccumGreenBits"] = _WGL__init__.LAYERPLANEDESCRIPTOR_cAccumGreenBits_set
    __swig_getmethods__["cAccumGreenBits"] = _WGL__init__.LAYERPLANEDESCRIPTOR_cAccumGreenBits_get
    if _newclass:cAccumGreenBits = property(_WGL__init__.LAYERPLANEDESCRIPTOR_cAccumGreenBits_get, _WGL__init__.LAYERPLANEDESCRIPTOR_cAccumGreenBits_set)
    __swig_setmethods__["cAccumBlueBits"] = _WGL__init__.LAYERPLANEDESCRIPTOR_cAccumBlueBits_set
    __swig_getmethods__["cAccumBlueBits"] = _WGL__init__.LAYERPLANEDESCRIPTOR_cAccumBlueBits_get
    if _newclass:cAccumBlueBits = property(_WGL__init__.LAYERPLANEDESCRIPTOR_cAccumBlueBits_get, _WGL__init__.LAYERPLANEDESCRIPTOR_cAccumBlueBits_set)
    __swig_setmethods__["cAccumAlphaBits"] = _WGL__init__.LAYERPLANEDESCRIPTOR_cAccumAlphaBits_set
    __swig_getmethods__["cAccumAlphaBits"] = _WGL__init__.LAYERPLANEDESCRIPTOR_cAccumAlphaBits_get
    if _newclass:cAccumAlphaBits = property(_WGL__init__.LAYERPLANEDESCRIPTOR_cAccumAlphaBits_get, _WGL__init__.LAYERPLANEDESCRIPTOR_cAccumAlphaBits_set)
    __swig_setmethods__["cDepthBits"] = _WGL__init__.LAYERPLANEDESCRIPTOR_cDepthBits_set
    __swig_getmethods__["cDepthBits"] = _WGL__init__.LAYERPLANEDESCRIPTOR_cDepthBits_get
    if _newclass:cDepthBits = property(_WGL__init__.LAYERPLANEDESCRIPTOR_cDepthBits_get, _WGL__init__.LAYERPLANEDESCRIPTOR_cDepthBits_set)
    __swig_setmethods__["cStencilBits"] = _WGL__init__.LAYERPLANEDESCRIPTOR_cStencilBits_set
    __swig_getmethods__["cStencilBits"] = _WGL__init__.LAYERPLANEDESCRIPTOR_cStencilBits_get
    if _newclass:cStencilBits = property(_WGL__init__.LAYERPLANEDESCRIPTOR_cStencilBits_get, _WGL__init__.LAYERPLANEDESCRIPTOR_cStencilBits_set)
    __swig_setmethods__["cAuxBuffers"] = _WGL__init__.LAYERPLANEDESCRIPTOR_cAuxBuffers_set
    __swig_getmethods__["cAuxBuffers"] = _WGL__init__.LAYERPLANEDESCRIPTOR_cAuxBuffers_get
    if _newclass:cAuxBuffers = property(_WGL__init__.LAYERPLANEDESCRIPTOR_cAuxBuffers_get, _WGL__init__.LAYERPLANEDESCRIPTOR_cAuxBuffers_set)
    __swig_setmethods__["iLayerPlane"] = _WGL__init__.LAYERPLANEDESCRIPTOR_iLayerPlane_set
    __swig_getmethods__["iLayerPlane"] = _WGL__init__.LAYERPLANEDESCRIPTOR_iLayerPlane_get
    if _newclass:iLayerPlane = property(_WGL__init__.LAYERPLANEDESCRIPTOR_iLayerPlane_get, _WGL__init__.LAYERPLANEDESCRIPTOR_iLayerPlane_set)
    __swig_setmethods__["bReserved"] = _WGL__init__.LAYERPLANEDESCRIPTOR_bReserved_set
    __swig_getmethods__["bReserved"] = _WGL__init__.LAYERPLANEDESCRIPTOR_bReserved_get
    if _newclass:bReserved = property(_WGL__init__.LAYERPLANEDESCRIPTOR_bReserved_get, _WGL__init__.LAYERPLANEDESCRIPTOR_bReserved_set)
    __swig_setmethods__["crTransparent"] = _WGL__init__.LAYERPLANEDESCRIPTOR_crTransparent_set
    __swig_getmethods__["crTransparent"] = _WGL__init__.LAYERPLANEDESCRIPTOR_crTransparent_get
    if _newclass:crTransparent = property(_WGL__init__.LAYERPLANEDESCRIPTOR_crTransparent_get, _WGL__init__.LAYERPLANEDESCRIPTOR_crTransparent_set)
    def __init__(self, *args):
        _swig_setattr(self, LAYERPLANEDESCRIPTOR, 'this', _WGL__init__.new_LAYERPLANEDESCRIPTOR(*args))
        _swig_setattr(self, LAYERPLANEDESCRIPTOR, 'thisown', 1)
    def __del__(self, destroy=_WGL__init__.delete_LAYERPLANEDESCRIPTOR):
        try:
            if self.thisown: destroy(self)
        except: pass


class LAYERPLANEDESCRIPTORPtr(LAYERPLANEDESCRIPTOR):
    def __init__(self, this):
        _swig_setattr(self, LAYERPLANEDESCRIPTOR, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, LAYERPLANEDESCRIPTOR, 'thisown', 0)
        _swig_setattr(self, LAYERPLANEDESCRIPTOR,self.__class__,LAYERPLANEDESCRIPTOR)
_WGL__init__.LAYERPLANEDESCRIPTOR_swigregister(LAYERPLANEDESCRIPTORPtr)

LPD_DOUBLEBUFFER = _WGL__init__.LPD_DOUBLEBUFFER
LPD_STEREO = _WGL__init__.LPD_STEREO
LPD_SUPPORT_GDI = _WGL__init__.LPD_SUPPORT_GDI
LPD_SUPPORT_OPENGL = _WGL__init__.LPD_SUPPORT_OPENGL
LPD_SHARE_DEPTH = _WGL__init__.LPD_SHARE_DEPTH
LPD_SHARE_STENCIL = _WGL__init__.LPD_SHARE_STENCIL
LPD_SHARE_ACCUM = _WGL__init__.LPD_SHARE_ACCUM
LPD_SWAP_EXCHANGE = _WGL__init__.LPD_SWAP_EXCHANGE
LPD_SWAP_COPY = _WGL__init__.LPD_SWAP_COPY
LPD_TRANSPARENT = _WGL__init__.LPD_TRANSPARENT
LPD_TYPE_RGBA = _WGL__init__.LPD_TYPE_RGBA
LPD_TYPE_COLORINDEX = _WGL__init__.LPD_TYPE_COLORINDEX
WGL_SWAP_MAIN_PLANE = _WGL__init__.WGL_SWAP_MAIN_PLANE
WGL_SWAP_OVERLAY1 = _WGL__init__.WGL_SWAP_OVERLAY1
WGL_SWAP_OVERLAY2 = _WGL__init__.WGL_SWAP_OVERLAY2
WGL_SWAP_OVERLAY3 = _WGL__init__.WGL_SWAP_OVERLAY3
WGL_SWAP_OVERLAY4 = _WGL__init__.WGL_SWAP_OVERLAY4
WGL_SWAP_OVERLAY5 = _WGL__init__.WGL_SWAP_OVERLAY5
WGL_SWAP_OVERLAY6 = _WGL__init__.WGL_SWAP_OVERLAY6
WGL_SWAP_OVERLAY7 = _WGL__init__.WGL_SWAP_OVERLAY7
WGL_SWAP_OVERLAY8 = _WGL__init__.WGL_SWAP_OVERLAY8
WGL_SWAP_OVERLAY9 = _WGL__init__.WGL_SWAP_OVERLAY9
WGL_SWAP_OVERLAY10 = _WGL__init__.WGL_SWAP_OVERLAY10
WGL_SWAP_OVERLAY11 = _WGL__init__.WGL_SWAP_OVERLAY11
WGL_SWAP_OVERLAY12 = _WGL__init__.WGL_SWAP_OVERLAY12
WGL_SWAP_OVERLAY13 = _WGL__init__.WGL_SWAP_OVERLAY13
WGL_SWAP_OVERLAY14 = _WGL__init__.WGL_SWAP_OVERLAY14
WGL_SWAP_OVERLAY15 = _WGL__init__.WGL_SWAP_OVERLAY15
WGL_SWAP_UNDERLAY1 = _WGL__init__.WGL_SWAP_UNDERLAY1
WGL_SWAP_UNDERLAY2 = _WGL__init__.WGL_SWAP_UNDERLAY2
WGL_SWAP_UNDERLAY3 = _WGL__init__.WGL_SWAP_UNDERLAY3
WGL_SWAP_UNDERLAY4 = _WGL__init__.WGL_SWAP_UNDERLAY4
WGL_SWAP_UNDERLAY5 = _WGL__init__.WGL_SWAP_UNDERLAY5
WGL_SWAP_UNDERLAY6 = _WGL__init__.WGL_SWAP_UNDERLAY6
WGL_SWAP_UNDERLAY7 = _WGL__init__.WGL_SWAP_UNDERLAY7
WGL_SWAP_UNDERLAY8 = _WGL__init__.WGL_SWAP_UNDERLAY8
WGL_SWAP_UNDERLAY9 = _WGL__init__.WGL_SWAP_UNDERLAY9
WGL_SWAP_UNDERLAY10 = _WGL__init__.WGL_SWAP_UNDERLAY10
WGL_SWAP_UNDERLAY11 = _WGL__init__.WGL_SWAP_UNDERLAY11
WGL_SWAP_UNDERLAY12 = _WGL__init__.WGL_SWAP_UNDERLAY12
WGL_SWAP_UNDERLAY13 = _WGL__init__.WGL_SWAP_UNDERLAY13
WGL_SWAP_UNDERLAY14 = _WGL__init__.WGL_SWAP_UNDERLAY14
WGL_SWAP_UNDERLAY15 = _WGL__init__.WGL_SWAP_UNDERLAY15

ChoosePixelFormat = _WGL__init__.ChoosePixelFormat

DescribePixelFormat = _WGL__init__.DescribePixelFormat

GetPixelFormat = _WGL__init__.GetPixelFormat

SetPixelFormat = _WGL__init__.SetPixelFormat

SwapBuffers = _WGL__init__.SwapBuffers

wglCreateContext = _WGL__init__.wglCreateContext

wglCreateLayerContext = _WGL__init__.wglCreateLayerContext

wglCopyContext = _WGL__init__.wglCopyContext

wglDeleteContext = _WGL__init__.wglDeleteContext

wglDescribeLayerPlane = _WGL__init__.wglDescribeLayerPlane

wglGetCurrentContext = _WGL__init__.wglGetCurrentContext

wglGetCurrentDC = _WGL__init__.wglGetCurrentDC

wglGetLayerPaletteEntries = _WGL__init__.wglGetLayerPaletteEntries

wglGetProcAddress = _WGL__init__.wglGetProcAddress

wglMakeCurrent = _WGL__init__.wglMakeCurrent

wglRealizeLayerPalette = _WGL__init__.wglRealizeLayerPalette

wglSetLayerPaletteEntries = _WGL__init__.wglSetLayerPaletteEntries

wglShareLists = _WGL__init__.wglShareLists

wglSwapLayerBuffers = _WGL__init__.wglSwapLayerBuffers

wglUseFontBitmapsA = _WGL__init__.wglUseFontBitmapsA

wglUseFontBitmapsW = _WGL__init__.wglUseFontBitmapsW
wglUseFontBitmaps = _WGL__init__.wglUseFontBitmapsA


wglUseFontOutlinesA = _WGL__init__.wglUseFontOutlinesA

wglUseFontOutlinesW = _WGL__init__.wglUseFontOutlinesW
wglUseFontOutlines = _WGL__init__.wglUseFontOutlinesA

def __info():
	return []

__api_version__ = _WGL__init__.__api_version__
__author__ = _WGL__init__.__author__
__date__ = _WGL__init__.__date__
__doc__ = _WGL__init__.__doc__
__version__ = _WGL__init__.__version__


