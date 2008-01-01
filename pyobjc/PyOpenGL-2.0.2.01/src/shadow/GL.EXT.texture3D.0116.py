# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _texture3D

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


__version__ = _texture3D.__version__
__date__ = _texture3D.__date__
__api_version__ = _texture3D.__api_version__
__author__ = _texture3D.__author__
__doc__ = _texture3D.__doc__

glTexImage3DEXT = _texture3D.glTexImage3DEXT

glTexImage3DubEXT = _texture3D.glTexImage3DubEXT

glTexImage3DbEXT = _texture3D.glTexImage3DbEXT

glTexImage3DusEXT = _texture3D.glTexImage3DusEXT

glTexImage3DsEXT = _texture3D.glTexImage3DsEXT

glTexImage3DuiEXT = _texture3D.glTexImage3DuiEXT

glTexImage3DiEXT = _texture3D.glTexImage3DiEXT

glTexImage3DfEXT = _texture3D.glTexImage3DfEXT

glInitTexture3DEXT = _texture3D.glInitTexture3DEXT

glInitTex3DEXT = _texture3D.glInitTex3DEXT

__info = _texture3D.__info
GL_PACK_SKIP_IMAGES_EXT = _texture3D.GL_PACK_SKIP_IMAGES_EXT
GL_PACK_IMAGE_HEIGHT_EXT = _texture3D.GL_PACK_IMAGE_HEIGHT_EXT
GL_UNPACK_SKIP_IMAGES_EXT = _texture3D.GL_UNPACK_SKIP_IMAGES_EXT
GL_UNPACK_IMAGE_HEIGHT_EXT = _texture3D.GL_UNPACK_IMAGE_HEIGHT_EXT
GL_TEXTURE_3D_EXT = _texture3D.GL_TEXTURE_3D_EXT
GL_PROXY_TEXTURE_3D_EXT = _texture3D.GL_PROXY_TEXTURE_3D_EXT
GL_TEXTURE_DEPTH_EXT = _texture3D.GL_TEXTURE_DEPTH_EXT
GL_TEXTURE_WRAP_R_EXT = _texture3D.GL_TEXTURE_WRAP_R_EXT
GL_MAX_3D_TEXTURE_SIZE_EXT = _texture3D.GL_MAX_3D_TEXTURE_SIZE_EXT

