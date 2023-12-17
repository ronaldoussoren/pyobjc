/*
 * This module is used in the unittests for the sequence API
 */
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

@interface OC_TestSequence : NSObject {
    NSObject*  objects[128];
    NSUInteger len;
}
- (id)initWithArray:(NSArray*)array;
- (NSUInteger)count;
- (id)objectAtIndex:(NSUInteger)idx;

@end

@implementation OC_TestSequence

- (id)initWithArray:(NSArray*)array
{
    NSUInteger i;

    self = [super init];
    if (!self)
        return nil;

    len = [array count];
    if (len > 128) {
        len = 128;
    }
    for (i = 0; i < len; i++) {
        objects[i] = [[array objectAtIndex:i] retain];
    }
    return self;
}

- (void)dealloc
{
    NSUInteger i;
    for (i = 0; i < len; i++) {
        [objects[i] release];
    }
    [super dealloc];
}

- (NSUInteger)count
{
    return len;
}

- (id)objectAtIndex:(NSUInteger)idx
{
    if (idx >= len) {
        [NSException raise:NSRangeException
                    format:@"Index %ld is out of range", (long)idx];
    }
    return [[objects[idx] retain] autorelease];
}

@end

@interface OC_TestMutableSequence : OC_TestSequence {
}
- (void)setObject:(id)value atIndex:(NSUInteger)idx;
@end

@implementation OC_TestMutableSequence
- (void)setObject:(id)value atIndex:(NSUInteger)idx
{
    if (idx >= len) {
        [NSException raise:NSRangeException
                    format:@"Index %ld is out of range", (long)idx];
    }
    [value retain];
    [objects[idx] release];
    objects[idx] = value;
}
@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "sequence", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_sequence(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_sequence(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    if (PyObjC_ImportAPI(m) < 0) {
        return NULL;
    }

    if (PyModule_AddObject(m, "OC_TestSequence",
                           PyObjC_IdToPython([OC_TestSequence class]))
        < 0) {
        return NULL;
    }

    if (PyModule_AddObject(m, "OC_TestMutableSequence",
                           PyObjC_IdToPython([OC_TestMutableSequence class]))
        < 0) {
        return NULL;
    }

    return m;
}
