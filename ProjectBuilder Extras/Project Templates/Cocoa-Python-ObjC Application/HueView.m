#import "HueView.h"

@implementation HueView

- (id)initWithFrame:(NSRect)frameRect
{
	[super initWithFrame:frameRect];
	return self;
}

- (void)drawRect:(NSRect)rect
{
    [[NSColor colorWithCalibratedHue: hue saturation: 1.0 brightness: 1.0 alpha: 1.0] set];
    NSRectFill([self bounds]);
}

- (float)hue { return hue; }
- (void)setHue:(float)aHue
{
    hue = aHue;
    [self setNeedsDisplay: YES];
}
@end
