/* Copyright (c) 1996,97 by Lele Gaifax.  All Rights Reserved
 *
 * This software may be used and distributed freely for any purpose
 * provided that this notice is included unchanged on any and all
 * copies. The author does not warrant or guarantee this software in
 * any way.
 *
 * This file is part of the PyObjC package.
 *
 * RCSfile: OC_PythonBundle.h,v
 * Revision: 1.8
 * Date: 1998/08/18 15:35:50
 *
 * Created Wed Oct 16 17:35:05 1996.
 * Thanx to Bill Bumgarner for the idea and first implementation.
 */

#ifndef _OC_PythonBundle_H
#define _OC_PythonBundle_H

#import <Foundation/NSBundle.h>

/*#C This class fills specific Python needs about bundles. */  
@interface OC_PythonBundle : NSBundle
{
}

//#M Initialize the version number of this class.
+ (void) initialize;

/*#M Find the name of the main script in  execution, and return a
  bundle relative to the script's pathname; if we are in interactive
  mode, a bundle on the current working directory is returned. */
+ (NSBundle *) mainBundle;

@end

#endif /* _OC_PythonBundle_H */
