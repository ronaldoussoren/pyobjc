#
#  ÇPROJECTNAMEASIDENTIFIERÈ.py
#  ÇPROJECTNAMEASIDENTIFIERÈ
#

from PyObjCTools import NibClassBuilder, AppHelper
from Foundation import NSBundle

info = NSBundle.mainBundle().infoDictionary()[u'PyObjCXcode']

for nibFile in info[u'NIBFiles']:
    NibClassBuilder.extractClasses(nibFile)

for pythonModule in info[u'Modules']:
    __import__(pythonModule)

if __name__ == '__main__':
    AppHelper.runEventLoop()