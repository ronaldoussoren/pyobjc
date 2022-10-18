/* Copyright (c) 1996,97 by Lele Gaifax. All Rights Reserved
 * Copyright 2002, 2003 Ronald Oussoren, Jack Jansen
 * Copyright 2003-2021 Ronald Oussoren
 *
 * This software may be used and distributed freely for any purpose
 * provided that this notice is included unchanged on any and all
 * copies. The author does not warrant or guarantee this software in
 * any way.
 */

#include "pyobjc.h"

/* XXX: Are these includes still needed */
#include "compile.h" /* From Python */
#include <dlfcn.h>

#include <stdarg.h>

#import <Foundation/NSDictionary.h>
#import <Foundation/NSEnumerator.h>
#import <Foundation/NSInvocation.h>
#import <Foundation/NSKeyValueObserving.h>
#import <Foundation/NSMethodSignature.h>
#import <Foundation/NSObject.h>
#import <Foundation/NSString.h>

#import "OC_PythonUnicode.h"

NS_ASSUME_NONNULL_BEGIN

@implementation OC_PythonObject
+ (id<NSObject> _Nullable)objectWithPythonObject:(PyObject*)obj
{
    return [[[self alloc] initWithPyObject:obj] autorelease];
}

- (id _Nullable)initWithPyObject:(PyObject*)obj
{
    PyObjC_RegisterObjCProxy(obj, self);

    SET_FIELD_INCREF(pyObject, obj);

    return self;
}

- (oneway void)release
{
    /* See comment in OC_PythonUnicode */
    if (unlikely(!Py_IsInitialized())) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        [super release];
        return;
        // LCOV_EXCL_STOP
    }

    PyObjC_BEGIN_WITH_GIL
        @try {
            [super release];

        } @catch (NSObject* exc) { // LCOV_EXCL_LINE
            /* This catch statement is here mostly
             * for code consistency, [NSProxy release]
             * should never raise.
             */
            // LCOV_EXCL_START
            PyObjC_LEAVE_GIL;
            @throw;
            // LCOV_EXCL_STOP
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
        PyObjC_UnregisterObjCProxy(pyObject, self);
        Py_CLEAR(pyObject);

    PyObjC_END_WITH_GIL

    [super dealloc];
}

- (id)copyWithZone:(NSZone* _Nullable)zone
{
    (void)zone;
    NSObject* result;
    PyObject* copy;

    if (PyObjC_CopyFunc == NULL || PyObjC_CopyFunc == Py_None) {
        @throw [NSException exceptionWithName:NSInvalidArgumentException
                                       reason:@"cannot copy Python objects"
                                     userInfo:nil];

    } else {
        PyObjC_BEGIN_WITH_GIL
            copy = PyObjC_CallCopyFunc(pyObject);
            if (copy == NULL) {
                PyObjC_GIL_FORWARD_EXC();
            }

            if (depythonify_python_object(copy, &result) == -1) {
                Py_DECREF(copy);
                PyObjC_GIL_FORWARD_EXC();
            }
            Py_DECREF(copy);

        PyObjC_END_WITH_GIL
    }

    if (result) {
        [result retain];
    }
    return result;
}

- (id)copy
{
    return [self copyWithZone:NULL];
}

/* Undocumented method used by NSLog, this seems to work. */
- (NSString*)_copyDescription
{
    return [[self description] copy];
}

- (NSString*)description
{
    PyObject* repr;

    if (pyObject == NULL)           // LCOV_BR_EXCL_LINE
        return @"no python object"; // LCOV_EXCL_LINE

    PyObjC_BEGIN_WITH_GIL

        repr = PyObject_Repr(pyObject);

        if (repr) {
            int       err;
            NSString* result;

            err = depythonify_python_object(repr, &result);
            Py_DECREF(repr);
            if (err == -1) {
                PyObjC_GIL_FORWARD_EXC();
            }

            PyObjC_GIL_RETURN(result);
        }
        PyObjC_GIL_FORWARD_EXC();

    PyObjC_END_WITH_GIL
}

- (void)doesNotRecognizeSelector:(SEL)aSelector
{
    @throw [NSException
        exceptionWithName:NSInvalidArgumentException
                   reason:[NSString stringWithFormat:@"%@ does not recognize -%s", self,
                                                     sel_getName(aSelector)]
                 userInfo:nil];
}

