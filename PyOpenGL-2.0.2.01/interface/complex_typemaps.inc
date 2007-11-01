
/**********  Vector input values **********/

%{

int __PyObject_AsArray_Size(PyObject* x);

#ifdef NUMERIC

#define _PyObject_AsArray_Size(x) ((x == Py_None) ? 0 : ((PyArray_Check(x)) ? PyArray_Size(x) : __PyObject_AsArray_Size(x)))

#else /* NUMERIC */

#define _PyObject_AsArray_Size(x) ((x == Py_None) ? 0 : __PyObject_AsArray_Size(x))

#endif /* NUMERIC */


#define _PyObject_As(NAME, BASE) BASE* _PyObject_As##NAME(PyObject* source, PyObject** temp, int* len);

#define _PyObject_AsArray_Cleanup(target, temp) if (temp) Py_XDECREF(temp); else PyMem_Del(target)

_PyObject_As(FloatArray, float)

_PyObject_As(DoubleArray, double)

_PyObject_As(CharArray, signed char)

_PyObject_As(UnsignedCharArray, unsigned char)

_PyObject_As(ShortArray, short)

_PyObject_As(UnsignedShortArray, unsigned short)

_PyObject_As(IntArray, int)

_PyObject_As(UnsignedIntArray, unsigned int)

void* _PyObject_AsArray(GLenum type, PyObject* source, PyObject** temp, int* len);

%}



/* This is an ugly attempt to avoid passing array length to OpenGL. */
/* It relies on SWIG's naming and numbering scheme for arguments, */
/* and hence is fragile. */

