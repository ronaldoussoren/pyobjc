/* HueView */

#import <Cocoa/Cocoa.h>

@interface HueView : NSView
{
    float hue;
}

- (float)hue;
- (void)setHue:(float)aHue;
@end
