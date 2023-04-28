
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>
__attribute__((__visibility__("default")))
@interface OC_Category_GP33 : NSObject {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_P33 : OC_Category_GP33 {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_C33 : OC_Category_P33 {
}
@end

@implementation
OC_Category_GP33 (Cat)
- (id)gpMethod1
{
    return @"GP33 - gpMethod1 - GP33(Cat)";
}
- (id)gpMethod5
{
    return @"GP33 - gpMethod5 - GP33(Cat)";
}
- (id)pMethod1
{
    return @"GP33 - pMethod1 - GP33(Cat)";
}
- (id)pMethod3
{
    return @"GP33 - pMethod3 - GP33(Cat)";
}
- (id)method1
{
    return @"GP33 - method1 - GP33(Cat)";
}
- (id)method2
{
    return @"GP33 - method2 - GP33(Cat)";
}
@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "category_gp33", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_category_gp33(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_category_gp33(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    PyObjC_ImportAPI(m);

    return m;
}
