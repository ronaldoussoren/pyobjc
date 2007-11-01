#include "../config.h"

#ifndef GL_ABGR_EXT
#define GL_ABGR_EXT 0x8000
#endif

#define _PyTuple_From(NAME, BASE, PY_OBJECT)\
PyObject* _PyTuple_From##NAME(int len, BASE* data)\
{\
	PyObject* result;\
	int i;\
\
	switch (len)\
	{\
	case 0:\
		Py_INCREF(result = Py_None);\
		break;\
	case 1:\
		result = PY_OBJECT(data[0]);\
		break;\
	default:\
		result = PyTuple_New(len);\
		for (i = 0; i < len; i++) PyTuple_SetItem(result, i, PY_OBJECT(data[i]));\
	}\
\
	return result;\
}

_PyTuple_From(UnsignedCharArray, unsigned char, PyInt_FromLong)

_PyTuple_From(CharArray, signed char, PyInt_FromLong)

_PyTuple_From(UnsignedShortArray, unsigned short, PyInt_FromLong)

_PyTuple_From(ShortArray, short, PyInt_FromLong)

_PyTuple_From(UnsignedIntArray, unsigned int, PyLong_FromUnsignedLong)

_PyTuple_From(IntArray, int, PyInt_FromLong)

_PyTuple_From(FloatArray, float, PyFloat_FromDouble)

_PyTuple_From(DoubleArray, double, PyFloat_FromDouble)


