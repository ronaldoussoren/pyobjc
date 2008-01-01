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

static PyMethodDef filepointer_methods[] = {
	{ 0, 0, 0, 0 }
};

void initfilepointer(void);
void initfilepointer(void)
{
	PyObject* m;

	m = Py_InitModule4("filepointer", filepointer_methods, 
			NULL, NULL, PYTHON_API_VERSION);

	PyObjC_ImportAPI(m);

	PyModule_AddObject(m, "OC_TestFilePointer", 
			PyObjCClass_New([OC_TestFilePointer class]));
}
