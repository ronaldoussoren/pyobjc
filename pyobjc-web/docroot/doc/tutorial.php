<?
    $title = "Creating your first PyObjC application.";
    $cvs_author = '$Author: ronaldoussoren $';
    $cvs_date = '$Date: 2003/10/08 17:30:40 $';

    include "header.inc";
?>
<div class="document" id="creating-your-first-pyobjc-application">
<h1 class="title">Creating your first PyObjC application.</h1>
<p>In this tutorial you will learn how to create your first Python Cocoa application:
a simple dialog that allows you to convert amounts of money from one
currency to another. Definitely easier to do with a calculator, but in the
process of following the tutorial you will learn which bits of Apple's Cocoa
documentation apply to PyObjC and which bits are different, and how to adapt
the different bits to PyObjC from Objective-C.</p>
<p>To follow the tutorial you need PyObjC, which you apparently have, and either
Python 2.2 (pre-installed by Apple since Mac OS X 10.2) or MacPython 2.3,
which you probably also have. PyObjC works fine with any python more recent than
2.2, so if you installed python 2.2.2 through <tt class="literal"><span class="pre">fink</span></tt> that should work, but
you will have to work out the details for step 1 yourself. PyObjC does not
work with MacPython-2.2 or MacPython-OS9 2.3.</p>
<p>In addition you need Interface Builder to
create your user interface. Interface Builder is not included in Mac OS X
by default, but it is part of Apple's free Developer Tools, which can
be gotten from <a class="reference" href="http://developer.apple.com/tools">http://developer.apple.com/tools</a> as a hefty 300 MB download
after registering (for free).</p>
<div class="section" id="getting-started">
<h1><a name="getting-started">Getting Started</a></h1>
<ol class="arabic">
<li><p class="first">Create a work directory <tt class="literal"><span class="pre">src</span></tt>. Check which Python you have installed PyObjC
for, by running <tt class="literal"><span class="pre">python</span></tt> and checking that <tt class="literal"><span class="pre">import</span> <span class="pre">Foundation</span></tt> works. If it
does not work it could be that you have installed PyObjC for <tt class="literal"><span class="pre">/usr/local/python</span></tt>
but Apple's <tt class="literal"><span class="pre">/usr/bin/python</span></tt> comes first in your <tt class="literal"><span class="pre">$PATH</span></tt>. Make sure you
use the right python whereever it says <tt class="literal"><span class="pre">python</span></tt> in this tutorial.</p>
<p>For convenience, set a shell variable PYLIB
to the Python Lib directory. For MacPython-2.3 this will be:</p>
<pre class="literal-block">
$ setenv PYLIB /Library/Frameworks/Python.framework/Versions/Current/lib/python2.3
</pre>
<p>or if you use bash as your shell:</p>
<pre class="literal-block">
$ export PYLIB=/Library/Frameworks/Python.framework/Versions/Current/lib/python2.3
</pre>
<p>For Apple's <tt class="literal"><span class="pre">/usr/bin/python</span></tt> set the variable to <tt class="literal"><span class="pre">/usr/lib/python2.2</span></tt>.</p>
</li>
<li><p class="first">Start Interface Builder, select <em>Cocoa Application</em>
in the new file dialog, save this file as <tt class="literal"><span class="pre">src/MainMenu.nib</span></tt>.</p>
</li>
<li><p class="first">Proceed with the instructions as lined out in Apple's
<a class="reference" href="http://developer.apple.com/techpubs/macosx/Cocoa/ObjCTutorial/index.html">Developing Cocoa Objective-C Applications: a Tutorial</a>, <a class="reference" href="http://developer.apple.com/techpubs/macosx/Cocoa/ObjCTutorial/chapter03/index.html">chapter 3</a>,
just after the section &quot;<em>Creating the Currency Converter Interface</em>&quot;.
Work through &quot;Defining the Classes of Currency Converter&quot;, &quot;Connecting
ConverterController to the Interface&quot;, and stop at &quot;<em>Implementing the Classes
of Currency Converter</em>&quot;, as we are going to do this in Python, not Objective-C.
Your nib file should now be the same as <a class="reference" href="step3-MainMenu.nib.zip">step3-MainMenu.nib</a>.</p>
</li>
</ol>
<ol class="arabic" start="4">
<li><p class="first">Create the skeleton Python script by running <tt class="literal"><span class="pre">NibClassBuilder</span></tt> as a tool.
When invoked as a main program from the command line <tt class="literal"><span class="pre">NibClassBuilder</span></tt> will
parse the NIB file and create a skeleton module for you. Invoke
it as follows (from the <tt class="literal"><span class="pre">src</span></tt> directory):</p>
<pre class="literal-block">
$ python $PYLIB/site-packages/PyObjC/PyObjCTools/NibClassBuilder.py \
        MainMenu.nib &gt; CurrencyConverter.py
