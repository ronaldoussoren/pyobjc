"""
CoreGraphics isn't wrapped properly yet (except in Apple's python2.3 
installation), this example shows how you can access functions in CoreGraphics
anyway.
"""
import objc 
bndl = objc.loadBundle('CoreGraphics', globals(), 
        '/System/Library/Frameworks/ApplicationServices.framework') 
objc.loadBundleFunctions(bndl, globals(), [ 
     ('CGWarpMouseCursorPosition', 'v{CGPoint=ff}'), 
]) 

if __name__ == "__main__":
    # Move cursor to the Apple menu
    CGWarpMouseCursorPosition((25, 10))
