<?
    $title = "Understanding existing PyObjC examples";
    $cvs_author = '$Author: ronaldoussoren $';
    $cvs_date = '$Date: 2003/07/05 14:59:47 $';

    include "header.inc";
?>
<h1 class="title">Understanding existing PyObjC examples</h1>
<div class="section" id="introduction">
<h3><a name="introduction">Introduction</a></h3>
<p>This tutorial is aimed primarily at people with little or no background
in Objective-C and Cocoa, and it will help you to understand PyObjC programs
written by other people, such as the examples included with the distribution.
This document is actually not a true tutorial: you do not get to build anything,
only read and examine things.</p>
<p>It is strongly suggested that you first do the
<a class="reference" href="tutorial/tutorial.html">Creating your first PyObjC application</a> tutorial to get some hands-on
experience with PyObjC, Cocoa and especially Interface Builder.</p>
</div>
<div class="section" id="model-view-controller">
<h3><a name="model-view-controller">Model-View-Controller</a></h3>
<p>If you have used another GUI toolkit in the past it is essential that
you understand that Cocoa is different.  For this once this isn't
marketing-speak: Cocoa is inherently different from common toolkits such as
Tk, wxWindows, Carbon, MFC, etc.  Apple's documentation explains this, but
such introductory text is often skipped.  It is a good idea to refer back to
<a class="reference" href="http://developer.apple.com/documentation/Cocoa/Conceptual/AppArchitecture/index.html">Application Architecture</a> after reading this section.  If you want, you can
write code that does not follow the Model-View-Controller paradigm, but you
would be on your own.  Cocoa and Interface Builder are designed to suit this
model.</p>
<p>Cocoa is built on the Model-View-Controller paradigm (MVC).  What this means
is that the application code should be split into three parts:</p>
<ul class="simple">
<li>The <em>Model</em> is the storage of and operations on the data.  The model
could be as complicated as a large database, or as simple as a
currency conversion function that only knows how to multiply two floating
point numbers, as in the Currency Converter application built in the first
tutorial.</li>
<li>The <em>View</em> is what the user sees and interacts with on-screen.</li>
<li>The <em>Controller</em> is the glue that binds the Model and the View together.
In the Currency Converter tutorial it is the callback that is triggered
when the user presses the &quot;Convert&quot; button, which gets the data from the
&quot;amount&quot; and &quot;rate&quot; fields of the View, passes them to the Model for
computation and sends the result back to the View.</li>
</ul>
<p>To summarize: the Model knows nothing about the user, the View knows nothing
about the data and operations, and the Controller only knows how to relate
the Model and the View.  For really tiny applications, such as the currency
converter, it may be tempting to do away with the Model and simply put that
code in the Controller.  You probably shouldn't do this, as it can make
your code harder to read since it will be a mix of algorithms and glue code,
however there is no technical limitation that prevents you from doing this.
If you do combine the functionality of the model and controller, it is
customary to name it as if it represented the document (without &quot;Controller&quot;).
Note that the MVC paradigm is not specific to Cocoa and can be used with almost
any GUI toolkit, but Cocoa is explicitly designed for this paradigm.</p>
<p>You should have an MVC trio for every distinct unit of information in your
program.  In case of a simple dialog-style application such as Currency Converter
you will have one such trio.  Most applications, however, will have at least
two: one for the application itself and one for the &quot;documents&quot; the application
handles.  These may be real documents (i.e. files), but a document can be more
abstract.  For example, if your application does scientific simulations that
run in separate windows, each simulation could be a document.</p>
</div>
<div class="section" id="the-nib-file">
<h3><a name="the-nib-file">The NIB file</a></h3>
<p>Cocoa and Interface Builder strongly encourage you to use a NIB file
per MVC trio.   You should follow this encouragement unless you are sure
that you know what you are doing.</p>
<p>This brings us to the second big difference between Cocoa and other GUI
toolkits: almost all of the boilerplate code is replaced by the NIB.
The source of Cocoa programs that do little work, especially example programs,
will typically be much shorter than the equivalent with other toolkits.</p>
<p>The NIB file is <em>not</em> a description of dialogs and menus and buttons, as you 
would get out of interface-builders for other toolkits.  A NIB file is more:
it contains a archived object graph that represents the GUI, conceptually
similar to a pickle in Python.  You tell Interface Builder
about all the relevant classes in your application, the instances you
want to create from those classes, and how the classes should connect to
each other.  Interface Builder the actually instantiates the classes, makes
all the connections and at that point freezes and stores the whole lot.</p>
<p>Unarchival of a NIB happens in two phases.  The objects are restored using the
<tt class="docutils literal"><span class="pre">NSCoding</span></tt> protocol (<tt class="docutils literal"><span class="pre">initWithCoder:</span></tt> is similar to <tt class="docutils literal"><span class="pre">__setstate__</span></tt> of
Python's <tt class="docutils literal"><span class="pre">pickle</span></tt> protocol), and then each object is sent an
<tt class="docutils literal"><span class="pre">awakeFromNib:</span></tt> message so that they may do any initialization that depends
on a fully restored object graph (<tt class="docutils literal"><span class="pre">pickle</span></tt> does not have this functionality
built-in).</p>
<p>The section above explains a lot of the strangeness in AppKit-based PyObjC
applications:</p>
<ul class="simple">
<li>Windows and dialogs are typically not explicitly created, because they were
instantiated by the NIB.</li>
<li>Initialization is not always done in <tt class="docutils literal"><span class="pre">__init__</span></tt> or equivalent, because
the object graph may not be completely unarchived until the first
<tt class="docutils literal"><span class="pre">awakeFromNib:</span></tt> is called.</li>
<li>Attributes that reference other objects are not typically set explicitly,
but are done by the NIB file during unarchival.</li>
</ul>
<p>This also explains why you want separate NIB files for each MVC trio:
the objects and classes in a NIB file are all unarchived together.  In other
words, if you had created your document window in your application NIB
(even if you set it to &quot;hidden&quot; initially so it does not show up) it would
become very difficult to create a second window for a new document.</p>
<p>If you think about the consequences of this section for a while it will
become clear why all the boilerplate code is missing from Cocoa applications:
you don't need it.  Like the output of other gui-builders, a NIB usually
contains enough information to recreate the view objects, but a NIB can also
contain a large proportion of the setup for your Model and Controller
functionality.  This is especially true when using <a class="reference" href="http://developer.apple.com/documentation/Cocoa/Conceptual/CocoaBindings/">Cocoa Bindings</a>.</p>
</div>
<div class="section" id="delegates">
<h3><a name="delegates">Delegates</a></h3>
<p>If you are familiar with other object-oriented GUI toolkits such as MFC
another thing to notice is that Cocoa applications often use a <em>delegate</em>
object where other toolkits would use a subclass.  For example: it is not
common to use your own subclass of <tt class="docutils literal"><span class="pre">NSApplication</span></tt> for the main application
object.  <tt class="docutils literal"><span class="pre">NSApplication</span></tt> objects have a helper called its <tt class="docutils literal"><span class="pre">delegate</span></tt>.
The application object will attempt to inform its delegate many interesting
events, and the delegate implements only the methods for the events it is
interested in.</p>
<p>For example, the method <tt class="docutils literal"><span class="pre">applicationShouldTerminate:</span></tt> of the delegate
is called just before the application quits, and it has a chance to return
<tt class="docutils literal"><span class="pre">NO</span></tt> if it is not appropriate to quit just yet.</p>
</div>
<div class="section" id="examining-a-nib-file">
<h3><a name="examining-a-nib-file">Examining a NIB file</a></h3>
<p>Let us examine the final NIB of the Currency Converter tutorial with this in
mind.  If you open it and look at the main window (titled &quot;MainMenu.nib&quot;)
and select the &quot;Instances&quot; pane you should see six objects.  Two of these
have greyed-out names (&quot;File's Owner&quot; and &quot;First Responder&quot;), these are present
in every nib can not be changed.  The &quot;File's Owner&quot; is either the Controller
or the combined Model-Controller object, and is specified by the application
when it loads the NIB.  For the main nib, which is loaded automatically by
<tt class="docutils literal"><span class="pre">NSApplicationMain</span></tt> or <tt class="docutils literal"><span class="pre">PyObjCTools.AppHelper.runEventLoop</span></tt>, this will be
the instance of <tt class="docutils literal"><span class="pre">NSApplication</span></tt>.  Currency Converter is not a document-based
application, so the MVC trio for the conversion window are in here too.  These
are named <tt class="docutils literal"><span class="pre">Converter</span></tt>, <tt class="docutils literal"><span class="pre">Window</span></tt> and <tt class="docutils literal"><span class="pre">ConverterController</span></tt> respectively.</p>
<p>Let us have a look at the <tt class="docutils literal"><span class="pre">ConverterController</span></tt> object by double clicking it.
The &quot;MainMenu.nib&quot; window goes to the &quot;Classes&quot; tab, and an info window shows up.
In the &quot;MainMenu.nib&quot; window the <tt class="docutils literal"><span class="pre">ConverterController</span></tt> class is selected, and
you can see it is a subclass of <tt class="docutils literal"><span class="pre">NSObject</span></tt>.  Having the same name for the class
and the instance is common in Cocoa programs, the main exception being the File
Owner object.</p>
<p>The info window shows more information on the <tt class="docutils literal"><span class="pre">ConverterController</span></tt> class.  It
should pop open to the &quot;attributes&quot; page.  In the &quot;Outlets&quot; tab you see that instances
of this class have four attributes, <tt class="docutils literal"><span class="pre">converter</span></tt>, <tt class="docutils literal"><span class="pre">rateField</span></tt>, <tt class="docutils literal"><span class="pre">dollarField</span></tt>
and <tt class="docutils literal"><span class="pre">totalField</span></tt>.  In any instance of <tt class="docutils literal"><span class="pre">ConverterController</span></tt> you can connect these
to other objects, as we shall see below.  The &quot;Actions&quot; tab shows that there are two
methods <tt class="docutils literal"><span class="pre">convert:</span></tt> and <tt class="docutils literal"><span class="pre">invertRate:</span></tt>, and again you can arrange for these to
be called on instances of your <tt class="docutils literal"><span class="pre">ConverterController</span></tt> on certain events by
making connections.</p>
<p>So let us now look at the connections for our <tt class="docutils literal"><span class="pre">ConverterController</span></tt> <em>instance</em>.  Select
the &quot;Instances&quot; tab in the main window, select <tt class="docutils literal"><span class="pre">ConverterController</span></tt> and set the info
window to show &quot;Connections&quot;.  You now see all the outlets defined in the class.
Select one, and in the lower half of the info window you will see which object it connects
to.  Moreover, a blue line will also link the object representations in the main window and
in the dialog preview window.</p>
<p>Finding out who calls your <tt class="docutils literal"><span class="pre">convert:</span></tt> method is more difficult, though, with this view.
But, if you select the &quot;Convert&quot; button in the dialog you will see that its <tt class="docutils literal"><span class="pre">target</span></tt>
action will go to the <tt class="docutils literal"><span class="pre">ConverterController.convert_</span></tt> method.</p>
<p>Luckily there is a way to find such incoming connections without reverting to guessing.
For instance, you will be hard put to find who, if anyone, calls 
<tt class="docutils literal"><span class="pre">ConverterController.invertRate_</span></tt>.  The solution: go to the &quot;MainMenu.nib&quot; window and
look at the top of the vertical scrollbar.  There are two little icons there, one with
lines and one with squares, with the squares being highlighted.  Press it.  The view will change
to a scrollable list with objects in the left column and an indication of connections
in the right column.  You can now see our ConverterController object has four
outgoing connections (the ones we found earlier) and two incoming connections.  Click
on the incoming connections icon.  The view will change again and ConverterController
will probably scroll out of sight.  Locate it, and see that there are two lines
going out of the ConverterController object.  One goes to <tt class="docutils literal"><span class="pre">NSButton(Convert)</span></tt>
and is labeled <tt class="docutils literal"><span class="pre">convert:</span></tt>, we knew about that already.  The other one goes to an
object <tt class="docutils literal"><span class="pre">NSMenuItem(Invert</span> <span class="pre">Exchange</span> <span class="pre">Rate)</span></tt> and is labeled <tt class="docutils literal"><span class="pre">invertRate:</span></tt>, so that
is where calls to <tt class="docutils literal"><span class="pre">invertRate:</span></tt> come from.  And if you look at where this
<tt class="docutils literal"><span class="pre">NSMenuItem</span></tt> sits in the object hierarchy you find that it is an entry in the
&quot;Edit&quot; menu in the menubar.</p>
</div>
<div class="section" id="examining-an-apple-example">
<h3><a name="examining-an-apple-example">Examining an Apple example</a></h3>
<p>This section remains to be written.  Contributions will be gratefully accepted :-)</p>
</div>
</div>
<?
    include "footer.inc";
?>