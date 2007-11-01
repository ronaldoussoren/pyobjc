# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _GL__init__

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


__version__ = _GL__init__.__version__
__date__ = _GL__init__.__date__
__api_version__ = _GL__init__.__api_version__
__author__ = _GL__init__.__author__
__doc__ = _GL__init__.__doc__
__numeric_present__ = _GL__init__.__numeric_present__
__numeric_support__ = _GL__init__.__numeric_support__

from operator import isSequenceType


glArrayElement = _GL__init__.glArrayElement

glBegin = _GL__init__.glBegin

glCallList = _GL__init__.glCallList

glCallLists = _GL__init__.glCallLists

glColor3b = _GL__init__.glColor3b

glColor3bv = _GL__init__.glColor3bv

glColor3d = _GL__init__.glColor3d

glColor3dv = _GL__init__.glColor3dv

glColor3f = _GL__init__.glColor3f

glColor3fv = _GL__init__.glColor3fv

glColor3i = _GL__init__.glColor3i

glColor3iv = _GL__init__.glColor3iv

glColor3s = _GL__init__.glColor3s

glColor3sv = _GL__init__.glColor3sv

glColor3ub = _GL__init__.glColor3ub

glColor3ubv = _GL__init__.glColor3ubv

glColor3ui = _GL__init__.glColor3ui

glColor3uiv = _GL__init__.glColor3uiv

glColor3us = _GL__init__.glColor3us

glColor3usv = _GL__init__.glColor3usv

glColor4b = _GL__init__.glColor4b

glColor4bv = _GL__init__.glColor4bv

glColor4d = _GL__init__.glColor4d

glColor4dv = _GL__init__.glColor4dv

glColor4f = _GL__init__.glColor4f

glColor4fv = _GL__init__.glColor4fv

glColor4i = _GL__init__.glColor4i

glColor4iv = _GL__init__.glColor4iv

glColor4s = _GL__init__.glColor4s

glColor4sv = _GL__init__.glColor4sv

glColor4ub = _GL__init__.glColor4ub

glColor4ubv = _GL__init__.glColor4ubv

glColor4ui = _GL__init__.glColor4ui

glColor4uiv = _GL__init__.glColor4uiv

glColor4us = _GL__init__.glColor4us

glColor4usv = _GL__init__.glColor4usv
# color utility funcs

def glColorub(*args):
	'glColorub(red, green, blue[, alpha]) | glColorub((red, green, blue[, alpha])) -> None'

	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]

	if len(args) == 3:
		glColor3ubv(args)
	elif len(args) == 4:
		glColor4ubv(args)
	else:
		raise TypeError, 'glColorub() takes 1, 3, or 4 arguments (%d given)' % len(args)


def glColorb(*args):
	'glColorb(red, green, blue[, alpha]) | glColorb((red, green, blue[, alpha])) -> None'

	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]

	if len(args) == 3:
		glColor3bv(args)
	elif len(args) == 4:
		glColor4bv(args)
	else:
		raise TypeError, 'glColorb() takes 1, 3, or 4 arguments (%d given)' % len(args)

def glColorus(*args):
	'glColorus(red, green, blue[, alpha]) | glColorus((red, green, blue[, alpha])) -> None'

	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]

	if len(args) == 3:
		glColor3usv(args)
	elif len(args) == 4:
		glColor4usv(args)
	else:
		raise TypeError, 'glColorus() takes 1, 3, or 4 arguments (%d given)' % len(args)

def glColors(*args):
	'glColors(red, green, blue[, alpha]) | glColors((red, green, blue[, alpha])) -> None'

	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]

	if len(args) == 3:
		glColor3sv(args)
	elif len(args) == 4:
		glColor4sv(args)
	else:
		raise TypeError, 'glColors() takes 1, 3, or 4 arguments (%d given)' % len(args)
	

def glColorui(*args):
	'glColorui(red, green, blue[, alpha]) | glColorui((red, green, blue[, alpha])) -> None'

	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]

	if len(args) == 3:
		glColor3uiv(args)
	elif len(args) == 4:
		glColor4uiv(args)
	else:
		raise TypeError, 'glColorui() takes 1, 3, or 4 arguments (%d given)' % len(args)
	

def glColori(*args):
	'glColori(red, green, blue[, alpha]) | glColori((red, green, blue[, alpha])) -> None'

	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]

	if len(args) == 3:
		glColor3iv(args)
	elif len(args) == 4:
		glColor4iv(args)
	else:
		raise TypeError, 'glColori() takes 1, 3, or 4 arguments (%d given)' % len(args)
	

def glColorf(*args):
	'glColorf(red, green, blue[, alpha]) | glColorf((red, green, blue[, alpha])) -> None'

	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]

	if len(args) == 3:
		glColor3fv(args)
	elif len(args) == 4:
		glColor4fv(args)
	else:
		raise TypeError, 'glColorf() takes 1, 3, or 4 arguments (%d given)' % len(args)
	

def glColord(*args):
	'glColord(red, green, blue[, alpha]) | glColord((red, green, blue[, alpha])) -> None'

	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]

	if len(args) == 3:
		glColor3dv(args)
	elif len(args) == 4:
		glColor4dv(args)
	else:
		raise TypeError, 'glColord() takes 1, 3, or 4 arguments (%d given)' % len(args)


glColor = glColord
glColor3 = glColord
glColor4 = glColord



glEdgeFlag = _GL__init__.glEdgeFlag

glEdgeFlagv = _GL__init__.glEdgeFlagv

glEvalCoord1d = _GL__init__.glEvalCoord1d

glEvalCoord1dv = _GL__init__.glEvalCoord1dv

glEvalCoord1f = _GL__init__.glEvalCoord1f

glEvalCoord1fv = _GL__init__.glEvalCoord1fv

glEvalCoord2d = _GL__init__.glEvalCoord2d

glEvalCoord2dv = _GL__init__.glEvalCoord2dv

glEvalCoord2f = _GL__init__.glEvalCoord2f

glEvalCoord2fv = _GL__init__.glEvalCoord2fv
# evalCoord utility funcs

def glEvalCoordf(*args):
	'glEvalCoordf(u[, v]) | glEvalCoordf((u[, v])) -> None'

	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]

	if len(args) == 1:
		glEvalCoord1f(args[0])
	elif len(args) == 2:
		glEvalCoord2fv(args)
	else:
		raise TypeError, 'glEvalCoordf() takes 1 or 2 arguments (%d given)' % len(args)
	

def glEvalCoordd(*args):
	'glEvalCoordd(u[, v]) | glEvalCoordd((u[, v])) -> None'

	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]

	if len(args) == 1:
		glEvalCoord1d(args[0])
	elif len(args) == 2:
		glEvalCoord2dv(args)
	else:
		raise TypeError, 'glEvalCoordd() takes 1 or 2 arguments (%d given)' % len(args)
		

glEvalCoord = glEvalCoordd
glEvalCoord1 = glEvalCoordd
glEvalCoord2 = glEvalCoordd



glEvalPoint1 = _GL__init__.glEvalPoint1

glEvalPoint2 = _GL__init__.glEvalPoint2
# evalPoint utility funcs

def glEvalPoint(*args):
	'glEvalPoint(i[, j]) | glEvalPoint((i[, j])) -> None'

	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]

	if len(args) == 1:
		glEvalPoint1(args[0])
	elif len(args) == 2:
		glEvalPoint2f(args[0], args[1])
	else:
		raise TypeError, 'glEvalPoint() takes 1 or 2 arguments (%d given)' % len(args)



glIndexd = _GL__init__.glIndexd

glIndexdv = _GL__init__.glIndexdv

glIndexf = _GL__init__.glIndexf

glIndexfv = _GL__init__.glIndexfv

glIndexi = _GL__init__.glIndexi

glIndexiv = _GL__init__.glIndexiv

glIndexs = _GL__init__.glIndexs

glIndexsv = _GL__init__.glIndexsv

glIndexub = _GL__init__.glIndexub

glIndexubv = _GL__init__.glIndexubv
glIndex = _GL__init__.glIndexd


glMaterialf = _GL__init__.glMaterialf

glMaterialfv = _GL__init__.glMaterialfv

glMateriali = _GL__init__.glMateriali

glMaterialiv = _GL__init__.glMaterialiv
glMaterial = _GL__init__.glMaterialfv


glNormal3b = _GL__init__.glNormal3b

glNormal3bv = _GL__init__.glNormal3bv

glNormal3d = _GL__init__.glNormal3d

glNormal3dv = _GL__init__.glNormal3dv

glNormal3f = _GL__init__.glNormal3f

glNormal3fv = _GL__init__.glNormal3fv

glNormal3i = _GL__init__.glNormal3i

glNormal3iv = _GL__init__.glNormal3iv

glNormal3s = _GL__init__.glNormal3s

glNormal3sv = _GL__init__.glNormal3sv
# normal utility funcs

def glNormalb(*args):
	'glNormalb(nx, ny, nz) | glNormalb((nx, ny, nz)) -> None'

	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]

	if len(args) == 3:
		glNormal3bv(args)
	elif len(args) == 4:
		glNormal4bv(args)
	else:
		raise TypeError, 'glNormalb() takes 1 or 3 arguments (%d given)' % len(args)
	

def glNormals(*args):
	'glNormals(nx, ny, nz) | glNormals((nx, ny, nz)) -> None'

	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]

	if len(args) == 3:
		glNormal3sv(args)
	elif len(args) == 4:
		glNormal4sv(args)
	else:
		raise TypeError, 'glNormals() takes 1 or 3 arguments (%d given)' % len(args)
	

def glNormali(*args):
	'glNormali(nx, ny, nz) | glNormali((nx, ny, nz)) -> None'

	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]

	if len(args) == 3:
		glNormal3iv(args)
	elif len(args) == 4:
		glNormal4iv(args)
	else:
		raise TypeError, 'glNormali() takes 1 or 3 arguments (%d given)' % len(args)
	

def glNormalf(*args):
	'glNormalf(nx, ny, nz) | glNormalf((nx, ny, nz)) -> None'

	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]

	if len(args) == 3:
		glNormal3fv(args)
	elif len(args) == 4:
		glNormal4fv(args)
	else:
		raise TypeError, 'glNormalf() takes 1 or 3 arguments (%d given)' % len(args)
	

def glNormald(*args):
	'glNormald(nx, ny, nz) | glNormald((nx, ny, nz)) -> None'

	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]

	if len(args) == 3:
		glNormal3dv(args)
	elif len(args) == 4:
		glNormal4dv(args)
	else:
		raise TypeError, 'glNormald() takes 1 or 3 arguments (%d given)' % len(args)


glNormal = glNormald
glNormal3 = glNormald
glNormal4 = glNormald


glTexCoord1d = _GL__init__.glTexCoord1d

glTexCoord1dv = _GL__init__.glTexCoord1dv

glTexCoord1f = _GL__init__.glTexCoord1f

glTexCoord1fv = _GL__init__.glTexCoord1fv

glTexCoord1i = _GL__init__.glTexCoord1i

glTexCoord1iv = _GL__init__.glTexCoord1iv

glTexCoord1s = _GL__init__.glTexCoord1s

glTexCoord1sv = _GL__init__.glTexCoord1sv

glTexCoord2d = _GL__init__.glTexCoord2d

glTexCoord2dv = _GL__init__.glTexCoord2dv

glTexCoord2f = _GL__init__.glTexCoord2f

