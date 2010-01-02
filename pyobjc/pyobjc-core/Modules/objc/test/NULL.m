#include <Python.h>
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

@interface OCTestNULL : NSObject {}
-(int)callList:(NSMutableArray*)list andInOut:(int*)pval;
-(int)callList:(NSMutableArray*)list andInOut2:(int*)pval;
-(int)callList:(NSMutableArray*)list andIn:(int*)pval;
-(int)callList:(NSMutableArray*)list andOut:(int*)pval;
-(void)callOut:(int*)pval;
@end

@implementation OCTestNULL

-(int)callList:(NSMutableArray*)list andInOut:(int*)pval
{
	if (pval == NULL) {
		[list addObject: @"NULL"];
	} else {
		[list addObject: [NSString stringWithFormat:@"%d", *pval]];
		*pval = *pval / 2;
	}
	return 12;
}

/* This is the same implementation as callList:andInOut:, the python code
 * uses a different type string for this one.
 */
-(int)callList:(NSMutableArray*)list andInOut2:(int*)pval
{
	if (pval == NULL) {
		[list addObject: @"NULL"];
	} else {
		[list addObject: [NSString stringWithFormat:@"%d", *pval]];
		*pval = *pval / 2;
	}
	return 12;
}

-(int)callList:(NSMutableArray*)list andIn:(int*)pval
{
	if (pval == NULL) {
		[list addObject: @"NULL"];
	} else {
		[list addObject: [NSString stringWithFormat:@"%d", *pval]];
	}
	return 24;
}

-(int)callList:(NSMutableArray*)list andOut:(int*)pval
{
	if (pval == NULL) {
		[list addObject: @"NULL"];
	} else {
		[list addObject: @"POINTER"];
		*pval = 99;
	}

	return 24;
}

-(int)on:(OCTestNULL*)object callList:(NSMutableArray*)list andInOut:(int*)pval
{
	return [object callList:list andInOut:pval];
}

-(int)on:(OCTestNULL*)object callList:(NSMutableArray*)list andIn:(int*)pval
{
	return [object callList:list andIn:pval];
}

-(int)on:(OCTestNULL*)object callList:(NSMutableArray*)list andOut:(int*)pval
{
	return [object callList:list andOut:pval];
}

-(void)callOut:(int*)pval
{
	*pval = 144;
}

-(void)on:(OCTestNULL*)object callOut:(int*)pval
{
	[object callOut:pval];
}

@end


static PyMethodDef mod_methods[] = {
	        { 0, 0, 0, 0 }
};

#if PY_VERSION_HEX >= 0x03000000

static struct PyModuleDef mod_module = {
	PyModuleDef_HEAD_INIT,
	"NULL",
	NULL,
	0,
	mod_methods,
	NULL,
	NULL,
	NULL,
	NULL
};

#define INITERROR() return NULL
#define INITDONE()  return m

PyObject* PyInit_NULL(void);

PyObject*
PyInit_NULL(void)

#else

#define INITERROR() return
#define INITDONE()  return

void initNULL(void);

void
initNULL(void)
#endif
{
	PyObject* m;

#if PY_VERSION_HEX >= 0x03000000
	m = PyModule_Create(&mod_module);
#else
	m = Py_InitModule4("NULL", mod_methods,
		NULL, NULL, PYTHON_API_VERSION);
#endif
	if (!m) {
		INITERROR();
	}

	if (PyObjC_ImportAPI(m) < 0) {
		INITERROR();
	}

	if (PyModule_AddObject(m, "OCTestNULL",
	    PyObjCClass_New([OCTestNULL class])) < 0) {
		INITERROR();
	}

	INITDONE();
}
