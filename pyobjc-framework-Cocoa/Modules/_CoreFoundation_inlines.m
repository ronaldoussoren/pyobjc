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
#if  PyObjC_BUILD_RELEASE >= 1006
	{"CFStringIsSurrogateHighCharacter", (FUNCTION)&CFStringIsSurrogateHighCharacter },
	{"CFStringIsSurrogateLowCharacter", (FUNCTION)&CFStringIsSurrogateLowCharacter },
	{"CFStringGetLongCharacterForSurrogatePair", (FUNCTION)&CFStringGetLongCharacterForSurrogatePair },
	{"CFStringGetSurrogatePairForLongCharacter", (FUNCTION)&CFStringGetSurrogatePairForLongCharacter },
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
		PyCObject_FromVoidPtr(function_map, NULL)) < 0) {
		INITERROR();
	}

	INITDONE();
}
