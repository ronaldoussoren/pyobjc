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
#include "_AppKitMapping_NSATSTypeSetter.m"
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
	if (_pyobjc_install_NSApplication() < 0) return;
	if (_pyobjc_install_NSATSTypesetter() < 0) return;
	if (_pyobjc_install_NSBezierPath() < 0) return;
	if (_pyobjc_install_NSBitmap() < 0) return;
	if (_pyobjc_install_NSBitmapImageRep() < 0) return;
	if (_pyobjc_install_NSFont() < 0) return;
	if (_pyobjc_install_NSLayoutManager() < 0) return;
	if (_pyobjc_install_NSMatrix() < 0) return;
	if (_pyobjc_install_NSMovie() < 0) return;
	if (_pyobjc_install_NSOpenGLContext() < 0) return;
	if (_pyobjc_install_NSOpenGLPixelFormat() < 0) return;
	if (_pyobjc_install_NSQuickDrawView() < 0) return;
	if (_pyobjc_install_NSSimpleHorizontalTypesetter() < 0) return;
	if (_pyobjc_install_NSView() < 0) return;
	if (_pyobjc_install_NSWindow() < 0) return;

}
