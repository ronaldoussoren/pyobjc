
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>
__attribute__((__visibility__("default")))
@interface OC_Category_GP27 : NSObject {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_P27 : OC_Category_GP27 {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_C27 : OC_Category_P27 {
}
@end

@implementation
OC_Category_GP27 (Cat)
- (id)gpMethod1
{
    return @"GP27 - gpMethod1 - GP27(Cat)";
}
- (id)gpMethod5
{
    return @"GP27 - gpMethod5 - GP27(Cat)";
}
- (id)pMethod1
{
    return @"GP27 - pMethod1 - GP27(Cat)";
}
- (id)pMethod3
{
    return @"GP27 - pMethod3 - GP27(Cat)";
}
- (id)method1
{
    return @"GP27 - method1 - GP27(Cat)";
}
- (id)method2
{
    return @"GP27 - method2 - GP27(Cat)";
}
@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "category_gp27", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_category_gp27(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_category_gp27(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    PyObjC_ImportAPI(m);

    return m;
}
