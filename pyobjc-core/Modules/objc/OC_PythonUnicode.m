#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

@implementation OC_PythonUnicode

+ (instancetype _Nullable)unicodeWithPythonObject:(PyObject*)v
{
    return [[[self alloc] initWithPythonObject:v] autorelease];
}

- (instancetype _Nullable)initWithPythonObject:(PyObject*)v
{
    self = [super init];
    if (unlikely(self == nil)) // LCOV_BR_EXCL_LINE
        return nil;            // LCOV_EXCL_LINE

    SET_FIELD_INCREF(value, v);
    return self;
}

- (PyObject*)__pyobjc_PythonObject__
{
    /* XXX: Can value ever be NULL? */
    if (value == NULL) {
        Py_INCREF(Py_None);
        return Py_None;
    }
    Py_INCREF(value);
    return value;
}

- (PyObject*)__pyobjc_PythonTransient__:(int*)cookie
{
    *cookie = 0;
    Py_INCREF(value);
    return value;
}

+ (BOOL)supportsSecureCoding
{
    return NO;
}

- (oneway void)release
{
    /* There is small race condition when an object is almost deallocated
     * in one thread and fetched from the registration mapping in another
     * thread. If we don't get the GIL this object might get a -dealloc
     * message just as the other thread is fetching us from the mapping.
     * That's why we need to grab the GIL here (getting it in dealloc is
     * too late, we'd already be dead).
     */
    /* FIXME: Should switch to __weak on OSX 10.7 or later, that should
     * fix this issue without a performance penalty.
     */
    /*
     * There is also a race condition on application shutdown between
     * the call to Py_Finalize (shutting down the interpreter) and the
     * cleanup performed by Cocoa, possible on other threads.
     */
    if (unlikely(!Py_IsInitialized())) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        [super release];
        return;
        // LCOV_EXCL_STOP
    }

    PyObjC_BEGIN_WITH_GIL
        @try {
            [super release];

        } @catch (NSObject* exc) {
            PyObjC_LEAVE_GIL;
            @throw;
        }
    PyObjC_END_WITH_GIL
}

- (void)dealloc
{
    if (unlikely(!Py_IsInitialized())) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        [super dealloc];
        return;
        // LCOV_EXCL_STOP
    }
    PyObjC_BEGIN_WITH_GIL
        PyObjC_UnregisterObjCProxy(value, self);
        @try {
            [realObject release];
        } @catch (NSObject* exc) { // LCOV_EXCL_LINE
            // LCOV_EXCL_START
            PyObjC_LEAVE_GIL;
            @throw;
            // LCOV_EXCL_STOP
        }
        realObject = nil;
        Py_CLEAR(value);

    PyObjC_END_WITH_GIL

    [super dealloc];
}

- (id _Nullable)__realObject__
{
#ifdef Py_DEBUG
    if (!PyUnicode_IS_READY(value)) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        /* Object should be ready, ensure we crash with the GIL
         * held when it's not.
         */
        PyObjC_BEGIN_WITH_GIL
            PyUnicode_GET_LENGTH(value);
        PyObjC_END_WITH_GIL
        // LCOV_EXCL_STOP
    }
#endif

    if (!realObject) {
        switch (PyUnicode_KIND(value)) {
        case PyUnicode_1BYTE_KIND:
            if (PyUnicode_IS_ASCII(value)) {
                realObject = [[NSString alloc]
                    initWithBytesNoCopy:PyUnicode_1BYTE_DATA(value)
                                 length:(NSUInteger)PyUnicode_GET_LENGTH(value)
                               encoding:NSASCIIStringEncoding
                           freeWhenDone:NO];
            } else {
                realObject = [[NSString alloc]
                    initWithBytesNoCopy:PyUnicode_1BYTE_DATA(value)
                                 length:(NSUInteger)PyUnicode_GET_LENGTH(value)
                               encoding:NSISOLatin1StringEncoding
                           freeWhenDone:NO];
            }
            break;

        case PyUnicode_2BYTE_KIND:
            realObject = [[NSString alloc]
                initWithCharactersNoCopy:PyUnicode_2BYTE_DATA(value)
                                  length:(NSUInteger)PyUnicode_GET_LENGTH(value)
                            freeWhenDone:NO];
            break;

#if PY_VERSION_HEX < 0x030C0000
        case PyUnicode_WCHAR_KIND:
            /* wchar_t representation, treat same
             * as UCS4 strings
             */
#endif
        case PyUnicode_4BYTE_KIND:
            PyObjC_BEGIN_WITH_GIL
                PyObject* utf8 = PyUnicode_AsUTF8String(value);
                if (!utf8) {
                    NSLog(@"failed to encode unicode string to byte string");
                    PyErr_Clear();
                } else {
                    realObject =
                        [[NSString alloc] initWithBytes:PyBytes_AS_STRING(utf8)
                                                 length:(NSUInteger)PyBytes_GET_SIZE(utf8)
                                               encoding:NSUTF8StringEncoding];
                    Py_DECREF(utf8);
                }
            PyObjC_END_WITH_GIL
        }
    }
    return realObject;
}

