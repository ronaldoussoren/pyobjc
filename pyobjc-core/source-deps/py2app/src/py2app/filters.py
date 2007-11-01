import os
import sys
from macholib.util import has_filename_filter, in_system_path

def not_stdlib_filter(module, prefix=None):
    """
    Return False if the module is located in the standard library
    """
    if prefix is None:
        prefix = sys.prefix
    prefix = os.path.join(os.path.realpath(prefix), '')
    rp = os.path.realpath(module.filename)
    if rp.startswith(prefix):
        rest = rp[len(prefix):]
        if '/site-python/' in rest:
            return True
        elif '/site-packages/' in rest:
            return True
        else:
            return False
    return True

def not_system_filter(module):
    """
    Return False if the module is located in a system directory
    """
    return not in_system_path(module.filename)

def bundle_or_dylib_filter(module):
    """
    Return False if the module does not have a filetype attribute
    corresponding to a Mach-O bundle or dylib
    """
    return getattr(module, 'filetype', None) in ('bundle', 'dylib')