glTexCoord2fv = _GL__init__.glTexCoord2fv

glTexCoord2i = _GL__init__.glTexCoord2i

glTexCoord2iv = _GL__init__.glTexCoord2iv

glTexCoord2s = _GL__init__.glTexCoord2s

glTexCoord2sv = _GL__init__.glTexCoord2sv

glTexCoord3d = _GL__init__.glTexCoord3d

glTexCoord3dv = _GL__init__.glTexCoord3dv

glTexCoord3f = _GL__init__.glTexCoord3f

glTexCoord3fv = _GL__init__.glTexCoord3fv

glTexCoord3i = _GL__init__.glTexCoord3i

glTexCoord3iv = _GL__init__.glTexCoord3iv

glTexCoord3s = _GL__init__.glTexCoord3s

glTexCoord3sv = _GL__init__.glTexCoord3sv

glTexCoord4d = _GL__init__.glTexCoord4d

glTexCoord4dv = _GL__init__.glTexCoord4dv

glTexCoord4f = _GL__init__.glTexCoord4f

glTexCoord4fv = _GL__init__.glTexCoord4fv

glTexCoord4i = _GL__init__.glTexCoord4i

glTexCoord4iv = _GL__init__.glTexCoord4iv

glTexCoord4s = _GL__init__.glTexCoord4s

glTexCoord4sv = _GL__init__.glTexCoord4sv
# texCoord utility funcs

def glTexCoordb(*args):
	'glTexCoordb(s[, t[, r[, q]]]) | glTexCoordb((s[, t[, r[, q]]])) -> None'

	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]

	if len(args) == 1:
		glTexCoord1b(args[0])
	elif len(args) == 2:
		glTexCoord2bv(args)
	elif len(args) == 3:
		glTexCoord3bv(args)
	elif len(args) == 4:
		glTexCoord4bv(args)
	else:
		raise TypeError, 'glTexCoordb() takes 1, 2, 3, or 4 arguments (%d given)' % len(args)
	

def glTexCoords(*args):
	'glTexCoords(s[, t[, r[, q]]]) | glTexCoords((s[, t[, r[, q]]])) -> None'

	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]

	if len(args) == 1:
		glTexCoord1s(args[0])
	elif len(args) == 2:
		glTexCoord2sv(args)
	elif len(args) == 3:
		glTexCoord3sv(args)
	elif len(args) == 4:
		glTexCoord4sv(args)
	else:
		raise TypeError, 'glTexCoords() takes 1, 2, 3, or 4 arguments (%d given)' % len(args)
	

def glTexCoordi(*args):
	'glTexCoordi(s[, t[, r[, q]]]) | glTexCoordi((s[, t[, r[, q]]])) -> None'

	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]

	if len(args) == 1:
		glTexCoord1i(args[0])
	elif len(args) == 2:
		glTexCoord2iv(args)
	elif len(args) == 3:
		glTexCoord3iv(args)
	elif len(args) == 4:
		glTexCoord4iv(args)
	else:
		raise TypeError, 'glTexCoordi() takes 1, 2, 3, or 4 arguments (%d given)' % len(args)
	

def glTexCoordf(*args):
	'glTexCoordf(s[, t[, r[, q]]]) | glTexCoordf((s[, t[, r[, q]]])) -> None'

	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]

	if len(args) == 1:
		glTexCoord1f(args[0])
	elif len(args) == 2:
		glTexCoord2fv(args)
	elif len(args) == 3:
		glTexCoord3fv(args)
	elif len(args) == 4:
		glTexCoord4fv(args)
	else:
		raise TypeError, 'glTexCoordf() takes 1, 2, 3, or 4 arguments (%d given)' % len(args)
	

def glTexCoordd(*args):
	'glTexCoordd(s[, t[, r[, q]]]) | glTexCoordd((s[, t[, r[, q]]])) -> None'

	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]

	if len(args) == 1:
		glTexCoord1d(args[0])
	elif len(args) == 2:
		glTexCoord2dv(args)
	elif len(args) == 3:
		glTexCoord3dv(args)
	elif len(args) == 4:
		glTexCoord4dv(args)
	else:
		raise TypeError, 'glTexCoordd() takes 1, 2, 3, or 4 arguments (%d given)' % len(args)


glTexCoord = glTexCoordd
glTexCoord1 = glTexCoordd
glTexCoord2 = glTexCoordd
glTexCoord3 = glTexCoordd
glTexCoord4 = glTexCoordd


glVertex2d = _GL__init__.glVertex2d

glVertex2dv = _GL__init__.glVertex2dv

glVertex2f = _GL__init__.glVertex2f

glVertex2fv = _GL__init__.glVertex2fv

glVertex2i = _GL__init__.glVertex2i

glVertex2iv = _GL__init__.glVertex2iv

glVertex2s = _GL__init__.glVertex2s

glVertex2sv = _GL__init__.glVertex2sv

glVertex3d = _GL__init__.glVertex3d

glVertex3dv = _GL__init__.glVertex3dv

glVertex3f = _GL__init__.glVertex3f

glVertex3fv = _GL__init__.glVertex3fv

glVertex3i = _GL__init__.glVertex3i

glVertex3iv = _GL__init__.glVertex3iv

glVertex3s = _GL__init__.glVertex3s

glVertex3sv = _GL__init__.glVertex3sv

glVertex4d = _GL__init__.glVertex4d

glVertex4dv = _GL__init__.glVertex4dv

glVertex4f = _GL__init__.glVertex4f

glVertex4fv = _GL__init__.glVertex4fv

glVertex4i = _GL__init__.glVertex4i

glVertex4iv = _GL__init__.glVertex4iv

glVertex4s = _GL__init__.glVertex4s

glVertex4sv = _GL__init__.glVertex4sv
# vertex utility funcs

def glVertexb(*args):
	'glVertexb(x, y[, z[, w]]) | glVertexb((x, y[, z[, w]])) -> None'

	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]

	if len(args) == 2:
		glVertex2bv(args)
	elif len(args) == 3:
		glVertex3bv(args)
	elif len(args) == 4:
		glVertex4bv(args)
	else:
		raise TypeError, 'glVertexb() takes 2, 3, or 4 arguments (%d given)' % len(args)
	

def glVertexs(*args):
	'glVertexs(x, y[, z[, w]]) | glVertexs((x, y[, z[, w]])) -> None'

	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]

	if len(args) == 2:
		glVertex2sv(args)
	elif len(args) == 3:
		glVertex3sv(args)
	elif len(args) == 4:
		glVertex4sv(args)
	else:
		raise TypeError, 'glVertexs() takes 2, 3, or 4 arguments (%d given)' % len(args)
	

def glVertexi(*args):
	'glVertexi(x, y[, z[, w]]) | glVertexi((x, y[, z[, w]])) -> None'

	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]

	if len(args) == 2:
		glVertex2iv(args)
	elif len(args) == 3:
		glVertex3iv(args)
	elif len(args) == 4:
		glVertex4iv(args)
	else:
		raise TypeError, 'glVertexi() takes 2, 3, or 4 arguments (%d given)' % len(args)
	

def glVertexf(*args):
	'glVertexf(x, y[, z[, w]]) | glVertexf((x, y[, z[, w]])) -> None'

	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]

	if len(args) == 2:
		glVertex2fv(args)
	elif len(args) == 3:
		glVertex3fv(args)
	elif len(args) == 4:
		glVertex4fv(args)
	else:
		raise TypeError, 'glVertexf() takes 2, 3, or 4 arguments (%d given)' % len(args)
	

def glVertexd(*args):
	'glVertexd(x, y[, z[, w]]) | glVertexd((x, y[, z[, w]])) -> None'

	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]

	if len(args) == 2:
		glVertex2dv(args)
	elif len(args) == 3:
		glVertex3dv(args)
	elif len(args) == 4:
		glVertex4dv(args)
	else:
		raise TypeError, 'glVertexd() takes 2, 3, or 4 arguments (%d given)' % len(args)


glVertex = glVertexd


__has_extension = _GL__init__.__has_extension

glAccum = _GL__init__.glAccum

glAlphaFunc = _GL__init__.glAlphaFunc

glAreTexturesResident = _GL__init__.glAreTexturesResident

glBindTexture = _GL__init__.glBindTexture

glBitmap = _GL__init__.glBitmap

glBlendFunc = _GL__init__.glBlendFunc

glClear = _GL__init__.glClear

glClearAccum = _GL__init__.glClearAccum

glClearColor = _GL__init__.glClearColor

glClearDepth = _GL__init__.glClearDepth

glClearIndex = _GL__init__.glClearIndex

glClearStencil = _GL__init__.glClearStencil

glClipPlane = _GL__init__.glClipPlane

glColorMask = _GL__init__.glColorMask

glColorMaterial = _GL__init__.glColorMaterial

glColorPointer = _GL__init__.glColorPointer

glColorPointerub = _GL__init__.glColorPointerub

glColorPointerb = _GL__init__.glColorPointerb

glColorPointerus = _GL__init__.glColorPointerus

glColorPointers = _GL__init__.glColorPointers

glColorPointerui = _GL__init__.glColorPointerui

glColorPointeri = _GL__init__.glColorPointeri

glColorPointerf = _GL__init__.glColorPointerf

glColorPointerd = _GL__init__.glColorPointerd

glCopyPixels = _GL__init__.glCopyPixels

glCopyTexImage1D = _GL__init__.glCopyTexImage1D

glCopyTexImage2D = _GL__init__.glCopyTexImage2D

glCopyTexSubImage1D = _GL__init__.glCopyTexSubImage1D

glCopyTexSubImage2D = _GL__init__.glCopyTexSubImage2D

glCullFace = _GL__init__.glCullFace

glDeleteLists = _GL__init__.glDeleteLists

glDeleteTextures = _GL__init__.glDeleteTextures

glDepthFunc = _GL__init__.glDepthFunc

glDepthMask = _GL__init__.glDepthMask

glDepthRange = _GL__init__.glDepthRange

glDisable = _GL__init__.glDisable

glDisableClientState = _GL__init__.glDisableClientState

glDrawArrays = _GL__init__.glDrawArrays

glDrawBuffer = _GL__init__.glDrawBuffer

glDrawElements = _GL__init__.glDrawElements

glDrawElementsub = _GL__init__.glDrawElementsub

glDrawElementsus = _GL__init__.glDrawElementsus

glDrawElementsui = _GL__init__.glDrawElementsui

glDrawPixels = _GL__init__.glDrawPixels

glDrawPixelsub = _GL__init__.glDrawPixelsub

glDrawPixelsb = _GL__init__.glDrawPixelsb

glDrawPixelsus = _GL__init__.glDrawPixelsus

glDrawPixelss = _GL__init__.glDrawPixelss

glDrawPixelsui = _GL__init__.glDrawPixelsui

glDrawPixelsi = _GL__init__.glDrawPixelsi

glDrawPixelsf = _GL__init__.glDrawPixelsf

glEdgeFlagPointer = _GL__init__.glEdgeFlagPointer

glEdgeFlagPointerb = _GL__init__.glEdgeFlagPointerb

glEnable = _GL__init__.glEnable

glEnableClientState = _GL__init__.glEnableClientState

glEnd = _GL__init__.glEnd

glEndList = _GL__init__.glEndList

glEvalMesh1 = _GL__init__.glEvalMesh1

glEvalMesh2 = _GL__init__.glEvalMesh2

glFeedbackBuffer = _GL__init__.glFeedbackBuffer

