/* Copyright (c) 1996,97 by Lele Gaifax.  All Rights Reserved
 *
 * This software may be used and distributed freely for any purpose
 * provided that this notice is included unchanged on any and all
 * copies. The author does not warrant or guarantee this software in
 * any way.
 *
 * This file is part of the PyObjC package.
 *
 * RCSfile: OC_PythonString.m,v
 * Revision: 1.9
 * Date: 1998/01/04 17:59:22
 *
 * Created Thu Sep  5 19:49:36 1996.
 */

#include "OC_PythonString.h"

@implementation OC_PythonString

+ (id <PythonObject>) fromString:(char *) str andSize:(int) size
{
	PyObject *pystr = PyString_FromStringAndSize (str, size);
	id <PythonObject> result = [self newWithObject:pystr];

	Py_DECREF(pystr);
	return result;
}

+ (id <PythonObject>) fromString:(char *) str
{
	PyObject *pystr = PyString_FromString(str);
	id <PythonObject> result = [self newWithObject:pystr];

	Py_DECREF(pystr);
	return result;
}

- (int) size
{
	return PyString_Size([self pyObject]);
}

- (char *) asString
{
	return PyString_AsString([self pyObject]);
}

@end /* OC_PythonString class implementation */
