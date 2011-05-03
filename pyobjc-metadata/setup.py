import ez_setup
ez_setup.use_setuptools()

from setuptools import setup
import sys

CLASSIFIERS = filter(None,
"""
Development Status :: 5 - Production/Stable
Environment :: Console
Environment :: MacOS X :: Cocoa
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Natural Language :: English
Operating System :: MacOS :: MacOS X
Programming Language :: Python
Programming Language :: Objective C
Topic :: Software Development :: Libraries :: Python Modules
Topic :: Software Development :: User Interfaces
""".splitlines())

install_requires = [ 'pyobjc-core>=2.0' ]
if sys.version_info[:2] <  (2,5):
    install_requires.append('elementtree')

setup(
        name='pyobjc-metadata',
        version='2.0',
        description='Metadata tools for PyObjC',
        long_description=open('ReadMe.txt', 'r').read().strip(),
        author="Ronald Oussoren",
        author_email="pyobjc-dev@lists.sourceforge.net",
        url="http://pyobjc.sourceforge.net/",
        platforms=['MacOS X'],
        entry_points = {
            'console_scripts': [
                "pyobjc-metadata-gen=PyObjCMetaData.scanframework:main",
                "pyobjc-wrapper-gen=PyObjCMetaData.genwrapper:main",
                "pyobjc-metadata-lint=PyObjCMetaData.lint:main",
                "pyobjc-metadata-overrides=PyObjCMetaData.overrides:main",
            ],
        },
        package_dir={
            '': 'Lib',
        },
        packages =  [ 
            'PyObjCMetaData' 
        ],
        setup_requires = [
        ],
        install_requires = install_requires,
        download_url = 'http://pyobjc.sourceforge.net/software/index.php',
        options = {
            'egg_info': { 'egg_base': 'Lib' },
        },
        classifiers = CLASSIFIERS,
        license = 'MIT License',
        zip_safe = True,
        dependency_links = [],
)
