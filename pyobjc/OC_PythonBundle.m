/* Copyright (c) 1996,97 by Lele Gaifax.  All Rights Reserved
 *
 * This software may be used and distributed freely for any purpose
 * provided that this notice is included unchanged on any and all
 * copies. The author does not warrant or guarantee this software in
 * any way.
 *
 * This file is part of the PyObjC package.
 *
 * RCSfile: OC_PythonBundle.m,v
 * Revision: 1.8
 * Date: 1998/08/18 15:35:51
 *
 * Created Wed Oct 16 17:39:54 1996.
 */

#include "ObjC.h"
#include "OC_PythonBundle.h"

#import <Foundation/NSString.h> /* sdm7g -- chg #include to #import */

#include "Python.h"
#include "compile.h"
#include "frameobject.h"

#include <sys/param.h>

#define CLASS_VERSION 0

@implementation OC_PythonBundle

+ (void) initialize
{
  if (self == [OC_PythonBundle class])
    {
      [OC_PythonBundle setVersion:CLASS_VERSION];
    }
}

+ (NSBundle *) mainBundle
{
  static NSBundle *mainScriptBundle = nil;

  if (!mainScriptBundle)
    {
      PyFrameObject *frame = (PyFrameObject *) PyEval_GetFrame();
      const char *mainscript;

      /* go back to the first frame */
      while (frame->f_back)
        frame = frame->f_back;
      
      mainscript = PyString_AsString (frame->f_code->co_filename);
      if (strcmp (mainscript, "<stdin>"))
        {
          const char *lslash = strrchr (mainscript, '/');
          
          if (lslash)
            {
              unsigned int len = lslash - mainscript;
              char pathbuf[len + 1];

              memcpy (pathbuf, mainscript, len);
              pathbuf[len] = 0;

              mainScriptBundle = [NSBundle alloc];
              [mainScriptBundle initWithPath:
                                  [NSString stringWithCString:pathbuf]];
            }
        }

      if (!mainScriptBundle)
        {
          char cwdbuf[1024];
          extern const char *getcwd (char *, unsigned int);
          
          if (getcwd (cwdbuf, sizeof (cwdbuf)))
            {
              mainScriptBundle = [NSBundle alloc];
              [mainScriptBundle initWithPath:
                                  [NSString stringWithCString:cwdbuf]];
            }
        }
    }

  return mainScriptBundle;
}

@end /* OC_PythonBundle class implementation */
