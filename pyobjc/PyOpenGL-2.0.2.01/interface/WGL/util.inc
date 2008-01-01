%include util.inc

#define CONST const
typedef long HDC;
typedef long HGLRC;
typedef unsigned int UINT;
typedef long HENHMETAFILE;
typedef void VOID;
typedef unsigned int DWORD;
typedef unsigned short WORD;
typedef float FLOAT;
typedef double DOUBLE;
typedef int BOOL;
typedef unsigned char BYTE;
typedef DWORD COLORREF;
typedef const char *LPCSTR;
typedef long PROC;

%{
#if PY_MAJOR_VERSION < 2
#define PyExc_WindowsError PyExc_OSError
#endif

int WGLErrOccurred()
{
	DWORD error = GetLastError();
	if (error != ERROR_SUCCESS)
	{
		LPSTR buffer;
		FormatMessageA(FORMAT_MESSAGE_FROM_SYSTEM | FORMAT_MESSAGE_ALLOCATE_BUFFER, NULL, error, 0, (LPSTR)&buffer, 0, NULL);
		PyErr_SetObject(PyExc_WindowsError, Py_BuildValue("is", error, buffer));
		LocalFree(buffer);
		return 1;
	}

	return 0;
}
%}


#define WGL_EXCEPTION_HANDLER()\
%except\
{\
	SetLastError(0);\
	$function\
	if (WGLErrOccurred()) return NULL;\
}

/* Appears that newer versions of swig don't include recursively */
#define DOC(NAME, VALUE)\
%{\
static char _doc_##NAME[] = VALUE;\
%}

