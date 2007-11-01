# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _vertex_program

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


__version__ = _vertex_program.__version__
__date__ = _vertex_program.__date__
__api_version__ = _vertex_program.__api_version__
__author__ = _vertex_program.__author__
__doc__ = _vertex_program.__doc__

glAreProgramsResidentNV = _vertex_program.glAreProgramsResidentNV

glBindProgramNV = _vertex_program.glBindProgramNV

glDeleteProgramsNV = _vertex_program.glDeleteProgramsNV

glExecuteProgramNV = _vertex_program.glExecuteProgramNV

glGenProgramsNV = _vertex_program.glGenProgramsNV

glGetProgramParameterdvNV = _vertex_program.glGetProgramParameterdvNV

glGetProgramParameterfvNV = _vertex_program.glGetProgramParameterfvNV

glGetProgramivNV = _vertex_program.glGetProgramivNV

glGetProgramStringNV = _vertex_program.glGetProgramStringNV

glGetTrackMatrixivNV = _vertex_program.glGetTrackMatrixivNV

glGetVertexAttribdvNV = _vertex_program.glGetVertexAttribdvNV

glGetVertexAttribfvNV = _vertex_program.glGetVertexAttribfvNV

glGetVertexAttribivNV = _vertex_program.glGetVertexAttribivNV

glGetVertexAttribPointervNV = _vertex_program.glGetVertexAttribPointervNV

glIsProgramNV = _vertex_program.glIsProgramNV

glLoadProgramNV = _vertex_program.glLoadProgramNV

glProgramParameter4dNV = _vertex_program.glProgramParameter4dNV

glProgramParameter4dvNV = _vertex_program.glProgramParameter4dvNV

glProgramParameter4fNV = _vertex_program.glProgramParameter4fNV

glProgramParameter4fvNV = _vertex_program.glProgramParameter4fvNV

glProgramParameters4dvNV = _vertex_program.glProgramParameters4dvNV

glProgramParameters4fvNV = _vertex_program.glProgramParameters4fvNV

glRequestResidentProgramsNV = _vertex_program.glRequestResidentProgramsNV

glTrackMatrixNV = _vertex_program.glTrackMatrixNV

glVertexAttribPointerNV = _vertex_program.glVertexAttribPointerNV

glVertexAttrib1dNV = _vertex_program.glVertexAttrib1dNV

glVertexAttrib1dvNV = _vertex_program.glVertexAttrib1dvNV

glVertexAttrib1fNV = _vertex_program.glVertexAttrib1fNV

glVertexAttrib1fvNV = _vertex_program.glVertexAttrib1fvNV

glVertexAttrib1sNV = _vertex_program.glVertexAttrib1sNV

glVertexAttrib1svNV = _vertex_program.glVertexAttrib1svNV

glVertexAttrib2dNV = _vertex_program.glVertexAttrib2dNV

glVertexAttrib2dvNV = _vertex_program.glVertexAttrib2dvNV

glVertexAttrib2fNV = _vertex_program.glVertexAttrib2fNV

glVertexAttrib2fvNV = _vertex_program.glVertexAttrib2fvNV

glVertexAttrib2sNV = _vertex_program.glVertexAttrib2sNV

glVertexAttrib2svNV = _vertex_program.glVertexAttrib2svNV

glVertexAttrib3dNV = _vertex_program.glVertexAttrib3dNV

glVertexAttrib3dvNV = _vertex_program.glVertexAttrib3dvNV

glVertexAttrib3fNV = _vertex_program.glVertexAttrib3fNV

glVertexAttrib3fvNV = _vertex_program.glVertexAttrib3fvNV

glVertexAttrib3sNV = _vertex_program.glVertexAttrib3sNV

glVertexAttrib3svNV = _vertex_program.glVertexAttrib3svNV

glVertexAttrib4dNV = _vertex_program.glVertexAttrib4dNV

glVertexAttrib4dvNV = _vertex_program.glVertexAttrib4dvNV

glVertexAttrib4fNV = _vertex_program.glVertexAttrib4fNV

glVertexAttrib4fvNV = _vertex_program.glVertexAttrib4fvNV

glVertexAttrib4sNV = _vertex_program.glVertexAttrib4sNV

glVertexAttrib4svNV = _vertex_program.glVertexAttrib4svNV