glFinish = _GL__init__.glFinish

glFlush = _GL__init__.glFlush

glFogf = _GL__init__.glFogf

glFogfv = _GL__init__.glFogfv

glFogi = _GL__init__.glFogi

glFogiv = _GL__init__.glFogiv
glFog = _GL__init__.glFogfv


glFrontFace = _GL__init__.glFrontFace

glFrustum = _GL__init__.glFrustum

glGenLists = _GL__init__.glGenLists

glGenTextures = _GL__init__.glGenTextures

glGetBooleanv = _GL__init__.glGetBooleanv
glGetBoolean = _GL__init__.glGetBooleanv


glGetClipPlane = _GL__init__.glGetClipPlane

glGetDoublev = _GL__init__.glGetDoublev
glGetDouble = _GL__init__.glGetDoublev


glGetFloatv = _GL__init__.glGetFloatv
glGetFloat = _GL__init__.glGetFloatv


glGetIntegerv = _GL__init__.glGetIntegerv
glGetInteger = _GL__init__.glGetIntegerv


glGetLightfv = _GL__init__.glGetLightfv

glGetLightiv = _GL__init__.glGetLightiv

glGetMapdv = _GL__init__.glGetMapdv

glGetMapfv = _GL__init__.glGetMapfv

glGetMapiv = _GL__init__.glGetMapiv

glGetMaterialfv = _GL__init__.glGetMaterialfv

glGetMaterialiv = _GL__init__.glGetMaterialiv

glGetPixelMapfv = _GL__init__.glGetPixelMapfv

glGetPixelMapuiv = _GL__init__.glGetPixelMapuiv

glGetPixelMapusv = _GL__init__.glGetPixelMapusv

glGetPolygonStipple = _GL__init__.glGetPolygonStipple

glGetPolygonStippleub = _GL__init__.glGetPolygonStippleub

glGetString = _GL__init__.glGetString

glGetTexEnvfv = _GL__init__.glGetTexEnvfv

glGetTexEnviv = _GL__init__.glGetTexEnviv

glGetTexGendv = _GL__init__.glGetTexGendv

glGetTexGenfv = _GL__init__.glGetTexGenfv

glGetTexGeniv = _GL__init__.glGetTexGeniv

glGetTexImage = _GL__init__.glGetTexImage

glGetTexImageub = _GL__init__.glGetTexImageub

glGetTexImageb = _GL__init__.glGetTexImageb

glGetTexImageus = _GL__init__.glGetTexImageus

glGetTexImages = _GL__init__.glGetTexImages

glGetTexImageui = _GL__init__.glGetTexImageui

glGetTexImagei = _GL__init__.glGetTexImagei

glGetTexImagef = _GL__init__.glGetTexImagef

glGetTexImaged = _GL__init__.glGetTexImaged

glGetTexLevelParameterfv = _GL__init__.glGetTexLevelParameterfv

glGetTexLevelParameteriv = _GL__init__.glGetTexLevelParameteriv

glGetTexParameterfv = _GL__init__.glGetTexParameterfv

glGetTexParameteriv = _GL__init__.glGetTexParameteriv

glHint = _GL__init__.glHint

glIndexMask = _GL__init__.glIndexMask

glIndexPointer = _GL__init__.glIndexPointer

glIndexPointerub = _GL__init__.glIndexPointerub

glIndexPointerb = _GL__init__.glIndexPointerb

glIndexPointers = _GL__init__.glIndexPointers

glIndexPointeri = _GL__init__.glIndexPointeri

glIndexPointerf = _GL__init__.glIndexPointerf

glIndexPointerd = _GL__init__.glIndexPointerd

glInitNames = _GL__init__.glInitNames

glInterleavedArrays = _GL__init__.glInterleavedArrays

glIsEnabled = _GL__init__.glIsEnabled

glIsList = _GL__init__.glIsList

glIsTexture = _GL__init__.glIsTexture

glLightModelf = _GL__init__.glLightModelf

glLightModelfv = _GL__init__.glLightModelfv

glLightModeli = _GL__init__.glLightModeli

glLightModeliv = _GL__init__.glLightModeliv
glLightModel = _GL__init__.glLightModelfv


glLightf = _GL__init__.glLightf

glLightfv = _GL__init__.glLightfv

glLighti = _GL__init__.glLighti

glLightiv = _GL__init__.glLightiv
glLight = _GL__init__.glLightfv


glLineStipple = _GL__init__.glLineStipple

glLineWidth = _GL__init__.glLineWidth

glListBase = _GL__init__.glListBase

glLoadIdentity = _GL__init__.glLoadIdentity

glLoadMatrixd = _GL__init__.glLoadMatrixd

glLoadMatrixf = _GL__init__.glLoadMatrixf

glLoadName = _GL__init__.glLoadName

glLogicOp = _GL__init__.glLogicOp

glMap1d = _GL__init__.glMap1d

glMap1f = _GL__init__.glMap1f

glMap2d = _GL__init__.glMap2d

glMap2f = _GL__init__.glMap2f

glMapGrid1d = _GL__init__.glMapGrid1d

glMapGrid1f = _GL__init__.glMapGrid1f

glMapGrid2d = _GL__init__.glMapGrid2d

glMapGrid2f = _GL__init__.glMapGrid2f

glMatrixMode = _GL__init__.glMatrixMode

glMultMatrixd = _GL__init__.glMultMatrixd

glMultMatrixf = _GL__init__.glMultMatrixf

glNewList = _GL__init__.glNewList

glNormalPointer = _GL__init__.glNormalPointer

glNormalPointerb = _GL__init__.glNormalPointerb

glNormalPointers = _GL__init__.glNormalPointers

glNormalPointeri = _GL__init__.glNormalPointeri

glNormalPointerf = _GL__init__.glNormalPointerf

glNormalPointerd = _GL__init__.glNormalPointerd

glOrtho = _GL__init__.glOrtho

glPassThrough = _GL__init__.glPassThrough

glPixelMapfv = _GL__init__.glPixelMapfv

glPixelMapuiv = _GL__init__.glPixelMapuiv

glPixelMapusv = _GL__init__.glPixelMapusv

glPixelStoref = _GL__init__.glPixelStoref

glPixelStorei = _GL__init__.glPixelStorei

glPixelTransferf = _GL__init__.glPixelTransferf

glPixelTransferi = _GL__init__.glPixelTransferi

glPixelZoom = _GL__init__.glPixelZoom

glPointSize = _GL__init__.glPointSize

glPolygonMode = _GL__init__.glPolygonMode

glPolygonOffset = _GL__init__.glPolygonOffset

glPolygonStipple = _GL__init__.glPolygonStipple

glPolygonStippleub = _GL__init__.glPolygonStippleub

glPopAttrib = _GL__init__.glPopAttrib

glPopClientAttrib = _GL__init__.glPopClientAttrib

glPopMatrix = _GL__init__.glPopMatrix

glPopName = _GL__init__.glPopName

glPrioritizeTextures = _GL__init__.glPrioritizeTextures

glPushAttrib = _GL__init__.glPushAttrib

glPushClientAttrib = _GL__init__.glPushClientAttrib

glPushMatrix = _GL__init__.glPushMatrix

glPushName = _GL__init__.glPushName

glRasterPos2d = _GL__init__.glRasterPos2d

glRasterPos2dv = _GL__init__.glRasterPos2dv

glRasterPos2f = _GL__init__.glRasterPos2f

glRasterPos2fv = _GL__init__.glRasterPos2fv

glRasterPos2i = _GL__init__.glRasterPos2i

glRasterPos2iv = _GL__init__.glRasterPos2iv

glRasterPos2s = _GL__init__.glRasterPos2s

glRasterPos2sv = _GL__init__.glRasterPos2sv

glRasterPos3d = _GL__init__.glRasterPos3d

glRasterPos3dv = _GL__init__.glRasterPos3dv

glRasterPos3f = _GL__init__.glRasterPos3f

glRasterPos3fv = _GL__init__.glRasterPos3fv

glRasterPos3i = _GL__init__.glRasterPos3i

glRasterPos3iv = _GL__init__.glRasterPos3iv

glRasterPos3s = _GL__init__.glRasterPos3s

glRasterPos3sv = _GL__init__.glRasterPos3sv

glRasterPos4d = _GL__init__.glRasterPos4d

glRasterPos4dv = _GL__init__.glRasterPos4dv

glRasterPos4f = _GL__init__.glRasterPos4f

glRasterPos4fv = _GL__init__.glRasterPos4fv

glRasterPos4i = _GL__init__.glRasterPos4i

glRasterPos4iv = _GL__init__.glRasterPos4iv

glRasterPos4s = _GL__init__.glRasterPos4s

glRasterPos4sv = _GL__init__.glRasterPos4sv
# rasterPos utility funcs

def glRasterPoss(*args):
	'glRasterPoss(x, y[, z[, w]]) | glRasterPoss((x, y[, z[, w]])) -> None'

	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]

	if len(args) == 2:
		glRasterPos2sv(args)
	elif len(args) == 3:
		glRasterPos3sv(args)
	elif len(args) == 4:
		glRasterPos4sv(args)
	else:
		raise TypeError, 'glRasterPoss() takes 2, 3, or 4 arguments (%d given)' % len(args)
	

def glRasterPosi(*args):
	'glRasterPosi(x, y[, z[, w]]) | glRasterPosi((x, y[, z[, w]])) -> None'

	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]

	if len(args) == 2:
		glRasterPos2iv(args)
	elif len(args) == 3:
		glRasterPos3iv(args)
	elif len(args) == 4:
		glRasterPos4iv(args)
	else:
		raise TypeError, 'glRasterPosi() takes 2, 3, or 4 arguments (%d given)' % len(args)
	

def glRasterPosf(*args):
	'glRasterPosf(x, y[, z[, w]]) | glRasterPosf((x, y[, z[, w]])) -> None'

	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]

	if len(args) == 2:
		glRasterPos2fv(args)
	elif len(args) == 3:
		glRasterPos3fv(args)
	elif len(args) == 4:
		glRasterPos4fv(args)
	else:
		raise TypeError, 'glRasterPosf() takes 2, 3, or 4 arguments (%d given)' % len(args)
	

def glRasterPosd(*args):
	'glRasterPosd(x, y[, z[, w]]) | glRasterPosd((x, y[, z[, w]])) -> None'

	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]

	if len(args) == 2:
		glRasterPos2dv(args)
	elif len(args) == 3:
		glRasterPos3dv(args)
	elif len(args) == 4:
		glRasterPos4dv(args)
	else:
		raise TypeError, 'glRasterPosd() takes 2, 3, or 4 arguments (%d given)' % len(args)


glRasterPos = glRasterPosd
glRasterPos2 = glRasterPosd
glRasterPos3 = glRasterPosd
glRasterPos4 = glRasterPosd



glReadBuffer = _GL__init__.glReadBuffer

glReadPixels = _GL__init__.glReadPixels

glReadPixelsub = _GL__init__.glReadPixelsub

glReadPixelsb = _GL__init__.glReadPixelsb

glReadPixelsus = _GL__init__.glReadPixelsus

glReadPixelss = _GL__init__.glReadPixelss

glReadPixelsui = _GL__init__.glReadPixelsui

glReadPixelsi = _GL__init__.glReadPixelsi

glReadPixelsf = _GL__init__.glReadPixelsf

glReadPixelsd = _GL__init__.glReadPixelsd

glRectd = _GL__init__.glRectd

