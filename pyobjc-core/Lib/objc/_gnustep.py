__all__ = ['pathForFramework', 'infoForFramework']
#
# TODO - I have no idea what the semantics are for GNUStep ..
#
from _framework import infoForFramework

def ensure_unicode(s):
    if isinstance(s, str):
        return unicode(s)
    return s

def pathForFramework(path):
    return ensure_unicode(path)
