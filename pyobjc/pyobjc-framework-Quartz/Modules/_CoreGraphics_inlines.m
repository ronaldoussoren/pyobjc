#include "Python.h"
#include "pyobjc-api.h"
#import <ApplicationServices/ApplicationServices.h>

static PyObjC_function_map function_map[] = {
	{"CGPointMake", (PyObjC_Function_Pointer)&CGPointMake },
	{"CGRectMake", (PyObjC_Function_Pointer)&CGRectMake },
	{"CGSizeMake", (PyObjC_Function_Pointer)&CGSizeMake },
	{"__CGAffineTransformMake", (PyObjC_Function_Pointer)&__CGAffineTransformMake },
	{"__CGPointApplyAffineTransform", (PyObjC_Function_Pointer)&__CGPointApplyAffineTransform },
	{"__CGSizeApplyAffineTransform", (PyObjC_Function_Pointer)&__CGSizeApplyAffineTransform },
    { 0, 0 }
};

static PyMethodDef mod_methods[] = {
        { 0, 0, 0, 0 } /* sentinel */
};

PyObjC_MODULE_INIT(_inlines)
{
    PyObject* m = PyObjC_MODULE_CREATE(_inlines);
    if (!m) PyObjC_INITERROR();

    if (PyModule_AddObject(m, "_inline_list_", 
        PyObjC_CreateInlineTab(function_map)) < 0) PyObjC_INITERROR();

    PyObjC_INITDONE();
}
