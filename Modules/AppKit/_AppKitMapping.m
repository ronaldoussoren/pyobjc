/*
 * This module contains custom mapping functions for problematic methods
 */

#include <Python.h>
#include <Foundation/Foundation.h>
#include <AppKit/AppKit.h> // really should be Cocoa
#include "pyobjc-api.h"



PyDoc_STRVAR(mapping_doc,
	"This module registers some utility functions with the PyObjC core \n"
	"and is not used by 'normal' python code"
);

static PyMethodDef mapping_methods[] = {
	{ 0, 0, 0, 0 }
};


void init_AppKitMapping(void);

#include "_AppKitMapping_NSApplication.m"
#include "_AppKitMapping_NSBezierPath.m"
#include "_AppKitMapping_NSBitmap.m"
#include "_AppKitMapping_NSBitmapImageRep.m"
#include "_AppKitMapping_NSFont.m"
#include "_AppKitMapping_NSMatrix.m"
#include "_AppKitMapping_NSLayoutManager.m"
#include "_AppKitMapping_NSMovie.m"
#include "_AppKitMapping_NSOpenGLContext.m"
#include "_AppKitMapping_NSOpenGLPixelFormat.m"
#include "_AppKitMapping_NSQuickDrawView.m"
#include "_AppKitMapping_NSSimpleHorizontalTypesetter.m"
#include "_AppKitMapping_NSView.m"
#include "_AppKitMapping_NSWindow.m"

void init_AppKitMapping(void)
{
	PyObject *m, *d;

	m = Py_InitModule4("_AppKitMapping", mapping_methods, mapping_doc, 
		NULL, PYTHON_API_VERSION);
	if (!m) return;

	d = PyModule_GetDict(m);
	if (!d) return;
	

	if (PyObjC_ImportAPI(m) < 0) {
		return;
	}


	/* register other specials */
	_pyobjc_install_NSApplication();
	_pyobjc_install_NSBezierPath();
	_pyobjc_install_NSBitmap();
	_pyobjc_install_NSBitmapImageRep();
	_pyobjc_install_NSFont();
	_pyobjc_install_NSLayoutManager();
	_pyobjc_install_NSMatrix();
	_pyobjc_install_NSMovie();
	_pyobjc_install_NSOpenGLContext();
	_pyobjc_install_NSOpenGLPixelFormat();
	_pyobjc_install_NSQuickDrawView();
	_pyobjc_install_NSSimpleHorizontalTypesetter();
	_pyobjc_install_NSView();
	_pyobjc_install_NSWindow();

}
