
/*
 *     *** GENERATED FILE ***
 *
 * This file is generated by Tools/generate-category-tests.py
 */
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>
__attribute__((__visibility__("default")))
@interface OC_Category_GP52 : NSObject {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_P52 : OC_Category_GP52 {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_C52 : OC_Category_P52 {
}
@end

@implementation
OC_Category_C52 (Cat)
- (id)gpMethod1
{
    return @"C52 - gpMethod1 - C52(Cat)";
}
- (id)gpMethod5
{
    return @"C52 - gpMethod5 - C52(Cat)";
}
- (id)pMethod1
{
    return @"C52 - pMethod1 - C52(Cat)";
}
- (id)pMethod3
{
    return @"C52 - pMethod3 - C52(Cat)";
}
- (id)method1
{
    return @"C52 - method1 - C52(Cat)";
}
- (id)method2
{
    return @"C52 - method2 - C52(Cat)";
}
@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "category_c52", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_category_c52(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_category_c52(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    PyObjC_ImportAPI(m);

    return m;
}
