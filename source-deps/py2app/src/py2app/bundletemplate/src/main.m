//
//  main.m
//  apptemplate
//
//  Created by Bob Ippolito on Mon September 20 2004.
//  Copyright (c) 2004 Bob Ippolito. All rights reserved.
//

#import <Cocoa/Cocoa.h>
#include <mach-o/dyld.h>
#include <mach-o/loader.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/syslimits.h>
#include <crt_externs.h>

#include <objc/objc-class.h>

// XXX - tightly bound to PyObjC API
struct class_wrapper {
    struct objc_class class;
    struct objc_class meta_class;
    void* python_class;
    unsigned int magic;
};
static struct class_wrapper evil_class_wrapper __attribute__ ((section (SEG_OBJC ", __class")));

//
// Constants
//
NSString *ERR_REALLYBADTITLE = @"The bundle could not be launched.";
NSString *ERR_TITLEFORMAT = @"%@ has encountered a fatal error, and will now terminate.";
NSString *ERR_NONAME = @"The Info.plist file must have values for the CFBundleName or CFBundleExecutable strings.";
NSString *ERR_PYRUNTIMELOCATIONS = @"The Info.plist file must have a PyRuntimeLocations array containing string values for preferred Python runtime locations.  These strings should be \"otool -L\" style mach ids; \"@executable_stub\" and \"~\" prefixes will be translated accordingly.";
NSString *ERR_NOPYTHONRUNTIME = @"A Python runtime could be located.  You may need to install a framework build of Python, or edit the PyRuntimeLocations array in this bundle's Info.plist file.\rThese runtime locations were attempted:\r\r";
NSString *ERR_NOPYTHONSCRIPT = @"A main script could not be located in the Resources folder.\rThese files were tried:\r\r";
NSString *ERR_LINKERRFMT = @"An internal error occurred while attempting to link with:\r\r%s\r\rSee the Console for a detailed dyld error message";
NSString *ERR_PYTHONEXCEPTION = @"An uncaught exception was raised during execution of the main script:\r\r%@: %@\r\rThis may mean that an unexpected error has occurred, or that you do not have all of the dependencies for this bundle.\r\rSee the Console for a detailed traceback.";
NSString *ERR_DEFAULTURLTITLE = @"Visit Website";
NSString *ERR_CONSOLEAPP = @"Console.app";
NSString *ERR_CONSOLEAPPTITLE = @"Open Console";
NSString *ERR_TERMINATE = @"Terminate";
#define PYMACAPP_NSIMAGEFLAGS (NSADDIMAGE_OPTION_RETURN_ON_ERROR | NSADDIMAGE_OPTION_WITH_SEARCHING)
#define PYMACAPP_NSLOOKUPSYMBOLINIMAGEFLAGS (NSLOOKUPSYMBOLINIMAGE_OPTION_BIND | NSLOOKUPSYMBOLINIMAGE_OPTION_RETURN_ON_ERROR)
//
// Typedefs
//

typedef int PyObject;
typedef int PyGILState_STATE;
typedef PyGILState_STATE (*PyGILState_EnsurePtr)(void);
typedef void (*PyGILState_ReleasePtr)(PyGILState_STATE);
typedef void (*PyErr_ClearPtr)(void);
typedef void (*Py_DecRefPtr)(PyObject *);
typedef void (*Py_SetProgramNamePtr)(const char *);
typedef int (*Py_IsInitializedPtr)(void);
typedef void (*Py_InitializePtr)(void);
typedef void (*PyEval_InitThreadsPtr)(void);
typedef int (*PyRun_SimpleFilePtr)(FILE *, const char *);
typedef PyObject *(*PySys_GetObjectPtr)(const char *);
typedef int *(*PySys_SetArgvPtr)(int argc, char **argv);
typedef PyObject *(*PyObject_StrPtr)(PyObject *);
typedef const char *(*PyString_AsStringPtr)(PyObject *);
typedef PyObject *(*PyObject_GetAttrStringPtr)(PyObject *, const char *);

//
// Signatures
//

static void DefaultDecRef(PyObject *op);
static int report_error(NSString *err);
static int report_linkEdit_error(void);
static int report_script_error(NSString *err, NSString *errClassName, NSString *errName);
static NSString *pyStandardizePath(NSString *pyLocation);
static BOOL doesPathExist(NSString *path);
static NSString *getBundleName(void);
static NSString *getErrorTitle(NSString *bundleName);
static const char *bundlePath();
static NSBundle *bundleBundle();
static int pyobjc_main(int argc, char * const *argv, char * const *envp);
#pragma CALL_ON_LOAD _py2app_bundle_load
static void __attribute__ ((__unused__)) _py2app_bundle_load(void);

