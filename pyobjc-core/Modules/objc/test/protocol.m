/*
 * This module is used in the unittests for object identity.
 */
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

@protocol OC_NSObjectBased <NSObject>
@optional
- (int)optionalmethod;
@end

@protocol OC_TestProtocol
- (int)method1;
- (void)method2:(int)v;
@end

@protocol OC_TestProtocol2
- (id)description;
- (void)method;
+ (id)alloc;
+ (id)classMethod;
@end

@protocol OC_TestProtocolT1
+ (int)classMethod1;
@end

#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wprotocol"
#pragma clang diagnostic ignored "-Wincomplete-implementation"
@interface OC_TestProtocolClass : NSObject <OC_TestProtocol, OC_TestProtocol2> {
}
@end

@implementation OC_TestProtocolClass
@end
#pragma clang diagnostic pop

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "protocols", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_protocol(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_protocol(void)
{
    PyObject* m;
    Protocol* p;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }
    if (PyObjC_ImportAPI(m) < 0) {
        return NULL;
    }

    p              = @protocol(OC_TestProtocol);
    PyObject* prot = PyObjC_ObjCToPython("@", &p);
    if (!prot) {
        return NULL;
    }

    if (PyModule_AddObject(m, "OC_TestProtocol", prot) < 0) {
        return NULL;
    }

    p    = @protocol(OC_NSObjectBased);
    prot = PyObjC_ObjCToPython("@", &p);
    if (!prot) {
        return NULL;
    }
    if (PyModule_AddObject(m, "OC_NSObjectBased", prot) < 0) {
        return NULL;
    }

    p    = @protocol(OC_TestProtocolT1);
    prot = PyObjC_ObjCToPython("@", &p);
    if (!prot) {
        return NULL;
    }
    if (PyModule_AddObject(m, "OC_TestProtocolT1", prot) < 0) {
        return NULL;
    }

    return m;
}
