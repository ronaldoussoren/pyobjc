#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

@implementation OC_BuiltinPythonNumber

/*
 * This method is never actually used by the Foundation
 * framework because ``-[OC_PythonNumber classForArchiver]``
 * returns ``NSNumber`` for all values that are proxied
 * using ``OC_BuiltinPythonNumber``.
 *
 * I'm leaving this method in just in case there is a
 * valid usecase for this.
 */
// LCOV_EXCL_START
+ (BOOL)supportsSecureCoding
{
    return YES;
}
// LCOV_EXCL_STOP

+ (NSArray*)classFallbacksForKeyedArchiver
{
    return [NSArray arrayWithObjects:@"OC_PythonNumber", @"NSNumber", nil];
}

@end

NS_ASSUME_NONNULL_END
