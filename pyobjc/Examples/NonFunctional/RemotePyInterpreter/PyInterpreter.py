import sys
import traceback
import sets
import keyword
import time
from Foundation import *
from AppKit import *
from PyObjCTools import NibClassBuilder, AppHelper

NibClassBuilder.extractClasses("PyInterpreter.nib")

from AsyncPyInterpreter import *
from ConsoleReactor import *

class RemotePyInterpreterReactor(ConsoleReactor):
    def handleExpectCommand_(self, command):
        super(RemotePyInterpreterReactor, self).handleExpectCommand_(command)
    

class PseudoUTF8Input(object):
    softspace = 0
    def __init__(self, readlinemethod):
        self._buffer = u''
        self._readline = readlinemethod

    def read(self, chars=None):
        if chars is None:
            if self._buffer:
                rval = self._buffer
                self._buffer = u''
                if rval.endswith(u'\r'):
                    rval = rval[:-1]+u'\n'
                return rval.encode('utf-8')
            else:
                return self._readline(u'\x04')[:-1].encode('utf-8')
        else:
            while len(self._buffer) < chars:
                self._buffer += self._readline(u'\x04\r')
                if self._buffer.endswith('\x04'):
                    self._buffer = self._buffer[:-1]
                    break
            rval, self._buffer = self._buffer[:chars], self._buffer[chars:]
            return rval.encode('utf-8').replace('\r','\n')

    def readline(self):
        if u'\r' not in self._buffer:
            self._buffer += self._readline(u'\x04\r')
        if self._buffer.endswith('\x04'):
            rval = self._buffer[:-1].encode('utf-8')
        elif self._buffer.endswith('\r'):
            rval = self._buffer[:-1].encode('utf-8')+'\n'
        self._buffer = u''

        return rval


DEBUG_DELEGATE = 0
PASSTHROUGH = (
   'deleteBackward:',
   'complete:',
   'moveRight:',
   'moveLeft:',
)

