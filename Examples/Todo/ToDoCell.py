from AppKit import *
from Foundation import *
from objc import selector

NOT_DONE=0
DONE=1
DEFERRED=2

class ToDoCell (NSButtonCell):

    __slots__ = ('_triState', '_doneImage', '_deferredImage', '_timeDue' )

    def init(self):
        self._triState = NOT_DONE
        self._timeDue = None
        self._doneImage = None
        self._deferredImage = None

        NSButtonCell.initTextCell_(self, "")

        self.setType_(NSToggleButton)
        self.setImagePosition_(NSImageLeft)
        self.setBezelStyle_(NSShadowlessSquareBezelStyle)
        self.setFont_(NSFont.userFontOfSize_(10))
        self.setAlignment_(NSRightTextAlignment)

        self._doneImage = NSImage.imageNamed_("DoneMark")
        self._deferredImage = NSImage.imageNamed_("DeferredMark")
        return self

    def setTriState_(self, newState):
        if newState > DEFERRED:
            self._triState = NOT_DONE
        else:
            self._triState = newState

        self.updateImage()
    setTriState_ = selector(setTriState_, signature="v@:i")

    def triState(self):
        return self._triState
    triState = selector(triState, signature="i@:")


    def setState_(self, val):
        pass

    def state(self):
        if self._triState == DEFERRED:
            return DONE
        else:
            return self._triState

    def updateImage(self):

        if self._triState == NOT_DONE:
            #print "NO IMAGE"
            self.setImage_(None)
        elif self._triState == DONE:
            #print "DONE IMAGE"
            self.setImage_(self._doneImage)
        elif self._triState == DEFERRED:
            #print "DEFERRED IMAGE"
            self.setImage_(self._deferredImage)

        self.controlView().updateCell_(self)

    def startTrackingAt_inView_(self, startPoint, controlView):
        #print "startTracking:", startPoint, controlView
        return 1
    startTrackingAt_inView_ = selector(
        startTrackingAt_inView_, signature="c@:{NSPoint=ff}@")

    def stopTracking_at_inView_mouseIsUp_(self, lastPoint, stopPoint, controlView, flag):
        #print "stopTracking:", lastPoint, stopPoint, controlView, flag, self.triState()
        if flag:
            self.setTriState_(self.triState() + 1)
    stopTracking_at_inView_mouseIsUp_ = selector(
        stopTracking_at_inView_mouseIsUp_,
        signature="v@:{NSPoint=ff}{NSPoint=ff}@c")

    def setTimeDue_(self, newTime):
        if newTime:
            self._timeDue = newTime
            self.setTitle_(self._timeDue.descriptionWithCalendarFormat_timeZone_locale_("%I:%M %p", NSTimeZone.localTimeZone(), None))
        else:
            self._timeDue = None
            self.setTitle_("-->")

    def timeDue(self):
        return self._timeDue
