/*
# BUILD api_versions [0x100, 0x101]
# BUILD macro_template 'defined(GL_VERSION_%(api_version_underscore)s)'
# BUILD shadow 1
*/

%module GL__init__

#define __version__ "$Revision: 1.3.2.3 $"
#define __date__ "$Date: 2004/11/14 23:19:04 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>\nMike C. Fletcher <mcfletch@users.sourceforge.net>"
#define __doc__ "For general information about OpenGL, including documentation, see http:\057\057www.opengl.org\n\
\n\
Other sites that might be useful include:\n\
    MSDN:  http:\057\057msdn.microsoft.com/library/default.asp?url=/library/en-us/opengl/hh/opengl/openglstart_9uw5.asp?frame=true\n\
    Mesa3d:  http:\057\057www.mesa3d.org\n\
    OpenGL at Apple:  http:\057\057developer.apple.com/opengl"

/*
# GL Module for PyOpenGL
#  
# Date: May 2001
# 
# Authors: Tarn Weisner Burton <twburton@users.sourceforge.net>
#          Mike C. Fletcher
*/

/* License from SGI's OpenGL® Sample Implementation */

/*
# License Applicability. Except to the extent portions of this file are
# made subject to an alternative license as permitted in the SGI Free
# Software License B, Version 1.1 (the "License"), the contents of this
# file are subject only to the provisions of the License. You may not use
# this file except in compliance with the License. You may obtain a copy
# of the License at Silicon Graphics, Inc., attn: Legal Services, 1600
# Amphitheatre Parkway, Mountain View, CA 94043-1351, or at:
#
# http://oss.sgi.com/projects/FreeB
#
# Note that, as provided in the License, the Software is distributed on an
# "AS IS" basis, with ALL EXPRESS AND IMPLIED WARRANTIES AND CONDITIONS
# DISCLAIMED, INCLUDING, WITHOUT LIMITATION, ANY IMPLIED WARRANTIES AND
# CONDITIONS OF MERCHANTABILITY, SATISFACTORY QUALITY, FITNESS FOR A
# PARTICULAR PURPOSE, AND NON-INFRINGEMENT.
#
# Original Code. The Original Code is: OpenGL Sample Implementation,
# Version 1.2.1, released January 26, 2000, developed by Silicon Graphics,
# Inc. The Original Code is Copyright (c) 1991-2000 Silicon Graphics, Inc.
# Copyright in any portions created by third parties is as indicated
# elsewhere herein. All Rights Reserved.
#
# Additional Notice Provisions: The application programming interfaces
# established by SGI in conjunction with the Original Code are The
# OpenGL(R) Graphics System: A Specification (Version 1.2.1), released
# April 1, 1999; The OpenGL(R) Graphics System Utility Library (Version
# 1.3), released November 4, 1998; and OpenGL(R) Graphics with the X
# Window System(R) (Version 1.3), released October 19, 1998. This software
# was created using the OpenGL(R) version 1.2.1 Sample Implementation
# published by SGI, but has not been independently verified as being
# compliant with the OpenGL(R) version 1.2.1 Specification.
*/

/*************************************************************/
/*** FUNCTIONS                                               */

#define EXPORT_UTIL

%include util.inc

%init %{
PyDict_SetItemString(d, "GLerror", GLerror);
%}



%shadow %{
from operator import isSequenceType
%}


/* These are functions that are called between glBegin and glEnd and do not need a GL exception handler */
/* turn the normal exception handler on */
%include py_exception_handler.inc


/*
# glArrayElement
# 
# Python binding unchanged from spec.
*/

void glArrayElement(GLint i);
DOC(glArrayElement, "glArrayElement(i) -> None")


/*
# glBegin
#
# Python binding unchanged from spec
*/

void glBegin(GLenum mode);
DOC(glBegin, "glBegin(mode) -> None")


/*
# glCallList
#
# Python binding unchanged from spec
*/

void glCallList(GLuint list);
DOC(glCallList, "glCallList(list) -> None")


/*
# glCallLists
#
# void glCallLists(GLsizei n, GLenum type, const GLuint *lists)
#
# "n" parameter is automatically determined from the lists argument
# "type" is always set to GL_UNSIGNED_INT since "lists" is cast to unsigned int
*/

void glCallLists(GLsizei n_1, GLenum type_UNSIGNED_INT, const GLuint *lists);
DOC(glCallLists, "glCallLists(lists[]) -> None")


/*
# glColorX
#
# Python binding unchanged from spec, except that the undecorated
# utility functions are provided
*/

void glColor3b(GLbyte red, GLbyte green, GLbyte blue);
DOC(glColor3b, "glColor3b(red, green, blue) -> None")

void glColor3bv(const GLbyte *v);
DOC(glColor3bv, "glColor3bv(v) -> None")

void glColor3d(GLdouble red, GLdouble green, GLdouble blue);
DOC(glColor3d, "glColor3d(red, green, blue) -> None")

void glColor3dv(const GLdouble *v);
DOC(glColor3dv, "glColor3dv(v) -> None")

void glColor3f(GLfloat red, GLfloat green, GLfloat blue);
DOC(glColor3f, "glColor3f(red, green, blue) -> None")

void glColor3fv(const GLfloat *v);
DOC(glColor3fv, "glColor3fv(v) -> None")

void glColor3i(GLint red, GLint green, GLint blue);
DOC(glColor3i, "glColor3i(red, green, blue) -> None")

void glColor3iv(const GLint *v);
DOC(glColor3iv, "glColor3iv(v) -> None")

void glColor3s(GLshort red, GLshort green, GLshort blue);
DOC(glColor3s, "glColor3s(red, green, blue) -> None")

void glColor3sv(const GLshort *v);
DOC(glColor3sv, "glColor3sv(v) -> None")

void glColor3ub(GLubyte red, GLubyte green, GLubyte blue);
DOC(glColor3ub, "glColor3ub(red, green, blue) -> None")

void glColor3ubv(const GLubyte *v);
DOC(glColor3ubv, "glColor3ubv(v) -> None")

void glColor3ui(GLuint red, GLuint green, GLuint blue);
DOC(glColor3ui, "glColor3ui(red, green, blue) -> None")

void glColor3uiv(const GLuint *v);
DOC(glColor3uiv, "glColor3uiv(v) -> None")

void glColor3us(GLushort red, GLushort green, GLushort blue);
DOC(glColor3us, "glColor3us(red, green, blue) -> None")

void glColor3usv(const GLushort *v);
DOC(glColor3usv, "glColor3usv(v) -> None")

void glColor4b(GLbyte red, GLbyte green, GLbyte blue, GLbyte alpha);
DOC(glColor4b, "glColor4b(red, green, blue) -> None")

void glColor4bv(const GLbyte *v);
DOC(glColor4bv, "glColor4bv(v) -> None")

void glColor4d(GLdouble red, GLdouble green, GLdouble blue, GLdouble alpha);
DOC(glColor4d, "glColor4d(red, green, blue) -> None")

void glColor4dv(const GLdouble *v);
DOC(glColor4dv, "glColor4dv(v) -> None")

void glColor4f(GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha);
DOC(glColor4f, "glColor4f(red, green, blue) -> None")

void glColor4fv(const GLfloat *v);
DOC(glColor4fv, "glColor4fv(v) -> None")

void glColor4i(GLint red, GLint green, GLint blue, GLint alpha);
DOC(glColor4i, "glColor4i(red, green, blue) -> None")

void glColor4iv(const GLint *v);
DOC(glColor4iv, "glColor4iv(v) -> None")

void glColor4s(GLshort red, GLshort green, GLshort blue, GLshort alpha);
DOC(glColor4s, "glColor4s(red, green, blue) -> None")

void glColor4sv(const GLshort *v);
DOC(glColor4sv, "glColor4sv(v) -> None")

void glColor4ub(GLubyte red, GLubyte green, GLubyte blue, GLubyte alpha);
DOC(glColor4ub, "glColor4ub(red, green, blue) -> None")

void glColor4ubv(const GLubyte *v);
DOC(glColor4ubv, "glColor4ubv(v) -> None")

void glColor4ui(GLuint red, GLuint green, GLuint blue, GLuint alpha);
DOC(glColor4ui, "glColor4ui(red, green, blue) -> None")

void glColor4uiv(const GLuint *v);
DOC(glColor4uiv, "glColor4uiv(v) -> None")

void glColor4us(GLushort red, GLushort green, GLushort blue, GLushort alpha);
DOC(glColor4us, "glColor4us(red, green, blue) -> None")

void glColor4usv(const GLushort *v);
DOC(glColor4usv, "glColor4usv(v) -> None")




%shadow %{
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

%}






/*
# glEdgeFlag
#
# Python binding unchanged from spec
*/

void glEdgeFlag(GLboolean flag);
DOC(glEdgeFlag, "glEdgeFlag(flag) -> None")

void glEdgeFlagv(const GLboolean *flag);
DOC(glEdgeFlagv, "glEdgeFlagv(flag) -> None")


/*
# glEvalCoord
#
# Python binding unchanged from spec, except that the undecorated
# utility functions are provided
*/

void glEvalCoord1d(GLdouble u);
DOC(glEvalCoord1d, "glEvalCoord1d(u) -> None")

void glEvalCoord1dv(const GLdouble *v);
DOC(glEvalCoord1dv, "glEvalCoord1dv(v) -> None")

void glEvalCoord1f(GLfloat u);
DOC(glEvalCoord1f, "glEvalCoord1f(u) -> None")

void glEvalCoord1fv(const GLfloat *v);
DOC(glEvalCoord1fv, "glEvalCoord1fv(v) -> None")

void glEvalCoord2d(GLdouble u, GLdouble v);
DOC(glEvalCoord2d, "glEvalCoord2d(u, v) -> None")

void glEvalCoord2dv(const GLdouble *v);
DOC(glEvalCoord2dv, "glEvalCoord2dv(v) -> None")

void glEvalCoord2f(GLfloat u, GLfloat v);
DOC(glEvalCoord2f, "glEvalCoord2f(u, v) -> None")

void glEvalCoord2fv(const GLfloat *v);
DOC(glEvalCoord2fv, "glEvalCoord2fv(v) -> None")


%shadow %{
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

%}










/*
# glEvalPoint
#
# Python binding unchanged from spec, except that the undecorated
# utility functions are provided
*/

void glEvalPoint1(GLint i);
DOC(glEvalPoint1, "glEvalPoint1(i) -> None")

void glEvalPoint2(GLint i, GLint j);
DOC(glEvalPoint2, "glEvalPoint2(i, j) -> None")


%shadow %{
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

%}


/*
# glIndex
#
# Python binding unchanged from spec.
*/

void glIndexd(GLdouble c);
DOC(glIndexd, "glIndexd(c) -> None")

void glIndexdv(const GLdouble *c);
DOC(glIndexdv, "glIndexdv(c) -> None")

void glIndexf(GLfloat c);
DOC(glIndexf, "glIndexf(d) -> None")

void glIndexfv(const GLfloat *c);
DOC(glIndexfv, "glIndexfv(c) -> None")

void glIndexi(GLint c);
DOC(glIndexi, "glIndexi(c) -> None")

void glIndexiv(const GLint *c);
DOC(glIndexiv, "glIndexiv(c) -> None")

void glIndexs(GLshort c);
DOC(glIndexs, "glIndexs(c) -> None")

void glIndexsv(const GLshort *c);
DOC(glIndexsv, "glIndexsv(c) -> None")

void glIndexub(GLubyte c);
DOC(glIndexub, "glIndexub(c) -> None")

void glIndexubv(const GLubyte *c);
DOC(glIndexubv, "glIndexubv(c) -> None")


%shadow %{
glIndex = _GL__init__.glIndexd
%}


/*
# glMaterial
#
# Technically the Python binding is unchanged from spec, but
# in reality the glMaterial{f|i}v is more forgiving than the
# spec function since the array typemap will accept a scalar
# turning glMaterial{f|i}v into glMaterial{f|i}.
#
# The backwards compatibility alias glMaterial is also provided.
*/

void glMaterialf(GLenum face, GLenum pname, GLfloat param);
DOC(glMaterialf, "glMaterialf(face, pname, param) -> None")

void glMaterialfv(GLenum face, GLenum pname, const GLfloat *params);
DOC(glMaterialfv, "glMaterialfv(face, pname, params[]) -> None")

void glMateriali(GLenum face, GLenum pname, GLint param);
DOC(glMateriali, "glMateriali(face, pname, param) -> None")

void glMaterialiv(GLenum face, GLenum pname, const GLint *params);
DOC(glMaterialiv, "glMaterialiv(face, pname, params[]) -> None")


%shadow %{
glMaterial = _GL__init__.glMaterialfv
%}





/*
# glNormal
#
# Python binding unchanged from spec, except that the undecorated
# utility functions are provided
*/

void glNormal3b(GLbyte nx, GLbyte ny, GLbyte nz);
DOC(glNormal3b, "glNormal3b(nx, ny, nz) -> None")

void glNormal3bv(const GLbyte *v);
DOC(glNormal3bv, "glNormal3bv(v) -> None")

void glNormal3d(GLdouble nx, GLdouble ny, GLdouble nz);
DOC(glNormal3d, "glNormal3d(nx, ny, nz) -> None")

void glNormal3dv(const GLdouble *v);
DOC(glNormal3dv, "glNormal3dv(v) -> None")

void glNormal3f(GLfloat nx, GLfloat ny, GLfloat nz);
DOC(glNormal3f, "glNormal3f(nx, ny, nz) -> None")

void glNormal3fv(const GLfloat *v);
DOC(glNormal3fv, "glNormal3fv(v) -> None")

void glNormal3i(GLint nx, GLint ny, GLint nz);
DOC(glNormal3i, "glNormal3i(nx, ny, nz) -> None")

void glNormal3iv(const GLint *v);
DOC(glNormal3iv, "glNormal3iv(v) -> None")

void glNormal3s(GLshort nx, GLshort ny, GLshort nz);
DOC(glNormal3s, "glNormal3s(nx, ny, nz) -> None")

void glNormal3sv(const GLshort *v);
DOC(glNormal3sv, "glNormal3sv(v) -> None")

%shadow %{
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
%}






/*
# glTexCoord
#
# Python binding unchanged from spec, except that the undecorated
# utility functions are provided
*/

void glTexCoord1d(GLdouble s);
DOC(glTexCoord1d, "glTexCoord1d(s) -> None")

void glTexCoord1dv(const GLdouble *v);
DOC(glTexCoord1dv, "glTexCoord1dv(v) -> None")

void glTexCoord1f(GLfloat s);
DOC(glTexCoord1f, "glTexCoord1f(s) -> None")

void glTexCoord1fv(const GLfloat *v);
DOC(glTexCoord1fv, "glTexCoord1fv(v) -> None")

void glTexCoord1i(GLint s);
DOC(glTexCoord1i, "glTexCoord1i(s) -> None")

void glTexCoord1iv(const GLint *v);
DOC(glTexCoord1iv, "glTexCoord1iv(v) -> None")

void glTexCoord1s(GLshort s);
DOC(glTexCoord1s, "glTexCoord1s(s) -> None")

void glTexCoord1sv(const GLshort *v);
DOC(glTexCoord1sv, "glTexCoord1sv(v) -> None")

void glTexCoord2d(GLdouble s, GLdouble t);
DOC(glTexCoord2d, "glTexCoord2d(s, t) -> None")

void glTexCoord2dv(const GLdouble *v);
DOC(glTexCoord2dv, "glTexCoord2dv(v) -> None")

void glTexCoord2f(GLfloat s, GLfloat t);
DOC(glTexCoord2f, "glTexCoord2f(s, t) -> None")

void glTexCoord2fv(const GLfloat *v);
DOC(glTexCoord2fv, "glTexCoord2fv(v) -> None")

void glTexCoord2i(GLint s, GLint t);
DOC(glTexCoord2i, "glTexCoord2i(s, t) -> None")

void glTexCoord2iv(const GLint *v);
DOC(glTexCoord2iv, "glTexCoord2iv(v) -> None")

void glTexCoord2s(GLshort s, GLshort t);
DOC(glTexCoord2s, "glTexCoord2s(s, t) -> None")

void glTexCoord2sv(const GLshort *v);
DOC(glTexCoord2sv, "glTexCoord2sv(v) -> None")

void glTexCoord3d(GLdouble s, GLdouble t, GLdouble r);
DOC(glTexCoord3d, "glTexCoord3d(s, t, r) -> None")

void glTexCoord3dv(const GLdouble *v);
DOC(glTexCoord3dv, "glTexCoord3dv(v) -> None")

void glTexCoord3f(GLfloat s, GLfloat t, GLfloat r);
DOC(glTexCoord3f, "glTexCoord3f(s, t, r) -> None")

void glTexCoord3fv(const GLfloat *v);
DOC(glTexCoord3fv, "glTexCoord3fv(v) -> None")

void glTexCoord3i(GLint s, GLint t, GLint r);
DOC(glTexCoord3i, "glTexCoord3i(s, t, r) -> None")

void glTexCoord3iv(const GLint *v);
DOC(glTexCoord3iv, "glTexCoord3iv(v) -> None")

void glTexCoord3s(GLshort s, GLshort t, GLshort r);
DOC(glTexCoord3s, "glTexCoord3s(s, t, r) -> None")

void glTexCoord3sv(const GLshort *v);
DOC(glTexCoord3sv, "glTexCoord3sv(v) -> None")

void glTexCoord4d(GLdouble s, GLdouble t, GLdouble r, GLdouble q);
DOC(glTexCoord4d, "glTexCoord4d(s, t, r, q) -> None")

void glTexCoord4dv(const GLdouble *v);
DOC(glTexCoord4dv, "glTexCoord4dv(v) -> None")

void glTexCoord4f(GLfloat s, GLfloat t, GLfloat r, GLfloat q);
DOC(glTexCoord4f, "glTexCoord4f(s, t, r, q) -> None")

void glTexCoord4fv(const GLfloat *v);
DOC(glTexCoord4fv, "glTexCoord4fv(v) -> None")

void glTexCoord4i(GLint s, GLint t, GLint r, GLint q);
DOC(glTexCoord4i, "glTexCoord4i(s, t, r, q) -> None")

void glTexCoord4iv(const GLint *v);
DOC(glTexCoord4iv, "glTexCoord4iv(v) -> None")

void glTexCoord4s(GLshort s, GLshort t, GLshort r, GLshort q);
DOC(glTexCoord4s, "glTexCoord4s(s, t, r, q) -> None")

void glTexCoord4sv(const GLshort *v);
DOC(glTexCoord4sv, "glTexCoord4sv(v) -> None")



%shadow %{
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
%}



/*
# glVertex
#
# Python binding unchanged from spec, except that the undecorated
# utility functions are provided
*/

void glVertex2d(GLdouble x, GLdouble y);
DOC(glVertex2d, "glVertex2d(x, y) -> None")

void glVertex2dv(const GLdouble *v);
DOC(glVertex2dv, "glVertex2dv(v) -> None")

void glVertex2f(GLfloat x, GLfloat y);
DOC(glVertex2f, "glVertex2f(x, y) -> None")

void glVertex2fv(const GLfloat *v);
DOC(glVertex2fv, "glVertex2fv(v) -> None")

void glVertex2i(GLint x, GLint y);
DOC(glVertex2i, "glVertex2i(x, y) -> None")

void glVertex2iv(const GLint *v);
DOC(glVertex2iv, "glVertex2iv(v) -> None")

void glVertex2s(GLshort x, GLshort y);
DOC(glVertex2s, "glVertex2s(x, y) -> None")

void glVertex2sv(const GLshort *v);
DOC(glVertex2sv, "glVertex2sv(v) -> None")

void glVertex3d(GLdouble x, GLdouble y, GLdouble z);
DOC(glVertex3d, "glVertex3d(x, y, z) -> None")

void glVertex3dv(const GLdouble *v);
DOC(glVertex3dv, "glVertex3dv(v) -> None")

void glVertex3f(GLfloat x, GLfloat y, GLfloat z);
DOC(glVertex3f, "glVertex3f(x, y, z) -> None")

void glVertex3fv(const GLfloat *v);
DOC(glVertex3fv, "glVertex3fv(v) -> None")

void glVertex3i(GLint x, GLint y, GLint z);
DOC(glVertex3i, "glVertex3i(x, y, z) -> None")

void glVertex3iv(const GLint *v);
DOC(glVertex3iv, "glVertex3iv(v) -> None")

void glVertex3s(GLshort x, GLshort y, GLshort z);
DOC(glVertex3s, "glVertex3s(x, y, z) -> None")

void glVertex3sv(const GLshort *v);
DOC(glVertex3sv, "glVertex3sv(v) -> None")

void glVertex4d(GLdouble x, GLdouble y, GLdouble z, GLdouble w);
DOC(glVertex4d, "glVertex4d(x, y, z, w) -> None")

void glVertex4dv(const GLdouble *v);
DOC(glVertex4dv, "glVertex4dv(v) -> None")

void glVertex4f(GLfloat x, GLfloat y, GLfloat z, GLfloat w);
DOC(glVertex4f, "glVertex4f(x, y, z, w) -> None")

void glVertex4fv(const GLfloat *v);
DOC(glVertex4fv, "glVertex4fv(v) -> None")

void glVertex4i(GLint x, GLint y, GLint z, GLint w);
DOC(glVertex4i, "glVertex4i(x, y, z, w) -> None")

void glVertex4iv(const GLint *v);
DOC(glVertex4iv, "glVertex4iv(v) -> None")

void glVertex4s(GLshort x, GLshort y, GLshort z, GLshort w);
DOC(glVertex4s, "glVertex4s(x, y, z, w) -> None")

