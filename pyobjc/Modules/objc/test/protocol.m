/*
 * This module is used in the unittests for object identity.
 */
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

@protocol OC_TestProtocol
-(int)method1;
-(void)method2:(int)v;
@end

static PyMethodDef protocol_methods[] = {
	{ 0, 0, 0, 0 }
};

void initprotocol(void);
void initprotocol(void)
{
	PyObject* m;
	Protocol* p;

	m = Py_InitModule4("protocol", protocol_methods, 
			NULL, NULL, PYTHON_API_VERSION);

	PyObjC_ImportAPI(m);

	p = @protocol(OC_TestProtocol);
	PyModule_AddObject(m, "OC_TestProtocol", PyObjC_ObjCToPython("@", &p));
}
