/**********  Simple input values **********/
%{
GLint PyOpenGL_round(double x) {
  if (x >= 0) {
    return (GLint) (x+0.5);
	} else {
    return (GLint) (x-0.5);
	}
}

%}

%typemap(python, in) GLint x, GLint y {
	if (PyInt_Check($input) || PyLong_Check($input)) {
		$1= ($1_type)(PyInt_AsLong( $input ));
	} else if (PyFloat_Check($input)) {
		double $1_temp_float;
		$1_temp_float = PyFloat_AsDouble($input);
		if (($1_temp_float <= INT_MIN-0.5) || ($1_temp_float >= INT_MAX+0.5)) {
			PyErr_SetString(PyExc_ValueError, "GLint value too large to convert");
			return NULL;
		}
		$1 = PyOpenGL_round( $1_temp_float );
	}
}

/* yes, this is ugly, basically we don't want to override the sizes which are derived from arrays */
%typemap(python, in) GLsizei width, GLsizei height, GLsizei count, GLsizei start, GLsizei depth, GLsizei stride {
	if (PyInt_Check($input) || PyLong_Check($input)) {
		$1= ($1_type)(PyInt_AsLong( $input ));
	} else if (PyFloat_Check($input)) {
		double $1_temp_float;
		$1_temp_float = PyFloat_AsDouble($input);
		if ($1_temp_float >= (INT_MAX-0.5)) {
			PyErr_SetString(PyExc_ValueError, "Value too large to be converted to a size measurement");
			return NULL;
		} else if ($1_temp_float <= -0.5) {
			PyErr_SetString(PyExc_ValueError, "Value less than 0, cannot be converted to a size measurement");
			return NULL;
		}
		$1 = (GLsizei) PyOpenGL_round( $1_temp_float );
	}
}

%typemap(python, in) GLbyte, GLubyte, GLshort
{
	if (PyInt_Check($input) || PyLong_Check($input))
	{
		$1= ($1_type)(PyInt_AsLong( $input ));
	}
	else if (PyString_Check ($input))
	{
		/* what is a GLshort's size? */
		$1= ($1_type) PyString_AsString($input)[0];
	}
}

%typemap(python, in) GLboolean
{
	$1= (PyObject_IsTrue($input)) ? GL_TRUE : GL_FALSE;
}


%typemap(python, out) const GLubyte*
{
	if ($1) 
	{
	    $result= PyString_FromString($1); 
	}
	else 
	{
	    Py_INCREF($result = Py_None);
	}
}


%typemap(python, in) const void *buffer
{
	int len;
	PyObject* str;
	if ($input == Py_None) 
	{
		$1= NULL; 
	}
	else
	{
		str = PyObject_Str($input);
		PyString_AsStringAndSize(str, (char**)&$1, &len);
		Py_DECREF(str);
	}
}


%typemap(python, out) const wchar_t*
{
	if ($1) 
	{
	    $result = PyUnicode_FromWideChar($1, wcslen($1)); 
	}
	else 
	{
	    Py_INCREF($result= Py_None);
	}
}


%typemap(python,in) PyObject*, void*
{
	$1 = $input;
}

%typemap(python,out) PyObject*, void*
{
	$result= $1;
}

%typemap(python,in) PyObject* pyfunc
{
	if ($input != Py_None && !PyCallable_Check($input))
	{
		PyErr_SetString(PyExc_Exception, "Not callable.");
		return NULL;
	}
	$1 = $input;
}












%typemap(in, numinputs=0) GLenum type_UNSIGNED_BYTE
{
	$1 = GL_UNSIGNED_BYTE;
}

%typemap(in, numinputs=0) GLenum type_BYTE
{
	$1 = GL_BYTE;
}

%typemap(in, numinputs=0) GLenum type_UNSIGNED_SHORT
{
	$1 = GL_UNSIGNED_SHORT;
}

%typemap(in, numinputs=0) GLenum type_SHORT
{
	$1 = GL_SHORT;
}

%typemap(in, numinputs=0) GLenum type_UNSIGNED_INT
{
	$1 = GL_UNSIGNED_INT;
}

%typemap(in, numinputs=0) GLenum type_INT
{
	$1 = GL_INT;
}

%typemap(in, numinputs=0) GLenum type_FLOAT
{
	$1 = GL_FLOAT;
}

%typemap(in, numinputs=0) GLenum type_DOUBLE
{
	$1 = GL_DOUBLE;
}

%typemap(in, numinputs=0) GLsizei stride_0, GLint stride_0, GLint ustride_0, GLint vstride_0
{
	$1 = 0;
}