void glVertex4sv(const GLshort *v);
DOC(glVertex4sv, "glVertex4sv(v) -> None")



%shadow %{
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
%}




/* turn the exception handler on */
%include gl_exception_handler.inc


%name(__has_extension) int has_extension(const char* name);
DOC(__has_extension, "Private function:  use appropriate extension initialization function instead.")


/*
# glAccum
# 
# Python binding unchanged from spec.
*/

void glAccum(GLenum op, GLfloat value);
DOC(glAccum, "glAccum(op, value) -> None")

void glAlphaFunc(GLenum func, GLclampf ref);
DOC(glAlphaFunc, "glAlphaFunc(func, ref) -> None")


/*
# glAreTexturesResident
# 
# The Python binding returns the "residences" instead of taking it
# as a function parameter.
*/

%{
PyObject* _glAreTexturesResident(GLsizei n, const GLuint *textures)
{
	GLboolean *residences = PyMem_New(GLboolean, n);
	PyObject *result;
	
	glAreTexturesResident(n, textures, residences);
	result = _PyTuple_FromUnsignedCharArray(n, residences);
	
	PyMem_Del(residences);
	return result;
}
%}

%name(glAreTexturesResident) PyObject* _glAreTexturesResident(GLsizei n_1, const GLuint *textures);
DOC(glAreTexturesResident, "glAreTexturesResident(textures[]) -> residences")


/*
# glBindTexture
# 
# Python binding unchanged from spec.
*/

void glBindTexture(GLenum target, GLuint texture);
DOC(glBindTexture, "glBindTexture(target, texture) -> None")


/*
# glBitmap
# 
# Python binding unchanged from spec.
*/

void glBitmap(GLsizei width, GLsizei height, GLfloat xorig, GLfloat yorig, GLfloat xmove, GLfloat ymove, const GLubyte *bitmap);
DOC(glBitmap, "glBitmap(width, height, xorig, yorig, xmove, ymove, bitmap) -> None")


/*
# glBlendFunc
# 
# Python binding unchanged from spec.
*/

void glBlendFunc(GLenum sfactor, GLenum dfactor);
DOC(glBlendFunc, "glBlendFunc(sfactor, dfactor) -> None")


/*
# glClear
# 
# Python binding unchanged from spec.
*/

void glClear(GLbitfield mask);
DOC(glClear, "glClear(mask) -> None")


/*
# glClearAccum
# 
# Python binding unchanged from spec.
*/

void glClearAccum(GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha);
DOC(glClearAccum, "glClearAccum(red, green, blue, alpha) -> None")


/*
# glClearColor
# 
# Python binding unchanged from spec.
*/

void glClearColor(GLclampf red, GLclampf green, GLclampf blue, GLclampf alpha);
DOC(glClearColor, "glClearColor(red, green, blue, alpha) -> None")


/*
# glClearDepth
# 
# Python binding unchanged from spec.
*/

void glClearDepth(GLclampd depth);
DOC(glClearDepth, "glClearDepth(depth) -> None")


/*
# glClearIndex
# 
# Python binding unchanged from spec.
*/

void glClearIndex(GLfloat c);
DOC(glClearIndex, "glClearIndex(c) -> None")


/*
# glClearStencil
# 
# Python binding unchanged from spec.
*/

void glClearStencil(GLint s);
DOC(glClearStencil, "glClearStencil(s) -> None")


/*
# glClipPlane
# 
# Python binding unchanged from spec.
*/

void glClipPlane(GLenum plane, const GLdouble *equation);
DOC(glClipPlane, "glClipPlane(plane, equation[]) -> None")


/*
# glColorMask
# 
# Python binding unchanged from spec.
*/

void glColorMask(GLboolean red, GLboolean green, GLboolean blue, GLboolean alpha);
DOC(glColorMask, "glColorMask(red, gree, blue, alpha) -> None")


/*
# glColorMaterial
# 
# Python binding unchanged from spec.
*/

void glColorMaterial(GLenum face, GLenum mode);
DOC(glColorMaterial, "glColorMaterial(face, mode) -> None")


/*
# glColorPointer
# 
# The glColorPointer function is unchanged from the spec, but the
# Python binding adds the decorated variants which take a multidimensional
# array as the data source and set the "size", "type", and "stride"
# arguments as appropriate.
*/

#if API_VERSION > 256
%{
void _glColorPointer(GLint size, GLenum type, GLsizei stride, GLvoid *pointer)
{
	decrementPointerLock(GL_COLOR_ARRAY_POINTER);
	acquire(pointer);
	glColorPointer(size, type, stride, pointer);
}
%}

%name(glColorPointer) void _glColorPointer(GLint size, GLenum type, GLsizei stride, void *pointer);
DOC(glColorPointer, "glColorPointer(size, type, stride, pointer) -> None")

%name(glColorPointerub) void _glColorPointer(GLint d_3_1, GLenum type_UNSIGNED_BYTE, GLsizei stride_0, GLubyte* pointer);
DOC(glColorPointerub, "glColorPointerub(pointer[][]) -> None")

%name(glColorPointerb) void _glColorPointer(GLint d_3_1, GLenum type_BYTE, GLsizei stride_0, GLbyte* pointer);
DOC(glColorPointerb, "glColorPointerb(pointer[][]) -> None")

%name(glColorPointerus) void _glColorPointer(GLint d_3_1, GLenum type_UNSIGNED_SHORT, GLsizei stride_0, GLushort* pointer);
DOC(glColorPointerus, "glColorPointerus(pointer[][]) -> None")

%name(glColorPointers) void _glColorPointer(GLint d_3_1, GLenum type_SHORT, GLsizei stride_0, GLshort* pointer);
DOC(glColorPointers, "glColorPointers(pointer[][]) -> None")

%name(glColorPointerui) void _glColorPointer(GLint d_3_1, GLenum type_UNSIGNED_INT, GLsizei stride_0, GLuint* pointer);
DOC(glColorPointerui, "glColorPointerui(pointer[][]) -> None")

%name(glColorPointeri) void _glColorPointer(GLint d_3_1, GLenum type_INT, GLsizei stride_0, GLint* pointer);
DOC(glColorPointeri, "glColorPointeri(pointer[][]) -> None")

%name(glColorPointerf) void _glColorPointer(GLint d_3_1, GLenum type_FLOAT, GLsizei stride_0, GLfloat *pointer);
DOC(glColorPointerf, "glColorPointerf(pointer[][]) -> None")

%name(glColorPointerd) void _glColorPointer(GLint d_3_1, GLenum type_DOUBLE, GLsizei stride_0, GLdouble *pointer);
DOC(glColorPointerd, "glColorPointerd(pointer[][]) -> None")
#endif


/*
# glCopyPixels
# 
# Python binding unchanged from spec.
*/

void glCopyPixels(GLint x, GLint y, GLsizei width, GLsizei height, GLenum type);
DOC(glCopyPixels, "glCopyPixels(x, y, width, height, type) -> None")


/*
# glCopyTexImage
# 
# Python binding unchanged from spec.
*/

void glCopyTexImage1D(GLenum target, GLint level, GLenum internalFormat, GLint x, GLint y, GLsizei width, GLint border);
DOC(glCopyTexImage1D, "glCopyTexImage1D(target, level, internalFormat, x, y, width, border) -> None")

void glCopyTexImage2D(GLenum target, GLint level, GLenum internalFormat, GLint x, GLint y, GLsizei width, GLsizei height, GLint border);
DOC(glCopyTexImage2D, "glCopyTexImage2D(target, level, internalFormat, x, y, width, height, border) -> None")


/*
# glCopyTexSubImage
# 
# Python binding unchanged from spec.
*/

void glCopyTexSubImage1D(GLenum target, GLint level, GLint xoffset, GLint x, GLint y, GLsizei width);
DOC(glCopyTexSubImage1D, "glCopyTexSubImage1D(target, level, xoffset, x, y, width) -> None")

void glCopyTexSubImage2D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei width, GLsizei height);
DOC(glCopyTexSubImage2D, "glCopyTexSubImage2D(target, level, xoffset, yoffset, x, y, width, height) -> None")


/*
# glCullFace
# 
# Python binding unchanged from spec.
*/

void glCullFace(GLenum mode);
DOC(glCullFace, "glCullFace(mode) -> None")


/*
# glDeleteLists
# 
# Python binding unchanged from spec.
*/

void glDeleteLists(GLuint list, GLsizei range);
DOC(glDeleteLists, "glDeleteLists(list, range) -> None")


/*
# glColorMaterial
# 
# The "n" parameter of the C prototype is not needed
# since the Python binding automatically determines this
# from the "textures" parameter.
*/

void glDeleteTextures(GLsizei n_1, const GLuint *textures);
DOC(glDeleteTextures, "glDeleteTextures(textures[]) -> None")


/*
# glDepthFunc
# 
# Python binding unchanged from spec.
*/

void glDepthFunc(GLenum func);
DOC(glDepthFunc, "glDepthFunc(func) -> None")


/*
# glDepthMask
#
# Python binding unchanged from spec
*/

void glDepthMask(GLboolean flag);
DOC(glDepthMask, "glDepthMask(flag) -> None")


/*
# glDepthRange
#
# Python binding unchanged from spec
*/

void glDepthRange(GLclampd zNear, GLclampd zFar);
DOC(glDepthRange, "glDepthRange(zNear, zFar) -> None")


/*
# glDisable
#
# Python binding unchanged from spec
*/

void glDisable(GLenum cap);
DOC(glDisable, "glDisable(cap) -> None")


/*
# glDisableClientState
#
# Python binding unchanged from spec
*/

void glDisableClientState(GLenum array);
DOC(glDisableClientState, "glDisableClientState(array) -> None")


/*
# glDrawArrays
#
# Python binding unchanged from spec
*/

#if API_VERSION > 256
void glDrawArrays(GLenum mode, GLint first, GLsizei count);
DOC(glDrawArrays, "glDrawArrays(mode, first, count) -> None")
#endif


/*
# glDrawBuffer
#
# Python binding unchanged from spec
*/

void glDrawBuffer(GLenum mode);
DOC(glDrawBuffer, "glDrawBuffer(mode) -> None")


/*
# glDrawElements
#
# Python binding unchanged from spec, with the addition of the
# decorated utility functions
*/

#if API_VERSION > 256
void glDrawElements(GLenum mode, GLsizei count, GLenum type, const void *buffer);
DOC(glDrawElements, "glDrawElements(mode, count, type, indices) -> None")

%name(glDrawElementsub) void glDrawElements(GLenum mode, GLsizei n_2, GLenum type_UNSIGNED_BYTE, const GLubyte *indices);
DOC(glDrawElementsub, "glDrawElementsub(mode, indices[]) -> None")

%name(glDrawElementsus) void glDrawElements(GLenum mode, GLsizei n_2, GLenum type_UNSIGNED_SHORT, const GLushort *indices);
DOC(glDrawElementsus, "glDrawElementsus(mode, indices[]) -> None")

%name(glDrawElementsui) void glDrawElements(GLenum mode, GLsizei n_2, GLenum type_UNSIGNED_INT, const GLuint *indices);
DOC(glDrawElementsui, "glDrawElementsui(mode, indices[]) -> None")
#endif


/*
# glDrawPixels
#
# Python binding unchanged from spec, with the addition of the
# decorated utility functions
*/

void glDrawPixels(GLsizei width, GLsizei height, GLenum format, GLenum type, const void *buffer);
DOC(glDrawPixels, "glDrawPixels(width, height, format, type, pixels) -> None")

%{
void _glDrawPixels(GLsizei width, GLsizei height, GLenum format, GLenum type, const GLvoid* pixels)
{
	SetupPixelWrite(2);
	glDrawPixels(width, height, format, type, pixels);
}
%}

%name(glDrawPixelsub) void _glDrawPixels(GLsizei d_4_0, GLsizei d_4_1, GLenum format, GLenum type_UNSIGNED_BYTE, const GLubyte *pixels);
DOC(glDrawPixelsub, "glDrawPixelsub(format, pixels[][] | pixels[][][]) -> None")

%name(glDrawPixelsb) void _glDrawPixels(GLsizei d_4_0, GLsizei d_4_1, GLenum format, GLenum type_BYTE, const GLbyte *pixels);
DOC(glDrawPixelsb, "glDrawPixelsb(format, pixels[][] | pixels[][][]) -> None")

%name(glDrawPixelsus) void _glDrawPixels(GLsizei d_4_0, GLsizei d_4_1, GLenum format, GLenum type_UNSIGNED_SHORT, const GLushort *pixels);
DOC(glDrawPixelsus, "glDrawPixelsus(format, pixels[][] | pixels[][][]) -> None")

%name(glDrawPixelss) void _glDrawPixels(GLsizei d_4_0, GLsizei d_4_1, GLenum format, GLenum type_SHORT, const GLshort *pixels);
DOC(glDrawPixelss, "glDrawPixelss(format, pixels[][] | pixels[][][]) -> None")

%name(glDrawPixelsui) void _glDrawPixels(GLsizei d_4_0, GLsizei d_4_1, GLenum format, GLenum type_UNSIGNED_INT, const GLuint *pixels);
DOC(glDrawPixelsui, "glDrawPixelsui(format, pixels[][] | pixels[][][]) -> None")

%name(glDrawPixelsi) void _glDrawPixels(GLsizei d_4_0, GLsizei d_4_1, GLenum format, GLenum type_INT, const GLint *pixels);
DOC(glDrawPixelsi, "glDrawPixelsi(format, pixels[][] | pixels[][][]) -> None")

%name(glDrawPixelsf) void _glDrawPixels(GLsizei d_4_0, GLsizei d_4_1, GLenum format, GLenum type_FLOAT, const GLfloat *pixels);
DOC(glDrawPixelsf, "glDrawPixelsf(format, pixels[][] | pixels[][][]) -> None")


/*
# glEdgeFlagPointer
#
# Python binding unchanged from spec, with the exception of
# the decorated function.
*/

#if API_VERSION > 256
%{
void _glEdgeFlagPointer(GLsizei stride, GLvoid *pointer)
{
	decrementPointerLock(GL_EDGE_FLAG_ARRAY_POINTER);
	acquire(pointer);
	glEdgeFlagPointer(stride, pointer);
}
%}

%name(glEdgeFlagPointer) void _glEdgeFlagPointer(GLsizei stride, void *pointer);
DOC(glEdgeFlagPointer, "glEdgeFlagPointer(stride, pointer) -> None")

%name(glEdgeFlagPointerb) void _glEdgeFlagPointer(GLsizei stride_0, GLbyte* pointer);
DOC(glEdgeFlagPointerb, "glEdgeFlagPointerb(pointer[]) -> None")
#endif


/*
# glEnable
#
# Python binding unchanged from spec
*/

void glEnable(GLenum cap);
DOC(glEnable, "glEnable(cap) -> None")


/*
# glEnableClientState
#
# Python binding unchanged from spec
*/

void glEnableClientState(GLenum array);
DOC(glEnableClientState, "glEnableClientState(array) -> None")


/*
# glEnd
#
# Python binding unchanged from spec
*/

void glEnd();
DOC(glEnd, "glEnd() -> None")


/*
# glEndList
#
# Python binding unchanged from spec
*/

void glEndList();
DOC(glEndList, "glEndList() -> None")


/*
# glEvalMesh
#
# Python binding unchanged from spec
*/

void glEvalMesh1(GLenum mode, GLint i1, GLint i2);
DOC(glEvalMesh1, "glEvalMesh1(mode, i1, i2) -> None")
void glEvalMesh2(GLenum mode, GLint i1, GLint i2, GLint j1, GLint j2);
DOC(glEvalMesh2, "glEvalMesh2(mode, i1, i2, j1, j2) -> None")


/*
# glFeedbackBuffer
#
# The "buffer" parameter of the C prototype is not needed
# since the buffer is dynamically allocated and returned
# by glRenderMode which the mode is changed to something
# besides GL_FEEDBACK.
*/

%{

static GLfloat null_feedback_buffer[1];
void _glFeedbackBuffer(GLsizei size, GLenum type)
{
	GLfloat *buffer = (size > 0) ? PyMem_New(GLfloat, size) : null_feedback_buffer;
#ifndef GL_VERSION_1_1
	PyGLcontext *context = GetGLcontext();
	context->feedback_type = type;
	context->feedback_buffer = buffer;
#endif
	glFeedbackBuffer(size, type, buffer);
}
%}

%name(glFeedbackBuffer) void _glFeedbackBuffer(GLsizei size, GLenum type);
DOC(glFeedbackBuffer, "glFeedbackBuffer(size, type) -> None")


/*
# glFinish
#
# Python binding unchanged from spec
*/

void glFinish();
DOC(glFinish, "glFinish() -> None")


/*
# glFlush
#
# Python binding unchanged from spec
*/

void glFlush();
DOC(glFlush, "glFlush() -> None")


/*
# glFog
#
# Python binding unchanged from spec, except for addition of
# an alias.
*/

void glFogf(GLenum pname, GLfloat param);
DOC(glFogf, "glFogf(pname, param) -> None")

void glFogfv(GLenum pname, const GLfloat *v);
DOC(glFogfv, "glFogfv(pname, params[]) -> None")

void glFogi(GLenum pname, GLint param);
DOC(glFogi, "glFogi(pname, param) -> None")

void glFogiv(GLenum pname, const GLint *v);
DOC(glFogiv, "glFogiv(pname, params[]) -> None")

%shadow %{
glFog = _GL__init__.glFogfv
%}




/*
# glFrontFace
#
# Python binding unchanged from spec
*/

void glFrontFace(GLenum mode);
DOC(glFrontFace, "glFrontFace(mode) -> None")


/*
# glFrustum
#
# Python binding unchanged from spec
*/

void glFrustum(GLdouble left, GLdouble right, GLdouble bottom, GLdouble top, GLdouble zNear, GLdouble zFar);
DOC(glFrustum, "glFrustum(left, right, bottom, top, zNear, zFar) -> None")


/*
# glGenLists
#
# Python binding unchanged from spec
*/

GLuint glGenLists(GLsizei range);
DOC(glGenLists, "glGenLists(range) -> listBase")


/*
# glGenTextures
#
# The "textures" parameters of the C prototype is
# unneeded since the Python binding returns resulting
# textures instead.
*/

%{
PyObject* _glGenTextures(GLsizei n)
{
	GLuint* textures;
	PyObject* result;
	
	textures = PyMem_New(GLuint, n);
	glGenTextures(n, textures);
	result = _PyTuple_FromUnsignedIntArray(n, textures);

	PyMem_Del(textures);
	return result;
}
%}

%name(glGenTextures) PyObject* _glGenTextures(GLsizei n);
DOC(glGenTextures, "glGenTextures(n) -> textures")


/*
# glGetBooleanv
#
# The "params" parameter of the C prototype is
# unneeded since the Python binding returns resulting
# params instead.
*/

void glGetBooleanv(GLenum pname, GLboolean params[16]);
DOC(glGetBooleanv, "glGetBooleanv(pname) -> params")

%shadow %{
glGetBoolean = _GL__init__.glGetBooleanv
%}

/*
# glGetClipPlane
#
# The "equation" parameter of the C prototype is
# unneeded since the Python binding returns resulting
# equation instead.
*/

void glGetClipPlane(GLenum plane, GLdouble equation[4]);
DOC(glGetClipPlane, "glGetClipPlane(plane) -> equation")


/*
# glGetDoublev
#
# The "params" parameter of the C prototype is
# unneeded since the Python binding returns resulting
# params instead.
*/

void glGetDoublev(GLenum pname, GLdouble params[16]);
DOC(glGetDoublev, "glGetDoublev(pname) -> params")


%shadow %{
glGetDouble = _GL__init__.glGetDoublev
%}



/*
# glGetFloatv
#
# The "params" parameter of the C prototype is
# unneeded since the Python binding returns resulting
# params instead.
*/

void glGetFloatv(GLenum pname, GLfloat params[16]);
DOC(glGetFloatv, "glGetFloatv(pname) -> params")


%shadow %{
glGetFloat = _GL__init__.glGetFloatv
%}



/*
# glGetIntegerv
#
# The "params" parameter of the C prototype is
# unneeded since the Python binding returns resulting
# params instead.
*/

void glGetIntegerv(GLenum pname, GLint params[16]);
DOC(glGetIntegerv, "glGetIntegerv(pname) -> params")


%shadow %{
glGetInteger = _GL__init__.glGetIntegerv
%}



/*
# glGetLight
#
# The "params" parameter of the C prototype is
# unneeded since the Python binding returns resulting
# params instead.
*/

void glGetLightfv(GLenum light, GLenum pname, GLfloat params[4]);
DOC(glGetLightfv, "glGetLightfv(light, pname) -> params")

void glGetLightiv(GLenum light, GLenum pname, GLint params[4]);
DOC(glGetLightiv, "glGetLightiv(light, pname) -> params")


/*
# glGetMap
#
# The map is returned instead of passed in as the paramter "v"
*/

