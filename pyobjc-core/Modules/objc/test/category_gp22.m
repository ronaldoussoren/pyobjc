
/*
 *     *** GENERATED FILE ***
 *
 * This file is generated by Tools/generate-category-tests.py
 */
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>
__attribute__((__visibility__("default")))
@interface OC_Category_GP22 : NSObject {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_P22 : OC_Category_GP22 {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_C22 : OC_Category_P22 {
}
@end

@implementation
OC_Category_GP22 (Cat)
- (id)gpMethod1
{
    return @"GP22 - gpMethod1 - GP22(Cat)";
}
- (id)gpMethod5
{
    return @"GP22 - gpMethod5 - GP22(Cat)";
}
- (id)pMethod1
{
    return @"GP22 - pMethod1 - GP22(Cat)";
}
- (id)pMethod3
{
    return @"GP22 - pMethod3 - GP22(Cat)";
}
- (id)method1
{
    return @"GP22 - method1 - GP22(Cat)";
}
- (id)method2
{
    return @"GP22 - method2 - GP22(Cat)";
}
@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "category_gp22", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_category_gp22(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_category_gp22(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    PyObjC_ImportAPI(m);

    return m;
}
