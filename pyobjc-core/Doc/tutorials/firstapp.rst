=======================================
Creating your first PyObjC application.
=======================================

.. warning::
   
   This document is old and hasn't been updated for modern versions of
   PyObjC and Apple's developer tools.

In this tutorial you will learn how to create your first Python Cocoa
application: a simple dialog that allows you to convert amounts of money from
one currency to another.  Definitely easier to do with a calculator, but in the
process of following the tutorial you will learn which bits of Apple's Cocoa
documentation apply to PyObjC and which bits are different, and how to adapt
the different bits to PyObjC from Objective-C.

To follow the tutorial you need:

 * PyObjC 1.3.1
 * py2app 0.2 or later (included in the binary installer for PyObjC)
 * Python 2.3 or later (note: PyObjC is NOT compatible with MacPython-OS9)
 * Mac OS X 10.2 or later
 * Xcode Tools (was Developer Tools for Mac OS X 10.2)

If you do not have a ``/Developer`` folder, then you do not have Xcode Tools
installed.  See `Apple's developer website <https://developer.apple.com/xcode/>`
for more information on getting Xcode.

Getting Started
---------------

.. note:: Before you start, download the :download:`reference source package <firstapp_src.zip>` for this tutorial.

1. Create a work directory ``src``.  Check which Python you have installed
   PyObjC for, by running ``python`` and checking that ``import Foundation``
   works.  If it does not work it could be that you have installed PyObjC for
   ``/usr/local/bin/python`` but Apple's ``/usr/bin/python`` comes first in
   your ``$PATH``.  Make sure you use the right python wherever it says
   ``python`` in this tutorial.
   
2. Start Interface Builder, select *Cocoa Application*
   in the new file dialog, save this file as ``src/MainMenu.nib``.
   
3. Proceed with the instructions as lined out in Apple's
   `Developing Cocoa Objective-C Applications: a Tutorial`_, `chapter 3`_,
   just after the section "*Creating the Currency Converter Interface*".
   Work through "Defining the Classes of Currency Converter", "Connecting
   ConverterController to the Interface", and stop at
   "*Implementing the Classes of Currency Converter*", as we are going to do
   this in Python, not Objective-C.  Your nib file should now be the same as
   *step3-MainMenu.nib*.
   
.. _`Developing Cocoa Objective-C Applications: a Tutorial`: http://developer.apple.com/documentation/Cocoa/Conceptual/ObjCTutorial/index.html
.. _`chapter 3`: http://developer.apple.com/documentation/Cocoa/Conceptual/ObjCTutorial/index.html?http://developer.apple.com/documentation/Cocoa/Conceptual/ObjCTutorial/chapter03/chapter_3_section_1.html

4. Create the skeleton Python script by running the ``nibclassbuilder`` script.
   ``nibclassbuilder`` will parse the NIB file and create a skeleton module for
   you.  Invoke it as follows (from the ``src`` directory):

   .. sourcecode:: sh
   
       $ python -c "import PyObjCScripts.nibclassbuilder" MainMenu.nib > CurrencyConverter.py
               
   Depending on your installation, the ``nibclassbuilder`` script may be on your ``$PATH``.
   If so, it can be invoked as such:

   .. sourcecode:: sh

       $ nibclassbuilder MainMenu.nib > CurrencyConverter.py
   
   The result of this can be seen in *step4-CurrencyConverter.py*.

Testing the user interface
--------------------------

5. Now we need to create an build script for CurrencyConverter.  To do this,
   create a file named ``setup.py`` with the following contents:

   .. sourcecode:: python
      :linenos:
   
        from distutils.core import setup
        import py2app

        setup(
            app=['CurrencyConverter.py'],
            data_files=['MainMenu.nib'],
        )

   The result of this can be seen in *step5-setup.py*.

6. Run the setup script to create a temporary application bundle for
   development:

   .. sourcecode:: sh

        $ python setup.py py2app -A
      
   Note that we use the ``-A`` argument to create an alias bundle at 
   ``dist/CurrencyConverter.app``.  Alias bundles contain an alias to the
   main script (``CurrencyConverter.py``) and symlinks to the data files
   (``MainMenu.nib``), rather than including them and their dependencies
   into a standalone application bundle.  This allows us to keep working on
   the source files without having to rebuild the application.  This alias
   bundle is similar to a ZeroLink executable for Xcode - it is for
   DEVELOPMENT ONLY, and will not work on other machines.
   
