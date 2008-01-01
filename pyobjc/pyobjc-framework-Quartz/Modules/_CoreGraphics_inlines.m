#include "Python.h"
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

void init_inlines(void)
{
    PyObject* m = Py_InitModule4("_inlines", mod_methods, NULL, NULL, PYTHON_API_VERSION);

    PyModule_AddObject(m, "_inline_list_", 
        PyCObject_FromVoidPtr(function_map, NULL));
}