//
// Implementation
//

void *_py2app_bundle_exported_symbol;

static
const char *bundlePath() {
    struct mach_header *myHeader = _dyld_get_image_header_containing_address((unsigned long)&_py2app_bundle_exported_symbol);
    NSSymbol mySymbol = NSLookupSymbolInImage(myHeader, "__py2app_bundle_exported_symbol", NSLOOKUPSYMBOLINIMAGE_OPTION_BIND);
    NSModule myModule = NSModuleForSymbol(mySymbol);
    return NSNameOfModule(myModule);
}

static
NSBundle *bundleBundle() {
    static NSBundle *myBundle = NULL;
    if (!myBundle) {
        myBundle = [[NSBundle alloc] initWithPath:[[[[NSString stringWithUTF8String:bundlePath()] stringByDeletingLastPathComponent] stringByDeletingLastPathComponent] stringByDeletingLastPathComponent]];
    }
    return myBundle;
}

//
// THIS WILL NOT WORK WITH Py_TRACE_REFS / Py_DEBUG ON UNLESS USING 2.4 OR LATER!
//
static
void DefaultDecRef(PyObject *op) {
    if (op != NULL) {
        --(*op);
    }
}

static
int report_script_error(NSString *err, NSString *errClassName, NSString *errName) {

    NSArray *errorScripts = [[bundleBundle() infoDictionary] objectForKey:@"PyErrorScripts"];
    if ( !errorScripts )
        errorScripts = [NSArray array];
    // find main python file.  __main__.py seems to be a standard, so we'll go ahead and add defaults.
    errorScripts = [errorScripts arrayByAddingObjectsFromArray:[NSArray arrayWithObjects:
        @"__error__",
        @"__error__.py",
        @"__error__.pyc",
        @"__error__.pyo",
        @"__error__.sh",
        nil]];
    NSEnumerator *errorScriptsEnumerator = [errorScripts objectEnumerator];
    NSString *path = nil;
    NSString *nextFileName;
    
    while ((nextFileName = [errorScriptsEnumerator nextObject])) {
        path = [bundleBundle() pathForResource: nextFileName ofType: nil];
        if ( path )
            break;
    }
    
    if ( !path )
        return report_error(err);
    
    NSTask *task = [[NSTask alloc] init];
    NSPipe *stdoutPipe = [NSPipe pipe];
    [task setLaunchPath: path];
    [task setArguments: [NSArray arrayWithObjects:getBundleName(),errClassName,errName,nil]];
    [task setStandardOutput: stdoutPipe];

    NS_DURING
        [task launch];
        [task waitUntilExit];
    NS_HANDLER
        NSLog(@"Could not execute %@: %@", [path lastPathComponent], localException);
        [task release];
        return report_error(err);
    NS_ENDHANDLER

    NSData *taskData = [[stdoutPipe fileHandleForReading] readDataToEndOfFile];
    [task autorelease];
    
    if ([task terminationStatus])
        return report_error(err);
    NSString *result = [[[NSString alloc] initWithData:taskData encoding:NSUTF8StringEncoding] autorelease];
    NSArray *lines = [result componentsSeparatedByString:@"\n"];
    while ([[lines lastObject] isEqualToString: @""])
        lines = [lines subarrayWithRange:NSMakeRange(0, [lines count]-1)];
    if ( ![lines count] )
        return report_error(err);
    NSURL *buttonURL = nil;
    NSString *buttonString = nil;
        
    if ([[lines lastObject] hasPrefix:@"ERRORURL: "]) {
        NSString *lastLine = [lines lastObject];
        lines = [lines subarrayWithRange:NSMakeRange(0, [lines count]-1)];
        NSArray *buttonArr = [lastLine componentsSeparatedByString:@" "];
        buttonArr = [buttonArr subarrayWithRange:NSMakeRange(1, [buttonArr count]-1)];
        while ([[buttonArr objectAtIndex:0] isEqualToString: @""])
            buttonArr = [buttonArr subarrayWithRange:NSMakeRange(1, [buttonArr count]-1)];
        buttonURL = [NSURL URLWithString:[buttonArr objectAtIndex:0]];
        if ( buttonURL ) {
            buttonArr = [buttonArr subarrayWithRange:NSMakeRange(1, [buttonArr count]-1)];
            while ([[buttonArr objectAtIndex:0] isEqualToString: @""])
                buttonArr = [buttonArr subarrayWithRange:NSMakeRange(1, [buttonArr count]-1)];
            buttonString = [buttonArr componentsJoinedByString:@" "];
            if ( !buttonString )
                buttonString = ERR_DEFAULTURLTITLE;
        }
    }

    NSString *title = nil;
    NSString *msg = nil;
    title = [lines objectAtIndex:0];
    if ( !title )
        return report_error(err);
    
    msg = [[lines subarrayWithRange:NSMakeRange(1, [lines count]-1)] componentsJoinedByString:@"\r"];
    if ( !msg )
        msg = @"";
    
    NSLog(title);
    NSLog(msg);
    [NSApplication sharedApplication];
    if ( !buttonURL ) {
        int choice = NSRunAlertPanel(title, msg, ERR_TERMINATE, ERR_CONSOLEAPPTITLE, NULL);
        switch (choice) {
            case NSAlertAlternateReturn:
                [[NSWorkspace sharedWorkspace] launchApplication:ERR_CONSOLEAPP];
                break;
            default:
                break;
        }
    } else {
        int choice = NSRunAlertPanel(title, msg, ERR_TERMINATE, buttonString, NULL);
        switch (choice) {
            case NSAlertAlternateReturn:
                [[NSWorkspace sharedWorkspace] openURL:buttonURL];
                break;
            default:
                break;
        }
    }
    
    return -1;
}

