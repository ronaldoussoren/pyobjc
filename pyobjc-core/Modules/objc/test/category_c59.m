
/*
 *     *** GENERATED FILE ***
 *
 * This file is generated by Tools/generate-category-tests.py
 */
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>
__attribute__((__visibility__("default")))
@interface OC_Category_GP59 : NSObject {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_P59 : OC_Category_GP59 {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_C59 : OC_Category_P59 {
}
@end

@implementation
OC_Category_C59 (Cat)
- (id)gpMethod1
{
    return @"C59 - gpMethod1 - C59(Cat)";
}
- (id)gpMethod5
{
    return @"C59 - gpMethod5 - C59(Cat)";
}
- (id)pMethod1
{
    return @"C59 - pMethod1 - C59(Cat)";
}
- (id)pMethod3
{
    return @"C59 - pMethod3 - C59(Cat)";
}
- (id)method1
{
    return @"C59 - method1 - C59(Cat)";
}
- (id)method2
{
    return @"C59 - method2 - C59(Cat)";
}
@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "category_c59", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_category_c59(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_category_c59(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    PyObjC_ImportAPI(m);

    return m;
}
