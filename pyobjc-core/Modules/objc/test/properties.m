#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

typedef struct s {
    int  i;
    char b;
} struct_s;

typedef NSObject<NSObject> ObjectClass;

@interface OCPropertyDefinitions : NSObject {
    int      _prop1;
    float    _prop2;
    struct_s _prop3;
    id       _prop4;
    id       _prop5;
    id       _prop6;
    id       _prop7;
    id       _prop8;
    id       _prop9;
    struct_s _prop10;
    id       _prop11;
    id       _prop12;
}

#pragma clang diagnostic                            push
#pragma clang diagnostic                            ignored "-Wobjc-property-no-attribute"
@property int                                       prop1;
@property float                                     prop2;
@property struct_s                                  prop3;
@property id                                        prop4;
@property(readonly) id                              prop5;
@property(readwrite) id                             prop6;
@property(assign) id                                prop7;
@property(retain) id                                prop8;
@property(copy) id                                  prop9;
@property(nonatomic) struct_s                       prop10;
@property(getter=propGetter, setter=propSetter:) id prop11;
@property(nonatomic, readwrite, retain) id          prop12;
@property(readwrite, copy) id                       prop13;
@property(weak, readonly) ObjectClass*              parent;

#pragma clang diagnostic pop

@end

@implementation OCPropertyDefinitions

@synthesize prop1  = _prop1;
@synthesize prop2  = _prop2;
@synthesize prop3  = _prop3;
@synthesize prop4  = _prop4;
@synthesize prop5  = _prop5;
@synthesize prop6  = _prop6;
@synthesize prop7  = _prop7;
@synthesize prop8  = _prop8;
@synthesize prop9  = _prop9;
@synthesize prop10 = _prop10;
@synthesize prop11 = _prop11;
@synthesize prop12 = _prop12;
@dynamic    prop13;

- (ObjectClass*)parent
{
    return [NSArray array];
}

- (void)dealloc
{
    [self->_prop8 release];
    [self->_prop9 release];
    [self->_prop12 release];

    [super dealloc];
}

@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static int mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0) {
        return -1;
    }

    if (PyModule_AddObject(m, "OCPropertyDefinitions",
                           PyObjC_IdToPython([OCPropertyDefinitions class]))
        < 0) {
        return -1;
    }
    return 0;
}

static struct PyModuleDef_Slot mod_slots[] = {
    {
        .slot = Py_mod_exec,
        .value = (void*)mod_exec_module
    },
#if PY_VERSION_HEX >= 0x030c0000
    {
        /* This extension does not use the CPython API other than initializing
         * the module, hence is safe with subinterpreters and per-interpreter
         * GILs
         */
        .slot = Py_mod_multiple_interpreters,
        .value = Py_MOD_PER_INTERPRETER_GIL_SUPPORTED,
    },
#endif
#if PY_VERSION_HEX >= 0x030d0000
    {
        .slot = Py_mod_gil,
        .value = Py_MOD_GIL_NOT_USED,
    },
#endif
    {  /* Sentinel */
        .slot = 0,
        .value = 0
    }
};

static struct PyModuleDef mod_module = {
    .m_base = PyModuleDef_HEAD_INIT,
    .m_name = "properties",
    .m_doc = NULL,
    .m_size = 0,
    .m_methods = mod_methods,
    .m_slots = mod_slots,
    .m_traverse = NULL,
    .m_clear = NULL,
    .m_free = NULL,
};

PyObject* PyInit_properties(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_properties(void)
{
    return PyModuleDef_Init(&mod_module);
}
