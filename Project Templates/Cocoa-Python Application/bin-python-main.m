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

int pyobjc_main(int argc, char * const *argv, char * const *envp)
{
  // The autorelease pool is not released on purpose.   The call to execve() destroys the
  // calling process entirely and, as such, memory management in the traditional sense
  // is not necessary (and not doing so avoids potential bugs associated with releasing
  // the pool prior to the call to execve).
  [[NSAutoreleasePool alloc] init];

  const char **childArgv = alloca(sizeof(char *) * (argc + 5));
  char **childEnvp = (char **)envp;
  NSEnumerator *bundleEnumerator = [[NSBundle allFrameworks] reverseObjectEnumerator];
  NSBundle *aBundle;
  NSBundle *mainBundle = [NSBundle mainBundle];
  NSMutableArray *bundlePaths = [NSMutableArray array];
  int i;

  // if this is set, it is most likely because of PBX or because the developer is doing something....
  if ( !getenv("DYLD_FRAMEWORK_PATH") ) {
    // if not, put the DYLD environment into a state where we can actually load frameworks from within the app
    // wrapper where the frameworks may have inter-dependencies.
    NSArray *paths = [NSArray arrayWithObjects: [mainBundle sharedFrameworksPath], [mainBundle privateFrameworksPath], nil];
    NSString *joinedPaths = [paths componentsJoinedByString: @":"];
    const char *dyldFrameworkPath = [[NSString stringWithFormat: @"DYLD_FRAMEWORK_PATH=%@", joinedPaths] UTF8String];
    const char *dyldLibraryPath = [[NSString stringWithFormat: @"DYLD_LIBRARY_PATH=%@", joinedPaths] UTF8String];

    for(i=0; envp[i]; i++);
    childEnvp = malloc( sizeof(char *) * (i+4) );

    bcopy( envp, childEnvp, ( i * sizeof(char *) ) );

    childEnvp[i++] = (char *)dyldFrameworkPath;
    childEnvp[i++] = (char *)dyldLibraryPath;

    // useful for debugging-- set this as a default.
    if ([[NSUserDefaults standardUserDefaults] boolForKey: @"DYLD_PRINT_LIBRARIES"])
      childEnvp[i++] = (char *)"DYLD_PRINT_LIBRARIES=1";
    childEnvp[i++] = NULL;
  }

  // grab a list of all frameworks that were linked into this executable
  while ( aBundle = [bundleEnumerator nextObject] ) {
    if ( [[[aBundle bundlePath] pathExtension] isEqualToString: @"framework"] )
      [bundlePaths addObject: [aBundle bundlePath]];
  }

  // figure out which python interpreter to use
  NSString *pythonBinPath = [[NSUserDefaults standardUserDefaults] stringForKey: @"PythonBinPath"];
  pythonBinPath = pythonBinPath ? pythonBinPath : @"/usr/bin/python";

  const char *pythonBinPathPtr = [pythonBinPath UTF8String];

  // find main python file.  __main__.py seems to be a standard.
  NSString *mainPyPath = [mainBundle pathForResource: @"__main__.py" ofType: nil];
  if ( !mainPyPath )
    [NSException raise: NSInternalInconsistencyException
                format: @"%s:%d pyobjc_main() Failed to find file __main__.py in app wrapper.  Exiting.", __FILE__, __LINE__];
  const char *mainPyPathPtr = [mainPyPath UTF8String];

  // construct argv for the child

  // the path to the executable in the app wrapper -- must be in the app wrapper or CFBundle does not initialize correctly
  childArgv[0] = argv[0];

  // path to the python file that acts as the main entry point
  childArgv[1] = mainPyPathPtr;

  // Pass original arguments (such as -NSOpen) verbatum
  //
  // Move each argument right one slot
  for (i = 1; i<argc; i++)
    childArgv[i+1] = argv[i];
  i++; // compensate for i+1 in for() loop

  // add an argument that lists all frameworks
  childArgv[i++] = "-PyFrameworkPaths";
  childArgv[i++] = [[bundlePaths componentsJoinedByString: @":"] UTF8String];

  // terminate the arg list
  childArgv[i++] = NULL;

  // print a nice debugging helper message, if desired
  if ([[[NSProcessInfo processInfo] environment] objectForKey: @"SHOWPID"])
    NSLog(@"Process ID is: %d (\n\tgdb %s %d\n to debug)", getpid(), pythonBinPathPtr, getpid());

  // pass control to the python interpreter
  return execve(pythonBinPathPtr, (char **)childArgv, childEnvp);
}

int main(int argc, char * const *argv, char * const *envp)
{
  return pyobjc_main(argc, argv, envp);
}
