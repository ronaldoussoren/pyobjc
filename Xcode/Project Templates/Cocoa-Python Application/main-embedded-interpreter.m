#import <Python/Python.h>
#import <Foundation/Foundation.h>
#import <Cocoa/Cocoa.h>
#import <sys/param.h>

int pyobjc_main(int argc, const char *argv[])
{
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
    NSString *pythonBinPath = [[NSUserDefaults standardUserDefaults] stringForKey: @"PythonBinPath"];
    
    NSString *pythonPath = [[[NSProcessInfo processInfo] environment] objectForKey: @"PYTHONPATH"];
    NSString *resourcePath = [[NSBundle mainBundle] resourcePath];
    NSMutableArray *pythonPathArray = [NSMutableArray arrayWithObjects: resourcePath, [resourcePath stringByAppendingPathComponent:@"PyObjC"], nil];
    
    if (pythonPath != nil)
        [pythonPathArray addObjectsFromArray: [pythonPath componentsSeparatedByString: @":"]];

    setenv("PYTHONPATH", [[pythonPathArray componentsJoinedByString:@":"] UTF8String], 1);

    pythonBinPath = pythonBinPath ? pythonBinPath : @"/usr/bin/python";
    [pythonBinPath retain];
    Py_SetProgramName((char *)[pythonBinPath cString]);
    Py_Initialize();

    // find main python file.  __main__.py seems to be a standard.
    NSArray *possibleMains = [NSArray arrayWithObjects:
        @"__main__.py",
        @"__main__.pyc",
        @"__main__.pyo",
        @"__realmain__.py",
        @"__realmain__.pyc",
        @"__realmain__.pyo",
        @"Main.py",
        @"Main.pyc",
        @"Main.pyo",
        nil];
    NSEnumerator *possibleMainsEnumerator = [possibleMains objectEnumerator];
    NSString *mainPyPath = nil;
    NSString *nextFileName;

    while (nextFileName = [possibleMainsEnumerator nextObject]) {
        mainPyPath = [[NSBundle mainBundle] pathForResource: nextFileName ofType: nil];
        if ( mainPyPath )
            break;
    }

    if ( !mainPyPath )
        [NSException raise: NSInternalInconsistencyException
                    format: @"%s:%d pyobjc_main() Failed to find one of %@ in app wrapper.  Exiting.", __FILE__, __LINE__, possibleMains];
    const char *mainPyPathPtr = [mainPyPath UTF8String];

    FILE *mainPy = fopen(mainPyPathPtr, "r");
    int result = PyRun_SimpleFile(mainPy, (char *)[[mainPyPath lastPathComponent] cString]);

    if ( result != 0 )
        [NSException raise: NSInternalInconsistencyException
                    format: @"%s:%d pyobjc_main() PyRun_SimpleFile failed with file '%@'.  See console for errors.", __FILE__, __LINE__, mainPyPath];

    [pool release];

    return result;
}

int main(int argc, const char *argv[])
{
    return pyobjc_main(argc, argv);
}
