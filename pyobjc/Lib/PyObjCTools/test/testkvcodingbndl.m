/*
 * This file implements a (number of) class(es) that are used to test
 * the Key/Value coding support within PyObjC
 *
 * NOTES
 * - The implementation must be synchronized with test_keyvalue2.py, see that
 *   file for more details.
 */
#import <Foundation/Foundation.h>

#include <Python.h>
#include <pyobjc-api.h>
#include <objc/objc-runtime.h>


@interface KVBaseClass : NSObject
{
    NSString *directString;
    NSNumber *directNumber;
    NSString *indirectString;
    NSNumber *indirectNumber;
}
@end

@implementation KVBaseClass
- init
{
    self = [super init];
    if (!self) return nil;

    directString = [@"Direct String" retain];
    directNumber = [[NSNumber numberWithInt: 42] retain];
    indirectString = [@"Indirect String" retain];
    indirectNumber = [[NSNumber numberWithInt: 84] retain];

    return self;
}

- (NSString *) indirectString; { return indirectString; }
- (void) setIndirectString: (NSString *) aString;
{
    [aString retain];
    [indirectString release];
    indirectString = aString;
}

- (NSNumber *) indirectNumber; { return indirectNumber; }
- (void) setIndirectNumber: (NSNumber *) aNumber;
{
    [aNumber retain];
    [indirectNumber release];
    indirectNumber = aNumber;
}
@end

@interface KVPathClass : NSObject
{
    KVBaseClass *directHead;
    KVBaseClass *indirectHead;
}
@end

@implementation KVPathClass
- init
{
    self = [super init];
    if (!self) return nil;

    directHead = [[KVBaseClass alloc] init];
    indirectHead = [[KVBaseClass alloc] init];

    return self;
}

- (KVBaseClass *) indirectHead { return indirectHead; } 
- (void) setInidrectHead: (KVBaseClass *) aHead;
{
    [aHead retain];
    [indirectHead release];
    indirectHead = aHead;
}
@end

/* Python glue */

static PyMethodDef no_methods[] = {
	{ 0, 0, 0, 0 }
};

void inittestkvcodingbndl(void);
void inittestkvcodingbndl(void)
{
    PyObject* m;

    m = Py_InitModule4("testkvcodingbndl", no_methods, 
		       NULL, NULL, PYTHON_API_VERSION);
    if (!m) return;

    if (PyObjC_ImportAPI(m) < 0) return;

    PyModule_AddObject(m, "KVBaseClass", 
		       PyObjCClass_New([KVBaseClass class]));
    PyModule_AddObject(m, "KVPathClass", 
		       PyObjCClass_New([KVPathClass class]));
}