%{
int _calcMapSizes(GLenum target, GLenum query, int *dimension, int *cp_size, int *v_size, int order[2])
{
	switch (target)
	{
	case GL_MAP1_INDEX:
	case GL_MAP1_TEXTURE_COORD_1:
		*dimension = 1;
		*cp_size = 1;
		break;
	case GL_MAP1_TEXTURE_COORD_2:
		*dimension = 1;
		*cp_size = 2;
		break;
	case GL_MAP1_NORMAL:
	case GL_MAP1_TEXTURE_COORD_3:
	case GL_MAP1_VERTEX_3:
		*dimension = 1;
		*cp_size = 3;
		break;
	case GL_MAP1_COLOR_4:
	case GL_MAP1_TEXTURE_COORD_4:
	case GL_MAP1_VERTEX_4:
		*dimension = 1;
		*cp_size = 4;
		break;
	case GL_MAP2_INDEX:
	case GL_MAP2_TEXTURE_COORD_1:
		*dimension = 2;
		*cp_size = 1;
		break;
	case GL_MAP2_TEXTURE_COORD_2:
		*dimension = 2;
		*cp_size = 2;
		break;
	case GL_MAP2_NORMAL:
	case GL_MAP2_TEXTURE_COORD_3:
	case GL_MAP2_VERTEX_3:
		*dimension = 2;
		*cp_size = 3;
		break;
	case GL_MAP2_COLOR_4:
	case GL_MAP2_TEXTURE_COORD_4:
	case GL_MAP2_VERTEX_4:
		*dimension = 2;
		*cp_size = 4;
		break;
	default:
		PyErr_SetString(PyExc_Exception, "Unknown target.");
		return 0;
	}

	switch (query)
	{
	case GL_COEFF:
		glGetMapiv(target, GL_ORDER, order);
		*v_size = (*cp_size)*order[0]*((*dimension == 2) ? order[1] : 1);
		break;
	case GL_ORDER:
		*v_size = *dimension;
		break;
	case GL_DOMAIN:
		*v_size = 2*(*dimension);
		break;
	default:
		PyErr_SetString(PyExc_Exception, "Unknown query.");
		return 0;
	}
	
	return 1;
}

%}

#define GET_MAP(EXT_NAME, NAME, BASE)\
%{\
PyObject* _glGetMap##EXT_NAME(GLenum target, GLenum query)\
{\
	int dimension, cp_size, v_size;\
	GLint order[2];\
	BASE* v;\
	PyObject* result;\
	int dims[3];\
\
	if (!_calcMapSizes(target, query, &dimension, &cp_size, &v_size, order)) return NULL;\
\
	v = PyMem_New(BASE, v_size);\
	glGetMap##EXT_NAME(target, query, v);\
\
	if (query == GL_COEFF)\
	{\
		if (dimension == 2)\
		{\
			dims[0] = order[1];\
			dims[1] = order[0];\
			dims[2] = cp_size;\
		}\
		else\
		{\
			dims[0] = order[0];\
			dims[1] = cp_size;\
		}\
		result = _PyObject_From##NAME(dimension + 1, dims, v, 1);\
	}\
	else\
	{\
		result = _PyTuple_From##NAME(v_size, v);\
		PyMem_Del(v);\
	}\
\
	return result;\
}\
%}

GET_MAP(dv, DoubleArray, double)
GET_MAP(fv, FloatArray, float)
GET_MAP(iv, IntArray, int)

%name(glGetMapdv) PyObject* _glGetMapdv(GLenum target, GLenum query);
DOC(glGetMapdv, "glGetMapdv(target, query) -> values")

%name(glGetMapfv) PyObject* _glGetMapdv(GLenum target, GLenum query);
DOC(glGetMapfv, "glGetMapfv(target, query) -> values")

%name(glGetMapiv) PyObject* _glGetMapiv(GLenum target, GLenum query);
DOC(glGetMapiv, "glGetMapiv(target, query) -> values")


/*
# glGetMaterial
#
# The "params" argument is returned instead of passed as a parameter.
*/

void glGetMaterialfv(GLenum face, GLenum pname, GLfloat params[4]);
DOC(glGetMaterialfv, "glGetMaterialfv(face, pname) -> params")

void glGetMaterialiv(GLenum face, GLenum pname, GLint params[4]);
DOC(glGetMaterialiv, "glGetMaterialiv(face, pname) -> params")


/*
# glGetPixelMap
#
# The "values" argument is returned instead of passed as a parameter.
*/

#define GET_PIXEL_MAP(NAME, TYPE, PY_OBJECT)\
%{\
PyObject* _##NAME(GLenum map)\
{\
	int i;\
	GLint size;\
	TYPE* values;\
	PyObject* result;\
\
	glGetIntegerv(GL_PIXEL_MAP_I_TO_I_SIZE - GL_PIXEL_MAP_I_TO_I + map, &size);\
	values = PyMem_New(TYPE, size);\
	NAME(map, values);\
\
	result = PyTuple_New(size);\
	for (i = 0; i < size; i++) PyTuple_SetItem(result, i, PY_OBJECT(values[i]));\
	PyMem_Del(values);\
\
	return result;\
}\
%}

GET_PIXEL_MAP(glGetPixelMapfv, GLfloat, PyFloat_FromDouble)

GET_PIXEL_MAP(glGetPixelMapuiv, GLuint, PyLong_FromUnsignedLong)

GET_PIXEL_MAP(glGetPixelMapusv, GLushort, PyInt_FromLong)

%name(glGetPixelMapfv) PyObject* _glGetPixelMapfv(GLenum map);
DOC(glGetPixelMapfv, "glGetPixelMapfv(map) -> values")

%name(glGetPixelMapuiv) PyObject* _glGetPixelMapuiv(GLenum map);
DOC(glGetPixelMapuiv, "glGetPixelMapuiv(map) -> values")

%name(glGetPixelMapusv) PyObject* _glGetPixelMapusv(GLenum map);
DOC(glGetPixelMapusv, "glGetPixelMapusv(map) -> values")


/*
# glGetPolygonStipple
#
# The "mask" argument is returned instead of passed as a parameter.
#
# The undecorated version respects any pixel transfer flags and returns
# a string containing the packed data.
#
# The decorated version resets any pixel transfer flags and returns an
# GLubyte array with each element equal to a single pixel, i.e. 0 or 1.
*/

%{
PyObject* _glGetPolygonStipple()
{
	PyObject* result;
	int size;
	GLint dims[] = {32, 32};
	void* data = SetupRawPixelRead(GL_BITMAP, GL_UNSIGNED_BYTE, 2, dims, &size);
	if (!data) return NULL;
	
	glGetPolygonStipple(data);
	result = PyString_FromStringAndSize((const char*)data, size);
	PyMem_Del(data);

	return result;
}
%}

%name(glGetPolygonStipple) PyObject* _glGetPolygonStipple();
DOC(glGetPolygonStipple, "glGetPolygonStipple() -> packed stipple")

%{
PyObject* glGetPolygonStippleub()
{
	int dims[] = {32, 32};
	GLubyte packed[128];
	GLubyte unpacked[1024];
	int i, j;
	
	glPixelStorei(GL_PACK_SWAP_BYTES, 0);
	glPixelStorei(GL_PACK_LSB_FIRST, 1);

	glGetPolygonStipple(packed);
	
	for (i = 0; i < 128; i++) for (j = 0; j < 8; j++) unpacked[8*i + j] = (packed[i] >> j) & 1;
	
	return _PyObject_FromUnsignedCharArray(2, dims, unpacked, 0);
}
%}

%name(glGetPolygonStippleub) PyObject* glGetPolygonStippleub();
DOC(glGetPolygonStippleub, "glGetPolygonStippleub() -> stipple[][]")


/*
# glGetString
#
# Python binding unchanged from spec
*/

const GLubyte * glGetString(GLenum name);
DOC(glGetString, "glGetString(name) -> string")


/*
# glGetTexEnv
#
# The "params" argument is returned instead of passed as a parameter.
*/

void glGetTexEnvfv(GLenum target, GLenum pname, GLfloat params[4]);
DOC(glGetTexEnvfv, "glGetTexEnvfv(target, pname) -> params")

void glGetTexEnviv(GLenum target, GLenum pname, GLint params[4]);
DOC(glGetTexEnviv, "glGetTexEnviv(target, pname) -> params")


/*
# glGetTexGen
#
# The "params" argument is returned instead of passed as a parameter.
*/

void glGetTexGendv(GLenum coord, GLenum pname, GLdouble params[4]);
DOC(glGetTexGendv, "glGetTexGendv(coord, pname) -> params")

void glGetTexGenfv(GLenum coord, GLenum pname, GLfloat params[4]);
DOC(glGetTexGenfv, "glGetTexGenfv(coord, pname) -> params")

void glGetTexGeniv(GLenum coord, GLenum pname, GLint params[4]);
DOC(glGetTexGeniv, "glGetTexGeniv(coord, pname) -> params")


/*
# glGetTexImage
#
# For the undecorated version the returned image is a packed string which respects
# the pixel store settings.
#
# For the decorated versions the "type" parameter is automatically determined and
# the returned image is a multidimensional array of the correct type.  Any pixel
# transfer settings are ignored.
*/

%{
#ifndef GL_SGIS_texture4D
#define GL_TEXTURE_4D_SGIS                0x8134
#define GL_TEXTURE_4DSIZE_SGIS            0x8136
#endif

#ifndef GL_VERSION_1_2
#define GL_TEXTURE_3D				0x806F
#define GL_TEXTURE_DEPTH			0x8071
#endif

/* figure out the rank of the image and the dimensions */
int get_tex_dims(GLenum target, GLint level, int dims[4])
{
	int rank = 0;

	/* just cascade through the switch, retrieving the apropriate sizes */
	switch (target)
	{
	case GL_TEXTURE_4D_SGIS:
		glGetTexLevelParameteriv(target, level, GL_TEXTURE_4DSIZE_SGIS, dims + rank++);
	case GL_TEXTURE_3D:
		glGetTexLevelParameteriv(target, level, GL_TEXTURE_DEPTH, dims + rank++);
	case GL_TEXTURE_2D:
		glGetTexLevelParameteriv(target, level, GL_TEXTURE_WIDTH, dims + rank++);
	case GL_TEXTURE_1D:
		glGetTexLevelParameteriv(target, level, GL_TEXTURE_HEIGHT, dims + rank++);
	}
	return rank;
}

PyObject* _glGetTexImage (GLenum target, GLint level, GLenum format, GLenum type)
{
	PyObject* result;
	int size;
	GLint dims[4];
	int rank;
	void* data = NULL;
	
	rank = get_tex_dims(target, level, dims);
	
	/* dims[rank] is set to the appropriate value for format here */
	data = SetupRawPixelRead(format, type, rank, dims, &size);
	if (!data) return NULL;
	
	glGetTexImage(target, level, format, type, data);
	result = PyString_FromStringAndSize((const char*)data, size);
	PyMem_Del(data);

	return result;
}
%}

%name(glGetTexImage) PyObject* _glGetTexImage(GLenum target, GLint level, GLenum format, GLenum type);
DOC(glGetTexImage, "glGetTexImage(target, level, format, type) -> pixels")

%{
PyObject* __glGetTexImage (GLenum target, GLint level, GLenum format, GLenum type)
{
	int dims[5], rank;
	void* data;
	

	rank = get_tex_dims(target, level, dims);
	
	/* dims[rank] is set to the appropriate value for format here */
	data = SetupPixelRead(rank, format, type, dims);
	if (!data) return NULL;
	
	glGetTexImage(target, level, format, type, data);

	/* Note need to add one
		rank will be used as "nd" (number of dimensions),
		for constructing the array. _PyObject_FromArray counts
		from 1 for this parameter
	*/
	return _PyObject_FromArray(type, (dims[rank] == 1) ? rank : rank+1, dims, data, 1);
}
%}

%name(glGetTexImageub) PyObject* __glGetTexImage(GLenum target, GLint level, GLenum format, GLenum type_UNSIGNED_BYTE);
DOC(glGetTexImageub, "glGetTexImageub(target, level, format) -> pixels[][] | pixels[][][]")

%name(glGetTexImageb) PyObject* __glGetTexImage(GLenum target, GLint level, GLenum format, GLenum type_BYTE);
DOC(glGetTexImageb, "glGetTexImageb(target, level, format) -> pixels[][] | pixels[][][]")

%name(glGetTexImageus) PyObject* __glGetTexImage(GLenum target, GLint level, GLenum format, GLenum type_UNSIGNED_SHORT);
DOC(glGetTexImageus, "glGetTexImageus(target, level, format) -> pixels[][] | pixels[][][]")

%name(glGetTexImages) PyObject* __glGetTexImage(GLenum target, GLint level, GLenum format, GLenum type_SHORT);
DOC(glGetTexImages, "glGetTexImages(target, level, format) -> pixels[][] | pixels[][][]")

%name(glGetTexImageui) PyObject* __glGetTexImage(GLenum target, GLint level, GLenum format, GLenum type_UNSIGNED_INT);
DOC(glGetTexImageui, "glGetTexImageui(target, level, format) -> pixels[][] | pixels[][][]")

%name(glGetTexImagei) PyObject* __glGetTexImage(GLenum target, GLint level, GLenum format, GLenum type_INT);
DOC(glGetTexImagei, "glGetTexImagei(target, level, format) -> pixels[][] | pixels[][][]")

%name(glGetTexImagef) PyObject* __glGetTexImage(GLenum target, GLint level, GLenum format, GLenum type_FLOAT);
DOC(glGetTexImagef, "glGetTexImagef(target, level, format) -> pixels[][] | pixels[][][]")

%name(glGetTexImaged) PyObject* __glGetTexImage(GLenum target, GLint level, GLenum format, GLenum type_DOUBLE);
DOC(glGetTexImaged, "glGetTexImagef(target, level, format) -> pixels[][] | pixels[][][]")


/*
# glGetTexLevelParameter
#
# The "params" argument is returned instead of passed as a parameter.
*/

void glGetTexLevelParameterfv(GLenum target, GLint level, GLenum pname, GLfloat params[4]);
DOC(glGetTexLevelParameterfv, "glGetTexLevelParameterfv(target, level, pname) -> params")

void glGetTexLevelParameteriv(GLenum target, GLint level, GLenum pname, GLint params[4]);
DOC(glGetTexLevelParameteriv, "glGetTexLevelParameteriv(target, level, pname) -> params")


/*
# glGetTexParameter
#
# The "params" argument is returned instead of passed as a parameter.
*/

void glGetTexParameterfv(GLenum target, GLenum pname, GLfloat params[4]);
DOC(glGetTexParameterfv, "glGetTexParameterfv(target, pname) -> params")

void glGetTexParameteriv(GLenum target, GLenum pname, GLint params[4]);
DOC(glGetTexParameteriv, "glGetTexParameteriv(target, pname) -> params")


/*
# glHint
#
# Python binding unchanged from spec
*/

void glHint(GLenum target, GLenum mode);
DOC(glHint, "glHint(target, mode) -> None")


/*
# glIndexMask
#
# Python binding unchanged from spec
*/

void glIndexMask(GLuint mask);
DOC(glIndexMask, "glIndexMask(mask) -> None")


/*
# glIndexPointer
# 
# The glIndexPointer function is unchanged from the spec, but the
# Python binding adds the decorated variants which take a multidimensional
# array as the data source and set the "type", and "stride"
# arguments as appropriate.
*/

#if API_VERSION > 256
%{
void _glIndexPointer(GLenum type, GLsizei stride, GLvoid *pointer)
{
	decrementPointerLock(GL_INDEX_ARRAY_POINTER);
	acquire(pointer);
	glIndexPointer(type, stride, pointer);
}
%}

%name(glIndexPointer) void _glIndexPointer(GLenum type, GLsizei stride, void *pointer);
DOC(glIndexPointer, "glIndexPointer(type, stride, pointer) -> None")

%name(glIndexPointerub) void _glIndexPointer(GLenum type_UNSIGNED_BYTE, GLsizei stride_0, GLubyte* pointer);
DOC(glIndexPointerub, "glIndexPointerub(pointer[]) -> None")

%name(glIndexPointerb) void _glIndexPointer(GLenum type_BYTE, GLsizei stride_0, GLbyte* pointer);
DOC(glIndexPointerb, "glIndexPointerub(pointer[]) -> None")

%name(glIndexPointers) void _glIndexPointer(GLenum type_SHORT, GLsizei stride_0, GLshort* pointer);
DOC(glIndexPointers, "glIndexPointers(pointer[]) -> None")

%name(glIndexPointeri) void _glIndexPointer(GLenum type_INT, GLsizei stride_0, GLint* pointer);
DOC(glIndexPointeri, "glIndexPointeri(pointer[]) -> None")

%name(glIndexPointerf) void _glIndexPointer(GLenum type_FLOAT, GLsizei stride_0, GLfloat* pointer);
DOC(glIndexPointerf, "glIndexPointerf(pointer[]) -> None")

%name(glIndexPointerd) void _glIndexPointer(GLenum type_DOUBLE, GLsizei stride_0, GLdouble* pointer);
DOC(glIndexPointerd, "glIndexPointerd(pointer[]) -> None")
#endif


/*
# glInitNames
#
# Python binding unchanged from spec
*/

void glInitNames();
DOC(glInitNames, "glInitNames() -> None")


/*
# glInterleavedArrays
# 
# The glInterleavedArrays function is unchanged from the spec, except
# the "pointer" should be packed string containing the data.
*/

#if API_VERSION > 256
%{
#ifndef GL_SUN_triangle_list
#define GL_R1UI_V3F_SUN 0x85C4
#define GL_R1UI_C4UB_V3F_SUN 0x85C5
#define GL_R1UI_C3F_V3F_SUN 0x85C6
#define GL_R1UI_N3F_V3F_SUN 0x85C7
#define GL_R1UI_C4F_N3F_V3F_SUN 0x85C8
#define GL_R1UI_T2F_V3F_SUN 0x85C9
#define GL_R1UI_T2F_N3F_V3F_SUN 0x85CA
#define GL_R1UI_T2F_C4F_N3F_V3F_SUN 0x85CB

#define GL_REPLACEMENT_CODE_ARRAY_POINTER_SUN 0x85C3
#endif

#ifndef GL_EXT_index_array_formats
#define GL_IUI_V2F_EXT                    0x81AD
#define GL_IUI_V3F_EXT                    0x81AE
#define GL_IUI_N3F_V2F_EXT                0x81AF
#define GL_IUI_N3F_V3F_EXT                0x81B0
#define GL_T2F_IUI_V2F_EXT                0x81B1
#define GL_T2F_IUI_V3F_EXT                0x81B2
#define GL_T2F_IUI_N3F_V2F_EXT            0x81B3
#define GL_T2F_IUI_N3F_V3F_EXT            0x81B4
#endif

void _glInterleavedArrays(GLenum format, GLsizei stride, GLvoid *pointer)
{
	GLenum p[POINTER_COUNT];
	
	decrementPointerLock(p[0] = GL_VERTEX_ARRAY_POINTER);
	
	switch (format)
	{
	case GL_C3F_V3F:
	case GL_C4F_N3F_V3F:
	case GL_C4UB_V2F:
	case GL_C4UB_V3F:
	case GL_T2F_C3F_V3F:
	case GL_T2F_C4F_N3F_V3F:
	case GL_T2F_C4UB_V3F:
	case GL_T4F_C4F_N3F_V4F:
	case GL_R1UI_C4UB_V3F_SUN:
	case GL_R1UI_C3F_V3F_SUN:
	case GL_R1UI_C4F_N3F_V3F_SUN:
	case GL_R1UI_T2F_C4F_N3F_V3F_SUN:
		decrementPointerLock(p[1] = GL_COLOR_ARRAY_POINTER);
		break;
	default:
		p[1] = 0;
	}

	switch (format)
	{
	case GL_N3F_V3F:
	case GL_C4F_N3F_V3F:
	case GL_T2F_N3F_V3F:
	case GL_T2F_C4F_N3F_V3F:
	case GL_T4F_C4F_N3F_V4F:
	case GL_R1UI_N3F_V3F_SUN:
	case GL_R1UI_C4F_N3F_V3F_SUN:
	case GL_R1UI_T2F_N3F_V3F_SUN:
	case GL_R1UI_T2F_C4F_N3F_V3F_SUN:
	case GL_IUI_N3F_V2F_EXT:
	case GL_IUI_N3F_V3F_EXT:
	case GL_T2F_IUI_N3F_V2F_EXT:
	case GL_T2F_IUI_N3F_V3F_EXT:
		decrementPointerLock(p[2] = GL_NORMAL_ARRAY_POINTER);
		break;
	default:
		p[2] = 0;
	}

	switch (format)
	{
	case GL_T2F_V3F:
	case GL_T4F_V4F:
	case GL_T2F_C4UB_V3F:
	case GL_T2F_C3F_V3F:
	case GL_T2F_N3F_V3F:
	case GL_T2F_C4F_N3F_V3F:
	case GL_T4F_C4F_N3F_V4F:
	case GL_R1UI_T2F_V3F_SUN:
	case GL_R1UI_T2F_N3F_V3F_SUN:
	case GL_R1UI_T2F_C4F_N3F_V3F_SUN:
	case GL_T2F_IUI_V2F_EXT:
	case GL_T2F_IUI_V3F_EXT:
	case GL_T2F_IUI_N3F_V2F_EXT:
	case GL_T2F_IUI_N3F_V3F_EXT:
		decrementPointerLock(p[3] = GL_TEXTURE_COORD_ARRAY_POINTER);
		break;
	default:
		p[3] = 0;
	}

	switch (format)
	{
	case GL_R1UI_V3F_SUN:
	case GL_R1UI_C4UB_V3F_SUN:
	case GL_R1UI_C3F_V3F_SUN:
	case GL_R1UI_N3F_V3F_SUN:
	case GL_R1UI_C4F_N3F_V3F_SUN:
	case GL_R1UI_T2F_V3F_SUN:
	case GL_R1UI_T2F_N3F_V3F_SUN:
	case GL_R1UI_T2F_C4F_N3F_V3F_SUN:
		decrementPointerLock(p[4] = GL_REPLACEMENT_CODE_ARRAY_POINTER_SUN);
		break;
	default:
		p[4] = 0;
	}

	switch (format)
	{
	case GL_IUI_V2F_EXT:
	case GL_IUI_V3F_EXT:
	case GL_IUI_N3F_V2F_EXT:
	case GL_IUI_N3F_V3F_EXT:
	case GL_T2F_IUI_V2F_EXT:
	case GL_T2F_IUI_V3F_EXT:
	case GL_T2F_IUI_N3F_V2F_EXT:
	case GL_T2F_IUI_N3F_V3F_EXT:
		decrementPointerLock(p[5] = GL_INDEX_ARRAY_POINTER);
		break;
	default:
		p[5] = 0;
	}

	glInterleavedArrays(format, stride, pointer);
	acquireInterleavedPointer(pointer, p);
}
%}

