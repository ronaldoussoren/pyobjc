//
//  main.m
//  ÇPROJECTNAMEÈ
//
//  Created by ÇFULLUSERNAMEÈ on ÇDATEÈ.
//  Copyright (c) ÇYEARÈ ÇORGANIZATIONNAMEÈ. All rights reserved.
//

#import <Cocoa/Cocoa.h>
#include <mach-o/dyld.h>
#include <sys/types.h>
#include <sys/stat.h>

//
// Constants
//
NSString *ERR_REALLYBADTITLE = @"The application could not be launched.";
NSString *ERR_TITLEFORMAT = @"%@ has encountered a fatal error, and will now terminate.";
NSString *ERR_NONAME = @"The Info.plist file must have values for the CFBundleName or CFBundleExecutable strings.";
NSString *ERR_PYRUNTIMELOCATIONS = @"The Info.plist file must have a PyRuntimeLocations array containing string values for preferred Python runtime locations.  These strings should be \"otool -L\" style mach ids; \"@executable_stub\" and \"~\" prefixes will be translated accordingly.";
NSString *ERR_NOPYTHONRUNTIME = @"A Python runtime could be located.  You may need to install a framework build of Python, or edit the PyRuntimeLocations array in this application's Info.plist file.\rThese runtime locations were attempted:\r\r";
NSString *ERR_NOPYTHONSCRIPT = @"A main script could not be located in the Resources folder.\rThese files were tried:\r\r";
NSString *ERR_LINKERRFMT = @"An internal error occurred while attempting to link with:\r\r%s\r\rSee the Console for a detailed dyld error message";
NSString *ERR_PYTHONEXCEPTION = @"An uncaught exception was raised during execution of the main script:\r\r%@: %@\r\rThis may mean that an unexpected error has occurred, or that you do not have all of the dependencies for this application.\r\rSee the Console for a detailed traceback.";
NSString *ERR_DEFAULTURLTITLE = @"Visit Website";
NSString *ERR_CONSOLEAPP = @"Console.app";
NSString *ERR_CONSOLEAPPTITLE = @"Open Console";
NSString *ERR_TERMINATE = @"Terminate";
#define PYMACAPP_NSIMAGEFLAGS (NSADDIMAGE_OPTION_RETURN_ON_ERROR | NSADDIMAGE_OPTION_WITH_SEARCHING)
#define PYMACAPP_NSLOOKUPSYMBOLINIMAGEFLAGS (NSLOOKUPSYMBOLINIMAGE_OPTION_BIND | NSLOOKUPSYMBOLINIMAGE_OPTION_RETURN_ON_ERROR)
//
// THIS WILL NOT WORK WITH Py_TRACE_REFS / Py_DEBUG ON!!! WARNING!!
//
#define Py_XDECREF(op) if ((op) == NULL) ; else --(*op)

//
// Typedefs
//

typedef int PyObject;
typedef void (*Py_SetProgramNamePtr)(const char *);
typedef void (*Py_InitializePtr)(void);
typedef int (*PyRun_SimpleFilePtr)(FILE *, const char *);
typedef void (*Py_FinalizePtr)(void);
typedef PyObject *(*PySys_GetObjectPtr)(const char *);
typedef PyObject *(*PyObject_StrPtr)(PyObject *);
typedef const char *(*PyString_AsStringPtr)(PyObject *);
typedef PyObject *(*PyObject_GetAttrStringPtr)(PyObject *, const char *);

//
// Signatures
//

int report_error(NSString *err);
int report_linkEdit_error(void);
int report_script_error(NSString *err, NSString *errClassName, NSString *errName);
NSString *pyStandardizePath(NSString *pyLocation);
BOOL doesPathExist(NSString *path);
NSString *getApplicationName(void);
NSString *getErrorTitle(NSString *applicationName);
int pyobjc_main(int argc, char * const *argv, char * const *envp);
int main(int argc, char * const *argv, char * const *envp);


//
// Implementation
//

