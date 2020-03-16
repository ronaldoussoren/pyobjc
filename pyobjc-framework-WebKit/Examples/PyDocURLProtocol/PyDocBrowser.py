import AppKit  # noqa: F401
import Foundation  # noqa: F401
import PyDocEvents  # noqa: F401
import PyDocURLProtocol  # noqa: F401
import WebKit  # noqa: F401
from PyObjCTools import AppHelper

PyDocURLProtocol.setup()

# the web browser doesn't have or need any code really

if __name__ == "__main__":
    AppHelper.runEventLoop()
