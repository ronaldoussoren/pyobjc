/* Copyright (c) 1996,97 by Lele Gaifax.  All Rights Reserved
 * Copyright (c) 2002,2003 Ronald Oussoren.
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
 * Created Wed Sep  4 18:36:15 1996.
 *
 * NOTE: This used to be an ObjC translation of 'Python/abstract.h', most of
 *       that was removed by Ronald because no-one was using or maintaining
 *       that functionality. OC_PythonObject is now a simple proxy for plain
 *       python objects.
 *
 */

#ifndef _OC_PythonObject_H
#define _OC_PythonObject_H

#import <Foundation/NSProxy.h>
#import <Foundation/NSDictionary.h>
#import <Foundation/NSMethodSignature.h>


@interface OC_PythonObject : NSProxy 
{
  PyObject *pyObject;
}

+ (int)wrapPyObject:(PyObject *)argument toId:(id *)datum;
+ newWithObject:(PyObject *) obj;
+ depythonifyTable;
+ pythonifyStructTable;
+ (PyObject *)__pythonifyStruct:(PyObject *) obj withType:(const char *) type length:(Py_ssize_t) length;
+ newWithCoercedObject:(PyObject *) obj;
- initWithObject:(PyObject *) obj;

/*!
 * @method pyObject
 * @result Returns a borrowed reference to the wrapped object
 */
- (PyObject*) pyObject;

/*!
 * @method __pyobjc_PythonObject__
 * @result Returns a new reference to the wrapped object
 * @discussion
 * 	This method is part of the implementation of objc_support.m,
 * 	see that file for details.
 */
- (PyObject*) __pyobjc_PythonObject__;
- (void) forwardInvocation:(NSInvocation *) invocation;
- (BOOL) respondsToSelector:(SEL) aSelector;
- (NSMethodSignature *) methodSignatureForSelector:(SEL) selector;
- (void) doesNotRecognizeSelector:(SEL) aSelector;

/* NSObject protocol */
- (unsigned)hash;
- (BOOL)isEqual:(id)anObject;
/* NSObject methods */
- (NSComparisonResult)compare:(id)other;

/* Key-Value Coding support */
+ (BOOL)useStoredAccessor;
+ (BOOL)accessInstanceVariablesDirectly;
- valueForKey:(NSString*) key;
- (NSDictionary*) valuesForKeys: (NSArray*)keys;
- valueForKeyPath: (NSString*) keyPath;
- storedValueForKey: (NSString*) key;
- (void)takeValue: value forKey: (NSString*) key;
- (void)setValue: value forKey: (NSString*) key;
- (void)setValue: value forKeyPath: (NSString*) key;
- (void)takeStoredValue: value forKey: (NSString*) key;
- (void)takeValue: value forKeyPath: (NSString*) keyPath;
- (void)takeValuesFromDictionary: (NSDictionary*) aDictionary;
- (void)setValuesForKeysWithDictionary: (NSDictionary*) aDictionary;
- (void)unableToSetNilForKey: (NSString*) key;
- (void)valueForUndefinedKey: (NSString*) key;
- (void)handleTakeValue: value forUnboundKey: (NSString*) key;
- (void)setValue: value forUndefinedKey: (NSString*) key;

/* These two are only present to *disable* coding, not implement it */
- (void)encodeWithCoder:(NSCoder*)coder;
- initWithCoder:(NSCoder*)coder;

@end /* OC_PythonObject class interface */

#endif /* _OC_PythonObject_H */
