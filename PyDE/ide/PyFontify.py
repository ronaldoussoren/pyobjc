"""Module to analyze Python source code; for syntax coloring tools.

Interface:
        for tag, start, end, sublist in fontify(pytext, searchfrom, searchto):
                ...

The 'pytext' argument is a string containing Python source code.
The (optional) arguments 'searchfrom' and 'searchto' may contain a slice in pytext.
The returned value is a list of tuples, formatted like this:
        [('keyword', 0, 6, None), ('keyword', 11, 17, None), ('comment', 23, 53, None), etc. ]
The tuple contents are always like this:
        (tag, startindex, endindex, sublist)
tag is one of 'keyword', 'string', 'comment' or 'identifier'
sublist is not used, hence always None.
"""

# Based on FontText.py by Mitchell S. Chapman,
# which was modified by Zachary Roadhouse,
# then un-Tk'd by Just van Rossum.
# Many thanks for regular expression debugging & authoring are due to:
#       Tim (the-incredib-ly y'rs) Peters and Cristian Tismer
# So, who owns the copyright? ;-) How about this:
# Copyright 1996-2003:
#       Mitchell S. Chapman,
#       Zachary Roadhouse,
#       Tim Peters,
#       Just van Rossum

from __future__ import generators

__version__ = "0.5"

import re
from keyword import kwlist as keywordsList
keywordsList = keywordsList[:]
keywordsList += ["None", "True", "False"]


# Build up a regular expression which will match anything
# interesting, including multi-line triple-quoted strings.
commentPat = r"#[^\n]*"

pat = r"[uU]?[rR]?q[^\\q\n]*(\\[\000-\377][^\\q\n]*)*q?"
quotePat = pat.replace("q", "'") + "|" + pat.replace('q', '"')

# Way to go, Tim!
pat = r"""
        [uU]?[rR]?
        qqq
        [^\\q]*
        (
                (       \\[\000-\377]
                |       q
                        (       \\[\000-\377]
                        |       [^\q]
                        |       q
                                (       \\[\000-\377]
                                |       [^\\q]
                                )
                        )
                )
                [^\\q]*
        )*
        (qqq)?
"""
pat = "".join(pat.split())      # get rid of whitespace
tripleQuotePat = pat.replace("q", "'") + "|" + pat.replace('q', '"')

# Build up a regular expression which matches all and only
# Python keywords. This will let us skip the uninteresting
# identifier references.
keyPat = r"\b(" + "|".join(keywordsList) + r")\b"

matchPat = commentPat + "|" + keyPat + "|(" + tripleQuotePat + "|" + quotePat + ")"
matchRE = re.compile(matchPat)

idKeyPat = "[ \t]*([A-Za-z_][A-Za-z_0-9.]*)"    # Ident w. leading whitespace.
idRE = re.compile(idKeyPat)
asRE = re.compile(r".*?\b(as)\b")

def fontify(pytext, searchfrom=0, searchto=None):
    if searchto is None:
        searchto = len(pytext)
    # Cache a few attributes for quicker reference.
    search = matchRE.search
    idMatch = idRE.match
    asMatch = asRE.match

    commentTag = 'comment'
    stringTag = 'string'
    keywordTag = 'keyword'
    identifierTag = 'identifier'

    start = 0
    end = searchfrom
    while 1:
        m = search(pytext, end)
        if m is None:
            break   # EXIT LOOP
        if start >= searchto:
            break   # EXIT LOOP
        keyword = m.group(1)
        if keyword is not None:
            # matched a keyword
            start, end = m.span(1)
            yield keywordTag, start, end, None
            if keyword in ["def", "class"]:
                # If this was a defining keyword, color the
                # following identifier.
                m = idMatch(pytext, end)
                if m is not None:
                    start, end = m.span(1)
                    yield identifierTag, start, end, None
            elif keyword == "import":
                # color all the "as" words on same line;
                # cheap approximation to the truth
                while 1:
                    m = asMatch(pytext, end)
                    if not m:
                        break
                    start, end = m.span(1)
                    yield keywordTag, start, end, None
        elif m.group(0)[0] == "#":
            start, end = m.span()
            yield commentTag, start, end, None
        else:
            start, end = m.span()
            yield stringTag, start, end, None


def test(path):
    f = open(path)
    text = f.read()
    f.close()
    for tag, start, end, sublist in fontify(text):
        print tag, repr(text[start:end])


if __name__ == "__main__":
    import sys
    test(sys.argv[1])
