/*
 * Test support for the special support for BOOL, UniChar and "flavours of char"
 * (using special metadata)
 */
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

NS_ASSUME_NONNULL_BEGIN

typedef struct _EmbeddedBool {
    int  count;
    BOOL isValid;
} EmbeddedBoolStruct;

typedef struct _EmbeddedBoolArray {
    int  count;
    BOOL valid[4];
} EmbeddedBoolArrayStruct;

@interface OC_TestSpecialTypeCode : NSObject {
    int _idx;
}
@end

@implementation OC_TestSpecialTypeCode

static BOOL    gBOOLValues[]     = {YES, NO};
static UniChar gUniCharValues[]  = {'a', 55, 9243, 'b'};
static char    gTextCharValues[] = {'a', 55, 'z'};
static char    gNumCharValues[]  = {1, 2, 3, 4};

- (instancetype)init
{
    self = [super init];
    if (self == nil)
        return nil;

    _idx = 0;
    return self;
}

- (BOOL)BOOLValue
{
    BOOL result = gBOOLValues[_idx];
    _idx        = (_idx + 1) % (sizeof(gBOOLValues) / sizeof(BOOL));
    return result;
}

- (UniChar)UniCharValue
{
    UniChar result = gUniCharValues[_idx];
    _idx           = (_idx + 1) % (sizeof(gUniCharValues) / sizeof(UniChar));
    return result;
}

- (char)byteValue
{
    char result = gTextCharValues[_idx];
    _idx        = (_idx + 1) % (sizeof(gTextCharValues) / sizeof(char));
    return result;
}

- (char)int8Value
{
    char result = gNumCharValues[_idx];
    _idx        = (_idx + 1) % (sizeof(gNumCharValues) / sizeof(char));
    return result;
}

- (BOOL*)BOOLArray
{
    static BOOL gBOOLArray[] = {YES, NO, YES, NO};
    return gBOOLArray;
}

- (UniChar*)UniCharArray
{
    static UniChar gUniCharArray[] = {100, 400, 955, 40000};
    return gUniCharArray;
}

- (UniChar*)UniCharString
{
    static UniChar gUniCharArray[] = {'h', 'e', 'l', 'p', 0};
    return gUniCharArray;
}

- (char*)byteArray
{
    static char gByteArray[] = {100, 200, 150, 99};
    return gByteArray;
}

- (char*)byteString
{
    static char gByteString[] = "hello world";
    return gByteString;
}

- (char*)int8Array
{
    static char gByteArray[] = {100, 200, 150, 99};
    return gByteArray;
}

- (char*)int8String
{
    static char gByteString[] = "hello";
    return gByteString;
}

- (NSObject* _Nullable)BOOLArg:(BOOL)v1 andBOOLArg:(BOOL)v2
{
    return [NSArray arrayWithObjects:[NSNumber numberWithInt:(int)v1],
                                     [NSNumber numberWithInt:(int)v2], nil];
}

- (NSObject* _Nullable)BOOLArrayOf4In:(BOOL*)value
{
    return [NSArray arrayWithObjects:[NSNumber numberWithInt:(int)value[0]],
                                     [NSNumber numberWithInt:(int)value[1]],
                                     [NSNumber numberWithInt:(int)value[2]],
                                     [NSNumber numberWithInt:(int)value[3]], nil];
}

- (void)BOOLArrayOf4Out:(BOOL*)value
{
    switch (_idx % 4) {
    case 0:
        value[0] = YES;
        value[1] = NO;
        value[2] = YES;
        value[3] = NO;
        break;
    case 1:
        value[0] = NO;
        value[1] = YES;
        value[2] = NO;
        value[3] = YES;
        break;
    case 2:
        value[0] = YES;
        value[1] = YES;
        value[2] = YES;
        value[3] = YES;
        break;
    case 3:
        value[0] = NO;
        value[1] = NO;
        value[2] = NO;
        value[3] = NO;
        break;
    }

    _idx += 1;
}

- (NSObject* _Nullable)BOOLArrayOf4InOut:(BOOL*)value
{
    NSObject* result =
        [NSArray arrayWithObjects:[NSNumber numberWithInt:(int)value[0]],
                                  [NSNumber numberWithInt:(int)value[1]],
                                  [NSNumber numberWithInt:(int)value[2]],
                                  [NSNumber numberWithInt:(int)value[3]], nil];

    switch (_idx % 4) {
    case 0:
        value[0] = YES;
        value[1] = YES;
        value[2] = YES;
        value[3] = YES;
        break;
    case 1:
        value[0] = NO;
        value[1] = NO;
        value[2] = NO;
        value[3] = NO;
        break;
    case 2:
        value[0] = YES;
        value[1] = NO;
        value[2] = YES;
        value[3] = NO;
        break;
    case 3:
        value[0] = NO;
        value[1] = YES;
        value[2] = NO;
        value[3] = YES;
        break;
    }

    _idx += 1;

    return result;
}

- (EmbeddedBoolArrayStruct)identicalEmbeddedBoolArrayStruct:(EmbeddedBoolArrayStruct)v
{
    return v;
}

- (EmbeddedBoolStruct)identicalEmbeddedBoolStruct:(EmbeddedBoolStruct)v
{
    return v;
}

