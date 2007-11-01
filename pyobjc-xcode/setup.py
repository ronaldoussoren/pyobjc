''' 
Xcode integration for  Python/PyObjC

This package provides a number of Xcode project and file templates that make
it easier to develop (GUI) Python programs using Xcode.

The templates won't be installed in the right location. Run 
``pyobjc-xcode-install`` after installing this package to install the templates
in the right location. Use ``pyobjc-xcode-uninstall`` to uninstall the templates
again.
'''


import ez_setup
ez_setup.use_setuptools()

from setuptools import setup

setup(
    name='pyobjc-xcode',
    version='2.0',
    description = "Xcode integration for pyobjc",
    long_description = __doc__,
    author='bbum, RonaldO, SteveM, LeleG, many others stretching back through the reaches of time...',
    author_email='pyobjc-dev@lists.sourceforge.net',
    url='http://pyobjc.sourceforge.net',
    platforms = [ "MacOS X" ],
    packages = [ 'PyObjCTools', ], 
    namespace_packages = [ 'PyObjCTools' ],
    package_dir = { '': 'Lib' },
    install_requires = [ 
        'pyobjc-core>=2.0' 
    ],
    dependency_links = [],
    package_data = { 
        '': ['*.bridgesupport'] 
    },

    entry_points = {
        'console_scripts': [
            'pyobjc-xcode-install = PyObjCTools.XcodeSupport._scripts:install',
            'pyobjc-xcode-uninstall = PyObjCTools.XcodeSupport._scripts:uninstall',
        ],
    },

    # This package is not zip-safe by design: the actual templates are in 
    # the package data and must be in a normal filesystem to be able to use
    # them from Xcode.
    zip_safe = False,
    include_package_data = True
)
