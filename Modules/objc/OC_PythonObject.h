/* Copyright (c) 1996,97 by Lele Gaifax.  All Rights Reserved
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
 */

#ifndef _OC_PythonObject_H
#define _OC_PythonObject_H

#include <Python.h>
#import <Foundation/NSProxy.h>
#import <Foundation/NSMethodSignature.h>


@interface OC_PythonObject : NSProxy 
{
  PyObject *pyObject;
}

+ newWithObject:(PyObject *) obj;
- initWithObject:(PyObject *) obj;
- (PyObject*) pyObject;
- (PyObject*) __pyobjc_PythonObject__;
- (void) forwardInvocation:(NSInvocation *) invocation;
- (BOOL) respondsToSelector:(SEL) aSelector;
- (NSMethodSignature *) methodSignatureForSelector:(SEL) selector;
- (void) doesNotRecognizeSelector:(SEL) aSelector;

@end /* OC_PythonObject class interface */

#endif /* _OC_PythonObject_H */
