/*
 * Support code for dealing with Carbon types (at least those
 * used in AppKit and wrapped in the python core).
 */
#include <Python.h>
#include "pyobjc-api.h"

#import <AppKit/AppKit.h>
#import <Carbon/Carbon.h>

#ifndef __LP64__

#include "pymactoolbox.h"

#else
	/* FIXME: the bits of pymactoolbox.h that we need,
	 * because said header doesn't work in 64-bit mode
	 */
extern PyObject *WinObj_New(WindowPtr);
extern int WinObj_Convert(PyObject *, WindowPtr *);
extern PyObject *WinObj_WhichWindow(WindowPtr);


#endif

static int
py2window(PyObject* obj, void* output)
{
	return WinObj_Convert(obj, (WindowPtr*)output);
}

static PyObject*
window2py(void* value)
{
	return WinObj_New((WindowPtr)value);
}


static PyMethodDef mod_methods[] = {
        { 0, 0, 0, 0 } /* sentinel */
};


/* Python glue */
#if PY_VERSION_HEX >= 0x03000000

static struct PyModuleDef mod_module = {
        PyModuleDef_HEAD_INIT,
	"_carbon",
	NULL,
	0,
	mod_methods,
	NULL,
	NULL,
	NULL,
	NULL
};

#define INITERROR() return NULL
#define INITDONE() return m

PyObject* PyInit__carbon(void);

PyObject*
PyInit__carbon(void)

#else

#define INITERROR() return
#define INITDONE() return

void init_carbon(void);

void
init_carbon(void)
#endif
{
	PyObject* m;
#if PY_VERSION_HEX >= 0x03000000
	m = PyModule_Create(&mod_module);
#else
	m = Py_InitModule4("_carbon", mod_methods,
		NULL, NULL, PYTHON_API_VERSION);
#endif
	if (!m) { 
		INITERROR();
	}

	if (PyObjC_ImportAPI(m) == -1) INITERROR();

	if (PyObjCPointerWrapper_Register(@encode(WindowRef),
	                &window2py, &py2window) < 0)
		INITERROR();

	INITDONE();
}
