te: this information is relevant to `py2app`_ 0.1.2 - which is currently just on the `svn trunk`_)

In order to see how hard it would be to package a complicated application such as `wxGlade`_, I decided to give it a try.  `wxGlade`_ is quite a dynamic beast with regard to code generation and widget plugins, so it was a bit of a pain to deal with.  I actually had to add several features to `py2app`_ in the process:

* A feature where one module can be "aliased" to another module.  I needed this because wxPython.wx points to wx, but is not actually on the filesystem.
* An extensible module filtering system, so a recipe can say "yes" or "no" to any extension or python module it comes across.  Before this, there was only one static filter that would say "no" to standard library modules when using a vendor Python.

`wxGlade`_ causes problems because it needs to list the "codegen" and "widgets" directories, and load code from them.  This would be easy if:

* The path were configurable in some way (using sys.path, a separate variable, etc.).  Packages go into .../Python/site-packages/, where it expected to see them at .../
* The list of modules were configurable in some way (right now it expects to perform an os.listdir)

The naive way would be to just include them as data files, however this prevents dependency analysis from occurring.  It turns out that `wxGlade`_ did indeed cause new dependencies in these modules so a more complicated solution was required.  The solution to this particular problem is in three parts:

1. Add "codegen" and "widgets" as data files
2. Add a wxglade recipe that scans all of these plugins for dependencies
3. Have the wxglade recipe install a filter that makes sure these dependencies aren't copied into the normal place

The other customization I used was a custom boot script, wxGlade.py.  This boot script does two things:

1. Starts up wxGlade as per wxglade.py, but in a simpler way (less is needed, the environment is already sane)
2. Monkeypatches a bug in `wxGlade`_ so that it can open the help files

Note that setup.py expects a `wxGlade 0.3.4`_ distribution to be unpacked in ./wxGlade-0.3.4

.. _`py2app`: http://undefined.org/python/#py2app
.. _`svn trunk`: http://svn.red-bean.com/bob/py2app/trunk
.. _`wxGlade`: http://wxglade.sourceforge.net/
.. _`wxGlade 0.3.4`: http://sourceforge.net/project/showfiles.php?group_id=58225&package_id=54072&release_id=264401
