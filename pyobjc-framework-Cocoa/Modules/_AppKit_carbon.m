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

void init_carbon(void);
void init_carbon(void)
{
	PyObject* m = Py_InitModule4("_carbon", mod_methods, "", NULL,
                        PYTHON_API_VERSION);

	if (PyObjC_ImportAPI(m) < 0) return;

	if (PyObjCPointerWrapper_Register(@encode(WindowRef),
	                &window2py, &py2window) < 0)
		return;
}
