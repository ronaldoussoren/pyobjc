#!/usr/bin/python

import sys
import os.path

sys.path.insert(0, os.path.join(sys.path[0], "pyobjc"))

import objc
import Foundation
import AppKit

import WSTApplicationDelegateClass
import WSTConnectionWindowControllerClass

sys.exit( AppKit.NSApplicationMain(sys.argv) )
