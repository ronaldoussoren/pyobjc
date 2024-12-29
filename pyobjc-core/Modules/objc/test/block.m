#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

static void erase_signature(id _block);

@interface
NSObject (IndirectBlockTest)
- (double)processBlock:(double (^)(double, double))aBlock;
- (id)optionalBlock:(id (^)(id))aBlock;
- (void)callWithCompletion:(void (^)(id))aBlock;
@end

@interface OCTestBlock : NSObject {
    id (^stored_block)(id, id);
}

- (int (^)(void))getIntBlock;
- (double (^)(double, double))getFloatBlock;
- (NSRect (^)(double, double, double, double))getStructBlock;
- (void)callIntBlock:(void (^)(int))block withValue:(int)value;
- (double)callDoubleBlock:(double (^)(double, double))block
                withValue:(double)v1
                 andValue:(double)v2;
- (id)callOptionalBlock:(id (^)(id))block withValue:(id)value;
- (void)callCompletionOn:(NSObject*)v
                andArray:(NSMutableArray*)w
     withErasedSignature:(int)erased;

- (int (^)(int))getIntBlock2;
- (int (^)(int, int))getIntBlock3;
- (int (^)(NSString*))getObjectBlock;
- (int (^)(NSString*, NSString*))getObjectBlock2;
- (void (^)(void))getRaisingBlock;
- (id (^)(id, ...))getVariadicBlock;
- (id (^)(const char*, ...))getPrintfBlock;
- (id (^)(const char*, ...))getPrintfBlock2;
- (id (^)(const char*, ...))getPrintfBlock3;

- (id)signatureForBlock1:(double (^)(double, double))block;
- (id)signatureForBlock2:(id (^)(id))block;
- (id)signatureForBlock3:(id (^)(short))block;
- (id)signatureForBlock4:(char (^)(int, int, float))block;

@end

static int (^gIntBlock)(void) = nil;

@implementation OCTestBlock

-(id)init
{
    self = [super init];
    if (!self) {
        return nil;
    }

    if (gIntBlock == nil) {
        gIntBlock = [^{
          return 42;
        } copy];
    }

    stored_block = nil;
    return self;
}

- (NSRect (^)(double, double, double, double))getStructBlock
{
    return [[^(double a, double b, double c, double d) {
      return NSMakeRect(a, b, c, d);
    } copy] autorelease];
}

- (int (^)(void))getIntBlock
{
    return gIntBlock;
}

- (int (^)(int))getIntBlock2
{
    return [[^(int x) {
      return x * 2;
    } copy] autorelease];
}

- (int (^)(int, int))getIntBlock3
{
    return [[^(int x, int y) {
      return x + y;
    } copy] autorelease];
}

- (int (^)(NSString*))getObjectBlock
{
    return [[^(NSString* a) {
      return [a length];
    } copy] autorelease];
}

- (int (^)(NSString*, NSString*))getObjectBlock2
{
    return [[^(NSString* a, NSString* b) {
      return [a length] + [b length];
    } copy] autorelease];
}

- (double (^)(double, double))getFloatBlock
{
    __block int counter = 0;
    return [[^(double a, double b) {
        counter ++;
        return a + b + counter;
    } copy] autorelease];
}

- (double (^)(double, double))getFloatBlock2
{
    return [[^(double a, double b) {
      return a * b;
    } copy] autorelease];
}

- (void (^)(void))getRaisingBlock
{
    return [[^(void) {
        [NSException raise:@"SimpleException" format:@"hello world"];
    } copy] autorelease];
}

- (id (^)(id, ...))getVariadicBlock
{
    return [[^(id first, ...) {
        NSMutableArray* result = [NSMutableArray array];
        va_list ap;

        va_start(ap, first);

        do {
            [result addObject:first];

            first = va_arg(ap, id);
        } while (first != nil);

        va_end(ap);
        return result;
    } copy] autorelease];
}

- (id (^)(const char*, ...))getPrintfBlock
{
    return [[^(id fmt, ...) {
        char buffer[256];
        va_list ap;

        va_start(ap, fmt);

#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wformat-nonliteral"

        vsnprintf(buffer, sizeof(buffer), [fmt UTF8String], ap);
#pragma clang diagnostic pop

        va_end(ap);
        return [NSString stringWithUTF8String:buffer];
    } copy] autorelease];
}

- (id (^)(const char*, ...))getPrintfBlock2
{
    return [[^(int* output, id fmt, ...) {
        *output=42;
        char buffer[256];
        va_list ap;

        va_start(ap, fmt);

#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wformat-nonliteral"

        vsnprintf(buffer, sizeof(buffer), [fmt UTF8String], ap);
#pragma clang diagnostic pop

        va_end(ap);
        return [NSString stringWithUTF8String:buffer];
    } copy] autorelease];
}

