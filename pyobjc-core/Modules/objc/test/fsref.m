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

static PyMethodDef methods[] = {
	{ 0, 0, 0, 0 }
};

void initfsref(void);
void initfsref(void)
{
	PyObject* m;

	m = Py_InitModule4("fsref", methods, 
			NULL, NULL, PYTHON_API_VERSION);

	PyObjC_ImportAPI(m);

	PyModule_AddObject(m, "OC_TestFSRefHelper", 
			PyObjCClass_New([OC_TestFSRefHelper class]));
}
