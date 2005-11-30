import sys
import traceback
import sets
import keyword
import time
from Foundation import *
from AppKit import *
from PyObjCTools import NibClassBuilder, AppHelper

NibClassBuilder.extractClasses("RemotePyInterpreterDocument.nib")

from AsyncPythonInterpreter import *
from ConsoleReactor import *
from netrepr import RemoteObjectReference

def ensure_unicode(s):
    if not isinstance(s, unicode):
        s = unicode(s, 'utf-8', 'replace')
    return s

class RemotePyInterpreterReactor(NibClassBuilder.AutoBaseClass):
    def handleExpectCommand_(self, command):
        print command
        seq = command[0]
        name = command[1]
        args = command[2:]
        netrepr = self.netReprCenter.netrepr
        rval = None
        code = None
        if name == 'RemoteConsole.raw_input':
            prompt = ensure_unicode(args[0])
            def input_received(line):
                self.sendResult_sequence_(line, seq)
            self.delegate.expectCodeInput_withPrompt_(input_received, prompt)
        elif name == 'RemoteConsole.write':
            args = [ensure_unicode(args[0]), u'code']
            self.doCallback_sequence_args_(self.delegate.writeString_forOutput_, seq, args)
        elif name == 'RemoteConsole.displayhook':
            obj = args[0]
            def displayhook_respond(reprobject):
                self.delegate.writeString_forOutput_(ensure_unicode(reprobject) + u'\n', u'code')
            def displayhook_local(obj):
                if obj is not None:
                    displayhook_respond(repr(obj))
            if isinstance(obj, RemoteObjectReference):
                self.deferCallback_sequence_value_(displayhook_respond, seq, 'repr(%s)' % (netrepr(obj),))
            else:
                self.doCallback_sequence_args_(displayhook_local, seq, args)
        elif name.startswith('RemoteFileLike.'):
            method = name[len('RemoteFileLike.'):]
            if method == 'write':
                style, msg = map(ensure_unicode, args)
                args = [msg, style]
                self.doCallback_sequence_args_(self.delegate.writeString_forOutput_, seq, args)

            elif method == 'readline':
                def input_received(line):
                    self.sendResult_sequence_(line, seq)
                self.delegate.expectCodeInput_withPrompt_(input_received, '')

            else:
                self.doCallback_sequence_args_(NSLog, seq, [u'%r does not respond to expect %r' % (self, command,)])
        elif name == 'RemoteConsole.initialize':
            def gotTitle(repr_versioninfo, executable, pid):
                self.delegate.setVersion_executable_pid_(
                    u'.'.join(map(unicode, self.netEval_(repr_versioninfo)[:3])),
                    ensure_unicode(executable),
                    pid,
                )
            self.doCallback_sequence_args_(gotTitle, seq, args)
        #    fh = getattr(sys, args[0])
        #    meth = getattr(fh, name[len('RemoteFileLike.'):])
        #    self.doCallback_sequence_args_(meth, seq, args[1:])
        else:
            self.doCallback_sequence_args_(NSLog, seq, [u'%r does not respond to expect %r' % (self, command,)])
    
    def close(self):
        super(RemotePyInterpreterReactor, self).close()
        self.delegate = None


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

