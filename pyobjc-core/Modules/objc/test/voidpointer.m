/*
 * This module is used in the unittests for object identity.
 */
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

@interface OC_TestVoidPointer : NSObject
{
	void* value;
}

-(void*)getvalue;
-(void)setvalue:(void*)v;
@end

@implementation OC_TestVoidPointer
-init 
{
	self = [super init];
	if (self) {
		value = NULL;
	}
	return self;
}
-(void*)getvalue
{
	return value;
}
-(void)setvalue:(void*)v
{
	value = v;
}
@end

static PyMethodDef mod_methods[] = {
	{ 0, 0, 0, 0 }
};

#if PY_VERSION_HEX >= 0x03000000

static struct PyModuleDef mod_module = {
	PyModuleDef_HEAD_INIT,
	"voidpointer",
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

PyObject* PyInit_voidpointer(void);

PyObject*
PyInit_voidpointer(void)

#else

#define INITERROR() return
#define INITDONE() return

void initvoidpointer(void);

void
initvoidpointer(void)
#endif
{
	PyObject* m;


#if PY_VERSION_HEX >= 0x03000000
	m = PyModule_Create(&mod_module);
#else
	m = Py_InitModule4("voidpointer", mod_methods,
		NULL, NULL, PYTHON_API_VERSION);
#endif
	if (!m) {
		INITERROR();
	}
	if (PyObjC_ImportAPI(m) < 0) {
		INITERROR();
	}

	if (PyModule_AddObject(m, "OC_TestVoidPointer", 
			PyObjCClass_New([OC_TestVoidPointer class])) < 0){
		INITERROR();
	}

	INITDONE();
}
