/*
 */
#include "Python.h"
#include "pyobjc-api.h"

#import <Cocoa/Cocoa.h>

@interface StructArgClass : NSObject 
{
}
-(NSString*)compP:(NSPoint)aPoint aRect:(NSRect)aRect anOp:(int)op;
-(size_t)stackPtr;
-(NSRect)someRect;
-(NSRect)someRectWithRect:(NSRect)rect;
-(NSRect)someRectWithX:(int)x Y:(int)y H:(int)h W:(int)w;
-(NSRect)someRectWithObject:(StructArgClass*)o X:(int)x Y:(int)y H:(int)h W:(int)w;
@end

@implementation StructArgClass
-(NSRect)someRectWithRect:(NSRect)rect
{
	return rect;
}

-(NSRect)someRectWithX:(int)x Y:(int)y H:(int)h W:(int)w
{
	return NSMakeRect(x, y, h, w);
}

-(NSRect)someRectWithObject:(StructArgClass*)o X:(int)x Y:(int)y H:(int)h W:(int)w
{
	return [o someRectWithRect:NSMakeRect(x, y, h, w)];
}

-(NSRect)someRect
{
	NSRect retval = NSMakeRect(1,2,3,4);
	return retval;
}


-(NSString*)compP:(NSPoint)aPoint aRect:(NSRect)aRect anOp:(int)op
{
	return [NSString stringWithFormat:@"aP:%@ aR:%@ anO:%d",
			NSStringFromPoint(aPoint),
			NSStringFromRect(aRect),
			op];
}

static size_t ident(size_t v)
{
	return v;
}
-(size_t)stackPtr
{
	char c;

	return ident(((size_t)&c)+1);
}
@end

static PyMethodDef mod_methods[] = {
	                { 0, 0, 0, 0 }
};

#if PY_VERSION_HEX >= 0x03000000

static struct PyModuleDef mod_module = {
	PyModuleDef_HEAD_INIT,
	"structargs",
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

PyObject* PyInit_structargs(void);

PyObject*
PyInit_structargs(void)

#else

#define INITERROR() return
#define INITDONE() return

void initstructargs(void);

void
initstructargs(void)
#endif
{
	PyObject* m;

#if PY_VERSION_HEX >= 0x03000000
	m = PyModule_Create(&mod_module);
#else
	m = Py_InitModule4("structargs", mod_methods,
		NULL, NULL, PYTHON_API_VERSION);
#endif
	if (!m) {
		INITERROR();
	}

	if (PyObjC_ImportAPI(m) < 0) {
		INITERROR();
	}

	if (PyModule_AddObject(m, "StructArgClass",
		PyObjCClass_New([StructArgClass class])) < 0) {
		INITERROR();
	}

	INITDONE();
}



