typedef unsigned int GLenum;
typedef unsigned char GLboolean;
typedef unsigned int GLbitfield;
typedef signed char GLbyte;
typedef short GLshort;
typedef int GLint;
typedef int GLsizei;
typedef unsigned char GLubyte;
typedef unsigned short GLushort;
typedef unsigned int GLuint;
typedef float GLfloat;
typedef float GLclampf;
typedef double GLdouble;
typedef double GLclampd;
typedef void GLvoid;

%include simple_typemaps.inc
%include complex_typemaps.inc


#define DOC(NAME, VALUE)\
%{\
static char _doc_##NAME[] = VALUE;\
%}

%{

#define PyErr_XPrint() if (PyErr_Occurred()) PyErr_Print()


#if HAS_DYNAMIC_EXT

#define DECLARE_EXT(PROC_NAME, RET, ERROR_RET, PROTO, CALL)\
RET PROC_NAME PROTO\
{\
	typedef RET (APIENTRY *proc_##PROC_NAME) PROTO;\
	proc_##PROC_NAME proc = (proc_##PROC_NAME)GL_GetProcAddress(#PROC_NAME);\
	if (proc) return proc CALL;\
	PyErr_SetGLErrorMessage( GL_INVALID_OPERATION, "Dynamic function loading not implemented/supported on this platform" );\
	return ERROR_RET;\
}

#define DECLARE_VOID_EXT(PROC_NAME, PROTO, CALL)\
void PROC_NAME PROTO\
{\
	typedef void (APIENTRY *proc_##PROC_NAME) PROTO;\
	proc_##PROC_NAME proc = (proc_##PROC_NAME)GL_GetProcAddress(#PROC_NAME);\
	if (proc) proc CALL;\
	else {\
		PyErr_SetGLErrorMessage( GL_INVALID_OPERATION, "Dynamic function loading not implemented/supported on this platform" );\
	}\
}

#else

#define DECLARE_EXT(PROC_NAME, RET, ERROR_RET, PROTO, CALL)\
RET PROC_NAME PROTO\
{\
	PyErr_SetGLErrorMessage( GL_INVALID_OPERATION, "Dynamic function loading not implemented/supported on this platform" );\
	return ERROR_RET;\
}


#define DECLARE_VOID_EXT(PROC_NAME, PROTO, CALL)\
void PROC_NAME PROTO\
{\
	PyErr_SetGLErrorMessage( GL_INVALID_OPERATION, "Dynamic function loading not implemented/supported on this platform" );\
}

#endif


#define _PyTuple_From(NAME, BASE) PyObject* _PyTuple_From##NAME(int len, BASE* data);

_PyTuple_From(UnsignedCharArray, unsigned char)

_PyTuple_From(CharArray, signed char)

_PyTuple_From(UnsignedShortArray, unsigned short)

_PyTuple_From(ShortArray, short)

_PyTuple_From(UnsignedIntArray, unsigned int)

_PyTuple_From(IntArray, int)

_PyTuple_From(FloatArray, float)

_PyTuple_From(DoubleArray, double)


#define _PyObject_From(NAME, BASE) PyObject* _PyObject_From##NAME(int nd, int* dims, BASE* data, int own);

_PyObject_From(UnsignedCharArray, unsigned char)

_PyObject_From(CharArray, signed char)

_PyObject_From(UnsignedShortArray, unsigned short)

_PyObject_From(ShortArray, short)

_PyObject_From(UnsignedIntArray, unsigned int)

_PyObject_From(IntArray, int)

_PyObject_From(FloatArray, float)

_PyObject_From(DoubleArray, double)


PyObject* _PyObject_FromArray(GLenum type, int nd, int *dims, void* data, int own);

void* SetupPixelRead(int rank, GLenum format, GLenum type, int *dims);

void SetupPixelWrite(int rank);

void* SetupRawPixelRead(GLenum format, GLenum type, int n, const int *dims, int* size);

void* _PyObject_AsPointer(PyObject* x);

/* The following line causes a warning on linux and cygwin

	The function is defined in interface_utils.c, which is
	linked to each extension module.  For some reason, though,
	this declaration doesn't get recognised as a declaration
	prototype for that function.
*/
void init_util();

typedef void *PTR;

typedef struct
{
	void (*_decrement)(void* pointer);
	void (*_decrementPointer)(GLenum pname);
	int (*_incrementLock)(void *pointer);
	int (*_incrementPointerLock)(GLenum pname);
	void (*_acquire)(void* pointer);
	void (*_acquirePointer)(GLenum pname);
#if HAS_DYNAMIC_EXT
	PTR (*GL_GetProcAddress)(const char* name);
#endif
	int (*InitExtension)(const char *name, const char** procs);
	PyObject *_GLerror;
	PyObject *_GLUerror;
}  util_API;

%}

#ifdef EXPORT_UTIL
%{

#ifndef GL_VERSION_1_1
PyObject *contexts;

typedef struct
{
	PyObject_HEAD
	GLenum feedback_type;
	GLfloat *feedback_buffer;
	GLuint *selection_buffer;
} PyGLcontext;


static void PyGLcontext_Del(PyObject *self)
{
	PyObject_Del(self);
}


PyTypeObject PyGLcontext_Type =
{
    PyObject_HEAD_INIT(0)
    0,									// ob_size
    "GLcontext",					// tp_name
    sizeof(PyGLcontext),			// tp_basicsize
    0,									// tp_itemsize
    PyGLcontext_Del,				// tp_dealloc
};


PyGLcontext* PyGLcontext_New()
{
	PyGLcontext *self = PyObject_NEW(PyGLcontext, &PyGLcontext_Type);

	self->feedback_buffer = NULL;
	self->selection_buffer = NULL;

	return self;
}


PyGLcontext *GetGLcontext()
{
	if (CurrentContextIsValid())
	{
		PyObject *key = PyInt_FromLong(GetCurrentContext());
		PyGLcontext *context = (PyGLcontext*)PyDict_GetItem(contexts, key);
		if (!context)
		{
			context = PyGLcontext_New();
			PyDict_SetItem(contexts, key, (PyObject*)context);
		}
		Py_DECREF(key);
		return context;
	}
	return NULL;
}

#endif /* GL_VERSION_1_1 */

#define POINTER_COUNT 6

typedef struct
{
	void *pointers[POINTER_COUNT+1];
	int ref_count;
} PointerLock;

PointerLock *PointerLocks = NULL;
int PointerLockCount = 0;

GLenum *PointerTypes = NULL;
int PointerTypeCount = 0;

#ifndef GL_VERSION_1_1
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_vertex_array)
DECLARE_VOID_EXT(glGetPointervEXT, (GLenum pname, void** params)), (GLenum pname, void** params))
#endif

static char *va_proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_vertex_array)
	"glGetPointervEXT",
