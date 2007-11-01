//
//  main.m
//  apptemplate
//
//  Created by Bob Ippolito on Mon September 20 2004.
//  Copyright (c) 2004 Bob Ippolito. All rights reserved.
//

#import <Foundation/Foundation.h>
#include <mach-o/dyld.h>
#include <mach-o/loader.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/syslimits.h>
#include <crt_externs.h>

#include <objc/objc-class.h>

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

#define Py_file_input 257
typedef int PyObject;
typedef int PyThreadState;
typedef enum {PyGILState_LOCKED, PyGILState_UNLOCKED} PyGILState_STATE;
typedef PyGILState_STATE (*PyGILState_EnsurePtr)(void);
typedef void (*PyGILState_ReleasePtr)(PyGILState_STATE);
typedef PyThreadState *(*PyThreadState_SwapPtr)(PyThreadState *);
typedef void (*PyEval_ReleaseLockPtr)(void);
typedef void (*PyErr_ClearPtr)(void);
typedef void (*PyErr_PrintPtr)(void);
typedef int (*PyErr_OccurredPtr)(void);
typedef PyObject *(*PyString_FromStringPtr)(const char *);
typedef int (*PyList_InsertPtr)(PyObject *, int, PyObject *);
typedef void (*Py_DecRefPtr)(PyObject *);
typedef void (*Py_SetProgramNamePtr)(const char *);
typedef int (*Py_IsInitializedPtr)(void);
typedef void (*Py_InitializePtr)(void);
typedef void (*PyEval_InitThreadsPtr)(void);
typedef PyObject *(*PyRun_FilePtr)(FILE *, const char *, int, PyObject *, PyObject *);
typedef PyObject *(*PySys_GetObjectPtr)(const char *);
typedef int *(*PySys_SetArgvPtr)(int argc, char **argv);
typedef PyObject *(*PyObject_StrPtr)(PyObject *);
typedef const char *(*PyString_AsStringPtr)(PyObject *);
typedef PyObject *(*PyObject_GetAttrStringPtr)(PyObject *, const char *);
typedef PyObject *(*PyImport_ImportModulePtr)(char *);
typedef PyObject *(*PyImport_AddModulePtr)(char *);
typedef PyObject *(*PyModule_AddStringConstantPtr)(PyObject *, char *, char *);
typedef PyObject *(*PyModule_AddObjectPtr)(PyObject *, char *, PyObject *);
typedef PyObject *(*PyModule_GetDictPtr)(PyObject *);
typedef void (*PyObject_SetItemPtr)(PyObject *, PyObject *, PyObject *);
typedef void (*Py_SetPythonHomePtr)(char *);

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
#if 0
#if __GNUC__ < 4
#pragma CALL_ON_LOAD _py2app_bundle_load
#endif
#endif
static void __attribute__ ((constructor)) _py2app_bundle_load(void);

//
// Implementation
//

static
const char *bundlePath() {
    int i;
    struct mach_header *myHeader = _dyld_get_image_header_containing_address((unsigned long)&bundlePath);
    int count = _dyld_image_count();
    for (i = 0; i < count; i++) {
        if (_dyld_get_image_header(i) == myHeader) {
            return _dyld_get_image_name(i);
        }
    }
    abort();
    return NULL;
}