class RemotePyInterpreterDocument(NibClassBuilder.AutoBaseClass):
    """
    PyInterpreter is a delegate/controller for a NSTextView,
    turning it into a full featured interactive Python interpreter.
    """

    def expectCodeInput_withPrompt_(self, callback, prompt):
        self.writeString_forOutput_(prompt, u'code')
        self.setCharacterIndexForInput_(self.lengthOfTextView())
        self.p_input_callbacks.append(callback)
        self.flushCallbacks()

    def flushCallbacks(self):
        while self.p_input_lines and self.p_input_callbacks:
            self.p_input_callbacks.pop(0)(self.p_input_lines.pop(0))

    def setupTextView(self):
        self.textView.setFont_(self.font())
        self.textView.setContinuousSpellCheckingEnabled_(False)
        self.textView.setRichText_(False)
        self.setCharacterIndexForInput_(0)

    def setVersion_executable_pid_(self, version, executable, pid):
        self.version = version
        self.pid = pid
        self.executable = executable
        self.setFileName_(executable)

    def displayName(self):
        if not hasattr(self, 'version'):
            return u'Starting...'
        return u'Python %s - %s - %s' % (self.version, self.executable, self.pid)
    
    def updateChangeCount_(self, val):
        return

    def windowWillClose_(self, window):
        if self.commandReactor is not None:
            self.commandReactor.close()
            self.commandReactor = None
        if self.interpreter is not None:
            self.interpreter.close()
            self.interpreter = None
    
    def windowNibName(self):
        return u'RemotePyInterpreterDocument'
    
    def isDocumentEdited(self):
        return False
    
    def awakeFromNib(self):
        # XXX - should this be done later?
        self.setFont_(NSFont.userFixedPitchFontOfSize_(10))
        self.p_colors = {
            u'stderr': NSColor.redColor(),
            u'stdout': NSColor.blueColor(),
            u'code': NSColor.blackColor(),
        }
        self.setHistoryLength_(50)
        self.setHistoryView_(0)
        self.setInteracting_(False)
        self.setAutoScroll_(True)
        self.setSingleLineInteraction_(False)
        self.p_history = [u'']
        self.p_input_callbacks = []
        self.p_input_lines = []
        self.setupTextView()
        self.interpreter.connect()

    #
    #  Modal input dialog support
    #

    #def p_nestedRunLoopReaderUntilEOLchars_(self, eolchars):
    #    """
    #    This makes the baby jesus cry.

    #    I want co-routines.
    #    """
    #    app = NSApplication.sharedApplication()
    #    window = self.textView.window()
    #    self.setCharacterIndexForInput_(self.lengthOfTextView())
    #    # change the color.. eh
    #    self.textView.setTypingAttributes_({
    #        NSFontAttributeName: self.font(),
    #        NSForegroundColorAttributeName: self.colorForName_(u'code'),
    #    })
    #    while True:
    #        event = app.nextEventMatchingMask_untilDate_inMode_dequeue_(
    #            NSAnyEventMask,
    #            NSDate.distantFuture(),
    #            NSDefaultRunLoopMode,
    #            True)
    #        if (event.type() == NSKeyDown) and (event.window() is window):
    #            eol = event.characters()
    #            if eol in eolchars:
    #                break
    #        app.sendEvent_(event)
    #    cl = self.currentLine()
    #    if eol == u'\r':
    #        self.writeNewLine()
    #    return cl + eol

    def executeLine_(self, line):
        self.addHistoryLine_(line)
        self.p_input_lines.append(line)
        self.flushCallbacks()
        self.p_history = filter(None, self.p_history)
        self.p_history.append(u'')
        self.setHistoryView_(len(self.p_history) - 1)

    def executeInteractiveLine_(self, line):
        self.setInteracting_(True)
        try:
            self.executeLine_(line)
        finally:
            self.setInteracting_(False)

    def replaceLineWithCode_(self, s):
        idx = self.characterIndexForInput()
        ts = self.textView.textStorage()
        s = self.formatString_forOutput_(s, u'code')
        ts.replaceCharactersInRange_withAttributedString_(
            (idx, len(ts.mutableString())-idx),
            s,
        )

    #
    #  History functions
    #

    def addHistoryLine_(self, line):
        line = line.rstrip(u'\n')
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

    def formatString_forOutput_(self, s, name):
        return NSAttributedString.alloc().initWithString_attributes_(
            s,
            {
                NSFontAttributeName: self.font(),
                NSForegroundColorAttributeName: self.colorForName_(name),
            },
        )

    def writeString_forOutput_(self, s, name):
        s = self.formatString_forOutput_(s, name)
        self.textView.textStorage().appendAttributedString_(s)
        if self.isAutoScroll():
            self.textView.scrollRangeToVisible_((self.lengthOfTextView(), 0))

    def writeNewLine(self):
        self.writeString_forOutput_(u'\n', u'code')

    def colorForName_(self, name):
        return self.p_colors[name]

    def setColor_forName_(self, color, name):
        self.p_colors[name] = color
    
    #
    #  Convenience methods for manipulating the NSTextView
    #

    def currentLine(self):
        return self.textView.textStorage().mutableString()[self.characterIndexForInput():]

    def moveAndScrollToIndex_(self, idx):
        self.textView.scrollRangeToVisible_((idx, 0))
        self.textView.setSelectedRange_((idx, 0))

    def lengthOfTextView(self):
        return len(self.textView.textStorage().mutableString())

    #
    #  NSTextViewDelegate methods
    #

    def textView_completions_forPartialWordRange_indexOfSelectedItem_(self, aTextView, completions, (begin, length), index):
        # XXX 
        # this will probably have to be tricky in order to be asynchronous..
        # either by:
        #     nesting a run loop (bleh)
        #     polling the subprocess (bleh)
        #     returning nothing and calling self.textView.complete_ later
        return None, 0

        if False:
            txt = self.textView.textStorage().mutableString()
            end = begin+length
            while (begin>0) and (txt[begin].isalnum() or txt[begin] in u'._'):
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
        newString = newString.replace(u'\r', u'\n')
        if u'\n' in newString:
            if begin != lastLocation:
                # no pasting multiline unless you're at the end
                # of the interactive line
                return False
            # multiline paste support
            #self.clearLine()
            newString = self.currentLine() + newString
            for s in newString.strip().split(u'\n'):
                self.writeString_forOutput_(s + u'\n', u'code')
                self.executeLine_(s)
            return False
        return True

    def textView_willChangeSelectionFromCharacterRange_toCharacterRange_(self, aTextView, fromRange, toRange):
        begin, length = toRange
        if self.singleLineInteraction() and length == 0 and begin < self.characterIndexForInput():
            # no cursor movement off the interactive line
            return fromRange
        else:
            return toRange

    def textView_doCommandBySelector_(self, aTextView, aSelector):
        # deleteForward: is ctrl-d
        if self.isInteracting():
            if aSelector == 'insertNewline:':
                self.writeNewLine()
            return False
        # XXX - this is ugly
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
        if begin + length > pos:
            self.textView.setSelectedRange_((pos, begin + length - pos))
        else:
            self.moveToBeginningOfLine_(sender)

    def moveToEndOfLineAndModifySelection_(self, sender):
        begin, length = self.textView.selectedRange()
        pos = max(self.characterIndexForInput(), begin)
        self.textView.setSelectedRange_((pos, self.lengthOfTextView()))

    def insertNewline_(self, sender):
        line = self.currentLine()
        self.writeNewLine()
        self.executeInteractiveLine_(line)

    moveToBeginningOfParagraph_ = moveToBeginningOfLine_
    moveToEndOfParagraph_ = moveToEndOfLine_
    insertNewlineIgnoringFieldEditor_ = insertNewline_
    moveDown_ = historyDown_
    moveUp_ = historyUp_

    #
    #  Accessors
    #

    def historyLength(self):
        return self.p_historyLength

    def setHistoryLength_(self, length):
        self.p_historyLength = length

    def font(self):
        return self.p_font

    def setFont_(self, font):
        self.p_font = font

    def isInteracting(self):
        return self.p_interacting

    def setInteracting_(self, v):
        self.p_interacting = v

    def isAutoScroll(self):
        return self.p_autoScroll

    def setAutoScroll_(self, v):
        self.p_autoScroll = v

    def characterIndexForInput(self):
        return self.p_characterIndexForInput

    def setCharacterIndexForInput_(self, idx):
        self.p_characterIndexForInput = idx
        self.moveAndScrollToIndex_(idx)

    def historyView(self):
        return self.p_historyView

    def setHistoryView_(self, v):
        self.p_historyView = v

    def singleLineInteraction(self):
        return self.p_singleLineInteraction

    def setSingleLineInteraction_(self, v):
        self.p_singleLineInteraction = v
    
        

if __name__ == '__main__':
    AppHelper.runEventLoop(installInterrupt=True)
