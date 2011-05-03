#include <Python.h>
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

typedef struct s { int i; char b; } struct_s;
@interface OCPropertyDefinitions : NSObject {
	int _prop1;
	float _prop2;
	struct_s _prop3;
	id	_prop4;
	id	_prop5;
	id	_prop6;
	id	_prop7;
	id	_prop8;
	id	_prop9;
	struct_s _prop10;
	id	_prop11;
	id	_prop12;
}

#if (PyObjC_BUILD_RELEASE >= 1005) 

@property int prop1;
@property float prop2;
@property struct_s prop3;
@property id prop4;
@property(readonly) id prop5;
@property(readwrite) id prop6;
@property(assign) id prop7;
@property(retain) id prop8;
@property(copy) id prop9;
@property(nonatomic) struct_s prop10;
@property(getter=propGetter,setter=propSetter:) id prop11;
@property(nonatomic,readwrite,retain) id prop12;
@property(readwrite,copy) id prop13;

#endif

@end

@implementation OCPropertyDefinitions

#if (PyObjC_BUILD_RELEASE >= 1005 )

@synthesize prop1 = _prop1;
@synthesize prop2 = _prop2;
@synthesize prop3 = _prop3;
@synthesize prop4 = _prop4;
@synthesize prop5 = _prop5;
@synthesize prop6 = _prop6;
@synthesize prop7 = _prop7;
@synthesize prop8 = _prop8;
@synthesize prop9 = _prop9;
@synthesize prop10 = _prop10;
@synthesize prop11 = _prop11;
@synthesize prop12 = _prop12;
@dynamic prop13;

#endif

@end


static PyMethodDef mod_methods[] = {
	        { 0, 0, 0, 0 }
};

#if PY_VERSION_HEX >= 0x03000000

static struct PyModuleDef mod_module = {
	PyModuleDef_HEAD_INIT,
	"properties",
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

PyObject* PyInit_properties(void);

PyObject*
PyInit_properties(void)

#else

#define INITERROR() return
#define INITDONE() return

void initproperties(void);

void
initproperties(void)
#endif
{
	PyObject* m;

#if PY_VERSION_HEX >= 0x03000000
	m = PyModule_Create(&mod_module);
#else
	m = Py_InitModule4("properties", mod_methods,
		NULL, NULL, PYTHON_API_VERSION);
#endif
	if (!m) {
		INITERROR();
	}

	if (PyObjC_ImportAPI(m) < 0) {
		INITERROR();
	}

	if (PyModule_AddObject(m, "OCPropertyDefinitions",
	    PyObjCClass_New([OCPropertyDefinitions class])) < 0) {
		INITERROR();
	}

	INITDONE();
}