%name(glInterleavedArrays) void _glInterleavedArrays(GLenum format, GLsizei stride, void *pointer);
DOC(glInterleavedArrays, "glInterleavedArrays(format, stride, pointer) -> None")
#endif


/*
# glIsEnabled
#
# Python binding unchanged from spec
*/

GLboolean glIsEnabled(GLenum cap);
DOC(glIsEnabled, "glIsEnabled(cap) -> None")


/*
# glIsList
#
# Python binding unchanged from spec
*/

GLboolean glIsList(GLuint list);
DOC(glIsList, "glIsList(list) -> boolean")


/*
# glIsTexture
#
# Python binding unchanged from spec
*/

GLboolean glIsTexture(GLuint texture);
DOC(glIsTexture, "glIsTexture(texture) -> boolean")


/*
# glLightModel
#
# Python binding unchanged from spec
*/

void glLightModelf(GLenum pname, GLfloat param);
DOC(glLightModelf, "glLightModelf(pname, param) -> None")

void glLightModelfv(GLenum pname, const GLfloat *v);
DOC(glLightModelfv, "glLightModelfv(pname, params) -> None")

void glLightModeli(GLenum pname, GLint param);
DOC(glLightModeli, "glLightModeli(pname, param) -> None")

void glLightModeliv(GLenum pname, const GLint *v);
DOC(glLightModeliv, "glLightModeliv(pname, params) -> None")



%shadow %{
glLightModel = _GL__init__.glLightModelfv
%}


/*
# glLight
#
# Python binding unchanged from spec
*/

void glLightf(GLenum light, GLenum pname, GLfloat param);
DOC(glLightf, "glLightf(light, pname, param) -> None")

void glLightfv(GLenum light, GLenum pname, const GLfloat *v);
DOC(glLightfv, "glLightfv(light, pname, params) -> None")

void glLighti(GLenum light, GLenum pname, GLint param);
DOC(glLighti, "glLighti(light, pname, param) -> None")

void glLightiv(GLenum light, GLenum pname, const GLint *v);
DOC(glLightiv, "glLightiv(light, pname, params) -> None")


%shadow %{
glLight = _GL__init__.glLightfv
%}

/*
# glLineStipple
#
# Python binding unchanged from spec
*/

void glLineStipple(GLint factor, GLushort pattern);
DOC(glLineStipple, "glLineStipple(factor, pattern) -> None")


/*
# glLineWidth
#
# Python binding unchanged from spec
*/

void glLineWidth(GLfloat width);
DOC(glLineWidth, "glLineWidth(width) -> None")


/*
# glListBase
#
# Python binding unchanged from spec
*/

void glListBase(GLuint base);
DOC(glListBase, "glListBase(base) -> None")


/*
# glLoadIdentity
#
# Python binding unchanged from spec
*/

void glLoadIdentity();
DOC(glLoadIdentity, "glLoadIdentity() -> None")


/*
# glLoadMatrix
#
# Python binding unchanged from spec
*/

void glLoadMatrixd(const GLdouble *v);
DOC(glLoadMatrixd, "glLoadMatrixd(matrix) -> None")

void glLoadMatrixf(const GLfloat *v);
DOC(glLoadMatrixf, "glLoadMatrixf(matrix) -> None")


/*
# glLoadName
#
# Python binding unchanged from spec
*/

void glLoadName(GLuint name);
DOC(glLoadName, "glLoadName(name) -> None")


/*
# glLogicOp
#
# Python binding unchanged from spec
*/

void glLogicOp(GLenum opcode);
DOC(glLogicOp, "glLogicOp(opcode) -> None")


/*
# glMap
#
# Unlike the C prototype all the stride and order arguments are automatically
# derived from the multidimensional parameter "points"
*/

void glMap1d(GLenum target, GLdouble u1, GLdouble u2, GLint d_6_1, GLint d_6_0, const GLdouble *points);
DOC(glMap1d, "glMap1d(target, u1, u2, points[][]) -> None")

void glMap1f(GLenum target, GLfloat u1, GLfloat u2, GLint d_6_1, GLint d_6_0, const GLfloat *points);
DOC(glMap1f, "glMap1f(target, u1, u2, points[][]) -> None")

%{
#define _glMap2d(target, u1, u2, uorder, v1, v2, vstride, vorder, points) glMap2d(target, u1, u2, vstride*vorder, uorder, v1, v2, vstride, vorder, points) 
%}

%name(glMap2d) void _glMap2d(GLenum target, GLdouble u1, GLdouble u2, GLint d_8_0, GLdouble v1, GLdouble v2, GLint d_8_2, GLint d_8_1, const GLdouble *points);
DOC(glMap2d, "glMap2d(target, u1, u2, v1, v2, points[][][]) -> None")

%{
#define _glMap2f(target, u1, u2, uorder, v1, v2, vstride, vorder, points) glMap2f(target, u1, u2, vstride*vorder, uorder, v1, v2, vstride, vorder, points) 
%}

%name(glMap2f) void _glMap2f(GLenum target, GLfloat u1, GLfloat u2, GLint d_8_0, GLfloat v1, GLfloat v2, GLint d_8_2, GLint d_8_1, const GLfloat *points);
DOC(glMap2f, "glMap2f(target, u1, u2, v1, v2, points[][][]) -> None")


/*
# glMapGrid
#
# Python binding unchanged from spec
*/

void glMapGrid1d(GLint un, GLdouble u1, GLdouble u2);
DOC(glMapGrid1d, "glMapGrid1d(un, u1, u2) -> None")

void glMapGrid1f(GLint un, GLfloat u1, GLfloat u2);
DOC(glMapGrid1f, "glMapGrid1f(un, u1, u2) -> None")

void glMapGrid2d(GLint un, GLdouble u1, GLdouble u2, GLint vn, GLdouble v1, GLdouble v2);
DOC(glMapGrid2d, "glMapGrid2d(un, u1, u2, vn, v1, v2) -> None")

void glMapGrid2f(GLint un, GLfloat u1, GLfloat u2, GLint vn, GLfloat v1, GLfloat v2);
DOC(glMapGrid2f, "glMapGrid2f(un, u1, u2, vn, v1, v2) -> None")


/*
# glLogicOp
#
# Python binding unchanged from spec
*/

void glMatrixMode(GLenum mode);
DOC(glMatrixMode, "glMatrixMode(mode) -> None")


/*
# glMultMatrix
#
# Python binding unchanged from spec
*/

void glMultMatrixd(const GLdouble *v);
DOC(glMultMatrixd, "glMultMatrixd(v) -> None")

void glMultMatrixf(const GLfloat *v);
DOC(glMultMatrixf, "glMultMatrixf(v) -> None")


/*
# glNewList
#
# Python binding unchanged from spec
*/

void glNewList(GLuint list, GLenum mode);
DOC(glNewList, "glNewList(list, mode) -> None")


/*
# glNormalPointer
# 
# The glNormalPointer function is unchanged from the spec, but the
# Python binding adds the decorated variants which take a multidimensional
# array as the data source and set the "type", and "stride"
# arguments as appropriate.
*/

#if API_VERSION > 256
%{
void _glNormalPointer(GLenum type, GLsizei stride, GLvoid *pointer)
{
	decrementPointerLock(GL_NORMAL_ARRAY_POINTER);
	acquire(pointer);
	glNormalPointer(type, stride, pointer);
}
%}

%name(glNormalPointer) void _glNormalPointer(GLenum type, GLsizei stride, void *pointer);
DOC(glNormalPointer, "glNormalPointer(size, type, stride, pointer) -> None")

%name(glNormalPointerb) void _glNormalPointer(GLenum type_BYTE, GLsizei stride_0, GLbyte* pointer);
DOC(glNormalPointerb, "glNormalPointerub(pointer[][3]) -> None")

%name(glNormalPointers) void _glNormalPointer(GLenum type_SHORT, GLsizei stride_0, GLshort* pointer);
DOC(glNormalPointers, "glNormalPointers(pointer[][3]) -> None")

%name(glNormalPointeri) void _glNormalPointer(GLenum type_INT, GLsizei stride_0, GLint* pointer);
DOC(glNormalPointeri, "glNormalPointeri(pointer[][3]) -> None")

%name(glNormalPointerf) void _glNormalPointer(GLenum type_FLOAT, GLsizei stride_0, GLfloat* pointer);
DOC(glNormalPointerf, "glNormalPointerf(pointer[][3]) -> None")

%name(glNormalPointerd) void _glNormalPointer(GLenum type_DOUBLE, GLsizei stride_0, GLdouble* pointer);
DOC(glNormalPointerd, "glNormalPointerd(pointer[][3]) -> None")
#endif


/*
# glOrtho
#
# Python binding unchanged from spec
*/

void glOrtho(GLdouble left, GLdouble right, GLdouble bottom, GLdouble top, GLdouble zNear, GLdouble zFar);
DOC(glOrtho, "glOrtho(left, right, bottom, top, zNear, zFar) -> None")


/*
# glPassThrough
#
# Python binding unchanged from spec
*/

void glPassThrough(GLfloat token);
DOC(glPassThrough, "glPassThrough(token) -> None")


/*
# glPixelMap
#
# The "count" parameter of C prototype is automatically derived from the
# array "values"
*/

void glPixelMapfv(GLenum map, GLsizei n_2, const GLfloat *values);
DOC(glPixelMapfv, "glPixelMapfv(map, values) -> None")

void glPixelMapuiv(GLenum map, GLsizei n_2, const GLuint *values);
DOC(glPixelMapuiv, "glPixelMapuiv(map, values) -> None")

void glPixelMapusv(GLenum map, GLsizei n_2, const GLushort *values);
DOC(glPixelMapusv, "glPixelMapusv(map, values) -> None")


/*
# glPixelStore
#
# Python binding unchanged from spec
*/

void glPixelStoref(GLenum pname, GLfloat param);
DOC(glPixelStoref, "glPixelStoref(pname, param) -> None")

void glPixelStorei(GLenum pname, GLint param);
DOC(glPixelStorei, "glPixelStorei(pname, param) -> None")


/*
# glPixelTransfer
#
# Python binding unchanged from spec
*/

void glPixelTransferf(GLenum pname, GLfloat param);
DOC(glPixelTransferf, "glPixelTransferf(name, param) -> None")

void glPixelTransferi(GLenum pname, GLint param);
DOC(glPixelTransferi, "glPixelTransferi(name, param) -> None")


/*
# glPixelZoom
#
# Python binding unchanged from spec
*/

void glPixelZoom(GLfloat xfactor, GLfloat yfactor);
DOC(glPixelZoom, "glPixelZoom(xfactor, yfactor) -> None")


/*
# glPointSize
#
# Python binding unchanged from spec
*/

void glPointSize(GLfloat size);
DOC(glPointSize, "glPointSize(size) -> None")


/*
# glPolygonMode
#
# Python binding unchanged from spec
*/

void glPolygonMode(GLenum face, GLenum mode);
DOC(glPolygonMode, "glPolygonMode(face, mode) -> None")


/*
# glPolygonOffset
#
# Python binding unchanged from spec
*/

#if API_VERSION > 256
void glPolygonOffset(GLfloat factor, GLfloat units);
DOC(glPolygonOffset, "glPolygonOffset(factor, units) -> None")
#endif


/*
# glPolygonStipple
#
# The undecorated version takes a string as the argument "mask"
# and respects pixel storage settings.
#
# The decorated version takes a multidimensional array as the
# mask parameter and ignores and pixel storage settings.
*/

void glPolygonStipple(const void *buffer);
DOC(glPolygonStipple, "glPolygonStipple(mask) -> None")

%{
void glPolygonStippleub (const GLubyte *mask)
{
	GLubyte packed[128];
	int i, j;
	
	glPixelStorei(GL_UNPACK_SWAP_BYTES, 0);
	glPixelStorei(GL_UNPACK_LSB_FIRST, 1);

	for (i = 0; i < 128; i++)
	{
		packed[i] = 0;
		for (j = 0; j < 8; j++) packed[i] += mask[8*i + j] << j;
	}
	
	glPolygonStipple(packed);
}
%}

void glPolygonStippleub(const GLubyte *mask);
DOC(glPolygonStippleub, "glPolygonStippleub(mask[][]) -> None")


/*
# glPopAttrib
#
# Python binding unchanged from spec
*/

void glPopAttrib();
DOC(glPopAttrib, "glPopAttrib() -> None")


/*
# glPopClientAttrib
#
# Python binding unchanged from spec, except that reference counting
# is done on all allocated client memory.
*/

%{
void _glPopClientAttrib()
{
	decrementAllLocks();
	glPopClientAttrib();
}
%}

%name(glPopClientAttrib) void _glPopClientAttrib();
DOC(glPopClientAttrib, "glPopClientAttrib() -> None")


/*
# glPopMatrix
#
# Python binding unchanged from spec
*/

void glPopMatrix();
DOC(glPopMatrix, "glPopMatrix() -> None")


/*
# glPopName
#
# Python binding unchanged from spec
*/

void glPopName(void);
DOC(glPopName, "glPopName() -> None")


/*
# glPrioritizeTextures
#
# The "count" parameter of the C prototype is automatically
# derived from the length of the "textures" array.
*/

void glPrioritizeTextures(GLsizei n_1, const GLuint *textures, const GLclampf *priorities);
DOC(glPrioritizeTextures, "glPrioritizeTextures(textures[], priorities[]) -> None")


/*
# glPushAttrib
#
# Python binding unchanged from spec, except that the flag GL_CLIENT_VERTEX_ARRAY_BIT
# is always set and client memory reference counting is done.
*/

void glPushAttrib(GLbitfield mask);
DOC(glPushAttrib, "glPushAttrib(mask) -> None")

%{
#ifndef GL_CLIENT_VERTEX_ARRAY_BIT
#define GL_CLIENT_VERTEX_ARRAY_BIT        0x00000002
#endif

void _glPushClientAttrib (GLbitfield mask)
{
	mask |= GL_CLIENT_VERTEX_ARRAY_BIT;

	incrementAllLocks();
	glPushClientAttrib(mask);
}

%}

%name(glPushClientAttrib) void _glPushClientAttrib(GLbitfield mask);
DOC(glPushClientAttrib, "glPushClientAttrib(mask) -> None")


/*
# glPushMatrix
#
# Python binding unchanged from spec
*/

void glPushMatrix();
DOC(glPushMatrix, "glPushMatrix() -> None")


/*
# glPushName
#
# Python binding unchanged from spec
*/

void glPushName(GLuint name);
DOC(glPushName, "glPushName(name) -> None")


/*
# glRasterPos
#
# Python binding unchanged from spec, except for the addition of
# the utility functions.
*/

void glRasterPos2d(GLdouble x, GLdouble y);
DOC(glRasterPos2d, "glRasterPos2d(x, y) -> None")

void glRasterPos2dv(const GLdouble *v);
DOC(glRasterPos2dv, "glRasterPos2dv(v) -> None")

void glRasterPos2f(GLfloat x, GLfloat y);
DOC(glRasterPos2f, "glRasterPos2f(x, y) -> None")

void glRasterPos2fv(const GLfloat *v);
DOC(glRasterPos2fv, "glRasterPos2fv(v) -> None")

void glRasterPos2i(GLint x, GLint y);
DOC(glRasterPos2i, "glRasterPos2i(x, y) -> None")

void glRasterPos2iv(const GLint *v);
DOC(glRasterPos2iv, "glRasterPos2iv(v) -> None")

void glRasterPos2s(GLshort x, GLshort y);
DOC(glRasterPos2s, "glRasterPos2s(x, y) -> None")

void glRasterPos2sv(const GLshort *v);
DOC(glRasterPos2sv, "glRasterPos2sv(v) -> None")

void glRasterPos3d(GLdouble x, GLdouble y, GLdouble z);
DOC(glRasterPos3d, "glRasterPos3d(x, y, z) -> None")

void glRasterPos3dv(const GLdouble *v);
DOC(glRasterPos3dv, "glRasterPos3dv(v) -> None")

void glRasterPos3f(GLfloat x, GLfloat y, GLfloat z);
DOC(glRasterPos3f, "glRasterPos3f(x, y, z) -> None")

void glRasterPos3fv(const GLfloat *v);
DOC(glRasterPos3fv, "glRasterPos3fv(v) -> None")

void glRasterPos3i(GLint x, GLint y, GLint z);
DOC(glRasterPos3i, "glRasterPos3i(x, y, z) -> None")

void glRasterPos3iv(const GLint *v);
DOC(glRasterPos3iv, "glRasterPos3iv(v) -> None")

void glRasterPos3s(GLshort x, GLshort y, GLshort z);
DOC(glRasterPos3s, "glRasterPos3s(x, y, z) -> None")

void glRasterPos3sv(const GLshort *v);
DOC(glRasterPos3sv, "glRasterPos3sv(v) -> None")

void glRasterPos4d(GLdouble x, GLdouble y, GLdouble z, GLdouble w);
DOC(glRasterPos4d, "glRasterPos4d(x, y, z, w) -> None")

void glRasterPos4dv(const GLdouble *v);
DOC(glRasterPos4dv, "glRasterPos4dv(v) -> None")

void glRasterPos4f(GLfloat x, GLfloat y, GLfloat z, GLfloat w);
DOC(glRasterPos4f, "glRasterPos4f(x, y, z, w) -> None")

void glRasterPos4fv(const GLfloat *v);
DOC(glRasterPos4fv, "glRasterPos4fv(v) -> None")

void glRasterPos4i(GLint x, GLint y, GLint z, GLint w);
DOC(glRasterPos4i, "glRasterPos4i(x, y, z, w) -> None")

void glRasterPos4iv(const GLint *v);
DOC(glRasterPos4iv, "glRasterPos4iv(v) -> None")

void glRasterPos4s(GLshort x, GLshort y, GLshort z, GLshort w);
DOC(glRasterPos4s, "glRasterPos4s(x, y, z, w) -> None")

void glRasterPos4sv(const GLshort *v);
DOC(glRasterPos4sv, "glRasterPos4sv(v) -> None")

%shadow %{
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

%}


/*
# glReadBuffer
#
# Python binding unchanged from spec
*/

void glReadBuffer(GLenum mode);
DOC(glReadBuffer, "glReadBuffer(mode) -> None")


/*
# glReadPixels
#
# The result is returned instead of being passed as a parameter.  The decorated functions
# return a multidimensional array instead of packed string which respects the pixel
# storage settings.
*/

%{
PyObject* _glReadPixels (GLint x, GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type)
{
	PyObject* result;
	int size;
	GLint dims[2];
	void* data = NULL;
	
	dims[0] = width;
	dims[1] = height;
	data = SetupRawPixelRead(format, type, 2, dims, &size);
	if (!data) return NULL;
	
	glReadPixels(x, y, width, height, format, type, data);
	result = PyString_FromStringAndSize((const char*)data, size);
	PyMem_Del(data);

	return result;
}
%}

%name(glReadPixels) PyObject* _glReadPixels(GLint x, GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type);
DOC(glReadPixels, "glReadPixels(x, y, width, height, format, type) -> pixels")

%{
PyObject* __glReadPixels (GLint x, GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type)
{
	int dims[3];
	void* data;

	dims[0] = width;
	dims[1] = height;

	data = SetupPixelRead(2, format, type, dims);
	if (!data) return NULL;

	glReadPixels(x, y, width, height, format, type, data);
	
	return _PyObject_FromArray(type, (dims[2] == 1) ? 2 : 3, dims, data, 1);
}
%}

%name(glReadPixelsub) PyObject* __glReadPixels(GLint x, GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type_UNSIGNED_BYTE);
DOC(glReadPixelsub, "glReadPixelsub(x, y, width, height, format) -> pixels[][] | pixels[][][]")

%name(glReadPixelsb) PyObject* __glReadPixels(GLint x, GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type_BYTE);
DOC(glReadPixelsb, "glReadPixelsb(x, y, width, height, format) -> pixels[][] | pixels[][][]")

%name(glReadPixelsus) PyObject* __glReadPixels(GLint x, GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type_UNSIGNED_SHORT);
DOC(glReadPixelsus, "glReadPixelsus(x, y, width, height, format) -> pixels[][] | pixels[][][]")

%name(glReadPixelss) PyObject* __glReadPixels(GLint x, GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type_SHORT);
DOC(glReadPixelss, "glReadPixelss(x, y, width, height, format) -> pixels[][] | pixels[][][]")

%name(glReadPixelsui) PyObject* __glReadPixels(GLint x, GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type_UNSIGNED_INT);
DOC(glReadPixelsui, "glReadPixelsui(x, y, width, height, format) -> pixels[][] | pixels[][][]")

%name(glReadPixelsi) PyObject* __glReadPixels(GLint x, GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type_INT);
DOC(glReadPixelsi, "glReadPixelsi(x, y, width, height, format) -> pixels[][] | pixels[][][]")

