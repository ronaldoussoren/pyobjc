from PyObjCTools import NibClassBuilder, AppHelper

import Foundation, AppKit, WebKit
from Foundation import *
from AppKit import *

import PyDocURLProtocol

PyDocURLProtocol.setup()

NibClassBuilder.extractClasses('PyDocBrowser')

# the web browser doesn't have or need any code really

if __name__ == '__main__':
    AppHelper.runEventLoop()
