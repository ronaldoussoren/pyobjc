#error The project does not use this file.  It is left here both for reference purposes (if anyone is interested in going the embedded interpreter route) and in case Apple ships the Python library in OS X (the embedded interpreter is actually more efficient). 

/*
 This main file can be used in cases where the developer desires to embed the python interpreter directly into the application.   The pyobjc_main() function initializes the python interpreter in an embedded context.

 This is useful if the application has a mix of ObjC and Python.  The ObjC can be compiled/linked without having to load a series of bundles (which is considerably slower than launching a normal application).

 The point is somewhat moot in that the PyObjC module has to dynamically load the AppKit and related frameworks anyway.

 As of 10.2.1 [6d52], This style of build will not work with the python supplied with OS X as Apple did not provide a python library or framework to link against.
 */

#import <Python.h>
#import <Foundation/Foundation.h>
#import <Cocoa/Cocoa.h>
#import <sys/param.h>

int pyobjc_main(int argc, const char *argv[])
{
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
    NSString *pythonBinPath = [[NSUserDefaults standardUserDefaults] stringForKey: @"PythonBinPath"];

    pythonBinPath = pythonBinPath ? pythonBinPath : @"/usr/bin/python";
    [pythonBinPath retain];
    Py_SetProgramName((char *)[pythonBinPath cString]);
    Py_Initialize();

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

    FILE *mainPy = fopen([mainPyPath cString], "r");
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