static
int report_error(NSString *err) {
    int choice;
    [NSApplication sharedApplication];
    NSLog(err);
    choice = NSRunAlertPanel(getErrorTitle(getBundleName()), err, ERR_TERMINATE, ERR_CONSOLEAPPTITLE, NULL);
    switch (choice) {
        case NSAlertAlternateReturn:
            [[NSWorkspace sharedWorkspace] launchApplication:ERR_CONSOLEAPP];
            break;
        default:
            break;
    }
    return -1;
}

static
int report_linkEdit_error() {
    NSLinkEditErrors errorClass;
    int errorNumber;
    const char *fileName;
    const char *errorString;
    NSLinkEditError(&errorClass, &errorNumber, &fileName, &errorString);
    NSLog(@"%s", errorString);
    return report_error([NSString stringWithFormat:ERR_LINKERRFMT,fileName]);
}

static
NSString *pyStandardizePath(NSString *pyLocation) {
        if ([pyLocation hasPrefix:@"@executable_path/"]) {
            NSMutableArray *newComponents = [[pyLocation pathComponents] mutableCopy];
            [newComponents replaceObjectAtIndex:0 withObject:[bundleBundle() privateFrameworksPath]];
            pyLocation = [NSString pathWithComponents: newComponents];
        }
        return [pyLocation stringByStandardizingPath];
};

static
BOOL doesPathExist(NSString *path) {
        struct stat sb;
        return (stat([path fileSystemRepresentation], &sb) == -1) ? NO : YES;
}

static
NSString *getBundleName(void) {
    NSDictionary *infoDictionary = [bundleBundle() infoDictionary];
    NSString *bundleName = [infoDictionary objectForKey:@"CFBundleName"];
    if (!bundleName) {
        bundleName = [infoDictionary objectForKey:@"CFBundleExecutable"];
    }
    return bundleName;
}

static
NSString *getErrorTitle(NSString *bundleName) {
    if (!bundleName)
        return ERR_REALLYBADTITLE;
    return [NSString stringWithFormat:ERR_TITLEFORMAT,bundleName];
}