#endif
	NULL
};

int InitExtension(const char* name, const char** procs);

void glGetPointerv(GLenum pname, void** params)
{
	if (InitExtension("GL_EXT_vertex_array", va_proc_names))
	{
		glGetPointervEXT(pname, params);
	} else {
		printf( "Critical failure, unable to load GL_EXT_vertex_array, expect crashes when accessing array pointers" );
	}
}
#endif /* GL_VERSION_1_1 */

/* decrementLock a pointer */
void decrementLock(void* pointer)
{
	if (pointer && PointerLocks)
	{
		int i, j;
		for (i = 0; i < PointerLockCount; i++)
		{
			for (j = 0; j < POINTER_COUNT+1; j++)
			{
				if (PointerLocks[i].pointers[j] == pointer && --PointerLocks[i].ref_count == 0)
				{
					int k;
					PyMem_Free(PointerLocks[i].pointers[0]);
					PointerLockCount--;
					for (k = i; k < PointerLockCount; k++) PointerLocks[k] = PointerLocks[k+1];
					return;
				}
			}
		}
	}
}


/* decrementLock a pointer referenced by glSelectBuffer, glFeedbackBuffer, glColorPointer, etc. */
void decrementPointerLock(GLenum pname)
{
	void* pointer = NULL;
	glGetPointerv(pname, &pointer);
	decrementLock(pointer);
}


void decrementAllLocks()
{
	int i;
	
	for (i = 0; i < PointerTypeCount; i++) decrementPointerLock(PointerTypes[i]);
}


/* increment pointer lock */
int incrementLock(void *pointer)
{
	if (pointer && PointerLocks)
	{
		int i, j;
		
		for (i = 0; i < PointerLockCount; i++)
		{
			for (j = 0; j < POINTER_COUNT+1; j++)
			{
				if (PointerLocks[i].pointers[j] == pointer)
				{
					PointerLocks[i].ref_count++;
					return 1;
				}
			}
		}
	}

	return 0;
}


void addPointerType(GLenum type)
{
	int i;
	
	for (i = 0; i < PointerTypeCount; i++) if (PointerTypes[i] == type) return;
	
	PointerTypes = (PointerTypes) ? PyMem_Resize(PointerTypes, GLenum, ++PointerTypeCount) : PyMem_New(GLenum, PointerTypeCount = 1);
	
	PointerTypes[PointerTypeCount-1] = type;
}


int incrementPointerLock(GLenum pname)
{
	void* pointer = NULL;
	int found;
	
	glGetPointerv(pname, &pointer);
	found = incrementLock(pointer);
	if (found) addPointerType(pname);

	return found;
}


void incrementAllLocks()
{
	int i;
	
	for (i = 0; i < PointerTypeCount; i++) incrementPointerLock(PointerTypes[i]);
}


