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
  [[NSAutoreleasePool alloc] init];

  const char **childArgv = alloca(sizeof(char *) * (argc + 5));
  const char *pythonBinPathPtr;
  const char *mainPyPathPtr;
  NSEnumerator *bundleEnumerator = [[NSBundle allFrameworks] reverseObjectEnumerator];
  NSBundle *aBundle;
  NSMutableArray *bundlePaths = [[NSMutableArray array] retain];
  int i;
  int envc;
  char** childEnvp;
  char*  PYTHONPATH = NULL;

  for (envc = 0; envp[envc] != NULL; envc++) {
  	if (strncmp(envp[envc], "PYTHONPATH=", sizeof("PYTHONPATH=")-1) == 0) {
		PYTHONPATH=envp[envc] + sizeof("PYTHONPATH=") - 1;
		/* No break, we also want to know how large envp is */
	}
  } 

  childEnvp = alloca(sizeof(char*) * (envc + 2));
  for (envc = 0; envp[envc] != NULL; envc ++) {
  	if (strncmp(envp[envc], "PYTHONPATH=", sizeof("PYTHONPATH=")-1) == 0) {
		const char* s = [[[NSBundle mainBundle] resourcePath] UTF8String];
		childEnvp[envc] = alloca(strlen(envp[envc]) + strlen(s) + 2);
		sprintf(childEnvp[envc], "%s:%s", envp[envc], s);

	} else {
		childEnvp[envc] = envp[i];
	}
  }
  if (PYTHONPATH) {
	envp[envc] = NULL;
  } else {
	const char* s = [[[NSBundle mainBundle] resourcePath] UTF8String];
	childEnvp[envc] = alloca(sizeof("PYTHONPATH=") + strlen(s));
	sprintf(childEnvp[envc], "PYTHONPATH=%s", s);
	childEnvp[envc+1] = NULL;
  }


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

  i = execve(pythonBinPathPtr, (char **)childArgv, (char**) childEnvp);
  if (i == -1) perror("execv");
  return 1;
}

int main(int argc, char * const *argv, char *envp[])
{
  return pyobjc_main(argc, argv, envp);
}
