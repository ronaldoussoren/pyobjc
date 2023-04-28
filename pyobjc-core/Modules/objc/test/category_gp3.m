
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>
__attribute__((__visibility__("default")))
@interface OC_Category_GP3 : NSObject {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_P3 : OC_Category_GP3 {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_C3 : OC_Category_P3 {
}
@end

@implementation
OC_Category_GP3 (Cat)
- (id)gpMethod1
{
    return @"GP3 - gpMethod1 - GP3(Cat)";
}
- (id)gpMethod5
{
    return @"GP3 - gpMethod5 - GP3(Cat)";
}
- (id)pMethod1
{
    return @"GP3 - pMethod1 - GP3(Cat)";
}
- (id)pMethod3
{
    return @"GP3 - pMethod3 - GP3(Cat)";
}
- (id)method1
{
    return @"GP3 - method1 - GP3(Cat)";
}
- (id)method2
{
    return @"GP3 - method2 - GP3(Cat)";
}
@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "category_gp3", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_category_gp3(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_category_gp3(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    PyObjC_ImportAPI(m);

    return m;
}