- (NSUInteger)length
{
    return [[self __realObject__] length];
}

- (unichar)characterAtIndex:(NSUInteger)anIndex
{
    return [[self __realObject__] characterAtIndex:anIndex];
}

- (void)getCharacters:(unichar*)buffer range:(NSRange)aRange
{
    [[self __realObject__] getCharacters:buffer range:aRange];
}

- (void)getCharacters:(unichar*)buffer
{
    [[self __realObject__] getCharacters:buffer];
}

/*
 * NSCoding support
 */
- (id)initWithCharactersNoCopy:(unichar*)characters
                        length:(NSUInteger)length
                  freeWhenDone:(BOOL)flag
{
    int byteorder = 0;
    /* XXX: Call super? */
    PyObjC_BEGIN_WITH_GIL
        /* Decode as a UTF-16 string in native byteorder */
        value =
            PyUnicode_DecodeUTF16((const char*)characters, length * 2, NULL, &byteorder);
        if (value == NULL) {
            /* XXX: Maybe just return nil? */
            PyObjC_GIL_FORWARD_EXC();
        }

    PyObjC_END_WITH_GIL;
    if (flag) {
        free(characters);
    }
    return self;
}

- (id _Nullable)initWithBytes:(const void*)bytes
                       length:(NSUInteger)length
                     encoding:(NSStringEncoding)encoding
{
    int byteorder = 0;

    /*
     * Call the super initializer first.
     */
    self = [super init];
    if (self == nil) { // LCOV_BR_EXCL_LINE
        return nil;    // LCOV_EXCL_LINE
    }

    /*
     * The most common encoding is UTF-8, use a shortcut
     * for that.
     */
    if (encoding == NSUTF8StringEncoding) {
        PyObjC_BEGIN_WITH_GIL
            value = PyUnicode_DecodeUTF8(bytes, length, NULL);
            if (value == NULL) {
                PyObjC_GIL_FORWARD_EXC();
            }
        PyObjC_END_WITH_GIL
        return self;
    }

    /* And finally: first use the Cocoa decoder to create an NSString, copy the unichars
     * into a temporary buffer and use that to create a Python unicode string using the
     * UTF16 decoder.
     *
     * This can be slightly optimized on systems where sizeof(Py_UNICODE) ==
     * sizeof(unichar), but that's not worth the additional complexity and won't work on
     * Python 3.3 or later anyway.
     */

    NSString*  tmpval    = [[NSString alloc] initWithBytes:bytes
                                                length:length
                                              encoding:encoding];
    Py_ssize_t charcount = [tmpval length];

    /* NOTE: the malloc() call can be avoided when sizeof(unichar) == sizeof(Py_UNICODE)
     * and we're on python 3.2 or earlier. That's not worth the added complexity.
     */
    unichar* chars = malloc(charcount * 2);

    if (chars == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        [tmpval release];
        [self release];
        return nil;
        // LCOV_EXCL_STOP
    }
    [tmpval getCharacters:chars range:NSMakeRange(0, charcount)];
    [tmpval release];

    PyObjC_BEGIN_WITH_GIL
        /* Decode as a UTF-16 string in native byteorder */
        byteorder = 0;
        value = PyUnicode_DecodeUTF16((const char*)chars, length * 2, NULL, &byteorder);
        free(chars);
        if (value == NULL) { // LCOV_BR_EXCL_LINE
            //  LCOV_EXCL_START
            PyObjC_GIL_FORWARD_EXC();
            //  LCOV_EXCL_STOP
        }

    PyObjC_END_WITH_GIL;
    return self;
}

/*
 * Helper method for initWithCoder, needed to deal with
 * recursive objects (e.g. o.value = o)
 */
- (void)pyobjcSetValue:(NSObject*)other
{
    PyObjC_BEGIN_WITH_GIL
        PyObject* v = id_to_python(other);

        SET_FIELD(value, v);
    PyObjC_END_WITH_GIL
}

