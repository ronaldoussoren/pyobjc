/* Copyright (c) 1996,97 by Lele Gaifax.  All Rights Reserved
 *
 * This software may be used and distributed freely for any purpose
 * provided that this notice is included unchanged on any and all
 * copies. The author does not warrant or guarantee this software in
 * any way.
 *
 * This file is part of the PyObjC package.
 *
 * RCSfile: OC_PythonString.h,v
 * Revision: 1.8
 * Date: 1998/01/04 17:59:21
 *
 * Created Thu Sep  5 19:46:45 1996.
 */

#ifndef _OC_PythonString_H
#define _OC_PythonString_H

#include "OC_PythonObject.h"

/*#C This class wraps a PyString object, making it easier to handle this
  kind of objects from Objective-C.  */
@interface OC_PythonString : OC_PythonObject
{
}

/*#M Returns a new autoreleased PyString object with @var{str} of
  length @var{size} as contents. */
+ (id <PythonObject>) fromString:(char *) str andSize:(int) size;

//#M Returns a new autoreleased PyString object with @var{str} as contents.
+ (id <PythonObject>) fromString:(char *) str;

//#M Returns the size of the string.
- (int) size;

//#M Returns the ``C'' equivalent.
- (char *) asString;

@end /* OC_PythonString class interface */


#endif /* _OC_PythonString_H */
