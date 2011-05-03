#include "Python.h"
#include "pyobjc-api.h"
#import <ScreenSaver/ScreenSaver.h>

static PyObjC_function_map function_map[] = {
	{"SSCenteredRectInRect", (PyObjC_Function_Pointer)&SSCenteredRectInRect },
	{"SSRandomFloatBetween", (PyObjC_Function_Pointer)&SSRandomFloatBetween },
	{"SSRandomIntBetween", (PyObjC_Function_Pointer)&SSRandomIntBetween },
	{"SSRandomPointForSizeWithinRect", (PyObjC_Function_Pointer)&SSRandomPointForSizeWithinRect },
    { 0, 0 }
};

static PyMethodDef mod_methods[] = {
        { 0, 0, 0, 0 } /* sentinel */
};

PyObjC_MODULE_INIT(_inlines)
{
	PyObject* m = PyObjC_MODULE_CREATE(_inlines);
	if (!m) {
		PyObjC_INITERROR();
	}

	if (PyModule_AddObject(m, "_inline_list_", 
		PyObjC_CreateInlineTab(function_map)) < 0) {
			PyObjC_INITERROR();
	}

	PyObjC_INITDONE();
}