- (NSObject* _Nullable)UniCharStringArg:(UniChar*)value
{
    NSUInteger length = 0;
    while (value[length] != 0) {
        length++;
    }
    return [NSString stringWithCharacters:value length:length];
}

- (NSObject* _Nullable)UniCharArg:(UniChar)a andUniCharArg:(UniChar)b
{
    return [NSArray arrayWithObjects:[NSString stringWithCharacters:&a length:1],
                                     [NSString stringWithCharacters:&b length:1], nil];
}

- (void)UniCharArrayOf4Out:(UniChar*)buffer
{
    buffer[0] = 'b';
    buffer[1] = 'o';
    buffer[2] = 'a';
    buffer[3] = 't';
}
- (NSObject* _Nullable)UniCharArrayOf4InOut:(UniChar*)buffer
{
    NSObject* result = [NSString stringWithCharacters:buffer length:4];
    buffer[0]        = 'h';
    buffer[1]        = 'a';
    buffer[2]        = 'n';
    buffer[3]        = 'd';
    return result;
}
- (NSObject* _Nullable)UniCharArrayOf4In:(UniChar*)buffer
{
    return [NSString stringWithCharacters:buffer length:4];
}

- (NSObject* _Nullable)byteStringArg:(char*)value
{
    return [NSString stringWithCString:value encoding:NSISOLatin1StringEncoding];
}

- (NSObject* _Nullable)byteArg:(char)a andbyteArg:(char)b
{
    char      abuf[2];
    char      bbuf[2];
    NSObject* a1;
    NSObject* a2;

    abuf[0] = a;
    abuf[1] = 0;
    bbuf[0] = b;
    bbuf[1] = 0;

    a1 = [NSString stringWithCString:abuf encoding:NSISOLatin1StringEncoding];
    if (!a1)
        return nil;
    a2 = [NSString stringWithCString:bbuf encoding:NSISOLatin1StringEncoding];
    if (!a2)
        return nil;
    return [NSArray arrayWithObjects:a1, a2, nil];
}

- (void)byteArrayOf4Out:(char*)buffer
{
    buffer[0] = 'b';
    buffer[1] = 'o';
    buffer[2] = 'a';
    buffer[3] = 't';
}

- (NSObject* _Nullable)byteArrayOf4InOut:(char*)buffer
{
    char tmp[5];
    int  i;
    for (i = 0; i < 4; i++) {
        tmp[i] = buffer[i];
    }
    tmp[4]           = 0;
    NSObject* result = [NSString stringWithCString:tmp
                                          encoding:NSISOLatin1StringEncoding];
    buffer[0]        = 'h';
    buffer[1]        = 'a';
    buffer[2]        = 'n';
    buffer[3]        = 'd';
    return result;
}

- (NSObject* _Nullable)byteArrayOf4In:(char*)buffer
{
    char tmp[5];
    int  i;
    for (i = 0; i < 4; i++) {
        tmp[i] = buffer[i];
    }
    tmp[4] = 0;
    return [NSString stringWithCString:tmp encoding:NSISOLatin1StringEncoding];
}

- (NSObject* _Nullable)int8StringArg:(char*)value
{
    NSMutableArray* a = [[NSMutableArray alloc] init];
    int             i;

    for (i = 0; value[i] != 0; i++) {
        [a addObject:[NSNumber numberWithInt:value[i]]];
    }
    return [a autorelease];
}

- (NSObject*)int8Arg:(char)a andint8Arg:(char)b
{
    return [NSArray
        arrayWithObjects:[NSNumber numberWithInt:a], [NSNumber numberWithInt:b], nil];
}

- (void)int8ArrayOf4Out:(char*)buffer
{
    buffer[0] = 'b';
    buffer[1] = 'o';
    buffer[2] = 'a';
    buffer[3] = 't';
}

- (NSObject* _Nullable)int8ArrayOf4InOut:(char*)buffer
{
    NSObject* result = [NSArray arrayWithObjects:[NSNumber numberWithInt:buffer[0]],
                                                 [NSNumber numberWithInt:buffer[1]],
                                                 [NSNumber numberWithInt:buffer[2]],
                                                 [NSNumber numberWithInt:buffer[3]], nil];
    buffer[0]        = 'h';
    buffer[1]        = 'a';
    buffer[2]        = 'n';
    buffer[3]        = 'd';
    return result;
}

- (NSObject* _Nullable)int8ArrayOf4In:(char*)buffer
{
    NSObject* result = [NSArray arrayWithObjects:[NSNumber numberWithInt:buffer[0]],
                                                 [NSNumber numberWithInt:buffer[1]],
                                                 [NSNumber numberWithInt:buffer[2]],
                                                 [NSNumber numberWithInt:buffer[3]], nil];
    return result;
}

@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static int mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0) {
        return -1;
    }

    if (PyModule_AddObject(m, "OC_TestSpecialTypeCode",
                           PyObjC_IdToPython([OC_TestSpecialTypeCode class]))
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
    .m_name = "specialtypecodes",
    .m_doc = NULL,
    .m_size = 0,
    .m_methods = mod_methods,
    .m_slots = mod_slots,
    .m_traverse = NULL,
    .m_clear = NULL,
    .m_free = NULL,
};

PyObject* PyInit_specialtypecodes(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_specialtypecodes(void)
{
    return PyModuleDef_Init(&mod_module);
}

NS_ASSUME_NONNULL_END
