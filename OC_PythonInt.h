/* Copyright (c) 1996,97 by Lele Gaifax.  All Rights Reserved
 *
 * This software may be used and distributed freely for any purpose
 * provided that this notice is included unchanged on any and all
 * copies. The author does not warrant or guarantee this software in
 * any way.
 *
 * This file is part of the PyObjC package.
 *
 * RCSfile: OC_PythonInt.h,v
 * Revision: 1.8
 * Date: 1998/01/04 17:59:16
 *
 * Created Thu Sep  5 20:28:35 1996.
 */

#ifndef _OC_PythonInt_H
#define _OC_PythonInt_H

#include "OC_PythonObject.h"

/*#C This class wraps a PyInt object, making it easier to handle this
  kind of objects from Objective-C. */
@interface OC_PythonInt : OC_PythonObject
{
}

//#M Initialize the version number of this class.
+ (void) initialize;

//#M Returns a new autoreleased PyInt object with @var{i} as contents.
+ (id <PythonObject>) fromLong:(long) i;

//#M Returns the ``C'' equivalent.
- (long) asLong;

@end /* OC_PythonInt class interface */


#endif /* _OC_PythonInt_H */
