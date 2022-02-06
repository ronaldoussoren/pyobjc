#include "Python.h"
#include "pyobjc-api.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

@interface OC_NullDelimitedResult : NSObject {
}
@end

@implementation OC_NullDelimitedResult

#define BODY(type)                                                                       \
    {                                                                                    \
        static type buffer[] = {1, 2, 3, 4, 0};                                          \
        return buffer;                                                                   \
    }

+ (char*)intchars
{
    static char buffer[] = {1, 2, 3, 4, 0};
    return buffer;
}

+ (void*)voids
{
    static char buffer[] = {1, 2, 3, 4, 0};
    return (void*)buffer;
}

+ (FILE**)files
{
    static FILE* buffer[3] = {0, 0, 0};
    if (buffer[0] == 0) {
        buffer[0] = stdin;
        buffer[1] = stdout;
    }
    return buffer;
}

+ (char*)chars BODY(char)

                   + (char*)chars2 BODY(char)

                   + (unsigned char*)uchars BODY(unsigned char)

                   + (unsigned char*)uchars2 BODY(unsigned char)

                   + (short*)shorts BODY(short)

                   + (unsigned short*)ushorts BODY(unsigned short)

                   + (int*)ints BODY(int)

                   + (unsigned int*)uints BODY(unsigned int)

                   + (long*)longs BODY(long)

                   + (unsigned long*)ulongs BODY(unsigned long)

                   + (long long*)longlongs BODY(long long)

                   + (unsigned long long*)ulonglongs BODY(unsigned long long)

                   + (float*)floats BODY(float)

                   + (id*)objects
{
    static id buf[] = {@"one", @"two", @"three", @"four", nil};
    return buf;
}

+ (id*)newrefsOfClass:(Class)aClass
{
    /* XXX: This leaks, but that's ok for a test */
    id* buf = malloc(sizeof(id) * 3);
    if (buf == NULL) {
        NSLog(@"Cannot allocate buffer");
        return NULL;
    }
    buf[0] = buf[1] = buf[2] = nil;
    buf[0]                   = [[aClass alloc] init];
    if (buf[0] == nil) {
        NSLog(@"Cannot allocate instance 0");
        return nil;
    }
    buf[1] = [[aClass alloc] init];
    if (buf[1] == nil) {
        NSLog(@"Cannot allocate instance 1");
        return nil;
    }
    return buf;
}

@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {PyModuleDef_HEAD_INIT,
                                        "nulldelimitedresult",
                                        NULL,
                                        0,
                                        mod_methods,
                                        NULL,
                                        NULL,
                                        NULL,
                                        NULL};

PyObject* PyInit_nulldelimitedresult(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_nulldelimitedresult(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    PyObjC_ImportAPI(m);

    if (PyModule_AddObject(m, "OC_NullDelimitedResult",
                           PyObjC_IdToPython([OC_NullDelimitedResult class]))
        < 0) {
        return NULL;
    }

    return m;
}