- (id _Nullable)initWithCoder:(NSCoder*)coder
{
    int ver;
    if ([coder allowsKeyedCoding]) {
        ver = [coder decodeInt32ForKey:@"pytype"];
    } else {
        [coder decodeValueOfObjCType:@encode(int) at:&ver];
    }
    if (ver == 1) {
        /* Version 1: plain unicode string (not subclass).
         * emitted by some versions of PyObjC (< 2.4.1, < 2.5.1, <2.6)
         */
        self = [super initWithCoder:coder];
        return self;
    } else if (ver == 2) {

        if (PyObjC_Decoder != NULL && PyObjC_Decoder != Py_None) {
            PyObjC_BEGIN_WITH_GIL
                PyObject* setValue;
                PyObject* selfAsPython;
                PyObject* v;

                PyObject* cdr = id_to_python(coder);
                if (cdr == NULL) {            // LCOV_BR_EXCL_LINE
                    PyObjC_GIL_FORWARD_EXC(); // LCOV_EXCL_LINE
                }

                selfAsPython = PyObjCObject_New(self, 0, YES);
                if (selfAsPython == NULL) {   // LCOV_BR_EXCL_LINE
                    PyObjC_GIL_FORWARD_EXC(); // LCOV_EXCL_LINE
                }
                setValue = PyObject_GetAttrString(selfAsPython, "pyobjcSetValue_");

                v = PyObjC_CallDecoder(cdr, setValue);
                Py_DECREF(cdr);
                Py_DECREF(setValue);
                Py_DECREF(selfAsPython);

                if (v == NULL) {
                    PyObjC_GIL_FORWARD_EXC();
                }

                SET_FIELD(value, v);

                self = PyObjC_FindOrRegisterObjCProxy(value, self);

            PyObjC_END_WITH_GIL

            return self;

        } else { // LCOV_BR_EXCL_LINE
            // LOCV_EXCL_START
            @throw
                [NSException exceptionWithName:NSInvalidArgumentException
                                        reason:@"decoding Python objects is not supported"
                                      userInfo:nil];
            return nil;
            // LOCV_EXCL_STOP
        }
    } else {
        @throw [NSException exceptionWithName:NSInvalidArgumentException
                                       reason:@"decoding Python objects is not supported"
                                     userInfo:nil];
    }
}

- (void)encodeWithCoder:(NSCoder*)coder
{
    int is_exact_unicode;
    PyObjC_BEGIN_WITH_GIL
        is_exact_unicode = PyUnicode_CheckExact(value);
    PyObjC_END_WITH_GIL

    if (is_exact_unicode) {
        if ([coder allowsKeyedCoding]) {
            [coder encodeInt32:1 forKey:@"pytype"];
        }
        [super encodeWithCoder:coder];
    } else {
        if ([coder allowsKeyedCoding]) {
            [coder encodeInt32:2 forKey:@"pytype"];
        } else {
            int v = 2;
            [coder encodeValueOfObjCType:@encode(int) at:&v];
        }

        PyObjC_encodeWithCoder(value, coder);
    }
}

- (NSObject* _Nullable)replacementObjectForArchiver:
    (NSArchiver*)__attribute__((__unused__))archiver
{
    return self;
}

- (NSObject* _Nullable)replacementObjectForKeyedArchiver:
    (NSKeyedArchiver*)__attribute__((__unused__))archiver
{
    return self;
}

- (NSObject* _Nullable)replacementObjectForCoder:(NSCoder*)__attribute__((__unused__))
                                                 archiver
{
    return self;
}

- (NSObject* _Nullable)replacementObjectForPortCoder:
    (NSPortCoder*)__attribute__((__unused__))archiver
{
    return self;
}

/*
 * Plain unicode objects (not subclasses) are archived as "real"
 * NSString objects. This means you won't get the same object type back
 * when reading them back, but does allow for better interop with code
 * that uses a non-keyed archiver.
 */
- (Class)classForCoder
{
    Class result;
    PyObjC_BEGIN_WITH_GIL
        if (PyUnicode_CheckExact(value)) {
            result = [NSString class];
        } else {
            result = [OC_PythonUnicode class];
        }
    PyObjC_END_WITH_GIL
    return result;
}

- (Class _Nullable)classForKeyedArchiver
{
    return [OC_PythonUnicode class];
}

/* Ensure that we can be unarchived as a generic string by pure ObjC
 * code.
 */
+ (NSArray*)classFallbacksForKeyedArchiver
{
    return [NSArray arrayWithObject:@"NSString"];
}

@end /* implementation OC_PythonUnicode */

NS_ASSUME_NONNULL_END
