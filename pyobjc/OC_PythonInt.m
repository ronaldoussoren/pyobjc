/* Copyright (c) 1996,97 by Lele Gaifax.  All Rights Reserved
 *
 * This software may be used and distributed freely for any purpose
 * provided that this notice is included unchanged on any and all
 * copies. The author does not warrant or guarantee this software in
 * any way.
 *
 * This file is part of the PyObjC package.
 *
 * RCSfile: OC_PythonInt.m,v
 * Revision: 1.9
 * Date: 1998/01/04 17:59:17
 *
 * Created Thu Sep  5 20:29:52 1996.
 */

#include "OC_PythonInt.h"

#define CLASS_VERSION 0

@implementation OC_PythonInt
+ (void) initialize
{
/*
  // NSProxy does not implement +setVersion:
  if (self == [OC_PythonInt class])
    {
      [OC_PythonInt setVersion:CLASS_VERSION];
    }
*/
}

+ (id <PythonObject>) fromLong:(long) i
{
  PyObject *pyint = PyInt_FromLong (i);
  id <PythonObject> result = [self newWithObject:pyint];

  Py_DECREF(pyint);
  return result;
}

- (long) asLong
{
  return PyInt_AsLong ([self pyObject]);
}


@end /* OC_PythonInt class implementation */
