
/*
 *     *** GENERATED FILE ***
 *
 * This file is generated by Tools/generate-category-tests.py
 */
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>
__attribute__((__visibility__("default")))
@interface OC_Category_GP19 : NSObject {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_P19 : OC_Category_GP19 {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_C19 : OC_Category_P19 {
}
@end

@implementation
OC_Category_GP19 (Cat)
- (id)gpMethod1
{
    return @"GP19 - gpMethod1 - GP19(Cat)";
}
- (id)gpMethod5
{
    return @"GP19 - gpMethod5 - GP19(Cat)";
}
- (id)pMethod1
{
    return @"GP19 - pMethod1 - GP19(Cat)";
}
- (id)pMethod3
{
    return @"GP19 - pMethod3 - GP19(Cat)";
}
- (id)method1
{
    return @"GP19 - method1 - GP19(Cat)";
}
- (id)method2
{
    return @"GP19 - method2 - GP19(Cat)";
}
@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "category_gp19", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_category_gp19(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_category_gp19(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    PyObjC_ImportAPI(m);

    return m;
}
