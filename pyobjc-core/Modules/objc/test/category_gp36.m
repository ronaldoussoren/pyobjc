
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>
__attribute__((__visibility__("default")))
@interface OC_Category_GP36 : NSObject {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_P36 : OC_Category_GP36 {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_C36 : OC_Category_P36 {
}
@end

@implementation
OC_Category_GP36 (Cat)
- (id)gpMethod1
{
    return @"GP36 - gpMethod1 - GP36(Cat)";
}
- (id)gpMethod5
{
    return @"GP36 - gpMethod5 - GP36(Cat)";
}
- (id)pMethod1
{
    return @"GP36 - pMethod1 - GP36(Cat)";
}
- (id)pMethod3
{
    return @"GP36 - pMethod3 - GP36(Cat)";
}
- (id)method1
{
    return @"GP36 - method1 - GP36(Cat)";
}
- (id)method2
{
    return @"GP36 - method2 - GP36(Cat)";
}
@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "category_gp36", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_category_gp36(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_category_gp36(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    PyObjC_ImportAPI(m);

    return m;
}
