# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _shader_objects

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


__version__ = _shader_objects.__version__
__date__ = _shader_objects.__date__
__api_version__ = _shader_objects.__api_version__
__author__ = _shader_objects.__author__
__doc__ = _shader_objects.__doc__

glDeleteObjectARB = _shader_objects.glDeleteObjectARB

glGetHandleARB = _shader_objects.glGetHandleARB

glDetachObjectARB = _shader_objects.glDetachObjectARB

glCreateShaderObjectARB = _shader_objects.glCreateShaderObjectARB

glShaderSourceARB = _shader_objects.glShaderSourceARB

glCompileShaderARB = _shader_objects.glCompileShaderARB

glCreateProgramObjectARB = _shader_objects.glCreateProgramObjectARB

glAttachObjectARB = _shader_objects.glAttachObjectARB

glLinkProgramARB = _shader_objects.glLinkProgramARB

glUseProgramObjectARB = _shader_objects.glUseProgramObjectARB

glValidateProgramARB = _shader_objects.glValidateProgramARB

glUniform1fARB = _shader_objects.glUniform1fARB

glUniform2fARB = _shader_objects.glUniform2fARB

glUniform3fARB = _shader_objects.glUniform3fARB

glUniform4fARB = _shader_objects.glUniform4fARB

glUniform1iARB = _shader_objects.glUniform1iARB

glUniform2iARB = _shader_objects.glUniform2iARB

glUniform3iARB = _shader_objects.glUniform3iARB

glUniform4iARB = _shader_objects.glUniform4iARB

glUniform1fvARB = _shader_objects.glUniform1fvARB

glUniform2fvARB = _shader_objects.glUniform2fvARB

glUniform3fvARB = _shader_objects.glUniform3fvARB

glUniform4fvARB = _shader_objects.glUniform4fvARB

glUniform1ivARB = _shader_objects.glUniform1ivARB

glUniform2ivARB = _shader_objects.glUniform2ivARB

glUniform3ivARB = _shader_objects.glUniform3ivARB

glUniform4ivARB = _shader_objects.glUniform4ivARB

glUniformMatrix2fvARB = _shader_objects.glUniformMatrix2fvARB

glUniformMatrix3fvARB = _shader_objects.glUniformMatrix3fvARB

glUniformMatrix4fvARB = _shader_objects.glUniformMatrix4fvARB

glGetObjectParameterfvARB = _shader_objects.glGetObjectParameterfvARB

glGetObjectParameterivARB = _shader_objects.glGetObjectParameterivARB

glGetInfoLogARB = _shader_objects.glGetInfoLogARB

glGetAttachedObjectsARB = _shader_objects.glGetAttachedObjectsARB

glGetUniformLocationARB = _shader_objects.glGetUniformLocationARB

glGetActiveUniformARB = _shader_objects.glGetActiveUniformARB

glGetUniformfvARB = _shader_objects.glGetUniformfvARB

glGetUniformivARB = _shader_objects.glGetUniformivARB

glGetShaderSourceARB = _shader_objects.glGetShaderSourceARB
GL_PROGRAM_OBJECT_ARB = _shader_objects.GL_PROGRAM_OBJECT_ARB
GL_SHADER_OBJECT_ARB = _shader_objects.GL_SHADER_OBJECT_ARB
GL_OBJECT_TYPE_ARB = _shader_objects.GL_OBJECT_TYPE_ARB
GL_OBJECT_SUBTYPE_ARB = _shader_objects.GL_OBJECT_SUBTYPE_ARB
GL_FLOAT_VEC2_ARB = _shader_objects.GL_FLOAT_VEC2_ARB
GL_FLOAT_VEC3_ARB = _shader_objects.GL_FLOAT_VEC3_ARB
GL_FLOAT_VEC4_ARB = _shader_objects.GL_FLOAT_VEC4_ARB
GL_INT_VEC2_ARB = _shader_objects.GL_INT_VEC2_ARB
GL_INT_VEC3_ARB = _shader_objects.GL_INT_VEC3_ARB
GL_INT_VEC4_ARB = _shader_objects.GL_INT_VEC4_ARB
GL_BOOL_ARB = _shader_objects.GL_BOOL_ARB
GL_BOOL_VEC2_ARB = _shader_objects.GL_BOOL_VEC2_ARB
GL_BOOL_VEC3_ARB = _shader_objects.GL_BOOL_VEC3_ARB
GL_BOOL_VEC4_ARB = _shader_objects.GL_BOOL_VEC4_ARB
GL_FLOAT_MAT2_ARB = _shader_objects.GL_FLOAT_MAT2_ARB
GL_FLOAT_MAT3_ARB = _shader_objects.GL_FLOAT_MAT3_ARB
GL_FLOAT_MAT4_ARB = _shader_objects.GL_FLOAT_MAT4_ARB
GL_SAMPLER_1D_ARB = _shader_objects.GL_SAMPLER_1D_ARB
GL_SAMPLER_2D_ARB = _shader_objects.GL_SAMPLER_2D_ARB
GL_SAMPLER_3D_ARB = _shader_objects.GL_SAMPLER_3D_ARB
GL_SAMPLER_CUBE_ARB = _shader_objects.GL_SAMPLER_CUBE_ARB
GL_SAMPLER_1D_SHADOW_ARB = _shader_objects.GL_SAMPLER_1D_SHADOW_ARB
GL_SAMPLER_2D_SHADOW_ARB = _shader_objects.GL_SAMPLER_2D_SHADOW_ARB
GL_SAMPLER_2D_RECT_ARB = _shader_objects.GL_SAMPLER_2D_RECT_ARB
GL_SAMPLER_2D_RECT_SHADOW_ARB = _shader_objects.GL_SAMPLER_2D_RECT_SHADOW_ARB
GL_OBJECT_DELETE_STATUS_ARB = _shader_objects.GL_OBJECT_DELETE_STATUS_ARB
GL_OBJECT_COMPILE_STATUS_ARB = _shader_objects.GL_OBJECT_COMPILE_STATUS_ARB
GL_OBJECT_LINK_STATUS_ARB = _shader_objects.GL_OBJECT_LINK_STATUS_ARB
GL_OBJECT_VALIDATE_STATUS_ARB = _shader_objects.GL_OBJECT_VALIDATE_STATUS_ARB
GL_OBJECT_INFO_LOG_LENGTH_ARB = _shader_objects.GL_OBJECT_INFO_LOG_LENGTH_ARB
GL_OBJECT_ATTACHED_OBJECTS_ARB = _shader_objects.GL_OBJECT_ATTACHED_OBJECTS_ARB
GL_OBJECT_ACTIVE_UNIFORMS_ARB = _shader_objects.GL_OBJECT_ACTIVE_UNIFORMS_ARB
GL_OBJECT_ACTIVE_UNIFORM_MAX_LENGTH_ARB = _shader_objects.GL_OBJECT_ACTIVE_UNIFORM_MAX_LENGTH_ARB
GL_OBJECT_SHADER_SOURCE_LENGTH_ARB = _shader_objects.GL_OBJECT_SHADER_SOURCE_LENGTH_ARB

glInitShaderObjectsARB = _shader_objects.glInitShaderObjectsARB

__info = _shader_objects.__info

