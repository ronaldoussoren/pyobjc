<?
    $title = "Creating your first PyObjC application.";
    $cvs_author = '$Author: ronaldoussoren $';
    $cvs_date = '$Date: 2003/07/05 14:59:47 $';

    include "header.inc";
?>
<h1 class="title">Creating your first PyObjC application.</h1>
<p>In this tutorial you will learn how to create your first Python Cocoa application:
a simple dialog that allows you to convert amounts of money from one
currency to another. Definitely easier to do with a calculator, but in the
process of following the tutorial you will learn which bits of Apple's Cocoa
documentation apply to PyObjC and which bits are different, and how to adapt
the different bits to PyObjC from Objective-C.</p>
<p>To follow the tutorial you need:</p>
<blockquote>
<ul class="simple">
<li>PyObjC 1.2</li>
<li>py2app 0.1.6 or later (included in the binary installer for PyObjC)</li>
<li>Python 2.3 or later (note: PyObjC is NOT compatible with MacPython-OS9)</li>
<li>Mac OS X 10.2 or later</li>
<li>Xcode Tools (was Developer Tools for Mac OS X 10.2)</li>
</ul>
</blockquote>
<p>If you do not have a <tt class="docutils literal"><span class="pre">/Developer</span></tt> folder, then you do not have Xcode Tools
installed.  See <a class="reference" href="http://developer.apple.com/tools/download/">Getting the Xcode Tools</a>.</p>
<div class="section" id="getting-started">
<h3><a name="getting-started">Getting Started</a></h3>
<ol class="arabic simple">
<li>Create a work directory <tt class="docutils literal"><span class="pre">src</span></tt>. Check which Python you have installed PyObjC
for, by running <tt class="docutils literal"><span class="pre">python</span></tt> and checking that <tt class="docutils literal"><span class="pre">import</span> <span class="pre">Foundation</span></tt> works. If it
does not work it could be that you have installed PyObjC for
<tt class="docutils literal"><span class="pre">/usr/local/bin/python</span></tt> but Apple's <tt class="docutils literal"><span class="pre">/usr/bin/python</span></tt> comes first in your
<tt class="docutils literal"><span class="pre">$PATH</span></tt>. Make sure you use the right python whereever it says <tt class="docutils literal"><span class="pre">python</span></tt> in this
tutorial.</li>
<li>Start Interface Builder, select <em>Cocoa Application</em>
in the new file dialog, save this file as <tt class="docutils literal"><span class="pre">src/MainMenu.nib</span></tt>.</li>
<li>Proceed with the instructions as lined out in Apple's
<a class="reference" href="http://developer.apple.com/documentation/Cocoa/Conceptual/ObjCTutorial/index.html">Developing Cocoa Objective-C Applications: a Tutorial</a>, <a class="reference" href="http://developer.apple.com/documentation/Cocoa/Conceptual/ObjCTutorial/index.html?http://developer.apple.com/documentation/Cocoa/Conceptual/ObjCTutorial/chapter03/chapter_3_section_1.html">chapter 3</a>,
just after the section &quot;<em>Creating the Currency Converter Interface</em>&quot;.
Work through &quot;Defining the Classes of Currency Converter&quot;, &quot;Connecting
ConverterController to the Interface&quot;, and stop at &quot;<em>Implementing the Classes
of Currency Converter</em>&quot;, as we are going to do this in Python, not Objective-C.
Your nib file should now be the same as <a class="reference" href="step3-MainMenu.nib.zip">step3-MainMenu.nib</a>.</li>
</ol>
<ol class="arabic" start="4">
<li><p class="first">Create the skeleton Python script by running the <tt class="docutils literal"><span class="pre">nibclassbuilder</span></tt> script.
<tt class="docutils literal"><span class="pre">nibclassbuilder</span></tt> will parse the NIB file and create a skeleton module for you.
Invoke it as follows (from the <tt class="docutils literal"><span class="pre">src</span></tt> directory):</p>
<pre class="literal-block">
$ python -c &quot;import PyObjCScripts.nibclassbuilder&quot; English.lproj/MainMenu.nib &gt; CurrencyConverter.py
</pre>
<p>Depending on your installation, the <tt class="docutils literal"><span class="pre">nibclassbuilder</span></tt> script may be on your <tt class="docutils literal"><span class="pre">$PATH</span></tt>.
If so, it can be invoked as such:</p>
<pre class="literal-block">
$ nibclassbuilder English.lproj/MainMenu.nib &gt; CurrencyConverter.py
</pre>
<p>The result of this can be seen in <a class="reference" href="step4-CurrencyConverter.py">step4-CurrencyConverter.py</a>.</p>
</li>
</ol>
</div>
<div class="section" id="testing-the-user-interface">
<h3><a name="testing-the-user-interface">Testing the user interface</a></h3>
<ol class="arabic" start="5">
<li><p class="first">Now we need to create an build script for CurrencyConverter.  To do this,
create a file named <tt class="docutils literal"><span class="pre">setup.py</span></tt> with the following contents:</p>
<pre class="literal-block">
from distutils.core import setup
import py2app