int pyobjc_main(int argc, char * const *argv, char * const *envp) {
   
    // I'm not going to default anything here.. explicit is better than implicit.

    // get the runtime locations from the Info.plist
    NSArray *pyLocations = [[bundleBundle() infoDictionary] objectForKey:@"PyRuntimeLocations"];
    if ( !pyLocations )
        return report_error(ERR_PYRUNTIMELOCATIONS);
    
    //  *does not* inspect DYLD environment variables for overrides, fallbacks, suffixes, etc.
    //  I don't really consider that a very bad thing, as it makes this search extremely deterministic.
    //  Note that I use the env variables when the image is actually linked, so what you find here 
    //  may not be what gets linked.  If this is the case, you deserve it :)

    // find a Python runtime
    NSString *pyLocation;
    NSEnumerator *pyLocationsEnumerator = [pyLocations objectEnumerator];
    while ((pyLocation = [pyLocationsEnumerator nextObject])) {
        pyLocation = pyStandardizePath(pyLocation);
        if ( doesPathExist(pyLocation) )
            break;
    }
    if ( !pyLocation ) {
    
        return report_script_error([ERR_NOPYTHONRUNTIME stringByAppendingString:[pyLocations componentsJoinedByString:@"\r\r"]], nil, nil);
    }
    
    NSString *pythonPath = [[[NSProcessInfo processInfo] environment] objectForKey: @"PYTHONPATH"];
    NSString *resourcePath = [bundleBundle() resourcePath];
    NSMutableArray *pythonPathArray = [NSMutableArray arrayWithObject: resourcePath];
    NSArray *pyResourcePackages = [[bundleBundle() infoDictionary] objectForKey:@"PyResourcePackages"];
    if (pyResourcePackages != nil) {
        NSEnumerator *pyResourcePackageEnumerator = [pyResourcePackages objectEnumerator];
        NSString *pkg;
        while ((pkg = [pyResourcePackageEnumerator nextObject])) {
            pkg = [pkg stringByExpandingTildeInPath];
            if (![@"/" isEqualToString: [pkg substringToIndex:1]])
                pkg = [resourcePath stringByAppendingPathComponent: pkg];
            [pythonPathArray addObject: pkg];
        }
    }
    if (pythonPath != nil)
        [pythonPathArray addObjectsFromArray: [pythonPath componentsSeparatedByString: @":"]];

    setenv("PYOBJC_BUNDLE_CLASS_WRAPPER_ADDRESS", [[NSString stringWithFormat:@"%p",&evil_class_wrapper] UTF8String], 1);
    setenv("EXECUTABLEPATH", bundlePath(), 1);
    setenv("ARGVZERO", argv[0], 1);
    setenv("RESOURCEPATH", [resourcePath fileSystemRepresentation], 1);
    
    NSArray *possibleMains = [[bundleBundle() infoDictionary] objectForKey:@"PyMainFileNames"];
    if ( !possibleMains )
        possibleMains = [NSArray array];
    // find main python file.  __main__.py seems to be a standard, so we'll go ahead and add defaults.
    possibleMains = [possibleMains arrayByAddingObjectsFromArray:[NSArray arrayWithObjects:
        @"__main__",
        @"__realmain__",
        @"Main",
        nil]];
    NSEnumerator *possibleMainsEnumerator = [possibleMains objectEnumerator];
    NSString *mainPyPath = nil;
    NSString *nextFileName = nil;
    NSString *nextExtension = nil;
    NSArray *extensions = [NSArray arrayWithObjects:@".py", @".pyc", @".pyo", @"", nil];
    
    NSMutableArray *runtimeAttempts = [NSMutableArray array];
    while ((nextFileName = [possibleMainsEnumerator nextObject])) {
        NSEnumerator *nextExtensionEnumerator = [extensions objectEnumerator];
        while ((nextExtension = [nextExtensionEnumerator nextObject])) {
            [runtimeAttempts addObject:[nextFileName stringByAppendingString:nextExtension]];
        }
    }
    possibleMainsEnumerator = [runtimeAttempts objectEnumerator];
    while ((nextFileName = [possibleMainsEnumerator nextObject]) && !mainPyPath) {
            mainPyPath = [bundleBundle() pathForResource:nextFileName ofType:nil];
    }

    if ( !mainPyPath )
        return report_error([ERR_NOPYTHONSCRIPT stringByAppendingString:[runtimeAttempts componentsJoinedByString:@"\r"]]);
    
    const struct mach_header *py_dylib = NSAddImage([pyLocation fileSystemRepresentation], PYMACAPP_NSIMAGEFLAGS);
    if ( !py_dylib ) 
        return report_linkEdit_error();
    
    NSSymbol tmpSymbol;

#define LOOKUP_SYMBOL(NAME) \
    tmpSymbol = NSLookupSymbolInImage(py_dylib, "_" #NAME, PYMACAPP_NSLOOKUPSYMBOLINIMAGEFLAGS)
#define LOOKUP_DEFINEADDRESS(NAME, ADDRESS) \
    NAME ## Ptr NAME = (NAME ## Ptr)ADDRESS
#define LOOKUP_DEFINE(NAME) \
    LOOKUP_DEFINEADDRESS(NAME, NSAddressOfSymbol(tmpSymbol))
#define LOOKUP(NAME) \
    LOOKUP_SYMBOL(NAME); \
    if ( !tmpSymbol ) \
        return report_linkEdit_error(); \
    LOOKUP_DEFINE(NAME)

    LOOKUP_SYMBOL(Py_DecRef);
    LOOKUP_DEFINEADDRESS(Py_DecRef, (tmpSymbol ? NSAddressOfSymbol(tmpSymbol) : &DefaultDecRef));
    LOOKUP(Py_SetProgramName);
    LOOKUP(Py_IsInitialized);
    LOOKUP(Py_Initialize);
    LOOKUP(PyErr_Clear);
    LOOKUP(PyGILState_Ensure);
    LOOKUP(PyGILState_Release);
    LOOKUP(PyEval_InitThreads);
    LOOKUP(PyRun_SimpleFile);
    LOOKUP(PySys_GetObject);
    LOOKUP(PySys_SetArgv);
    LOOKUP(PyObject_Str);
    LOOKUP(PyString_AsString);
    LOOKUP(PyObject_GetAttrString);

#undef LOOKUP
#undef LOOKUP_DEFINE
#undef LOOKUP_DEFINEADDRESS
#undef LOOKUP_SYMBOL

    // XXX - this value should be used!
    int __attribute__ ((__unused__)) was_initialized;
    was_initialized = Py_IsInitialized();
    NSString *pythonProgramName;
    // $PREFIX/Python -> $PREFIX
    pythonProgramName = [pyLocation stringByDeletingLastPathComponent];
    // this is the non-framework case, hopefully
    if (![[pyLocation pathExtension] isEqualToString:@""]) {
        pythonProgramName = [pythonProgramName stringByDeletingLastPathComponent];
    }

    setenv("PYTHONPATH", [[pythonPathArray componentsJoinedByString:@":"] fileSystemRepresentation], 1);
    setenv("PYTHONHOME", [pythonProgramName fileSystemRepresentation], 1);
    
    NSString *pyExecutableName = [[bundleBundle() infoDictionary] objectForKey:@"PyExecutableName"];
    if ( !pyExecutableName )
        pyExecutableName = @"python";

    pythonProgramName = [[pythonProgramName stringByAppendingPathComponent:@"bin"] stringByAppendingPathComponent:pyExecutableName];
    Py_SetProgramName([pythonProgramName fileSystemRepresentation]);

    NSMutableData *data_argv = [NSMutableData dataWithCapacity:(sizeof(char *) * argc)];
    char *c_mainPyPath = (char *)[mainPyPath fileSystemRepresentation];
    char **argv_new = [data_argv mutableBytes];
    argv_new[0] = c_mainPyPath;
    memcpy(&argv_new[1], &argv[1], (argc - 1) * sizeof(char *));
    Py_Initialize();
    PyEval_InitThreads();
    PyGILState_STATE gilState = PyGILState_Ensure();
    PySys_SetArgv(argc, argv_new);
    
    FILE *mainPy = fopen(c_mainPyPath, "r");
    int rval = PyRun_SimpleFile(mainPy, c_mainPyPath);
    fclose(mainPy);

    while ( rval ) {
        PyObject *exc = PySys_GetObject("last_type");        
        if ( !exc ) {
            rval = report_error([NSString stringWithFormat:ERR_PYTHONEXCEPTION,"<<PyMacAppException>>","The exception went away?"]);
            break;
        }

        PyObject *exceptionClassName = PyObject_GetAttrString(exc, "__name__");
        if ( !exceptionClassName ) {
            rval = report_error([NSString stringWithFormat:ERR_PYTHONEXCEPTION,"<<PyMacAppException>>","Could not get exception class name?"]);
            break;
        }
        
        PyObject *v = PySys_GetObject("last_value");
        PyObject *exceptionName = NULL;
        if ( v )
            exceptionName = PyObject_Str(v);
                
        NSString *nsExceptionClassName = [NSString stringWithCString:PyString_AsString(exceptionClassName)];
        Py_DecRef(exceptionClassName);exceptionClassName = NULL;
        NSString *nsExceptionName;
        if ( exceptionName ) {
            nsExceptionName = [NSString stringWithCString:PyString_AsString(exceptionName)];
            Py_DecRef(exceptionName);exceptionName = NULL;
        } else {
            nsExceptionName = @"";
        }
        rval = report_script_error([NSString stringWithFormat:ERR_PYTHONEXCEPTION, nsExceptionClassName, nsExceptionName], nsExceptionClassName, nsExceptionName);
        break;
    }

    PyErr_Clear();
    PyGILState_Release(gilState);

    return rval;
}


static
void _py2app_bundle_load(void)
{
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
    int argc = 1;
    char * const argv[] = { (char *)bundlePath(), NULL };
    char * const *envp = *_NSGetEnviron();
    (void)pyobjc_main(argc, argv, envp);
    [pool release];
}


