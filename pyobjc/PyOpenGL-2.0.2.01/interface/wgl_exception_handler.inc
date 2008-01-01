/* Exception handler for areas with WGL exception handling 

	This used to be done by a macro expansion, but it turns
	out that SWIG 1.3.20+ doesn't expand macros before getting
	to the %exception definition, or at least does it badly,
	so we wind up with SyntaxErrors in the source code.

	Old name of the macro was:  WGL_EXCEPTION_HANDLER

	Requires WGL/util.inc's WGLErrOccurred to be available
*/
%exception
{
	SetLastError(0);
	$action
	if (WGLErrOccurred()) { return NULL; }
}

