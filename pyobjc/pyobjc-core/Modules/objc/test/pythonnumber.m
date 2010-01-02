#include <Python.h>
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

@interface OC_TestNumber : NSObject {}
+(Class)numberClass:(NSNumber*)number;
+(BOOL)numberAsBOOL:(NSNumber*)number;
+(char)numberAsChar:(NSNumber*)number;
+(short)numberAsShort:(NSNumber*)number;
+(int)numberAsInt:(NSNumber*)number;
+(long)numberAsLong:(NSNumber*)number;
+(long long)numberAsLongLong:(NSNumber*)number;
+(unsigned char)numberAsUnsignedChar:(NSNumber*)number;
+(unsigned short)numberAsUnsignedShort:(NSNumber*)number;
+(unsigned int)numberAsUnsignedInt:(NSNumber*)number;
+(unsigned long)numberAsUnsignedLong:(NSNumber*)number;
+(unsigned long long)numberAsUnsignedLongLong:(NSNumber*)number;
+(NSDecimal)numberAsDecimal:(NSNumber*)number;
+(float)numberAsFloat:(NSNumber*)number;
+(double)numberAsDouble:(NSNumber*)number;

+(const char*)objCTypeOf:(NSNumber*)number;
+(int)compareA:(NSNumber*)a andB:(NSNumber*)b;
+(BOOL)number:(NSNumber*)a isEqualTo:(NSNumber*)b;
+(NSString*)numberDescription:(NSNumber*)number;
+(NSString*)numberDescription:(NSNumber*)number withLocale:(id)aLocale;
@end

@implementation OC_TestNumber

+(Class)numberClass:(NSNumber*)number
{
	return [number class];
}

+(const char*)objCTypeOf:(NSNumber*)number
{
	return [number objCType];
}

+(int)compareA:(NSNumber*)a andB:(NSNumber*)b
{
	return [a compare:b];
}

+(BOOL)number:(NSNumber*)a isEqualTo:(NSNumber*)b
{
	return [a isEqualToNumber:b];
}

+(NSString*)numberDescription:(NSNumber*)number
{
	return [number description];
}

+(NSString*)numberAsString:(NSNumber*)number
{
	return [number stringValue];
}

+(NSString*)numberDescription:(NSNumber*)number withLocale:(id)aLocale
{
	return [number descriptionWithLocale:aLocale];
}

+(BOOL)numberAsBOOL:(NSNumber*)number
{
	return [number boolValue];
}

+(char)numberAsChar:(NSNumber*)number
{
	return [number charValue];
}

+(short)numberAsShort:(NSNumber*)number
{
	return [number shortValue];
}

+(int)numberAsInt:(NSNumber*)number
{
	return [number intValue];
}

+(long)numberAsLong:(NSNumber*)number
{
	return [number longValue];
}

+(long long)numberAsLongLong:(NSNumber*)number
{
	return [number longLongValue];
}

+(unsigned char)numberAsUnsignedChar:(NSNumber*)number
{
	return [number unsignedCharValue];
}

+(unsigned short)numberAsUnsignedShort:(NSNumber*)number
{
	return [number unsignedShortValue];
}

+(unsigned int)numberAsUnsignedInt:(NSNumber*)number
{
	return [number unsignedIntValue];
}

+(unsigned long)numberAsUnsignedLong:(NSNumber*)number
{
	return [number unsignedLongValue];
}

+(unsigned long long)numberAsUnsignedLongLong:(NSNumber*)number
{
	return [number unsignedLongLongValue];
}

+(NSDecimal)numberAsDecimal:(NSNumber*)number
{
	return [number decimalValue];
}

+(float)numberAsFloat:(NSNumber*)number
{
	return [number floatValue];
}

+(double)numberAsDouble:(NSNumber*)number
{
	return [number doubleValue];
}


@end


static PyMethodDef mod_methods[] = {
	        { 0, 0, 0, 0 }
};

#if PY_VERSION_HEX >= 0x03000000

static struct PyModuleDef mod_module = {
	PyModuleDef_HEAD_INIT,
	"pythonnumber",
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

PyObject* PyInit_pythonnumber(void);

PyObject*
PyInit_pythonnumber(void)

#else

#define INITERROR() return
#define INITDONE() return

void initpythonnumber(void);

void
initpythonnumber(void)
#endif
{
	PyObject* m;

#if PY_VERSION_HEX >= 0x03000000
	m = PyModule_Create(&mod_module);
#else
	m = Py_InitModule4("pythonnumber", mod_methods,
		NULL, NULL, PYTHON_API_VERSION);
#endif
	if (!m) {
		INITERROR();
	}

	if (PyObjC_ImportAPI(m) < 0) {
		INITERROR();
	}

	if (PyModule_AddObject(m, "OC_TestNumber",
	    PyObjCClass_New([OC_TestNumber class])) < 0){
		INITERROR();
	}

	INITDONE();
}
