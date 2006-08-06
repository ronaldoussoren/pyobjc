import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, Extension

LONG_DESCRIPTION="""
Wrappers for the launch library on Mac OS X 10.4 or later.  
"""

CLASSIFIERS = filter(None,
"""
Development Status :: 5 - Production/Stable
Environment :: Console
Environment :: MacOS X
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Natural Language :: English
Operating System :: MacOS :: MacOS X
Programming Language :: Python
Topic :: Software Development :: Libraries :: Python Modules
""".splitlines())


def grep_version():
    fp = open("Lib/launch/__init__.py", "r")
    for ln in fp:
        if ln.startswith("__version__"):
            return ln.split('=')[-1].strip()[1:-1]


setup(
    name="macosx-launch",
    version=grep_version(),
    description="Wrapper for the launch library in MacOSX 10.3 or later",
    long_description=LONG_DESCRIPTION,
    author="Ronald Oussoren",
    author_email="ronaldoussoren@mac.com",
    # url=
    platforms=[ "MacOS X" ],
    ext_modules=[
        Extension("launch._launch", [ 'Modules/_launch.c']),
    ],
    packages = ['launch'],
    package_dir = { '': 'Lib' },
    classifiers = CLASSIFIERS,
    license = "MIT License",
    # download_url=
)