%name(glReadPixelsf) PyObject* __glReadPixels(GLint x, GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type_FLOAT);
DOC(glReadPixelsf, "glReadPixelsf(x, y, width, height, format) -> pixels[][] | pixels[][][]")

%name(glReadPixelsd) PyObject* __glReadPixels(GLint x, GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type_DOUBLE);
DOC(glReadPixelsd, "glReadPixelsd(x, y, width, height, format) -> pixels[][] | pixels[][][]")


/*
# glRect
#
# Python binding unchanged from spec
*/

void glRectd(GLdouble x1, GLdouble y1, GLdouble x2, GLdouble y2);
DOC(glRectd, "glRectd(x1, y1, x2, y2) -> None")

void glRectdv(const GLdouble *p1, const GLdouble *p2);
DOC(glRectdv, "glRectdv(p1, p2) -> None")

void glRectf(GLfloat x1, GLfloat y1, GLfloat x2, GLfloat y2);
DOC(glRectf, "glRectf(x1, y1, x2, y2) -> None")

void glRectfv(const GLfloat *p1, const GLfloat *p2);
DOC(glRectfv, "glRectfv(p1, p2) -> None")

void glRecti(GLint x1, GLint y1, GLint x2, GLint y2);
DOC(glRecti, "glRecti(x1, y1, x2, y2) -> None")

void glRectiv(const GLint *p1, const GLint *p2);
DOC(glRectiv, "glRectiv(p1, p2) -> None")

void glRects(GLshort x1, GLshort y1, GLshort x2, GLshort y2);
DOC(glRects, "glRects(x1, y1, x2, y2) -> None")

void glRectsv(const GLshort *p1, const GLshort *p2);
DOC(glRectsv, "glRectsv(p1, p2) -> None")


/*
# glRenderMode
#
# Instead of returning a "count" value indicating the number of
# entries in a selection or feedback buffer the Python binding
# returns the buffer allocated by glSelectBuffer or glFeedbackBuffer
*/

%{
typedef struct
{
	PyObject_HEAD
	GLint count;
	GLint vertex_len;
	GLfloat* buffer;
	GLint* pos;
} PyFeedbackBuffer;


static int PyFeedbackBuffer_Length(PyObject *self)
{
	return ((PyFeedbackBuffer*)self)->count;
}


static PyObject *PyFeedbackBuffer_GetItem(PyObject *self, int i)
{
	PyObject *result;
	int pos, dims[2];
	GLenum token;
	GLint vertex_count;
	
	if (i < 0) i += ((PyFeedbackBuffer*)self)->count;

	/* Throw an exception if index is out of bounds */
	if (i < 0 || i >= ((PyFeedbackBuffer*)self)->count)
	{
		PyErr_SetString(PyExc_IndexError, "Index out of range.");
		return NULL;
	}
	pos = ((PyFeedbackBuffer*)self)->pos[i];

	result = PyTuple_New(2);
	PyTuple_SetItem(result, 0, PyLong_FromUnsignedLong(token = (GLenum)((PyFeedbackBuffer*)self)->buffer[pos++]));
	if (token == GL_PASS_THROUGH_TOKEN)
	{
		/* pass through has a single value */
		PyTuple_SetItem(result, 1, PyFloat_FromDouble(((PyFeedbackBuffer*)self)->buffer[pos]));
	}
	else
	{
		/* figure out how many vertices there are */
		switch (token)
		{
		case GL_POINT_TOKEN:
		case GL_BITMAP_TOKEN:
		case GL_DRAW_PIXEL_TOKEN:
		case GL_COPY_PIXEL_TOKEN:
			vertex_count = 1;
			break;
		case GL_LINE_TOKEN:
		case GL_LINE_RESET_TOKEN:
			vertex_count = 2;
			break;
		case GL_POLYGON_TOKEN:
			vertex_count = (GLint)((PyFeedbackBuffer*)self)->buffer[pos++];
			break;
		default:
			Py_DECREF(result);
			PyErr_SetString(PyExc_Exception, "Unknown token found in feedback buffer.");
			return NULL;
		}
		
		dims[0] = vertex_count;
		dims[1] = ((PyFeedbackBuffer*)self)->vertex_len;
		PyTuple_SetItem(result, 1, _PyObject_FromFloatArray(2, dims, ((PyFeedbackBuffer*)self)->buffer + pos, 0));
	}

	return result;
}


static void PyFeedbackBuffer_Del(PyObject *self)
{
	PyMem_Del(((PyFeedbackBuffer*)self)->buffer);
	PyMem_Del(((PyFeedbackBuffer*)self)->pos);
    PyObject_Del(self);
}


static PySequenceMethods PyFeedbackBuffer_SequenceMethods =
{
    PyFeedbackBuffer_Length,	/* sq_length */
    NULL,						/* nb_add */
    NULL,						/* nb_multiply */
    PyFeedbackBuffer_GetItem,	/* sq_item */
};


PyTypeObject PyFeedbackBuffer_Type =
{
    PyObject_HEAD_INIT(0)
    0,									/* ob_size */
    "FeedbackBuffer",					/* tp_name */
    sizeof(PyFeedbackBuffer),			/* tp_basicsize */
    0,									/* tp_itemsize */
    PyFeedbackBuffer_Del,				/* tp_dealloc */
    NULL,								/* tp_print */
    NULL,								/* tp_getattr */
    NULL,								/* tp_setattr */
    NULL,								/* tp_compare */
    NULL,								/* tp_repr */
    NULL,								/* tp_as_number */
    &PyFeedbackBuffer_SequenceMethods,	/* tp_as_sequence */
};


PyObject* PyFeedbackBuffer_New(GLint value_count)
{
	/* Initialise a Python-friendly Feedback-buffer wrapper
	
		glRenderMode returns length of the buffer not the number of 
		records  So value_count is the number of GLfloat values 
		currently in the buffer, it will always be a lower value 
		than that specified in the glFeedbackBuffer() call.
	*/
	int len;
	int color_len;
	int texture_len;
	GLboolean rgba_mode;
	GLenum type;
	PyFeedbackBuffer *result = PyObject_NEW(PyFeedbackBuffer, &PyFeedbackBuffer_Type);

	/* explicitly initialise just to be safe... */
	result->count = 0;
	result->vertex_len = 0;
	result->buffer = NULL;
	result->pos = NULL;
	
	/* Get the buffer type and color mode so we can calculate the length of a vertex */
#ifdef GL_VERSION_1_1
	glGetPointerv(GL_FEEDBACK_BUFFER_POINTER, (void**)&result->buffer);
	glGetIntegerv(GL_FEEDBACK_BUFFER_TYPE, (GLint*)&type);
#else
	PyGLcontext *context = GetGLcontext();
	result->buffer = context->feedback_buffer;
	type = context->feedback_type;
#endif
	glGetBooleanv(GL_RGBA_MODE, &rgba_mode);
	/* Stop anyone writing to the buffer we're wrapping 
	
		This is only necessary if something else is manipulating
		the feedback buffer (i.e. not PyOpenGL).
	*/
	glFeedbackBuffer(0, type, null_feedback_buffer);


	/* Calculate the length of a vertex */
	color_len = ((rgba_mode) ? 4 : 1);
	texture_len = 4;

	switch (type)
	{
	case GL_2D:
		result->vertex_len = 2;
		break;
	case GL_3D:
		result->vertex_len = 3;
		break;
	case GL_3D_COLOR:
		result->vertex_len = 3 + color_len;
		break;
	case GL_3D_COLOR_TEXTURE:
		result->vertex_len = 3 + color_len + texture_len;
		break;
	case GL_4D_COLOR_TEXTURE:
		result->vertex_len = 4 + color_len + texture_len;
		break;
	default:
		Py_DECREF(result);
		PyErr_SetString(PyExc_Exception, "Unknown vertex type in feedback buffer.");
		return NULL;
	}
	result->pos = PyMem_New(GLint, 1);
	/* Go through the buffer and find the position of each item */
	for (len = 0; len < value_count;)
	{
		result->count += 1;
		/* add new slot for position-entry */
		result->pos = PyMem_Resize(result->pos, GLint, result->count); 
		/* store current read-position */
		result->pos[result->count-1] = len;

		switch ((GLenum)result->buffer[len++])
		{
		case GL_POINT_TOKEN:
		case GL_BITMAP_TOKEN:
		case GL_DRAW_PIXEL_TOKEN:
		case GL_COPY_PIXEL_TOKEN:
			len += result->vertex_len;
			break;
		case GL_LINE_TOKEN:
		case GL_LINE_RESET_TOKEN:
			len += 2*result->vertex_len;
			break;
		case GL_POLYGON_TOKEN:
			len += (int)result->buffer[len++]*result->vertex_len;
			break;
		case GL_PASS_THROUGH_TOKEN:
			len++;
			break;
		default:
			Py_DECREF(result);
			PyErr_SetString(PyExc_Exception, "Unknown token found in feedback buffer.");
			return NULL;
		};
	}
	return (PyObject*)result;
}


typedef struct
{
	PyObject_HEAD
	GLint count;
	GLuint* buffer;
	GLint* pos;
} PySelectBuffer;


static int PySelectBuffer_Length(PyObject *self)
{
	return ((PySelectBuffer*)self)->count;
}


static PyObject *PySelectBuffer_GetItem(PyObject *self, int i)
{
	PyObject *result, *names;
	int pos,j;
	GLint name_count;
	
	if (i < 0) i += ((PySelectBuffer*)self)->count;

	/* Throw an exception if out of bounds */
	if (i < 0 || i >= ((PySelectBuffer*)self)->count)
	{
		PyErr_SetString(PyExc_IndexError, "Index out of range.");
		return NULL;
	}
	pos = ((PySelectBuffer*)self)->pos[i];

	/* Create the element */
	result = PyTuple_New(3);

	PyTuple_SetItem(result, 2, names = PyTuple_New(name_count = ((PySelectBuffer*)self)->buffer[pos++]));

	PyTuple_SetItem(result, 0, PyLong_FromUnsignedLong(((PySelectBuffer*)self)->buffer[pos++]));
	PyTuple_SetItem(result, 1, PyLong_FromUnsignedLong(((PySelectBuffer*)self)->buffer[pos++]));
		
	for (j = 0; j < name_count; j++, pos++) PyTuple_SetItem(names, j, PyLong_FromUnsignedLong(((PySelectBuffer*)self)->buffer[pos]));
	
	return result;
}


static void PySelectBuffer_Del(PyObject *self)
{
	PyMem_Del(((PySelectBuffer*)self)->buffer);
	PyMem_Del(((PySelectBuffer*)self)->pos);
    PyObject_Del(self);
}


static PySequenceMethods PySelectBuffer_SequenceMethods =
{
    PySelectBuffer_Length,		/* sq_length */
    NULL,						/* nb_add */
    NULL,						/* nb_multiply */
    PySelectBuffer_GetItem,		/* sq_item */
};


PyTypeObject PySelectBuffer_Type =
{
    PyObject_HEAD_INIT(0)
    0,									/* ob_size */
    "SelectBuffer",						/* tp_name */
    sizeof(PySelectBuffer),				/* tp_basicsize */
    0,									/* tp_itemsize */
    PySelectBuffer_Del,					/* tp_dealloc */
    NULL,								/* tp_print */
    NULL,								/* tp_getattr */
    NULL,								/* tp_setattr */
    NULL,								/* tp_compare */
    NULL,								/* tp_repr */
    NULL,								/* tp_as_number */
    &PySelectBuffer_SequenceMethods,	/* tp_as_sequence */
};

/* Work around for GL bug (Microsoft?) */
static GLuint null_select_buffer[1];


PyObject* PySelectBuffer_New(GLint count)
{
	int len, i;
	PySelectBuffer *result = PyObject_NEW(PySelectBuffer, &PySelectBuffer_Type);
	
#ifdef GL_VERSION_1_1
	glGetPointerv(GL_SELECTION_BUFFER_POINTER, (void**)&result->buffer);
#else
	PyGLcontext *context = GetGLcontext();
	result->buffer = context->selection_buffer;
	context->selection_buffer = null_select_buffer;
#endif
	glSelectBuffer(0, null_select_buffer);

	result->count = count;
	result->pos = PyMem_New(GLint, count);

	/* Go through the buffer and find the location of each item, so random access is possible */
	/* Calculate the total length at the same time */
	for (len = i = 0; i < count; i++)
	{
		result->pos[i] = len;
		len += 3 + result->buffer[len];
	}
	
	return (PyObject*)result;
}

PyObject* _glRenderMode (GLenum mode)
{
	GLint previous_mode, count;

	glGetIntegerv(GL_RENDER_MODE, &previous_mode);
	count = glRenderMode(mode);
	
	/* count == -1 means that there wasn't enough space in the buffer */
	/* Sould this be an exception? */
	if (count > -1) {
		switch (previous_mode)
		{
		case GL_SELECT:
			return PySelectBuffer_New(count);
		case GL_FEEDBACK:
			return PyFeedbackBuffer_New(count);
		}
		
		Py_INCREF(Py_None);
		return Py_None;
	} else {
		switch( previous_mode) {
			case GL_SELECT:
				PyErr_SetGLErrorMessage( GL_STACK_OVERFLOW, "glSelectBuffer too small to hold selection results" );
				break;
			case GL_FEEDBACK:
				PyErr_SetGLErrorMessage( GL_STACK_OVERFLOW, "glFeedbackBuffer too small to hold feedback results" );
				break;
			default:
				PyErr_SetGLErrorMessage( GL_NO_ERROR, "Unspecified error in glRenderMode" );
		}
		return NULL;
	}
}
%}

%name(glRenderMode) PyObject* _glRenderMode(GLenum mode);
DOC(glRenderMode, "glRenderMode(mode) -> None | FeedbackBuffer | SelectBuffer")


/*
# glRotate
#
# Python binding unchanged from spec, with the addition of the alias
*/

void glRotated(GLdouble angle, GLdouble x, GLdouble y, GLdouble z);
DOC(glRotated, "glRotated(angle, x, y, z) -> None")

void glRotatef(GLfloat angle, GLfloat x, GLfloat y, GLfloat z);
DOC(glRotatef, "glRotatef(angle, x, y, z) -> None")


%shadow %{
glRotate = _GL__init__.glRotated
%}



/*
# glScale
#
# Python binding unchanged from spec, with the addition of the alias
*/

void glScaled(GLdouble x, GLdouble y, GLdouble z);
DOC(glScaled, "glScaled(x, y, z) -> None")

void glScalef(GLfloat x, GLfloat y, GLfloat z);
DOC(glScalef, "glScalef(x, y, z) -> None")


%shadow %{
glScale = _GL__init__.glScaled
%}



/*
# glScissor
#
# Python binding unchanged from spec
*/

void glScissor(GLint x, GLint y, GLsizei width, GLsizei height);
DOC(glScissor, "glScissor(x, y, width, height) -> None")


/*
# glSelectBuffer
#
# The "buffer" parameter is omitted.  Instead a buffer of "size" is allocated
# and returned by glRenderMode
*/

%{
void _glSelectBuffer(GLsizei size)
{
	GLuint *buffer = (size > 0) ? PyMem_New(GLuint, size) : null_select_buffer;
#ifndef GL_VERSION_1_1
	PyGLcontext *context = GetGLcontext();
	context->selection_buffer = buffer;
#endif
	glSelectBuffer(size, buffer);
}
%}

%name(glSelectBuffer) void _glSelectBuffer(GLsizei size);
DOC(glSelectBuffer, "glSelectBuffer(size) -> None")


/*
# glSelectWithCallback
#
# Backwards compatible selection function.
*/


%shadow %{
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

%}



/*
# glShadeModel
#
# Python binding unchanged from spec
*/

void glShadeModel(GLenum mode);
DOC(glShadeModel, "glShadeModel(mode) -> None")


/*
# glStencilFunc
#
# Python binding unchanged from spec
*/

void glStencilFunc(GLenum func, GLint ref, GLuint mask);
DOC(glStencilFunc, "glStencilFunc(func, ref, mask) -> None")


/*
# glStencilMask
#
# Python binding unchanged from spec
*/

void glStencilMask(GLuint mask);
DOC(glStencilMask, "glStencilMask(mask) -> None")


/*
# glStencilOp
#
# Python binding unchanged from spec
*/

void glStencilOp(GLenum fail, GLenum zfail, GLenum zpass);
DOC(glStencilOp, "glStencilOp(fail, zfail, zpass) -> None")


/*
# glTexCoordPointer
# 
# The glTexCoordPointer function is unchanged from the spec, but the
# Python binding adds the decorated variants which take a multidimensional
# array as the data source and set the "size", "type", and "stride"
# arguments as appropriate.
*/

#if API_VERSION > 256
%{
void _glTexCoordPointer(GLint size, GLenum type, GLsizei stride, GLvoid *pointer)
{
	decrementPointerLock(GL_TEXTURE_COORD_ARRAY_POINTER);
	acquire(pointer);
	glTexCoordPointer(size, type, stride, pointer);
}
%}

%name(glTexCoordPointer) void _glTexCoordPointer(GLint size, GLenum type, GLsizei stride, void *pointer);
DOC(glTexCoordPointer, "glTexCoordPointer(size, type, stride, pointer) -> None")

%name(glTexCoordPointerb) void _glTexCoordPointer(GLint d_3_1, GLenum type_BYTE, GLsizei stride_0, GLbyte* pointer);
DOC(glTexCoordPointerb, "glTexCoordPointerub(pointer[][]) -> None")

%name(glTexCoordPointers) void _glTexCoordPointer(GLint d_3_1, GLenum type_SHORT, GLsizei stride_0, GLshort* pointer);
DOC(glTexCoordPointers, "glTexCoordPointers(pointer[][]) -> None")

%name(glTexCoordPointeri) void _glTexCoordPointer(GLint d_3_1, GLenum type_INT, GLsizei stride_0, GLint* pointer);
DOC(glTexCoordPointeri, "glTexCoordPointeri(pointer[][]) -> None")

%name(glTexCoordPointerf) void _glTexCoordPointer(GLint d_3_1, GLenum type_FLOAT, GLsizei stride_0, GLfloat* pointer);
DOC(glTexCoordPointerf, "glTexCoordPointerf(pointer[][]) -> None")

%name(glTexCoordPointerd) void _glTexCoordPointer(GLint d_3_1, GLenum type_DOUBLE, GLsizei stride_0, GLdouble* pointer);
DOC(glTexCoordPointerd, "glTexCoordPointerd(pointer[][]) -> None")
#endif


/*
# glTexEnv
#
# Python binding unchanged from spec
*/

void glTexEnvf(GLenum target, GLenum pname, GLfloat param);
DOC(glTexEnvf, "glTexEnvf(target, pname, param) -> None")

void glTexEnvfv(GLenum target, GLenum pname, const GLfloat *v);
DOC(glTexEnvfv, "glTexEnvfv(target, pname, v) -> None")

void glTexEnvi(GLenum target, GLenum pname, GLint param);
DOC(glTexEnvi, "glTexEnvi(target, pname, param) -> None")

void glTexEnviv(GLenum target, GLenum pname, const GLint *v);
DOC(glTexEnviv, "glTexEnviv(target, pname, v) -> None")


/*
# glTexGen
#
# Python binding unchanged from spec, with addition of the alias
*/

void glTexGend(GLenum coord, GLenum pname, GLdouble param);
DOC(glTexGend, "glTexGend(coord, pname, param) -> None")

void glTexGendv(GLenum coord, GLenum pname, const GLdouble *v);
DOC(glTexGendv, "glTexGendv(coord, pname, v) -> None")

void glTexGenf(GLenum coord, GLenum pname, GLfloat param);
DOC(glTexGenf, "glTexGenf(coord, pname, param) -> None")

void glTexGenfv(GLenum coord, GLenum pname, const GLfloat *v);
DOC(glTexGenfv, "glTexGenfv(coord, pname, v) -> None")

void glTexGeni(GLenum coord, GLenum pname, GLint param);
DOC(glTexGeni, "glTexGeni(coord, pname, param) -> None")

void glTexGeniv(GLenum coord, GLenum pname, const GLint *v);
DOC(glTexGeniv, "glTexGeniv(coord, pname, v) -> None")


%shadow %{
glTexGen = _GL__init__.glTexGendv
%}


/*
# glTexImage1D
#
# Python binding unchanged from spec, with the addition of the
# decorated utility functions which calculate all image size and
# type parameters automatically.
*/

void glTexImage1D(GLenum target, GLint level, GLint internalFormat, GLsizei width, GLint border, GLenum format, GLenum type, const void *buffer);
DOC(glTexImage1D, "glTexImage1D(target, level, internalFormat, width, border, format, type, pixels) -> None")

%{
void _glTexImage1D(GLenum target, GLint level, GLint internalFormat, GLsizei width, GLint border, GLenum format, GLenum type, const GLvoid* pixels)
{
	SetupPixelWrite(1);
	glTexImage1D(target, level, internalFormat, width, border, format, type, pixels);
}
%}

%name(glTexImage1Dub) void _glTexImage1D(GLenum target, GLint level, GLint internalFormat, GLsizei d_7_0, GLint border, GLenum format, GLenum type_UNSIGNED_BYTE, const GLubyte *pixels);
DOC(glTexImage1Dub, "glTexImage1Dub(target, level, internalFormat, border, format, pixels[] | pixels[][]) -> None")

%name(glTexImage1Db) void _glTexImage1D(GLenum target, GLint level, GLint internalFormat, GLsizei d_7_0, GLint border, GLenum format, GLenum type_BYTE, const GLbyte *pixels);
DOC(glTexImage1Db, "glTexImage1Db(target, level, internalFormat, border, format, pixels[] | pixels[][]) -> None")

