/*
 * Objective-C runtime 2.0 compatibility for MacOS X 10.4 and earlier.
 *
 * This code works by poking into the ObjC runtime, which means loads of
 * warnings on 10.5+ ;-)
 */

#define PYOBJC_COMPAT_IMPL
#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

BOOL
PyObjC_class_isSubclassOf(Class child, Class parent)
{
    Class _Nullable cur = child;

    while (cur != nil) {
        if (cur == parent) {
            return YES;
        }

        cur = class_getSuperclass(cur);
    }
    return NO;
}

#if defined(__x86_64__)

/* XXX: Is this not needed for arm64? */

@implementation
Protocol (NSObjectCompat)
- (id)self
{
    return self;
}
@end

#endif /* __x86_64__ */

BOOL
PyObjC_class_addMethodList(Class cls, struct PyObjC_method* list, unsigned int count)
{
    unsigned int i;
    BOOL         r;
    Method       m;

    for (i = 0; i < count; i++) {
        /*
         * First try class_addMethod, if that fails assume this is
         * because the method already exists in the class.
         * Strictly speaking this isn't correct, but this is the best
         * we can do through the 2.0 API (see 4809039 in RADAR)
         */
        r = class_addMethod(cls, list[i].name, list[i].imp, list[i].type);
        if (!r) {
            m = class_getInstanceMethod(cls, list[i].name);

            if (m != NULL) {
                method_setImplementation(m, list[i].imp);

            } else { // LCOV_BR_EXCL_LINE
                /* I don't know how to trigger this */
                return NO; // LCOV_EXCL_LINE
            }
        }
    }
    return YES;
}

NS_ASSUME_NONNULL_END
