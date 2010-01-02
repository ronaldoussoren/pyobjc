/*
 * This module is used for tests dealing with FSRef "objects"
 */
#include "Python.h"
#include "pyobjc-api.h"

#import <CoreServices/CoreServices.h>

#import <Foundation/Foundation.h>

@interface OC_TestFSRefHelper : NSObject
{
}

-(FSRef)fsrefForPath:(NSString*)path;
-(NSString*)pathForFSRef:(in FSRef *)fsref;
-(void)getFSRef:(out FSRef*)fsref forPath:(NSString*)path;
-(NSString*)stringForFSRef:(FSRef)fsref;

@end

@implementation OC_TestFSRefHelper

-(NSString*)stringForFSRef:(FSRef)fsref
{
	return [self pathForFSRef:&fsref];
}

-(FSRef)fsrefForPath:(NSString*)path
{
	FSRef fsref;
	Boolean isDirectory;
	OSStatus rc;

	rc = FSPathMakeRef((UInt8*)[path UTF8String],
		&fsref, &isDirectory);
	if (rc != 0) {
		[NSException raise:@"failure" format:@"status: %d", rc];
	}

	return fsref;
}

-(NSString*)pathForFSRef:(in FSRef *)fsref
{
	UInt8 buffer[256];
	OSStatus rc;

	rc = FSRefMakePath(fsref, buffer, sizeof(buffer));
	if (rc != 0) {
		[NSException raise:@"failure" format:@"status: %d", rc];
	}

	return [NSString stringWithUTF8String: (char*)buffer];
}

-(void)getFSRef:(out FSRef*)fsref forPath:(NSString*)path
{
	Boolean isDirectory;
	OSStatus rc;

	rc = FSPathMakeRef((UInt8*)[path UTF8String],
		fsref, &isDirectory);
	if (rc != 0) {
		[NSException raise:@"failure" format:@"status: %d", rc];
	}
}

@end

static PyMethodDef mod_methods[] = {
	{ 0, 0, 0, 0 }
};

#if PY_VERSION_HEX >= 0x03000000

static struct PyModuleDef mod_module = {
	PyModuleDef_HEAD_INIT,
	"fsref",
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

PyObject* PyInit_fsref(void);

PyObject*
PyInit_fsref(void)

#else

#define INITERROR() return
#define INITDONE() return

void initfsref(void);

void
initfsref(void)
#endif
{
	PyObject* m;

#if PY_VERSION_HEX >= 0x03000000
	m = PyModule_Create(&mod_module);
#else
	m = Py_InitModule4("fsref", mod_methods,
		NULL, NULL, PYTHON_API_VERSION);
#endif
	if (!m) {
		INITERROR();
	}

	if (PyObjC_ImportAPI(m) < 0) {
		INITERROR();
	}

	if (PyModule_AddObject(m, "OC_TestFSRefHelper", 
			PyObjCClass_New([OC_TestFSRefHelper class])) < 0) {
		INITERROR();
	}

	INITDONE();
}