setup(
    app=['CurrencyConverter.py'],
    data_files=['English.lproj'],
)
</pre>
<p>The result of this can be seen in <a class="reference" href="step5-setup.py">step5-setup.py</a>.</p>
</li>
</ol>
<ol class="arabic" start="6">
<li><p class="first">Run the setup script to create a temporary application bundle for
development:</p>
<pre class="literal-block">
$ python setup.py py2app -A
</pre>
<p>Note that we use the <tt class="docutils literal"><span class="pre">-A</span></tt> argument to create an alias bundle at 
<tt class="docutils literal"><span class="pre">dist/CurrencyConverter.app</span></tt>.  Alias bundles contain an alias to the
main script (<tt class="docutils literal"><span class="pre">CurrencyConverter.py</span></tt>) and symlinks to the data files
(<tt class="docutils literal"><span class="pre">English.lproj</span></tt>), rather than including them and their dependencies
into a standalone application bundle.  This allows us to keep working on
the source files without having to rebuild the application.  This alias
bundle is similar to a ZeroLink executable for Xcode - it is for
DEVELOPMENT ONLY, and will not work on other machines.</p>
</li>
<li><p class="first">Run the program. This can be done in three ways:</p>
<ul>
<li><p class="first">double-click <tt class="docutils literal"><span class="pre">dist/CurrencyConverter</span></tt> from the Finder
(you won't see the .app extension)</p>
</li>
<li><p class="first">open it from the terminal with:</p>
<pre class="literal-block">
$ open dist/CurrencyConverter.app
</pre>
</li>
<li><p class="first">run it directly from the Terminal, as:</p>
<pre class="literal-block">
$ ./dist/CurrencyConverter.app/Contents/MacOS/CurrencyConverter
</pre>
</li>
</ul>
<p>The last method is typically the best to use for development: it leaves
stdout and stderr connected to your terminal session so you can see what
is going on if there are errors, and it allows you to interact with <tt class="docutils literal"><span class="pre">pdb</span></tt>
if you are using it to debug your application.  Note that your application
will likely appear in the background, so you will have to cmd-tab or click
on its dock icon to see its user interface.</p>
<p>The other methods cause stdout and stderr to go to the Console log, which
can be viewed with <tt class="docutils literal"><span class="pre">/Applications/Utilities/Console.app</span></tt>.</p>
<p>When you run your script as it is now it should behave identically as when you
tested your interface in Interface Builder in step 3, only now the skeleton is
in Python, not Objective-C.</p>
</li>
</ol>
</div>
<div class="section" id="writing-the-code">
<h3><a name="writing-the-code">Writing the code</a></h3>
<ol class="arabic" start="8">
<li><p class="first">Time to actually write some code. Open <tt class="docutils literal"><span class="pre">CurrencyConverter.py</span></tt> in your favorite
text editor.  Follow Apple's documentation again, chapter 3, section &quot;Implementing
Currency Converter's Classes&quot;.  To translate this Objective C code to Python syntax,
we will need to do some name mangling of the selectors.  See 
<em>An introduction to PyObjC</em> for the details, but the short is that:</p>
<pre class="literal-block">
[anObject modifyArg: arg1 andAnother: arg2]
</pre>
<p>translates into the following Python code, by replacing the colons in the selector
with underscores, and passing the arguments as you would with a normal Python
method call:</p>
<pre class="literal-block">
anObject.modifyArg_andAnother_(arg1, arg2)
</pre>
<p>Note that we don't do this mangling for <tt class="docutils literal"><span class="pre">Converter.convertAmount()</span></tt>: this method is
only called by other Python code, so there is no need to go through the name mangling.
Also, if we would want to make this method callable from ObjC code we may have
to tell the PyObjC runtime system about the types of the arguments, so it could
do the conversion. This is beyond the scope of this first tutorial, <em>An introduction to PyObjC</em>
has a little more detail on this.</p>
<p>The application should now be fully functional, try it. The results of what we have
up to now can be seen in <a class="reference" href="step8-CurrencyConverter.py">step8-CurrencyConverter.py</a>.</p>
</li>
</ol>
</div>
<div class="section" id="extending-the-functionality">
<h3><a name="extending-the-functionality">Extending the functionality</a></h3>
<ol class="arabic" start="9">
<li><p class="first">We are going to add one more goodie, just to show how you edit an existing application.
The main problem, which may be obvious, is that we cannot run <tt class="docutils literal"><span class="pre">nibclassbuilder</span></tt> again
because we would destroy all the code we wrote in steps 5 and 8, so we do this by
hand.</p>
<p>What we are going to do is add an &quot;invert rate&quot; command, because I always get this
wrong: instead of typing in the exchange rate from dollars to euros I type in the
rate to convert from euros to dollars.</p>
<p>Open <tt class="docutils literal"><span class="pre">MainMenu.nib</span></tt> in Interface Builder. Select the <em>Classes</em> view and there select the
<tt class="docutils literal"><span class="pre">ConverterController</span></tt> class.  In the info panel select the <em>Attributes</em> from the popup.
Select the <em>Actions</em> tab, and add an action <tt class="docutils literal"><span class="pre">invertRate:</span></tt>.  You have now told Interface Builder
that instances of the <tt class="docutils literal"><span class="pre">ConverterController</span></tt> class have grown a new method <tt class="docutils literal"><span class="pre">invertRate_()</span></tt>.</p>
<p>In the <tt class="docutils literal"><span class="pre">MainMenu.nib</span> <span class="pre">main</span></tt> window open the <em>MainMenu</em> menubar. Select the <tt class="docutils literal"><span class="pre">Edit</span></tt>
menu. Make sure the <em>Menus</em> palette is open and selected, drag a separator to the 
<tt class="docutils literal"><span class="pre">Edit</span></tt> menu and then drag an <tt class="docutils literal"><span class="pre">Item</span></tt> there.  Double-click the item and set the text to
<tt class="docutils literal"><span class="pre">Invert</span> <span class="pre">Exchange</span> <span class="pre">Rate</span></tt>.</p>
<p>Make the connection by control-dragging from the new <tt class="docutils literal"><span class="pre">Invert</span> <span class="pre">Exchange</span> <span class="pre">Rate</span></tt> menu item to
the <tt class="docutils literal"><span class="pre">ConverterController</span></tt> instance in the Instances tab in the <tt class="docutils literal"><span class="pre">MainMenu.nib</span></tt> main window.
<em>NOTE:</em> you drag to the <em>instance</em> of <tt class="docutils literal"><span class="pre">ConverterController</span></tt>, not to the class.
In the <em>Info</em> panel, <em>Connections</em> section, select <tt class="docutils literal"><span class="pre">invertRate:</span></tt> and press <em>Connect</em>.</p>
</li>
<li><p class="first">We know our program can't invert rates yet, because we haven't actually written the code
to do it, but we are going to try it anyway, just to see what sort of spectacular
crash we get. Alas, nothing spectacular about it: when the NIB is loaded the Cocoa runtime
system tries to make the connection, notices that we have no <tt class="docutils literal"><span class="pre">invertRate_()</span></tt> method in
our <tt class="docutils literal"><span class="pre">ConverterController</span></tt> class and it gives an error message:</p>
<pre class="literal-block">
$ ./dist/CurrencyConverter.app/Contents/MacOS/CurrencyConverter 
2004-12-09 03:29:09.957 CurrencyConverter[4454] Could not connect the action 
invertRate: to target of class ConverterController
</pre>
<p>Moreover, it has disabled the <tt class="docutils literal"><span class="pre">Invert</span> <span class="pre">Exchange</span> <span class="pre">Rate</span></tt> menu command and continues, so the 
program works as it did before, only with one more (disabled) menu item.</p>
</li>
</ol>
</div>
<div class="section" id="debugging">
<h3><a name="debugging">Debugging</a></h3>
<ol class="arabic" start="11">
<li><p class="first">Writing the code is easy: add a method <tt class="docutils literal"><span class="pre">invertRate_(self,</span> <span class="pre">sender)</span></tt> that gets the float
value of <tt class="docutils literal"><span class="pre">rateField</span></tt>, inverts it and puts it back. We deliberately forget to test for
divide by zero. We run the program again, and now the menu entry is enabled. After
trying it with a couple of non-zero exchange rates we try it with an exchange rate of
zero (or empty, which is the same). We get a dialog box giving the Python exception, and
offering the choice of continuing or quitting.</p>
<p>To debug this application with pdb, start the application with the following command line:</p>
<pre class="literal-block">
$ USE_PDB=1 ./dist/CurrencyConverter.app/Contents/MacOS
</pre>
<p>When running in this mode, we will get a <tt class="docutils literal"><span class="pre">pdb.post_mortem(...)</span></tt> console in the terminal
instead of the alert panel.  You can see this in action if you try and invert an exchange
rate of <tt class="docutils literal"><span class="pre">0</span></tt>.</p>
</li>
<li><p class="first">Fix the final bug by testing for <tt class="docutils literal"><span class="pre">rate</span> <span class="pre">==</span> <span class="pre">0.0</span></tt> in <tt class="docutils literal"><span class="pre">invertRate_()</span></tt>. The result is in the
<a class="reference" href="step12-src.zip">step12-src</a> directory.</p>
</li>
</ol>
</div>
<div class="section" id="creating-a-redistributable-application">
<h3><a name="creating-a-redistributable-application">Creating a redistributable application</a></h3>
<p>Your application is finished, and you want to run it on other computers, or
simply just move it to the <tt class="docutils literal"><span class="pre">Applications</span></tt> folder (or anywhere else) and
insulate it from the original source code.</p>
<p>This can be done with the following steps from the <tt class="docutils literal"><span class="pre">src</span></tt> directory:</p>
<pre class="literal-block">
$ rm -rf dist
$ python setup.py py2app
</pre>
<p>Now the application bundle located at <tt class="docutils literal"><span class="pre">dist/CurrencyConverter.app</span></tt> is a fully
standalone application that should run on any computer running the same major
version of Mac OS X or later.  This means that applications built on Mac OS X 10.2
are compatible with Mac OS X 10.3, but NOT vice versa.  If you are not using
an Apple-supplied version of Python, a subset of your Python installation will
be included in this application.</p>
<p>For more complicated examples of py2app usage to do things such as change the
application's icon, see the Examples or the py2app documentation.</p>
</div>
</div>
<?
    include "footer.inc";
?>