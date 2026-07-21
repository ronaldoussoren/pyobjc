from AppKit import (
    NSApplication,
    NSView,
    NSColor,
    NSBezierPath,
    NSWindow,
    NSBorderlessWindowMask,
    NSBackingStoreBuffered,
    NSScreen,
)

app = NSApplication.sharedApplication()
app.setActivationPolicy_(1)  # Accessory

screen = NSScreen.mainScreen()
frame = screen.frame()


class OverlayView(NSView):
    def drawRect_(self, dirty):
        # Never reached — crash happens before this line
        print("drawRect_ called")
        NSColor.blackColor().colorWithAlphaComponent_(0.4).set()
        NSBezierPath.fillRect_(self.bounds())


win = NSWindow.alloc().initWithContentRect_styleMask_backing_defer_(
    frame, NSBorderlessWindowMask, NSBackingStoreBuffered, False
)
win.setLevel_(1000)  # high level is required to trigger the bug
win.setOpaque_(False)
win.setBackgroundColor_(NSColor.clearColor())

view = OverlayView.alloc().initWithFrame_(frame)
win.setContentView_(view)
win.makeKeyAndOrderFront_(None)
win.orderFrontRegardless()
app.activateIgnoringOtherApps_(True)
app.run()
