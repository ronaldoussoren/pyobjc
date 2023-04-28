
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>
__attribute__((__visibility__("default")))
@interface OC_Category_GP57 : NSObject {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_P57 : OC_Category_GP57 {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_C57 : OC_Category_P57 {
}
@end

@implementation
OC_Category_GP57 (Cat)
- (id)gpMethod1
{
    return @"GP57 - gpMethod1 - GP57(Cat)";
}
- (id)gpMethod5
{
    return @"GP57 - gpMethod5 - GP57(Cat)";
}
- (id)pMethod1
{
    return @"GP57 - pMethod1 - GP57(Cat)";
}
- (id)pMethod3
{
    return @"GP57 - pMethod3 - GP57(Cat)";
}
- (id)method1
{
    return @"GP57 - method1 - GP57(Cat)";
}
- (id)method2
{
    return @"GP57 - method2 - GP57(Cat)";
}
@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "category_gp57", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_category_gp57(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_category_gp57(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    PyObjC_ImportAPI(m);

    return m;
}
