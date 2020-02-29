import Cocoa
import objc

NOT_DONE = 0
DONE = 1
DEFERRED = 2


class ToDoCell(Cocoa.NSButtonCell):

    __slots__ = ("_triState", "_doneImage", "_deferredImage", "_timeDue")

    def init(self):
        self._triState = NOT_DONE
        self._timeDue = None
        self._doneImage = None
        self._deferredImage = None

        Cocoa.NSButtonCell.initTextCell_(self, "")

        self.setType_(Cocoa.NSToggleButton)
        self.setImagePosition_(Cocoa.NSImageLeft)
        self.setBezelStyle_(Cocoa.NSShadowlessSquareBezelStyle)
        self.setFont_(Cocoa.NSFont.userFontOfSize_(10))
        self.setAlignment_(Cocoa.NSRightTextAlignment)

        self._doneImage = Cocoa.NSImage.imageNamed_("DoneMark")
        self._deferredImage = Cocoa.NSImage.imageNamed_("DeferredMark")
        return self

    @objc.typedAccessor(objc._C_INT)
    def setTriState_(self, newState):
        if newState > DEFERRED:
            self._triState = NOT_DONE
        else:
            self._triState = newState

        self.updateImage()

    @objc.typedAccessor(objc._C_INT)
    def triState(self):
        return self._triState

    def setState_(self, val):
        pass

    def state(self):
        if self._triState == DEFERRED:
            return DONE
        else:
            return self._triState

    def updateImage(self):

        if self._triState == NOT_DONE:
            self.setImage_(None)
        elif self._triState == DONE:
            self.setImage_(self._doneImage)
        elif self._triState == DEFERRED:
            self.setImage_(self._deferredImage)

        self.controlView().updateCell_(self)

    def startTrackingAt_inView_(self, startPoint, controlView):
        return 1

    def stopTracking_at_inView_mouseIsUp_(
        self, lastPoint, stopPoint, controlView, flag
    ):
        if flag:
            self.setTriState_(self.triState() + 1)

    def setTimeDue_(self, newTime):
        if newTime:
            self._timeDue = newTime
            self.setTitle_(
                self._timeDue.descriptionWithCalendarFormat_timeZone_locale_(
                    "%I:%M %p", Cocoa.NSTimeZone.localTimeZone(), None
                )
            )
        else:
            self._timeDue = None
            self.setTitle_("-->")

    def timeDue(self):
        return self._timeDue
