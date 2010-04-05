#include "Python.h"
#include "pyobjc-api.h"
#import <ApplicationServices/ApplicationServices.h>

typedef void (*FUNCTION)(void);

struct function_map {
    const char* name;
    FUNCTION    function;
} function_map[] = {
	{"CGPointMake", (FUNCTION)&CGPointMake },
	{"CGRectMake", (FUNCTION)&CGRectMake },
	{"CGSizeMake", (FUNCTION)&CGSizeMake },
	{"__CGAffineTransformMake", (FUNCTION)&__CGAffineTransformMake },
	{"__CGPointApplyAffineTransform", (FUNCTION)&__CGPointApplyAffineTransform },
	{"__CGSizeApplyAffineTransform", (FUNCTION)&__CGSizeApplyAffineTransform },
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
