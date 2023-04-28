
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>
__attribute__((__visibility__("default")))
@interface OC_Category_GP48 : NSObject {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_P48 : OC_Category_GP48 {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_C48 : OC_Category_P48 {
}
@end

@implementation
OC_Category_GP48 (Cat)
- (id)gpMethod1
{
    return @"GP48 - gpMethod1 - GP48(Cat)";
}
- (id)gpMethod5
{
    return @"GP48 - gpMethod5 - GP48(Cat)";
}
- (id)pMethod1
{
    return @"GP48 - pMethod1 - GP48(Cat)";
}
- (id)pMethod3
{
    return @"GP48 - pMethod3 - GP48(Cat)";
}
- (id)method1
{
    return @"GP48 - method1 - GP48(Cat)";
}
- (id)method2
{
    return @"GP48 - method2 - GP48(Cat)";
}
@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "category_gp48", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_category_gp48(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_category_gp48(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    PyObjC_ImportAPI(m);

    return m;
}
