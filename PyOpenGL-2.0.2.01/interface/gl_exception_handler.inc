/* Exception handler for areas with GL exception handling 

	This used to be done by a macro expansion, but it turns
	out that SWIG 1.3.20+ doesn't expand macros before getting
	to the %exception definition, or at least does it badly,
	so we wind up with SyntaxErrors in the source code.

	Old name of the macro was:  GL_EXCEPTION_HANDLER

	Requires util.inc's GLErrOccurred to be available
*/
%exception
{
	$action
	if (GLErrOccurred()) { return NULL; }
}