glRectdv = _GL__init__.glRectdv

glRectf = _GL__init__.glRectf

glRectfv = _GL__init__.glRectfv

glRecti = _GL__init__.glRecti

glRectiv = _GL__init__.glRectiv

glRects = _GL__init__.glRects

glRectsv = _GL__init__.glRectsv

glRenderMode = _GL__init__.glRenderMode

glRotated = _GL__init__.glRotated

glRotatef = _GL__init__.glRotatef
glRotate = _GL__init__.glRotated


glScaled = _GL__init__.glScaled

glScalef = _GL__init__.glScalef
glScale = _GL__init__.glScaled


glScissor = _GL__init__.glScissor

glSelectBuffer = _GL__init__.glSelectBuffer
# glSelectWithCallback utility

def glSelectWithCallback(x, y, callback, xsize = 5, ysize = 5, buffer_size = 512):
	'''glSelectWithCallback(int x, int y, Callable callback, int xsize=5, int ysize=5)
  x,y -- x and y window coordinates for the center of the pick box
  rendercallback -- callback (callable Python object) taking 0 arguments
    which performs pick-mode rendering
  xsize,ysize -- x and y dimensions of the pick box (default = 5x5)
The function returns a tuple (possibly empty) of:
  ( (minimumzdepth, maximumzdepth, (name, name, name),...)
    minimumzdepth, maximumzdepth -- depths in integer format
      If you want the more traditional 0.0 to 1.0 numbers, divide
	  by (2**32)-1
      If you want the physical depth, multiply that by the frustrum depth and
        add your near clipping plane.
    name -- the names (integers) used in calls to glPushName( int )'''

	# this import needs to be late binding or Python gets stuck in an infinite import loop	
	from OpenGL.GLU import gluPickMatrix
	viewport = glGetIntegerv(GL_VIEWPORT)
	glSelectBuffer(buffer_size)
	glRenderMode(GL_SELECT)

	glInitNames()
	glMatrixMode(GL_PROJECTION)
	previousviewmatrix = glGetDoublev(GL_PROJECTION_MATRIX)
	glLoadIdentity()
	gluPickMatrix(x, viewport[3] - y, xsize, ysize, viewport)
	glMultMatrixd(previousviewmatrix)
	callback()
	glFlush()
	glMatrixMode(GL_PROJECTION)
	glLoadMatrixd(previousviewmatrix)

	return glRenderMode(GL_RENDER)



glShadeModel = _GL__init__.glShadeModel

glStencilFunc = _GL__init__.glStencilFunc

glStencilMask = _GL__init__.glStencilMask

glStencilOp = _GL__init__.glStencilOp

glTexCoordPointer = _GL__init__.glTexCoordPointer

glTexCoordPointerb = _GL__init__.glTexCoordPointerb

glTexCoordPointers = _GL__init__.glTexCoordPointers

glTexCoordPointeri = _GL__init__.glTexCoordPointeri

glTexCoordPointerf = _GL__init__.glTexCoordPointerf

glTexCoordPointerd = _GL__init__.glTexCoordPointerd

glTexEnvf = _GL__init__.glTexEnvf

glTexEnvfv = _GL__init__.glTexEnvfv

glTexEnvi = _GL__init__.glTexEnvi

glTexEnviv = _GL__init__.glTexEnviv

glTexGend = _GL__init__.glTexGend

glTexGendv = _GL__init__.glTexGendv

glTexGenf = _GL__init__.glTexGenf

glTexGenfv = _GL__init__.glTexGenfv

glTexGeni = _GL__init__.glTexGeni

glTexGeniv = _GL__init__.glTexGeniv
glTexGen = _GL__init__.glTexGendv


glTexImage1D = _GL__init__.glTexImage1D

glTexImage1Dub = _GL__init__.glTexImage1Dub

glTexImage1Db = _GL__init__.glTexImage1Db

glTexImage1Dus = _GL__init__.glTexImage1Dus

glTexImage1Ds = _GL__init__.glTexImage1Ds

glTexImage1Dui = _GL__init__.glTexImage1Dui

glTexImage1Di = _GL__init__.glTexImage1Di

glTexImage1Df = _GL__init__.glTexImage1Df

glTexImage2D = _GL__init__.glTexImage2D

glTexImage2Dub = _GL__init__.glTexImage2Dub

glTexImage2Db = _GL__init__.glTexImage2Db

glTexImage2Dus = _GL__init__.glTexImage2Dus

glTexImage2Ds = _GL__init__.glTexImage2Ds

glTexImage2Dui = _GL__init__.glTexImage2Dui

glTexImage2Di = _GL__init__.glTexImage2Di

glTexImage2Df = _GL__init__.glTexImage2Df

glTexParameterf = _GL__init__.glTexParameterf

glTexParameterfv = _GL__init__.glTexParameterfv

glTexParameteri = _GL__init__.glTexParameteri

glTexParameteriv = _GL__init__.glTexParameteriv
glTexParameter = _GL__init__.glTexParameterfv


glTexSubImage1D = _GL__init__.glTexSubImage1D

glTexSubImage1Dub = _GL__init__.glTexSubImage1Dub

glTexSubImage1Db = _GL__init__.glTexSubImage1Db

glTexSubImage1Dus = _GL__init__.glTexSubImage1Dus

glTexSubImage1Ds = _GL__init__.glTexSubImage1Ds

glTexSubImage1Dui = _GL__init__.glTexSubImage1Dui

glTexSubImage1Di = _GL__init__.glTexSubImage1Di

glTexSubImage1Df = _GL__init__.glTexSubImage1Df

glTexSubImage2D = _GL__init__.glTexSubImage2D

glTexSubImage2Dub = _GL__init__.glTexSubImage2Dub

glTexSubImage2Db = _GL__init__.glTexSubImage2Db

glTexSubImage2Dus = _GL__init__.glTexSubImage2Dus

glTexSubImage2Ds = _GL__init__.glTexSubImage2Ds

glTexSubImage2Dui = _GL__init__.glTexSubImage2Dui

glTexSubImage2Di = _GL__init__.glTexSubImage2Di

glTexSubImage2Df = _GL__init__.glTexSubImage2Df

glTranslated = _GL__init__.glTranslated

glTranslatef = _GL__init__.glTranslatef
glTranslate = _GL__init__.glTranslated


glVertexPointer = _GL__init__.glVertexPointer

glVertexPointerb = _GL__init__.glVertexPointerb

glVertexPointers = _GL__init__.glVertexPointers

glVertexPointeri = _GL__init__.glVertexPointeri

glVertexPointerf = _GL__init__.glVertexPointerf

glVertexPointerd = _GL__init__.glVertexPointerd

