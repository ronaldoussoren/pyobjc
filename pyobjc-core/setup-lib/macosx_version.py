import os
if not os.path.exists('/usr/bin/sw_vers'):
    raise ImportError("Not Mac OS X")
from distutils.version import StrictVersion, LooseVersion

def Version(s):
    try:
        return StrictVersion(s)
    except ValueError:
        return LooseVersion(s)

def sw_vers(_cache=[]):
    # Using os.popen makes it annoyinly hard to debug using gdb...
    try:
        import plistlib

        pl = plistlib.readPlist('/System/Library/CoreServices/SystemVersion.plist')
        _cache.append(Version(pl['ProductVersion']))
    except (ImportError, KeyError):
        pass

    if not _cache:
        info = os.popen('/usr/bin/sw_vers').read().splitlines()
        for line in info:
            key, value = line.split(None, 1)
            if key == 'ProductVersion:':
                _cache.append(Version(value.strip()))
                break
        else:
            raise ValueError("sw_vers not behaving correctly")
    return _cache[0]
