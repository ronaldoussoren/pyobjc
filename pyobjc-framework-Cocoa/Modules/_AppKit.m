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


static PyMethodDef mod_methods[] = {
	APPKIT_APPMAIN_METHODS
	APPKIT_NSFONT_METHODS
	{ 0, 0, 0, 0 } /* sentinel */
};


/* Python glue */
#if PY_VERSION_HEX >= 0x03000000

static struct PyModuleDef mod_module = {
        PyModuleDef_HEAD_INIT,
	"_AppKit",
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

PyObject* PyInit__AppKit(void);

PyObject*
PyInit__AppKit(void)

#else

#define INITERROR() return
#define INITDONE() return

void init_AppKit(void);

void
init_AppKit(void)
#endif
{
	PyObject* m;
#if PY_VERSION_HEX >= 0x03000000
	m = PyModule_Create(&mod_module);
#else
	m = Py_InitModule4("_AppKit", mod_methods,
		NULL, NULL, PYTHON_API_VERSION);
#endif
	if (!m) { 
		INITERROR();
	}

	if (PyObjC_ImportAPI(m) == -1) INITERROR();

	if (setup_carbon(m) == -1) INITERROR();
	if (setup_nsbezierpath(m) == -1) INITERROR();
	if (setup_nsbitmap(m) == -1) INITERROR();
	if (setup_nsquickdrawview(m) == -1) INITERROR();
	if (setup_nsview(m) == -1) INITERROR();
	if (setup_nswindows(m) == -1) INITERROR();

	INITDONE();
}
