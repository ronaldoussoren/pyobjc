#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

@interface OC_ArgSizeInArg : NSObject {
}
@end

#define BODY                                                                             \
    {                                                                                    \
        size_t          i, len = count;                                                  \
        NSMutableArray* result = [NSMutableArray array];                                 \
        if (result == nil)                                                               \
            return nil;                                                                  \
        for (i = 0; i < len; i++) {                                                      \
            [result addObject:[NSNumber numberWithInt:values[i]]];                       \
        }                                                                                \
        return result;                                                                   \
    }

#define PBODY                                                                            \
    {                                                                                    \
        size_t          i, len = *count;                                                 \
        NSMutableArray* result = [NSMutableArray array];                                 \
        if (result == nil)                                                               \
            return nil;                                                                  \
        for (i = 0; i < len; i++) {                                                      \
            [result addObject:[NSNumber numberWithInt:values[i]]];                       \
        }                                                                                \
        return result;                                                                   \
    }

@implementation OC_ArgSizeInArg
+ (NSArray*)nsrange:(NSRange)count array:(int*)values
{
    size_t          i, len = count.length;
    NSMutableArray* result = [NSMutableArray array];
    if (result == nil)
        return nil;
    for (i = 0; i < len; i++) {
        [result addObject:[NSNumber numberWithInt:values[i]]];
    }
    return result;
}

+ (NSArray*)cfrange:(CFRange)count array:(int*)values
{
    size_t          i, len = count.length;
    NSMutableArray* result = [NSMutableArray array];
    if (result == nil)
        return nil;
    for (i = 0; i < len; i++) {
        [result addObject:[NSNumber numberWithInt:values[i]]];
    }
    return result;
}

+ (NSArray*)id:(NSArray*)count array:(int*)values
{
    size_t          i, len = [count count];
    NSMutableArray* result = [NSMutableArray array];
    if (result == nil)
        return nil;
    for (i = 0; i < len; i++) {
        [result addObject:[NSNumber numberWithInt:values[i]]];
    }
    return result;
}

+ (NSArray*)cfarray:(CFArrayRef)count array:(int*)values
{
    size_t          i, len = [(NSArray*)count count];
    NSMutableArray* result = [NSMutableArray array];
    if (result == nil)
        return nil;
    for (i = 0; i < len; i++) {
        [result addObject:[NSNumber numberWithInt:values[i]]];
    }
    return result;
}

+ (NSArray*)pnsrange:(NSRange*)count array:(int*)values
{
    size_t          i, len = count->length;
    NSMutableArray* result = [NSMutableArray array];
    if (result == nil)
        return nil;
    for (i = 0; i < len; i++) {
        [result addObject:[NSNumber numberWithInt:values[i]]];
    }
    return result;
}

+ (NSArray*)pcfrange:(CFRange*)count array:(int*)values
{
    size_t          i, len = count->length;
    NSMutableArray* result = [NSMutableArray array];
    if (result == nil)
        return nil;
    for (i = 0; i < len; i++) {
        [result addObject:[NSNumber numberWithInt:values[i]]];
    }
    return result;
}

+ (NSArray*)pid:(NSArray**)count array:(int*)values
{
    if (!count) {
        return nil;
    }
    size_t          i, len = [*count count];
    NSMutableArray* result = [NSMutableArray array];
    if (result == nil)
        return nil;
    for (i = 0; i < len; i++) {
        [result addObject:[NSNumber numberWithInt:values[i]]];
    }
    return result;
}

+ (NSArray*)pcfarray:(CFArrayRef*)count array:(int*)values
{
    size_t          i, len = [*(NSArray**)count count];
    NSMutableArray* result = [NSMutableArray array];
    if (result == nil)
        return nil;
    for (i = 0; i < len; i++) {
        [result addObject:[NSNumber numberWithInt:values[i]]];
    }
    return result;
}

+ (NSArray*)intchar:(char)count
              array:(int*)values BODY

                    + (NSArray*)char
                   :(char)count
              array:(int*)values BODY

                    + (NSArray*)uchar
                   :(unsigned char)count
              array:(int*)values BODY

                    + (NSArray*)short
                   :(short)count
              array:(int*)values BODY

                    + (NSArray*)ushort
                   :(unsigned short)count
              array:(int*)values BODY

                    + (NSArray*)int
                   :(int)count
              array:(int*)values BODY

                    + (NSArray*)uint
                   :(unsigned int)count
              array:(int*)values BODY

                    + (NSArray*)long
                   :(long)count
              array:(int*)values BODY

                    + (NSArray*)ulong
                   :(unsigned long)count
              array:(int*)values BODY

                    + (NSArray*)longlong
                   :(long long)count
              array:(int*)values BODY

                    + (NSArray*)float
                   :(float)count
              array:(int*)values BODY

                    + (NSArray*)ulonglong
                   :(unsigned long long)count
              array:(int*)values BODY

                    + (NSArray*)pintchar
                   :(char*)count
              array:(int*)values PBODY

                    + (NSArray*)pchar
                   :(char*)count
              array:(int*)values PBODY

                    + (NSArray*)pchar2
                   :(char*)count
              array:(int*)values PBODY

                    + (NSArray*)puchar
                   :(unsigned char*)count
              array:(int*)values PBODY

                    + (NSArray*)pshort
                   :(short*)count
              array:(int*)values PBODY

                    + (NSArray*)pushort
                   :(unsigned short*)count
              array:(int*)values PBODY

                    + (NSArray*)pint
                   :(int*)count
              array:(int*)values PBODY

                    + (NSArray*)puint
                   :(unsigned int*)count
              array:(int*)values PBODY

                    + (NSArray*)plong
                   :(long*)count
              array:(int*)values PBODY

                    + (NSArray*)pulong
                   :(unsigned long*)count
              array:(int*)values PBODY

                    + (NSArray*)plonglong
                   :(long long*)count
              array:(int*)values PBODY

                    + (NSArray*)pulonglong
                   :(unsigned long long*)count
              array:(int*)values PBODY

                    + (NSArray*)pfloat
                   :(float*)count
              array:(int*)values PBODY

                    @end

                    static PyMethodDef mod_methods[] =
{
    {
        0, 0, 0, 0
    }
};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "bufsizeinarg", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_bufsizeinarg(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_bufsizeinarg(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    if (PyObjC_ImportAPI(m) < 0) {
        return NULL;
    }

    if (PyModule_AddObject(m, "OC_ArgSizeInArg",
                           PyObjC_IdToPython([OC_ArgSizeInArg class]))
        < 0) {
        return NULL;
    }

    return m;
}
