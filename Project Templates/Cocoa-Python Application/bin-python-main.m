//
//  bin-python-main.m
//  ÇPROJECTNAMEÈ
//
//  Created by ÇFULLUSERNAMEÈ on ÇDATEÈ.
//  Copyright (c) ÇYEARÈ ÇORGANIZATIONNAMEÈ. All rights reserved.
//

/*
 This main file uses execve() to transfer control of execution to the standard command line python interpreter.   As such, compiled classes in the project will not actually be linked into the runtime as execve() effectively overlays the existing process with the process being called -- in this case the python command line tool.

 To use compiled classes with this main, create a separate bundle target and load the bundle in the Main.py file.

 This style of execution works with the Apple provided version of Python.
 */

#import <Foundation/Foundation.h>
#import <sys/param.h>
#import <unistd.h>

int pyobjc_main(int argc, char * const *argv, char *envp[])
{
  // The autorelease pool is not released on purpose.   The call to execve() destroys the
  // calling process entirely and, as such, memory management in the traditional sense
  // is not necessary (and not doing so avoids potential bugs associated with releasing
  // the pool prior to the call to execve).
  [[NSAutoreleasePool alloc] init];

  const char **childArgv = alloca(sizeof(char *) * (argc + 5));
  const char *pythonBinPathPtr;
  const char *mainPyPathPtr;
  NSEnumerator *bundleEnumerator = [[NSBundle allFrameworks] reverseObjectEnumerator];
  NSBundle *aBundle;
  NSMutableArray *bundlePaths = [[NSMutableArray array] retain];
  int i;

  while ( aBundle = [bundleEnumerator nextObject] ) {
    if ( [[[aBundle bundlePath] pathExtension] isEqualToString: @"framework"] )
      [bundlePaths addObject: [aBundle bundlePath]];
  }

  NSString *pythonBinPath = [[NSUserDefaults standardUserDefaults] stringForKey: @"PythonBinPath"];
  pythonBinPath = pythonBinPath ? pythonBinPath : @"/usr/bin/python";
  [pythonBinPath retain];
  pythonBinPathPtr = [pythonBinPath UTF8String];

  NSString *mainPyFile = [[[NSBundle mainBundle] infoDictionary] objectForKey: @"PrincipalPythonFile"];
  NSString *mainPyPath = nil;

  if (mainPyFile)
    mainPyPath = [[NSBundle mainBundle] pathForResource: mainPyFile ofType: nil];

  if ( !mainPyPath )
    mainPyPath = [[NSBundle mainBundle] pathForResource: @"Main.py" ofType: nil];

  if ( !mainPyPath )
    [NSException raise: NSInternalInconsistencyException
                format: @"%s:%d pyobjc_main() Failed to find main python entry point for application.  Exiting.", __FILE__, __LINE__];
  [mainPyPath retain];
  mainPyPathPtr = [mainPyPath UTF8String];

  childArgv[0] = argv[0];
  childArgv[1] = mainPyPathPtr;
  for (i = 1; i<argc; i++)
    childArgv[i+1] = argv[i];
  childArgv[i+1] = "-PyFrameworkPaths";
  childArgv[i+2] = [[bundlePaths componentsJoinedByString: @":"] UTF8String];
  childArgv[i+3] = NULL;

  return execve(pythonBinPathPtr, (char **)childArgv, envp);
}

int main(int argc, char * const *argv, char *envp[])
{
  return pyobjc_main(argc, argv, envp);
}