class PyInterpreter(NibClassBuilder.AutoBaseClass):
    """
    PyInterpreter is a delegate/controller for a NSTextView,
    turning it into a full featured interactive Python interpreter.
    """

    #
    #  NSApplicationDelegate methods
    #

    def applicationDidFinishLaunching_(self, aNotification):
        self.textView.setFont_(self.font())
        self.textView.setContinuousSpellCheckingEnabled_(False)
        self.textView.setRichText_(False)
        self.p_executeWithRedirectedIO(self.p_interp)

    #
    #  NIB loading protocol
    #

    def awakeFromNib(self):
        self = super(PyInterpreter, self).init()
        self.p_font = NSFont.userFixedPitchFontOfSize_(10)
        self.p_stderrColor = NSColor.redColor()
        self.p_stdoutColor = NSColor.blueColor()
        self.p_codeColor = NSColor.blackColor()
        self.p_historyLength = 50
        self.p_history = [u'']
        self.p_historyView = 0
        self.p_characterIndexForInput = 0
        self.p_stdin = PseudoUTF8Input(self.p_nestedRunLoopReaderUntilEOLchars_)
        self.p_isInteracting = False
        self.p_console = AsyncInteractiveConsole()
        self.p_interp = self.p_console.asyncinteract(
            write=self.writeCode_,
        ).next
        self.p_autoscroll = True

    #
    #  Modal input dialog support
    #

    def p_nestedRunLoopReaderUntilEOLchars_(self, eolchars):
        """
        This makes the baby jesus cry.

        I want co-routines.
        """
        app = NSApplication.sharedApplication()
        window = self.textView.window()
        self.setCharacterIndexForInput_(self.lengthOfTextView())
        # change the color.. eh
        self.textView.setTypingAttributes_({
            NSFontAttributeName:self.font(),
            NSForegroundColorAttributeName:self.codeColor(),
        })
        while True:
            event = app.nextEventMatchingMask_untilDate_inMode_dequeue_(
                NSAnyEventMask,
                NSDate.distantFuture(),
                NSDefaultRunLoopMode,
                True)
            if (event.type() == NSKeyDown) and (event.window() == window):
                eol = event.characters()
                if eol in eolchars:
                    break
            app.sendEvent_(event)
        cl = self.currentLine()
        if eol == '\r':
            self.writeCode_('\n')
        return cl+eol

    #
    #  Interpreter functions
    #

    def p_executeWithRedirectedIO(self, fn, *args, **kwargs):
        old = sys.stdin, sys.stdout, sys.stderr
        if self.p_stdin is not None:
            sys.stdin = self.p_stdin
        sys.stdout, sys.stderr = self.p_stdout, self.p_stderr
        try:
            rval = fn(*args, **kwargs)
        finally:
            sys.stdin, sys.stdout, sys.stderr = old
            self.setCharacterIndexForInput_(self.lengthOfTextView())
        return rval

    def executeLine_(self, line):
        self.addHistoryLine_(line)
        self.p_executeWithRedirectedIO(self.p_executeLine_, line)
        self.p_history = filter(None, self.p_history)
        self.p_history.append(u'')
        self.p_historyView = len(self.p_history) - 1

    def p_executeLine_(self, line):
        self.p_interp()(line)
        self.p_more = self.p_interp()

    def executeInteractiveLine_(self, line):
        self.setIsInteracting(True)
        try:
            self.executeLine_(line)
        finally:
            self.setIsInteracting(False)

    def replaceLineWithCode_(self, s):
        idx = self.characterIndexForInput()
        ts = self.textView.textStorage()
        ts.replaceCharactersInRange_withAttributedString_(
            (idx, len(ts.mutableString())-idx), self.codeString_(s))

    #
    #  History functions
    #

    def historyLength(self):
        return self.p_historyLength

    def setHistoryLength_(self, length):
        self.p_historyLength = length

    def addHistoryLine_(self, line):
        line = line.rstrip('\n')
        if self.p_history[-1] == line:
            return False
        if not line:
            return False
        self.p_history.append(line)
        if len(self.p_history) > self.historyLength():
            self.p_history.pop(0)
        return True

    def historyDown_(self, sender):
        if self.p_historyView == (len(self.p_history) - 1):
            return
        self.p_history[self.p_historyView] = self.currentLine()
        self.p_historyView += 1
        self.replaceLineWithCode_(self.p_history[self.p_historyView])
        self.moveToEndOfLine_(self)

    def historyUp_(self, sender):
        if self.p_historyView == 0:
            return
        self.p_history[self.p_historyView] = self.currentLine()
        self.p_historyView -= 1
        self.replaceLineWithCode_(self.p_history[self.p_historyView])
        self.moveToEndOfLine_(self)

    #
    #  Convenience methods to create/write decorated text
    #

    def p_formatString_forOutput_(self, s, name):
        return NSAttributedString.alloc().initWithString_attributes_(
            s,
            {
                NSFontAttributeName:self.font(),
                NSForegroundColorAttributeName:getattr(self, name+'Color')(),
            },
        )

    def p_writeString_forOutput_(self, s, name):
        self.textView.textStorage().appendAttributedString_(getattr(self, name+'String_')(s))

        window = self.textView.window()

        if self.p_autoscroll:
            self.textView.scrollRangeToVisible_((self.lengthOfTextView(), 0))

    codeString_   = lambda self, s: self.p_formatString_forOutput_(s, 'code')
    stderrString_ = lambda self, s: self.p_formatString_forOutput_(s, 'stderr')
    stdoutString_ = lambda self, s: self.p_formatString_forOutput_(s, 'stdout')
    writeCode_    = lambda self, s: self.p_writeString_forOutput_(s, 'code')
    writeStderr_  = lambda self, s: self.p_writeString_forOutput_(s, 'stderr')
    writeStdout_  = lambda self, s: self.p_writeString_forOutput_(s, 'stdout')

    #
    #  Accessors
    #

    def more(self):
        return self.p_more

    def font(self):
        return self.p_font

    def setFont_(self, font):
        self.p_font = font

    def stderrColor(self):
        return self.p_stderrColor

    def setStderrColor_(self, color):
        self.p_stderrColor = color

    def stdoutColor(self):
        return self.p_stdoutColor

    def setStdoutColor_(self, color):
        self.p_stdoutColor = color

    def codeColor(self):
        return self.p_codeColor

    def setStdoutColor_(self, color):
        self.p_codeColor = color

    def isInteracting(self):
        return self.p_isInteracting

    def setIsInteracting(self, v):
        self.p_isInteracting = v

    def isAutoScroll(self):
        return self.p_autoScroll

    def setAutoScroll(self, v):
        self.p_autoScroll = v


    #
    #  Convenience methods for manipulating the NSTextView
    #

    def currentLine(self):
        return self.textView.textStorage().mutableString()[self.characterIndexForInput():]

    def moveAndScrollToIndex_(self, idx):
        self.textView.scrollRangeToVisible_((idx, 0))
        self.textView.setSelectedRange_((idx, 0))

    def characterIndexForInput(self):
        return self.p_characterIndexForInput

    def lengthOfTextView(self):
        return len(self.textView.textStorage().mutableString())

    def setCharacterIndexForInput_(self, idx):
        self.p_characterIndexForInput = idx
        self.moveAndScrollToIndex_(idx)

    #
    #  NSTextViewDelegate methods
    #

    def textView_completions_forPartialWordRange_indexOfSelectedItem_(self, aTextView, completions, (begin, length), index):
        txt = self.textView.textStorage().mutableString()
        end = begin+length
        while (begin>0) and (txt[begin].isalnum() or txt[begin] in '._'):
            begin -= 1
        while not txt[begin].isalnum():
            begin += 1
        return self.p_console.recommendCompletionsFor(txt[begin:end])

    def textView_shouldChangeTextInRange_replacementString_(self, aTextView, aRange, newString):
        begin, length = aRange
        lastLocation = self.characterIndexForInput()
        if begin < lastLocation:
            # no editing anywhere but the interactive line
            return False
        newString = newString.replace('\r', '\n')
        if '\n' in newString:
            if begin != lastLocation:
                # no pasting multiline unless you're at the end
                # of the interactive line
                return False
            # multiline paste support
            #self.clearLine()
            newString = self.currentLine() + newString
            for s in newString.strip().split('\n'):
                self.writeCode_(s+'\n')
                self.executeLine_(s)
            return False
        return True

    def textView_willChangeSelectionFromCharacterRange_toCharacterRange_(self, aTextView, fromRange, toRange):
        return toRange
        begin, length = toRange
        if length == 0 and begin < self.characterIndexForInput():
            # no cursor movement off the interactive line
            return fromRange
        return toRange

    def textView_doCommandBySelector_(self, aTextView, aSelector):
        # deleteForward: is ctrl-d
        if self.isInteracting():
            if aSelector == 'insertNewline:':
                self.writeCode_('\n')
            return False
        responder = getattr(self, aSelector.replace(':','_'), None)
        if responder is not None:
            responder(aTextView)
            return True
        else:
            if DEBUG_DELEGATE and aSelector not in PASSTHROUGH:
                print aSelector
            return False

    #
    #  doCommandBySelector "posers" on the textView
    #

    def insertTabIgnoringFieldEditor_(self, sender):
        # this isn't terribly necessary, b/c F5 and opt-esc do completion
        # but why not
        sender.complete_(self)

    def moveToBeginningOfLine_(self, sender):
        self.moveAndScrollToIndex_(self.characterIndexForInput())

    def moveToEndOfLine_(self, sender):
        self.moveAndScrollToIndex_(self.lengthOfTextView())

    def moveToBeginningOfLineAndModifySelection_(self, sender):
        begin, length = self.textView.selectedRange()
        pos = self.characterIndexForInput()
        if begin+length > pos:
            self.textView.setSelectedRange_((pos, begin+length-pos))
        else:
            self.moveToBeginningOfLine_(sender)

    def moveToEndOfLineAndModifySelection_(self, sender):
        begin, length = self.textView.selectedRange()
        pos = max(self.characterIndexForInput(), begin)
        self.textView.setSelectedRange_((pos, self.lengthOfTextView()))

    def insertNewline_(self, sender):
        line = self.currentLine()
        self.writeCode_('\n')
        self.executeInteractiveLine_(line)

    moveToBeginningOfParagraph_ = moveToBeginningOfLine_
    moveToEndOfParagraph_ = moveToEndOfLine_
    insertNewlineIgnoringFieldEditor_ = insertNewline_
    moveDown_ = historyDown_
    moveUp_ = historyUp_


if __name__ == '__main__':
    AppHelper.runEventLoop()