</pre>
<p>The result of this can be seen in <a class="reference" href="step4-CurrencyConverter.py">step4-CurrencyConverter.py</a>.</p>
</li>
</ol>
<ol class="arabic simple" start="5">
<li>There is no step 5.</li>
</ol>
</div>
<div class="section" id="testing-the-user-interface">
<h1><a name="testing-the-user-interface">Testing the user interface</a></h1>
<ol class="arabic" start="6">
<li><p class="first">Now we need to create an application framework around our program. Again,
in the future it could well be that this step is not needed during development,
or that it becomes simpler, but for now we do the following:</p>
<pre class="literal-block">
$ python $PYLIB/site-packages/PyObjC/bundlebuilder.py --link --nib=MainMenu \
        --mainprogram=CurrencyConverter.py --resource=MainMenu.nib build
</pre>
<p>There are a few things to note:</p>
<ul class="simple">
<li>We use the <tt class="literal"><span class="pre">--link</span></tt> argument. This creates a <tt class="literal"><span class="pre">.app</span></tt> bundle which has symlinks
to our source files (<tt class="literal"><span class="pre">CurrencyConverter.py</span></tt> and <tt class="literal"><span class="pre">MainMenu.nib</span></tt>) in stead of copies.
This allows us to keep working on the sources without having to re-run bundlebuilder
after every edit.</li>
<li>You have to specify MainMenu twice: once (with <tt class="literal"><span class="pre">--resource</span></tt>) to get it linked/copied 
into the bundle and once (with <tt class="literal"><span class="pre">--nib</span></tt>) to get it listed in the <tt class="literal"><span class="pre">.plist</span></tt> file.</li>
</ul>
</li>
<li><p class="first">Run the program. This can be done in three ways:</p>
<ul>
<li><p class="first">double-click <tt class="literal"><span class="pre">build/CurrencyConverter.app</span></tt> from the Finder (where you won't see the
.app extension)</p>
</li>
<li><p class="first">similarly, open it from the terminal with:</p>
<pre class="literal-block">
$ open build/CurrencyConverter.app
</pre>
</li>
<li><p class="first">run it directly from the Terminal, as:</p>
<pre class="literal-block">
$ ./build/CurrencyConverter.app/Contents/MacOS/CurrencyConverter
</pre>
</li>
</ul>
<p>The last method is actually the best to use: it leaves stdout and stderr connected
to your terminal session so you can see what is going on if there are errors. When
running with the other two methods stdout and stderr go to the console.</p>
<p>When you run your script as it is now it should behave identically as when you
tested your interface in Interface Builder in step 3, only now the skeleton is
in Python, not Objective-C.</p>
</li>
</ol>
</div>
<div class="section" id="writing-the-code">
<h1><a name="writing-the-code">Writing the code</a></h1>
<ol class="arabic" start="8">
<li><p class="first">Time to actually write some code. Edit CurrencyConverter.py again, and add
some. Follow Apple's documentation again, chapter 3, section &quot;Implementing
Currency Converter's Classes&quot;. We need to do some name mangling on ObjC
names to get the corresponding Python names, see <em>An introduction to PyObjC</em>
for the details, but
in short if the ObjC name of a method is <tt class="literal"><span class="pre">modifyArg:andAnother:</span></tt>, in
other words, if an ObjC call would be:</p>
<pre class="literal-block">
[object modifyArg: arg1 andAnother: arg2]
</pre>
<p>the Python name will be <tt class="literal"><span class="pre">modifyArg_andAnother_</span></tt> and you invoke it as:</p>
<pre class="literal-block">
object.modifyArg_andAnother_(arg1, arg2)
</pre>
<p>Note that we don't do this mangling for <tt class="literal"><span class="pre">Converter.convertAmount()</span></tt>: this method is
only called by other Python code, so there is no need to go through the name mangling.
Also, if we would want to make this method callable from ObjC code we would have
to tell the PyObjC runtime system about the types of the arguments, so it could
do the conversion. This is beyond the scope of this first tutorial, <em>An introduction to PyObjC</em>
has a little more detail on this.</p>
<p>The application should now be fully functional, try it. The results of what we have
up to now can be seen in <a class="reference" href="step8-CurrencyConverter.py">step8-CurrencyConverter.py</a>.</p>
</li>
</ol>
</div>
<div class="section" id="extending-the-functionality">
<h1><a name="extending-the-functionality">Extending the functionality</a></h1>
<ol class="arabic" start="9">
<li><p class="first">We are going to add one more goodie, just to show how you edit an existing application.
The main problem, which may be obvious, is that we cannot run NibClassBuilder again
because we would destroy all the code we wrote in steps 5 and 8, so we do this by
hand.</p>
<p>What we are going to do is add an &quot;invert rate&quot; command, because I always get this
wrong: in stead of typing in the exchange rate from dollars to euros I type in the
rate to convert from euros to dollars.</p>
<p>Open <tt class="literal"><span class="pre">MainMenu.nib</span></tt> in Interface Builder. Select the <em>Classes</em> view and there select the
<tt class="literal"><span class="pre">ConverterController</span></tt> class. In the info panel select the <em>Attributes</em> from the popup.
Select the <em>Actions</em> tab, and add an action <tt class="literal"><span class="pre">invertRate:</span></tt>. You have now told Interface Builder
that instances of the <tt class="literal"><span class="pre">ConverterController</span></tt> class have grown a new method <tt class="literal"><span class="pre">invertRate_()</span></tt>.</p>
<p>In the <tt class="literal"><span class="pre">MainMenu.nib</span> <span class="pre">main</span></tt> window open the <em>MainMenu</em> menubar. Select the <tt class="literal"><span class="pre">Edit</span></tt>
menu. Make sure the <em>Menus</em> palette is open and selected, drag a separator to the 
<tt class="literal"><span class="pre">Edit</span></tt> menu and then drag an <tt class="literal"><span class="pre">Item</span></tt> there. Double click the item and set the text to
<tt class="literal"><span class="pre">Invert</span> <span class="pre">Exchange</span> <span class="pre">Rate</span></tt>.</p>
<p>Make the connection by control-dragging from the new <tt class="literal"><span class="pre">Invert</span> <span class="pre">Exchange</span> <span class="pre">Rate</span></tt> menu item to
the <tt class="literal"><span class="pre">ConverterController</span></tt> instance in the Instances tab in the <tt class="literal"><span class="pre">MainMenu.nib</span></tt> main window.
<em>NOTE:</em> you drag to the <em>instance</em> of <tt class="literal"><span class="pre">ConverterController</span></tt>, not to the class. This is logical
if you think about it, but I keep forgetting it myself all the time too.
In the <em>Info</em> panel, <em>Connections</em> section, select <tt class="literal"><span class="pre">invertRate:</span></tt> and press <em>Connect</em>. 
<em>NOTE:</em> that is another thing I always forget: pressing <em>Connect</em> after selecting the action:-)</p>
</li>
<li><p class="first">We know our program can't invert rates yet, because we haven't actually written the code
to do it, but we are going to try it anyway, just to see what sort of spectacular
crash we get. Alas, nothing spectacular about it: when the NIB is loaded the Cocoa runtime
system tries to make the connection, notices that we have no <tt class="literal"><span class="pre">invertRate_()</span></tt> method in
our <tt class="literal"><span class="pre">ConverterController</span></tt> class and it gives an error message:</p>
<pre class="literal-block">
$ ./build/CurrencyConverter.app/Contents/MacOS/CurrencyConverter 
2003-03-24 16:22:43.037 CurrencyConverter[16163] Could not connect the action 
invertRate: to target of class ConverterController
</pre>
<p>Moreover, it has disabled the <tt class="literal"><span class="pre">Invert</span> <span class="pre">Exchange</span> <span class="pre">Rate</span></tt> menu command and continues, so the 
program really works as it did before, only with one more (disabled) menu item.</p>
</li>
</ol>
</div>
<div class="section" id="debugging">
<h1><a name="debugging">Debugging</a></h1>
<ol class="arabic" start="11">
<li><p class="first">Writing the code is easy: add a method <tt class="literal"><span class="pre">invertRate_(self,</span> <span class="pre">sender)</span></tt> that gets the float
value of <tt class="literal"><span class="pre">rateField</span></tt>, inverts it and puts it back. We deliberately forget to test for
divide by zero. We run the program again, and now the menu entry is enabled. After
trying it with a couple of non-zero exchange rates we try it with an exchange rate of
zero (or empty, which is the same). We get a dialog box giving the Python exception, and
offering the choice of continuing or quitting.</p>
<p><em>XXXX Implementation Note:</em> what is described in the next paragraph does not
seem to work in the current distribution.</p>
<p>If we select <em>Quit</em> then we get a normal
Python exception traceback in the Terminal window. The exception is actually re-raised,
so we can use the standard Python trick to debug this: set shell variable
<tt class="literal"><span class="pre">PYTHONINSPECT</span></tt> to <tt class="literal"><span class="pre">1</span></tt>, run our program, try to invert an exchange rate of <tt class="literal"><span class="pre">0</span></tt>, press quit.
At the <tt class="literal"><span class="pre">&gt;&gt;&gt;</span></tt> prompt, type <tt class="literal"><span class="pre">import</span> <span class="pre">pdb</span> <span class="pre">;</span> <span class="pre">pdb.pm()</span></tt> and we can inspect all local variables,
etc.</p>
</li>
<li><p class="first">Fix the final bug by testing for <tt class="literal"><span class="pre">rate==0</span></tt> in <tt class="literal"><span class="pre">invertRate_()</span></tt>. The result is in the
<a class="reference" href="step12-src">step12-src</a> directory.</p>
</li>
</ol>
</div>
<div class="section" id="creating-an-applet-for-local-use">
<h1><a name="creating-an-applet-for-local-use">Creating an applet for local use</a></h1>
<p>Your application is finished, and you want to move it to the <tt class="literal"><span class="pre">Applications</span></tt> folder
(or anywhere else) and insulate it from the original source code.
This can be done by re-running the <tt class="literal"><span class="pre">bundlebuilder.py</span></tt> invocation from step
6 without  using the '--link' in the invocation. Move <tt class="literal"><span class="pre">build/CurrencyConverter.app</span></tt>
anywhere you want and double-click it from the Finder to run it.</p>
<p>For programs with more Python sourcefiles you include all additional sources as resources.</p>
<p>It is even possible to include all of Python (or, if you are using Apple's Python 2.2,
all the bits of Python that are non-standard), this gives you an application that
is distributable to anyone in the world (as long as they have Mac OS X 10.2)! Unfortunately,
the exact details of this procedure are not streamlined enough for inclusion in this
tutorial at this point in time.</p>
</div>
</div>
<?
    include "footer.inc";
?>
