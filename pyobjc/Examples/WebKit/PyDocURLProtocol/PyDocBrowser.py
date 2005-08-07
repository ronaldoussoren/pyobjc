from PyObjCTools import NibClassBuilder, AppHelper

import Foundation, AppKit, WebKit
from Foundation import *
from AppKit import *
import objc; objc.setVerbose(1)

import PyDocURLProtocol
import PyDocEvents

PyDocURLProtocol.setup()

NibClassBuilder.extractClasses('PyDocBrowser')

# the web browser doesn't have or need any code really

if __name__ == '__main__':
    AppHelper.runEventLoop()
