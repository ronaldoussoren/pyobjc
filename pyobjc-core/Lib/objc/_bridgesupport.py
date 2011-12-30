"""
This file used to contain bridgesupport support and will be removed
in a future release.
"""
__all__ = ()

import sys

from objc import registerMetaDataForSelector

for method in (b'alloc', b'copy', b'copyWithZone:', b'mutableCopy', b'mutableCopyWithZone:'):
    registerMetaDataForSelector(b'NSObject', method,
            dict(
                retval=dict(already_retained=True),
            ))