#define STRING_PyObject_From(PREFIX, NAME, BASE)\
PyObject* __PyObject_From##NAME(int nd, int* dims, BASE* data)\
{\
	PyObject *result;\
	int i, l;\
\
	if (nd > 1)\
	{\
		result = PyList_New(*dims);\
		for (i = 1, l = 1; i < nd; i++) l *= dims[i];\
		for (i = 0; i < *dims; i++) PyList_SetItem(result, i, __PyObject_From##NAME(nd-1, dims+1, data + i*l));\
	}\
	else result = PyString_FromStringAndSize(data, *dims);\
\
	return result;\
}\
\
PyObject* PREFIX##PyObject_From##NAME(int nd, int* dims, BASE* data, int own)\
{\
	PyObject* result = __PyObject_From##NAME(nd, dims, data);\
	if (own) PyMem_Del(data);\
	return result;\
}


#define _PyObject_From(PREFIX, NAME, BASE, PY_OBJECT)\
PyObject* __PyObject_From##NAME(int nd, int* dims, BASE* data)\
{\
	PyObject *result;\
	int i, l;\
\
	if (nd)\
	{\
		result = PyList_New(*dims);\
		for (i = 1, l = 1; i < nd; i++) {\
			l *= dims[i];\
		}\
		for (i = 0; i < *dims; i++) PyList_SetItem(result, i, __PyObject_From##NAME(nd-1, dims+1, data + i*l));\
	}\
	else result = PY_OBJECT(*data);\
\
	return result;\
}\
\
PyObject* PREFIX##PyObject_From##NAME(int nd, int* dims, BASE* data, int own)\
{\
	PyObject* result = __PyObject_From##NAME(nd, dims, data);\
	if (own) PyMem_Del(data);\
	return result;\
}

#define NUMERIC_PyObject_From(NAME, BASE, TYPECODE)\
PyObject* _PyObject_From##NAME(int nd, int* dims, BASE* data, int own)\
{\
	if (PyArray_API)\
	{\
		BASE* my;\
		int i, l;\
		PyObject * result;\
		result = PyArray_FromDims(nd, dims, TYPECODE);\
		/* get total length */\
		for (i = 0, l = 1; i < nd; i++) {\
			l *= dims[i];\
		}\
		/* get a simple array of base-type to copy */\
		my = (BASE *) ((PyArrayObject *) result)->data;\
		/* copy the data */\
		for (i=0;i<l;i++) { my[i] = data[i];}\
			if (own) {\
				PyMem_Del(data);\
			}\
		return result;\
	}\
	return NonNumeric_PyObject_From##NAME(nd, dims, data, own);\
}

#ifdef NUMERIC
STRING_PyObject_From(NonNumeric_, UnsignedCharArray, unsigned char)
NUMERIC_PyObject_From(UnsignedCharArray, unsigned char, PyArray_UBYTE)
#else
STRING_PyObject_From(_, UnsignedCharArray, unsigned char)
#endif

#ifdef NUMERIC
_PyObject_From(NonNumeric_, CharArray, signed char, PyInt_FromLong)
NUMERIC_PyObject_From(CharArray, signed char, PyArray_SBYTE)
#else
_PyObject_From(_, CharArray, signed char, PyInt_FromLong)
#endif

_PyObject_From(_, UnsignedShortArray, unsigned short, PyInt_FromLong)

#ifdef NUMERIC
_PyObject_From(NonNumeric_, ShortArray, short, PyInt_FromLong)
NUMERIC_PyObject_From(ShortArray, short, PyArray_SHORT)
#else
_PyObject_From(_, ShortArray, short, PyInt_FromLong)
#endif

_PyObject_From(_, UnsignedIntArray, unsigned int, PyLong_FromUnsignedLong)

#ifdef NUMERIC
_PyObject_From(NonNumeric_, IntArray, int, PyInt_FromLong)
NUMERIC_PyObject_From(IntArray, int, PyArray_INT)
#else
_PyObject_From(_, IntArray, int, PyInt_FromLong)
#endif

#ifdef NUMERIC
_PyObject_From(NonNumeric_, FloatArray, float, PyFloat_FromDouble)
NUMERIC_PyObject_From(FloatArray, float, PyArray_FLOAT)
#else
_PyObject_From(_, FloatArray, float, PyFloat_FromDouble)
#endif

#ifdef NUMERIC
_PyObject_From(NonNumeric_, DoubleArray, double, PyFloat_FromDouble)
NUMERIC_PyObject_From(DoubleArray, double, PyArray_DOUBLE)
#else
_PyObject_From(_, DoubleArray, double, PyFloat_FromDouble)
#endif


PyObject* _PyObject_FromArray(GLenum type, int nd, int *dims, void* data, int own)
{
	switch (type)
	{
	case GL_UNSIGNED_BYTE:
		return _PyObject_FromUnsignedCharArray(nd, dims, data, own);
	case GL_BYTE:
		return _PyObject_FromCharArray(nd, dims, data, own);
	case GL_UNSIGNED_SHORT:
		return _PyObject_FromUnsignedShortArray(nd, dims, data, own);
	case GL_SHORT:
		return _PyObject_FromShortArray(nd, dims, data, own);
	case GL_UNSIGNED_INT:
		return _PyObject_FromUnsignedIntArray(nd, dims, data, own);
	case GL_INT:
		return _PyObject_FromIntArray(nd, dims, data, own);
	case GL_FLOAT:
		return _PyObject_FromFloatArray(nd, dims, data, own);
	case GL_DOUBLE:
		return _PyObject_FromDoubleArray(nd, dims, data, own);
	}

	if (own) PyMem_Del(data);
	PyErr_SetString(PyExc_Exception, "Unknown type.");
	return NULL;
}

#ifndef GL_SGIS_texture4D
#define GL_PACK_SKIP_VOLUMES_SGIS         0x8130
#define GL_PACK_IMAGE_DEPTH_SGIS          0x8131
#define GL_UNPACK_SKIP_VOLUMES_SGIS       0x8132
#define GL_UNPACK_IMAGE_DEPTH_SGIS        0x8133
#define GL_TEXTURE_4D_SGIS                0x8134
#define GL_PROXY_TEXTURE_4D_SGIS          0x8135
#define GL_TEXTURE_4DSIZE_SGIS            0x8136
#define GL_TEXTURE_WRAP_Q_SGIS            0x8137
#define GL_MAX_4D_TEXTURE_SIZE_SGIS       0x8138
#define GL_TEXTURE_4D_BINDING_SGIS        0x814F
#endif

#ifndef GL_EXT_cmyka
#define GL_CMYK_EXT                       0x800C
#define GL_CMYKA_EXT                      0x800D
#define GL_PACK_CMYK_HINT_EXT             0x800E
#define GL_UNPACK_CMYK_HINT_EXT           0x800F
#endif

#ifndef GL_VERSION_1_2
#define GL_PACK_SKIP_IMAGES				0x806B
#define GL_PACK_IMAGE_HEIGHT			0x806C
#define GL_UNPACK_SKIP_IMAGES			0x806D
#define GL_UNPACK_IMAGE_HEIGHT			0x806E
#define GL_TEXTURE_3D				0x806F
#define GL_PROXY_TEXTURE_3D			0x8070
#define GL_TEXTURE_DEPTH			0x8071
#define GL_TEXTURE_WRAP_R			0x8072
#define GL_MAX_3D_TEXTURE_SIZE			0x8073
#define GL_TEXTURE_BINDING_3D			0x806A

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
#endif

#ifndef GL_SGIX_ycrcb
#define GL_YCRCB_422_SGIX                 0x81BB
#define GL_YCRCB_444_SGIX                 0x81BC
#endif

#ifndef GL_OML_subsample
#define GL_FORMAT_SUBSAMPLE_24_24_OML 0x8982
#define GL_FORMAT_SUBSAMPLE_244_244_OML 0x8983
#endif


void* SetupPixelRead(int rank, GLenum format, GLenum type, int *dims)
{
	int i, size;

	glPixelStorei(GL_PACK_SWAP_BYTES, 0);
	glPixelStorei(GL_PACK_LSB_FIRST, 0);

	switch (rank)
	{
	case 4:
		glPixelStorei(GL_PACK_SKIP_VOLUMES_SGIS, 0);
		glPixelStorei(GL_PACK_IMAGE_DEPTH_SGIS, 0);
	case 3:
		glPixelStorei(GL_PACK_SKIP_IMAGES, 0);
		glPixelStorei(GL_PACK_IMAGE_HEIGHT, 0);
	case 2:
		glPixelStorei(GL_PACK_ROW_LENGTH, 0);
		glPixelStorei(GL_PACK_SKIP_ROWS, 0);
		glPixelStorei(GL_PACK_ALIGNMENT, 1);
	case 1:
		glPixelStorei(GL_PACK_SKIP_PIXELS, 0);
	}

	switch (format)
	{
	case GL_RED:
	case GL_GREEN:
	case GL_BLUE:
	case GL_ALPHA:
	case GL_LUMINANCE:
	case GL_LUMINANCE_ALPHA:
	case GL_COLOR_INDEX:
	case GL_STENCIL_INDEX:
	case GL_DEPTH_COMPONENT:
		dims[rank] = 1;
		break;
	case GL_RGB:
	case GL_BGR:
		dims[rank] = 3;
		break;
	case GL_RGBA:
	case GL_BGRA:
	case GL_ABGR_EXT:
	case GL_CMYK_EXT:
		dims[rank] = 4;
		break;
	case GL_CMYKA_EXT:
		dims[rank] = 5;
		break;
	default:
		PyErr_SetString(PyExc_Exception, "Unknown format.");
		return NULL;
	}

	for (i = 0, size = 1; i <= rank; i++) size *= dims[i];

	switch (type)
	{
	case GL_UNSIGNED_BYTE:
		return PyMem_New(GLubyte, size);
	case GL_BYTE:
		return PyMem_New(GLbyte, size);
	case GL_UNSIGNED_SHORT:
		return PyMem_New(GLushort, size);
	case GL_SHORT:
		return PyMem_New(GLshort, size);
	case GL_UNSIGNED_INT:
		return PyMem_New(GLuint, size);
	case GL_INT:
		return PyMem_New(GLint, size);
	case GL_FLOAT:
		return PyMem_New(GLfloat, size);
	default:
		PyErr_SetString(PyExc_Exception, "Unknown type.");
		return NULL;
	}
}

void* SetupRawPixelRead(GLenum format, GLenum type, int rank, const int *dims, int* size)
{
	GLint skip_pixels = 0, _size;

	switch (format)
	{
	case GL_RED:
	case GL_GREEN:
	case GL_BLUE:
	case GL_ALPHA:
	case GL_LUMINANCE:
	case GL_LUMINANCE_ALPHA:
	case GL_COLOR_INDEX:
	case GL_STENCIL_INDEX:
	case GL_DEPTH_COMPONENT:
		_size = 8;
		break;
	case GL_RGB:
	case GL_BGR:
		_size = 24;
		break;
	case GL_RGBA:
	case GL_BGRA:
	case GL_ABGR_EXT:
	case GL_CMYK_EXT:
		_size = 32;
		break;
	case GL_CMYKA_EXT:
		_size = 40;
		break;
	case GL_BITMAP:
		if (type != GL_UNSIGNED_BYTE)
		{
			PyErr_SetString(PyExc_Exception, "Unknown format.");
			return NULL;
		}
		_size = 1;
		break;
	case GL_YCRCB_422_SGIX:
		if (type != GL_UNSIGNED_BYTE)
		{
			PyErr_SetString(PyExc_Exception, "Unknown format.");
			return NULL;
		}
		_size = 8;
		break;
	case GL_YCRCB_444_SGIX:
		if (type != GL_UNSIGNED_SHORT)
		{
			PyErr_SetString(PyExc_Exception, "Unknown format.");
			return NULL;
		}
		_size = 8;
		break;
	case GL_FORMAT_SUBSAMPLE_24_24_OML:
	case GL_FORMAT_SUBSAMPLE_244_244_OML:
		if (type != GL_UNSIGNED_INT_10_10_10_2)
		{
			PyErr_SetString(PyExc_Exception, "Unknown format.");
			return NULL;
		}
		_size = 32;
		break;
	default:
		PyErr_SetString(PyExc_Exception, "Unknown format.");
		return NULL;
	}

	switch (type)
	{
	case GL_UNSIGNED_BYTE_3_3_2:
	case GL_UNSIGNED_BYTE_2_3_3_REV:
		if (_size != 24)
		{
			PyErr_SetString(PyExc_Exception, "Incompatible type/format");
			return NULL;
		}
		_size = 8*sizeof(GLubyte);
		break;
	case GL_UNSIGNED_SHORT_4_4_4_4:
	case GL_UNSIGNED_SHORT_4_4_4_4_REV:
	case GL_UNSIGNED_SHORT_5_5_5_1:
	case GL_UNSIGNED_SHORT_1_5_5_5_REV:
		if (_size != 32)
		{
			PyErr_SetString(PyExc_Exception, "Incompatible type/format");
			return NULL;
		}
		_size = 8*sizeof(GLushort);
		break;
	case GL_UNSIGNED_SHORT_5_6_5:
	case GL_UNSIGNED_SHORT_5_6_5_REV:
		if (_size != 24)
		{
			PyErr_SetString(PyExc_Exception, "Incompatible type/format");
			return NULL;
		}
		_size = 8*sizeof(GLushort);
		break;
	case GL_UNSIGNED_INT_8_8_8_8:
	case GL_UNSIGNED_INT_8_8_8_8_REV:
	case GL_UNSIGNED_INT_10_10_10_2:
	case GL_UNSIGNED_INT_2_10_10_10_REV:
		if (_size != 32)
		{
			PyErr_SetString(PyExc_Exception, "Incompatible type/format");
			return NULL;
		}
		_size = 8*sizeof(GLuint);
		break;
	case GL_UNSIGNED_BYTE:
		_size *= sizeof(GLubyte);
		break;
	case GL_BYTE:
		_size *= sizeof(GLbyte);
		break;
	case GL_UNSIGNED_SHORT:
		_size *= sizeof(GLushort);
		break;
	case GL_SHORT:
		_size *= sizeof(GLshort);
		break;
	case GL_UNSIGNED_INT:
		_size *= sizeof(GLuint);
		break;
	case GL_INT:
		_size *= sizeof(GLint);
		break;
	case GL_FLOAT:
		_size *= sizeof(GLfloat);
		break;
	case GL_DOUBLE:
		_size *= sizeof(GLdouble);
		break;
	default:
		PyErr_SetString(PyExc_Exception, "Unknown type.");
		return NULL;
	}

	glGetIntegerv(GL_PACK_SKIP_PIXELS, &skip_pixels);

	if (rank == 1)
	{
		_size *= skip_pixels + dims[0];
		_size = (_size + (8 - (_size % 8)) % 8) / 8;
	}
	else
	{
		GLint row_length = 0, alignment = 1;

		glGetIntegerv(GL_PACK_ALIGNMENT, &alignment);
		glGetIntegerv(GL_PACK_ROW_LENGTH, &row_length);
		if (row_length <= 0) row_length = dims[0];

		_size *= row_length;
		_size = (_size + (8 - (_size % 8)) % 8) / 8;
		_size += (alignment - (_size % alignment)) % alignment;

		if (rank == 2)
		{
			GLint skip_rows = 0;

			glGetIntegerv(GL_PACK_SKIP_ROWS, &skip_rows);
			_size *= skip_rows + dims[1];
		}
		else
		{
			GLint image_height = 0;

			glGetIntegerv(GL_PACK_IMAGE_HEIGHT, &image_height);
			if (image_height <= 0) image_height = dims[1];

			_size *= image_height;

			if (rank == 3)
			{
				GLint skip_images = 0;

				glGetIntegerv(GL_PACK_SKIP_IMAGES, &skip_images);
				_size *= skip_images + dims[2];
			}
			else
			{
				GLint image_depth = 0, skip_volumes = 0;

				glGetIntegerv(GL_PACK_SKIP_VOLUMES_SGIS, &skip_volumes);
				glGetIntegerv(GL_PACK_IMAGE_DEPTH_SGIS, &image_depth);
				if (image_depth <= 0) image_depth = dims[2];

				_size *= image_depth * (skip_volumes + dims[3]);
			}
		}
	}

	if (size) *size = _size;

	return PyMem_Malloc(_size);
}

void SetupPixelWrite(int rank)
{
	glPixelStorei(GL_UNPACK_SWAP_BYTES, 0);
	glPixelStorei(GL_UNPACK_LSB_FIRST, 0);

	switch (rank)
	{
	case 4:
		glPixelStorei(GL_UNPACK_SKIP_VOLUMES_SGIS, 0);
		glPixelStorei(GL_UNPACK_IMAGE_DEPTH_SGIS, 0);
	case 3:
		glPixelStorei(GL_UNPACK_SKIP_IMAGES, 0);
		glPixelStorei(GL_UNPACK_IMAGE_HEIGHT, 0);
	case 2:
		glPixelStorei(GL_UNPACK_ROW_LENGTH, 0);
		glPixelStorei(GL_UNPACK_SKIP_ROWS, 0);
		glPixelStorei(GL_UNPACK_ALIGNMENT, 1);
	case 1:
		glPixelStorei(GL_UNPACK_SKIP_PIXELS, 0);
	}
}

int __PyObject_AsArray_Size(PyObject* x)
{
	int i, l, n, p;
	PyObject* item;

	if (PyString_Check(x))
	{
		return PyString_Size(x);
	}
	else if (PySequence_Check(x))
	{
		for (i = 0, l = 0, n = PySequence_Length(x); i < n; i++)
		{
			item = PySequence_GetItem(x, i);
			if (!item) return 0;
			l += p = __PyObject_AsArray_Size(item);
			Py_DECREF(item);
			if (!p) return 0;
		}
		return l;
	}
	else
	{
		return PyNumber_Check(x);
	}
}

#ifdef NUMERIC

#define _PyObject_AsArray_Size(x) ((x == Py_None) ? 0 : (PyArray_API && (PyArray_Check(x)) ? PyArray_Size(x) : __PyObject_AsArray_Size(x)))

#else /* NUMERIC */

#define _PyObject_AsArray_Size(x) ((x == Py_None) ? 0 : __PyObject_AsArray_Size(x))

#endif /* NUMERIC */

#define __PyObject_As(NAME, BASE, PY_NUMBER_CAST, NUMBER_CAST)\
int __PyObject_As##NAME(BASE* dest, PyObject* src)\
{\
	int i, n, l, p;\
	char* b;\
	PyObject* item;\
\
	if (PyString_Check(src))\
	{\
		PyString_AsStringAndSize(src, &b, &n);\
		for (i = 0; i < n; i++) dest[i] = (BASE)b[i];\
		return n;\
	}\
	else if (PySequence_Check(src))\
	{\
		for (i = 0, l = 0, n = PySequence_Length(src); i < n; i++)\
		{\
			item = PySequence_GetItem(src, i);\
			if (!item) return 0;\
			l += (p = __PyObject_As##NAME(dest + l, item));\
			Py_DECREF(item);\
			if (!p) return 0;\
		}\
		return l;\
	}\
	else\
	{\
		item = PY_NUMBER_CAST(src);\
		if (!item) return 0;\
		dest[0] = (BASE)NUMBER_CAST(item);\
		Py_DECREF(item);\
		return 1;\
	}\
}\
BASE* NonNumeric_PyObject_As##NAME(PyObject* source, PyObject** temp, int* len)\
{\
	int n;\
	BASE* target = NULL;\
	if (n = __PyObject_AsArray_Size(source))\
	{\
		if (len) *len = n;\
		target = PyMem_New(BASE, n);\
		if (!target || !__PyObject_As##NAME(target, source))\
		{\
			PyMem_Del(target);\
			PyErr_SetString(PyExc_ValueError, "Unable to convert object to array, out of memory?");\
			return NULL;\
		}\
	}\
	else\
	{\
		PyErr_SetString(PyExc_ValueError, "Unable to convert object to array, i.e. possible empty sequences or items that are not numbers.");\
		return NULL;\
	}\
	return target;\
}


#define _PyObject_As(NAME, BASE)\
BASE* _PyObject_As##NAME(PyObject* source, PyObject** temp, int* len)\
{\
	if (temp) *temp = NULL;\
	if (source == Py_None) return NULL;\
	return NonNumeric_PyObject_As##NAME(source, temp, len);\
}


#ifdef NUMERIC
#define NUMERIC_PyObject_As(NAME, BASE, TYPECODE)\
BASE* Numeric_PyObject_As##NAME(PyObject *source, PyObject **temp, int *len)\
{\
	int size;\
	BASE* target = NULL;\
	PyArrayObject *contiguous = NULL;\
	/*printf( "Getting contiguous\n");*/\
	/* yes, this is redundant, as we are borrowing caller's pointer, I'm paranoid */\
	Py_INCREF( source );\
	contiguous = (PyArrayObject*)PyArray_ContiguousFromObject(source, TYPECODE | SAVESPACEBIT, 0, 0);\
	if (contiguous)\
	{\
		/* only need to calculate this if we actually got the contiguous array */\
		size = PyArray_Size(contiguous);\
		/*printf( "Got array size %i\n", size );*/\
		if (len) { *len = size;}\
		if (temp) {\
			/*printf( "Pointing passed temp pointer to contiguous data pointer\n" );*/\
			*temp = (PyObject*)contiguous;\
			target = (BASE*)contiguous->data;\
		} else {\
			/*printf( "Creating new target array\n");*/\
			target = PyMem_New(BASE, size);\
			/*printf( "Copying old data to new\n");*/\
			memcpy(target, contiguous->data, sizeof(BASE)*size);\
			/*printf( "Decrefing contiguous data array...\n");*/\
			Py_DECREF((PyObject*)contiguous);\
		}\
	}\
	else\
	{\
		PyErr_SetString(PyExc_ValueError, "Unable to get contiguous array from object");\
	}\
	Py_DECREF( source );\
	return target;\
}\
BASE* _PyObject_As##NAME(PyObject *source, PyObject **temp, int *len)\
{\
	if (temp) { *temp = NULL;}\
	if (source == Py_None) {return NULL;}\
	if (PyArray_API && PyArray_Check(source)) return Numeric_PyObject_As##NAME(source, temp, len);\
	return NonNumeric_PyObject_As##NAME(source, temp, len);\
}
#else
#define NUMERIC_PyObject_As(BASE, NAME, TYPECODE) _PyObject_As(BASE, NAME)
#endif


#define _PyObject_AsArray_Cleanup(target, temp) if (temp) Py_XDECREF(temp); else PyMem_Del(target)


__PyObject_As(FloatArray, float, PyNumber_Float, PyFloat_AsDouble)
NUMERIC_PyObject_As(FloatArray, float, PyArray_FLOAT)

__PyObject_As(DoubleArray, double, PyNumber_Float, PyFloat_AsDouble)
NUMERIC_PyObject_As(DoubleArray, double, PyArray_DOUBLE)

__PyObject_As(CharArray, signed char, PyNumber_Int, PyInt_AsLong)
NUMERIC_PyObject_As(CharArray, signed char, PyArray_SBYTE)

__PyObject_As(UnsignedCharArray, unsigned char, PyNumber_Int, PyInt_AsLong)
NUMERIC_PyObject_As(UnsignedCharArray, unsigned char, PyArray_UBYTE)

__PyObject_As(ShortArray, short, PyNumber_Int, PyInt_AsLong)
NUMERIC_PyObject_As(ShortArray, short, PyArray_SHORT)

__PyObject_As(UnsignedShortArray, unsigned short, PyNumber_Int, PyInt_AsLong)
_PyObject_As(UnsignedShortArray, unsigned short)

__PyObject_As(IntArray, int, PyNumber_Int, PyInt_AsLong)
NUMERIC_PyObject_As(IntArray, int, PyArray_INT)

__PyObject_As(UnsignedIntArray, unsigned int, PyNumber_Long, PyLong_AsUnsignedLong)
_PyObject_As(UnsignedIntArray, unsigned int)


void* _PyObject_AsPointer(PyObject* x)
{
	int len;
	char *buffer, *bufferCopy;

	PyString_AsStringAndSize(x = PyObject_Str(x), &buffer, &len);
	bufferCopy = PyMem_New(char, len+1);
	memcpy(bufferCopy, buffer, len);
	bufferCopy[len] = '\0';

	return (void*)bufferCopy;
}

int __PyObject_Dimension(PyObject* x, int rank)
{
	PyObject *item;
	int n;

	if (!PySequence_Check(x)) return -1;

	if (rank == 0) return PySequence_Size(x);

	if (PyString_Check(x)) return -1;

	item = PySequence_GetItem(x, 0);
	n = __PyObject_Dimension(item, --rank);
	Py_DECREF(item);

	return n;
}

int _PyObject_Dimension(PyObject* x, int rank)
{
#ifdef NUMERIC
	if (PyArray_API && PyArray_Check(x))
	{
		return (((PyArrayObject*)x)->nd > rank) ? ((PyArrayObject*)x)->dimensions[rank] : -1;
	}
#endif
	return __PyObject_Dimension(x, rank);
}


#if PY_VERSION_HEX < 0x02000000
int PyString_AsStringAndSize(PyObject *obj,	char **s, int *len)
{
	int l = PyString_Size(obj);

	if (s) *s = PyString_AsString(obj);
	if (len) *len = l;

	return l;
}
#endif


void init_util()
{
#ifdef NUMERIC
	import_array();
#endif
}
