/* Copyright (c) 1996,97 by Lele Gaifax. All Rights Reserved
 * Copyright (c) 2002-2021 Ronald Oussoren.
 *
 * This software may be used and distributed freely for any purpose
 * provided that this notice is included unchanged on any and all
 * copies. The author does not warrant or guarantee this software in
 * any way.
 *
 * This file is part of the PyObjC package.
 *
 * RCSfile: OC_PythonObject.h,v
 * Revision: 1.16
 * Date: 1998/08/18 15:35:51
 *
 * Created Wed Sep 4 18:36:15 1996.
 *
 * NOTE: This used to be an ObjC translation of 'Python/abstract.h', most of
 *       that was removed by Ronald because no-one was using or maintaining
 *       that functionality. OC_PythonObject is now a simple proxy for plain
 *       python objects.
 *
 */

#ifndef _OC_PythonObject_H
#define _OC_PythonObject_H

NS_ASSUME_NONNULL_BEGIN

/* XXX: Also implement <NSObject>? */
PyObjC_FINAL_CLASS @interface OC_PythonObject : NSProxy<NSCopying> {
    PyObject* pyObject;
}

+ (id<NSObject> _Nullable)objectWithPythonObject:(PyObject*)obj;
- (id _Nullable)initWithPyObject:(PyObject*)obj;

/*!
 * @method __pyobjc_PythonObject__
 * @result Returns a new reference to the wrapped object
 * @discussion
 *     This method is part of the implementation of objc_support.m,
 *     see that file for details.
 */
- (PyObject* _Nullable)__pyobjc_PythonObject__;
- (void)forwardInvocation:(NSInvocation*)invocation;
- (BOOL)respondsToSelector:(SEL)aSelector;
- (NSMethodSignature* _Nullable)methodSignatureForSelector:(SEL)selector;
- (void)doesNotRecognizeSelector:(SEL)aSelector;

/* NSObject protocol */
- (NSUInteger)hash;
- (BOOL)isEqual:(id)anObject;
/* NSObject methods */
- (NSComparisonResult)compare:(id)other;

/* Key-Value Coding support */
+ (BOOL)useStoredAccessor;
+ (BOOL)accessInstanceVariablesDirectly;
- (id)valueForKey:(NSString*)key;
- (NSDictionary* _Nullable)valuesForKeys:(NSArray*)keys;
- (id _Nullable)valueForKeyPath:(NSString*)keyPath;
- (id _Nullable)storedValueForKey:(NSString*)key;
- (void)takeValue:value forKey:(NSString*)key;
- (void)setValue:value forKey:(NSString*)key;
- (void)setValue:value forKeyPath:(NSString*)key;
- (void)takeStoredValue:value forKey:(NSString*)key;
- (void)takeValue:value forKeyPath:(NSString*)keyPath;
- (void)takeValuesFromDictionary:(NSDictionary*)aDictionary;
- (void)setValuesForKeysWithDictionary:(NSDictionary*)aDictionary;
- (void)unableToSetNilForKey:(NSString*)key;
- (id)valueForUndefinedKey:(NSString*)key;
- (void)handleTakeValue:value forUnboundKey:(NSString*)key;
- (void)setValue:value forUndefinedKey:(NSString*)key;

/* These two are only present to *disable* coding, not implement it */
- (void)encodeWithCoder:(NSCoder*)coder;
- (id _Nullable)initWithCoder:(NSCoder*)coder;
+ (id _Nullable)classFallbacksForKeyedArchiver;
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
- (NSObject*)replacementObjectForArchiver:(NSArchiver*)archiver;
- (NSObject*)replacementObjectForPortCoder:(NSPortCoder*)archiver;
#pragma clang diagnostic pop
- (NSObject*)replacementObjectForKeyedArchiver:(NSKeyedArchiver*)archiver;
- (NSObject*)replacementObjectForCoder:(NSCoder*)archiver;
- (Class)classForArchiver;
- (Class)classForKeyedArchiver;
+ (Class)classForKeyedUnarchiver;
- (Class)classForCoder;
- (Class)classForPortCoder;
- (id _Nullable)awakeAfterUsingCoder:(NSCoder*)coder;

@end /* OC_PythonObject class interface */

NS_ASSUME_NONNULL_END

#endif /* _OC_PythonObject_H */