static inline int
check_argcount(PyObject* pymethod, Py_ssize_t argcount)
{
    PyCodeObject* func_code;

    if (PyObjC_is_pyfunction(pymethod)) {
        func_code = (PyCodeObject*)PyObjC_get_code(pymethod);
        if (func_code == NULL) {
            return -1;
        }
        if (argcount == func_code->co_argcount) {
            Py_DECREF(func_code);
            return 0;
        }
        Py_DECREF(func_code);

    } else if (PyObjC_is_pymethod(pymethod)) {
        func_code = PyObjC_get_code(pymethod);
        if (func_code == NULL) {
            return -1;
        }
        if (argcount == func_code->co_argcount - 1) {
            Py_DECREF(func_code);
            return 0;
        }
        Py_DECREF(func_code);
    }

    return -1;
}

/*#F If the Python object @var{obj} implements a method whose name matches
  the Objective-C selector @var{aSelector} and accepts the correct number
  of arguments, return that method, otherwise NULL. */
static PyObject* _Nullable get_method_for_selector(PyObject* obj, SEL aSelector)
{
    const char* meth_name;
    char        pymeth_name[256];
    Py_ssize_t  argcount;
    PyObject*   pymethod;
    const char* p;

    if (!aSelector) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        @throw [NSException exceptionWithName:NSInvalidArgumentException
                                       reason:@"nil selector"
                                     userInfo:nil];
        // LCOV_EXCL_STOP
    }

    meth_name = sel_getName(aSelector);

    for (argcount = 0, p = meth_name; *p; p++) {
        if (*p == ':') {
            argcount++;
        }
    }

    const char* py_meth_name =
        PyObjC_SELToPythonName(aSelector, pymeth_name, sizeof(pymeth_name) - 1);
    if (py_meth_name == NULL) {
        return NULL;
    }
    pymethod = PyObject_GetAttrString(obj, py_meth_name);
    if (pymethod == NULL) {
        return NULL;
    }
    if (check_argcount(pymethod, argcount) == -1) {
        Py_DECREF(pymethod);
        return NULL;
    }
    return pymethod;
}

- (BOOL)respondsToSelector:(SEL)aSelector
{
    PyObject* m;
    Method    method;

    /*
     * We cannot rely on NSProxy, it doesn't implement most of the
     * NSObject interface anyway.
     */

    method = class_getInstanceMethod(object_getClass(self), aSelector);
    if (method != NULL) {
        return YES;
    }

    PyObjC_BEGIN_WITH_GIL
        m = get_method_for_selector(pyObject, aSelector);

        if (m) {
            Py_DECREF(m);
            PyObjC_GIL_RETURN(YES);
        } else {
            PyErr_Clear();
            PyObjC_GIL_RETURN(NO);
        }

    PyObjC_END_WITH_GIL
}

+ (NSMethodSignature* _Nullable)methodSignatureForSelector:(SEL)sel
{
    Method m;

    m = class_getClassMethod(self, sel);
    if (m) {
        /* A real Objective-C method */
        const char* typestr = method_getTypeEncoding(m);
        if (typestr == NULL) { // LCOV_BR_EXCL_LINE
            return nil;        // LCOV_EXCL_LINE
        }
        return [NSMethodSignature signatureWithObjCTypes:typestr];
    }
    return nil;
}

- (NSMethodSignature* _Nullable)methodSignatureForSelector:(SEL)sel
{
    /* We can't call our superclass implementation, NSProxy just raises
     * an exception.
     */

    char*      encoding;
    PyObject*  pymethod;
    Py_ssize_t argcount;
    Class      cls;
    Method     m;

    cls = object_getClass(self);
    m   = class_getInstanceMethod(cls, sel);
    if (m != NULL) {
        /* A real Objective-C method */
        const char* typestr = method_getTypeEncoding(m);
        if (typestr == NULL) { // LCOv_BR_EXCL_LINE
            return nil;        // LCOV_EXCL_LINE
        }
        return [NSMethodSignature signatureWithObjCTypes:typestr];
    }

    PyObjC_BEGIN_WITH_GIL

        pymethod = get_method_for_selector(pyObject, sel);
        if (!pymethod) {
            PyErr_Clear();
            PyObjC_GIL_RETURN(nil);
        }

        if (PyObjC_is_pymethod(pymethod)) {
            argcount = PyObjC_num_arguments(pymethod) - 1;

        } else {
            argcount = PyObjC_num_arguments(pymethod);
        }
        Py_DECREF(pymethod);
        if (argcount < 0) {
            PyObjC_GIL_FORWARD_EXC();
        }

        encoding = alloca(argcount + 4);
        memset(encoding, '@', argcount + 3);
        encoding[argcount + 3] = '\0';
        encoding[2]            = ':';

    PyObjC_END_WITH_GIL

    return [NSMethodSignature signatureWithObjCTypes:encoding];
}