#define ARRAY_LEN(NUMBER)\
%typemap(in, numinputs=0) int n_##NUMBER, unsigned int n_##NUMBER, GLint n_##NUMBER\
{\
}\
%typemap(python,check) int n_##NUMBER, unsigned int n_##NUMBER, GLint n_##NUMBER\
{\
	$1 = ($basetype)_PyObject_AsArray_Size(obj##NUMBER);\
}

#define ARRAY2_LEN(NUMBER, NUMBER2)\
%typemap(in, numinputs=0) int n_##NUMBER, unsigned int n_##NUMBER, GLint n_##NUMBER\
{\
}\
%typemap(python,check) int n_##NUMBER, unsigned int n_##NUMBER, GLint n_##NUMBER\
{\
	$1 = ($basetype)_PyObject_AsArray_Size(obj##NUMBER2);\
}

ARRAY2_LEN(1,0)
ARRAY2_LEN(2,1)
ARRAY2_LEN(3,2)
ARRAY2_LEN(4,3)
ARRAY2_LEN(5,4)
ARRAY2_LEN(6,5)
ARRAY2_LEN(7,6)
ARRAY2_LEN(8,7)
ARRAY2_LEN(9,8)
ARRAY2_LEN(10,9)
ARRAY2_LEN(11,10)
ARRAY2_LEN(12,11)
ARRAY_LEN(13)
ARRAY_LEN(14)
ARRAY_LEN(15)
ARRAY_LEN(16)
ARRAY_LEN(17)
ARRAY_LEN(18)
ARRAY_LEN(19)

/* This is an ugly attempt to avoid passing array dim to OpenGL. */
/* It relies on SWIG's naming and numbering scheme for arguments, */
/* and hence is fragile. */

#define ARRAY_DIM(NUMBER, DIM)\
%typemap(in, numinputs=0) int d_##NUMBER##_##DIM, unsigned int d_##NUMBER##_##DIM\
{\
}\
%typemap(python,check) int d_##NUMBER##_##DIM, unsigned int d_##NUMBER##_##DIM\
{\
	$1 = ($basetype)_PyObject_Dimension(obj##NUMBER, DIM);\
}

#define ARRAY2_DIM(NUMBER, DIM, NUMBER2)\
%typemap(in, numinputs=0) int d_##NUMBER##_##DIM, unsigned int d_##NUMBER##_##DIM\
{\
}\
%typemap(python,check) int d_##NUMBER##_##DIM, unsigned int d_##NUMBER##_##DIM\
{\
	$1 = ($basetype)_PyObject_Dimension(obj##NUMBER2, DIM);\
}

ARRAY_DIM(0, 0)
ARRAY_DIM(0, 1)
ARRAY_DIM(0, 2)
ARRAY_DIM(0, 3)

ARRAY_DIM(1, 0)
ARRAY_DIM(1, 1)
ARRAY_DIM(1, 2)
ARRAY_DIM(1, 3)

ARRAY2_DIM(2, 0, 0)
ARRAY2_DIM(2, 1, 0)
ARRAY2_DIM(2, 2, 0)
ARRAY2_DIM(2, 3, 0)

ARRAY2_DIM(3, 0, 0)
ARRAY2_DIM(3, 1, 0)
ARRAY2_DIM(3, 2, 0)
ARRAY2_DIM(3, 3, 0)

ARRAY2_DIM(4, 0, 1)
ARRAY2_DIM(4, 1, 1)
ARRAY2_DIM(4, 2, 1)
ARRAY2_DIM(4, 3, 1)

ARRAY2_DIM(5, 0,2)
ARRAY2_DIM(5, 1,2)
ARRAY2_DIM(5, 2,2)
ARRAY2_DIM(5, 3,2)


ARRAY2_DIM(6, 0, 3)
ARRAY2_DIM(6, 1, 3)
ARRAY2_DIM(6, 2, 3)
ARRAY2_DIM(6, 3, 3)

ARRAY2_DIM(7, 0, 4)
ARRAY2_DIM(7, 1, 4)
ARRAY2_DIM(7, 2, 4)
ARRAY2_DIM(7, 3, 4)

ARRAY2_DIM(8, 0, 5)
ARRAY2_DIM(8, 1, 5)
ARRAY2_DIM(8, 2, 5)
ARRAY2_DIM(8, 3, 5)

ARRAY2_DIM(9, 0, 6)
ARRAY2_DIM(9, 1, 6)
ARRAY2_DIM(9, 2, 6)
ARRAY2_DIM(9, 3, 6)

ARRAY2_DIM(10, 0, 7)
ARRAY2_DIM(10, 1, 7)
ARRAY2_DIM(10, 2, 7)
ARRAY2_DIM(10, 3, 7)

ARRAY2_DIM(11, 0, 8)
ARRAY2_DIM(11, 1, 8)
ARRAY2_DIM(11, 2, 8)
ARRAY2_DIM(11, 3, 8)

ARRAY2_DIM(12, 0, 9)
ARRAY2_DIM(12, 1, 9)
ARRAY2_DIM(12, 2, 9)
ARRAY2_DIM(12, 3, 9)


ARRAY_DIM(13, 0)
ARRAY_DIM(13, 1)
ARRAY_DIM(13, 2)
ARRAY_DIM(13, 3)

ARRAY_DIM(14, 0)
ARRAY_DIM(14, 1)
ARRAY_DIM(14, 2)
ARRAY_DIM(14, 3)

ARRAY_DIM(15, 0)
ARRAY_DIM(15, 1)
ARRAY_DIM(15, 2)
ARRAY_DIM(15, 3)

ARRAY_DIM(16, 0)
ARRAY_DIM(16, 1)
ARRAY_DIM(16, 2)
ARRAY_DIM(16, 3)

ARRAY_DIM(17, 0)
ARRAY_DIM(17, 1)
ARRAY_DIM(17, 2)
ARRAY_DIM(17, 3)

ARRAY_DIM(18, 0)
ARRAY_DIM(18, 1)
ARRAY_DIM(18, 2)
ARRAY_DIM(18, 3)

ARRAY_DIM(19, 0)
ARRAY_DIM(19, 1)
ARRAY_DIM(19, 2)
ARRAY_DIM(19, 3)

/* Following creates typesmaps as typemap( python, in) const float/double/int/uint */

#define CONST_ARRAY_TYPEMAP(NAME, BASE)\
%typemap(python,in) const BASE* (PyObject* temp_)\
{\
	$1 = _PyObject_As##NAME($input, &temp_, NULL);\
}\
\
%typemap(python,freearg) const BASE*\
{\
	_PyObject_AsArray_Cleanup($1, temp_$argnum);\
}

CONST_ARRAY_TYPEMAP(FloatArray, float)

CONST_ARRAY_TYPEMAP(DoubleArray, double)

CONST_ARRAY_TYPEMAP(CharArray, signed char)

CONST_ARRAY_TYPEMAP(UnsignedCharArray, unsigned char)

CONST_ARRAY_TYPEMAP(ShortArray, short)

CONST_ARRAY_TYPEMAP(UnsignedShortArray, unsigned short)

CONST_ARRAY_TYPEMAP(IntArray, int)

CONST_ARRAY_TYPEMAP(UnsignedIntArray, unsigned int)


#define POINTER_TYPEMAP(NAME, BASE)\
%typemap(python,in) BASE *pointer\
{\
	$1 = _PyObject_As##NAME($input, NULL, NULL);\
}\
%typemap(python,freearg) BASE *pointer\
{\
}

#define NOTNULL_TYPEMAP(NAME, BASE)\
%typemap(python,check) BASE * v\
{\
	if (!$1) {\
		PyErr_Format( PyExc_TypeError, "Expect non-null NAME pointer (i.e. an array/list/tuple) for argument %d, got null pointer", $argnum );\
		return NULL;\
	}\
}



POINTER_TYPEMAP(FloatArray, float)
NOTNULL_TYPEMAP(FloatArray, float)

POINTER_TYPEMAP(DoubleArray, double)
NOTNULL_TYPEMAP(DoubleArray, double)

POINTER_TYPEMAP(CharArray, signed char)
NOTNULL_TYPEMAP(CharArray, signed char)

POINTER_TYPEMAP(UnsignedCharArray, unsigned char)
NOTNULL_TYPEMAP(UnsignedCharArray, unsigned char)

POINTER_TYPEMAP(ShortArray, short)
NOTNULL_TYPEMAP(ShortArray, short)

POINTER_TYPEMAP(UnsignedShortArray, unsigned short)
NOTNULL_TYPEMAP(UnsignedShortArray, unsigned short)

POINTER_TYPEMAP(IntArray, int)
NOTNULL_TYPEMAP(IntArray, int)

POINTER_TYPEMAP(UnsignedIntArray, unsigned int)
NOTNULL_TYPEMAP(UnsignedIntArray, unsigned int)

%typemap(python,in) void* pointer
{
	$1 = _PyObject_AsPointer($input);
}

%typemap(python,freearg) void* pointer
{
}


#define ARRAY_OUT(NAME, TYPE, SIZE, DEFAULT, PY_OBJECT)\
%typemap(in, numinputs=0) TYPE[SIZE] (TYPE temp_[SIZE])\
{\
	int i;\
	$1 = temp_;\
	for (i = 0; i < SIZE; i++) $1[i] = DEFAULT;\
}\
\
%typemap(python,argout) TYPE[SIZE]\
{\
	int n, dims[2];\
	Py_XDECREF($result);\
	/* XXX this is a hack relying on not getting back particular values from funcs */\
	for (n = 0; n < SIZE && $1[n] != DEFAULT; n++);\
	switch (n)\
	{\
	case 0:\
		Py_INCREF(Py_None);\
		$result = Py_None;\
		break;\
	case 1:\
		$result = PY_OBJECT($1[0]);\
		break;\
	case 16:\
		dims[0] = 4;\
		dims[1] = 4;\
		$result = _PyObject_From##NAME(2, dims, $1, 0);\
		break;\
	default:\
		$result = _PyTuple_From##NAME(n, $1);\
	}\
}


ARRAY_OUT(FloatArray, float, 1, -FLT_MAX, PyFloat_FromDouble)

ARRAY_OUT(DoubleArray, double, 1, -DBL_MAX, PyFloat_FromDouble)

ARRAY_OUT(FloatArray, float, 4, -FLT_MAX, PyFloat_FromDouble)

ARRAY_OUT(DoubleArray, double, 4, -DBL_MAX, PyFloat_FromDouble)

ARRAY_OUT(IntArray, int, 4, INT_MIN, PyInt_FromLong)

ARRAY_OUT(UnsignedCharArray, unsigned char, 4, 255, PyInt_FromLong)

ARRAY_OUT(FloatArray, float, 16, -FLT_MAX, PyFloat_FromDouble)

ARRAY_OUT(DoubleArray, double, 16, -DBL_MAX, PyFloat_FromDouble)

ARRAY_OUT(IntArray, int, 16, INT_MIN, PyInt_FromLong)

ARRAY_OUT(UnsignedCharArray, unsigned char, 16, 255, PyInt_FromLong)



