/*
 * Workaround to make NSAppicationMain more usable from Python.
 */
#include <Python.h>
#include "pyobjc-api.h"

#import <AppKit/AppKit.h>

static PyObject* 
objc_NSApplicationMain(
	PyObject* self __attribute__((__unused__)), 
	PyObject* args, 
	PyObject* kwds)
{
static	char* keywords[] = { "argv", NULL };
	char** argv = NULL;
	int    argc;
	PyObject* arglist;
	int       i;
	PyObject* v;
	int       res;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "O:NSApplicationMain",
			keywords, &arglist)) {
		return NULL;
	}

	if (!PySequence_Check(arglist)) {
		PyErr_SetString(PyExc_TypeError, 
			"NSApplicationMain: need list of strings as argument");
		return NULL;
	}

	argc = PySequence_Size(arglist);
	argv = calloc((argc + 1), sizeof(char**));
	if (argv == NULL) {
		PyErr_SetString(PyExc_MemoryError,
			"Out of memory");
		return NULL;
	}

	for  (i = 0; i < argc; i++) {
		v = PySequence_GetItem(arglist, i);
		if (v == NULL) {
			goto error_cleanup;
		}
		if (!PyString_Check(v)) {
			PyErr_SetString(PyExc_TypeError, 
				"NSApplicationMain: need list of strings "
				"as argument");
			goto error_cleanup;
		}

		argv[i] = strdup(PyString_AsString(v));
		if (argv[i] == NULL) {
			PyErr_SetString(PyExc_MemoryError,
				"Out of memory");
			goto error_cleanup;
		}
	}

	argv[argc] = NULL;

#if 0
	/*
	 * NSApplicationMain on MacOS X completely ignores its arguments and 
	 * reads the argv from the shared NSProcessInfo. We *HACK* around this 
	 * by setting a (private) instance variable of the object.
	 *
	 * This code is evil. Look away if you're easily scared.
	 *
	 * This doesn't work in 64-bit mode however. Therefore this code
	 * is now disabled. This shouldn't make a difference when using
	 * py2app or Xcode's PyObjC templates.
	 */
	{
		typedef struct {
			@defs(NSProcessInfo)
		} NSProcessInfoStruct;
	  
		NSMutableArray *newarglist = [[NSMutableArray alloc] init];
		NSProcessInfo *processInfo = [NSProcessInfo processInfo];
		char **anArg = argv;

		while(*anArg) {
			[newarglist addObject: 
				[NSString stringWithUTF8String: *anArg]];
			anArg++;
		}

		/* Don't release the orignal arguments, because we don't know
		 * if the list is owned by the processInfo object.
		 *
		 *[((NSProcessInfoStruct *)processInfo)->arguments release]; 
		 */
		((NSProcessInfoStruct *)processInfo)->arguments = newarglist;
	}
#endif

	PyObjC_DURING
		res = NSApplicationMain(argc, (const char**)argv);
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		res = -1;
	PyObjC_ENDHANDLER

	for (i = 0; i < argc; i++) {
		free(argv[i]);
	}
	free(argv);

	if (res == -1 && PyErr_Occurred())
		return NULL;
	return PyInt_FromLong(res);

error_cleanup:
	if (argv != NULL) {
		for (i = 0; i < argc; i++) {
			if (argv[i] != NULL) {
				free(argv[i]);
				argv[i] = NULL;
			}
		}
		free(argv);
		argv = NULL;
	}

	return NULL;
}


static PyMethodDef mod_methods[] = {
	{ 
		"NSApplicationMain", 
		(PyCFunction)objc_NSApplicationMain, 
		METH_VARARGS|METH_KEYWORDS, 
		"int NSApplicationMain(int argc, const char *argv[]);"
	},
	{ 0, 0, 0, 0 } /* sentinel */
};

void init_appmain(void);
void init_appmain(void)
{
	PyObject* m = Py_InitModule4("_appmain", mod_methods, "", NULL,
			PYTHON_API_VERSION);

	PyObjC_ImportAPI(m);
}
