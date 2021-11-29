#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

@implementation OC_BuiltinPythonNumber

/* XXX: Never actually used because OC_PythonNumber uses
 * NSNumber for archiving for those instances that can
 * be represented by an NSNumber, resulting in the system
 * never using this method.
 */
+ (BOOL)supportsSecureCoding
{
    return YES;
}

+ (NSArray*)classFallbacksForKeyedArchiver
{
    return [NSArray arrayWithObjects:@"OC_PythonNumber", @"NSNumber", nil];
}

@end

NS_ASSUME_NONNULL_END
