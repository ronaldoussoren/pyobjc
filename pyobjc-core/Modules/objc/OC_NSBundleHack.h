/*!
 * @header OC_NSBundleHack.h
 * @abstract NSBundle hacks to support plugins
 * @discussion
 *     This file defines the class that is used to convince NSBundle
 *     that it should do the right thing for Python classes.
 */

#import "pyobjc.h"
#import <Foundation/Foundation.h>

NS_ASSUME_NONNULL_BEGIN

/*!
 * @class OC_NSBundleHack
 * @abstract NSBundle hacks to support plugins
 * @discussion
 *     This class that is used to pose for NSBundle
 *     if it does not do the right thing
 */

PyObjC_FINAL_CLASS @interface OC_NSBundleHack : NSBundle {
}
+ (void)installBundleHack;
+ (BOOL)bundleHackUsed;
@end

@interface OC_NSBundleHackCheck : NSObject {
}
+ (NSBundle* _Nullable)bundleForClass;
@end

NS_ASSUME_NONNULL_END
