import os
import shutil
from distutils.command.install import install

CRUFT = """
objc
Foundation
AppKit
AddressBook
autoGIL
"""

class pyobjc_install(install):
    def run(self):
        install.run(self)
        # Hack to remove a previous version that may have been installed
        install_dir = self.install_platlib
        if install_dir is None:
            return

        # clean up cruft from pre 0.9
        for name in CRUFT:
            path = os.path.join(install_dir, name)
            if os.path.isdir(path):
                print "(removing old version: %s)" % (path,)
                shutil.rmtree(path)
            elif os.path.isfile(path):
                print "(removing old version: %s)" % (path,)
                os.remove(path)

        install_dir = os.path.join(install_dir, 'PyObjC')
        if not os.path.exists(install_dir):
            return

        # In version 1.2 some of the extension modules moved, 
        # clean up the old location
        for fn in os.listdir(install_dir):
            fn = os.path.join(install_dir, fn)
            if fn.endswith('.so'):
                print "(removing old version: %s)" % (fn,)
                os.unlink(fn)

cmdclass = dict(install=pyobjc_install)
