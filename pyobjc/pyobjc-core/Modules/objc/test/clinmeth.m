/*
 * Helper classes for test_clinmeth
 */
#include "Python.h"
#include "pyobjc-api.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

@interface PyObjC_ClsInst1 : NSObject
{
}
-(int)instance;
-(int)both;
+(int)both;
+(int)clsmeth;
@end

@implementation PyObjC_ClsInst1

-(int)instance
{
	return 1;
}

-(int)both
{
	return 2;
}

+(int)both
{
	return 3;
}

+(int)clsmeth
{
	return 4;
}
@end


@interface PyObjC_ClsInst2 : PyObjC_ClsInst1
{
}
-(int)instance;
-(int)both;
+(int)both;
+(int)clsmeth;
@end

@implementation PyObjC_ClsInst2

-(int)instance
{
	return 10;
}

-(int)both
{
	return 20;
}

+(int)both
{
	return 30;
}

+(int)clsmeth
{
	return 40;
}
@end



static PyMethodDef mod_methods[] = {
	        { 0, 0, 0, 0 }
};

#if PY_VERSION_HEX >= 0x03000000

static struct PyModuleDef mod_module = {
	PyModuleDef_HEAD_INIT,
	"clinmeth",
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

PyObject* PyInit_clinmeth(void);

PyObject*
PyInit_clinmeth(void)

#else

#define INITERROR() return
#define INITDONE() return

void initclinmeth(void);

void
initclinmeth(void)
#endif
{
	PyObject* m;

#if PY_VERSION_HEX >= 0x03000000
	m = PyModule_Create(&mod_module);
#else
	m = Py_InitModule4("clinmeth", mod_methods,
		NULL, NULL, PYTHON_API_VERSION);
#endif
	if (!m) {
		INITERROR();
	}

	if (PyObjC_ImportAPI(m) < 0) {
		INITERROR();
	}

	if (PyModule_AddObject(m, "PyObjC_ClsInst1", 
		PyObjCClass_New([PyObjC_ClsInst1 class])) < 0) {
		INITERROR();
	}
	if (PyModule_AddObject(m, "PyObjC_ClsInst2", 
		PyObjCClass_New([PyObjC_ClsInst2 class])) < 0) {
		INITERROR();
	}

	INITDONE();
}
