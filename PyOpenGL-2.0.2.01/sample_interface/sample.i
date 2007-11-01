/*
# BUILD api_versions [0x100]
*/

%module sample

#define __version__ "$Revision: 1.1 $"
#define __date__ "$Date: 2001/10/18 15:41:01 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "Sample interface file for the PyOpenGL framework"

%include util.inc

GL_EXCEPTION_HANDLER()

%{
void foo(GLsizei count, const GLuint *data)
{
}
%}

void foo(GLsizei n_1, const GLuint *data);
DOC(foo, "foo(data) -> None")