- (BOOL)_forwardNative:(NSInvocation*)invocation
{
    SEL aSelector = [invocation selector];

    if (sel_isEqual(aSelector, @selector(description))) {
        id res = [self description];
        [invocation setReturnValue:&res];
        return YES;

    } else if (sel_isEqual(aSelector, @selector(_copyDescription))) {
        id res = [self _copyDescription];
        [invocation setReturnValue:&res];

        return YES;

    } else if (sel_isEqual(aSelector, @selector(respondsToSelector:))) {
        SEL  sel;
        BOOL b;

        [invocation getArgument:&sel atIndex:2];

        b = [self respondsToSelector:sel];
        [invocation setReturnValue:&b];

        return YES;

    } else if (sel_isEqual(aSelector, @selector(classForKeyedArchiver))) {
        Class c;

        c = [self classForKeyedArchiver];
        [invocation setReturnValue:&c];

        return YES;

    } else if (sel_isEqual(aSelector, @selector(classForArchiver))) {
        Class c;

        c = [self classForArchiver];
        [invocation setReturnValue:&c];

        return YES;

    } else if (sel_isEqual(aSelector, @selector(classForCoder))) {
        Class c;

        c = [self classForCoder];
        [invocation setReturnValue:&c];

        return YES;

    } else if (sel_isEqual(aSelector, @selector(classForPortCoder))) {
        Class c;

        c = [self classForPortCoder];
        [invocation setReturnValue:&c];

        return YES;

    } else if (sel_isEqual(aSelector, @selector(replacementObjectForKeyedArchiver:))) {
        NSObject*        c;
        NSKeyedArchiver* archiver;

        [invocation getArgument:&archiver atIndex:2];
        c = [self replacementObjectForKeyedArchiver:archiver];
        [invocation setReturnValue:&c];

        return YES;

    } else if (sel_isEqual(aSelector, @selector(replacementObjectForArchiver:))) {
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"

        NSObject*   c;
        NSArchiver* archiver;

        [invocation getArgument:&archiver atIndex:2];
        c = [self replacementObjectForArchiver:archiver];
        [invocation setReturnValue:&c];

#pragma clang diagnostic pop

        return YES;

    } else if (sel_isEqual(aSelector, @selector(replacementObjectForCoder:))) {
        NSObject* c;
        NSCoder*  archiver;

        [invocation getArgument:&archiver atIndex:2];
        c = [self replacementObjectForCoder:archiver];
        [invocation setReturnValue:&c];

        return YES;

    } else if (sel_isEqual(aSelector, @selector(replacementObjectForPortCoder:))) {
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"

        NSObject*    c;
        NSPortCoder* archiver;

        [invocation getArgument:&archiver atIndex:2];
        c = [self replacementObjectForPortCoder:archiver];
        [invocation setReturnValue:&c];

#pragma clang diagnostic pop

        return YES;

    } else if (sel_isEqual(aSelector, @selector(copy))) {
        NSObject* c;

        c = [self copy];
        [invocation setReturnValue:&c];

        return YES;

    } else if (sel_isEqual(aSelector, @selector(copyWithZone:))) {
        NSObject* c;
        NSZone*   zone;

        [invocation getArgument:&zone atIndex:2];
        c = [self copyWithZone:zone];
        [invocation setReturnValue:&c];

        return YES;

    } else if (sel_isEqual(aSelector, @selector(doesNotRecognizeSelector:))) {
        SEL sel;

        [invocation getArgument:&sel atIndex:2];
        [self doesNotRecognizeSelector:sel];

        return YES;

    } else if (sel_isEqual(aSelector, @selector(hash))) {
        NSUInteger hash;

        hash = [self hash];
        [invocation setReturnValue:&hash];

        return YES;
    } else if (sel_isEqual(aSelector, @selector(methodSignatureForSelector:))) {
        SEL       sel;
        NSObject* result;

        [invocation getArgument:&sel atIndex:2];
        result = [self methodSignatureForSelector:sel];
        [invocation setReturnValue:&result];

        return YES;
    }
    return NO;
}

