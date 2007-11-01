# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _texture4D

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


__version__ = _texture4D.__version__
__date__ = _texture4D.__date__
__api_version__ = _texture4D.__api_version__
__author__ = _texture4D.__author__
__doc__ = _texture4D.__doc__

glInitTexture4DSGIS = _texture4D.glInitTexture4DSGIS

glInitTex4DSGIS = _texture4D.glInitTex4DSGIS

glTexImage4DSGIS = _texture4D.glTexImage4DSGIS

glTexImage4DubSGIS = _texture4D.glTexImage4DubSGIS

glTexImage4DbSGIS = _texture4D.glTexImage4DbSGIS

glTexImage4DusSGIS = _texture4D.glTexImage4DusSGIS

glTexImage4DsSGIS = _texture4D.glTexImage4DsSGIS

glTexImage4DuiSGIS = _texture4D.glTexImage4DuiSGIS

glTexImage4DiSGIS = _texture4D.glTexImage4DiSGIS

glTexImage4DfSGIS = _texture4D.glTexImage4DfSGIS

glTexSubImage4DSGIS = _texture4D.glTexSubImage4DSGIS

glTexSubImage4DubSGIS = _texture4D.glTexSubImage4DubSGIS

glTexSubImage4DbSGIS = _texture4D.glTexSubImage4DbSGIS

glTexSubImage4DusSGIS = _texture4D.glTexSubImage4DusSGIS

glTexSubImage4DsSGIS = _texture4D.glTexSubImage4DsSGIS

glTexSubImage4DuiSGIS = _texture4D.glTexSubImage4DuiSGIS

glTexSubImage4DiSGIS = _texture4D.glTexSubImage4DiSGIS

glTexSubImage4DfSGIS = _texture4D.glTexSubImage4DfSGIS

__info = _texture4D.__info
GL_PACK_SKIP_VOLUMES_SGIS = _texture4D.GL_PACK_SKIP_VOLUMES_SGIS
GL_PACK_IMAGE_DEPTH_SGIS = _texture4D.GL_PACK_IMAGE_DEPTH_SGIS
GL_UNPACK_SKIP_VOLUMES_SGIS = _texture4D.GL_UNPACK_SKIP_VOLUMES_SGIS
GL_UNPACK_IMAGE_DEPTH_SGIS = _texture4D.GL_UNPACK_IMAGE_DEPTH_SGIS
GL_TEXTURE_4D_SGIS = _texture4D.GL_TEXTURE_4D_SGIS
GL_PROXY_TEXTURE_4D_SGIS = _texture4D.GL_PROXY_TEXTURE_4D_SGIS
GL_TEXTURE_4DSIZE_SGIS = _texture4D.GL_TEXTURE_4DSIZE_SGIS
GL_TEXTURE_WRAP_Q_SGIS = _texture4D.GL_TEXTURE_WRAP_Q_SGIS
GL_MAX_4D_TEXTURE_SIZE_SGIS = _texture4D.GL_MAX_4D_TEXTURE_SIZE_SGIS
GL_TEXTURE_4D_BINDING_SGIS = _texture4D.GL_TEXTURE_4D_BINDING_SGIS