%name(glTexImage1Dus) void _glTexImage1D(GLenum target, GLint level, GLint internalFormat, GLsizei d_7_0, GLint border, GLenum format, GLenum type_UNSIGNED_SHORT, const GLushort *pixels);
DOC(glTexImage1Dus, "glTexImage1Dus(target, level, internalFormat, border, format, pixels[] | pixels[][]) -> None")

%name(glTexImage1Ds) void _glTexImage1D(GLenum target, GLint level, GLint internalFormat, GLsizei d_7_0, GLint border, GLenum format, GLenum type_SHORT, const GLshort *pixels);
DOC(glTexImage1Ds, "glTexImage1Ds(target, level, internalFormat, border, format, pixels[] | pixels[][]) -> None")

%name(glTexImage1Dui) void _glTexImage1D(GLenum target, GLint level, GLint internalFormat, GLsizei d_7_0, GLint border, GLenum format, GLenum type_UNSIGNED_INT, const GLuint *pixels);
DOC(glTexImage1Dui, "glTexImage1Dui(target, level, internalFormat, border, format, pixels[] | pixels[][]) -> None")

%name(glTexImage1Di) void _glTexImage1D(GLenum target, GLint level, GLint internalFormat, GLsizei d_7_0, GLint border, GLenum format, GLenum type_INT, const GLint *pixels);
DOC(glTexImage1Di, "glTexImage1Di(target, level, internalFormat, border, format, pixels[] | pixels[][]) -> None")

%name(glTexImage1Df) void _glTexImage1D(GLenum target, GLint level, GLint internalFormat, GLsizei d_7_0, GLint border, GLenum format, GLenum type_FLOAT, const GLfloat *pixels);
DOC(glTexImage1Df, "glTexImage1Df(target, level, internalFormat, border, format, pixels[] | pixels[][]) -> None")


/*
# glTexImage2D
#
# Python binding unchanged from spec, with the addition of the
# decorated utility functions which calculate all image size and
# type parameters automatically.
*/

void glTexImage2D(GLenum target, GLint level, GLint internalFormat, GLsizei width, GLsizei height, GLint border, GLenum format, GLenum type, const void *buffer);
DOC(glTexImage2D, "glTexImage2D(target, level, internalFormat, width, height, border, format, type, pixels) -> None")

%{
void _glTexImage2D(GLenum target, GLint level, GLint internalFormat, GLsizei width, GLsizei height, GLint border, GLenum format, GLenum type, const GLvoid* pixels)
{
	SetupPixelWrite(2);
	glTexImage2D(target, level, internalFormat, width, height, border, format, type, pixels);
}
%}

%name(glTexImage2Dub) void _glTexImage2D(GLenum target, GLint level, GLint internalFormat, GLsizei d_8_1, GLsizei d_8_0, GLint border, GLenum format, GLenum type_UNSIGNED_BYTE, const GLubyte *pixels);
DOC(glTexImage2Dub, "glTexImage2Dub(target, level, internalFormat, border, format, pixels[][] | pixels[][][]) -> None")

%name(glTexImage2Db) void _glTexImage2D(GLenum target, GLint level, GLint internalFormat, GLsizei d_8_1, GLsizei d_8_0, GLint border, GLenum format, GLenum type_BYTE, const GLbyte *pixels);
DOC(glTexImage2Db, "glTexImage2Db(target, level, internalFormat, border, format, pixels[][] | pixels[][][]) -> None")

%name(glTexImage2Dus) void _glTexImage2D(GLenum target, GLint level, GLint internalFormat, GLsizei d_8_1, GLsizei d_8_0, GLint border, GLenum format, GLenum type_UNSIGNED_SHORT, const GLushort *pixels);
DOC(glTexImage2Dus, "glTexImage2Dus(target, level, internalFormat, border, format, pixels[][] | pixels[][][]) -> None")

%name(glTexImage2Ds) void _glTexImage2D(GLenum target, GLint level, GLint internalFormat, GLsizei d_8_1, GLsizei d_8_0, GLint border, GLenum format, GLenum type_SHORT, const GLshort *pixels);
DOC(glTexImage2Ds, "glTexImage2Ds(target, level, internalFormat, border, format, pixels[][] | pixels[][][]) -> None")

%name(glTexImage2Dui) void _glTexImage2D(GLenum target, GLint level, GLint internalFormat, GLsizei d_8_1, GLsizei d_8_0, GLint border, GLenum format, GLenum type_UNSIGNED_INT, const GLuint *pixels);
DOC(glTexImage2Dui, "glTexImage2Dui(target, level, internalFormat, border, format, pixels[][] | pixels[][][]) -> None")

%name(glTexImage2Di) void _glTexImage2D(GLenum target, GLint level, GLint internalFormat, GLsizei d_8_1, GLsizei d_8_0, GLint border, GLenum format, GLenum type_INT, const GLint *pixels);
DOC(glTexImage2Di, "glTexImage2Di(target, level, internalFormat, border, format, pixels[][] | pixels[][][]) -> None")

%name(glTexImage2Df) void _glTexImage2D(GLenum target, GLint level, GLint internalFormat, GLsizei d_8_1, GLsizei d_8_0, GLint border, GLenum format, GLenum type_FLOAT, const GLfloat *pixels);
DOC(glTexImage2Df, "glTexImage2Df(target, level, internalFormat, border, format, pixels[][] | pixels[][][]) -> None")


/*
# glTexParameter
#
# Python binding unchanged from spec, with the addition of the alias
*/

void glTexParameterf(GLenum target, GLenum pname, GLfloat param);
DOC(glTexParameterf, "glTexParameterf(target, pname, param) -> None")

void glTexParameterfv(GLenum target, GLenum pname, const GLfloat *v);
DOC(glTexParameterfv, "glTexParameterfv(target, pname, v) -> None")

void glTexParameteri(GLenum target, GLenum pname, GLint param);
DOC(glTexParameteri, "glTexParameteri(target, pname, param) -> None")

void glTexParameteriv(GLenum target, GLenum pname, const GLint *v);
DOC(glTexParameteriv, "glTexParameteriv(target, pname, v) -> None")

%shadow %{
glTexParameter = _GL__init__.glTexParameterfv
%}

/*
# glTexSubImage1D
#
# Python binding unchanged from spec, with the addition of the
# decorated utility functions which calculate all image size and
# type parameters automatically.
*/

void glTexSubImage1D(GLenum target, GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum type, const void *buffer);
DOC(glTexSubImage1D, "glTexSubImage1D(target, level, xoffset, width, format, type, pixels) -> None")

%{
void _glTexSubImage1D(GLenum target, GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum type, const GLvoid* pixels)
{
	SetupPixelWrite(1);
	glTexSubImage1D(target, level, xoffset, width, format, type, pixels);
}
%}

%name(glTexSubImage1Dub) void _glTexSubImage1D(GLenum target, GLint level, GLint xoffset, GLsizei d_6_0, GLenum format, GLenum type_UNSIGNED_BYTE, const GLubyte *pixels);
DOC(glTexSubImage1Dub, "glTexSubImage1Dub(target, level, xoffset, format, type, pixels[] | pixels[][]) -> None")

%name(glTexSubImage1Db) void _glTexSubImage1D(GLenum target, GLint level, GLint xoffset, GLsizei d_6_0, GLenum format, GLenum type_BYTE, const GLbyte *pixels);
DOC(glTexSubImage1Db, "glTexSubImage1Db(target, level, xoffset, format, type, pixels[] | pixels[][]) -> None")

%name(glTexSubImage1Dus) void _glTexSubImage1D(GLenum target, GLint level, GLint xoffset, GLsizei d_6_0, GLenum format, GLenum type_UNSIGNED_SHORT, const GLushort *pixels);
DOC(glTexSubImage1Dus, "glTexSubImage1Dus(target, level, xoffset, format, type, pixels[] | pixels[][]) -> None")

%name(glTexSubImage1Ds) void _glTexSubImage1D(GLenum target, GLint level, GLint xoffset, GLsizei d_6_0, GLenum format, GLenum type_SHORT, const GLshort *pixels);
DOC(glTexSubImage1Ds, "glTexSubImage1Ds(target, level, xoffset, format, type, pixels[] | pixels[][]) -> None")

%name(glTexSubImage1Dui) void _glTexSubImage1D(GLenum target, GLint level, GLint xoffset, GLsizei d_6_0, GLenum format, GLenum type_UNSIGNED_INT, const GLuint *pixels);
DOC(glTexSubImage1Dui, "glTexSubImage1Dui(target, level, xoffset, format, type, pixels[] | pixels[][]) -> None")

%name(glTexSubImage1Di) void _glTexSubImage1D(GLenum target, GLint level, GLint xoffset, GLsizei d_6_0, GLenum format, GLenum type_INT, const GLint *pixels);
DOC(glTexSubImage1Di, "glTexSubImage1Di(target, level, xoffset, format, type, pixels[] | pixels[][]) -> None")

%name(glTexSubImage1Df) void _glTexSubImage1D(GLenum target, GLint level, GLint xoffset, GLsizei d_6_0, GLenum format, GLenum type_FLOAT, const GLfloat *pixels);
DOC(glTexSubImage1Df, "glTexSubImage1Df(target, level, xoffset, format, type, pixels[] | pixels[][]) -> None")
	

/*
# glTexSubImage2D
#
# Python binding unchanged from spec, with the addition of the
# decorated utility functions which calculate all image size and
# type parameters automatically.
*/

void glTexSubImage2D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, const void *buffer);
DOC(glTexSubImage2D, "glTexSubImage2D(target, level, xoffset, yoffset, width, height, format, type, pixels) -> None")

%{
void _glTexSubImage2D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, const GLvoid* pixels)
{
	SetupPixelWrite(2);
	glTexSubImage2D(target, level, xoffset, yoffset, width, height, format, type, pixels);
}
%}

%name(glTexSubImage2Dub) void _glTexSubImage2D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei d_8_1, GLsizei d_8_0, GLenum format, GLenum type_UNSIGNED_BYTE, const GLubyte *pixels);
DOC(glTexSubImage2Dub, "glTexSubImage2Dub(target, level, xoffset, yoffset, format, type, pixels[][] | pixels[][][]) -> None")

%name(glTexSubImage2Db) void _glTexSubImage2D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei d_8_1, GLsizei d_8_0, GLenum format, GLenum type_BYTE, const GLbyte *pixels);
DOC(glTexSubImage2Db, "glTexSubImage2Db(target, level, xoffset, yoffset, format, type, pixels[][] | pixels[][][]) -> None")

%name(glTexSubImage2Dus) void _glTexSubImage2D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei d_8_1, GLsizei d_8_0, GLenum format, GLenum type_UNSIGNED_SHORT, const GLushort *pixels);
DOC(glTexSubImage2Dus, "glTexSubImage2Dus(target, level, xoffset, yoffset, format, type, pixels[][] | pixels[][][]) -> None")

%name(glTexSubImage2Ds) void _glTexSubImage2D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei d_8_1, GLsizei d_8_0, GLenum format, GLenum type_SHORT, const GLshort *pixels);
DOC(glTexSubImage2Ds, "glTexSubImage2Ds(target, level, xoffset, yoffset, format, type, pixels[][] | pixels[][][]) -> None")

%name(glTexSubImage2Dui) void _glTexSubImage2D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei d_8_1, GLsizei d_8_0, GLenum format, GLenum type_UNSIGNED_INT, const GLuint *pixels);
DOC(glTexSubImage2Dui, "glTexSubImage2Dui(target, level, xoffset, yoffset, format, type, pixels[][] | pixels[][][]) -> None")

%name(glTexSubImage2Di) void _glTexSubImage2D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei d_8_1, GLsizei d_8_0, GLenum format, GLenum type_INT, const GLint *pixels);
DOC(glTexSubImage2Di, "glTexSubImage2Di(target, level, xoffset, yoffset, format, type, pixels[][] | pixels[][][]) -> None")

%name(glTexSubImage2Df) void _glTexSubImage2D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei d_8_1, GLsizei d_8_0, GLenum format, GLenum type_FLOAT, const GLfloat *pixels);
DOC(glTexSubImage2Df, "glTexSubImage2Df(target, level, xoffset, yoffset, format, type, pixels[][] | pixels[][][]) -> None")


/*
# glTranslate
#
# Python binding unchanged from spec, with the addition of the alias
*/

void glTranslated(GLdouble x, GLdouble y, GLdouble z);
DOC(glTranslated, "glTranslated(x, y, z) -> None")

void glTranslatef(GLfloat x, GLfloat y, GLfloat z);
DOC(glTranslatef, "glTranslatef(x, y, z) -> None")

%shadow %{
glTranslate = _GL__init__.glTranslated
%}



/*
# glVertexPointer
# 
# The glVertexPointer function is unchanged from the spec, but the
# Python binding adds the decorated variants which take a multidimensional
# array as the data source and set the "size", "type", and "stride"
# arguments as appropriate.
*/

#if API_VERSION > 256
%{
void _glVertexPointer(GLint size, GLenum type, GLsizei stride, GLvoid *pointer)
{
	decrementPointerLock(GL_VERTEX_ARRAY_POINTER);
	acquire(pointer);
	glVertexPointer(size, type, stride, pointer);
}
%}

%name(glVertexPointer) void _glVertexPointer(GLint size, GLenum type, GLsizei stride, void *pointer);
DOC(glVertexPointer, "glVertexPointer(size, type, stride, pointer) -> None")

%name(glVertexPointerb) void _glVertexPointer(GLint d_3_1, GLenum type_BYTE, GLsizei stride_0, GLbyte* pointer);
DOC(glVertexPointerb, "glVertexPointerub(pointer[][]) -> None")

%name(glVertexPointers) void _glVertexPointer(GLint d_3_1, GLenum type_SHORT, GLsizei stride_0, GLshort* pointer);
DOC(glVertexPointers, "glVertexPointers(pointer[][]) -> None")

%name(glVertexPointeri) void _glVertexPointer(GLint d_3_1, GLenum type_INT, GLsizei stride_0, GLint* pointer);
DOC(glVertexPointeri, "glVertexPointeri(pointer[][]) -> None")

%name(glVertexPointerf) void _glVertexPointer(GLint d_3_1, GLenum type_FLOAT, GLsizei stride_0, GLfloat* pointer);
DOC(glVertexPointerf, "glVertexPointerf(pointer[][]) -> None")

%name(glVertexPointerd) void _glVertexPointer(GLint d_3_1, GLenum type_DOUBLE, GLsizei stride_0, GLdouble* pointer);
DOC(glVertexPointerd, "glVertexPointerd(pointer[][]) -> None")
#endif


/*
# glViewport
#
# Python binding unchanged from spec
*/

void glViewport(GLint x, GLint y, GLsizei width, GLsizei height);
DOC(glViewport, "glViewport(x, y, width, height) -> None")


#if API_VERSION_WORD >= 258

/* 1.2 imaging extension functions */

/*void glColorTable(GLenum target, GLenum internalformat, GLsizei width, GLenum format, GLenum type, const void *buffer);

void glColorSubTable(GLenum target, GLsizei start, GLsizei count, GLenum format, GLenum type, const void *buffer);

void glColorTableParameteriv(GLenum target, GLenum pname, const GLint *params);

void glColorTableParameterfv(GLenum target, GLenum pname, const GLfloat *params);

void glCopyColorSubTable( GLenum target, GLsizei start, GLint x, GLint y, GLsizei width );

void glCopyColorTable( GLenum target, GLenum internalformat, GLint x, GLint y, GLsizei width );

void glGetColorTable( GLenum target, GLenum format, GLenum type, GLvoid *table ); 

void glGetColorTableParameterfv( GLenum target, GLenum pname, GLfloat params[4] );

void glGetColorTableParameteriv( GLenum target, GLenum pname, GLint params[4] );

void glBlendEquation( GLenum mode );

void glBlendColor( GLclampf red, GLclampf green, GLclampf blue, GLclampf alpha );

void glHistogram( GLenum target, GLsizei width, GLenum internalformat, GLboolean sink );

void glResetHistogram( GLenum target );

void glGetHistogram( GLenum target, GLboolean reset, GLenum format, GLenum type, GLvoid *values );

void glGetHistogramParameterfv( GLenum target, GLenum pname, GLfloat params[4] );

void glGetHistogramParameteriv( GLenum target, GLenum pname, GLint params[4] );

void glMinmax( GLenum target, GLenum internalformat, GLboolean sink );

void glResetMinmax( GLenum target );

void glGetMinmax( GLenum target, GLboolean reset, GLenum format, GLenum types, GLvoid *values );

void glGetMinmaxParameterfv( GLenum target, GLenum pname, GLfloat params[4] );

void glGetMinmaxParameteriv( GLenum target, GLenum pname, GLint params[4] );

void glConvolutionFilter1D( GLenum target, GLenum internalformat, GLsizei width, GLenum format, GLenum type, const void *buffer );

void glConvolutionFilter2D( GLenum target, GLenum internalformat, GLsizei width, GLsizei height, GLenum format, GLenum type, const void *buffer );

void glConvolutionParameterf( GLenum target, GLenum pname, GLfloat params );

void glConvolutionParameterfv( GLenum target, GLenum pname, const GLfloat *params );

void glConvolutionParameteri( GLenum target, GLenum pname, GLint params );

void glConvolutionParameteriv( GLenum target, GLenum pname, const GLint *params );

void glCopyConvolutionFilter1D( GLenum target, GLenum internalformat, GLint x, GLint y, GLsizei width );

void glCopyConvolutionFilter2D( GLenum target, GLenum internalformat, GLint x, GLint y, GLsizei width, GLsizei height);

void glGetConvolutionFilter( GLenum target, GLenum format, GLenum type, GLvoid *image );

void glGetConvolutionParameterfv( GLenum target, GLenum pname, GLfloat params[4] );

void glGetConvolutionParameteriv( GLenum target, GLenum pname, GLint params[4] );

void glSeparableFilter2D( GLenum target, GLenum internalformat, GLsizei width, GLsizei height, GLenum format,
                          GLenum type, const void *buffer, const void *buffer );

void glGetSeparableFilter( GLenum target, GLenum format, GLenum type, GLvoid *row, GLvoid *column, GLvoid *span );
*/
#endif


#if API_VERSION > 256
#define GL_VERSION_1_1   1
#endif

/* AccumOp */
#define GL_ACCUM                          0x0100
#define GL_LOAD                           0x0101
#define GL_RETURN                         0x0102
#define GL_MULT                           0x0103
#define GL_ADD                            0x0104

/* AlphaFunction */
#define GL_NEVER                          0x0200
#define GL_LESS                           0x0201
#define GL_EQUAL                          0x0202
#define GL_LEQUAL                         0x0203
#define GL_GREATER                        0x0204
#define GL_NOTEQUAL                       0x0205
#define GL_GEQUAL                         0x0206
#define GL_ALWAYS                         0x0207

/* AttribMask  */
#define GL_CURRENT_BIT                    0x00000001
#define GL_POINT_BIT                      0x00000002
#define GL_LINE_BIT                       0x00000004
#define GL_POLYGON_BIT                    0x00000008
#define GL_POLYGON_STIPPLE_BIT            0x00000010
#define GL_PIXEL_MODE_BIT                 0x00000020
#define GL_LIGHTING_BIT                   0x00000040
#define GL_FOG_BIT                        0x00000080
#define GL_DEPTH_BUFFER_BIT               0x00000100
#define GL_ACCUM_BUFFER_BIT               0x00000200
#define GL_STENCIL_BUFFER_BIT             0x00000400
#define GL_VIEWPORT_BIT                   0x00000800
#define GL_TRANSFORM_BIT                  0x00001000
#define GL_ENABLE_BIT                     0x00002000
#define GL_COLOR_BUFFER_BIT               0x00004000
#define GL_HINT_BIT                       0x00008000
#define GL_EVAL_BIT                       0x00010000
#define GL_LIST_BIT                       0x00020000
#define GL_TEXTURE_BIT                    0x00040000
#define GL_SCISSOR_BIT                    0x00080000
#define GL_ALL_ATTRIB_BITS                0x000fffff

/* BeginMode */
#define GL_POINTS                         0x0000
#define GL_LINES                          0x0001
#define GL_LINE_LOOP                      0x0002
#define GL_LINE_STRIP                     0x0003
#define GL_TRIANGLES                      0x0004
#define GL_TRIANGLE_STRIP                 0x0005
#define GL_TRIANGLE_FAN                   0x0006
#define GL_QUADS                          0x0007
#define GL_QUAD_STRIP                     0x0008
#define GL_POLYGON                        0x0009

/* BlendingFactorDest */
#define GL_ZERO                           0
#define GL_ONE                            1
#define GL_SRC_COLOR                      0x0300
#define GL_ONE_MINUS_SRC_COLOR            0x0301
#define GL_SRC_ALPHA                      0x0302
#define GL_ONE_MINUS_SRC_ALPHA            0x0303
#define GL_DST_ALPHA                      0x0304
#define GL_ONE_MINUS_DST_ALPHA            0x0305

/* BlendingFactorSrc */
#define GL_DST_COLOR                      0x0306
#define GL_ONE_MINUS_DST_COLOR            0x0307
#define GL_SRC_ALPHA_SATURATE             0x0308

/* Boolean */
#define GL_TRUE                           1
#define GL_FALSE                          0

