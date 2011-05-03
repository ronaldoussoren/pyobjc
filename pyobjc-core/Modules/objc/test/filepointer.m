/*
 * This module is used in the unittests for object identity.
 */
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

@interface OC_TestFilePointer : NSObject
{
}

-(FILE*)openFile:(char*)path withMode:(char*)mode;
-(NSString*)readline:(FILE*)fp;
@end

@implementation OC_TestFilePointer
-(FILE*)openFile:(char*)path withMode:(char*)mode
{
	return fopen(path, mode);
}

-(NSString*)readline:(FILE*)fp
{
	char buf[1024];

	return [NSString stringWithCString: fgets(buf, sizeof(buf), fp)
		         encoding:NSASCIIStringEncoding];
}
@end

static PyMethodDef mod_methods[] = {
	{ 0, 0, 0, 0 }
};

#if PY_VERSION_HEX >= 0x03000000

static struct PyModuleDef mod_module = {
	PyModuleDef_HEAD_INIT,
	"filepointer",
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

PyObject* PyInit_filepointer(void);

PyObject*
PyInit_filepointer(void)

#else

#define INITERROR() return
#define INITDONE() return

void initfilepointer(void);

void
initfilepointer(void)
#endif
{
	PyObject* m;

#if PY_VERSION_HEX >= 0x03000000
	m = PyModule_Create(&mod_module);
#else
	m = Py_InitModule4("filepointer", mod_methods,
		NULL, NULL, PYTHON_API_VERSION);
#endif
	if (!m) {
		INITERROR();
	}

	if (PyObjC_ImportAPI(m) < 0) {
		INITERROR();
	}

	if (PyModule_AddObject(m, "OC_TestFilePointer", 
			PyObjCClass_New([OC_TestFilePointer class])) < 0) {
		INITERROR();
	}

	INITDONE();
}