- (void)forwardInvocation:(NSInvocation*)invocation
{
    NSMethodSignature* msign     = [invocation methodSignature];
    SEL                aSelector = [invocation selector];
    PyObject*          pymethod;
    PyObject*          result;
    const char*        rettype = [msign methodReturnType];
    int                err;
    PyObject*          args = NULL;
    unsigned int       i;
    NSUInteger         argcount;
    Py_ssize_t         retsize;
    char*              retbuffer;

    if ([self _forwardNative:invocation]) {
        return;
    }

    PyObjC_BEGIN_WITH_GIL

        retsize = PyObjCRT_SizeOfType(rettype);
        if (retsize == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }

        retbuffer = alloca(retsize);

        /* XXX: Convert this to vectorcall, needs with some
         * luck this can be done without creating a bound
         * method.
         */
        pymethod = get_method_for_selector(pyObject, aSelector);

        if (!pymethod) {
            PyObjC_LEAVE_GIL;

            [self doesNotRecognizeSelector:aSelector];
            return;
        }

        @try {
            argcount = [msign numberOfArguments];

            // LCOV_EXCL_START
        } @catch (NSObject* exc) {
            PyObjC_LEAVE_GIL;
            @throw;
        }
        // LCOV_EXCL_STOP

        args = PyTuple_New(argcount - 2);
        if (args == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(pymethod);
            PyObjC_GIL_FORWARD_EXC();
            // LCOV_EXCL_STOP
        }
        for (i = 2; i < argcount; i++) {
            const char* argtype;
            char*       argbuffer;
            Py_ssize_t  argsize;
            PyObject*   pyarg;

            @try {
                argtype = [msign getArgumentTypeAtIndex:i];
                // LCOV_EXCL_START
            } @catch (NSObject* exc) {
                PyObjC_LEAVE_GIL;
                @throw;
            }
            // LCOV_EXCL_STOP

            argsize = PyObjCRT_SizeOfType(argtype);
            if (argsize == -1) {
                Py_DECREF(args);
                Py_DECREF(pymethod);
                PyObjC_GIL_FORWARD_EXC();
            }
            argbuffer = alloca(argsize);

            Py_BEGIN_ALLOW_THREADS
                @try {
                    [invocation getArgument:argbuffer atIndex:i];

                    // LCOV_EXCL_START
                } @catch (NSObject* exc) {
                    PyObjC_LEAVE_GIL;
                    @throw;
                }
            // LCOV_EXCL_STOP
            Py_END_ALLOW_THREADS

            pyarg = pythonify_c_value(argtype, argbuffer);
            if (pyarg == NULL) {
                Py_DECREF(args);
                Py_DECREF(pymethod);
                PyObjC_GIL_FORWARD_EXC();
            }

            PyTuple_SET_ITEM(args, i - 2, pyarg);
        }
        result = PyObject_CallObject(pymethod, args);
        Py_DECREF(args);
        args = NULL;
        Py_DECREF(pymethod);
        pymethod = NULL;

        if (result == NULL) {
            PyObjC_GIL_FORWARD_EXC();
            return;
        }

        err = depythonify_c_value(rettype, result, retbuffer);
        Py_DECREF(result);
        if (err == -1) {
            PyObjC_GIL_FORWARD_EXC();
        } else {
            Py_BEGIN_ALLOW_THREADS
                @try {
                    [invocation setReturnValue:retbuffer];

                    // LCOV_EXCL_START
                } @catch (NSObject* localException) {
                    PyObjC_LEAVE_GIL;
                    @throw;
                }
            // LCOV_EXCL_STOP
            Py_END_ALLOW_THREADS
        }

    PyObjC_END_WITH_GIL
}

- (PyObject* _Nullable)__pyobjc_PythonObject__
{
    PyObjC_BEGIN_WITH_GIL
        /* XXX: This is a bit too magic. Can pyObject ever be NULL?
         * and why not return None in that case?
         */
        if (pyObject == NULL) {
            PyObject* r = PyObjCObject_New(self, PyObjCObject_kDEFAULT, YES);
            PyObjC_GIL_RETURN(r);
        } else {
            Py_XINCREF(pyObject);
            PyObjC_GIL_RETURN(pyObject);
        }
    PyObjC_END_WITH_GIL
}
- (PyObject*)__pyobjc_PythonTransient__:(int*)cookie
{
    PyObjC_BEGIN_WITH_GIL
        *cookie = 0;
        Py_INCREF(pyObject);
    PyObjC_END_WITH_GIL
    return pyObject;
}

