import keyword
import os
import sys
from code import InteractiveConsole, softspace

try:
    import __builtin__
except ImportError:
    import builtins as __builtin__


class RemoteConsole(InteractiveConsole):
    def __init__(self, pipe, **kw):
        self.pipe = pipe
        self.buffer = None
        InteractiveConsole.__init__(self, **kw)
        self.locals["__interpreter__"] = self

    def raw_input(self, prompt=""):
        return self.pipe.expect("RemoteConsole.raw_input", prompt)

    def write(self, msg):
        return self.pipe.expect("RemoteConsole.write", msg)

    def resetbuffer(self):
        self.lastbuffer = self.buffer
        InteractiveConsole.resetbuffer(self)

    def displayhook(self, value):
        if value is not None:
            __builtin__._ = value
        return self.pipe.expect("RemoteConsole.displayhook", value)

    def excepthook(self, exc_type, value, traceback):
        return self.pipe.expect("RemoteConsole.excepthook", exc_type, value, traceback)

    def runcode(self, code):
        try:
            exec(code, self.locals)
        except SystemExit:
            raise
        except:  # noqa: E722, B001
            self.showtraceback()
        else:
            if softspace(sys.stdout, 0):
                print

    def interact(self):
        old_raw_input = __builtin__.raw_input
        old_displayhook = sys.displayhook
        old_excepthook = sys.excepthook
        old_stdin = sys.stdin
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        old_help = __builtin__.help
        old_quit = __builtin__.quit
        __builtin__.raw_input = self.raw_input
        __builtin__.help = "Close window to exit."
        __builtin__.quit = "Close window to exit."
        sys.displayhook = self.displayhook
        sys.excepthook = self.excepthook
        sys.stdin = self.pipe.stdin
        sys.stdout = self.pipe.stdout
        sys.stderr = self.pipe.stderr
        try:
            self.pipe.expect(
                "RemoteConsole.initialize",
                repr(sys.version_info),
                sys.executable,
                os.getpid(),
            )
            InteractiveConsole.interact(self)
        finally:
            __builtin__.raw_input = old_raw_input
            __builtin__.help = old_help
            __builtin__.quit = old_quit
            sys.displayhook = old_displayhook
            sys.excepthook = old_excepthook
            sys.stdin = old_stdin
            sys.stdout = old_stdout
            sys.stderr = old_stderr

    def recommendCompletionsFor(self, word):
        parts = word.split(".")
        if len(parts) > 1:
            # has a . so it must be a module or class or something
            # using eval, which shouldn't normally have side effects
            # unless there's descriptors/metaclasses doing some nasty
            # get magic
            objname = ".".join(parts[:-1])
            try:
                obj = eval(objname, self.locals)
            except:  # noqa: E722, B001
                return None, 0
            wordlower = parts[-1].lower()
            if wordlower == "":
                # they just punched in a dot, so list all attributes
                # that don't look private or special
                prefix = ".".join(parts[-2:])
                check = [
                    (prefix + _method)
                    for _method in dir(obj)
                    if _method[:1] != "_" and _method.lower().startswith(wordlower)
                ]
            else:
                # they started typing the method name
                check = filter(lambda s: s.lower().startswith(wordlower), dir(obj))
        else:
            # no dots, must be in the normal namespaces.. no eval necessary
            check = set(dir(__builtin__))
            check.update(keyword.kwlist)
            check.update(self.locals)
            wordlower = parts[-1].lower()
            check = filter(lambda s: s.lower().startswith(wordlower), check)
        check.sort()
        return check, 0
