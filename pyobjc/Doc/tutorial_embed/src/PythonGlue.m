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