#define NS_INLINE
#include "Python.h"
#import <Foundation/Foundation.h>

typedef void (*FUNCTION)(void);

struct function_map {
    const char* name;
    FUNCTION    function;
} function_map[] = {
	{"NSConvertHostDoubleToSwapped", (FUNCTION)&NSConvertHostDoubleToSwapped },
	{"NSConvertHostFloatToSwapped", (FUNCTION)&NSConvertHostFloatToSwapped },
	{"NSConvertSwappedDoubleToHost", (FUNCTION)&NSConvertSwappedDoubleToHost },
	{"NSConvertSwappedFloatToHost", (FUNCTION)&NSConvertSwappedFloatToHost },
	{"NSDecimalIsNotANumber", (FUNCTION)&NSDecimalIsNotANumber },
	{"NSEqualRanges", (FUNCTION)&NSEqualRanges },
	{"NSHeight", (FUNCTION)&NSHeight },
	{"NSHostByteOrder", (FUNCTION)&NSHostByteOrder },
	{"NSLocationInRange", (FUNCTION)&NSLocationInRange },
	{"NSMakePoint", (FUNCTION)&NSMakePoint },
	{"NSMakeRange", (FUNCTION)&NSMakeRange },
	{"NSMakeRect", (FUNCTION)&NSMakeRect },
	{"NSMakeSize", (FUNCTION)&NSMakeSize },
	{"NSMaxRange", (FUNCTION)&NSMaxRange },
	{"NSMaxX", (FUNCTION)&NSMaxX },
	{"NSMaxY", (FUNCTION)&NSMaxY },
	{"NSMidX", (FUNCTION)&NSMidX },
	{"NSMidY", (FUNCTION)&NSMidY },
	{"NSMinX", (FUNCTION)&NSMinX },
	{"NSMinY", (FUNCTION)&NSMinY },
	{"NSSwapBigDoubleToHost", (FUNCTION)&NSSwapBigDoubleToHost },
	{"NSSwapBigDoubleToHost", (FUNCTION)&NSSwapBigDoubleToHost },
	{"NSSwapBigFloatToHost", (FUNCTION)&NSSwapBigFloatToHost },
	{"NSSwapBigFloatToHost", (FUNCTION)&NSSwapBigFloatToHost },
	{"NSSwapBigIntToHost", (FUNCTION)&NSSwapBigIntToHost },
	{"NSSwapBigLongLongToHost", (FUNCTION)&NSSwapBigLongLongToHost },
	{"NSSwapBigLongToHost", (FUNCTION)&NSSwapBigLongToHost },
	{"NSSwapBigShortToHost", (FUNCTION)&NSSwapBigShortToHost },
	{"NSSwapDouble", (FUNCTION)&NSSwapDouble },
	{"NSSwapFloat", (FUNCTION)&NSSwapFloat },
	{"NSSwapHostDoubleToBig", (FUNCTION)&NSSwapHostDoubleToBig },
	{"NSSwapHostDoubleToBig", (FUNCTION)&NSSwapHostDoubleToBig },
	{"NSSwapHostDoubleToLittle", (FUNCTION)&NSSwapHostDoubleToLittle },
	{"NSSwapHostDoubleToLittle", (FUNCTION)&NSSwapHostDoubleToLittle },
	{"NSSwapHostFloatToBig", (FUNCTION)&NSSwapHostFloatToBig },
	{"NSSwapHostFloatToBig", (FUNCTION)&NSSwapHostFloatToBig },
	{"NSSwapHostFloatToLittle", (FUNCTION)&NSSwapHostFloatToLittle },
	{"NSSwapHostFloatToLittle", (FUNCTION)&NSSwapHostFloatToLittle },
	{"NSSwapHostIntToBig", (FUNCTION)&NSSwapHostIntToBig },
	{"NSSwapHostIntToLittle", (FUNCTION)&NSSwapHostIntToLittle },
	{"NSSwapHostLongLongToBig", (FUNCTION)&NSSwapHostLongLongToBig },
	{"NSSwapHostLongLongToLittle", (FUNCTION)&NSSwapHostLongLongToLittle },
	{"NSSwapHostLongToBig", (FUNCTION)&NSSwapHostLongToBig },
	{"NSSwapHostLongToLittle", (FUNCTION)&NSSwapHostLongToLittle },
	{"NSSwapHostShortToBig", (FUNCTION)&NSSwapHostShortToBig },
	{"NSSwapHostShortToLittle", (FUNCTION)&NSSwapHostShortToLittle },
	{"NSSwapInt", (FUNCTION)&NSSwapInt },
	{"NSSwapLittleDoubleToHost", (FUNCTION)&NSSwapLittleDoubleToHost },
	{"NSSwapLittleDoubleToHost", (FUNCTION)&NSSwapLittleDoubleToHost },
	{"NSSwapLittleFloatToHost", (FUNCTION)&NSSwapLittleFloatToHost },
	{"NSSwapLittleFloatToHost", (FUNCTION)&NSSwapLittleFloatToHost },
	{"NSSwapLittleIntToHost", (FUNCTION)&NSSwapLittleIntToHost },
	{"NSSwapLittleLongLongToHost", (FUNCTION)&NSSwapLittleLongLongToHost },
	{"NSSwapLittleLongToHost", (FUNCTION)&NSSwapLittleLongToHost },
	{"NSSwapLittleShortToHost", (FUNCTION)&NSSwapLittleShortToHost },
	{"NSSwapLong", (FUNCTION)&NSSwapLong },
	{"NSSwapLongLong", (FUNCTION)&NSSwapLongLong },
	{"NSSwapShort", (FUNCTION)&NSSwapShort },
	{"NSWidth", (FUNCTION)&NSWidth },

#ifndef BUILD_TIGER
	{"NSMakeCollectable", (FUNCTION)&NSMakeCollectable },
	{"NSPointFromCGPoint", (FUNCTION)&NSPointFromCGPoint },
	{"NSPointToCGPoint", (FUNCTION)&NSPointToCGPoint },
	{"NSRectFromCGRect", (FUNCTION)&NSRectFromCGRect },
	{"NSRectToCGRect", (FUNCTION)&NSRectToCGRect },
	{"NSSizeFromCGSize", (FUNCTION)&NSSizeFromCGSize },
	{"NSSizeToCGSize", (FUNCTION)&NSSizeToCGSize },
#endif
	
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
