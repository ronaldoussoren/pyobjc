#define CF_INLINE
#include "Python.h"
#import <CoreFoundation/CoreFoundation.h>


typedef void (*FUNCTION)(void);

struct function_map {
    const char* name;
    FUNCTION    function;
} function_map[] = {
	{"CFByteOrderGetCurrent", (FUNCTION)&CFByteOrderGetCurrent },
	{"CFConvertDoubleHostToSwapped", (FUNCTION)&CFConvertDoubleHostToSwapped },
	{"CFConvertDoubleSwappedToHost", (FUNCTION)&CFConvertDoubleSwappedToHost },
	{"CFConvertFloat32HostToSwapped", (FUNCTION)&CFConvertFloat32HostToSwapped },
	{"CFConvertFloat32SwappedToHost", (FUNCTION)&CFConvertFloat32SwappedToHost },
	{"CFConvertFloat64HostToSwapped", (FUNCTION)&CFConvertFloat64HostToSwapped },
	{"CFConvertFloat64SwappedToHost", (FUNCTION)&CFConvertFloat64SwappedToHost },
	{"CFConvertFloatHostToSwapped", (FUNCTION)&CFConvertFloatHostToSwapped },
	{"CFConvertFloatSwappedToHost", (FUNCTION)&CFConvertFloatSwappedToHost },
	{"CFRangeMake", (FUNCTION)&CFRangeMake },
	{"CFStringGetCharacterFromInlineBuffer", (FUNCTION)&CFStringGetCharacterFromInlineBuffer },
	{"CFStringInitInlineBuffer", (FUNCTION)&CFStringInitInlineBuffer },
	{"CFSwapInt16", (FUNCTION)&CFSwapInt16 },
	{"CFSwapInt16BigToHost", (FUNCTION)&CFSwapInt16BigToHost },
	{"CFSwapInt16HostToBig", (FUNCTION)&CFSwapInt16HostToBig },
	{"CFSwapInt16HostToLittle", (FUNCTION)&CFSwapInt16HostToLittle },
	{"CFSwapInt16LittleToHost", (FUNCTION)&CFSwapInt16LittleToHost },
	{"CFSwapInt32", (FUNCTION)&CFSwapInt32 },
	{"CFSwapInt32BigToHost", (FUNCTION)&CFSwapInt32BigToHost },
	{"CFSwapInt32HostToBig", (FUNCTION)&CFSwapInt32HostToBig },
	{"CFSwapInt32HostToLittle", (FUNCTION)&CFSwapInt32HostToLittle },
	{"CFSwapInt32LittleToHost", (FUNCTION)&CFSwapInt32LittleToHost },
	{"CFSwapInt64", (FUNCTION)&CFSwapInt64 },
	{"CFSwapInt64BigToHost", (FUNCTION)&CFSwapInt64BigToHost },
	{"CFSwapInt64HostToBig", (FUNCTION)&CFSwapInt64HostToBig },
	{"CFSwapInt64HostToLittle", (FUNCTION)&CFSwapInt64HostToLittle },
	{"CFSwapInt64LittleToHost", (FUNCTION)&CFSwapInt64LittleToHost },
	{"CFUserNotificationCheckBoxChecked", (FUNCTION)&CFUserNotificationCheckBoxChecked },
	{"CFUserNotificationPopUpSelection", (FUNCTION)&CFUserNotificationPopUpSelection },
	{"CFUserNotificationSecureTextField", (FUNCTION)&CFUserNotificationSecureTextField },
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
