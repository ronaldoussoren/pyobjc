
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>
__attribute__((__visibility__("default")))
@interface OC_Category_GP42 : NSObject {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_P42 : OC_Category_GP42 {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_C42 : OC_Category_P42 {
}
@end

@implementation OC_Category_GP42 (Cat)
- (id)gpMethod1
{
    return @"GP42 - gpMethod1 - GP42(Cat)";
}
- (id)gpMethod5
{
    return @"GP42 - gpMethod5 - GP42(Cat)";
}
- (id)pMethod1
{
    return @"GP42 - pMethod1 - GP42(Cat)";
}
- (id)pMethod3
{
    return @"GP42 - pMethod3 - GP42(Cat)";
}
- (id)method1
{
    return @"GP42 - method1 - GP42(Cat)";
}
- (id)method2
{
    return @"GP42 - method2 - GP42(Cat)";
}
@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "category_gp42", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_category_gp42(void);

PyObject* __attribute__((__visibility__("default")))
PyInit_category_gp42(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    if (PyObjC_ImportAPI(m) < 0) { // LCOV_BR_EXCL_LINE
        return NULL;               // LCOV_EXCL_LINE
    }

    return m;
}