- (id (^)(const char*, ...))getPrintfBlock3
{
    return [[^(int* input, id fmt, ...) {
        *input=42;
        char buffer[256];
        va_list ap;

        va_start(ap, fmt);

#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wformat-nonliteral"

        vsnprintf(buffer, sizeof(buffer), [fmt UTF8String], ap);
#pragma clang diagnostic pop

        va_end(ap);
        return [NSString stringWithUTF8String:buffer];
    } copy] autorelease];
}

- (id(^)(id, id, id, id, id, id, id))getHugeBlock
{
    return [[^(id a, id b, id c, id d, id e, id f, id g) {
        return [NSArray arrayWithObjects:a, b, c, d, e, f, g, nil];
    } copy] autorelease];
}

- (void)callIntBlock:(void (^)(int))block withValue:(int)value
{
    block(value);
}

- (void)callCopiedIntBlock:(void (^)(int))block withValue:(int)value
{
    void (^copy)(int) = [block copy];
    copy(value);
    [copy release];
}

- (double)callDoubleBlock:(double (^)(double, double))block
                withValue:(double)v1
                 andValue:(double)v2
{
    return block(v1, v2);
}

- (NSRect)callStructBlock:(NSRect (^)(double, double, double, double))block
                        a:(double)a
                        b:(double)b
                        c:(double)c
                        d:(double)d
{
    return block(a, b, c, d);
}

- (double)callProcessBlockOn:(NSObject*)testObject
{
    return [testObject processBlock:^(double a, double b) {
      return a * b;
    }];
}

- (id)callOptionalBlockOn:(NSObject*)testObject
{
    return [testObject optionalBlock:nil];
}

- (id)callOptionalBlock:(id (^)(id))block withValue:(id)value
{
    if (!block) {
        return @"NOBLOCK";
    } else {
        return block(value);
    }
}

- (void)callCompletionOn:(NSObject*)v
                andArray:(NSMutableArray*)w
     withErasedSignature:(int)erased
{
    void (^block)(id value) = ^(id value) {
      [w addObject:value];
    };
    if (erased) {
        erase_signature(block);
    }
    [v callWithCompletion:block];
}

#define BLOCK_HAS_COPY_DISPOSE (1 << 25)
#define BLOCK_HAS_SIGNATURE (1 << 30)

struct block_descriptor {
    unsigned long int reserved;
    unsigned long int size;
    void (*copy_helper)(void* dst, void* src);
    void (*dispose_helper)(void* src);
    const char* signature;
};

struct block_literal {
    void* isa;
    int   flags;
    int   reserved;
    void (*invoke)(void*, ...);
    struct block_descriptor* descriptor;
};

static void
erase_signature(id _block)
{
    struct block_literal* block = (struct block_literal*)_block;
    if (block->flags & BLOCK_HAS_SIGNATURE) {
        block->flags &= ~BLOCK_HAS_SIGNATURE;
    }
}

static id
signature_for_block(id _block)
{
    struct block_literal* block = (struct block_literal*)_block;

    if (block->flags & BLOCK_HAS_SIGNATURE) {
        const char* signature_loc = (void*)(block->descriptor);
        signature_loc += sizeof(unsigned long) * 2;
        if (block->flags & BLOCK_HAS_COPY_DISPOSE) {
            signature_loc += sizeof(void (*)(void)) * 2;
        }
        return [NSString stringWithUTF8String:*(const char**)signature_loc];
    }

    return nil;
}

- (id)signatureForBlock1:(double (^)(double, double))block
{
    return signature_for_block(block);
}

- (id)signatureForBlock2:(id (^)(id))block
{
    return signature_for_block(block);
}

- (id)signatureForBlock3:(id (^)(short))block
{
    return signature_for_block(block);
}

- (id)signatureForBlock4:(char (^)(int, int, float))block
{
    return signature_for_block(block);
}

- (void)storeBlock:(id (^)(id, id))value
{
    [stored_block release];
    stored_block = [value copy];
}

- (id (^)(id, id))getStoredBlock
{
    return [[stored_block retain] autorelease];
}

-(void)dealloc
{
    [stored_block release];
    stored_block = nil;

    [super dealloc];
}


@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};


static int mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0) {
        return -1;
    }
    if (PyModule_AddObject(m, "OCTestBlock", PyObjC_IdToPython([OCTestBlock class]))
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
    .m_name = "block",
    .m_doc = NULL,
    .m_size = 0,
    .m_methods = mod_methods,
    .m_slots = mod_slots,
    .m_traverse = NULL,
    .m_clear = NULL,
    .m_free = NULL,
};

PyObject* PyInit_block(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_block(void)
{
    return PyModuleDef_Init(&mod_module);
}
