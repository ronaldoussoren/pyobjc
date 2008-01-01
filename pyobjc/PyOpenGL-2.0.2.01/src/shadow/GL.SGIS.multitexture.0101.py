# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _multitexture

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


__version__ = _multitexture.__version__
__date__ = _multitexture.__date__
__api_version__ = _multitexture.__api_version__
__author__ = _multitexture.__author__
__doc__ = _multitexture.__doc__
GL_TEXTURE0_SGIS = _multitexture.GL_TEXTURE0_SGIS
GL_TEXTURE1_SGIS = _multitexture.GL_TEXTURE1_SGIS
GL_TEXTURE2_SGIS = _multitexture.GL_TEXTURE2_SGIS
GL_TEXTURE3_SGIS = _multitexture.GL_TEXTURE3_SGIS
GL_TEXTURE4_SGIS = _multitexture.GL_TEXTURE4_SGIS
GL_TEXTURE5_SGIS = _multitexture.GL_TEXTURE5_SGIS
GL_TEXTURE6_SGIS = _multitexture.GL_TEXTURE6_SGIS
GL_TEXTURE7_SGIS = _multitexture.GL_TEXTURE7_SGIS
GL_TEXTURE8_SGIS = _multitexture.GL_TEXTURE8_SGIS
GL_TEXTURE9_SGIS = _multitexture.GL_TEXTURE9_SGIS
GL_TEXTURE10_SGIS = _multitexture.GL_TEXTURE10_SGIS
GL_TEXTURE11_SGIS = _multitexture.GL_TEXTURE11_SGIS
GL_TEXTURE12_SGIS = _multitexture.GL_TEXTURE12_SGIS
GL_TEXTURE13_SGIS = _multitexture.GL_TEXTURE13_SGIS
GL_TEXTURE14_SGIS = _multitexture.GL_TEXTURE14_SGIS
GL_TEXTURE15_SGIS = _multitexture.GL_TEXTURE15_SGIS
GL_TEXTURE16_SGIS = _multitexture.GL_TEXTURE16_SGIS
GL_TEXTURE17_SGIS = _multitexture.GL_TEXTURE17_SGIS
GL_TEXTURE18_SGIS = _multitexture.GL_TEXTURE18_SGIS
GL_TEXTURE19_SGIS = _multitexture.GL_TEXTURE19_SGIS
GL_TEXTURE20_SGIS = _multitexture.GL_TEXTURE20_SGIS
GL_TEXTURE21_SGIS = _multitexture.GL_TEXTURE21_SGIS
GL_TEXTURE22_SGIS = _multitexture.GL_TEXTURE22_SGIS
GL_TEXTURE23_SGIS = _multitexture.GL_TEXTURE23_SGIS
GL_TEXTURE24_SGIS = _multitexture.GL_TEXTURE24_SGIS
GL_TEXTURE25_SGIS = _multitexture.GL_TEXTURE25_SGIS
GL_TEXTURE26_SGIS = _multitexture.GL_TEXTURE26_SGIS
GL_TEXTURE27_SGIS = _multitexture.GL_TEXTURE27_SGIS
GL_TEXTURE28_SGIS = _multitexture.GL_TEXTURE28_SGIS
GL_TEXTURE29_SGIS = _multitexture.GL_TEXTURE29_SGIS
GL_TEXTURE30_SGIS = _multitexture.GL_TEXTURE30_SGIS
GL_TEXTURE31_SGIS = _multitexture.GL_TEXTURE31_SGIS
GL_SELECTED_TEXTURE_SGIS = _multitexture.GL_SELECTED_TEXTURE_SGIS
GL_SELECTED_TEXTURE_COORD_SET_SGIS = _multitexture.GL_SELECTED_TEXTURE_COORD_SET_SGIS
GL_MAX_TEXTURES_SGIS = _multitexture.GL_MAX_TEXTURES_SGIS
GL_TEXTURE_COORD_SET_SOURCE_SGIS = _multitexture.GL_TEXTURE_COORD_SET_SOURCE_SGIS

glInitMultitextureSGIS = _multitexture.glInitMultitextureSGIS

glInitMultiTexSGIS = _multitexture.glInitMultiTexSGIS

glMultiTexCoord1dSGIS = _multitexture.glMultiTexCoord1dSGIS

glMultiTexCoord1dvSGIS = _multitexture.glMultiTexCoord1dvSGIS

glMultiTexCoord1fSGIS = _multitexture.glMultiTexCoord1fSGIS

glMultiTexCoord1fvSGIS = _multitexture.glMultiTexCoord1fvSGIS

glMultiTexCoord1iSGIS = _multitexture.glMultiTexCoord1iSGIS

glMultiTexCoord1ivSGIS = _multitexture.glMultiTexCoord1ivSGIS

glMultiTexCoord1sSGIS = _multitexture.glMultiTexCoord1sSGIS

glMultiTexCoord1svSGIS = _multitexture.glMultiTexCoord1svSGIS

glMultiTexCoord2dSGIS = _multitexture.glMultiTexCoord2dSGIS

glMultiTexCoord2dvSGIS = _multitexture.glMultiTexCoord2dvSGIS

glMultiTexCoord2fSGIS = _multitexture.glMultiTexCoord2fSGIS

glMultiTexCoord2fvSGIS = _multitexture.glMultiTexCoord2fvSGIS

glMultiTexCoord2iSGIS = _multitexture.glMultiTexCoord2iSGIS

glMultiTexCoord2ivSGIS = _multitexture.glMultiTexCoord2ivSGIS

glMultiTexCoord2sSGIS = _multitexture.glMultiTexCoord2sSGIS

glMultiTexCoord2svSGIS = _multitexture.glMultiTexCoord2svSGIS

glMultiTexCoord3dSGIS = _multitexture.glMultiTexCoord3dSGIS

glMultiTexCoord3dvSGIS = _multitexture.glMultiTexCoord3dvSGIS

glMultiTexCoord3fSGIS = _multitexture.glMultiTexCoord3fSGIS

glMultiTexCoord3fvSGIS = _multitexture.glMultiTexCoord3fvSGIS

glMultiTexCoord3iSGIS = _multitexture.glMultiTexCoord3iSGIS

glMultiTexCoord3ivSGIS = _multitexture.glMultiTexCoord3ivSGIS

glMultiTexCoord3sSGIS = _multitexture.glMultiTexCoord3sSGIS

glMultiTexCoord3svSGIS = _multitexture.glMultiTexCoord3svSGIS

glMultiTexCoord4dSGIS = _multitexture.glMultiTexCoord4dSGIS

glMultiTexCoord4dvSGIS = _multitexture.glMultiTexCoord4dvSGIS

glMultiTexCoord4fSGIS = _multitexture.glMultiTexCoord4fSGIS

glMultiTexCoord4fvSGIS = _multitexture.glMultiTexCoord4fvSGIS

glMultiTexCoord4iSGIS = _multitexture.glMultiTexCoord4iSGIS

glMultiTexCoord4ivSGIS = _multitexture.glMultiTexCoord4ivSGIS

glMultiTexCoord4sSGIS = _multitexture.glMultiTexCoord4sSGIS

glMultiTexCoord4svSGIS = _multitexture.glMultiTexCoord4svSGIS

glSelectTextureSGIS = _multitexture.glSelectTextureSGIS

glSelectTextureCoordSetSGIS = _multitexture.glSelectTextureCoordSetSGIS

__info = _multitexture.__info

