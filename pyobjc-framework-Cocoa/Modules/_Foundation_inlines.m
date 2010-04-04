#define NS_INLINE
#include "Python.h"
#include "pyobjc-api.h"
#import <Foundation/Foundation.h>

static PyObjC_function_map function_map[] = {
	{"NSConvertHostDoubleToSwapped", (PyObjC_Function_Pointer)&NSConvertHostDoubleToSwapped },
	{"NSConvertHostFloatToSwapped", (PyObjC_Function_Pointer)&NSConvertHostFloatToSwapped },
	{"NSConvertSwappedDoubleToHost", (PyObjC_Function_Pointer)&NSConvertSwappedDoubleToHost },
	{"NSConvertSwappedFloatToHost", (PyObjC_Function_Pointer)&NSConvertSwappedFloatToHost },
	{"NSDecimalIsNotANumber", (PyObjC_Function_Pointer)&NSDecimalIsNotANumber },
	{"NSEqualRanges", (PyObjC_Function_Pointer)&NSEqualRanges },
	{"NSHeight", (PyObjC_Function_Pointer)&NSHeight },
	{"NSHostByteOrder", (PyObjC_Function_Pointer)&NSHostByteOrder },
	{"NSLocationInRange", (PyObjC_Function_Pointer)&NSLocationInRange },
	{"NSMakePoint", (PyObjC_Function_Pointer)&NSMakePoint },
	{"NSMakeRange", (PyObjC_Function_Pointer)&NSMakeRange },
	{"NSMakeRect", (PyObjC_Function_Pointer)&NSMakeRect },
	{"NSMakeSize", (PyObjC_Function_Pointer)&NSMakeSize },
	{"NSMaxRange", (PyObjC_Function_Pointer)&NSMaxRange },
	{"NSMaxX", (PyObjC_Function_Pointer)&NSMaxX },
	{"NSMaxY", (PyObjC_Function_Pointer)&NSMaxY },
	{"NSMidX", (PyObjC_Function_Pointer)&NSMidX },
	{"NSMidY", (PyObjC_Function_Pointer)&NSMidY },
	{"NSMinX", (PyObjC_Function_Pointer)&NSMinX },
	{"NSMinY", (PyObjC_Function_Pointer)&NSMinY },
	{"NSSwapBigDoubleToHost", (PyObjC_Function_Pointer)&NSSwapBigDoubleToHost },
	{"NSSwapBigDoubleToHost", (PyObjC_Function_Pointer)&NSSwapBigDoubleToHost },
	{"NSSwapBigFloatToHost", (PyObjC_Function_Pointer)&NSSwapBigFloatToHost },
	{"NSSwapBigFloatToHost", (PyObjC_Function_Pointer)&NSSwapBigFloatToHost },
	{"NSSwapBigIntToHost", (PyObjC_Function_Pointer)&NSSwapBigIntToHost },
	{"NSSwapBigLongLongToHost", (PyObjC_Function_Pointer)&NSSwapBigLongLongToHost },
	{"NSSwapBigLongToHost", (PyObjC_Function_Pointer)&NSSwapBigLongToHost },
	{"NSSwapBigShortToHost", (PyObjC_Function_Pointer)&NSSwapBigShortToHost },
	{"NSSwapDouble", (PyObjC_Function_Pointer)&NSSwapDouble },
	{"NSSwapFloat", (PyObjC_Function_Pointer)&NSSwapFloat },
	{"NSSwapHostDoubleToBig", (PyObjC_Function_Pointer)&NSSwapHostDoubleToBig },
	{"NSSwapHostDoubleToBig", (PyObjC_Function_Pointer)&NSSwapHostDoubleToBig },
	{"NSSwapHostDoubleToLittle", (PyObjC_Function_Pointer)&NSSwapHostDoubleToLittle },
	{"NSSwapHostDoubleToLittle", (PyObjC_Function_Pointer)&NSSwapHostDoubleToLittle },
	{"NSSwapHostFloatToBig", (PyObjC_Function_Pointer)&NSSwapHostFloatToBig },
	{"NSSwapHostFloatToBig", (PyObjC_Function_Pointer)&NSSwapHostFloatToBig },
	{"NSSwapHostFloatToLittle", (PyObjC_Function_Pointer)&NSSwapHostFloatToLittle },
	{"NSSwapHostFloatToLittle", (PyObjC_Function_Pointer)&NSSwapHostFloatToLittle },
	{"NSSwapHostIntToBig", (PyObjC_Function_Pointer)&NSSwapHostIntToBig },
	{"NSSwapHostIntToLittle", (PyObjC_Function_Pointer)&NSSwapHostIntToLittle },
	{"NSSwapHostLongLongToBig", (PyObjC_Function_Pointer)&NSSwapHostLongLongToBig },
	{"NSSwapHostLongLongToLittle", (PyObjC_Function_Pointer)&NSSwapHostLongLongToLittle },
	{"NSSwapHostLongToBig", (PyObjC_Function_Pointer)&NSSwapHostLongToBig },
	{"NSSwapHostLongToLittle", (PyObjC_Function_Pointer)&NSSwapHostLongToLittle },
	{"NSSwapHostShortToBig", (PyObjC_Function_Pointer)&NSSwapHostShortToBig },
	{"NSSwapHostShortToLittle", (PyObjC_Function_Pointer)&NSSwapHostShortToLittle },
	{"NSSwapInt", (PyObjC_Function_Pointer)&NSSwapInt },
	{"NSSwapLittleDoubleToHost", (PyObjC_Function_Pointer)&NSSwapLittleDoubleToHost },
	{"NSSwapLittleDoubleToHost", (PyObjC_Function_Pointer)&NSSwapLittleDoubleToHost },
	{"NSSwapLittleFloatToHost", (PyObjC_Function_Pointer)&NSSwapLittleFloatToHost },
	{"NSSwapLittleFloatToHost", (PyObjC_Function_Pointer)&NSSwapLittleFloatToHost },
	{"NSSwapLittleIntToHost", (PyObjC_Function_Pointer)&NSSwapLittleIntToHost },
	{"NSSwapLittleLongLongToHost", (PyObjC_Function_Pointer)&NSSwapLittleLongLongToHost },
	{"NSSwapLittleLongToHost", (PyObjC_Function_Pointer)&NSSwapLittleLongToHost },
	{"NSSwapLittleShortToHost", (PyObjC_Function_Pointer)&NSSwapLittleShortToHost },
	{"NSSwapLong", (PyObjC_Function_Pointer)&NSSwapLong },
	{"NSSwapLongLong", (PyObjC_Function_Pointer)&NSSwapLongLong },
	{"NSSwapShort", (PyObjC_Function_Pointer)&NSSwapShort },
	{"NSWidth", (PyObjC_Function_Pointer)&NSWidth },

#ifndef NO_OBJC2_RUNTIME
	{"NSMakeCollectable", (PyObjC_Function_Pointer)&NSMakeCollectable },
	{"NSPointFromCGPoint", (PyObjC_Function_Pointer)&NSPointFromCGPoint },
	{"NSPointToCGPoint", (PyObjC_Function_Pointer)&NSPointToCGPoint },
	{"NSRectFromCGRect", (PyObjC_Function_Pointer)&NSRectFromCGRect },
	{"NSRectToCGRect", (PyObjC_Function_Pointer)&NSRectToCGRect },
	{"NSSizeFromCGSize", (PyObjC_Function_Pointer)&NSSizeFromCGSize },
	{"NSSizeToCGSize", (PyObjC_Function_Pointer)&NSSizeToCGSize },
#endif
	
    { 0, 0 }
};

static PyMethodDef mod_methods[] = {
        { 0, 0, 0, 0 } /* sentinel */
};

/* Python glue */
#if PY_VERSION_HEX >= 0x03000000

static struct PyModuleDef mod_module = {
        PyModuleDef_HEAD_INIT,
	"_inlines",
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

PyObject* PyInit__inlines(void);

PyObject*
PyInit__inlines(void)

#else

#define INITERROR() return
#define INITDONE() return

void init_inlines(void);

void
init_inlines(void)
#endif
{
	PyObject* m;
#if PY_VERSION_HEX >= 0x03000000
	m = PyModule_Create(&mod_module);
#else
	m = Py_InitModule4("_inlines", mod_methods,
		NULL, NULL, PYTHON_API_VERSION);
#endif


	if (PyModule_AddObject(m, "_inline_list_", 
		PyObjC_CreateInlineTab(function_map)) < 0)

		INITERROR();

	INITDONE();
}
