
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>
__attribute__((__visibility__("default")))
@interface OC_Category_GP30 : NSObject {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_P30 : OC_Category_GP30 {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_C30 : OC_Category_P30 {
}
@end

@implementation
OC_Category_GP30 (Cat)
- (id)gpMethod1
{
    return @"GP30 - gpMethod1 - GP30(Cat)";
}
- (id)gpMethod5
{
    return @"GP30 - gpMethod5 - GP30(Cat)";
}
- (id)pMethod1
{
    return @"GP30 - pMethod1 - GP30(Cat)";
}
- (id)pMethod3
{
    return @"GP30 - pMethod3 - GP30(Cat)";
}
- (id)method1
{
    return @"GP30 - method1 - GP30(Cat)";
}
- (id)method2
{
    return @"GP30 - method2 - GP30(Cat)";
}
@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "category_gp30", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_category_gp30(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_category_gp30(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    PyObjC_ImportAPI(m);

    return m;
}