/* acquire a pointer */
void acquire(void* pointer)
{
	if (pointer)
	{
		int i;
		PointerLock *lock;

		PointerLocks = (PointerLocks) ? PyMem_Resize(PointerLocks, PointerLock, ++PointerLockCount) : PyMem_New(PointerLock, PointerLockCount = 1);
		lock = PointerLocks + PointerLockCount - 1;
		(*lock).pointers[0] = pointer;
		(*lock).ref_count = 1;

		for (i = 1; i < POINTER_COUNT+1; i++) (*lock).pointers[i] = NULL;
	}
}

void acquirePointer(GLenum pname)
{
	void* pointer = NULL;
	glGetPointerv(pname, &pointer);
	acquire(pointer);
	addPointerType(pname);
}

void acquireInterleavedPointer(void* pointer, GLenum pnames[POINTER_COUNT])
{
	if (pointer)
	{
		int i;
		PointerLock *lock;

		PointerLocks = (PointerLocks) ? PyMem_Resize(PointerLocks, PointerLock, ++PointerLockCount) : PyMem_New(PointerLock, PointerLockCount = 1);
		lock = PointerLocks + PointerLockCount - 1;
		(*lock).pointers[0] = pointer;
		(*lock).ref_count = 0;

		for (i = 0; i < POINTER_COUNT; i++)
		{
			(*lock).pointers[i+1] = NULL;
			if (pnames[i])
			{
				glGetPointerv(pnames[i], (*lock).pointers + i + 1);
				if ((*lock).pointers[i+1])
				{
					addPointerType(pnames[i]);
					(*lock).ref_count++;
				}
			}
		}
	}
}

int in_extension_list(const char* name, char *list)
{
	size_t len = strlen(name);
	
	while (list && strlen(list))
	{
		if (strlen(list) >= len && !strncmp(list, name, len)) return 1;
		list = strchr(list, ' ');
		if (!list) return 0;
		list++;
	}

	return 0;
}


const char* GetPlatformExtensionsString();
void* GetExtProc(const char* name);

int has_extension(const char* name)
{
	if (CurrentContextIsValid())
	{
		return in_extension_list(name, (char*)glGetString(GL_EXTENSIONS)) ||
		       in_extension_list(name, (char*)gluGetString(GLU_EXTENSIONS)) ||
		       in_extension_list(name, (char*)GetPlatformExtensionsString());
	}

	return 0;
}


#if HAS_DYNAMIC_EXT
PyObject *ProcAddresses = NULL;

void *GL_GetProcAddress(const char* name)
{
	void *address = NULL;
	if (CurrentContextIsValid())
	{
		PyObject *key = Py_BuildValue("ls", GetCurrentContext(), name);
		PyObject *py_address = PyDict_GetItem(ProcAddresses, key);
		if (py_address) address = PyCObject_AsVoidPtr(py_address);
		Py_DECREF(key);
	}
	return address;
}
#endif

int InitExtension(const char* name, const char** procs)
{
	if (has_extension(name))
	{
		int success = 1;
		void *proc;
		PyObject *key;
#if HAS_DYNAMIC_EXT
		while (*procs)
		{
			key = Py_BuildValue("ls", GetCurrentContext(), *procs);
			if (PyDict_GetItem(ProcAddresses, key)) break;
			proc = (void*)GetExtProc(*procs);
			if (proc)
			{
				PyDict_SetItem(ProcAddresses, key, PyCObject_FromVoidPtr(proc, NULL));
			}
			Py_DECREF(key);
			procs++;
		}
#endif
		return success;
	}
	return 0;
}

static util_API _util_API;

PyObject *GLerror = NULL;
PyObject *GLUerror = NULL;

%}
#else
%{
static util_API *_util_API = NULL;

#define decrementLock(x) (*_util_API)._decrement(x)
#define decrementPointerLock(x) (*_util_API)._decrementPointer(x)
#define incrementLock(x) (*_util_API)._incrementLock(x)
#define incrementPointerLock(x) (*_util_API)._incrementPointerLock(x)
#define acquire(x) (*_util_API)._acquire(x)
#define acquirePointer(x) (*_util_API)._acquirePointer(x)
#define GLerror (*_util_API)._GLerror
#define GLUerror (*_util_API)._GLUerror
#if HAS_DYNAMIC_EXT
#define GL_GetProcAddress(x) (*_util_API).GL_GetProcAddress(x)
#endif
#define InitExtension(x, y) (*_util_API).InitExtension(x, (const char**)y)

%}
#endif

