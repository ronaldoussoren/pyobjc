
/*
 *     *** GENERATED FILE ***
 *
 * This file is generated by Tools/generate-category-tests.py
 */
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>
__attribute__((__visibility__("default")))
@interface OC_Category_GP18 : NSObject {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_P18 : OC_Category_GP18 {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_C18 : OC_Category_P18 {
}
@end

@implementation
OC_Category_GP18 (Cat)
- (id)gpMethod1
{
    return @"GP18 - gpMethod1 - GP18(Cat)";
}
- (id)gpMethod5
{
    return @"GP18 - gpMethod5 - GP18(Cat)";
}
- (id)pMethod1
{
    return @"GP18 - pMethod1 - GP18(Cat)";
}
- (id)pMethod3
{
    return @"GP18 - pMethod3 - GP18(Cat)";
}
- (id)method1
{
    return @"GP18 - method1 - GP18(Cat)";
}
- (id)method2
{
    return @"GP18 - method2 - GP18(Cat)";
}
@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "category_gp18", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_category_gp18(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_category_gp18(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    PyObjC_ImportAPI(m);

    return m;
}
