"""
Helpers for NSURL
"""

import objc


def __fspath__(self):
    if self.scheme() == "file":
        return self.fileSystemRepresentation().decode()

    raise TypeError(f"NSURL with scheme {self.scheme()!r} instead of 'file'")


objc.addConvenienceForClass(
    "NSURL",
    (("__fspath__", __fspath__),),
)
