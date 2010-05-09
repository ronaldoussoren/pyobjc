======================================
Understanding existing PyObjC examples
======================================

Introduction
------------

This tutorial is aimed primarily at people with little or no background
in Objective-C and Cocoa, and it will help you to understand PyObjC programs
written by other people, such as the examples included with the distribution.
This document is actually not a true tutorial: you do not get to build anything,
only read and examine things.

It is strongly suggested that you first do the
:doc:`Creating your first PyObjC application <firstapp>` tutorial to get some hands-on
experience with PyObjC, Cocoa and especially Interface Builder.

Model-View-Controller
---------------------

If you have used another GUI toolkit in the past it is essential that
you understand that Cocoa is different.  For this once this isn't
marketing-speak: Cocoa is inherently different from common toolkits such as
Tk, wxWindows, Carbon, MFC, etc.  Apple's documentation explains this, but
such introductory text is often skipped.  It is a good idea to refer back to
`Application Architecture`__ after reading this section.  If you want, you can
write code that does not follow the Model-View-Controller paradigm, but you
would be on your own.  Cocoa and Interface Builder are designed to suit this
model.

.. __: http://developer.apple.com/documentation/Cocoa/Conceptual/AppArchitecture/index.html

Cocoa is built on the Model-View-Controller paradigm (MVC).  What this means
is that the application code should be split into three parts:

-   The *Model* is the storage of and operations on the data.  The model
    could be as complicated as a large database, or as simple as a
    currency conversion function that only knows how to multiply two floating
    point numbers, as in the Currency Converter application built in the first
    tutorial.

-   The *View* is what the user sees and interacts with on-screen.

-   The *Controller* is the glue that binds the Model and the View together.
    In the Currency Converter tutorial it is the callback that is triggered
    when the user presses the "Convert" button, which gets the data from the
    "amount" and "rate" fields of the View, passes them to the Model for
    computation and sends the result back to the View.
  
To summarize: the Model knows nothing about the user, the View knows nothing
about the data and operations, and the Controller only knows how to relate
the Model and the View.  For really tiny applications, such as the currency
converter, it may be tempting to do away with the Model and simply put that
code in the Controller.  You probably shouldn't do this, as it can make
your code harder to read since it will be a mix of algorithms and glue code,
however there is no technical limitation that prevents you from doing this.
If you do combine the functionality of the model and controller, it is
customary to name it as if it represented the document (without "Controller").
Note that the MVC paradigm is not specific to Cocoa and can be used with almost
any GUI toolkit, but Cocoa is explicitly designed for this paradigm.

You should have an MVC trio for every distinct unit of information in your
program.  In case of a simple dialog-style application such as Currency
Converter you will have one such trio.  Most applications, however, will have
at least two: one for the application itself and one for the "documents" the
application handles.  These may be real documents (i.e. files), but a document
can be more abstract.  For example, if your application does scientific
simulations that run in separate windows, each simulation could be a document.

The NIB file
------------

Cocoa and Interface Builder strongly encourage you to use a NIB file
per MVC trio.   You should follow this encouragement unless you are sure
that you know what you are doing.

This brings us to the second big difference between Cocoa and other GUI
toolkits: almost all of the boilerplate code is replaced by the NIB.
The source of Cocoa programs that do little work, especially example programs,
will typically be much shorter than the equivalent with other toolkits.

The NIB file is *not* a description of dialogs and menus and buttons, as you 
would get out of interface-builders for other toolkits.  A NIB file is more:
it contains a archived object graph that represents the GUI, conceptually
similar to a pickle in Python.  You tell Interface Builder
about all the relevant classes in your application, the instances you
want to create from those classes, and how the classes should connect to
each other.  Interface Builder the actually instantiates the classes, makes
all the connections and at that point freezes and stores the whole lot.

