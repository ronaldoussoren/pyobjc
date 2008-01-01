/*!
 * @header   OC_NSBundleHack.h 
 * @abstract NSBundle hacks to support plugins
 * @discussion
 *     This file defines the class that is used to convince NSBundle
 *     that it should do the right thing for Python classes.
 */

#import "pyobjc.h"
#import <Foundation/Foundation.h>

/*!
 * @class       OC_NSBundleHack
 * @abstract    NSBundle hacks to support plugins
 * @discussion
 *     This class that is used to post for NSBundle
 *     if it does not do the right thing
 */

@interface OC_NSBundleHack : NSBundle
{
}
+(void)installBundleHack;
@end

@interface OC_NSBundleHackCheck : NSObject
{
}
+(NSBundle*)bundleForClass;
@end
