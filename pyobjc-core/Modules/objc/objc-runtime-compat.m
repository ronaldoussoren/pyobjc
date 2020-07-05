/*
 * Objective-C runtime 2.0 compatibility for MacOS X 10.4 and earlier.
 *
 * This code works by poking into the ObjC runtime, which means loads of
 * warnings on 10.5+ ;-)
 */

#define PYOBJC_COMPAT_IMPL
#include "pyobjc.h"


BOOL
PyObjC_class_isSubclassOf(Class child, Class parent)
{
    if (parent == nil)
        return YES;

    while (child != nil) {
        if (child == parent) {
            return YES;
        }

        child = class_getSuperclass(child);
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

/* XXX: This should not be neccessary */
#undef protocol_getMethodDescription
struct objc_method_description
PyObjC_protocol_getMethodDescription(Protocol* p, SEL aSel, BOOL isRequiredMethod,
                                     BOOL isInstanceMethod)
{
    struct objc_method_description result =
        protocol_getMethodDescription(p, aSel, isRequiredMethod, isInstanceMethod);
    if (result.name != NULL) {
        return result;
    }

    {
        /* This code should not be necessary....
         *
         * for some reason the protocols created by PyObjC don't always work, without this
         * function test_protocol.py sometimes (but not always!) fails.
         */

        struct objc_method_description* methods;
        unsigned int                    count, i;
        methods = protocol_copyMethodDescriptionList(p, isRequiredMethod,
                                                     isInstanceMethod, &count);
        if (methods == NULL) {
            return result;
        }

        for (i = 0; i < count; i++) {
            if (sel_isEqual(methods[i].name, aSel)) {
                result = methods[i];
                free(methods);
                return result;
            }
        }
        free(methods);
        return result;
    }
}

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

            } else {
                return NO;
            }
        }
    }
    return YES;
}