glVertexAttrib4ubNV = _vertex_program.glVertexAttrib4ubNV

glVertexAttrib4ubvNV = _vertex_program.glVertexAttrib4ubvNV

glVertexAttribs1dvNV = _vertex_program.glVertexAttribs1dvNV

glVertexAttribs1fvNV = _vertex_program.glVertexAttribs1fvNV

glVertexAttribs1svNV = _vertex_program.glVertexAttribs1svNV

glVertexAttribs2dvNV = _vertex_program.glVertexAttribs2dvNV

glVertexAttribs2fvNV = _vertex_program.glVertexAttribs2fvNV

glVertexAttribs2svNV = _vertex_program.glVertexAttribs2svNV

glVertexAttribs3dvNV = _vertex_program.glVertexAttribs3dvNV

glVertexAttribs3fvNV = _vertex_program.glVertexAttribs3fvNV

glVertexAttribs3svNV = _vertex_program.glVertexAttribs3svNV

glVertexAttribs4dvNV = _vertex_program.glVertexAttribs4dvNV

glVertexAttribs4fvNV = _vertex_program.glVertexAttribs4fvNV

glVertexAttribs4svNV = _vertex_program.glVertexAttribs4svNV

glVertexAttribs4ubvNV = _vertex_program.glVertexAttribs4ubvNV
GL_VERTEX_PROGRAM_NV = _vertex_program.GL_VERTEX_PROGRAM_NV
GL_VERTEX_STATE_PROGRAM_NV = _vertex_program.GL_VERTEX_STATE_PROGRAM_NV
GL_ATTRIB_ARRAY_SIZE_NV = _vertex_program.GL_ATTRIB_ARRAY_SIZE_NV
GL_ATTRIB_ARRAY_STRIDE_NV = _vertex_program.GL_ATTRIB_ARRAY_STRIDE_NV
GL_ATTRIB_ARRAY_TYPE_NV = _vertex_program.GL_ATTRIB_ARRAY_TYPE_NV
GL_CURRENT_ATTRIB_NV = _vertex_program.GL_CURRENT_ATTRIB_NV
GL_PROGRAM_LENGTH_NV = _vertex_program.GL_PROGRAM_LENGTH_NV
GL_PROGRAM_STRING_NV = _vertex_program.GL_PROGRAM_STRING_NV
GL_MODELVIEW_PROJECTION_NV = _vertex_program.GL_MODELVIEW_PROJECTION_NV
GL_IDENTITY_NV = _vertex_program.GL_IDENTITY_NV
GL_INVERSE_NV = _vertex_program.GL_INVERSE_NV
GL_TRANSPOSE_NV = _vertex_program.GL_TRANSPOSE_NV
GL_INVERSE_TRANSPOSE_NV = _vertex_program.GL_INVERSE_TRANSPOSE_NV
GL_MAX_TRACK_MATRIX_STACK_DEPTH_NV = _vertex_program.GL_MAX_TRACK_MATRIX_STACK_DEPTH_NV
GL_MAX_TRACK_MATRICES_NV = _vertex_program.GL_MAX_TRACK_MATRICES_NV
GL_MATRIX0_NV = _vertex_program.GL_MATRIX0_NV
GL_MATRIX1_NV = _vertex_program.GL_MATRIX1_NV
GL_MATRIX2_NV = _vertex_program.GL_MATRIX2_NV
GL_MATRIX3_NV = _vertex_program.GL_MATRIX3_NV
GL_MATRIX4_NV = _vertex_program.GL_MATRIX4_NV
GL_MATRIX5_NV = _vertex_program.GL_MATRIX5_NV
GL_MATRIX6_NV = _vertex_program.GL_MATRIX6_NV
GL_MATRIX7_NV = _vertex_program.GL_MATRIX7_NV
GL_CURRENT_MATRIX_STACK_DEPTH_NV = _vertex_program.GL_CURRENT_MATRIX_STACK_DEPTH_NV
GL_CURRENT_MATRIX_NV = _vertex_program.GL_CURRENT_MATRIX_NV
GL_VERTEX_PROGRAM_POINT_SIZE_NV = _vertex_program.GL_VERTEX_PROGRAM_POINT_SIZE_NV
GL_VERTEX_PROGRAM_TWO_SIDE_NV = _vertex_program.GL_VERTEX_PROGRAM_TWO_SIDE_NV
GL_PROGRAM_PARAMETER_NV = _vertex_program.GL_PROGRAM_PARAMETER_NV
GL_ATTRIB_ARRAY_POINTER_NV = _vertex_program.GL_ATTRIB_ARRAY_POINTER_NV
GL_PROGRAM_TARGET_NV = _vertex_program.GL_PROGRAM_TARGET_NV
GL_PROGRAM_RESIDENT_NV = _vertex_program.GL_PROGRAM_RESIDENT_NV
GL_TRACK_MATRIX_NV = _vertex_program.GL_TRACK_MATRIX_NV
GL_TRACK_MATRIX_TRANSFORM_NV = _vertex_program.GL_TRACK_MATRIX_TRANSFORM_NV
GL_VERTEX_PROGRAM_BINDING_NV = _vertex_program.GL_VERTEX_PROGRAM_BINDING_NV
GL_PROGRAM_ERROR_POSITION_NV = _vertex_program.GL_PROGRAM_ERROR_POSITION_NV
GL_VERTEX_ATTRIB_ARRAY0_NV = _vertex_program.GL_VERTEX_ATTRIB_ARRAY0_NV
GL_VERTEX_ATTRIB_ARRAY1_NV = _vertex_program.GL_VERTEX_ATTRIB_ARRAY1_NV
GL_VERTEX_ATTRIB_ARRAY2_NV = _vertex_program.GL_VERTEX_ATTRIB_ARRAY2_NV
GL_VERTEX_ATTRIB_ARRAY3_NV = _vertex_program.GL_VERTEX_ATTRIB_ARRAY3_NV
GL_VERTEX_ATTRIB_ARRAY4_NV = _vertex_program.GL_VERTEX_ATTRIB_ARRAY4_NV
GL_VERTEX_ATTRIB_ARRAY5_NV = _vertex_program.GL_VERTEX_ATTRIB_ARRAY5_NV
GL_VERTEX_ATTRIB_ARRAY6_NV = _vertex_program.GL_VERTEX_ATTRIB_ARRAY6_NV
GL_VERTEX_ATTRIB_ARRAY7_NV = _vertex_program.GL_VERTEX_ATTRIB_ARRAY7_NV
GL_VERTEX_ATTRIB_ARRAY8_NV = _vertex_program.GL_VERTEX_ATTRIB_ARRAY8_NV
GL_VERTEX_ATTRIB_ARRAY9_NV = _vertex_program.GL_VERTEX_ATTRIB_ARRAY9_NV
GL_VERTEX_ATTRIB_ARRAY10_NV = _vertex_program.GL_VERTEX_ATTRIB_ARRAY10_NV
GL_VERTEX_ATTRIB_ARRAY11_NV = _vertex_program.GL_VERTEX_ATTRIB_ARRAY11_NV
GL_VERTEX_ATTRIB_ARRAY12_NV = _vertex_program.GL_VERTEX_ATTRIB_ARRAY12_NV
GL_VERTEX_ATTRIB_ARRAY13_NV = _vertex_program.GL_VERTEX_ATTRIB_ARRAY13_NV
GL_VERTEX_ATTRIB_ARRAY14_NV = _vertex_program.GL_VERTEX_ATTRIB_ARRAY14_NV
GL_VERTEX_ATTRIB_ARRAY15_NV = _vertex_program.GL_VERTEX_ATTRIB_ARRAY15_NV
GL_MAP1_VERTEX_ATTRIB0_4_NV = _vertex_program.GL_MAP1_VERTEX_ATTRIB0_4_NV
GL_MAP1_VERTEX_ATTRIB1_4_NV = _vertex_program.GL_MAP1_VERTEX_ATTRIB1_4_NV
GL_MAP1_VERTEX_ATTRIB2_4_NV = _vertex_program.GL_MAP1_VERTEX_ATTRIB2_4_NV
GL_MAP1_VERTEX_ATTRIB3_4_NV = _vertex_program.GL_MAP1_VERTEX_ATTRIB3_4_NV
GL_MAP1_VERTEX_ATTRIB4_4_NV = _vertex_program.GL_MAP1_VERTEX_ATTRIB4_4_NV
GL_MAP1_VERTEX_ATTRIB5_4_NV = _vertex_program.GL_MAP1_VERTEX_ATTRIB5_4_NV
GL_MAP1_VERTEX_ATTRIB6_4_NV = _vertex_program.GL_MAP1_VERTEX_ATTRIB6_4_NV
GL_MAP1_VERTEX_ATTRIB7_4_NV = _vertex_program.GL_MAP1_VERTEX_ATTRIB7_4_NV
GL_MAP1_VERTEX_ATTRIB8_4_NV = _vertex_program.GL_MAP1_VERTEX_ATTRIB8_4_NV
GL_MAP1_VERTEX_ATTRIB9_4_NV = _vertex_program.GL_MAP1_VERTEX_ATTRIB9_4_NV
GL_MAP1_VERTEX_ATTRIB10_4_NV = _vertex_program.GL_MAP1_VERTEX_ATTRIB10_4_NV
GL_MAP1_VERTEX_ATTRIB11_4_NV = _vertex_program.GL_MAP1_VERTEX_ATTRIB11_4_NV
GL_MAP1_VERTEX_ATTRIB12_4_NV = _vertex_program.GL_MAP1_VERTEX_ATTRIB12_4_NV
GL_MAP1_VERTEX_ATTRIB13_4_NV = _vertex_program.GL_MAP1_VERTEX_ATTRIB13_4_NV
GL_MAP1_VERTEX_ATTRIB14_4_NV = _vertex_program.GL_MAP1_VERTEX_ATTRIB14_4_NV
GL_MAP1_VERTEX_ATTRIB15_4_NV = _vertex_program.GL_MAP1_VERTEX_ATTRIB15_4_NV
GL_MAP2_VERTEX_ATTRIB0_4_NV = _vertex_program.GL_MAP2_VERTEX_ATTRIB0_4_NV
GL_MAP2_VERTEX_ATTRIB1_4_NV = _vertex_program.GL_MAP2_VERTEX_ATTRIB1_4_NV
GL_MAP2_VERTEX_ATTRIB2_4_NV = _vertex_program.GL_MAP2_VERTEX_ATTRIB2_4_NV
GL_MAP2_VERTEX_ATTRIB3_4_NV = _vertex_program.GL_MAP2_VERTEX_ATTRIB3_4_NV
GL_MAP2_VERTEX_ATTRIB4_4_NV = _vertex_program.GL_MAP2_VERTEX_ATTRIB4_4_NV
GL_MAP2_VERTEX_ATTRIB5_4_NV = _vertex_program.GL_MAP2_VERTEX_ATTRIB5_4_NV
GL_MAP2_VERTEX_ATTRIB6_4_NV = _vertex_program.GL_MAP2_VERTEX_ATTRIB6_4_NV
GL_MAP2_VERTEX_ATTRIB7_4_NV = _vertex_program.GL_MAP2_VERTEX_ATTRIB7_4_NV
GL_MAP2_VERTEX_ATTRIB8_4_NV = _vertex_program.GL_MAP2_VERTEX_ATTRIB8_4_NV
GL_MAP2_VERTEX_ATTRIB9_4_NV = _vertex_program.GL_MAP2_VERTEX_ATTRIB9_4_NV
GL_MAP2_VERTEX_ATTRIB10_4_NV = _vertex_program.GL_MAP2_VERTEX_ATTRIB10_4_NV
GL_MAP2_VERTEX_ATTRIB11_4_NV = _vertex_program.GL_MAP2_VERTEX_ATTRIB11_4_NV
GL_MAP2_VERTEX_ATTRIB12_4_NV = _vertex_program.GL_MAP2_VERTEX_ATTRIB12_4_NV
GL_MAP2_VERTEX_ATTRIB13_4_NV = _vertex_program.GL_MAP2_VERTEX_ATTRIB13_4_NV
GL_MAP2_VERTEX_ATTRIB14_4_NV = _vertex_program.GL_MAP2_VERTEX_ATTRIB14_4_NV
GL_MAP2_VERTEX_ATTRIB15_4_NV = _vertex_program.GL_MAP2_VERTEX_ATTRIB15_4_NV

glInitVertexProgramNV = _vertex_program.glInitVertexProgramNV

__info = _vertex_program.__info

