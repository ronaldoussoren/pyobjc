/*
 * This module is used in the unittests for object identity.
 */
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

@interface OC_TestFilePointer : NSObject {
}

- (FILE*)openFile:(char*)path withMode:(char*)mode;
- (FILE*)openNoFile;
- (NSString*)readline:(FILE*)fp;
@end

@implementation OC_TestFilePointer
- (FILE*)openFile:(char*)path withMode:(char*)mode
{
    return fopen(path, mode);
}

- (FILE*)openNoFile
{
    return NULL;
}

- (NSString*)readline:(FILE*)fp
{
    char buf[1024];

    if (!fp) {
        return nil;
    }

    return [NSString stringWithCString:fgets(buf, sizeof(buf), fp)
                              encoding:NSASCIIStringEncoding];
}
@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "filepointer", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_filepointer(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_filepointer(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    if (PyObjC_ImportAPI(m) < 0) {
        return NULL;
    }

    if (PyModule_AddObject(m, "OC_TestFilePointer",
                           PyObjC_IdToPython([OC_TestFilePointer class]))
        < 0) {
        return NULL;
    }

    return m;
}
