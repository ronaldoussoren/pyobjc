#
#  DNDTableView.py
#  Bookmarks
#
#  Converted by u.fiedler on 10.02.05.
#
#  The original version was written in Objective-C by Malcolm Crawford
#  at http://homepage.mac.com/mmalc/CocoaExamples/controllers.html

from AppKit import *

class DNDTableView (NSTableView):

    def draggingSourceOperationMaskForLocal_(self, flag):
        # This is a bug fix. See
        # file:///Developer/ADC%20Reference%20Library/documentation/Cocoa/Conceptual/DragandDrop/Tasks/faq.html#//apple_ref/doc/uid/20002248/BBCGGBHE
        # or http://developer.apple.com/documentation/Cocoa/Conceptual/DragandDrop/Tasks/faq.html#//apple_ref/doc/uid/20002248/BBCFIJGF
        if not flag:
            return NSDragOperationLink # link for external dragged URLs
        return super(DNDTableView, self).draggingSourceOperationMaskForLocal_(flag)