glViewport = _GL__init__.glViewport
GL_VERSION_1_1 = _GL__init__.GL_VERSION_1_1
GL_ACCUM = _GL__init__.GL_ACCUM
GL_LOAD = _GL__init__.GL_LOAD
GL_RETURN = _GL__init__.GL_RETURN
GL_MULT = _GL__init__.GL_MULT
GL_ADD = _GL__init__.GL_ADD
GL_NEVER = _GL__init__.GL_NEVER
GL_LESS = _GL__init__.GL_LESS
GL_EQUAL = _GL__init__.GL_EQUAL
GL_LEQUAL = _GL__init__.GL_LEQUAL
GL_GREATER = _GL__init__.GL_GREATER
GL_NOTEQUAL = _GL__init__.GL_NOTEQUAL
GL_GEQUAL = _GL__init__.GL_GEQUAL
GL_ALWAYS = _GL__init__.GL_ALWAYS
GL_CURRENT_BIT = _GL__init__.GL_CURRENT_BIT
GL_POINT_BIT = _GL__init__.GL_POINT_BIT
GL_LINE_BIT = _GL__init__.GL_LINE_BIT
GL_POLYGON_BIT = _GL__init__.GL_POLYGON_BIT
GL_POLYGON_STIPPLE_BIT = _GL__init__.GL_POLYGON_STIPPLE_BIT
GL_PIXEL_MODE_BIT = _GL__init__.GL_PIXEL_MODE_BIT
GL_LIGHTING_BIT = _GL__init__.GL_LIGHTING_BIT
GL_FOG_BIT = _GL__init__.GL_FOG_BIT
GL_DEPTH_BUFFER_BIT = _GL__init__.GL_DEPTH_BUFFER_BIT
GL_ACCUM_BUFFER_BIT = _GL__init__.GL_ACCUM_BUFFER_BIT
GL_STENCIL_BUFFER_BIT = _GL__init__.GL_STENCIL_BUFFER_BIT
GL_VIEWPORT_BIT = _GL__init__.GL_VIEWPORT_BIT
GL_TRANSFORM_BIT = _GL__init__.GL_TRANSFORM_BIT
GL_ENABLE_BIT = _GL__init__.GL_ENABLE_BIT
GL_COLOR_BUFFER_BIT = _GL__init__.GL_COLOR_BUFFER_BIT
GL_HINT_BIT = _GL__init__.GL_HINT_BIT
GL_EVAL_BIT = _GL__init__.GL_EVAL_BIT
GL_LIST_BIT = _GL__init__.GL_LIST_BIT
GL_TEXTURE_BIT = _GL__init__.GL_TEXTURE_BIT
GL_SCISSOR_BIT = _GL__init__.GL_SCISSOR_BIT
GL_ALL_ATTRIB_BITS = _GL__init__.GL_ALL_ATTRIB_BITS
GL_POINTS = _GL__init__.GL_POINTS
GL_LINES = _GL__init__.GL_LINES
GL_LINE_LOOP = _GL__init__.GL_LINE_LOOP
GL_LINE_STRIP = _GL__init__.GL_LINE_STRIP
GL_TRIANGLES = _GL__init__.GL_TRIANGLES
GL_TRIANGLE_STRIP = _GL__init__.GL_TRIANGLE_STRIP
GL_TRIANGLE_FAN = _GL__init__.GL_TRIANGLE_FAN
GL_QUADS = _GL__init__.GL_QUADS
GL_QUAD_STRIP = _GL__init__.GL_QUAD_STRIP
GL_POLYGON = _GL__init__.GL_POLYGON
GL_ZERO = _GL__init__.GL_ZERO
GL_ONE = _GL__init__.GL_ONE
GL_SRC_COLOR = _GL__init__.GL_SRC_COLOR
GL_ONE_MINUS_SRC_COLOR = _GL__init__.GL_ONE_MINUS_SRC_COLOR
GL_SRC_ALPHA = _GL__init__.GL_SRC_ALPHA
GL_ONE_MINUS_SRC_ALPHA = _GL__init__.GL_ONE_MINUS_SRC_ALPHA
GL_DST_ALPHA = _GL__init__.GL_DST_ALPHA
GL_ONE_MINUS_DST_ALPHA = _GL__init__.GL_ONE_MINUS_DST_ALPHA
GL_DST_COLOR = _GL__init__.GL_DST_COLOR
GL_ONE_MINUS_DST_COLOR = _GL__init__.GL_ONE_MINUS_DST_COLOR
GL_SRC_ALPHA_SATURATE = _GL__init__.GL_SRC_ALPHA_SATURATE
GL_TRUE = _GL__init__.GL_TRUE
GL_FALSE = _GL__init__.GL_FALSE
GL_CLIP_PLANE0 = _GL__init__.GL_CLIP_PLANE0
GL_CLIP_PLANE1 = _GL__init__.GL_CLIP_PLANE1
GL_CLIP_PLANE2 = _GL__init__.GL_CLIP_PLANE2
GL_CLIP_PLANE3 = _GL__init__.GL_CLIP_PLANE3
GL_CLIP_PLANE4 = _GL__init__.GL_CLIP_PLANE4
GL_CLIP_PLANE5 = _GL__init__.GL_CLIP_PLANE5
GL_BYTE = _GL__init__.GL_BYTE
GL_UNSIGNED_BYTE = _GL__init__.GL_UNSIGNED_BYTE
GL_SHORT = _GL__init__.GL_SHORT
GL_UNSIGNED_SHORT = _GL__init__.GL_UNSIGNED_SHORT
GL_INT = _GL__init__.GL_INT
GL_UNSIGNED_INT = _GL__init__.GL_UNSIGNED_INT
GL_FLOAT = _GL__init__.GL_FLOAT
GL_2_BYTES = _GL__init__.GL_2_BYTES
GL_3_BYTES = _GL__init__.GL_3_BYTES
GL_4_BYTES = _GL__init__.GL_4_BYTES
GL_DOUBLE = _GL__init__.GL_DOUBLE
GL_NONE = _GL__init__.GL_NONE
GL_FRONT_LEFT = _GL__init__.GL_FRONT_LEFT
GL_FRONT_RIGHT = _GL__init__.GL_FRONT_RIGHT
GL_BACK_LEFT = _GL__init__.GL_BACK_LEFT
GL_BACK_RIGHT = _GL__init__.GL_BACK_RIGHT
GL_FRONT = _GL__init__.GL_FRONT
GL_BACK = _GL__init__.GL_BACK
GL_LEFT = _GL__init__.GL_LEFT
GL_RIGHT = _GL__init__.GL_RIGHT
GL_FRONT_AND_BACK = _GL__init__.GL_FRONT_AND_BACK
GL_AUX0 = _GL__init__.GL_AUX0
GL_AUX1 = _GL__init__.GL_AUX1
GL_AUX2 = _GL__init__.GL_AUX2
GL_AUX3 = _GL__init__.GL_AUX3
GL_NO_ERROR = _GL__init__.GL_NO_ERROR
GL_INVALID_ENUM = _GL__init__.GL_INVALID_ENUM
GL_INVALID_VALUE = _GL__init__.GL_INVALID_VALUE
GL_INVALID_OPERATION = _GL__init__.GL_INVALID_OPERATION
GL_STACK_OVERFLOW = _GL__init__.GL_STACK_OVERFLOW
GL_STACK_UNDERFLOW = _GL__init__.GL_STACK_UNDERFLOW
GL_OUT_OF_MEMORY = _GL__init__.GL_OUT_OF_MEMORY
GL_2D = _GL__init__.GL_2D
GL_3D = _GL__init__.GL_3D
GL_3D_COLOR = _GL__init__.GL_3D_COLOR
GL_3D_COLOR_TEXTURE = _GL__init__.GL_3D_COLOR_TEXTURE
GL_4D_COLOR_TEXTURE = _GL__init__.GL_4D_COLOR_TEXTURE
GL_PASS_THROUGH_TOKEN = _GL__init__.GL_PASS_THROUGH_TOKEN
GL_POINT_TOKEN = _GL__init__.GL_POINT_TOKEN
GL_LINE_TOKEN = _GL__init__.GL_LINE_TOKEN
GL_POLYGON_TOKEN = _GL__init__.GL_POLYGON_TOKEN
GL_BITMAP_TOKEN = _GL__init__.GL_BITMAP_TOKEN
GL_DRAW_PIXEL_TOKEN = _GL__init__.GL_DRAW_PIXEL_TOKEN
GL_COPY_PIXEL_TOKEN = _GL__init__.GL_COPY_PIXEL_TOKEN
GL_LINE_RESET_TOKEN = _GL__init__.GL_LINE_RESET_TOKEN
GL_EXP = _GL__init__.GL_EXP
GL_EXP2 = _GL__init__.GL_EXP2
GL_CW = _GL__init__.GL_CW
GL_CCW = _GL__init__.GL_CCW
GL_COEFF = _GL__init__.GL_COEFF
GL_ORDER = _GL__init__.GL_ORDER
GL_DOMAIN = _GL__init__.GL_DOMAIN
GL_CURRENT_COLOR = _GL__init__.GL_CURRENT_COLOR
GL_CURRENT_INDEX = _GL__init__.GL_CURRENT_INDEX
GL_CURRENT_NORMAL = _GL__init__.GL_CURRENT_NORMAL
GL_CURRENT_TEXTURE_COORDS = _GL__init__.GL_CURRENT_TEXTURE_COORDS
GL_CURRENT_RASTER_COLOR = _GL__init__.GL_CURRENT_RASTER_COLOR
GL_CURRENT_RASTER_INDEX = _GL__init__.GL_CURRENT_RASTER_INDEX
GL_CURRENT_RASTER_TEXTURE_COORDS = _GL__init__.GL_CURRENT_RASTER_TEXTURE_COORDS
GL_CURRENT_RASTER_POSITION = _GL__init__.GL_CURRENT_RASTER_POSITION
GL_CURRENT_RASTER_POSITION_VALID = _GL__init__.GL_CURRENT_RASTER_POSITION_VALID
GL_CURRENT_RASTER_DISTANCE = _GL__init__.GL_CURRENT_RASTER_DISTANCE
GL_POINT_SMOOTH = _GL__init__.GL_POINT_SMOOTH
GL_POINT_SIZE = _GL__init__.GL_POINT_SIZE
GL_POINT_SIZE_RANGE = _GL__init__.GL_POINT_SIZE_RANGE
GL_POINT_SIZE_GRANULARITY = _GL__init__.GL_POINT_SIZE_GRANULARITY
GL_LINE_SMOOTH = _GL__init__.GL_LINE_SMOOTH
GL_LINE_WIDTH = _GL__init__.GL_LINE_WIDTH
GL_LINE_WIDTH_RANGE = _GL__init__.GL_LINE_WIDTH_RANGE
GL_LINE_WIDTH_GRANULARITY = _GL__init__.GL_LINE_WIDTH_GRANULARITY
GL_LINE_STIPPLE = _GL__init__.GL_LINE_STIPPLE
GL_LINE_STIPPLE_PATTERN = _GL__init__.GL_LINE_STIPPLE_PATTERN
GL_LINE_STIPPLE_REPEAT = _GL__init__.GL_LINE_STIPPLE_REPEAT
GL_LIST_MODE = _GL__init__.GL_LIST_MODE
GL_MAX_LIST_NESTING = _GL__init__.GL_MAX_LIST_NESTING
GL_LIST_BASE = _GL__init__.GL_LIST_BASE
GL_LIST_INDEX = _GL__init__.GL_LIST_INDEX
GL_POLYGON_MODE = _GL__init__.GL_POLYGON_MODE
GL_POLYGON_SMOOTH = _GL__init__.GL_POLYGON_SMOOTH
GL_POLYGON_STIPPLE = _GL__init__.GL_POLYGON_STIPPLE
GL_EDGE_FLAG = _GL__init__.GL_EDGE_FLAG
GL_CULL_FACE = _GL__init__.GL_CULL_FACE
GL_CULL_FACE_MODE = _GL__init__.GL_CULL_FACE_MODE
GL_FRONT_FACE = _GL__init__.GL_FRONT_FACE
GL_LIGHTING = _GL__init__.GL_LIGHTING
GL_LIGHT_MODEL_LOCAL_VIEWER = _GL__init__.GL_LIGHT_MODEL_LOCAL_VIEWER
GL_LIGHT_MODEL_TWO_SIDE = _GL__init__.GL_LIGHT_MODEL_TWO_SIDE
GL_LIGHT_MODEL_AMBIENT = _GL__init__.GL_LIGHT_MODEL_AMBIENT
GL_SHADE_MODEL = _GL__init__.GL_SHADE_MODEL
GL_COLOR_MATERIAL_FACE = _GL__init__.GL_COLOR_MATERIAL_FACE
GL_COLOR_MATERIAL_PARAMETER = _GL__init__.GL_COLOR_MATERIAL_PARAMETER
GL_COLOR_MATERIAL = _GL__init__.GL_COLOR_MATERIAL
GL_FOG = _GL__init__.GL_FOG
GL_FOG_INDEX = _GL__init__.GL_FOG_INDEX
GL_FOG_DENSITY = _GL__init__.GL_FOG_DENSITY
GL_FOG_START = _GL__init__.GL_FOG_START
GL_FOG_END = _GL__init__.GL_FOG_END
GL_FOG_MODE = _GL__init__.GL_FOG_MODE
GL_FOG_COLOR = _GL__init__.GL_FOG_COLOR
GL_DEPTH_RANGE = _GL__init__.GL_DEPTH_RANGE
GL_DEPTH_TEST = _GL__init__.GL_DEPTH_TEST
GL_DEPTH_WRITEMASK = _GL__init__.GL_DEPTH_WRITEMASK
GL_DEPTH_CLEAR_VALUE = _GL__init__.GL_DEPTH_CLEAR_VALUE
GL_DEPTH_FUNC = _GL__init__.GL_DEPTH_FUNC
GL_ACCUM_CLEAR_VALUE = _GL__init__.GL_ACCUM_CLEAR_VALUE
GL_STENCIL_TEST = _GL__init__.GL_STENCIL_TEST
GL_STENCIL_CLEAR_VALUE = _GL__init__.GL_STENCIL_CLEAR_VALUE
GL_STENCIL_FUNC = _GL__init__.GL_STENCIL_FUNC
GL_STENCIL_VALUE_MASK = _GL__init__.GL_STENCIL_VALUE_MASK
GL_STENCIL_FAIL = _GL__init__.GL_STENCIL_FAIL
GL_STENCIL_PASS_DEPTH_FAIL = _GL__init__.GL_STENCIL_PASS_DEPTH_FAIL
GL_STENCIL_PASS_DEPTH_PASS = _GL__init__.GL_STENCIL_PASS_DEPTH_PASS
GL_STENCIL_REF = _GL__init__.GL_STENCIL_REF
GL_STENCIL_WRITEMASK = _GL__init__.GL_STENCIL_WRITEMASK
GL_MATRIX_MODE = _GL__init__.GL_MATRIX_MODE
GL_NORMALIZE = _GL__init__.GL_NORMALIZE
GL_VIEWPORT = _GL__init__.GL_VIEWPORT
GL_MODELVIEW_STACK_DEPTH = _GL__init__.GL_MODELVIEW_STACK_DEPTH
GL_PROJECTION_STACK_DEPTH = _GL__init__.GL_PROJECTION_STACK_DEPTH
GL_TEXTURE_STACK_DEPTH = _GL__init__.GL_TEXTURE_STACK_DEPTH
GL_MODELVIEW_MATRIX = _GL__init__.GL_MODELVIEW_MATRIX
GL_PROJECTION_MATRIX = _GL__init__.GL_PROJECTION_MATRIX
GL_TEXTURE_MATRIX = _GL__init__.GL_TEXTURE_MATRIX
GL_ATTRIB_STACK_DEPTH = _GL__init__.GL_ATTRIB_STACK_DEPTH
GL_CLIENT_ATTRIB_STACK_DEPTH = _GL__init__.GL_CLIENT_ATTRIB_STACK_DEPTH
GL_ALPHA_TEST = _GL__init__.GL_ALPHA_TEST
GL_ALPHA_TEST_FUNC = _GL__init__.GL_ALPHA_TEST_FUNC
GL_ALPHA_TEST_REF = _GL__init__.GL_ALPHA_TEST_REF
GL_DITHER = _GL__init__.GL_DITHER
GL_BLEND_DST = _GL__init__.GL_BLEND_DST
GL_BLEND_SRC = _GL__init__.GL_BLEND_SRC
GL_BLEND = _GL__init__.GL_BLEND
GL_LOGIC_OP_MODE = _GL__init__.GL_LOGIC_OP_MODE
GL_INDEX_LOGIC_OP = _GL__init__.GL_INDEX_LOGIC_OP
GL_COLOR_LOGIC_OP = _GL__init__.GL_COLOR_LOGIC_OP
GL_AUX_BUFFERS = _GL__init__.GL_AUX_BUFFERS
GL_DRAW_BUFFER = _GL__init__.GL_DRAW_BUFFER
GL_READ_BUFFER = _GL__init__.GL_READ_BUFFER
GL_SCISSOR_BOX = _GL__init__.GL_SCISSOR_BOX
GL_SCISSOR_TEST = _GL__init__.GL_SCISSOR_TEST
GL_INDEX_CLEAR_VALUE = _GL__init__.GL_INDEX_CLEAR_VALUE
GL_INDEX_WRITEMASK = _GL__init__.GL_INDEX_WRITEMASK
GL_COLOR_CLEAR_VALUE = _GL__init__.GL_COLOR_CLEAR_VALUE
GL_COLOR_WRITEMASK = _GL__init__.GL_COLOR_WRITEMASK
GL_INDEX_MODE = _GL__init__.GL_INDEX_MODE
GL_RGBA_MODE = _GL__init__.GL_RGBA_MODE
GL_DOUBLEBUFFER = _GL__init__.GL_DOUBLEBUFFER
GL_STEREO = _GL__init__.GL_STEREO
GL_RENDER_MODE = _GL__init__.GL_RENDER_MODE
GL_PERSPECTIVE_CORRECTION_HINT = _GL__init__.GL_PERSPECTIVE_CORRECTION_HINT
GL_POINT_SMOOTH_HINT = _GL__init__.GL_POINT_SMOOTH_HINT
GL_LINE_SMOOTH_HINT = _GL__init__.GL_LINE_SMOOTH_HINT
GL_POLYGON_SMOOTH_HINT = _GL__init__.GL_POLYGON_SMOOTH_HINT
GL_FOG_HINT = _GL__init__.GL_FOG_HINT
GL_TEXTURE_GEN_S = _GL__init__.GL_TEXTURE_GEN_S
GL_TEXTURE_GEN_T = _GL__init__.GL_TEXTURE_GEN_T
GL_TEXTURE_GEN_R = _GL__init__.GL_TEXTURE_GEN_R
GL_TEXTURE_GEN_Q = _GL__init__.GL_TEXTURE_GEN_Q
GL_PIXEL_MAP_I_TO_I = _GL__init__.GL_PIXEL_MAP_I_TO_I
GL_PIXEL_MAP_S_TO_S = _GL__init__.GL_PIXEL_MAP_S_TO_S
GL_PIXEL_MAP_I_TO_R = _GL__init__.GL_PIXEL_MAP_I_TO_R
GL_PIXEL_MAP_I_TO_G = _GL__init__.GL_PIXEL_MAP_I_TO_G
GL_PIXEL_MAP_I_TO_B = _GL__init__.GL_PIXEL_MAP_I_TO_B
GL_PIXEL_MAP_I_TO_A = _GL__init__.GL_PIXEL_MAP_I_TO_A
GL_PIXEL_MAP_R_TO_R = _GL__init__.GL_PIXEL_MAP_R_TO_R
GL_PIXEL_MAP_G_TO_G = _GL__init__.GL_PIXEL_MAP_G_TO_G
GL_PIXEL_MAP_B_TO_B = _GL__init__.GL_PIXEL_MAP_B_TO_B
GL_PIXEL_MAP_A_TO_A = _GL__init__.GL_PIXEL_MAP_A_TO_A
GL_PIXEL_MAP_I_TO_I_SIZE = _GL__init__.GL_PIXEL_MAP_I_TO_I_SIZE
GL_PIXEL_MAP_S_TO_S_SIZE = _GL__init__.GL_PIXEL_MAP_S_TO_S_SIZE
GL_PIXEL_MAP_I_TO_R_SIZE = _GL__init__.GL_PIXEL_MAP_I_TO_R_SIZE
GL_PIXEL_MAP_I_TO_G_SIZE = _GL__init__.GL_PIXEL_MAP_I_TO_G_SIZE
GL_PIXEL_MAP_I_TO_B_SIZE = _GL__init__.GL_PIXEL_MAP_I_TO_B_SIZE
GL_PIXEL_MAP_I_TO_A_SIZE = _GL__init__.GL_PIXEL_MAP_I_TO_A_SIZE
GL_PIXEL_MAP_R_TO_R_SIZE = _GL__init__.GL_PIXEL_MAP_R_TO_R_SIZE
GL_PIXEL_MAP_G_TO_G_SIZE = _GL__init__.GL_PIXEL_MAP_G_TO_G_SIZE
GL_PIXEL_MAP_B_TO_B_SIZE = _GL__init__.GL_PIXEL_MAP_B_TO_B_SIZE
GL_PIXEL_MAP_A_TO_A_SIZE = _GL__init__.GL_PIXEL_MAP_A_TO_A_SIZE
GL_UNPACK_SWAP_BYTES = _GL__init__.GL_UNPACK_SWAP_BYTES
GL_UNPACK_LSB_FIRST = _GL__init__.GL_UNPACK_LSB_FIRST
GL_UNPACK_ROW_LENGTH = _GL__init__.GL_UNPACK_ROW_LENGTH
GL_UNPACK_SKIP_ROWS = _GL__init__.GL_UNPACK_SKIP_ROWS
GL_UNPACK_SKIP_PIXELS = _GL__init__.GL_UNPACK_SKIP_PIXELS
GL_UNPACK_ALIGNMENT = _GL__init__.GL_UNPACK_ALIGNMENT
GL_PACK_SWAP_BYTES = _GL__init__.GL_PACK_SWAP_BYTES
GL_PACK_LSB_FIRST = _GL__init__.GL_PACK_LSB_FIRST
GL_PACK_ROW_LENGTH = _GL__init__.GL_PACK_ROW_LENGTH
GL_PACK_SKIP_ROWS = _GL__init__.GL_PACK_SKIP_ROWS
GL_PACK_SKIP_PIXELS = _GL__init__.GL_PACK_SKIP_PIXELS
GL_PACK_ALIGNMENT = _GL__init__.GL_PACK_ALIGNMENT
GL_MAP_COLOR = _GL__init__.GL_MAP_COLOR
GL_MAP_STENCIL = _GL__init__.GL_MAP_STENCIL
GL_INDEX_SHIFT = _GL__init__.GL_INDEX_SHIFT
GL_INDEX_OFFSET = _GL__init__.GL_INDEX_OFFSET
GL_RED_SCALE = _GL__init__.GL_RED_SCALE
GL_RED_BIAS = _GL__init__.GL_RED_BIAS
GL_ZOOM_X = _GL__init__.GL_ZOOM_X
GL_ZOOM_Y = _GL__init__.GL_ZOOM_Y
GL_GREEN_SCALE = _GL__init__.GL_GREEN_SCALE
GL_GREEN_BIAS = _GL__init__.GL_GREEN_BIAS
GL_BLUE_SCALE = _GL__init__.GL_BLUE_SCALE
GL_BLUE_BIAS = _GL__init__.GL_BLUE_BIAS
GL_ALPHA_SCALE = _GL__init__.GL_ALPHA_SCALE
GL_ALPHA_BIAS = _GL__init__.GL_ALPHA_BIAS
GL_DEPTH_SCALE = _GL__init__.GL_DEPTH_SCALE
GL_DEPTH_BIAS = _GL__init__.GL_DEPTH_BIAS
GL_MAX_EVAL_ORDER = _GL__init__.GL_MAX_EVAL_ORDER
GL_MAX_LIGHTS = _GL__init__.GL_MAX_LIGHTS
GL_MAX_CLIP_PLANES = _GL__init__.GL_MAX_CLIP_PLANES
GL_MAX_TEXTURE_SIZE = _GL__init__.GL_MAX_TEXTURE_SIZE
GL_MAX_PIXEL_MAP_TABLE = _GL__init__.GL_MAX_PIXEL_MAP_TABLE
GL_MAX_ATTRIB_STACK_DEPTH = _GL__init__.GL_MAX_ATTRIB_STACK_DEPTH
GL_MAX_MODELVIEW_STACK_DEPTH = _GL__init__.GL_MAX_MODELVIEW_STACK_DEPTH
GL_MAX_NAME_STACK_DEPTH = _GL__init__.GL_MAX_NAME_STACK_DEPTH
GL_MAX_PROJECTION_STACK_DEPTH = _GL__init__.GL_MAX_PROJECTION_STACK_DEPTH
GL_MAX_TEXTURE_STACK_DEPTH = _GL__init__.GL_MAX_TEXTURE_STACK_DEPTH
GL_MAX_VIEWPORT_DIMS = _GL__init__.GL_MAX_VIEWPORT_DIMS
GL_MAX_CLIENT_ATTRIB_STACK_DEPTH = _GL__init__.GL_MAX_CLIENT_ATTRIB_STACK_DEPTH
GL_SUBPIXEL_BITS = _GL__init__.GL_SUBPIXEL_BITS
GL_INDEX_BITS = _GL__init__.GL_INDEX_BITS
GL_RED_BITS = _GL__init__.GL_RED_BITS
GL_GREEN_BITS = _GL__init__.GL_GREEN_BITS
GL_BLUE_BITS = _GL__init__.GL_BLUE_BITS
GL_ALPHA_BITS = _GL__init__.GL_ALPHA_BITS
GL_DEPTH_BITS = _GL__init__.GL_DEPTH_BITS
GL_STENCIL_BITS = _GL__init__.GL_STENCIL_BITS
GL_ACCUM_RED_BITS = _GL__init__.GL_ACCUM_RED_BITS
GL_ACCUM_GREEN_BITS = _GL__init__.GL_ACCUM_GREEN_BITS
GL_ACCUM_BLUE_BITS = _GL__init__.GL_ACCUM_BLUE_BITS
GL_ACCUM_ALPHA_BITS = _GL__init__.GL_ACCUM_ALPHA_BITS
GL_NAME_STACK_DEPTH = _GL__init__.GL_NAME_STACK_DEPTH
GL_AUTO_NORMAL = _GL__init__.GL_AUTO_NORMAL
GL_MAP1_COLOR_4 = _GL__init__.GL_MAP1_COLOR_4
GL_MAP1_INDEX = _GL__init__.GL_MAP1_INDEX
GL_MAP1_NORMAL = _GL__init__.GL_MAP1_NORMAL
GL_MAP1_TEXTURE_COORD_1 = _GL__init__.GL_MAP1_TEXTURE_COORD_1
GL_MAP1_TEXTURE_COORD_2 = _GL__init__.GL_MAP1_TEXTURE_COORD_2
GL_MAP1_TEXTURE_COORD_3 = _GL__init__.GL_MAP1_TEXTURE_COORD_3
GL_MAP1_TEXTURE_COORD_4 = _GL__init__.GL_MAP1_TEXTURE_COORD_4
GL_MAP1_VERTEX_3 = _GL__init__.GL_MAP1_VERTEX_3
GL_MAP1_VERTEX_4 = _GL__init__.GL_MAP1_VERTEX_4
GL_MAP2_COLOR_4 = _GL__init__.GL_MAP2_COLOR_4
GL_MAP2_INDEX = _GL__init__.GL_MAP2_INDEX
GL_MAP2_NORMAL = _GL__init__.GL_MAP2_NORMAL
GL_MAP2_TEXTURE_COORD_1 = _GL__init__.GL_MAP2_TEXTURE_COORD_1
GL_MAP2_TEXTURE_COORD_2 = _GL__init__.GL_MAP2_TEXTURE_COORD_2
GL_MAP2_TEXTURE_COORD_3 = _GL__init__.GL_MAP2_TEXTURE_COORD_3
GL_MAP2_TEXTURE_COORD_4 = _GL__init__.GL_MAP2_TEXTURE_COORD_4
GL_MAP2_VERTEX_3 = _GL__init__.GL_MAP2_VERTEX_3
GL_MAP2_VERTEX_4 = _GL__init__.GL_MAP2_VERTEX_4
GL_MAP1_GRID_DOMAIN = _GL__init__.GL_MAP1_GRID_DOMAIN
GL_MAP1_GRID_SEGMENTS = _GL__init__.GL_MAP1_GRID_SEGMENTS
GL_MAP2_GRID_DOMAIN = _GL__init__.GL_MAP2_GRID_DOMAIN
GL_MAP2_GRID_SEGMENTS = _GL__init__.GL_MAP2_GRID_SEGMENTS
GL_TEXTURE_1D = _GL__init__.GL_TEXTURE_1D
GL_TEXTURE_2D = _GL__init__.GL_TEXTURE_2D
GL_FEEDBACK_BUFFER_POINTER = _GL__init__.GL_FEEDBACK_BUFFER_POINTER
GL_FEEDBACK_BUFFER_SIZE = _GL__init__.GL_FEEDBACK_BUFFER_SIZE
GL_FEEDBACK_BUFFER_TYPE = _GL__init__.GL_FEEDBACK_BUFFER_TYPE
GL_SELECTION_BUFFER_POINTER = _GL__init__.GL_SELECTION_BUFFER_POINTER
GL_SELECTION_BUFFER_SIZE = _GL__init__.GL_SELECTION_BUFFER_SIZE
GL_TEXTURE_WIDTH = _GL__init__.GL_TEXTURE_WIDTH
GL_TEXTURE_HEIGHT = _GL__init__.GL_TEXTURE_HEIGHT
GL_TEXTURE_INTERNAL_FORMAT = _GL__init__.GL_TEXTURE_INTERNAL_FORMAT
GL_TEXTURE_BORDER_COLOR = _GL__init__.GL_TEXTURE_BORDER_COLOR
GL_TEXTURE_BORDER = _GL__init__.GL_TEXTURE_BORDER
GL_DONT_CARE = _GL__init__.GL_DONT_CARE
GL_FASTEST = _GL__init__.GL_FASTEST
GL_NICEST = _GL__init__.GL_NICEST
GL_LIGHT0 = _GL__init__.GL_LIGHT0
GL_LIGHT1 = _GL__init__.GL_LIGHT1
GL_LIGHT2 = _GL__init__.GL_LIGHT2
GL_LIGHT3 = _GL__init__.GL_LIGHT3
GL_LIGHT4 = _GL__init__.GL_LIGHT4
GL_LIGHT5 = _GL__init__.GL_LIGHT5
GL_LIGHT6 = _GL__init__.GL_LIGHT6
GL_LIGHT7 = _GL__init__.GL_LIGHT7
GL_AMBIENT = _GL__init__.GL_AMBIENT
GL_DIFFUSE = _GL__init__.GL_DIFFUSE
GL_SPECULAR = _GL__init__.GL_SPECULAR
GL_POSITION = _GL__init__.GL_POSITION
GL_SPOT_DIRECTION = _GL__init__.GL_SPOT_DIRECTION
GL_SPOT_EXPONENT = _GL__init__.GL_SPOT_EXPONENT
GL_SPOT_CUTOFF = _GL__init__.GL_SPOT_CUTOFF
GL_CONSTANT_ATTENUATION = _GL__init__.GL_CONSTANT_ATTENUATION
GL_LINEAR_ATTENUATION = _GL__init__.GL_LINEAR_ATTENUATION
GL_QUADRATIC_ATTENUATION = _GL__init__.GL_QUADRATIC_ATTENUATION
GL_COMPILE = _GL__init__.GL_COMPILE
GL_COMPILE_AND_EXECUTE = _GL__init__.GL_COMPILE_AND_EXECUTE
GL_CLEAR = _GL__init__.GL_CLEAR
GL_AND = _GL__init__.GL_AND
GL_AND_REVERSE = _GL__init__.GL_AND_REVERSE
GL_COPY = _GL__init__.GL_COPY
GL_AND_INVERTED = _GL__init__.GL_AND_INVERTED
GL_NOOP = _GL__init__.GL_NOOP
GL_XOR = _GL__init__.GL_XOR
GL_OR = _GL__init__.GL_OR
GL_NOR = _GL__init__.GL_NOR
GL_EQUIV = _GL__init__.GL_EQUIV
GL_INVERT = _GL__init__.GL_INVERT
GL_OR_REVERSE = _GL__init__.GL_OR_REVERSE
GL_COPY_INVERTED = _GL__init__.GL_COPY_INVERTED
GL_OR_INVERTED = _GL__init__.GL_OR_INVERTED
GL_NAND = _GL__init__.GL_NAND
GL_SET = _GL__init__.GL_SET
GL_EMISSION = _GL__init__.GL_EMISSION
GL_SHININESS = _GL__init__.GL_SHININESS
GL_AMBIENT_AND_DIFFUSE = _GL__init__.GL_AMBIENT_AND_DIFFUSE
GL_COLOR_INDEXES = _GL__init__.GL_COLOR_INDEXES
GL_MODELVIEW = _GL__init__.GL_MODELVIEW
GL_PROJECTION = _GL__init__.GL_PROJECTION
GL_TEXTURE = _GL__init__.GL_TEXTURE
GL_COLOR = _GL__init__.GL_COLOR
GL_DEPTH = _GL__init__.GL_DEPTH
GL_STENCIL = _GL__init__.GL_STENCIL
GL_COLOR_INDEX = _GL__init__.GL_COLOR_INDEX
GL_STENCIL_INDEX = _GL__init__.GL_STENCIL_INDEX
GL_DEPTH_COMPONENT = _GL__init__.GL_DEPTH_COMPONENT
GL_RED = _GL__init__.GL_RED
GL_GREEN = _GL__init__.GL_GREEN
GL_BLUE = _GL__init__.GL_BLUE
GL_ALPHA = _GL__init__.GL_ALPHA
GL_RGB = _GL__init__.GL_RGB
GL_RGBA = _GL__init__.GL_RGBA
GL_LUMINANCE = _GL__init__.GL_LUMINANCE
GL_LUMINANCE_ALPHA = _GL__init__.GL_LUMINANCE_ALPHA
GL_BITMAP = _GL__init__.GL_BITMAP
GL_POINT = _GL__init__.GL_POINT
GL_LINE = _GL__init__.GL_LINE
GL_FILL = _GL__init__.GL_FILL
GL_RENDER = _GL__init__.GL_RENDER
GL_FEEDBACK = _GL__init__.GL_FEEDBACK
GL_SELECT = _GL__init__.GL_SELECT
GL_FLAT = _GL__init__.GL_FLAT
GL_SMOOTH = _GL__init__.GL_SMOOTH
GL_KEEP = _GL__init__.GL_KEEP
GL_REPLACE = _GL__init__.GL_REPLACE
GL_INCR = _GL__init__.GL_INCR
GL_DECR = _GL__init__.GL_DECR
GL_VENDOR = _GL__init__.GL_VENDOR
GL_RENDERER = _GL__init__.GL_RENDERER
GL_VERSION = _GL__init__.GL_VERSION
GL_EXTENSIONS = _GL__init__.GL_EXTENSIONS
GL_S = _GL__init__.GL_S
GL_T = _GL__init__.GL_T
GL_R = _GL__init__.GL_R
GL_Q = _GL__init__.GL_Q
GL_MODULATE = _GL__init__.GL_MODULATE
GL_DECAL = _GL__init__.GL_DECAL
GL_TEXTURE_ENV_MODE = _GL__init__.GL_TEXTURE_ENV_MODE
GL_TEXTURE_ENV_COLOR = _GL__init__.GL_TEXTURE_ENV_COLOR
GL_TEXTURE_ENV = _GL__init__.GL_TEXTURE_ENV
GL_EYE_LINEAR = _GL__init__.GL_EYE_LINEAR
GL_OBJECT_LINEAR = _GL__init__.GL_OBJECT_LINEAR
GL_SPHERE_MAP = _GL__init__.GL_SPHERE_MAP
GL_TEXTURE_GEN_MODE = _GL__init__.GL_TEXTURE_GEN_MODE
GL_OBJECT_PLANE = _GL__init__.GL_OBJECT_PLANE
GL_EYE_PLANE = _GL__init__.GL_EYE_PLANE
GL_NEAREST = _GL__init__.GL_NEAREST
GL_LINEAR = _GL__init__.GL_LINEAR
GL_NEAREST_MIPMAP_NEAREST = _GL__init__.GL_NEAREST_MIPMAP_NEAREST
GL_LINEAR_MIPMAP_NEAREST = _GL__init__.GL_LINEAR_MIPMAP_NEAREST
GL_NEAREST_MIPMAP_LINEAR = _GL__init__.GL_NEAREST_MIPMAP_LINEAR
GL_LINEAR_MIPMAP_LINEAR = _GL__init__.GL_LINEAR_MIPMAP_LINEAR
GL_TEXTURE_MAG_FILTER = _GL__init__.GL_TEXTURE_MAG_FILTER
GL_TEXTURE_MIN_FILTER = _GL__init__.GL_TEXTURE_MIN_FILTER
GL_TEXTURE_WRAP_S = _GL__init__.GL_TEXTURE_WRAP_S
GL_TEXTURE_WRAP_T = _GL__init__.GL_TEXTURE_WRAP_T
GL_CLAMP = _GL__init__.GL_CLAMP
GL_REPEAT = _GL__init__.GL_REPEAT
GL_CLIENT_PIXEL_STORE_BIT = _GL__init__.GL_CLIENT_PIXEL_STORE_BIT
GL_CLIENT_VERTEX_ARRAY_BIT = _GL__init__.GL_CLIENT_VERTEX_ARRAY_BIT
GL_CLIENT_ALL_ATTRIB_BITS = _GL__init__.GL_CLIENT_ALL_ATTRIB_BITS
GL_POLYGON_OFFSET_FACTOR = _GL__init__.GL_POLYGON_OFFSET_FACTOR
GL_POLYGON_OFFSET_UNITS = _GL__init__.GL_POLYGON_OFFSET_UNITS
GL_POLYGON_OFFSET_POINT = _GL__init__.GL_POLYGON_OFFSET_POINT
GL_POLYGON_OFFSET_LINE = _GL__init__.GL_POLYGON_OFFSET_LINE
GL_POLYGON_OFFSET_FILL = _GL__init__.GL_POLYGON_OFFSET_FILL
GL_ALPHA4 = _GL__init__.GL_ALPHA4
GL_ALPHA8 = _GL__init__.GL_ALPHA8
GL_ALPHA12 = _GL__init__.GL_ALPHA12
GL_ALPHA16 = _GL__init__.GL_ALPHA16
GL_LUMINANCE4 = _GL__init__.GL_LUMINANCE4
GL_LUMINANCE8 = _GL__init__.GL_LUMINANCE8
GL_LUMINANCE12 = _GL__init__.GL_LUMINANCE12
GL_LUMINANCE16 = _GL__init__.GL_LUMINANCE16
GL_LUMINANCE4_ALPHA4 = _GL__init__.GL_LUMINANCE4_ALPHA4
GL_LUMINANCE6_ALPHA2 = _GL__init__.GL_LUMINANCE6_ALPHA2
GL_LUMINANCE8_ALPHA8 = _GL__init__.GL_LUMINANCE8_ALPHA8
GL_LUMINANCE12_ALPHA4 = _GL__init__.GL_LUMINANCE12_ALPHA4
GL_LUMINANCE12_ALPHA12 = _GL__init__.GL_LUMINANCE12_ALPHA12
GL_LUMINANCE16_ALPHA16 = _GL__init__.GL_LUMINANCE16_ALPHA16
GL_INTENSITY = _GL__init__.GL_INTENSITY
GL_INTENSITY4 = _GL__init__.GL_INTENSITY4
GL_INTENSITY8 = _GL__init__.GL_INTENSITY8
GL_INTENSITY12 = _GL__init__.GL_INTENSITY12
GL_INTENSITY16 = _GL__init__.GL_INTENSITY16
GL_R3_G3_B2 = _GL__init__.GL_R3_G3_B2
GL_RGB4 = _GL__init__.GL_RGB4
GL_RGB5 = _GL__init__.GL_RGB5
GL_RGB8 = _GL__init__.GL_RGB8
GL_RGB10 = _GL__init__.GL_RGB10
GL_RGB12 = _GL__init__.GL_RGB12
GL_RGB16 = _GL__init__.GL_RGB16
GL_RGBA2 = _GL__init__.GL_RGBA2
GL_RGBA4 = _GL__init__.GL_RGBA4
GL_RGB5_A1 = _GL__init__.GL_RGB5_A1
GL_RGBA8 = _GL__init__.GL_RGBA8
GL_RGB10_A2 = _GL__init__.GL_RGB10_A2
GL_RGBA12 = _GL__init__.GL_RGBA12
GL_RGBA16 = _GL__init__.GL_RGBA16
GL_TEXTURE_RED_SIZE = _GL__init__.GL_TEXTURE_RED_SIZE
GL_TEXTURE_GREEN_SIZE = _GL__init__.GL_TEXTURE_GREEN_SIZE
GL_TEXTURE_BLUE_SIZE = _GL__init__.GL_TEXTURE_BLUE_SIZE
GL_TEXTURE_ALPHA_SIZE = _GL__init__.GL_TEXTURE_ALPHA_SIZE
GL_TEXTURE_LUMINANCE_SIZE = _GL__init__.GL_TEXTURE_LUMINANCE_SIZE
GL_TEXTURE_INTENSITY_SIZE = _GL__init__.GL_TEXTURE_INTENSITY_SIZE
GL_PROXY_TEXTURE_1D = _GL__init__.GL_PROXY_TEXTURE_1D
GL_PROXY_TEXTURE_2D = _GL__init__.GL_PROXY_TEXTURE_2D
GL_TEXTURE_PRIORITY = _GL__init__.GL_TEXTURE_PRIORITY
GL_TEXTURE_RESIDENT = _GL__init__.GL_TEXTURE_RESIDENT
GL_TEXTURE_BINDING_1D = _GL__init__.GL_TEXTURE_BINDING_1D
GL_TEXTURE_BINDING_2D = _GL__init__.GL_TEXTURE_BINDING_2D
GL_VERTEX_ARRAY = _GL__init__.GL_VERTEX_ARRAY
GL_NORMAL_ARRAY = _GL__init__.GL_NORMAL_ARRAY
GL_COLOR_ARRAY = _GL__init__.GL_COLOR_ARRAY
GL_INDEX_ARRAY = _GL__init__.GL_INDEX_ARRAY
GL_TEXTURE_COORD_ARRAY = _GL__init__.GL_TEXTURE_COORD_ARRAY
GL_EDGE_FLAG_ARRAY = _GL__init__.GL_EDGE_FLAG_ARRAY
GL_VERTEX_ARRAY_SIZE = _GL__init__.GL_VERTEX_ARRAY_SIZE
GL_VERTEX_ARRAY_TYPE = _GL__init__.GL_VERTEX_ARRAY_TYPE
GL_VERTEX_ARRAY_STRIDE = _GL__init__.GL_VERTEX_ARRAY_STRIDE
GL_NORMAL_ARRAY_TYPE = _GL__init__.GL_NORMAL_ARRAY_TYPE
GL_NORMAL_ARRAY_STRIDE = _GL__init__.GL_NORMAL_ARRAY_STRIDE
GL_COLOR_ARRAY_SIZE = _GL__init__.GL_COLOR_ARRAY_SIZE
GL_COLOR_ARRAY_TYPE = _GL__init__.GL_COLOR_ARRAY_TYPE
GL_COLOR_ARRAY_STRIDE = _GL__init__.GL_COLOR_ARRAY_STRIDE
GL_INDEX_ARRAY_TYPE = _GL__init__.GL_INDEX_ARRAY_TYPE
GL_INDEX_ARRAY_STRIDE = _GL__init__.GL_INDEX_ARRAY_STRIDE
GL_TEXTURE_COORD_ARRAY_SIZE = _GL__init__.GL_TEXTURE_COORD_ARRAY_SIZE
GL_TEXTURE_COORD_ARRAY_TYPE = _GL__init__.GL_TEXTURE_COORD_ARRAY_TYPE
GL_TEXTURE_COORD_ARRAY_STRIDE = _GL__init__.GL_TEXTURE_COORD_ARRAY_STRIDE
GL_EDGE_FLAG_ARRAY_STRIDE = _GL__init__.GL_EDGE_FLAG_ARRAY_STRIDE
GL_VERTEX_ARRAY_POINTER = _GL__init__.GL_VERTEX_ARRAY_POINTER
GL_NORMAL_ARRAY_POINTER = _GL__init__.GL_NORMAL_ARRAY_POINTER
GL_COLOR_ARRAY_POINTER = _GL__init__.GL_COLOR_ARRAY_POINTER
GL_INDEX_ARRAY_POINTER = _GL__init__.GL_INDEX_ARRAY_POINTER
GL_TEXTURE_COORD_ARRAY_POINTER = _GL__init__.GL_TEXTURE_COORD_ARRAY_POINTER
GL_EDGE_FLAG_ARRAY_POINTER = _GL__init__.GL_EDGE_FLAG_ARRAY_POINTER
GL_V2F = _GL__init__.GL_V2F
GL_V3F = _GL__init__.GL_V3F
GL_C4UB_V2F = _GL__init__.GL_C4UB_V2F
GL_C4UB_V3F = _GL__init__.GL_C4UB_V3F
GL_C3F_V3F = _GL__init__.GL_C3F_V3F
GL_N3F_V3F = _GL__init__.GL_N3F_V3F
GL_C4F_N3F_V3F = _GL__init__.GL_C4F_N3F_V3F
GL_T2F_V3F = _GL__init__.GL_T2F_V3F
GL_T4F_V4F = _GL__init__.GL_T4F_V4F
GL_T2F_C4UB_V3F = _GL__init__.GL_T2F_C4UB_V3F
GL_T2F_C3F_V3F = _GL__init__.GL_T2F_C3F_V3F
GL_T2F_N3F_V3F = _GL__init__.GL_T2F_N3F_V3F
GL_T2F_C4F_N3F_V3F = _GL__init__.GL_T2F_C4F_N3F_V3F
GL_T4F_C4F_N3F_V4F = _GL__init__.GL_T4F_C4F_N3F_V4F
GL_LOGIC_OP = _GL__init__.GL_LOGIC_OP
GL_TEXTURE_COMPONENTS = _GL__init__.GL_TEXTURE_COMPONENTS
def __info():
	import string
	return [('GL_VERSION', GL_VERSION, 'sg'),
	        ('GL_VENDOR', GL_VENDOR, 'sg'),
	        ('GL_RENDERER', GL_RENDERER, 'sg'),
	        ('GL_EXTENSIONS', GL_EXTENSIONS, 'eg'),
	        ('GL_MAX_CLIENT_ATTRIB_STACK_DEPTH', GL_MAX_CLIENT_ATTRIB_STACK_DEPTH, 'i'),
	        ('GL_MAX_ATTRIB_STACK_DEPTH', GL_MAX_ATTRIB_STACK_DEPTH, 'i'),
	        ('GL_MAX_CLIP_PLANES', GL_MAX_CLIP_PLANES, 'i'),
	        ('GL_MAX_EVAL_ORDER', GL_MAX_EVAL_ORDER, 'i'),
	        ('GL_MAX_LIGHTS', GL_MAX_LIGHTS, 'i'),
	        ('GL_MAX_LIST_NESTING', GL_MAX_LIST_NESTING, 'i'),
	        ('GL_MAX_MODELVIEW_STACK_DEPTH', GL_MAX_MODELVIEW_STACK_DEPTH, 'i'),
	        ('GL_MAX_NAME_STACK_DEPTH', GL_MAX_NAME_STACK_DEPTH, 'i'),
	        ('GL_MAX_PIXEL_MAP_TABLE', GL_MAX_PIXEL_MAP_TABLE, 'i'),
	        ('GL_MAX_PROJECTION_STACK_DEPTH', GL_MAX_PROJECTION_STACK_DEPTH, 'i'),
	        ('GL_MAX_TEXTURE_SIZE', GL_MAX_TEXTURE_SIZE, 'i'),
	        ('GL_MAX_TEXTURE_STACK_DEPTH', GL_MAX_TEXTURE_STACK_DEPTH, 'i'),
	        ('GL_MAX_VIEWPORT_DIMS', GL_MAX_VIEWPORT_DIMS, 'i')]

GLerror = _GL__init__.GLerror

__numeric_present__ = _GL__init__.__numeric_present__
__numeric_support__ = _GL__init__.__numeric_support__

try:
	import Numeric
except ImportError:
	def contiguous( source ):
		"""Place-holder for contiguous-array function, just returns argument

		This is only visible if Numeric Python is not installed
		"""
		return source
else:
	def contiguous( source, typecode=None ):
		"""Get contiguous array from source
		
		source -- Numeric Python array (or compatible object)
			for use as the data source.  If this is not a contiguous
			array of the given typecode, a copy will be made, 
			otherwise will just be returned unchanged.
		typecode -- optional 1-character typecode specifier for
			the Numeric.array function.
			
		All gl*Pointer calls should use contiguous arrays, as non-
		contiguous arrays will be re-copied on every rendering pass.
		Although this doesn't raise an error, it does tend to slow
		down rendering.
		"""
		if isinstance( source, Numeric.ArrayType):
			if source.iscontiguous() and (typecode is None or typecode==source.typecode()):
				return source
			else:
				return Numeric.array(source,typecode or source.typecode())
		elif typecode:
			return Numeric.array( source, typecode )
		else:
			return Numeric.array( source )