+ (PyObject* _Nullable)__pyobjc_PythonTransient__:(int*)cookie
{
    PyObject* rval;

    PyObjC_BEGIN_WITH_GIL
        rval    = PyObjCClass_New([OC_PythonObject class]);
        *cookie = 0;
    PyObjC_END_WITH_GIL

    return rval;
}

/*
 * Implementation for Key-Value Coding.
 *
 * Because this is a subclass of NSProxy we must implement all of the protocol,
 * and cannot rely on the implementation in our superclass.
 *
 */

+ (BOOL)useStoredAccessor
{
    return YES;
}

+ (BOOL)accessInstanceVariablesDirectly
{
    return YES;
}

- (id)valueForKey:(NSString*)key
{
    PyObject* keyName;
    PyObject* val;
    id        res = nil;

    if (PyObjC_getKey == NULL || PyObjC_getKey == Py_None) {
        @throw [NSException exceptionWithName:NSInvalidArgumentException
                                       reason:@"helper function for getKey not set"
                                     userInfo:nil];
    }

    PyObjC_BEGIN_WITH_GIL

        keyName = id_to_python(key);
        if (keyName == NULL) {
            PyObjC_GIL_FORWARD_EXC();
        }

        PyObject* args[3] = {NULL, pyObject, keyName};

        val = PyObject_Vectorcall(PyObjC_getKey, args + 1,
                                  2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
        Py_DECREF(keyName);
        if (val == NULL) {
            PyObjC_GIL_FORWARD_EXC();
        }

        if (depythonify_c_value(@encode(id), val, &res) < 0) {
            Py_DECREF(val);
            PyObjC_GIL_FORWARD_EXC();
        }
        Py_DECREF(val);

    PyObjC_END_WITH_GIL

    return res;
}

- (id _Nullable)storedValueForKey:(NSString*)key
{
    return [self valueForKey:key];
}

- (void)takeValue:value forKey:(NSString*)key
{
    [self setValue:value forKey:key];
}

- (void)setValue:value forKey:(NSString*)key
{
    PyObject* keyName;
    PyObject* pyValue;
    PyObject* val;

    if (PyObjC_setKey == NULL || PyObjC_setKey == Py_None) {
        @throw [NSException exceptionWithName:NSInvalidArgumentException
                                       reason:@"helper function for setKey not set"
                                     userInfo:nil];
    }

    PyObjC_BEGIN_WITH_GIL

        keyName = id_to_python(key);
        if (keyName == NULL) {
            PyObjC_GIL_FORWARD_EXC();
        }

        pyValue = id_to_python(value);
        if (pyValue == NULL) {
            Py_DECREF(keyName);
            PyObjC_GIL_FORWARD_EXC();
        }

        PyObject* args[4] = {NULL, pyObject, keyName, pyValue};

        val = PyObject_Vectorcall(PyObjC_setKey, args + 1,
                                  3 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
        Py_DECREF(keyName);
        Py_DECREF(pyValue);
        if (val == NULL) {
            PyObjC_GIL_FORWARD_EXC();
        }

        Py_DECREF(val);

    PyObjC_END_WITH_GIL
}

- (void)takeStoredValue:value forKey:(NSString*)key
{
    [self takeValue:value forKey:key];
}

- (NSDictionary* _Nullable)valuesForKeys:(NSArray*)keys
{
    NSMutableDictionary* result;
    NSEnumerator*        enumerator;
    id                   aKey, aValue;

    enumerator = [keys objectEnumerator];
    result     = [NSMutableDictionary dictionary];

    while ((aKey = [enumerator nextObject]) != NULL) {
        aValue = [self valueForKey:aKey];
        [result setObject:aValue forKey:aKey];
    }

    return result;
}

- (id _Nullable)valueForKeyPath:(NSString*)keyPath
{
    PyObject* keyName;
    PyObject* val;
    id        res = nil;

    if (PyObjC_getKeyPath == NULL || PyObjC_getKeyPath == Py_None) {
        @throw [NSException exceptionWithName:NSInvalidArgumentException
                                       reason:@"helper function for getKeyPath not set"
                                     userInfo:nil];
    }

    PyObjC_BEGIN_WITH_GIL
        keyName = id_to_python(keyPath);
        if (keyName == NULL) {
            PyObjC_GIL_FORWARD_EXC();
        }

        PyObject* args[3] = {NULL, pyObject, keyName};

        val = PyObject_Vectorcall(PyObjC_getKeyPath, args + 1,
                                  2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
        Py_DECREF(keyName);
        if (val == NULL) {
            PyObjC_GIL_FORWARD_EXC();
        }

        if (depythonify_python_object(val, &res) < 0) {
            Py_DECREF(val);
            PyObjC_GIL_FORWARD_EXC();
        }
        Py_DECREF(val);

    PyObjC_END_WITH_GIL

    return res;
}

- (void)takeValue:value forKeyPath:(NSString*)keyPath
{
    [self setValue:value forKeyPath:keyPath];
}

- (void)setValue:value forKeyPath:(NSString*)keyPath
{
    PyObject* keyName;
    PyObject* pyValue;
    PyObject* val;

    if (PyObjC_setKeyPath == NULL || PyObjC_setKeyPath == Py_None) {
        @throw [NSException exceptionWithName:NSInvalidArgumentException
                                       reason:@"helper function for setKeyPath not set"
                                     userInfo:nil];
    }

    PyObjC_BEGIN_WITH_GIL
        keyName = id_to_python(keyPath);
        if (keyName == NULL) {
            PyObjC_GIL_FORWARD_EXC();
        }

        pyValue = id_to_python(value);
        if (pyValue == NULL) {
            Py_DECREF(keyName);
            PyObjC_GIL_FORWARD_EXC();
        }

        PyObject* args[4] = {NULL, pyObject, keyName, pyValue};

        val = PyObject_Vectorcall(PyObjC_setKeyPath, args + 1,
                                  3 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
        Py_DECREF(keyName);
        Py_DECREF(pyValue);
        if (val == NULL) {
            PyObjC_GIL_FORWARD_EXC();
        }

        Py_DECREF(val);

    PyObjC_END_WITH_GIL
}

- (void)takeValuesFromDictionary:(NSDictionary*)aDictionary
{
    [self setValuesForKeysWithDictionary:aDictionary];
}

- (void)setValuesForKeysWithDictionary:(NSDictionary*)aDictionary
{
    NSEnumerator* enumerator = [aDictionary keyEnumerator];
    id            aKey;
    id            aValue;

    while ((aKey = [enumerator nextObject]) != NULL) {
        aValue = [aDictionary objectForKey:aKey];
        [self takeValue:aValue forKey:aKey];
    }
}

- (void)unableToSetNilForKey:(NSString*)key
{
    @throw [NSException
        exceptionWithName:NSUndefinedKeyException
                   reason:[NSString stringWithFormat:@"cannot set Nil for key: %@", key]
                 userInfo:nil];
}

- (id)handleQueryWithUnboundKey:(NSString*)key
{
    return [self valueForUndefinedKey:key];
}

- (id)valueForUndefinedKey:(NSString*)key
{
    @throw [NSException
        exceptionWithName:NSUndefinedKeyException
                   reason:[NSString stringWithFormat:@"query for unknown key: %@", key]
                 userInfo:nil];
}

- (void)handleTakeValue:value forUnboundKey:(NSString*)key
{
    [self setValue:value forUndefinedKey:key];
}

- (void)setValue:value forUndefinedKey:(NSString*)key
{
    @throw [NSException
        exceptionWithName:NSUndefinedKeyException
                   reason:[NSString stringWithFormat:@"setting unknown key: %@ to <%@>",
                                                     key, value]
                 userInfo:nil];
}

- (void)addObserver:(NSObject*)observer
         forKeyPath:(NSString*)keyPath
            options:(NSKeyValueObservingOptions)options
            context:(void*)context
{
    NSLog(@"*** Ignoring *** %@ for '%@' (of %@ with %#lx in %p).\n",
          NSStringFromSelector(_cmd), keyPath, observer, (long)options, context);
    return;
}
- (void)removeObserver:(NSObject*)observer forKeyPath:(NSString*)keyPath
{
    NSLog(@"*** Ignoring *** %@ for '%@' (of %@).", NSStringFromSelector(_cmd), keyPath,
          observer);
}

/* NSObject protocol */
- (NSUInteger)hash
{
    Py_hash_t rval;

    PyObjC_BEGIN_WITH_GIL
        rval = PyObject_Hash(pyObject);
        if (rval == -1) {
            PyErr_Clear();
            rval = (NSUInteger)pyObject;
        }

    PyObjC_END_WITH_GIL

    return rval;
}

- (BOOL)isEqual:(id)anObject
{
    if (anObject == nil) {
        return NO;

    } else if (self == anObject) {
        return YES;
    }

    PyObjC_BEGIN_WITH_GIL
        PyObject* otherPyObject = id_to_python(anObject);
        if (otherPyObject == NULL) {
            PyErr_Clear();
            PyObjC_GIL_RETURN(NO);
        }
        if (otherPyObject == pyObject) {
            PyObjC_GIL_RETURN(YES);
        }
        switch (PyObject_RichCompareBool(pyObject, otherPyObject, Py_EQ)) {
        case -1:
            PyErr_Clear();
        case 0:
            PyObjC_GIL_RETURN(NO);
            break;
        default:
            PyObjC_GIL_RETURN(YES);
        }
    PyObjC_END_WITH_GIL
}

/* NSObject methods */
- (NSComparisonResult)compare:(id)other
{
    if (other == nil) {
        @throw [NSException exceptionWithName:NSInvalidArgumentException
                                       reason:@"nil argument"
                                     userInfo:nil];
    } else if (self == other) {
        return NSOrderedSame;
    }
    PyObjC_BEGIN_WITH_GIL
        PyObject* otherPyObject = id_to_python(other);
        if (otherPyObject == NULL) {
            PyObjC_GIL_FORWARD_EXC();
        }
        if (otherPyObject == pyObject) {
            PyObjC_GIL_RETURN(NSOrderedSame);
        }
        int r;
        if (PyObjC_Cmp(pyObject, otherPyObject, &r) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
        NSComparisonResult rval;
        switch (r) {
        case -1:
            rval = NSOrderedAscending;
            break;
        case 0:
            rval = NSOrderedSame;
            break;
        default:
            rval = NSOrderedDescending;
        }
        PyObjC_GIL_RETURN(rval);
    PyObjC_END_WITH_GIL
}

/*
 * Support of the NSCoding protocol
 */
- (void)encodeWithCoder:(NSCoder*)coder
{
    PyObjC_encodeWithCoder(pyObject, coder);
}

/*
 * Helper method for initWithCoder, needed to deal with
 * recursive objects (e.g. o.value = o)
 */
- (void)pyobjcSetValue:(NSObject*)other
{
    PyObjC_BEGIN_WITH_GIL
        PyObject* value = id_to_python(other);

        SET_FIELD(pyObject, value);
    PyObjC_END_WITH_GIL
}

- (id _Nullable)initWithCoder:(NSCoder*)coder
{
    pyObject = NULL;

    if (PyObjC_Decoder != NULL && PyObjC_Decoder != Py_None) {
        PyObjC_BEGIN_WITH_GIL
            PyObject* cdr = id_to_python(coder);
            PyObject* setValue;
            PyObject* selfAsPython;
            PyObject* v;

            if (cdr == NULL) {
                PyObjC_GIL_FORWARD_EXC();
            }

            selfAsPython = PyObjCObject_New(self, 0, YES);
            if (selfAsPython == NULL) {   // LCOV_BR_EXCL_LINE
                PyObjC_GIL_FORWARD_EXC(); // LCOV_EXCL_LINE
            }
            setValue = PyObject_GetAttrString(selfAsPython, "pyobjcSetValue_");
            if (setValue == NULL) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_STOP
                Py_DECREF(selfAsPython);
                PyObjC_GIL_FORWARD_EXC();
                // LCOV_EXCL_STOP
            }

            v = PyObjC_CallDecoder(cdr, setValue);
            Py_DECREF(cdr);
            Py_DECREF(setValue);
            Py_DECREF(selfAsPython);

            if (v == NULL) {
                PyObjC_GIL_FORWARD_EXC();
            }

            /* To make life more interesting the correct proxy
             * type for 'v' might not be OC_PythonObject, in particular
             * when introducing new proxy types in new versions
             * of PyObjC, and in some error cases.
             */
            NSObject* temp;
            if (depythonify_python_object(v, &temp) == -1) {
                Py_DECREF(v);
                PyObjC_GIL_FORWARD_EXC();
            }

            if (temp != (NSObject*)self) {
                [temp retain];
                [self release];
                self = (OC_PythonObject*)temp;
            }
            Py_DECREF(pyObject);

        PyObjC_END_WITH_GIL

        return self;

    } else {
        @throw [NSException exceptionWithName:NSInvalidArgumentException
                                       reason:@"decoding Python objects is not supported"
                                     userInfo:nil];
    }
}

- (id _Nullable)awakeAfterUsingCoder:(NSCoder*)__attribute__((__unused__))coder
{
    return self;
}

#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"

- (NSObject*)replacementObjectForArchiver:(NSArchiver*)__attribute__((__unused__))archiver
{
    return (NSObject*)self;
}

- (NSObject*)replacementObjectForPortCoder:(NSPortCoder*)__attribute__((__unused__))
                                           archiver
{
    return (NSObject*)self;
}
#pragma clang diagnostic pop

- (NSObject*)replacementObjectForKeyedArchiver:
    (NSKeyedArchiver*)__attribute__((__unused__))archiver
{
    return (NSObject*)self;
}

- (NSObject*)replacementObjectForCoder:(NSCoder*)__attribute__((__unused__))archiver
{
    return (NSObject*)self;
}

- (Class)classForArchiver
{
    return [OC_PythonObject class];
}

- (Class)classForKeyedArchiver
{
    return [OC_PythonObject class];
}

+ (Class)classForKeyedUnarchiver
{
    return [OC_PythonObject class];
}

- (Class)classForCoder
{
    return [OC_PythonObject class];
}

- (Class)classForPortCoder
{
    return [OC_PythonObject class];
}

/* NOTE: NSProxy does not implement isKindOfClass on Leopard, therefore we
 * have to provide it ourself.
 *
 * Luckily that's kind of easy, we know the entiry class hierarchy and also
 * know there are no subclasses.
 */
- (BOOL)isKindOfClass:(Class)aClass
{
    if (aClass == [NSProxy class] || aClass == [OC_PythonObject class]) {
        return YES;
    }
    return NO;
}

/*
 * This is needed to be able to add a python object to a
 * NSArray and then use array.description()
 */
- (BOOL)isNSArray__
{
    return NO;
}
- (BOOL)isNSDictionary__
{
    return NO;
}
- (BOOL)isNSSet__
{
    return NO;
}
- (BOOL)isNSNumber__
{
    return NO;
}
- (BOOL)isNSData__
{
    return NO;
}
- (BOOL)isNSDate__
{
    return NO;
}
- (BOOL)isNSString__
{
    return NO;
}
- (BOOL)isNSValue__
{
    return NO;
}

+ (id _Nullable)classFallbacksForKeyedArchiver
{
    return nil;
}

/*
 * Fake implementation for _cfTypeID, which gets called by
 * system frameworks on some occasions.
 */
static BOOL     haveTypeID = NO;
static CFTypeID _NSObjectTypeID;

- (CFTypeID)_cfTypeID
{
    if (haveTypeID) {
        NSObject* obj   = [[NSObject alloc] init];
        _NSObjectTypeID = CFGetTypeID((CFTypeRef)obj);
        [obj release];
        haveTypeID = YES;
    }
    return _NSObjectTypeID;
}

@end /* OC_PythonObject class implementation */

void
PyObjC_encodeWithCoder(PyObject* pyObject, NSCoder* coder)
{
    /* XXX: This should be called with the GIL held, and should
     * return an error indicator.
     */
    if (PyObjC_Encoder != NULL && PyObjC_Encoder != Py_None) {
        PyObjC_BEGIN_WITH_GIL
            PyObject* cdr = id_to_python(coder);
            if (cdr == NULL) {            // LCOV_BR_EXCL_LINE
                PyObjC_GIL_FORWARD_EXC(); // LCOV_EXCL_LINE
            }

            PyObject* args[3] = {NULL, pyObject, cdr};

            PyObject* r = PyObject_Vectorcall(PyObjC_Encoder, args + 1,
                                              2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
            Py_DECREF(cdr);
            Py_XDECREF(r);
            if (r == NULL) {
                PyObjC_GIL_FORWARD_EXC();
            }

        PyObjC_END_WITH_GIL

    } else {
        @throw [NSException exceptionWithName:NSInvalidArgumentException
                                       reason:@"encoding Python objects is not supported"
                                     userInfo:nil];
    }
}

NS_ASSUME_NONNULL_END