static
NSBundle *bundleBundle() {
    static NSBundle *myBundle = NULL;
    if (!myBundle) {
        int i;
        NSString *path = [NSString stringWithUTF8String:bundlePath()];
        // strip Contents/MacOS/App
        for (i = 0; i < 3; i++) {
            path = [path stringByDeletingLastPathComponent];
        }
        myBundle = [[NSBundle alloc] initWithPath:path];
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
    return report_error(err);
}

static
int report_error(NSString *err) {
    NSLog(getErrorTitle(getBundleName()));
    NSLog(err);
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
    return report_error([NSString stringWithFormat:ERR_LINKERRFMT, fileName]);
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
    if (!bundleName) {
        return ERR_REALLYBADTITLE;
    }
    return [NSString stringWithFormat:ERR_TITLEFORMAT,bundleName];
}

static
NSString *getPythonLocation(NSArray *pyLocations) {
    // get the runtime locations from the Info.plist
    
    //  *does not* inspect DYLD environment variables for overrides, fallbacks, suffixes, etc.
    //  I don't really consider that a very bad thing, as it makes this search extremely deterministic.
    //  Note that I use the env variables when the image is actually linked, so what you find here 
    //  may not be what gets linked.  If this is the case, you deserve it :)

    // find a Python runtime
    NSString *pyLocation;
    NSEnumerator *pyLocationsEnumerator = [pyLocations objectEnumerator];
    while ((pyLocation = [pyLocationsEnumerator nextObject])) {
        pyLocation = pyStandardizePath(pyLocation);
        if (doesPathExist(pyLocation)) {
            return pyLocation;
        }
    }
    return nil;
}

static
NSArray *getPythonPathArray(NSDictionary *infoDictionary, NSString *resourcePath) {
    NSMutableArray *pythonPathArray = [NSMutableArray arrayWithObject: resourcePath];
    NSArray *pyResourcePackages = [infoDictionary objectForKey:@"PyResourcePackages"];
    if (pyResourcePackages != nil) {
        NSString *pkg;
        NSEnumerator *pyResourcePackageEnumerator = [pyResourcePackages objectEnumerator];
        while ((pkg = [pyResourcePackageEnumerator nextObject])) {
            pkg = [pkg stringByExpandingTildeInPath];
            if (![@"/" isEqualToString: [pkg substringToIndex:1]]) {
                pkg = [resourcePath stringByAppendingPathComponent:pkg];
            }
            [pythonPathArray addObject:pkg];
        }
    }
    return pythonPathArray;
}

static
NSString *getMainPyPath(NSDictionary *infoDictionary) {
    NSArray *possibleMains = [infoDictionary objectForKey:@"PyMainFileNames"];
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
    if (!mainPyPath) {
        NSString *components = [runtimeAttempts componentsJoinedByString:@"\r"];
        report_error([ERR_NOPYTHONSCRIPT stringByAppendingString:components]);
    }
    return mainPyPath;
}


int pyobjc_main(int argc, char * const *argv, char * const *envp) {
    NSDictionary *infoDictionary = [bundleBundle() infoDictionary];

    NSString *pyLocation = nil;
    while (NSIsSymbolNameDefined("_Py_Initialize")) {
        // Python is already in-process
        NSSymbol sym = NSLookupAndBindSymbol("_Py_Initialize");
        if (!sym) {
            break;
        }
        NSModule mod = NSModuleForSymbol(sym);
        if (!mod) {
            break;
        }
        const char *python_dylib_path = NSLibraryNameForModule(mod);
        if (python_dylib_path) {
            pyLocation = [NSString stringWithUTF8String:python_dylib_path];
        }
        break;
    }
    NSArray *pyLocations = [infoDictionary objectForKey:@"PyRuntimeLocations"];
    if (!pyLocation) {
        // Python is not in-process
        if (!pyLocations) {
            return report_error(ERR_PYRUNTIMELOCATIONS);
        }
        pyLocation = getPythonLocation(pyLocations);
    }
    if (!pyLocation) {
        NSString *components = [pyLocations componentsJoinedByString:@"\r\r"];
        return report_script_error([ERR_NOPYTHONRUNTIME stringByAppendingString:components], nil, nil);
    }

    // Find our resource path and possible PYTHONPATH
    NSString *resourcePath = [bundleBundle() resourcePath];
    NSArray *pythonPathArray = getPythonPathArray(infoDictionary, resourcePath);

    // find the main script
    NSString *mainPyPath = getMainPyPath(infoDictionary);
    if (!mainPyPath) {
        // error already reported
        return -1;
    }

    // Load the Python dylib (may have already been loaded, that is OK)
    const struct mach_header *py_dylib = NSAddImage([pyLocation fileSystemRepresentation], PYMACAPP_NSIMAGEFLAGS);
    if (!py_dylib) { 
        return report_linkEdit_error();
    }

    // Load the symbols we need from Python
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
    LOOKUP(PyErr_Print);
    LOOKUP(PyErr_Occurred);
    LOOKUP(PyEval_ReleaseLock);
    LOOKUP(PyGILState_Ensure);
    LOOKUP(PyGILState_Release);
    LOOKUP(PyEval_InitThreads);
    LOOKUP(PyRun_File);
    LOOKUP(PySys_GetObject);
    LOOKUP(PySys_SetArgv);
    LOOKUP(PyObject_Str);
    LOOKUP(PyString_AsString);
    LOOKUP(PyString_FromString);
    LOOKUP(PyList_Insert);
    LOOKUP(PyObject_GetAttrString);
    LOOKUP(PyImport_ImportModule);
    LOOKUP(PyImport_AddModule);
    LOOKUP(PyObject_SetItem);
    LOOKUP(PyModule_AddStringConstant);
    LOOKUP(PyModule_AddObject);
    LOOKUP(PyModule_GetDict);
    LOOKUP(PyThreadState_Swap);
    LOOKUP(Py_SetPythonHome);

#undef LOOKUP
#undef LOOKUP_DEFINE
#undef LOOKUP_DEFINEADDRESS
#undef LOOKUP_SYMBOL

    int was_initialized = Py_IsInitialized();

    
    // Set up the environment variables to be transferred
    NSMutableDictionary *newEnviron = [NSMutableDictionary dictionary];
    [newEnviron setObject:[NSString stringWithFormat:@"%p", bundleBundle()] forKey:@"PYOBJC_BUNDLE_ADDRESS"];
    [newEnviron setObject:resourcePath forKey:@"RESOURCEPATH"];
    NSMutableDictionary *oldEnviron = [NSMutableDictionary dictionary];

    // bootstrap Python with information about how to find what it needs
    // if it is not already initialized
    if (!was_initialized) {
        // $PREFIX/Python -> $PREFIX
        NSString *pythonProgramName = [pyLocation stringByDeletingLastPathComponent];

        // this is the non-framework case, hopefully
        if (![[pyLocation pathExtension] isEqualToString:@""]) {
            pythonProgramName = [pythonProgramName stringByDeletingLastPathComponent];
        }

        [newEnviron setObject:[pythonPathArray componentsJoinedByString:@":"] forKey:@"PYTHONPATH"];

        // this doesn't copy, but the NSAutoreleasePool will last long enough
        Py_SetPythonHome((char *)[pythonProgramName fileSystemRepresentation]);
        
        NSString *pyExecutableName = [infoDictionary objectForKey:@"PyExecutableName"];
        if ( !pyExecutableName ) {
            pyExecutableName = @"python";
        }

        pythonProgramName = [[pythonProgramName stringByAppendingPathComponent:@"bin"] stringByAppendingPathComponent:pyExecutableName];
        Py_SetProgramName([pythonProgramName fileSystemRepresentation]);
    }

    // Set new environment variables and save older ones (for nested plugin loading)
    NSEnumerator *envEnumerator = [newEnviron keyEnumerator];
    NSString *envKey;
    while ((envKey = [envEnumerator nextObject])) {
        char *keyString = (char *)[envKey UTF8String];
        char *oldValue = getenv(keyString);
        if (oldValue) {
            [oldEnviron setObject:[NSString stringWithUTF8String:oldValue] forKey:envKey];
        }
        setenv(keyString, (char *)[[newEnviron objectForKey:envKey] UTF8String], 1);
    }

    int rval = 0;
    FILE *mainPyFile = NULL;
    Py_Initialize();
    PyEval_InitThreads();
    PyGILState_STATE gilState = PyGILState_Ensure();

    if (was_initialized) {
        // transfer path into existing Python process
        PyObject *path = PySys_GetObject("path");
        NSEnumerator *pathEnumerator = [pythonPathArray reverseObjectEnumerator];
        NSString *curPath;
        while ((curPath = [pathEnumerator nextObject])) {
            PyObject *s = PyString_FromString([curPath UTF8String]);
            PyList_Insert(path, 0, s);
            Py_DecRef(s);
        }

        // transfer environment variables into existing Python process
        PyObject *osModule = PyImport_ImportModule("os");
        PyObject *pyenv = PyObject_GetAttrString(osModule, "environ");
        Py_DecRef(osModule);
        envEnumerator = [newEnviron keyEnumerator];
        while ((envKey = [envEnumerator nextObject])) {
            char *keyString = (char *)[envKey UTF8String];
            PyObject *key = PyString_FromString(keyString);
            PyObject *value = PyString_FromString(getenv(keyString));
            PyObject_SetItem(pyenv, key, value);
            Py_DecRef(key);
            Py_DecRef(value);
        }
        Py_DecRef(pyenv);
    }

    char *c_mainPyPath = (char *)[mainPyPath fileSystemRepresentation];
    mainPyFile = fopen(c_mainPyPath, "r");
    if (!mainPyFile) {
        rval = report_error([NSString stringWithFormat:@"Could not open main script %@",mainPyPath]);
        goto cleanup;
    }
    if (!was_initialized) {
        NSMutableData *data_argv = [NSMutableData dataWithCapacity:(sizeof(char *) * argc)];
        char **argv_new = [data_argv mutableBytes];
        argv_new[0] = c_mainPyPath;
        memcpy(&argv_new[1], &argv[1], (argc - 1) * sizeof(char *));
        PySys_SetArgv(argc, argv_new);
    }

    // create a unique moduleName by CFBundleIdentifier replacing . with _ and prepending __main__
    NSString *moduleName = [NSString stringWithFormat:@"__main__%@", [[[infoDictionary objectForKey:@"CFBundleIdentifier"] componentsSeparatedByString:@"."] componentsJoinedByString:@"_"]];
    PyObject *module = PyImport_AddModule((char *)[moduleName UTF8String]);
    if (!module) {
        rval = report_error([NSString stringWithFormat:@"Could not create module '%@'",moduleName]);
        goto cleanup;
    }
    PyModule_AddStringConstant(module, "__file__", c_mainPyPath);
    PyObject *builtins = PyImport_ImportModule("__builtin__");
    PyModule_AddObject(module, "__builtins__", builtins);
    PyObject *module_dict = PyModule_GetDict(module);
    if (PyErr_Occurred()) {
        goto cleanup;
    }

    PyObject *res = PyRun_File(mainPyFile, c_mainPyPath, Py_file_input, module_dict, module_dict);
    Py_DecRef(res);

cleanup:
    // un-transfer the environment variables
    envEnumerator = [newEnviron keyEnumerator];
    while ((envKey = [envEnumerator nextObject])) {
        char *keyString = (char *)[envKey UTF8String];
        NSString *newValue = [oldEnviron objectForKey:envKey];
        if (newValue) {
            setenv(keyString, [newValue UTF8String], 1);
        } else {
            unsetenv(keyString);
        }
    }

    if (mainPyFile) {
        fclose(mainPyFile);
    }
    if (PyErr_Occurred()) {
        rval = -1;
        PyErr_Print();
    }
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
    if (gilState == PyGILState_LOCKED) {
        PyThreadState_Swap(NULL);
        PyEval_ReleaseLock();
    }

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


