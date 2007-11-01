# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _vertex_streams

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


__version__ = _vertex_streams.__version__
__date__ = _vertex_streams.__date__
__api_version__ = _vertex_streams.__api_version__
__author__ = _vertex_streams.__author__
__doc__ = _vertex_streams.__doc__

glVertexStream1sATI = _vertex_streams.glVertexStream1sATI

glVertexStream1svATI = _vertex_streams.glVertexStream1svATI

glVertexStream1iATI = _vertex_streams.glVertexStream1iATI

glVertexStream1ivATI = _vertex_streams.glVertexStream1ivATI

glVertexStream1fATI = _vertex_streams.glVertexStream1fATI

glVertexStream1fvATI = _vertex_streams.glVertexStream1fvATI

glVertexStream1dATI = _vertex_streams.glVertexStream1dATI

glVertexStream1dvATI = _vertex_streams.glVertexStream1dvATI

glVertexStream2sATI = _vertex_streams.glVertexStream2sATI

glVertexStream2svATI = _vertex_streams.glVertexStream2svATI

glVertexStream2iATI = _vertex_streams.glVertexStream2iATI

glVertexStream2ivATI = _vertex_streams.glVertexStream2ivATI

glVertexStream2fATI = _vertex_streams.glVertexStream2fATI

glVertexStream2fvATI = _vertex_streams.glVertexStream2fvATI

glVertexStream2dATI = _vertex_streams.glVertexStream2dATI

glVertexStream2dvATI = _vertex_streams.glVertexStream2dvATI

glVertexStream3sATI = _vertex_streams.glVertexStream3sATI

glVertexStream3svATI = _vertex_streams.glVertexStream3svATI

glVertexStream3iATI = _vertex_streams.glVertexStream3iATI

glVertexStream3ivATI = _vertex_streams.glVertexStream3ivATI

glVertexStream3fATI = _vertex_streams.glVertexStream3fATI

glVertexStream3fvATI = _vertex_streams.glVertexStream3fvATI

glVertexStream3dATI = _vertex_streams.glVertexStream3dATI

glVertexStream3dvATI = _vertex_streams.glVertexStream3dvATI

glVertexStream4sATI = _vertex_streams.glVertexStream4sATI

glVertexStream4svATI = _vertex_streams.glVertexStream4svATI

glVertexStream4iATI = _vertex_streams.glVertexStream4iATI

glVertexStream4ivATI = _vertex_streams.glVertexStream4ivATI

glVertexStream4fATI = _vertex_streams.glVertexStream4fATI

glVertexStream4fvATI = _vertex_streams.glVertexStream4fvATI

glVertexStream4dATI = _vertex_streams.glVertexStream4dATI

glVertexStream4dvATI = _vertex_streams.glVertexStream4dvATI

glNormalStream3bATI = _vertex_streams.glNormalStream3bATI

glNormalStream3bvATI = _vertex_streams.glNormalStream3bvATI

glNormalStream3sATI = _vertex_streams.glNormalStream3sATI

glNormalStream3svATI = _vertex_streams.glNormalStream3svATI

glNormalStream3iATI = _vertex_streams.glNormalStream3iATI

glNormalStream3ivATI = _vertex_streams.glNormalStream3ivATI

glNormalStream3fATI = _vertex_streams.glNormalStream3fATI

glNormalStream3fvATI = _vertex_streams.glNormalStream3fvATI

glNormalStream3dATI = _vertex_streams.glNormalStream3dATI

glNormalStream3dvATI = _vertex_streams.glNormalStream3dvATI

glClientActiveVertexStreamATI = _vertex_streams.glClientActiveVertexStreamATI

glVertexBlendEnviATI = _vertex_streams.glVertexBlendEnviATI

glVertexBlendEnvfATI = _vertex_streams.glVertexBlendEnvfATI
GL_MAX_VERTEX_STREAMS_ATI = _vertex_streams.GL_MAX_VERTEX_STREAMS_ATI
GL_VERTEX_STREAM0_ATI = _vertex_streams.GL_VERTEX_STREAM0_ATI
GL_VERTEX_STREAM1_ATI = _vertex_streams.GL_VERTEX_STREAM1_ATI
GL_VERTEX_STREAM2_ATI = _vertex_streams.GL_VERTEX_STREAM2_ATI
GL_VERTEX_STREAM3_ATI = _vertex_streams.GL_VERTEX_STREAM3_ATI
GL_VERTEX_STREAM4_ATI = _vertex_streams.GL_VERTEX_STREAM4_ATI
GL_VERTEX_STREAM5_ATI = _vertex_streams.GL_VERTEX_STREAM5_ATI
GL_VERTEX_STREAM6_ATI = _vertex_streams.GL_VERTEX_STREAM6_ATI
GL_VERTEX_STREAM7_ATI = _vertex_streams.GL_VERTEX_STREAM7_ATI
GL_VERTEX_SOURCE_ATI = _vertex_streams.GL_VERTEX_SOURCE_ATI

glInitVertexStreamsATI = _vertex_streams.glInitVertexStreamsATI

__info = _vertex_streams.__info

