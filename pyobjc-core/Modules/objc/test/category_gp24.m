
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>
__attribute__((__visibility__("default")))
@interface OC_Category_GP24 : NSObject {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_P24 : OC_Category_GP24 {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_C24 : OC_Category_P24 {
}
@end

@implementation
OC_Category_GP24 (Cat)
- (id)gpMethod1
{
    return @"GP24 - gpMethod1 - GP24(Cat)";
}
- (id)gpMethod5
{
    return @"GP24 - gpMethod5 - GP24(Cat)";
}
- (id)pMethod1
{
    return @"GP24 - pMethod1 - GP24(Cat)";
}
- (id)pMethod3
{
    return @"GP24 - pMethod3 - GP24(Cat)";
}
- (id)method1
{
    return @"GP24 - method1 - GP24(Cat)";
}
- (id)method2
{
    return @"GP24 - method2 - GP24(Cat)";
}
@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "category_gp24", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_category_gp24(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_category_gp24(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    PyObjC_ImportAPI(m);

    return m;
}
