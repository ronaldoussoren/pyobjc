import sre_parse, sre_compile
from sre_constants import BRANCH, SUBPATTERN
from sre import VERBOSE, MULTILINE, DOTALL
import re


__all__ = ['Scanner', 'Token', 'IgnoreToken']

class Scanner(object):
    def __init__(self, lexicon, flags=(VERBOSE | MULTILINE | DOTALL), verify=True):
        self.actions = [None]
        # combine phrases into a compound pattern
        s = sre_parse.Pattern()
        s.flags = flags
        p = []
        for idx, token in enumerate(lexicon):
            phrase = token.pattern
            subpattern = sre_parse.SubPattern(s,
                [(SUBPATTERN, (idx+1, sre_parse.parse(phrase, flags)))])
            token.regex = re.compile(phrase, flags)
            p.append(subpattern)
            self.actions.append(token)
        if verify:
            for token in lexicon:
                example = token.example
                if example is None:
                    continue
                match = token.regex.match
                j = len(example)
                i = 0
                while i < j:
                    res = match(example, i)
                    if res is None:
                        print token.__name__, i, j
                        print '--- PATTERN ---'
                        print token.pattern
                        print '--- PARSED EXAMPLE ---'
                        print example[:i]
                        print '--- EXAMPLE LEFT ---'
                        print example[i:]
                        raise ValueError, "Token %s can not be verified" % token.__name__
                    i = res.end()
        p = sre_parse.SubPattern(s, [(BRANCH, (None, p))])
        self.scanner = sre_compile.compile(p)

    def iterscan(self, string):
        match = self.scanner.scanner(string).search
        actions = self.actions
        i = 0
        while True:
            m = match()
            if m is None:
                print i, j
                print repr(string[i:])
                return
            j = m.end()
            if i == j:
                return
            action = actions[m.lastindex]
            if action is not None:
                yield action(m)
            i = j

class Token(object):
    pattern = None
    example = None
    regex = None
    match = None
    _groupdict = None

    def __new__(cls, match):
        self = super(Token, cls).__new__(cls)
        return self.found(match)
    
    def groupdict(self):
        groups = self._groupdict
        if groups is None:
            if self.match is None:
                return None
            groups = self._groupdict = self.match.groupdict()
        return groups
       
    def __getitem__(self, item):
        return self.groupdict()[item]

    def found(self, match):
        if self.regex is not None:
            match = self.regex.match(match.string, *match.span())
        self.match = match
        return self

    def __repr__(self):
        return '%s(%r)' % (type(self).__name__, self.groupdict())

class IgnoreToken(Token):
    def found(self, match):
        return None
