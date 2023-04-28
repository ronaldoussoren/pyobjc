
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>
__attribute__((__visibility__("default")))
@interface OC_Category_GP45 : NSObject {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_P45 : OC_Category_GP45 {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_C45 : OC_Category_P45 {
}
@end

@implementation
OC_Category_GP45 (Cat)
- (id)gpMethod1
{
    return @"GP45 - gpMethod1 - GP45(Cat)";
}
- (id)gpMethod5
{
    return @"GP45 - gpMethod5 - GP45(Cat)";
}
- (id)pMethod1
{
    return @"GP45 - pMethod1 - GP45(Cat)";
}
- (id)pMethod3
{
    return @"GP45 - pMethod3 - GP45(Cat)";
}
- (id)method1
{
    return @"GP45 - method1 - GP45(Cat)";
}
- (id)method2
{
    return @"GP45 - method2 - GP45(Cat)";
}
@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "category_gp45", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_category_gp45(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_category_gp45(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    PyObjC_ImportAPI(m);

    return m;
}
