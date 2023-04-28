
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>
__attribute__((__visibility__("default")))
@interface OC_Category_GP39 : NSObject {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_P39 : OC_Category_GP39 {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_C39 : OC_Category_P39 {
}
@end

@implementation
OC_Category_GP39 (Cat)
- (id)gpMethod1
{
    return @"GP39 - gpMethod1 - GP39(Cat)";
}
- (id)gpMethod5
{
    return @"GP39 - gpMethod5 - GP39(Cat)";
}
- (id)pMethod1
{
    return @"GP39 - pMethod1 - GP39(Cat)";
}
- (id)pMethod3
{
    return @"GP39 - pMethod3 - GP39(Cat)";
}
- (id)method1
{
    return @"GP39 - method1 - GP39(Cat)";
}
- (id)method2
{
    return @"GP39 - method2 - GP39(Cat)";
}
@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "category_gp39", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_category_gp39(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_category_gp39(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    PyObjC_ImportAPI(m);

    return m;
}
