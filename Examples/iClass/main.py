"""
"""
from AppKit import NSApplicationMain
from Foundation import NSBundle
import sys
import os

print sys.path	
import datasource

print datasource.ClassesDataSource

print "Starting NSApplicationMain"
NSApplicationMain(sys.argv)
print "done"
