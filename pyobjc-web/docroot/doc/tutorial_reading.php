<?
    $title = "Understanding existing PyObjC examples";
    $cvs_author = '$Author: ronaldoussoren $';
    $cvs_date = '$Date: 2003/07/05 14:59:46 $';

    include "header.inc";
?>
<div class="document" id="understanding-existing-pyobjc-examples">
<h1 class="title">Understanding existing PyObjC examples</h1>
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
you would use for your document class, so without &quot;Controller&quot;.</p>
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
The section above explains a lot of the strangeness in PyObjC
programs: why you don't create windows and other dialogs (they
already exist); why you shouldn't do initialization in <tt class="literal"><span class="pre">__init__</span></tt>
(because it will be called at some undefined point in time, while
reading the NIB) but in <tt class="literal"><span class="pre">awakeFromNIB</span></tt> in stead; why you don't
have to create and initialize the attributes that tie your
objects together (they are already tied together).</blockquote>
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
functionality: creating the View and Controller objects and tieing the
lot together.</p>
<p>XXXX Explain about delegates instead of subclassing.</p>
</div>
<div class="section" id="examining-a-nib-file">
<h1><a name="examining-a-nib-file">Examining a NIB file</a></h1>
<p>Let us examine the NIB of the Currency Converter tutorial with this in mind.
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
<p>XXXX Examine ConverterController, show how to see class and methods</p>
<p>XXXX Show how to see connections</p>
<p>XXXX Show how to use outline view</p>
</div>
<div class="section" id="examining-an-example">
<h1><a name="examining-an-example">Examining an example</a></h1>
<p>XXXX Pick one of the interesting examples and walk through it, looking at the
NIB file and the code.</p>
</div>
</div>
<?
    include "footer.inc";
?>