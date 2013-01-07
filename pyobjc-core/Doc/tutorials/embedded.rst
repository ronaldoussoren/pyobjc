=============================================================
Tutorial - Adding Python code to an existing ObjC application
=============================================================

In this tutorial we are going to take an existing ObjC application and
add Python and PyObjC to it.  One of the reasons why you may want to do
this is because some things are much simpler in Python than in ObjC, mainly
due to the rich library Python has.

To follow the tutorial you need:

 * PyObjC 1.3.1
 * py2app 0.2 or later (included in the binary installer for PyObjC)
 * Python 2.3 or later (note: PyObjC is NOT compatible with MacPython-OS9)
 * Mac OS X 10.3 or later
 * Xcode Tools

If you do not have a ``/Developer`` folder, then you do not have Xcode Tools
installed. On MacOSX 10.7 or later you can download Xcode from the App Store,
see `Apple's developer website <https://developer.apple.com/xcode/>` for
more information.

The application we are going to modify is Apple's SimpleComboBox example.
This example shows you how to use combo boxes, but that is not what interests
us right now: the application pretends to be a database application that allows
you to keep notes (such as track list) for your CD collection.  With such an
application it feels silly that even though you want to type notes on
the CD you are currently playing in iTunes you still have to retype
album title, artist and genre.  This is what we are going to fix: we
are going to add a button "ask iTunes", which will use Python's
AppleScript support to ask iTunes about the currently playing track
and fill in the fields for you.  

Follow these steps:

.. note:: Before you start, download the :download:`reference source package <embedded_src.zip>` for this tutorial.

1. Make a copy of ``/Developer/Examples/AppKit/SimpleComboBox`` to work on.
   Let's call this ``SimpleComboBoxPlus``:

   .. sourcecode: sh
   
      $ cp -R /Developer/Examples/AppKit/SimpleComboBox SimpleComboBoxPlus

  From this point on, all shell commands take place from this
  ``SimpleComboBoxPlus`` folder.
    
2. Open it in Xcode, build it, and see what it does.

3. Open ``CDInfoDocument.nib``.  Select the Class View, ``NSObject``, subclass
   as ``ITunesCommunication``.  Give the class an ``askITunes:`` action.
   Instantiate the class as object ``ITunesCommunication``.  This wll be the
   class that we write in Python.
   
4. Go to the object view again, open the Window.

5. Move the text box down a bit to make space, add a button "ask iTunes".

6. Connect this button to the ``askITunes:`` action of the
   ``ITunesCommunication`` object.
    
7. We now need to write the code implementing the ``ITunesCommunication``
   class.  As this tutorial is about using PyObjC in existing ObjC programs
   and not about PyObjC itself, we are going to skip writing the code and
   simply copy ``ITunesCommunication_1.py`` to ``ITunesCommunication.py``.

8. Now we need to create the build script for our plugin, create a file named
   ``setup.py`` with the following contents:

   .. sourcecode:: python

        from distutils.core import setup
        import py2app

        setup(
            plugin = ['ITunesCommunication.py']
        )   

   You may also copy this file from ``setup.py``. 

9. Run the setup script to create a temporary plugin bundle for development:

   .. sourcecode: sh

        $ python setup.py py2app -A

   Note that we use the ``-A`` argument to create an alias plugin bundle at
   ``dist/ITunesCommunication.py``.  Alias bundles contain an alias to the
   main script (``ITunesCommunication.py``) and symlinks to the data files
   (none in this case).  This allows us to keep working on the source files
   without having to rebuild the application.  This alias bundle is similar
   to a ZeroLink executable in Xcode - it is for DEVELOPMENT ONLY, and will
   not work on other machines.

10. Add ``dist/ITunesCommunication.plugin`` to the Resources folder in your
    Xcode project.  You can do this by ctrl-clicking the Resources folder
    and choosing "Add Existing Files...".  Make sure to choose
    "Create Folder References for any added folders".

11. Open ``main.m``, it is in the "Other Sources" folder in your Xcode
    project, and change the main(...) function to the following:

    .. sourcecode:: objective-c

        int main(int argc, const char *argv[]) {
            NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
            NSString *pluginPath = [[NSBundle mainBundle]
                                        pathForResource:@"ITunesCommunication"
                                                 ofType:@"plugin"];
            NSBundle *pluginBundle = [NSBundle bundleWithPath:pluginPath];
            [pluginBundle load];
            [pool release];
            return NSApplicationMain(argc, argv);
        }


    You may also copy a full main.m from ``main.m``.  This code ensures
    that our ITunesCommunication plugin is loaded before the nib
    files.

12. Build and run.  When you press the "Ask iTunes" the "CD Title" and
    "Band Name" fields will be filled with one of the best albums of the last
    few years :-)
    
13. Now we need to make the program talk to iTunes.  The current MacPython
    interface to the Open Scripting Architecture requires an extra step when
    compared to AppleScript: you need to manually generate a Python package
    that wraps all the AppleScript terminology for an application.  To make
    matters more complicated iTunes is one of those special cases where the
    standard way to generate this package (start the application, ask it for
    its terminology) does not work, so we have to actually look into the
    bowels of ``iTunes.app``.  This leads to the following hefty command line
    which you should run in the ``SimpleComboBoxPlus`` directory:

    .. sourcecode:: sh
    
        $ cd SimpleComboBoxPlus
        $ pythonw -c "from gensuitemodule import main;main()" \
            --output iTunes --creator hook --resource \
            /Applications/iTunes.app/Contents/Resources/iTunes.rsrc
    
14. Finally, add the code to ``ITunesCommunication.py`` to actually communicate
    with iTunes.  We cop out and copy it from ``ITunesCommunication_2.py``.
    
15. Build and run.  If you press the button when iTunes is playing the Title
    and Band names will be filled, otherwise they will be cleared.  In a real
    application you would disable the "Ask iTunes" button unless iTunes was
    active.  All that is left as an exercise to the reader.

16. To make this application redistributable, perform the following commands
    to make the plugin redistributable:

    .. sourcecode:: sh

        $ rm -rf dist
        $ python setup.py py2app

    Then, from Xcode, clean your project (shift-cmd-K), switch to Deployment
    mode, and rebuild.
 
A minor variation
-----------------

There a several projects that improve upon the built-in AppleScript support
(or to be more precise "application scripting support").  One of those is
`AppScript`_.

.. _`AppScript`: http://appscript.sourceforge.net

When you have this module installed you can replace the contents of
``ITunesCommuncation.py`` with ``ITunesCommunication_AppScript.py``,
and you can skip step 13 entirely.
