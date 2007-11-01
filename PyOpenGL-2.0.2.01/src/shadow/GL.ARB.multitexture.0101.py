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

glMultiTexCoord1dARB = _multitexture.glMultiTexCoord1dARB

glMultiTexCoord1dvARB = _multitexture.glMultiTexCoord1dvARB

glMultiTexCoord1fARB = _multitexture.glMultiTexCoord1fARB

glMultiTexCoord1fvARB = _multitexture.glMultiTexCoord1fvARB

glMultiTexCoord1iARB = _multitexture.glMultiTexCoord1iARB

glMultiTexCoord1ivARB = _multitexture.glMultiTexCoord1ivARB

glMultiTexCoord1sARB = _multitexture.glMultiTexCoord1sARB

glMultiTexCoord1svARB = _multitexture.glMultiTexCoord1svARB

glMultiTexCoord2dARB = _multitexture.glMultiTexCoord2dARB

glMultiTexCoord2dvARB = _multitexture.glMultiTexCoord2dvARB

glMultiTexCoord2fARB = _multitexture.glMultiTexCoord2fARB

glMultiTexCoord2fvARB = _multitexture.glMultiTexCoord2fvARB

glMultiTexCoord2iARB = _multitexture.glMultiTexCoord2iARB

glMultiTexCoord2ivARB = _multitexture.glMultiTexCoord2ivARB

glMultiTexCoord2sARB = _multitexture.glMultiTexCoord2sARB

glMultiTexCoord2svARB = _multitexture.glMultiTexCoord2svARB

glMultiTexCoord3dARB = _multitexture.glMultiTexCoord3dARB

glMultiTexCoord3dvARB = _multitexture.glMultiTexCoord3dvARB

glMultiTexCoord3fARB = _multitexture.glMultiTexCoord3fARB

glMultiTexCoord3fvARB = _multitexture.glMultiTexCoord3fvARB

glMultiTexCoord3iARB = _multitexture.glMultiTexCoord3iARB

glMultiTexCoord3ivARB = _multitexture.glMultiTexCoord3ivARB

glMultiTexCoord3sARB = _multitexture.glMultiTexCoord3sARB

glMultiTexCoord3svARB = _multitexture.glMultiTexCoord3svARB

glMultiTexCoord4dARB = _multitexture.glMultiTexCoord4dARB

glMultiTexCoord4dvARB = _multitexture.glMultiTexCoord4dvARB

glMultiTexCoord4fARB = _multitexture.glMultiTexCoord4fARB

glMultiTexCoord4fvARB = _multitexture.glMultiTexCoord4fvARB

glMultiTexCoord4iARB = _multitexture.glMultiTexCoord4iARB

glMultiTexCoord4ivARB = _multitexture.glMultiTexCoord4ivARB

glMultiTexCoord4sARB = _multitexture.glMultiTexCoord4sARB

glMultiTexCoord4svARB = _multitexture.glMultiTexCoord4svARB

glActiveTextureARB = _multitexture.glActiveTextureARB

glClientActiveTextureARB = _multitexture.glClientActiveTextureARB

glInitMultitextureARB = _multitexture.glInitMultitextureARB

glInitMultiTexARB = _multitexture.glInitMultiTexARB

__info = _multitexture.__info
GL_TEXTURE0_ARB = _multitexture.GL_TEXTURE0_ARB
GL_TEXTURE1_ARB = _multitexture.GL_TEXTURE1_ARB
GL_TEXTURE2_ARB = _multitexture.GL_TEXTURE2_ARB
GL_TEXTURE3_ARB = _multitexture.GL_TEXTURE3_ARB
GL_TEXTURE4_ARB = _multitexture.GL_TEXTURE4_ARB
GL_TEXTURE5_ARB = _multitexture.GL_TEXTURE5_ARB
GL_TEXTURE6_ARB = _multitexture.GL_TEXTURE6_ARB
GL_TEXTURE7_ARB = _multitexture.GL_TEXTURE7_ARB
GL_TEXTURE8_ARB = _multitexture.GL_TEXTURE8_ARB
GL_TEXTURE9_ARB = _multitexture.GL_TEXTURE9_ARB
GL_TEXTURE10_ARB = _multitexture.GL_TEXTURE10_ARB
GL_TEXTURE11_ARB = _multitexture.GL_TEXTURE11_ARB
GL_TEXTURE12_ARB = _multitexture.GL_TEXTURE12_ARB
GL_TEXTURE13_ARB = _multitexture.GL_TEXTURE13_ARB
GL_TEXTURE14_ARB = _multitexture.GL_TEXTURE14_ARB
GL_TEXTURE15_ARB = _multitexture.GL_TEXTURE15_ARB
GL_TEXTURE16_ARB = _multitexture.GL_TEXTURE16_ARB
GL_TEXTURE17_ARB = _multitexture.GL_TEXTURE17_ARB
GL_TEXTURE18_ARB = _multitexture.GL_TEXTURE18_ARB
GL_TEXTURE19_ARB = _multitexture.GL_TEXTURE19_ARB
GL_TEXTURE20_ARB = _multitexture.GL_TEXTURE20_ARB
GL_TEXTURE21_ARB = _multitexture.GL_TEXTURE21_ARB
GL_TEXTURE22_ARB = _multitexture.GL_TEXTURE22_ARB
GL_TEXTURE23_ARB = _multitexture.GL_TEXTURE23_ARB
GL_TEXTURE24_ARB = _multitexture.GL_TEXTURE24_ARB
GL_TEXTURE25_ARB = _multitexture.GL_TEXTURE25_ARB
GL_TEXTURE26_ARB = _multitexture.GL_TEXTURE26_ARB
GL_TEXTURE27_ARB = _multitexture.GL_TEXTURE27_ARB
GL_TEXTURE28_ARB = _multitexture.GL_TEXTURE28_ARB
GL_TEXTURE29_ARB = _multitexture.GL_TEXTURE29_ARB
GL_TEXTURE30_ARB = _multitexture.GL_TEXTURE30_ARB
GL_TEXTURE31_ARB = _multitexture.GL_TEXTURE31_ARB
GL_ACTIVE_TEXTURE_ARB = _multitexture.GL_ACTIVE_TEXTURE_ARB
GL_CLIENT_ACTIVE_TEXTURE_ARB = _multitexture.GL_CLIENT_ACTIVE_TEXTURE_ARB
GL_MAX_TEXTURE_UNITS_ARB = _multitexture.GL_MAX_TEXTURE_UNITS_ARB