/* ClipPlaneName */
#define GL_CLIP_PLANE0                    0x3000
#define GL_CLIP_PLANE1                    0x3001
#define GL_CLIP_PLANE2                    0x3002
#define GL_CLIP_PLANE3                    0x3003
#define GL_CLIP_PLANE4                    0x3004
#define GL_CLIP_PLANE5                    0x3005

/* DataType  */
#define GL_BYTE                           0x1400
#define GL_UNSIGNED_BYTE                  0x1401
#define GL_SHORT                          0x1402
#define GL_UNSIGNED_SHORT                 0x1403
#define GL_INT                            0x1404
#define GL_UNSIGNED_INT                   0x1405
#define GL_FLOAT                          0x1406
#define GL_2_BYTES                        0x1407
#define GL_3_BYTES                        0x1408
#define GL_4_BYTES                        0x1409

#if API_VERSION > 256
#define GL_DOUBLE                         0x140A
#endif

/* DrawBufferMode  */
#define GL_NONE                           0
#define GL_FRONT_LEFT                     0x0400
#define GL_FRONT_RIGHT                    0x0401
#define GL_BACK_LEFT                      0x0402
#define GL_BACK_RIGHT                     0x0403
#define GL_FRONT                          0x0404
#define GL_BACK                           0x0405
#define GL_LEFT                           0x0406
#define GL_RIGHT                          0x0407
#define GL_FRONT_AND_BACK                 0x0408
#define GL_AUX0                           0x0409
#define GL_AUX1                           0x040A
#define GL_AUX2                           0x040B
#define GL_AUX3                           0x040C

/* ErrorCode  */
#define GL_NO_ERROR                       0
#define GL_INVALID_ENUM                   0x0500
#define GL_INVALID_VALUE                  0x0501
#define GL_INVALID_OPERATION              0x0502
#define GL_STACK_OVERFLOW                 0x0503
#define GL_STACK_UNDERFLOW                0x0504
#define GL_OUT_OF_MEMORY                  0x0505

/* FeedBackMode  */
#define GL_2D                             0x0600
#define GL_3D                             0x0601
#define GL_3D_COLOR                       0x0602
#define GL_3D_COLOR_TEXTURE               0x0603
#define GL_4D_COLOR_TEXTURE               0x0604

/* FeedBackToken */
#define GL_PASS_THROUGH_TOKEN             0x0700
#define GL_POINT_TOKEN                    0x0701
#define GL_LINE_TOKEN                     0x0702
#define GL_POLYGON_TOKEN                  0x0703
#define GL_BITMAP_TOKEN                   0x0704
#define GL_DRAW_PIXEL_TOKEN               0x0705
#define GL_COPY_PIXEL_TOKEN               0x0706
#define GL_LINE_RESET_TOKEN               0x0707

/* FogMode  */
#define GL_EXP                            0x0800
#define GL_EXP2                           0x0801

/* FrontFaceDirection */
#define GL_CW                             0x0900
#define GL_CCW                            0x0901

/* GetMapTarget  */
#define GL_COEFF                          0x0A00
#define GL_ORDER                          0x0A01
#define GL_DOMAIN                         0x0A02

/* GetTarget  */
#define GL_CURRENT_COLOR                  0x0B00
#define GL_CURRENT_INDEX                  0x0B01
#define GL_CURRENT_NORMAL                 0x0B02
#define GL_CURRENT_TEXTURE_COORDS         0x0B03
#define GL_CURRENT_RASTER_COLOR           0x0B04
#define GL_CURRENT_RASTER_INDEX           0x0B05
#define GL_CURRENT_RASTER_TEXTURE_COORDS  0x0B06
#define GL_CURRENT_RASTER_POSITION        0x0B07
#define GL_CURRENT_RASTER_POSITION_VALID  0x0B08
#define GL_CURRENT_RASTER_DISTANCE        0x0B09
#define GL_POINT_SMOOTH                   0x0B10
#define GL_POINT_SIZE                     0x0B11
#define GL_POINT_SIZE_RANGE               0x0B12
#define GL_POINT_SIZE_GRANULARITY         0x0B13
#define GL_LINE_SMOOTH                    0x0B20
#define GL_LINE_WIDTH                     0x0B21
#define GL_LINE_WIDTH_RANGE               0x0B22
#define GL_LINE_WIDTH_GRANULARITY         0x0B23
#define GL_LINE_STIPPLE                   0x0B24
#define GL_LINE_STIPPLE_PATTERN           0x0B25
#define GL_LINE_STIPPLE_REPEAT            0x0B26
#define GL_LIST_MODE                      0x0B30
#define GL_MAX_LIST_NESTING               0x0B31
#define GL_LIST_BASE                      0x0B32
#define GL_LIST_INDEX                     0x0B33
#define GL_POLYGON_MODE                   0x0B40
#define GL_POLYGON_SMOOTH                 0x0B41
#define GL_POLYGON_STIPPLE                0x0B42
#define GL_EDGE_FLAG                      0x0B43
#define GL_CULL_FACE                      0x0B44
#define GL_CULL_FACE_MODE                 0x0B45
#define GL_FRONT_FACE                     0x0B46
#define GL_LIGHTING                       0x0B50
#define GL_LIGHT_MODEL_LOCAL_VIEWER       0x0B51
#define GL_LIGHT_MODEL_TWO_SIDE           0x0B52
#define GL_LIGHT_MODEL_AMBIENT            0x0B53
#define GL_SHADE_MODEL                    0x0B54
#define GL_COLOR_MATERIAL_FACE            0x0B55
#define GL_COLOR_MATERIAL_PARAMETER       0x0B56
#define GL_COLOR_MATERIAL                 0x0B57
#define GL_FOG                            0x0B60
#define GL_FOG_INDEX                      0x0B61
#define GL_FOG_DENSITY                    0x0B62
#define GL_FOG_START                      0x0B63
#define GL_FOG_END                        0x0B64
#define GL_FOG_MODE                       0x0B65
#define GL_FOG_COLOR                      0x0B66
#define GL_DEPTH_RANGE                    0x0B70
#define GL_DEPTH_TEST                     0x0B71
#define GL_DEPTH_WRITEMASK                0x0B72
#define GL_DEPTH_CLEAR_VALUE              0x0B73
#define GL_DEPTH_FUNC                     0x0B74
#define GL_ACCUM_CLEAR_VALUE              0x0B80
#define GL_STENCIL_TEST                   0x0B90
#define GL_STENCIL_CLEAR_VALUE            0x0B91
#define GL_STENCIL_FUNC                   0x0B92
#define GL_STENCIL_VALUE_MASK             0x0B93
#define GL_STENCIL_FAIL                   0x0B94
#define GL_STENCIL_PASS_DEPTH_FAIL        0x0B95
#define GL_STENCIL_PASS_DEPTH_PASS        0x0B96
#define GL_STENCIL_REF                    0x0B97
#define GL_STENCIL_WRITEMASK              0x0B98
#define GL_MATRIX_MODE                    0x0BA0
#define GL_NORMALIZE                      0x0BA1
#define GL_VIEWPORT                       0x0BA2
#define GL_MODELVIEW_STACK_DEPTH          0x0BA3
#define GL_PROJECTION_STACK_DEPTH         0x0BA4
#define GL_TEXTURE_STACK_DEPTH            0x0BA5
#define GL_MODELVIEW_MATRIX               0x0BA6
#define GL_PROJECTION_MATRIX              0x0BA7
#define GL_TEXTURE_MATRIX                 0x0BA8
#define GL_ATTRIB_STACK_DEPTH             0x0BB0
#define GL_CLIENT_ATTRIB_STACK_DEPTH      0x0BB1
#define GL_ALPHA_TEST                     0x0BC0
#define GL_ALPHA_TEST_FUNC                0x0BC1
#define GL_ALPHA_TEST_REF                 0x0BC2
#define GL_DITHER                         0x0BD0
#define GL_BLEND_DST                      0x0BE0
#define GL_BLEND_SRC                      0x0BE1
#define GL_BLEND                          0x0BE2
#define GL_LOGIC_OP_MODE                  0x0BF0
#define GL_INDEX_LOGIC_OP                 0x0BF1
#define GL_COLOR_LOGIC_OP                 0x0BF2
#define GL_AUX_BUFFERS                    0x0C00
#define GL_DRAW_BUFFER                    0x0C01
#define GL_READ_BUFFER                    0x0C02
#define GL_SCISSOR_BOX                    0x0C10
#define GL_SCISSOR_TEST                   0x0C11
#define GL_INDEX_CLEAR_VALUE              0x0C20
#define GL_INDEX_WRITEMASK                0x0C21
#define GL_COLOR_CLEAR_VALUE              0x0C22
#define GL_COLOR_WRITEMASK                0x0C23
#define GL_INDEX_MODE                     0x0C30
#define GL_RGBA_MODE                      0x0C31
#define GL_DOUBLEBUFFER                   0x0C32
#define GL_STEREO                         0x0C33
#define GL_RENDER_MODE                    0x0C40
#define GL_PERSPECTIVE_CORRECTION_HINT    0x0C50
#define GL_POINT_SMOOTH_HINT              0x0C51
#define GL_LINE_SMOOTH_HINT               0x0C52
#define GL_POLYGON_SMOOTH_HINT            0x0C53
#define GL_FOG_HINT                       0x0C54
#define GL_TEXTURE_GEN_S                  0x0C60
#define GL_TEXTURE_GEN_T                  0x0C61
#define GL_TEXTURE_GEN_R                  0x0C62
#define GL_TEXTURE_GEN_Q                  0x0C63
#define GL_PIXEL_MAP_I_TO_I               0x0C70
#define GL_PIXEL_MAP_S_TO_S               0x0C71
#define GL_PIXEL_MAP_I_TO_R               0x0C72
#define GL_PIXEL_MAP_I_TO_G               0x0C73
#define GL_PIXEL_MAP_I_TO_B               0x0C74
#define GL_PIXEL_MAP_I_TO_A               0x0C75
#define GL_PIXEL_MAP_R_TO_R               0x0C76
#define GL_PIXEL_MAP_G_TO_G               0x0C77
#define GL_PIXEL_MAP_B_TO_B               0x0C78
#define GL_PIXEL_MAP_A_TO_A               0x0C79
#define GL_PIXEL_MAP_I_TO_I_SIZE          0x0CB0
#define GL_PIXEL_MAP_S_TO_S_SIZE          0x0CB1
#define GL_PIXEL_MAP_I_TO_R_SIZE          0x0CB2
#define GL_PIXEL_MAP_I_TO_G_SIZE          0x0CB3
#define GL_PIXEL_MAP_I_TO_B_SIZE          0x0CB4
#define GL_PIXEL_MAP_I_TO_A_SIZE          0x0CB5
#define GL_PIXEL_MAP_R_TO_R_SIZE          0x0CB6
#define GL_PIXEL_MAP_G_TO_G_SIZE          0x0CB7
#define GL_PIXEL_MAP_B_TO_B_SIZE          0x0CB8
#define GL_PIXEL_MAP_A_TO_A_SIZE          0x0CB9
#define GL_UNPACK_SWAP_BYTES              0x0CF0
#define GL_UNPACK_LSB_FIRST               0x0CF1
#define GL_UNPACK_ROW_LENGTH              0x0CF2
#define GL_UNPACK_SKIP_ROWS               0x0CF3
#define GL_UNPACK_SKIP_PIXELS             0x0CF4
#define GL_UNPACK_ALIGNMENT               0x0CF5
#define GL_PACK_SWAP_BYTES                0x0D00
#define GL_PACK_LSB_FIRST                 0x0D01
#define GL_PACK_ROW_LENGTH                0x0D02
#define GL_PACK_SKIP_ROWS                 0x0D03
#define GL_PACK_SKIP_PIXELS               0x0D04
#define GL_PACK_ALIGNMENT                 0x0D05
#define GL_MAP_COLOR                      0x0D10
#define GL_MAP_STENCIL                    0x0D11
#define GL_INDEX_SHIFT                    0x0D12
#define GL_INDEX_OFFSET                   0x0D13
#define GL_RED_SCALE                      0x0D14
#define GL_RED_BIAS                       0x0D15
#define GL_ZOOM_X                         0x0D16
#define GL_ZOOM_Y                         0x0D17
#define GL_GREEN_SCALE                    0x0D18
#define GL_GREEN_BIAS                     0x0D19
#define GL_BLUE_SCALE                     0x0D1A
#define GL_BLUE_BIAS                      0x0D1B
#define GL_ALPHA_SCALE                    0x0D1C
#define GL_ALPHA_BIAS                     0x0D1D
#define GL_DEPTH_SCALE                    0x0D1E
#define GL_DEPTH_BIAS                     0x0D1F
#define GL_MAX_EVAL_ORDER                 0x0D30
#define GL_MAX_LIGHTS                     0x0D31
#define GL_MAX_CLIP_PLANES                0x0D32
#define GL_MAX_TEXTURE_SIZE               0x0D33
#define GL_MAX_PIXEL_MAP_TABLE            0x0D34
#define GL_MAX_ATTRIB_STACK_DEPTH         0x0D35
#define GL_MAX_MODELVIEW_STACK_DEPTH      0x0D36
#define GL_MAX_NAME_STACK_DEPTH           0x0D37
#define GL_MAX_PROJECTION_STACK_DEPTH     0x0D38
#define GL_MAX_TEXTURE_STACK_DEPTH        0x0D39
#define GL_MAX_VIEWPORT_DIMS              0x0D3A
#define GL_MAX_CLIENT_ATTRIB_STACK_DEPTH  0x0D3B
#define GL_SUBPIXEL_BITS                  0x0D50
#define GL_INDEX_BITS                     0x0D51
#define GL_RED_BITS                       0x0D52
#define GL_GREEN_BITS                     0x0D53
#define GL_BLUE_BITS                      0x0D54
#define GL_ALPHA_BITS                     0x0D55
#define GL_DEPTH_BITS                     0x0D56
#define GL_STENCIL_BITS                   0x0D57
#define GL_ACCUM_RED_BITS                 0x0D58
#define GL_ACCUM_GREEN_BITS               0x0D59
#define GL_ACCUM_BLUE_BITS                0x0D5A
#define GL_ACCUM_ALPHA_BITS               0x0D5B
#define GL_NAME_STACK_DEPTH               0x0D70
#define GL_AUTO_NORMAL                    0x0D80
#define GL_MAP1_COLOR_4                   0x0D90
#define GL_MAP1_INDEX                     0x0D91
#define GL_MAP1_NORMAL                    0x0D92
#define GL_MAP1_TEXTURE_COORD_1           0x0D93
#define GL_MAP1_TEXTURE_COORD_2           0x0D94
#define GL_MAP1_TEXTURE_COORD_3           0x0D95
#define GL_MAP1_TEXTURE_COORD_4           0x0D96
#define GL_MAP1_VERTEX_3                  0x0D97
#define GL_MAP1_VERTEX_4                  0x0D98
#define GL_MAP2_COLOR_4                   0x0DB0
#define GL_MAP2_INDEX                     0x0DB1
#define GL_MAP2_NORMAL                    0x0DB2
#define GL_MAP2_TEXTURE_COORD_1           0x0DB3
#define GL_MAP2_TEXTURE_COORD_2           0x0DB4
#define GL_MAP2_TEXTURE_COORD_3           0x0DB5
#define GL_MAP2_TEXTURE_COORD_4           0x0DB6
#define GL_MAP2_VERTEX_3                  0x0DB7
#define GL_MAP2_VERTEX_4                  0x0DB8
#define GL_MAP1_GRID_DOMAIN               0x0DD0
#define GL_MAP1_GRID_SEGMENTS             0x0DD1
#define GL_MAP2_GRID_DOMAIN               0x0DD2
#define GL_MAP2_GRID_SEGMENTS             0x0DD3
#define GL_TEXTURE_1D                     0x0DE0
#define GL_TEXTURE_2D                     0x0DE1
#define GL_FEEDBACK_BUFFER_POINTER        0x0DF0
#define GL_FEEDBACK_BUFFER_SIZE           0x0DF1
#define GL_FEEDBACK_BUFFER_TYPE           0x0DF2
#define GL_SELECTION_BUFFER_POINTER       0x0DF3
#define GL_SELECTION_BUFFER_SIZE          0x0DF4

#define GL_TEXTURE_WIDTH                  0x1000
#define GL_TEXTURE_HEIGHT                 0x1001
#define GL_TEXTURE_INTERNAL_FORMAT        0x1003
#define GL_TEXTURE_BORDER_COLOR           0x1004
#define GL_TEXTURE_BORDER                 0x1005

/* HintMode */
#define GL_DONT_CARE                      0x1100
#define GL_FASTEST                        0x1101
#define GL_NICEST                         0x1102

/* LightName */
#define GL_LIGHT0                         0x4000
#define GL_LIGHT1                         0x4001
#define GL_LIGHT2                         0x4002
#define GL_LIGHT3                         0x4003
#define GL_LIGHT4                         0x4004
#define GL_LIGHT5                         0x4005
#define GL_LIGHT6                         0x4006
#define GL_LIGHT7                         0x4007

/* LightParameter  */
#define GL_AMBIENT                        0x1200
#define GL_DIFFUSE                        0x1201
#define GL_SPECULAR                       0x1202
#define GL_POSITION                       0x1203
#define GL_SPOT_DIRECTION                 0x1204
#define GL_SPOT_EXPONENT                  0x1205
#define GL_SPOT_CUTOFF                    0x1206
#define GL_CONSTANT_ATTENUATION           0x1207
#define GL_LINEAR_ATTENUATION             0x1208
#define GL_QUADRATIC_ATTENUATION          0x1209

/* ListMode  */
#define GL_COMPILE                        0x1300
#define GL_COMPILE_AND_EXECUTE            0x1301

/* LogicOp  */
#define GL_CLEAR                          0x1500
#define GL_AND                            0x1501
#define GL_AND_REVERSE                    0x1502
#define GL_COPY                           0x1503
#define GL_AND_INVERTED                   0x1504
#define GL_NOOP                           0x1505
#define GL_XOR                            0x1506
#define GL_OR                             0x1507
#define GL_NOR                            0x1508
#define GL_EQUIV                          0x1509
#define GL_INVERT                         0x150A
#define GL_OR_REVERSE                     0x150B
#define GL_COPY_INVERTED                  0x150C
#define GL_OR_INVERTED                    0x150D
#define GL_NAND                           0x150E
#define GL_SET                            0x150F

/* MaterialParameter  */
#define GL_EMISSION                       0x1600
#define GL_SHININESS                      0x1601
#define GL_AMBIENT_AND_DIFFUSE            0x1602
#define GL_COLOR_INDEXES                  0x1603

/* MatrixMode  */
#define GL_MODELVIEW                      0x1700
#define GL_PROJECTION                     0x1701
#define GL_TEXTURE                        0x1702

/* PixelCopyType  */
#define GL_COLOR                          0x1800
#define GL_DEPTH                          0x1801
#define GL_STENCIL                        0x1802

/* PixelFormat  */
#define GL_COLOR_INDEX                    0x1900
#define GL_STENCIL_INDEX                  0x1901
#define GL_DEPTH_COMPONENT                0x1902
#define GL_RED                            0x1903
#define GL_GREEN                          0x1904
#define GL_BLUE                           0x1905
#define GL_ALPHA                          0x1906
#define GL_RGB                            0x1907
#define GL_RGBA                           0x1908
#define GL_LUMINANCE                      0x1909
#define GL_LUMINANCE_ALPHA                0x190A

/* PixelType  */
#define GL_BITMAP                         0x1A00

/* PolygonMode */
#define GL_POINT                          0x1B00
#define GL_LINE                           0x1B01
#define GL_FILL                           0x1B02

/* RenderingMode */
#define GL_RENDER                         0x1C00
#define GL_FEEDBACK                       0x1C01
#define GL_SELECT                         0x1C02

/* ShadingModel */
#define GL_FLAT                           0x1D00
#define GL_SMOOTH                         0x1D01

/* StencilOp */
#define GL_KEEP                           0x1E00
#define GL_REPLACE                        0x1E01
#define GL_INCR                           0x1E02
#define GL_DECR                           0x1E03

/* StringName */
#define GL_VENDOR                         0x1F00
#define GL_RENDERER                       0x1F01
#define GL_VERSION                        0x1F02
#define GL_EXTENSIONS                     0x1F03

/* TextureCoordName */
#define GL_S                              0x2000
#define GL_T                              0x2001
#define GL_R                              0x2002
#define GL_Q                              0x2003

/* TextureEnvMode */
#define GL_MODULATE                       0x2100
#define GL_DECAL                          0x2101

/* TextureEnvParameter */
#define GL_TEXTURE_ENV_MODE               0x2200
#define GL_TEXTURE_ENV_COLOR              0x2201

/* TextureEnvTarget */
#define GL_TEXTURE_ENV                    0x2300

/* TextureGenMode */
#define GL_EYE_LINEAR                     0x2400
#define GL_OBJECT_LINEAR                  0x2401
#define GL_SPHERE_MAP                     0x2402

/* TextureGenParameter */
#define GL_TEXTURE_GEN_MODE               0x2500
#define GL_OBJECT_PLANE                   0x2501
#define GL_EYE_PLANE                      0x2502

/* TextureMagFilter  */
#define GL_NEAREST                        0x2600
#define GL_LINEAR                         0x2601

/* TextureMinFilter */
#define GL_NEAREST_MIPMAP_NEAREST         0x2700
#define GL_LINEAR_MIPMAP_NEAREST          0x2701
#define GL_NEAREST_MIPMAP_LINEAR          0x2702
#define GL_LINEAR_MIPMAP_LINEAR           0x2703