Unarchival of a NIB happens in two phases.  The objects are restored using the
``NSCoding`` protocol (``initWithCoder:`` is similar to ``__setstate__`` of
Python's ``pickle`` protocol), and then each object is sent an
``awakeFromNib:`` message so that they may do any initialization that depends
on a fully restored object graph (``pickle`` does not have this functionality
built-in).

The section above explains a lot of the strangeness in AppKit-based PyObjC
applications:

*   Windows and dialogs are typically not explicitly created, because they were
    instantiated by the NIB.

*   Initialization is not always done in ``__init__`` or equivalent, because
    the object graph may not be completely unarchived until the first
    ``awakeFromNib:`` is called.

*   Attributes that reference other objects are not typically set explicitly,
    but are done by the NIB file during unarchival.
	
This also explains why you want separate NIB files for each MVC trio:
the objects and classes in a NIB file are all unarchived together.  In other
words, if you had created your document window in your application NIB
(even if you set it to "hidden" initially so it does not show up) it would
become very difficult to create a second window for a new document.

If you think about the consequences of this section for a while it will
become clear why all the boilerplate code is missing from Cocoa applications:
you don't need it.  Like the output of other gui-builders, a NIB usually
contains enough information to recreate the view objects, but a NIB can also
contain a large proportion of the setup for your Model and Controller
functionality.  This is especially true when using `Cocoa Bindings`__.

.. __: http://developer.apple.com/documentation/Cocoa/Conceptual/CocoaBindings/

Delegates
---------

If you are familiar with other object-oriented GUI toolkits such as MFC
another thing to notice is that Cocoa applications often use a *delegate*
object where other toolkits would use a subclass.  For example: it is not
common to use your own subclass of ``NSApplication`` for the main application
object.  ``NSApplication`` objects have a helper called its ``delegate``.
The application object will attempt to inform its delegate many interesting
events, and the delegate implements only the methods for the events it is
interested in.

For example, the method ``applicationShouldTerminate:`` of the delegate
is called just before the application quits, and it has a chance to return
``NO`` if it is not appropriate to quit just yet.

Examining a NIB file
--------------------

Let us examine the final NIB of the Currency Converter tutorial with this in
mind.  If you open it and look at the main window (titled "MainMenu.nib")
and select the "Instances" pane you should see six objects.  Two of these
have greyed-out names ("File's Owner" and "First Responder"), these are present
in every nib can not be changed.  The "File's Owner" is either the Controller
or the combined Model-Controller object, and is specified by the application
when it loads the NIB.  For the main nib, which is loaded automatically by
``NSApplicationMain`` or ``PyObjCTools.AppHelper.runEventLoop``, this will be
the instance of ``NSApplication``.  Currency Converter is not a document-based
application, so the MVC trio for the conversion window are in here too.  These
are named ``Converter``, ``Window`` and ``ConverterController`` respectively.

Let us have a look at the ``ConverterController`` object by double clicking it.
The "MainMenu.nib" window goes to the "Classes" tab, and an info window shows
up.  In the "MainMenu.nib" window the ``ConverterController`` class is
selected, and you can see it is a subclass of ``NSObject``.  Having the same
name for the class and the instance is common in Cocoa programs, the main
exception being the File Owner object.

The info window shows more information on the ``ConverterController`` class.
It should pop open to the "attributes" page.  In the "Outlets" tab you see that
instances of this class have four attributes, ``converter``, ``rateField``,
``dollarField`` and ``totalField``.  In any instance of ``ConverterController``
you can connect these to other objects, as we shall see below.  The "Actions"
tab shows that there are two methods ``convert:`` and ``invertRate:``, and
again you can arrange for these to be called on instances of your
``ConverterController`` on certain events by making connections.

So let us now look at the connections for our ``ConverterController``
*instance*.  Select the "Instances" tab in the main window, select
``ConverterController`` and set the info window to show "Connections".  You 
now see all the outlets defined in the class.  Select one, and in the lower 
half of the info window you will see which object it connects to.  Moreover, a 
blue line will also link the object representations in the main window and
in the dialog preview window.

Finding out who calls your ``convert:`` method is more difficult, though, with
this view.  But, if you select the "Convert" button in the dialog you will see
that its ``target`` action will go to the ``ConverterController.convert_``
method.

Luckily there is a way to find such incoming connections without reverting to
guessing.  For instance, you will be hard put to find who, if anyone, calls 
``ConverterController.invertRate_``.  The solution: go to the "MainMenu.nib"
window and look at the top of the vertical scrollbar.  There are two little
icons there, one with lines and one with squares, with the squares being
highlighted.  Press it.  The view will change to a scrollable list with objects 
in the left column and an indication of connections in the right column.  You
can now see our ConverterController object has four outgoing connections (the
ones we found earlier) and two incoming connections.  Click on the incoming
connections icon.  The view will change again and ConverterController will
probably scroll out of sight.  Locate it, and see that there are two lines
going out of the ConverterController object.  One goes to ``NSButton(Convert)``
and is labeled ``convert:``, we knew about that already.  The other one goes to
an object ``NSMenuItem(Invert Exchange Rate)`` and is labeled ``invertRate:``,
so that is where calls to ``invertRate:`` come from.  And if you look at where
this ``NSMenuItem`` sits in the object hierarchy you find that it is an entry
in the "Edit" menu in the menubar.

Examining an Apple example
--------------------------

This section remains to be written.  Contributions will be gratefully accepted
:-)
