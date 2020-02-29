import AppKit
import Foundation
import PyDocEvents
import PyDocURLProtocol
import WebKit
from PyObjCTools import AppHelper

PyDocURLProtocol.setup()

# the web browser doesn"t have or need any code really

if __name__ == "__main__":
    AppHelper.runEventLoop()