/* TextureParameterName */
#define GL_TEXTURE_MAG_FILTER             0x2800
#define GL_TEXTURE_MIN_FILTER             0x2801
#define GL_TEXTURE_WRAP_S                 0x2802
#define GL_TEXTURE_WRAP_T                 0x2803

/* TextureWrapMode  */
#define GL_CLAMP                          0x2900
#define GL_REPEAT                         0x2901

/* ClientAttribMask */
#define GL_CLIENT_PIXEL_STORE_BIT         0x00000001
#define GL_CLIENT_VERTEX_ARRAY_BIT        0x00000002
#define GL_CLIENT_ALL_ATTRIB_BITS         0xffffffff

#if API_VERSION > 256
/* polygon_offset */
#define GL_POLYGON_OFFSET_FACTOR          0x8038
#define GL_POLYGON_OFFSET_UNITS           0x2A00
#define GL_POLYGON_OFFSET_POINT           0x2A01
#define GL_POLYGON_OFFSET_LINE            0x2A02
#define GL_POLYGON_OFFSET_FILL            0x8037

/* texture  */
#define GL_ALPHA4                         0x803B
#define GL_ALPHA8                         0x803C
#define GL_ALPHA12                        0x803D
#define GL_ALPHA16                        0x803E
#define GL_LUMINANCE4                     0x803F
#define GL_LUMINANCE8                     0x8040
#define GL_LUMINANCE12                    0x8041
#define GL_LUMINANCE16                    0x8042
#define GL_LUMINANCE4_ALPHA4              0x8043
#define GL_LUMINANCE6_ALPHA2              0x8044
#define GL_LUMINANCE8_ALPHA8              0x8045
#define GL_LUMINANCE12_ALPHA4             0x8046
#define GL_LUMINANCE12_ALPHA12            0x8047
#define GL_LUMINANCE16_ALPHA16            0x8048
#define GL_INTENSITY                      0x8049
#define GL_INTENSITY4                     0x804A
#define GL_INTENSITY8                     0x804B
#define GL_INTENSITY12                    0x804C
#define GL_INTENSITY16                    0x804D
#define GL_R3_G3_B2                       0x2A10
#define GL_RGB4                           0x804F
#define GL_RGB5                           0x8050
#define GL_RGB8                           0x8051
#define GL_RGB10                          0x8052
#define GL_RGB12                          0x8053
#define GL_RGB16                          0x8054
#define GL_RGBA2                          0x8055
#define GL_RGBA4                          0x8056
#define GL_RGB5_A1                        0x8057
#define GL_RGBA8                          0x8058
#define GL_RGB10_A2                       0x8059
#define GL_RGBA12                         0x805A
#define GL_RGBA16                         0x805B
#define GL_TEXTURE_RED_SIZE               0x805C
#define GL_TEXTURE_GREEN_SIZE             0x805D
#define GL_TEXTURE_BLUE_SIZE              0x805E
#define GL_TEXTURE_ALPHA_SIZE             0x805F
#define GL_TEXTURE_LUMINANCE_SIZE         0x8060
#define GL_TEXTURE_INTENSITY_SIZE         0x8061
#define GL_PROXY_TEXTURE_1D               0x8063
#define GL_PROXY_TEXTURE_2D               0x8064

/* texture_object  */
#define GL_TEXTURE_PRIORITY               0x8066
#define GL_TEXTURE_RESIDENT               0x8067
#define GL_TEXTURE_BINDING_1D             0x8068
#define GL_TEXTURE_BINDING_2D             0x8069

/* vertex_array  */
#define GL_VERTEX_ARRAY                   0x8074
#define GL_NORMAL_ARRAY                   0x8075
#define GL_COLOR_ARRAY                    0x8076
#define GL_INDEX_ARRAY                    0x8077
#define GL_TEXTURE_COORD_ARRAY            0x8078
#define GL_EDGE_FLAG_ARRAY                0x8079
#define GL_VERTEX_ARRAY_SIZE              0x807A
#define GL_VERTEX_ARRAY_TYPE              0x807B
#define GL_VERTEX_ARRAY_STRIDE            0x807C
#define GL_NORMAL_ARRAY_TYPE              0x807E
#define GL_NORMAL_ARRAY_STRIDE            0x807F
#define GL_COLOR_ARRAY_SIZE               0x8081
#define GL_COLOR_ARRAY_TYPE               0x8082
#define GL_COLOR_ARRAY_STRIDE             0x8083
#define GL_INDEX_ARRAY_TYPE               0x8085
#define GL_INDEX_ARRAY_STRIDE             0x8086
#define GL_TEXTURE_COORD_ARRAY_SIZE       0x8088
#define GL_TEXTURE_COORD_ARRAY_TYPE       0x8089
#define GL_TEXTURE_COORD_ARRAY_STRIDE     0x808A
#define GL_EDGE_FLAG_ARRAY_STRIDE         0x808C
#define GL_VERTEX_ARRAY_POINTER           0x808E
#define GL_NORMAL_ARRAY_POINTER           0x808F
#define GL_COLOR_ARRAY_POINTER            0x8090
#define GL_INDEX_ARRAY_POINTER            0x8091
#define GL_TEXTURE_COORD_ARRAY_POINTER    0x8092
#define GL_EDGE_FLAG_ARRAY_POINTER        0x8093
#define GL_V2F                            0x2A20
#define GL_V3F                            0x2A21
#define GL_C4UB_V2F                       0x2A22
#define GL_C4UB_V3F                       0x2A23
#define GL_C3F_V3F                        0x2A24
#define GL_N3F_V3F                        0x2A25
#define GL_C4F_N3F_V3F                    0x2A26
#define GL_T2F_V3F                        0x2A27
#define GL_T4F_V4F                        0x2A28
#define GL_T2F_C4UB_V3F                   0x2A29
#define GL_T2F_C3F_V3F                    0x2A2A
#define GL_T2F_N3F_V3F                    0x2A2B
#define GL_T2F_C4F_N3F_V3F                0x2A2C
#define GL_T4F_C4F_N3F_V4F                0x2A2D
#endif

/* For compatibility with OpenGL v1.0 */
#define GL_LOGIC_OP GL_INDEX_LOGIC_OP
#define GL_TEXTURE_COMPONENTS GL_TEXTURE_INTERNAL_FORMAT


#if API_VERSION_WORD >= 258

/*%{
void glDrawRangeElements(GLenum mode, GLuint start, GLuint end, GLsizei count, GLenum type, const void *buffer)
DOC(glDrawRangeElements, "glDrawRangeElements(mode, start, end, count, type, indices) -> None")

%name(glDrawRangeElementsub) void glDrawRangeElements(GLenum mode, GLuint start, GLuint end, GLsizei n_5, GLenum type_UNSIGNED_BYTE, const GLubyte *indices)
DOC(glDrawRangeElementsub, "glDrawRangeElementsub(mode, start, end, indices[]) -> None")

%name(glDrawRangeElementsus) void glDrawRangeElements(GLenum mode, GLuint start, GLuint end, GLsizei n_5, GLenum type_UNSIGNED_SHORT, const GLushort *indices)
DOC(glDrawRangeElementsus, "glDrawRangeElementsus(mode, start, end, indices[]) -> None")

%name(glDrawRangeElementsui) void glDrawRangeElements(GLenum mode, GLuint start, GLuint end, GLsizei n_5, GLenum type_UNSIGNED_INT, const GLuint *indices)
DOC(glDrawRangeElementsui, "glDrawRangeElementsui(mode, start, end, indices[]) -> None")


void glCopyTexSubImage3D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLint x, GLint y, GLsizei width, GLsizei height);
DOC(glCopyTexSubImage3D, "glCopyTexSubImage3D(target, level, xoffset, yoffset, zoffset, x, y, width, height) -> None")


void glTexSubImage3D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLenum type, const void *buffer);
DOC(glTexSubImage3D, "glTexSubImage3D(target, level, xoffset, yoffset, zoffset, width, height, depth, format, type, pixels) -> None")

%{
void _glTexSubImage3D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLenum type, const GLvoid* pixels)
{
	SetupPixelWrite(3);
	glTexSubImage3D(target, level, xoffset, yoffset, zoffset, width, height, depth, format, type, pixels);
}
%}

%name(glTexSubImage3Dub) void _glTexSubImage3D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei d_10_2, GLsizei d_10_1, GLsizei d_10_0, GLenum format, GLenum type_UNSIGNED_BYTE, const GLubyte *pixels);
DOC(glTexSubImage3Dub, "glTexSubImage3Dub(target, level, xoffset, yoffset, zoffset, format, type, pixels) -> None")

%name(glTexSubImage3Db) void _glTexSubImage3D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei d_10_2, GLsizei d_10_1, GLsizei d_10_0, GLenum format, GLenum type_BYTE, const GLbyte *pixels);
DOC(glTexSubImage3Db, "glTexSubImage3Db(target, level, xoffset, yoffset, zoffset, format, type, pixels) -> None")

%name(glTexSubImage3Dus) void _glTexSubImage3D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei d_10_2, GLsizei d_10_1, GLsizei d_10_0, GLenum format, GLenum type_UNSIGNED_SHORT, const GLushort *pixels);
DOC(glTexSubImage3Dus, "glTexSubImage3Dus(target, level, xoffset, yoffset, zoffset, format, type, pixels) -> None")

%name(glTexSubImage3Ds) void _glTexSubImage3D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei d_10_2, GLsizei d_10_1, GLsizei d_10_0, GLenum format, GLenum type_SHORT, const GLshort *pixels);
DOC(glTexSubImage3Ds, "glTexSubImage3Ds(target, level, xoffset, yoffset, zoffset, format, type, pixels) -> None")

%name(glTexSubImage3Dui) void _glTexSubImage3D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei d_10_2, GLsizei d_10_1, GLsizei d_10_0, GLenum format, GLenum type_UNSIGNED_INT, const GLuint *pixels);
DOC(glTexSubImage3Dui, "glTexSubImage3Dui(target, level, xoffset, yoffset, zoffset, format, type, pixels) -> None")

%name(glTexSubImage3Di) void _glTexSubImage3D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei d_10_2, GLsizei d_10_1, GLsizei d_10_0, GLenum format, GLenum type_INT, const GLint *pixels);
DOC(glTexSubImage3Di, "glTexSubImage3Di(target, level, xoffset, yoffset, zoffset, format, type, pixels) -> None")

%name(glTexSubImage3Df) void _glTexSubImage3D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei d_10_2, GLsizei d_10_1, GLsizei d_10_0, GLenum format, GLenum type_FLOAT, const GLfloat *pixels);
DOC(glTexSubImage3Df, "glTexSubImage3Df(target, level, xoffset, yoffset, zoffset, format, type, pixels) -> None")


void glTexImage3D(GLenum target, GLint level, GLint internalFormat, GLsizei width, GLsizei height, GLsizei depth, GLint border, GLenum format, GLenum type, const void *buffer);
DOC(glTexImage3D, "glTexImage3D(target, level, internalFormat, width, height, depth, border, format, type, pixels) -> None")

%{
void __glTexImage3D(GLenum target, GLint level, GLint internalFormat, GLsizei width, GLsizei height, GLsizei depth, GLint border, GLenum format, GLenum type, const GLvoid* pixels)
{
	SetupPixelWrite(3);
	glTexImage3D(target, level, internalFormat, width, height, depth, border, format, type, pixels);
}
%}

%name(glTexImage3Dub) void __glTexImage3D(GLenum target, GLint level, GLint internalFormat, GLsizei d_9_2, GLsizei d_9_1, GLsizei d_9_0, GLint border, GLenum format, GLenum type_UNSIGNED_BYTE, const GLubyte *pixels);
DOC(glTexImage3Dub, "glTexImage3Dub(target, level, internalFormat, border, format, type, pixels) -> None")

%name(glTexImage3Db) void __glTexImage3D(GLenum target, GLint level, GLint internalFormat, GLsizei d_9_2, GLsizei d_9_1, GLsizei d_9_0, GLint border, GLenum format, GLenum type_BYTE, const GLbyte *pixels);
DOC(glTexImage3Db, "glTexImage3Db(target, level, internalFormat, border, format, type, pixels) -> None")

%name(glTexImage3Dus) void __glTexImage3D(GLenum target, GLint level, GLint internalFormat, GLsizei d_9_2, GLsizei d_9_1, GLsizei d_9_0, GLint border, GLenum format, GLenum type_UNSIGNED_SHORT, const GLushort *pixels);
DOC(glTexImage3Dus, "glTexImage3Dus(target, level, internalFormat, border, format, type, pixels) -> None")

%name(glTexImage3Ds) void __glTexImage3D(GLenum target, GLint level, GLint internalFormat, GLsizei d_9_2, GLsizei d_9_1, GLsizei d_9_0, GLint border, GLenum format, GLenum type_SHORT, const GLshort *pixels);
DOC(glTexImage3Ds, "glTexImage3Ds(target, level, internalFormat, border, format, type, pixels) -> None")

%name(glTexImage3Dui) void __glTexImage3D(GLenum target, GLint level, GLint internalFormat, GLsizei d_9_2, GLsizei d_9_1, GLsizei d_9_0, GLint border, GLenum format, GLenum type_UNSIGNED_INT, const GLuint *pixels);
DOC(glTexImage3Dui, "glTexImage3Dui(target, level, internalFormat, border, format, type, pixels) -> None")

%name(glTexImage3Di) void __glTexImage3D(GLenum target, GLint level, GLint internalFormat, GLsizei d_9_2, GLsizei d_9_1, GLsizei d_9_0, GLint border, GLenum format, GLenum type_INT, const GLint *pixels);
DOC(glTexImage3Di, "glTexImage3Di(target, level, internalFormat, border, format, type, pixels) -> None")

%name(glTexImage3Df) void __glTexImage3D(GLenum target, GLint level, GLint internalFormat, GLsizei d_9_2, GLsizei d_9_1, GLsizei d_9_0, GLint border, GLenum format, GLenum type_FLOAT, const GLfloat *pixels);
DOC(glTexImage3Df, "glTexImage3Df(target, level, internalFormat, border, format, type, pixels) -> None")*/


/* OpenGL 1.2 */

#define GL_VERSION_1_2   1

#define GL_RESCALE_NORMAL			0x803A
#define GL_CLAMP_TO_EDGE			0x812F
#define GL_MAX_ELEMENTS_VERTICES		0x80E8
#define GL_MAX_ELEMENTS_INDICES			0x80E9
#define GL_BGR					0x80E0
#define GL_BGRA					0x80E1
#define GL_UNSIGNED_BYTE_3_3_2			0x8032
#define GL_UNSIGNED_BYTE_2_3_3_REV		0x8362
#define GL_UNSIGNED_SHORT_5_6_5			0x8363
#define GL_UNSIGNED_SHORT_5_6_5_REV		0x8364
#define GL_UNSIGNED_SHORT_4_4_4_4		0x8033
#define GL_UNSIGNED_SHORT_4_4_4_4_REV		0x8365
#define GL_UNSIGNED_SHORT_5_5_5_1		0x8034
#define GL_UNSIGNED_SHORT_1_5_5_5_REV		0x8366
#define GL_UNSIGNED_INT_8_8_8_8			0x8035
#define GL_UNSIGNED_INT_8_8_8_8_REV		0x8367
#define GL_UNSIGNED_INT_10_10_10_2		0x8036
#define GL_UNSIGNED_INT_2_10_10_10_REV		0x8368
#define GL_LIGHT_MODEL_COLOR_CONTROL		0x81F8
#define GL_SINGLE_COLOR				0x81F9
#define GL_SEPARATE_SPECULAR_COLOR		0x81FA
#define GL_TEXTURE_MIN_LOD			0x813A
#define GL_TEXTURE_MAX_LOD			0x813B
#define GL_TEXTURE_BASE_LEVEL			0x813C
#define GL_TEXTURE_MAX_LEVEL			0x813D
#define GL_SMOOTH_POINT_SIZE_RANGE		0x0B12
#define GL_SMOOTH_POINT_SIZE_GRANULARITY	0x0B13
#define GL_SMOOTH_LINE_WIDTH_RANGE		0x0B22
#define GL_SMOOTH_LINE_WIDTH_GRANULARITY	0x0B23
#define GL_ALIASED_POINT_SIZE_RANGE		0x846D
#define GL_ALIASED_LINE_WIDTH_RANGE		0x846E

/* GL_EXT_color_table  */
#define GL_COLOR_TABLE				0x80D0
#define GL_POST_CONVOLUTION_COLOR_TABLE		0x80D1
#define GL_POST_COLOR_MATRIX_COLOR_TABLE	0x80D2
#define GL_PROXY_COLOR_TABLE			0x80D3
#define GL_PROXY_POST_CONVOLUTION_COLOR_TABLE	0x80D4
#define GL_PROXY_POST_COLOR_MATRIX_COLOR_TABLE	0x80D5
#define GL_COLOR_TABLE_SCALE			0x80D6
#define GL_COLOR_TABLE_BIAS			0x80D7
#define GL_COLOR_TABLE_FORMAT			0x80D8
#define GL_COLOR_TABLE_WIDTH			0x80D9
#define GL_COLOR_TABLE_RED_SIZE			0x80DA
#define GL_COLOR_TABLE_GREEN_SIZE		0x80DB
#define GL_COLOR_TABLE_BLUE_SIZE		0x80DC
#define GL_COLOR_TABLE_ALPHA_SIZE		0x80DD
#define GL_COLOR_TABLE_LUMINANCE_SIZE		0x80DE
#define GL_COLOR_TABLE_INTENSITY_SIZE		0x80DF

/* GL_EXT_convolution and GL_HP_convolution_border_modes */
#define GL_CONVOLUTION_1D			0x8010
#define GL_CONVOLUTION_2D			0x8011
#define GL_SEPARABLE_2D				0x8012
#define GL_CONVOLUTION_BORDER_MODE		0x8013
#define GL_CONVOLUTION_FILTER_SCALE		0x8014
#define GL_CONVOLUTION_FILTER_BIAS		0x8015
#define GL_REDUCE				0x8016
#define GL_CONVOLUTION_FORMAT			0x8017
#define GL_CONVOLUTION_WIDTH			0x8018
#define GL_CONVOLUTION_HEIGHT			0x8019
#define GL_MAX_CONVOLUTION_WIDTH		0x801A
#define GL_MAX_CONVOLUTION_HEIGHT		0x801B
#define GL_POST_CONVOLUTION_RED_SCALE		0x801C
#define GL_POST_CONVOLUTION_GREEN_SCALE		0x801D
#define GL_POST_CONVOLUTION_BLUE_SCALE		0x801E
#define GL_POST_CONVOLUTION_ALPHA_SCALE		0x801F
#define GL_POST_CONVOLUTION_RED_BIAS		0x8020
#define GL_POST_CONVOLUTION_GREEN_BIAS		0x8021
#define GL_POST_CONVOLUTION_BLUE_BIAS		0x8022
#define GL_POST_CONVOLUTION_ALPHA_BIAS		0x8023
#define GL_CONSTANT_BORDER			0x8151
#define GL_REPLICATE_BORDER			0x8153
#define GL_CONVOLUTION_BORDER_COLOR		0x8154

/* GL_SGI_color_matrix  */
#define GL_COLOR_MATRIX				0x80B1
#define GL_COLOR_MATRIX_STACK_DEPTH		0x80B2
#define GL_MAX_COLOR_MATRIX_STACK_DEPTH		0x80B3
#define GL_POST_COLOR_MATRIX_RED_SCALE		0x80B4
#define GL_POST_COLOR_MATRIX_GREEN_SCALE	0x80B5
#define GL_POST_COLOR_MATRIX_BLUE_SCALE		0x80B6
#define GL_POST_COLOR_MATRIX_ALPHA_SCALE	0x80B7
#define GL_POST_COLOR_MATRIX_RED_BIAS		0x80B8
#define GL_POST_COLOR_MATRIX_GREEN_BIAS		0x80B9
#define GL_POST_COLOR_MATRIX_BLUE_BIAS		0x80BA
#define GL_POST_COLOR_MATRIX_ALPHA_BIAS		0x80BB

/* GL_EXT_histogram  */
#define GL_HISTOGRAM				0x8024
#define GL_PROXY_HISTOGRAM			0x8025
#define GL_HISTOGRAM_WIDTH			0x8026
#define GL_HISTOGRAM_FORMAT			0x8027
#define GL_HISTOGRAM_RED_SIZE			0x8028
#define GL_HISTOGRAM_GREEN_SIZE			0x8029
#define GL_HISTOGRAM_BLUE_SIZE			0x802A
#define GL_HISTOGRAM_ALPHA_SIZE			0x802B
#define GL_HISTOGRAM_LUMINANCE_SIZE		0x802C
#define GL_HISTOGRAM_SINK			0x802D
#define GL_MINMAX				0x802E
#define GL_MINMAX_FORMAT			0x802F
#define GL_MINMAX_SINK				0x8030
#define GL_TABLE_TOO_LARGE			0x8031

/* GL_EXT_blend_color, GL_EXT_blend_minmax */
#define GL_BLEND_EQUATION			0x8009
#define GL_MIN					0x8007
#define GL_MAX					0x8008
#define GL_FUNC_ADD				0x8006
#define GL_FUNC_SUBTRACT			0x800A
#define GL_FUNC_REVERSE_SUBTRACT		0x800B
#define	GL_BLEND_COLOR				0x8005

#endif

%shadow %{
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
%}


%shadow %{
GLerror = _GL__init__.GLerror
%}
	
%shadow %{
__numeric_present__ = _GL__init__.__numeric_present__
__numeric_support__ = _GL__init__.__numeric_support__
%}

%shadow %{
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

%}


