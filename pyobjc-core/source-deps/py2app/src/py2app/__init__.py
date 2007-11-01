"""
builds Mac OS X application bundles from Python scripts

New keywords for distutils' setup function specify what to build:

    app
        list of scripts to convert into gui app bundles

py2app options, to be specified in the options keyword to the setup function:

    optimize - string or int (0, 1, or 2)

    includes - list of module names to include
    packages - list of packages to include with subpackages
    ignores - list of modules to ignore if they are not found
    excludes - list of module names to exclude
    dylib_excludes - list of dylibs and/or frameworks to exclude
    resources - list of additional files and folders to include
    plist - Info.plist template file, dict, or plistlib.Plist
    dist_dir - directory where to build the final files

Items in the macosx list can also be
dictionaries to further customize the build process.  The following
keys in the dictionary are recognized, most are optional:

    script (MACOSX) - list of python scripts (required)
    dest_base - directory and basename for the executable
                if a directory is contained, must be the same for all targets
"""

__version__ = "0.2.5"

import py2app.install
