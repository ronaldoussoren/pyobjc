
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>
__attribute__((__visibility__("default")))
@interface OC_Category_GP54 : NSObject {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_P54 : OC_Category_GP54 {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_C54 : OC_Category_P54 {
}
@end

@implementation
OC_Category_GP54 (Cat)
- (id)gpMethod1
{
    return @"GP54 - gpMethod1 - GP54(Cat)";
}
- (id)gpMethod5
{
    return @"GP54 - gpMethod5 - GP54(Cat)";
}
- (id)pMethod1
{
    return @"GP54 - pMethod1 - GP54(Cat)";
}
- (id)pMethod3
{
    return @"GP54 - pMethod3 - GP54(Cat)";
}
- (id)method1
{
    return @"GP54 - method1 - GP54(Cat)";
}
- (id)method2
{
    return @"GP54 - method2 - GP54(Cat)";
}
@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "category_gp54", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_category_gp54(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_category_gp54(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    PyObjC_ImportAPI(m);

    return m;
}