int report_script_error(NSString *err, NSString *errClassName, NSString *errName) {

	NSArray *errorScripts = [[[NSBundle mainBundle] infoDictionary] objectForKey:@"PyErrorScripts"];
	if ( !errorScripts )
		errorScripts = [NSArray array];
	// find main python file.  __main__.py seems to be a standard, so we'll go ahead and add defaults.
	errorScripts = [errorScripts arrayByAddingObjectsFromArray:[NSArray arrayWithObjects:
		@"__error__",
		@"__error__.py",
		@"__error__.sh",
		nil]];
	NSEnumerator *errorScriptsEnumerator = [errorScripts objectEnumerator];
	NSString *path = nil;
	NSString *nextFileName;
	
	while (nextFileName = [errorScriptsEnumerator nextObject]) {
		path = [[NSBundle mainBundle] pathForResource: nextFileName ofType: nil];
		if ( path )
			break;
	}
	
	if ( !path )
		return report_error(err);
	
	NSTask *task = [[NSTask alloc] init];
	NSPipe *stdoutPipe = [NSPipe pipe];
	[task setLaunchPath: path];
	[task setArguments: [NSArray arrayWithObjects:getApplicationName(),errClassName,errName,nil]];
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

int report_error(NSString *err) {
	int choice;
	[NSApplication sharedApplication];
	NSLog(err);
	choice = NSRunAlertPanel(getErrorTitle(getApplicationName()), err, ERR_TERMINATE, ERR_CONSOLEAPPTITLE, NULL);
	switch (choice) {
		case NSAlertAlternateReturn:
			[[NSWorkspace sharedWorkspace] launchApplication:ERR_CONSOLEAPP];
			break;
		default:
			break;
	}
	return -1;
}

int report_linkEdit_error() {
	NSLinkEditErrors errorClass;
	int errorNumber;
	const char *fileName;
	const char *errorString;
	NSLinkEditError(&errorClass, &errorNumber, &fileName, &errorString);
	NSLog(@"%s", errorString);
	return report_error([NSString stringWithFormat:ERR_LINKERRFMT,fileName]);
}


NSString *pyStandardizePath(NSString *pyLocation) {
		if ([pyLocation hasPrefix:@"@executable_path/"]) {
			NSMutableArray *newComponents = [[pyLocation pathComponents] mutableCopy];
			[newComponents replaceObjectAtIndex:0 withObject:[[NSBundle mainBundle] privateFrameworksPath]];
			pyLocation = [NSString pathWithComponents: newComponents];
		}
		return [pyLocation stringByStandardizingPath];
};

BOOL doesPathExist(NSString *path) {
		struct stat sb;
		return (stat([path fileSystemRepresentation], &sb) == -1) ? NO : YES;
}


NSString *getApplicationName(void) {
	NSDictionary *infoDictionary = [[NSBundle mainBundle] infoDictionary];
	NSString *applicationName = [infoDictionary objectForKey:@"CFBundleName"];
	if (!applicationName) {
		applicationName = [infoDictionary objectForKey:@"CFBundleExecutable"];
	}
	return applicationName;
}

NSString *getErrorTitle(NSString *applicationName) {
	if (!applicationName)
		return ERR_REALLYBADTITLE;
	return [NSString stringWithFormat:ERR_TITLEFORMAT,applicationName];
}



int pyobjc_main(int argc, char * const *argv, char * const *envp) {
	// little sanity check.
	if ( !getApplicationName() )
		return report_error(ERR_NONAME);
	
	
	// XXX - I'm not going to default anything here.. explicit is better than implicit.

	// get the runtime locations from the Info.plist
	NSArray *pyLocations = [[[NSBundle mainBundle] infoDictionary] objectForKey:@"PyRuntimeLocations"];
	if ( !pyLocations )
		return report_error(ERR_PYRUNTIMELOCATIONS);
	
	// XXX - *does not* inspect DYLD environment variables for overrides, fallbacks, suffixes, etc.
	//		 I don't really consider that a very bad thing, as it makes this search extremely deterministic.
	//		 Note that I use the env variables when the image is actually linked, so what you find here 
	//		 may not be what gets linked.  If this is the case, you deserve it :)

	// find a Python runtime
	NSString *pyLocation;
	NSEnumerator *pyLocationsEnumerator = [pyLocations objectEnumerator];
	while (pyLocation = [pyLocationsEnumerator nextObject]) {
		pyLocation = pyStandardizePath(pyLocation);
		if ( doesPathExist(pyLocation) )
			break;
	}
	if ( !pyLocation ) {
	
		return report_script_error([ERR_NOPYTHONRUNTIME stringByAppendingString:[pyLocations componentsJoinedByString:@"\r\r"]], nil, nil);
	}
	
	NSString *pythonPath = [[[NSProcessInfo processInfo] environment] objectForKey: @"PYTHONPATH"];
    NSString *resourcePath = [[NSBundle mainBundle] resourcePath];
    NSMutableArray *pythonPathArray = [NSMutableArray arrayWithObjects: resourcePath, [resourcePath stringByAppendingPathComponent:@"PyObjC"], nil];
	if (pythonPath != nil)
        [pythonPathArray addObjectsFromArray: [pythonPath componentsSeparatedByString: @":"]];
    
	// I *refuse* to set dirty DYLD environment variables..  
	// If you want that, you'll have to do it in your main script or fork this bootstrap ;)
	//
    setenv("PYTHONPATH", [[pythonPathArray componentsJoinedByString:@":"] UTF8String], 1);
	
	NSArray *possibleMains = [[[NSBundle mainBundle] infoDictionary] objectForKey:@"PyMainFileNames"];
	if ( !possibleMains )
		possibleMains = [NSArray array];
	// find main python file.  __main__.py seems to be a standard, so we'll go ahead and add defaults.
    possibleMains = [possibleMains arrayByAddingObjectsFromArray:[NSArray arrayWithObjects:
        @"__main__.py",
        @"__main__.pyc",
        @"__main__.pyo",
        @"__realmain__.py",
        @"__realmain__.pyc",
        @"__realmain__.pyo",
        @"Main.py",
        @"Main.pyc",
        @"Main.pyo",
        nil]];
    NSEnumerator *possibleMainsEnumerator = [possibleMains objectEnumerator];
    NSString *mainPyPath = nil;
    NSString *nextFileName;
	
    while (nextFileName = [possibleMainsEnumerator nextObject]) {
        mainPyPath = [[NSBundle mainBundle] pathForResource: nextFileName ofType: nil];
        if ( mainPyPath )
            break;
    }

	if ( !mainPyPath )
		return report_error([ERR_NOPYTHONSCRIPT stringByAppendingString:[possibleMains componentsJoinedByString:@"\r"]]);
	
	const struct mach_header *py_dylib = NSAddImage([pyLocation fileSystemRepresentation], PYMACAPP_NSIMAGEFLAGS);
	if ( !py_dylib ) 
		return report_linkEdit_error();
	
	NSSymbol tmpSymbol;

	tmpSymbol = NSLookupSymbolInImage(py_dylib, "_Py_SetProgramName", PYMACAPP_NSLOOKUPSYMBOLINIMAGEFLAGS);
	if ( !tmpSymbol ) 
		return report_linkEdit_error();
	Py_SetProgramNamePtr Py_SetProgramName = (Py_SetProgramNamePtr)NSAddressOfSymbol(tmpSymbol);
	
	tmpSymbol = NSLookupSymbolInImage(py_dylib, "_Py_Initialize", PYMACAPP_NSLOOKUPSYMBOLINIMAGEFLAGS);
	if ( !tmpSymbol ) 
		return report_linkEdit_error();
	Py_InitializePtr Py_Initialize = (Py_InitializePtr)NSAddressOfSymbol(tmpSymbol);

	tmpSymbol = NSLookupSymbolInImage(py_dylib, "_PyRun_SimpleFile", PYMACAPP_NSLOOKUPSYMBOLINIMAGEFLAGS);
	if ( !tmpSymbol )
		return report_linkEdit_error();
	PyRun_SimpleFilePtr PyRun_SimpleFile = (PyRun_SimpleFilePtr)NSAddressOfSymbol(tmpSymbol);
	
	tmpSymbol = NSLookupSymbolInImage(py_dylib, "_Py_Finalize", PYMACAPP_NSLOOKUPSYMBOLINIMAGEFLAGS);
	if ( !tmpSymbol ) 
		return report_linkEdit_error();
	Py_FinalizePtr Py_Finalize = (Py_FinalizePtr)NSAddressOfSymbol(tmpSymbol);
	
	tmpSymbol = NSLookupSymbolInImage(py_dylib, "_PySys_GetObject", PYMACAPP_NSLOOKUPSYMBOLINIMAGEFLAGS);
	if ( !tmpSymbol ) 
		return report_linkEdit_error();
	PySys_GetObjectPtr PySys_GetObject = (PySys_GetObjectPtr)NSAddressOfSymbol(tmpSymbol);

	tmpSymbol = NSLookupSymbolInImage(py_dylib, "_PyObject_Str", PYMACAPP_NSLOOKUPSYMBOLINIMAGEFLAGS);
	if ( !tmpSymbol ) 
		return report_linkEdit_error();
	PyObject_StrPtr PyObject_Str = (PyObject_StrPtr)NSAddressOfSymbol(tmpSymbol);

	tmpSymbol = NSLookupSymbolInImage(py_dylib, "_PyString_AsString", PYMACAPP_NSLOOKUPSYMBOLINIMAGEFLAGS);
	if ( !tmpSymbol ) 
		return report_linkEdit_error();
	PyString_AsStringPtr PyString_AsString = (PyString_AsStringPtr)NSAddressOfSymbol(tmpSymbol);

	tmpSymbol = NSLookupSymbolInImage(py_dylib, "_PyObject_GetAttrString", PYMACAPP_NSLOOKUPSYMBOLINIMAGEFLAGS);
	if ( !tmpSymbol ) 
		return report_linkEdit_error();
	PyObject_GetAttrStringPtr PyObject_GetAttrString = (PyObject_GetAttrStringPtr)NSAddressOfSymbol(tmpSymbol);

	NSString *pythonProgramName;
	// XXX - this is NOT tested with dylib builds.. but it might work if you do things "right"
	if ([[[pyLocation stringByDeletingLastPathComponent] lastPathComponent] isEqualToString:@"lib"]) {
		// $PREFIX/lib/python.dylib -> $PREFIX
		pythonProgramName = [[pyLocation stringByDeletingLastPathComponent] stringByDeletingLastPathComponent];
	} else {
		// $PREFIX/Python -> $PREFIX
		pythonProgramName = [pyLocation stringByDeletingLastPathComponent];
	}
	
	
	// Python might not copy the strings, and some evil code may not create a new NSAutoreleasePool.
	// Who knows.  We retain things just in case...	
	NSString *pyExecutableName = [[[NSBundle mainBundle] infoDictionary] objectForKey:@"PyExecutableName"];
	if ( !pyExecutableName )
		pyExecutableName = @"python";

	pythonProgramName = [[[pythonProgramName stringByAppendingPathComponent:@"bin"] stringByAppendingPathComponent:pyExecutableName] retain];
	Py_SetProgramName([pythonProgramName fileSystemRepresentation]);
	Py_Initialize();
	
	FILE *mainPy = fopen([[mainPyPath retain] fileSystemRepresentation], "r");
	NSString *scriptName = [mainPyPath lastPathComponent];
	int rval = PyRun_SimpleFile(mainPy, [[scriptName retain] cString]);
	fclose(mainPy);
	[scriptName release];
	[mainPyPath release];
	
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
		Py_XDECREF(exceptionClassName);exceptionClassName = NULL;
		NSString *nsExceptionName;
		if ( exceptionName ) {
			nsExceptionName = [NSString stringWithCString:PyString_AsString(exceptionName)];
			Py_XDECREF(exceptionName);exceptionName = NULL;
		} else {
			nsExceptionName = @"";
		}
		rval = report_script_error([NSString stringWithFormat:ERR_PYTHONEXCEPTION, nsExceptionClassName, nsExceptionName], nsExceptionClassName, nsExceptionName);
		break;
	}
	Py_Finalize();

	[pythonProgramName release];
	
	return rval;
}


int main(int argc, char * const *argv, char * const *envp)
{
	NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
	int rval = pyobjc_main(argc, argv, envp);
	[pool release];
	return rval;
}