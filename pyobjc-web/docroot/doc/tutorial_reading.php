<?
    $title = "Understanding existing PyObjC examples";
    $cvs_author = '$Author: ronaldoussoren $';
    $cvs_date = '$Date: 2003/07/05 14:59:47 $';

    include "header.inc";
?>
<div class="document" id="understanding-existing-pyobjc-examples">
<div class="section" id="introduction">
<h1><a name="introduction">Introduction</a></h1>
<p>This tutorial is aimed primarily at people with little or no background
in ObjC and Cocoa, and it will help you to understand PyObjC programs
written by other people, such as the examples included with the distribution.
This document is actually not a true tutorial: you do not get to build anything,
only read and examine things.</p>
<p>It is strongly suggested that you first do the
<a class="reference" href="tutorial/tutorial.html">Creating your first PyObjC application</a> tutorial to get some hands-on
experience with PyObjC, Cocoa and especially Interface Builder.</p>
</div>
<div class="section" id="model-view-controller">
<h1><a name="model-view-controller">Model-View-Controller</a></h1>
<p>If you have used another GUI toolkit in the past it is essential that
you understand that Cocoa is different. For this once this isn't marketing-speak:
Cocoa is inherently different from common toolkits such as Tk, wxWindows,
Carbon, win32 and all the other popular ones. Apple's documentation explains this,
but in the introductory sections that are often quickly glanced over. It is a
good idea to refer back to <a class="reference" href="http://developer.apple.com/documentation/Cocoa/Conceptual/AppArchitecture/index.html">Application Architecture</a> after reading this section. If you really
want you can break out of the architecture sketched in this section, but
then you are on your own, really: Cocoa and Interface Builder really
expect you to follow this model.</p>
<p>Cocoa is built on the Model-View-Controller paradigm (MVC). What this means
is that the application code is going to be split into three parts:</p>
<ul class="simple">
<li>The <em>Model</em> is the actual data you are manipulating, plus the operations
on it. It can be as big as a complete database engine or a scientific
simulation, or as small as a routine that multiplies one floating point
number (an amount of money in currency A) by another (the conversion
rate from currency A to currency B), as in the currency converter
application you built in the first tutorial.</li>
<li>The <em>View</em> is what the user sees on-screen, plus his or her interaction
with it.</li>
<li>The <em>Controller</em> is the glue that binds these two together. In the
currency converter example, it is the code that gets called when the user
presses the &quot;Convert&quot; button, whereupon it gets the data from the &quot;amount&quot;
and &quot;rate&quot; fields from the View, passes them to the Model for computation
and sends the result back to the View.</li>
</ul>
<p>To summarize: the Model knows nothing about dialogs and buttons and such,
the View knows nothing about data and algorithms and the Controller ties it
all together. For really tiny applications, such as the currency converter,
you could do away with the Model and simply put that code right in the
Controller. MVC purists say you should not do this, and it can indeed
make your code harder to read (because the Controller will contain a mix
of algorithms and glue code), but there is no architectural reason that
stops you. If you combine the two classes it is customary to use the name
you would use for your document class, so without &quot;Controller&quot;. Note that
MVC is not specific to Cocoa, you can use the paradigm with any GUI toolkit,
but Cocoa really steers you towards it.</p>
<p>You should have an MVC trio for every distinct unit of information in your
program. In case of a simple dialog-style application such as Currency Converter
you will have one such trio. Most applications, however, will have at least
two: one for the application itself and one for the &quot;documents&quot; the application
handles. These may be real documents (i.e. files), but they could also be more
abstract. If your application does scientific simulation and you want to be
able to open two simulation windows at the same time you should use the
document model.</p>
</div>
<div class="section" id="the-nib-file">
<h1><a name="the-nib-file">The NIB file</a></h1>
<p>Cocoa and Interface Builder strongly encourage you to use a NIB file
per MVC trio. Again: follow this encouragement unless you are sure what
you are doing.</p>
<p>This brings us to the second big difference between Cocoa and other GUI
toolkits: almost all the boilerplate code is in the NIB, and therefore
the source of Cocoa programs, especially example programs that do little
real work, will look stunningly small if you are familiar with, say,
Tkinter.</p>
<p>The NIB file is <em>not</em> a description of dialogs and menus and buttons, as you 
would get out of interface-builders for other toolkits. There, at startup
something will read the description, create the buttons and hand the finished
dialog to your code. A NIB file is more: it contains a complete set of frozen
objects, conceptually similar to a pickle in Python. You tell Interface Builder
knows about all the relevant classes in your application, the instances you
want to create from those classes, and how the classes should connect to
each other. Interface Builder the actually instantiates the classes, makes
all the connections and at that point freezes and stores the whole lot.</p>
<p>When your NIB is read the objects are thawed, the connections restored and
the objects get a running start. Again, this is conceptually similar
to how unpickling works.</p>
<blockquote>
<p>The section above explains a lot of the strangeness in PyObjC
programs: why you don't create windows and other dialogs (they
already exist); why you shouldn't do initialization in <tt class="literal"><span class="pre">__init__</span></tt>
(because it will be called at some undefined point in time, while
reading the NIB) but in <tt class="literal"><span class="pre">awakeFromNib:</span></tt> in stead; why you don't
have to create and initialize the attributes that tie your
objects together (they are already tied together).</p>
<p><tt class="literal"><span class="pre">awakeFromNib:</span></tt> is very similar in nature to <tt class="literal"><span class="pre">__setstate__</span></tt> for
a pickled Python object, but it happens after all objects have been
unserialized.</p>
</blockquote>
<p>This also explains why you want separate NIB files for each MVC trio:
the objects and classes in a NIB file are all unpickled together. In other
words: if you had created your document window in your application NIB
(even if you set it to &quot;hidden&quot; initially so it does not show up) it would
become very difficult to create a second window for a new document.</p>
<p>If you think about the consequences of this section for a while it will
become clear why all the boilerplate code is missing from Cocoa applications:
you don't need it. The NIB file usually contains all of the things that need to
be done for the Views objects, as is often the case with other gui-builders.
But in addition the NIB also contains a large proportion of your Model
functionality: creating the View and Controller objects and tying the
lot together.</p>
</div>
<div class="section" id="delegates">
<h1><a name="delegates">Delegates</a></h1>
<p>If you are familiar with other object-oriented GUI toolkits such as MFC
another thing to notice is that Cocoa applications often use a <em>delegate</em>
object where other toolkits would use a subclass. For example: it is not
common to use your own subclass in stead of <tt class="literal"><span class="pre">NSApplication</span></tt> for the
main application object. In stead, <tt class="literal"><span class="pre">NSApplication</span></tt> objects have a helper
called its <tt class="literal"><span class="pre">delegate</span></tt>. The application object will attempt to inform
its delegate of all sorts of things happening, and the delegate implements
only the methods for the events in which it is interested.</p>
<p>For example, the method <tt class="literal"><span class="pre">applicationShouldTerminate:</span></tt> on the delegate
is called just before the application quits, and it has a chance to return
<tt class="literal"><span class="pre">NO</span></tt> if you don't want to quit just yet.</p>
</div>
<div class="section" id="examining-a-nib-file">
<h1><a name="examining-a-nib-file">Examining a NIB file</a></h1>
<p>Let us examine the final NIB of the Currency Converter tutorial with this in mind.
If you open it and look at the main window (the one with &quot;MainMenu.nib&quot; as
its title) and select the &quot;Instances&quot; pane you see six objects. Two of these
have a greyed-out name (&quot;File's Owner&quot; and &quot;First Responder&quot;): these have
been created for you by Apple. The other four are created by you. Actually:
&quot;Main Menu&quot; was created by Apple as a convenience, but you are free to modify
it. The &quot;File's Owner&quot; is either the Controller or the combined Model-Controller
object, in this case it is the application itself, an instance of <tt class="literal"><span class="pre">NSApplication</span></tt>.
Because this application is not a document-based application the MVC trio
for the actual conversion window are in here too: <tt class="literal"><span class="pre">Converter</span></tt>, <tt class="literal"><span class="pre">Window</span></tt> and
<tt class="literal"><span class="pre">ConverterController</span></tt> respectively.</p>
<p>Let us have a look at the <tt class="literal"><span class="pre">ConverterController</span></tt> object by double clicking it.
The &quot;MainMenu.nib&quot; window goes to the &quot;Classes&quot; tab, and an info window shows up.
In the &quot;MainMenu.nib&quot; window the <tt class="literal"><span class="pre">ConverterController</span></tt> class is selected, and
you can see it is a subclass of <tt class="literal"><span class="pre">NSObject</span></tt>. Having the same name for the class
and the instance is common in Cocoa programs, the main exception being the File
Owner object.</p>
<p>The info window shows more information on the <tt class="literal"><span class="pre">ConverterController</span></tt> class. It
should pop open to the &quot;attributes&quot; page. In the &quot;Outlets&quot; tab you see that instances
of this class have four attributes, <tt class="literal"><span class="pre">converter</span></tt>, <tt class="literal"><span class="pre">rateField</span></tt>, <tt class="literal"><span class="pre">dollarField</span></tt>
and <tt class="literal"><span class="pre">totalField</span></tt>. In any instance of <tt class="literal"><span class="pre">ConverterController</span></tt> you can connect these
to other objects, as we shall see below. The &quot;Actions&quot; tab shows that there are two
methods <tt class="literal"><span class="pre">convert:</span></tt> and <tt class="literal"><span class="pre">invertRate:</span></tt>, and again you can arrange for these to
be called on instances of your <tt class="literal"><span class="pre">ConverterController</span></tt> on certain events by
making connections.</p>
<p>So let us now look at the connections for our <tt class="literal"><span class="pre">ConverterController</span></tt> <em>instance</em>. Select
the &quot;Instances&quot; tab in the main window, select <tt class="literal"><span class="pre">ConverterController</span></tt> and set the info
window to show &quot;Connections&quot;. You now see all the outlets defined in the class.
Select one, and in the lower half of the info window you will see which object it connects
to. Moreover, a blue line will also link the object representations in the main window and
in the dialog preview window.</p>
<p>Finding out who calls your <tt class="literal"><span class="pre">convert:</span></tt> method is more difficult, though, with this view.
But, if you select the &quot;Convert&quot; button in the dialog you will see that its <tt class="literal"><span class="pre">target</span></tt>
action will go to the <tt class="literal"><span class="pre">ConverterController.convert:</span></tt> method.</p>
<p>Luckily there is a way to find such incoming connections without reverting to guessing.
For instance, you will be hard put to find who, if anyone, calls 
<tt class="literal"><span class="pre">ConverterController.invertRate:</span></tt>. The solution: go to the &quot;MainMenu.nib&quot; window and
look at the top of the vertical scrollbar. There are two little icons there, one with
lines and one with squares, with the squares being highlighted. Press it. The view will change
to a scrollable list with objects in the left column and an indication of connections
in the right column. You can now see our ConverterController object has four
outgoing connections (the ones we found earlier) and two incoming connections. Click
on the incoming connections icon. The view will change again and ConverterController
will probably scroll out of sight. Locate it, and see that there are two lines
going out of the ConverterController object. One goes to <tt class="literal"><span class="pre">NSButton(Convert)</span></tt>
and is labeled <tt class="literal"><span class="pre">convert:</span></tt>, we knew about that already. The other one goes to an
object <tt class="literal"><span class="pre">NSMenuItem(Invert</span> <span class="pre">Exchange</span> <span class="pre">Rate)</span></tt> and is labeled <tt class="literal"><span class="pre">invertRate:</span></tt>, so that
is where calls to <tt class="literal"><span class="pre">invertRate:</span></tt> come from. And if you look at where this
<tt class="literal"><span class="pre">NSMenuItem</span></tt> sits in the object hierarchy you find that it is an entry in the
&quot;Edit&quot; menu in the menubar.</p>
</div>
<div class="section" id="examining-an-apple-example">
<h1><a name="examining-an-apple-example">Examining an Apple example</a></h1>
<p>This section remains to be written. Contributions will be gratefully accepted:-)</p>
</div>
</div>
<?
    include "footer.inc";
?>