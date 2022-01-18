#include "pyobjc.h"
/*
 * XXX: Is this code still needed?
 *      The code isn't used on macOS 12, haven't checked
 *      older macOS versions yet.
 */

NS_ASSUME_NONNULL_BEGIN

/* This code is never used on systems I use for coverage testing */
// LCOV_EXCL_START

static void
nsmaptable_objc_retain(NSMapTable* table __attribute__((__unused__)), const void* datum)
{
    CFRetain((id)datum);
}

static void
nsmaptable_objc_release(NSMapTable* table __attribute__((__unused__)), void* datum)
{
    CFRelease((id)datum);
}

static NSMapTableValueCallBacks PyObjC_ObjCValueCallBacks = {
    &nsmaptable_objc_retain, &nsmaptable_objc_release,
    NULL // generic description
};

static id (*bundleForClassIMP)(id, SEL, Class) = nil;

@implementation OC_NSBundleHackCheck
+ (NSBundle* _Nullable)bundleForClass
{
    return [NSBundle bundleForClass:[NSObject class]];
}
@end

@implementation OC_NSBundleHack
+ (NSBundle*)bundleForClass:(Class)aClass
{
    static NSBundle*   mainBundle  = nil;
    static NSMapTable* bundleCache = nil;
    id                 rval;

    if (unlikely(!mainBundle)) {
        mainBundle = [[NSBundle mainBundle] retain];
    }

    if (unlikely(!bundleCache)) {
        bundleCache =
            NSCreateMapTable(PyObjCUtil_PointerKeyCallBacks, PyObjC_ObjCValueCallBacks,
                             PYOBJC_EXPECTED_CLASS_COUNT);
    }

    if (!aClass) {
        return mainBundle;
    }

    rval = (id)NSMapGet(bundleCache, (const void*)aClass);
    if (rval) {
        return rval;
    }

    rval = bundleForClassIMP(self, @selector(bundleForClass:), aClass);
    if (rval == mainBundle) {
        Class base_isa     = aClass;
        Class nsobject_isa = object_getClass([NSObject class]);

        while (base_isa != nsobject_isa) {
            Class next_isa = object_getClass(base_isa);
            if (!next_isa || next_isa == base_isa) {
                break;
            }

            base_isa = next_isa;
        }

        if (base_isa == nsobject_isa) {
            if ([(id)aClass respondsToSelector:@selector(bundleForClass)]) {
                rval = [(id)aClass performSelector:@selector(bundleForClass)];
            }
        }
    }

    NSMapInsert(bundleCache, (const void*)aClass, (const void*)rval);
    return rval;
}

static const char BUNDLE_FOR_CLASS_SIGNATURE[] = {_C_ID, _C_ID, _C_SEL, _C_CLASS, 0};

+ (void)installBundleHack
{
    if ([[NSBundle bundleForClass:[NSObject class]]
            isEqual:[NSBundle bundleForClass:[OC_NSBundleHackCheck class]]]) {
        // implementation is already correct
        return;
    }

    bundleForClassIMP =
        (id(*)(id, SEL, Class))[NSBundle methodForSelector:@selector(bundleForClass:)];

    Method method = class_getInstanceMethod(object_getClass([NSBundle class]),
                                            @selector(bundleForClass:));

    if (method == NULL) {
        class_addMethod(object_getClass([NSBundle class]), @selector(bundleForClass:),
                        [self methodForSelector:@selector(bundleForClass:)],
                        BUNDLE_FOR_CLASS_SIGNATURE);
    } else {
        method_setImplementation(method,
                                 [self methodForSelector:@selector(bundleForClass:)]);
    }
}

+ (BOOL)bundleHackUsed
{
    return (bundleForClassIMP != nil);
}

@end

// LCOV_EXCL_STOP

NS_ASSUME_NONNULL_END
