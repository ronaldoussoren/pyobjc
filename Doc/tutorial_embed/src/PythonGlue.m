/*
PythonGlue is a class implementing a singleton object that does
nothing, but it has one side effect: it initializes Python (which
should be linked into the bundle containing this class) and executes
Contents/Resourcs/PythonGlue.py from the main bundle.

No error checking is done, but Python errors will result in messages
on standard error (or the console, for programs started from the Finder).
*/

#import <Foundation/Foundation.h>
#import "PythonGlue.h"
#import <Python/Python.h>
#import <stdio.h>

@implementation PythonGlue

- init
{
    static id _singleton;
    NSString *path;
    const char *c_path;
    FILE *fp;
    
    if (_singleton) return _singleton;
    _singleton = self;
    path = [[[NSBundle mainBundle] resourcePath] 
              stringByAppendingPathComponent: @"PythonGlue.py"];
    c_path = [path cString];
    if ((fp=fopen(c_path, "r")) == NULL) {
        perror(c_path);
        return self;
    }
    Py_Initialize();
    PyRun_SimpleFile(fp, c_path);
    return self;
}

@end