%{
#define PyErr_SetGLerror(code) PyErr_SetObject(GLerror, Py_BuildValue("is", code, gluErrorString(code)));
#define PyErr_SetGLUerror(code) PyErr_SetObject(GLUerror, Py_BuildValue("is", code, gluErrorString(code)));

int _PyObject_Dimension(PyObject* x, int rank);

#define ERROR_MSG_SEP ", "
#define ERROR_MSG_SEP_LEN 2

int GLErrOccurred()
{
	if (PyErr_Occurred()) return 1;

	if (CurrentContextIsValid())
	{
		GLenum error, *errors = NULL;
		char *msg = NULL;
		const char *this_msg;
		int count = 0;
	
		error = glGetError();

		while (error != GL_NO_ERROR)
		{
			this_msg = gluErrorString(error);
			if (count)
			{
				msg = realloc(msg, (strlen(msg) + strlen(this_msg) + ERROR_MSG_SEP_LEN + 1)*sizeof(char));
				strcat(msg, ERROR_MSG_SEP);
				strcat(msg, this_msg);
				
				errors = realloc(errors, (count + 1)*sizeof(GLenum));
			}
			else
			{
				msg = malloc((strlen(this_msg) + 1)*sizeof(char));
				strcpy(msg, this_msg);
				
				errors = malloc(sizeof(GLenum));
			}
			
			errors[count++] = error;
			error = glGetError();
		}
		
		if (count)
		{
			PyErr_SetObject(GLerror, Py_BuildValue("Os", _PyTuple_FromIntArray(count, (int*)errors), msg));
			free(errors);
			free(msg);
			return 1;
		}
	}

	return 0;
}

void PyErr_SetGLErrorMessage( int id, char * message ) {
	/* set a GLerror with an ID and string message
	
	This tries pretty hard to look just like a regular
	error as produced by GLErrOccurred()'s formatter,
	save that there's only the single error being reported.

	Using id 0 is probably best for any future use where 
	there isn't a good match for the exception description
	in the error-enumeration set.
	 */
	PyObject * args = NULL;
	args = Py_BuildValue( "(i)s", id, message );
	if (args) {
		PyErr_SetObject( GLerror, args );
		Py_XDECREF( args );
	} else {
		PyErr_SetGLerror(id);
	}
}


%}

#define EXCEPTION_HANDLER()\
%exception\
{\
	$function\
	if (PyErr_Occurred()) return NULL;\
}

#define GL_EXCEPTION_HANDLER()\
%exception\
{\
	$function\
	if (GLErrOccurred()) return NULL;\
}

%init
%{
#ifdef NUMERIC
	PyArray_API = NULL;
	import_array();
	init_util();
	PyErr_Clear();
#endif
%}

#ifdef EXPORT_UTIL
/*
*  Not sure that this prag-ma has any affect at all now...?
*/

%shadow %{
__numeric_present__ = _GL__init__.__numeric_present__
__numeric_support__ = _GL__init__.__numeric_support__
%}

%init
%{
	GLerror = PyErr_NewException("OpenGL.GL.GLerror", PyExc_EnvironmentError, NULL);
	GLUerror = PyErr_NewException("OpenGL.GLU.GLUerror", PyExc_EnvironmentError, NULL);
#if HAS_DYNAMIC_EXT
	ProcAddresses = PyDict_New();
	PyDict_SetItemString(d, "proc", ProcAddresses);
#endif
#ifndef GL_VERSION_1_1
	contexts = PyDict_New();
#endif
	_util_API._decrement = decrementLock;
	_util_API._decrementPointer = decrementPointerLock;
	_util_API._incrementLock = incrementLock;
	_util_API._incrementPointerLock = incrementPointerLock;
	_util_API._acquire = acquire;
	_util_API._acquirePointer = acquirePointer;
	_util_API.InitExtension = InitExtension;
#if HAS_DYNAMIC_EXT
	_util_API.GL_GetProcAddress = GL_GetProcAddress;
#endif
	_util_API._GLerror = GLerror;
	_util_API._GLUerror = GLUerror;
	PyDict_SetItemString(d, "_util_API", PyCObject_FromVoidPtr((void*)&_util_API, NULL));
#ifdef NUMERIC
	PyDict_SetItemString(d, "__numeric_support__", PyInt_FromLong(1));
	PyDict_SetItemString(d, "__numeric_present__", PyInt_FromLong((PyArray_API) ? 1 : 0));
#else
	PyDict_SetItemString(d, "__numeric_support__", PyInt_FromLong(0));
	PyDict_SetItemString(d, "__numeric_present__", PyInt_FromLong(0));
#endif
%}


#else
%init
%{
{
	PyObject *util = PyImport_ImportModule("OpenGL.GL._GL__init__");
	if (util)
	{
		PyObject *api_object = PyDict_GetItemString(PyModule_GetDict(util), "_util_API");
		if (PyCObject_Check(api_object)) _util_API = (util_API*)PyCObject_AsVoidPtr(api_object);
	}
}
%}
#endif

