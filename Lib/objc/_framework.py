"""
Generic framework path manipulation
"""

import re
__all__ = ['infoForFramework']

# This regexp should find:
#   \1 - framework location
#   \2 - framework name
#   \3 - framework version (optional)
#
FRAMEWORK_RE = re.compile(
    r"""(^.*)(?:^|/)(\w+).framework(?:/(?:Versions/([^/]+)/)?\2$)?"""
)

def infoForFramework(filename):
    """returns (location, name, version) or None"""
    is_framework = FRAMEWORK_RE.findall(filename)
    if not is_framework:
        return None
    return is_framework[-1]
