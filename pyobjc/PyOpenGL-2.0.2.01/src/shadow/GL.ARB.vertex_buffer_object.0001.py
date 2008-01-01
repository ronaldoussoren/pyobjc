# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _vertex_buffer_object

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


__version__ = _vertex_buffer_object.__version__
__date__ = _vertex_buffer_object.__date__
__api_version__ = _vertex_buffer_object.__api_version__
__author__ = _vertex_buffer_object.__author__
__doc__ = _vertex_buffer_object.__doc__

glBindBufferARB = _vertex_buffer_object.glBindBufferARB

glDeleteBuffersARB = _vertex_buffer_object.glDeleteBuffersARB

glGenBuffersARB = _vertex_buffer_object.glGenBuffersARB

glIsBufferARB = _vertex_buffer_object.glIsBufferARB

glBufferDataARB = _vertex_buffer_object.glBufferDataARB

glBufferSubDataARB = _vertex_buffer_object.glBufferSubDataARB

glGetBufferSubDataARB = _vertex_buffer_object.glGetBufferSubDataARB

glMapBufferARB = _vertex_buffer_object.glMapBufferARB

glUnmapBufferARB = _vertex_buffer_object.glUnmapBufferARB

glGetBufferParameterivARB = _vertex_buffer_object.glGetBufferParameterivARB

glGetBufferPointervARB = _vertex_buffer_object.glGetBufferPointervARB
GL_BUFFER_SIZE_ARB = _vertex_buffer_object.GL_BUFFER_SIZE_ARB
GL_BUFFER_USAGE_ARB = _vertex_buffer_object.GL_BUFFER_USAGE_ARB
GL_ARRAY_BUFFER_ARB = _vertex_buffer_object.GL_ARRAY_BUFFER_ARB
GL_ELEMENT_ARRAY_BUFFER_ARB = _vertex_buffer_object.GL_ELEMENT_ARRAY_BUFFER_ARB
GL_ARRAY_BUFFER_BINDING_ARB = _vertex_buffer_object.GL_ARRAY_BUFFER_BINDING_ARB
GL_ELEMENT_ARRAY_BUFFER_BINDING_ARB = _vertex_buffer_object.GL_ELEMENT_ARRAY_BUFFER_BINDING_ARB
GL_VERTEX_ARRAY_BUFFER_BINDING_ARB = _vertex_buffer_object.GL_VERTEX_ARRAY_BUFFER_BINDING_ARB
GL_NORMAL_ARRAY_BUFFER_BINDING_ARB = _vertex_buffer_object.GL_NORMAL_ARRAY_BUFFER_BINDING_ARB
GL_COLOR_ARRAY_BUFFER_BINDING_ARB = _vertex_buffer_object.GL_COLOR_ARRAY_BUFFER_BINDING_ARB
GL_INDEX_ARRAY_BUFFER_BINDING_ARB = _vertex_buffer_object.GL_INDEX_ARRAY_BUFFER_BINDING_ARB
GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING_ARB = _vertex_buffer_object.GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING_ARB
GL_EDGE_FLAG_ARRAY_BUFFER_BINDING_ARB = _vertex_buffer_object.GL_EDGE_FLAG_ARRAY_BUFFER_BINDING_ARB
GL_SECONDARY_COLOR_ARRAY_BUFFER_BINDING_ARB = _vertex_buffer_object.GL_SECONDARY_COLOR_ARRAY_BUFFER_BINDING_ARB
GL_FOG_COORDINATE_ARRAY_BUFFER_BINDING_ARB = _vertex_buffer_object.GL_FOG_COORDINATE_ARRAY_BUFFER_BINDING_ARB
GL_WEIGHT_ARRAY_BUFFER_BINDING_ARB = _vertex_buffer_object.GL_WEIGHT_ARRAY_BUFFER_BINDING_ARB
GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING_ARB = _vertex_buffer_object.GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING_ARB
GL_READ_ONLY_ARB = _vertex_buffer_object.GL_READ_ONLY_ARB
GL_WRITE_ONLY_ARB = _vertex_buffer_object.GL_WRITE_ONLY_ARB
GL_READ_WRITE_ARB = _vertex_buffer_object.GL_READ_WRITE_ARB
GL_BUFFER_ACCESS_ARB = _vertex_buffer_object.GL_BUFFER_ACCESS_ARB
GL_BUFFER_MAPPED_ARB = _vertex_buffer_object.GL_BUFFER_MAPPED_ARB
GL_BUFFER_MAP_POINTER_ARB = _vertex_buffer_object.GL_BUFFER_MAP_POINTER_ARB
GL_STREAM_DRAW_ARB = _vertex_buffer_object.GL_STREAM_DRAW_ARB
GL_STREAM_READ_ARB = _vertex_buffer_object.GL_STREAM_READ_ARB
GL_STREAM_COPY_ARB = _vertex_buffer_object.GL_STREAM_COPY_ARB
GL_STATIC_DRAW_ARB = _vertex_buffer_object.GL_STATIC_DRAW_ARB
GL_STATIC_READ_ARB = _vertex_buffer_object.GL_STATIC_READ_ARB
GL_STATIC_COPY_ARB = _vertex_buffer_object.GL_STATIC_COPY_ARB
GL_DYNAMIC_DRAW_ARB = _vertex_buffer_object.GL_DYNAMIC_DRAW_ARB
GL_DYNAMIC_READ_ARB = _vertex_buffer_object.GL_DYNAMIC_READ_ARB
GL_DYNAMIC_COPY_ARB = _vertex_buffer_object.GL_DYNAMIC_COPY_ARB

glInitVertexBufferObjectARB = _vertex_buffer_object.glInitVertexBufferObjectARB

__info = _vertex_buffer_object.__info

