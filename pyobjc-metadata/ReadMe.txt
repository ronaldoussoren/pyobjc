pyobjc-metadata is a project for generating metadata files for PyObjC. It
features a script for parsing framework headers and extracing metadata (such
as constant values and function definitions) from these.

The actual metadata format is shared between RubyCocoa and PyObjC. A short
description of this format is found in the document directory of this project.

There are four scripts:

* pyobjc-wrapper-gen

  This script is used to create a python project that wraps a single framework.

* pyobjc-metadata-gen

  This is the actual workhorse and extracts metadata from frameworks.

* pyobjc-metadata-lint

  This script checks the contents of a ".bridgesupport" file and reports on
  problems in the metadata.

* pyobjc-metadata-overrides

  This tool can be used to calculate PyObjCOverrides.bridgesupport from 
  a PyObjC metadata file and system metadata.

Wrapping a framework
--------------------

Wrapping a framework is fairly easy. You start with running the generator
script::

  $ pyobjc-wrapper-gen -f MyFramework

This will create 'pyobjc-framework-MyFramework' in the current directory (
run ``pyobjc-wrapper-gen -h`` to see how you can change these defaults).

Now start by edition ``setup.py``: this contains some PyObjC-specific defaults.

Then edit ``Exceptions/MyFramework.xml``, which contains metadata exception
data. If the framework doesn't contain complicated code this file may well be
empty. If it isn't empty you need to check and update its contents.

If you changed the contents run the following command to update the actual
metadata::

  $ python setup.py update_metadata

You can also update the exception data (for example when you're transitioning
to a new version of the framework):

  $ python setup.py update_exceptions

To make sure that the wrapper is correct you should also add some unittest,
add them to modules in ``Lib/MyFramework/test``, there's already a template
test-file in there. To run the unittests::

  $ python setup.py test

Known issues
------------

The script ``pyobjc-metadata-gen`` is rather slow because it builds runs loads 
of small programs to detect values for features (enum values, encodings for
types and more).  This could be sped up by batching work into several larger
programs, but at the cost of increasing complexity. As these scripts won't be
used much anyway I prefer to keep the scripts as simple as possible.

The header-scanning code tends to barf on input it doesn't understand. There is
(by design) no flag to avoid this. The only way around this is fixing the 
generator or tweaking headers until the scanner is happy.  

The wrapper generator sometimes hangs as well (makes no progress whatsoever,
I'm not sure yet what causes this and it might be a problem in subprocess)

Not all metadata is implemented at the moment.