7. Run the program.  This can be done in three ways:

   - double-click ``dist/CurrencyConverter`` from the Finder
     (you won't see the .app extension)

   - open it from the terminal with:

     .. sourcecode:: sh
   
        $ open dist/CurrencyConverter.app
       
   - run it directly from the Terminal, as:

     .. sourcecode:: sh
   
        $ ./dist/CurrencyConverter.app/Contents/MacOS/CurrencyConverter
       
   The last method is typically the best to use for development: it leaves
   stdout and stderr connected to your terminal session so you can see what
   is going on if there are errors, and it allows you to interact with ``pdb``
   if you are using it to debug your application.  Note that your application
   will likely appear in the background, so you will have to cmd-tab or click
   on its dock icon to see its user interface.
   
   The other methods cause stdout and stderr to go to the Console log, which
   can be viewed with ``/Applications/Utilities/Console.app``.
   
   When you run your script as it is now it should behave identically as when
   you tested your interface in Interface Builder in step 3, only now the
   skeleton is in Python, not Objective-C.
   

Writing the code
----------------

8.  Time to actually write some code.  Open ``CurrencyConverter.py`` in your
    favorite text editor.  Follow Apple's documentation again, chapter 3,
    section "Implementing Currency Converter's Classes".  To translate this
    Objective C code to Python syntax, we will need to do some name mangling of
    the selectors.  See *An introduction to PyObjC* for the details, but the
    short is that:

    .. sourcecode:: objective-c

        [anObject modifyArg: arg1 andAnother: arg2]

   translates into the following Python code, by replacing the colons in the
   selector with underscores, and passing the arguments as you would with a
   normal Python method call:

   .. sourcecode:: python

        anObject.modifyArg_andAnother_(arg1, arg2)
   
   Note that we don't do this mangling for ``Converter.convertAmount()``: this
   method is only called by other Python code, so there is no need to go
   through the name mangling.  Also, if we would want to make this method
   callable from ObjC code we may have to tell the PyObjC runtime system about
   the types of the arguments, so it could do the conversion.  This is beyond
   the scope of this first tutorial, *An introduction to PyObjC* has a little
   more detail on this.
   
   The application should now be fully functional, try it.  The results of what
   we have up to now can be seen in *step8-CurrencyConverter.py*.
   
Extending the functionality
---------------------------

9.  We are going to add one more goodie, just to show how you edit an existing
    application.  The main problem, which may be obvious, is that we cannot run
    ``nibclassbuilder`` again because we would destroy all the code we wrote in
    steps 5 and 8, so we do this by hand.  What we are going to do is add an
    "invert rate" command, because I always get this wrong: instead of typing
    in the exchange rate from dollars to euros I type in the rate to convert
    from euros to dollars.
   
    Open ``MainMenu.nib`` in Interface Builder.  Select the *Classes* view and
    then select the ``ConverterController`` class.  In the info panel select
    the *Attributes* from the popup.  Select the *Actions* tab, and add an
    action ``invertRate:``.  You have now told Interface Builder that instances
    of the ``ConverterController`` class have grown a new method
    ``invertRate_()``.
   
    In the ``MainMenu.nib main`` window open the *MainMenu* menubar.  Select
    the ``Edit`` menu.  Make sure the *Menus* palette is open and selected,
    drag a separator to the ``Edit`` menu and then drag an ``Item`` there.
    Double-click the item and set the text to ``Invert Exchange Rate``.
   
    Make the connection by control-dragging from the new
    ``Invert Exchange Rate`` menu item to the ``ConverterController`` instance
    in the Instances tab in the ``MainMenu.nib`` main window.

    *NOTE:* you drag to the *instance* of ``ConverterController``, not to the
    class.

    In the *Info* panel, *Connections* section, select ``invertRate:`` and
    press *Connect*. 
   
10. We know our program can't invert rates yet, because we haven't actually
    written the code to do it, but we are going to try it anyway, just to see
    what sort of spectacular crash we get.  Alas, nothing spectacular about it:
    when the NIB is loaded the Cocoa runtime system tries to make the
    connection, notices that we have no ``invertRate_()`` method in our
    ``ConverterController`` class and it gives an error message:

    .. sourcecode:: sh
       
       $ ./dist/CurrencyConverter.app/Contents/MacOS/CurrencyConverter 
       2004-12-09 03:29:09.957 CurrencyConverter[4454] Could not connect the action 
       invertRate: to target of class ConverterController
   
    Moreover, it has disabled the ``Invert Exchange Rate`` menu command and
    continues, so the program works as it did before, only with one more
    (disabled) menu item.
   
Debugging
---------

11. Writing the code is easy: add a method ``invertRate_(self, sender)`` that
    gets the float value of ``rateField``, inverts it and puts it back.  We
    deliberately forget to test for divide by zero.  We run the program again,
    and now the menu entry is enabled.  After trying it with a couple of
    non-zero exchange rates we try it with an exchange rate of zero (or empty,
    which is the same).  We get a dialog box giving the Python exception, and
    offering the choice of continuing or quitting. 
    
    To debug this application with pdb, start the application with the
    following command line:

    .. sourcecode:: sh

        $ env USE_PDB=1 ./dist/CurrencyConverter.app/Contents/MacOS/CurrencyConverter

    When running in this mode, we will get a ``pdb.post_mortem(...)`` console
    in the terminal instead of the alert panel.  You can see this in action if
    you try and invert an exchange rate of ``0``.
      
12. Fix the final bug by testing for ``rate == 0.0`` in ``invertRate_()``.
    The result is in the *step12-src* directory.
   
Creating a redistributable application
--------------------------------------

Your application is finished, and you want to run it on other computers, or
simply just move it to the ``Applications`` folder (or anywhere else) and
insulate it from the original source code.

This can be done with the following steps from the ``src`` directory:

 .. sourcecode: sh

    $ rm -rf dist
    $ python setup.py py2app

Now the application bundle located at ``dist/CurrencyConverter.app`` is a fully
standalone application that should run on any computer running the same major
version of Mac OS X or later.  This means that applications built on
Mac OS X 10.2 are compatible with Mac OS X 10.3, but NOT vice versa.  If you
are not using an Apple-supplied version of Python, a subset of your Python
installation will be included in this application.

For more complicated examples of py2app usage to do things such as change the
application's icon, see the Examples or the py2app documentation.
