#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "pyobjc-api.h"

#import <AppKit/AppKit.h>

/* We include the source code here instead of 
 * using the linker due to limitations in pyobjc-api.h
 */
#include "_AppKit_appmain.m"
#include "_AppKit_carbon.m"
#include "_AppKit_nsbezierpath.m"
#include "_AppKit_nsbitmap.m"
#include "_AppKit_nsfont.m"
#include "_AppKit_nsquickdrawview.m"
#include "_AppKit_nsview.m"
#include "_AppKit_nswindow.m"
#include "_AppKit_protocols.m"


static PyMethodDef mod_methods[] = {
	APPKIT_APPMAIN_METHODS
	APPKIT_NSFONT_METHODS
	{ 0, 0, 0, 0 } /* sentinel */
};


/* Python glue */
PyObjC_MODULE_INIT(_AppKit)
{
	PyObject* m;
	m = PyObjC_MODULE_CREATE(_AppKit)
	if (!m) { 
		PyObjC_INITERROR();
	}

	if (PyObjC_ImportAPI(m) == -1) PyObjC_INITERROR();

	if (setup_carbon(m) == -1) PyObjC_INITERROR();
	if (setup_nsbezierpath(m) == -1) PyObjC_INITERROR();
	if (setup_nsbitmap(m) == -1) PyObjC_INITERROR();
	if (setup_nsquickdrawview(m) == -1) PyObjC_INITERROR();
	if (setup_nsview(m) == -1) PyObjC_INITERROR();
	if (setup_nswindows(m) == -1) PyObjC_INITERROR();

	PyObjC_INITDONE();
}
