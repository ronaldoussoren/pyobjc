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

@implementation Protocol (NSObjectCompat)
- (id)self
{
    return self;
}
@end

#endif /* __x86_64__ */

void
PyObjC_class_addMethodList(Class cls, struct PyObjC_method* list, unsigned int count)
{
    unsigned int i;

    for (i = 0; i < count; i++) {
        /* class_replaceMethod returns the current IMP or NULL,
         * but doesn't indicate if it was successful
         */
        (void)class_replaceMethod(cls, list[i].name, list[i].imp, list[i].type);
    }
}

NS_ASSUME_NONNULL_END
