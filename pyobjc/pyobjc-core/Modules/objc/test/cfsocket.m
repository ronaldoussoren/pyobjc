/*
 * This module is used in the unittests for object identity.
 */
#include "Python.h"
#include "pyobjc-api.h"

#include <CoreFoundation/CoreFoundation.h>

@interface OC_TestCFSocket : NSObject
-(id)create;
@end

@implementation OC_TestCFSocket
-(id)create
{
	CFSocketRef sock;

	sock = CFSocketCreate(NULL, 0, 0, 0, 0, 0, 0);
	return (id)sock;
}
@end

static PyMethodDef cfsocket_methods[] = {
	{ 0, 0, 0, 0 }
};

void initcfsocket(void);
void initcfsocket(void)
{
	PyObject* m;

	m = Py_InitModule4("cfsocket", cfsocket_methods, 
			NULL, NULL, PYTHON_API_VERSION);

	PyObjC_ImportAPI(m);

	PyModule_AddObject(m, "OC_TestCFSocket", 
			PyObjCClass_New([OC_TestCFSocket class]));
}
