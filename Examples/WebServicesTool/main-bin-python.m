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
  [[NSAutoreleasePool alloc] init];

  const char **childArgv = alloca(sizeof(char *) * (argc + 5));
  char **childEnvp = (char **)envp;
  const char *pythonBinPathPtr;
  const char *mainPyPathPtr;
  NSEnumerator *bundleEnumerator = [[NSBundle allFrameworks] reverseObjectEnumerator];
  NSBundle *aBundle;
  NSBundle *mainBundle = [NSBundle mainBundle];
  NSMutableArray *bundlePaths = [NSMutableArray array];
  int i;

  if ( !getenv("DYLD_FRAMEWORK_PATH") ) {
    NSArray *paths = [NSArray arrayWithObjects: [mainBundle sharedFrameworksPath], [mainBundle privateFrameworksPath], nil];
    NSString *joinedPaths = [paths componentsJoinedByString: @":"];
    const char *dyldFrameworkPath = [[NSString stringWithFormat: @"DYLD_FRAMEWORK_PATH=%@", joinedPaths] UTF8String];
    const char *dyldLibraryPath = [[NSString stringWithFormat: @"DYLD_LIBRARY_PATH=%@", joinedPaths] UTF8String];

    for(i=0; envp[i]; i++);
    childEnvp = malloc( sizeof(char *) * (i+5) );

    bcopy( envp, childEnvp, ( i * sizeof(char *) ) );

    childEnvp[i++] = (char *)dyldFrameworkPath;
    childEnvp[i++] = (char *)dyldLibraryPath;
    //!    childEnvp[i++] = "DYLD_NO_FIX_PREBINDING=1";  Can't decide if this is a good idea.
    if ([[NSUserDefaults standardUserDefaults] boolForKey: @"DYLD_PRINT_LIBRARIES"])
      childEnvp[i++] = (char *)"DYLD_PRINT_LIBRARIES=1";
    childEnvp[i++] = NULL;
  }

  while ( aBundle = [bundleEnumerator nextObject] ) {
    if ( [[[aBundle bundlePath] pathExtension] isEqualToString: @"framework"] )
      [bundlePaths addObject: [aBundle bundlePath]];
  }

  NSString *pythonBinPath = [[NSUserDefaults standardUserDefaults] stringForKey: @"PythonBinPath"];
  pythonBinPath = pythonBinPath ? pythonBinPath : @"/usr/bin/python";
  pythonBinPathPtr = [pythonBinPath UTF8String];

  NSString *mainPyFile = [[mainBundle infoDictionary] objectForKey: @"PrincipalPythonFile"];
  NSString *mainPyPath = nil;

  if (mainPyFile)
    mainPyPath = [mainBundle pathForResource: mainPyFile ofType: nil];

  if ( !mainPyPath )
    mainPyPath = [mainBundle pathForResource: @"Main.py" ofType: nil];

  if ( !mainPyPath )
    [NSException raise: NSInternalInconsistencyException
                format: @"%s:%d pyobjc_main() Failed to find main python entry point for application.  Exiting.", __FILE__, __LINE__];
  mainPyPathPtr = [mainPyPath UTF8String];

  childArgv[0] = argv[0];
  childArgv[1] = mainPyPathPtr;
  for (i = 1; i<argc; i++)
    childArgv[i+1] = argv[i];
  childArgv[i+1] = "-PyFrameworkPaths";
  childArgv[i+2] = [[bundlePaths componentsJoinedByString: @":"] UTF8String];
  childArgv[i+3] = NULL;

  if ([[[NSProcessInfo processInfo] environment] objectForKey: @"SHOWPID"])
    NSLog(@"Process ID is: %d (\n\tgdb %s %d\n to debug)", getpid(), pythonBinPathPtr, getpid());

  return execve(pythonBinPathPtr, (char **)childArgv, childEnvp);
}

int main(int argc, char * const *argv, char * const *envp)
{
  return pyobjc_main(argc, argv, envp);
}
