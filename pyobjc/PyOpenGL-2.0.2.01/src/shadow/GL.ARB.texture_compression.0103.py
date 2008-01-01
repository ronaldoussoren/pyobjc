# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _texture_compression

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


__version__ = _texture_compression.__version__
__date__ = _texture_compression.__date__
__api_version__ = _texture_compression.__api_version__
__author__ = _texture_compression.__author__

glCompressedTexImage3DARB = _texture_compression.glCompressedTexImage3DARB

glCompressedTexImage2DARB = _texture_compression.glCompressedTexImage2DARB

glCompressedTexImage1DARB = _texture_compression.glCompressedTexImage1DARB

glCompressedTexSubImage3DARB = _texture_compression.glCompressedTexSubImage3DARB

glCompressedTexSubImage2DARB = _texture_compression.glCompressedTexSubImage2DARB

glCompressedTexSubImage1DARB = _texture_compression.glCompressedTexSubImage1DARB

glGetCompressedTexImageARB = _texture_compression.glGetCompressedTexImageARB

glInitTextureCompressionARB = _texture_compression.glInitTextureCompressionARB

glInitTexCompressionARB = _texture_compression.glInitTexCompressionARB

__info = _texture_compression.__info
GL_COMPRESSED_ALPHA_ARB = _texture_compression.GL_COMPRESSED_ALPHA_ARB
GL_COMPRESSED_LUMINANCE_ARB = _texture_compression.GL_COMPRESSED_LUMINANCE_ARB
GL_COMPRESSED_LUMINANCE_ALPHA_ARB = _texture_compression.GL_COMPRESSED_LUMINANCE_ALPHA_ARB
GL_COMPRESSED_INTENSITY_ARB = _texture_compression.GL_COMPRESSED_INTENSITY_ARB
GL_COMPRESSED_RGB_ARB = _texture_compression.GL_COMPRESSED_RGB_ARB
GL_COMPRESSED_RGBA_ARB = _texture_compression.GL_COMPRESSED_RGBA_ARB
GL_TEXTURE_COMPRESSION_HINT_ARB = _texture_compression.GL_TEXTURE_COMPRESSION_HINT_ARB
GL_TEXTURE_COMPRESSED_IMAGE_SIZE_ARB = _texture_compression.GL_TEXTURE_COMPRESSED_IMAGE_SIZE_ARB
GL_TEXTURE_COMPRESSED_ARB = _texture_compression.GL_TEXTURE_COMPRESSED_ARB
GL_NUM_COMPRESSED_TEXTURE_FORMATS_ARB = _texture_compression.GL_NUM_COMPRESSED_TEXTURE_FORMATS_ARB
GL_COMPRESSED_TEXTURE_FORMATS_ARB = _texture_compression.GL_COMPRESSED_TEXTURE_FORMATS_ARB

