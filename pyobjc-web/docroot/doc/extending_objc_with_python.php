<?
    $title = "Tutorial - Adding Python code to an existing ObjC application";
    $cvs_author = '$Author: ronaldoussoren $';
    $cvs_date = '$Date: 2004/02/02 15:23:01 $';

    include "header.inc";
?>
<div class="document" id="tutorial-adding-python-code-to-an-existing-objc-application">
<h1 class="title">Tutorial - Adding Python code to an existing ObjC application</h1>
<p>In this tutorial we are going to take an existing ObjC application and
add Python and PyObjC to it. One of the reasons why you may want to do
this is because some things are much simpler in Python than in ObjC, mainly
due to the rich library Python has.</p>
<p>At the time of this writing this tutorial only works with a framework-based
python 2.3 (also known as MacPython-2.3), it does not work with Apple's
<tt class="literal"><span class="pre">/usr/bin/python</span></tt> 2.2. The reason for this is that Apple forgot to ship
the Python dynamic library, so you cannot embed this Python in your
application.</p>
<p>You will also need the Apple Developer Kit, and it is expected you are familiar
with using Project Builder, Interface Builder and Terminal. MacPython 2.3b2
or later is expected in the
standard location (<tt class="literal"><span class="pre">/Library/Frameworks</span></tt>, with auxiliary executables
in <tt class="literal"><span class="pre">/usr/local/bin</span></tt> and on your <tt class="literal"><span class="pre">$PATH</span></tt>).</p>
<p>The application we are going to modify is Apple's SimpleComboBox example.
This example shows you how to use combo boxes, but that is not what interests
us right now: the application pretends to be a database application that allows
you to keep notes (such as track list) for your CD collection. With such an
application it feels silly that even though you want to type notes on
the CD you are currently playing in iTunes you still have to retype
album title, artist and genre. This is what we are going to fix: we
are going to add a button &quot;ask iTunes&quot;, which will use Python's
AppleScript support to ask iTunes about the currently playing track
and fill in the fields for you.</p>
<p>Follow these steps:</p>
<ol class="arabic">
<li><p class="first">Make a copy of <tt class="literal"><span class="pre">/Developer/Examples/AppKit/SimpleComboBox</span></tt> to work on.
Let's call this <tt class="literal"><span class="pre">SimpleComboBoxPlus</span></tt>:</p>
<pre class="literal-block">
% cp -R /Developer/Examples/AppKit/SimpleComboBox SimpleComboBoxPlus
</pre>
</li>
<li><p class="first">Open it in Project Builder, build it, and see what it does.</p>
</li>
<li><p class="first">Copy <tt class="literal"><span class="pre">PythonGlue.h</span></tt>, <tt class="literal"><span class="pre">PythonGlue.m</span></tt> and <tt class="literal"><span class="pre">PythonGlue.py</span></tt> from <tt class="literal"><span class="pre">src</span></tt>
into the <tt class="literal"><span class="pre">SimpleComboBoxPlus</span></tt> folder:</p>
<pre class="literal-block">
% cp -R src/PythonGlue.* SimpleComboBoxPlus
</pre>
</li>
<li><p class="first">Add <tt class="literal"><span class="pre">PythonGlue.h</span></tt> and <tt class="literal"><span class="pre">PythonGlue.m</span></tt> to the &quot;Classes&quot; group.</p>
<p>These files contain a class <tt class="literal"><span class="pre">PythonGlue</span></tt> that does nothing
visibly useful, but it has interesting side effects: when the first
class instance is initialized it will initialize the Python interpreter,
add the Resource folder of your application to the Python search path
and import any modules from that Resources folder. The first bit of
this is done by the ObjC code, the latter two by the Python code
in <tt class="literal"><span class="pre">PythonGlue.py</span></tt>.</p>
</li>
<li><p class="first">Add <tt class="literal"><span class="pre">PythonGlue.py</span></tt> to the &quot;Resources&quot; group.</p>
</li>
<li><p class="first">Select the &quot;Frameworks&quot; group, &quot;Add Framework...&quot;, 
select <tt class="literal"><span class="pre">/Library/Frameworks/Python.framework</span></tt>.</p>
</li>
<li><p class="first">Now we need to arrange to have a <tt class="literal"><span class="pre">PythonGlue</span></tt> object be instantiated
being called early during startup. A good place to do this for the
current application is when <tt class="literal"><span class="pre">MainMenu.nib</span></tt> is loaded, as it does not
contain any Python dependencies itself.</p>
<p>Open the MainMenu.nib in Interface Builder and define a subclas of 
<tt class="literal"><span class="pre">NSObject</span></tt> and call the new class PythonGlue. Instantiate it. Use this 
instance as the application delegate for the File Owner.</p>
<blockquote>
<p>Jack: I think this method will not work if you want to use Python-based
classes in your main NIB file. Suggestions for how to make sure
a PythonGlue object is instantiated before our main NIB file is read are
hereby requested.</p>
<p>Ronald: You might add <tt class="literal"><span class="pre">[[PythonGlue</span> <span class="pre">alloc]</span> <span class="pre">init]</span></tt> to <tt class="literal"><span class="pre">main.m</span></tt>, 
before the call to <tt class="literal"><span class="pre">NSApplicationMain</span></tt>. You'd also have to create an 
autorelease pool before creating the <tt class="literal"><span class="pre">PythonGlue</span></tt> instance.</p>
</blockquote>
</li>
<li><p class="first">Now compile, build and run. You will get a message printed to
standard output (&quot;PythonGlue: Warning: no Python modules found&quot;)
but all else should be well.</p>
</li>
<li><p class="first">Open <tt class="literal"><span class="pre">CDInfoDocument.nib</span></tt>. Select the Class View, <tt class="literal"><span class="pre">NSObject</span></tt>, subclass
as <tt class="literal"><span class="pre">ITunesCommunication</span></tt>. Give the class an <tt class="literal"><span class="pre">askITunes:</span></tt> action.
Instantiate the class as object <tt class="literal"><span class="pre">ITunesCommunication</span></tt>.</p>
</li>
<li><p class="first">Go to the object view again, open the Window.</p>
</li>
<li><p class="first">Move the text box down a bit to make space, add a button &quot;ask iTunes&quot;.</p>
</li>
<li><p class="first">Connect this button to the <tt class="literal"><span class="pre">askITunes:</span></tt> action of the <tt class="literal"><span class="pre">ITunesCommunication</span></tt>
object.</p>
</li>
<li><p class="first">We now need to write the code implementing the <tt class="literal"><span class="pre">ITunesCommunication</span></tt> class.
Create a file <tt class="literal"><span class="pre">ITunesCommunication.py</span></tt> in the Resources group. As this tutorial
is about using PyObjC in existing ObjC programs and not about PyObjC itself
we are going to skip the code itself and simply copy it from <tt class="literal"><span class="pre">src/ITunesCommunication_1.py</span></tt>.
Note that this is not the final code yet, it is a debug version that does not
yet talk to iTunes.</p>
<blockquote>
<p>Double-clicking on <tt class="literal"><span class="pre">ITunesCommunication.py</span></tt> in Project Builder may cause
it to try and run the code in stead of editing it. In this case bring up the
contextual menu and select &quot;Open As...&quot;-&gt;&quot;Plain Text File&quot;.</p>
</blockquote>
</li>
<li><p class="first">Build and run. When you press the &quot;Ask iTunes&quot; the &quot;CD Title&quot; and &quot;Band Name&quot;
fields will be filled with one of the best albums of the last few years:-)</p>
</li>
<li><p class="first">Now we need to make the program talk to iTunes. The MacPython implementation
to the Open Scripting Architecture requires an extra step when compared to
AppleScript: you need to manually generate a Python package that wraps all the
AppleScript terminology for an application. To make matters more complicated
iTunes is one of those special cases where the standard way to generate this
package (start the application, ask it for its terminology) does not work,
so we have to actually look into the bowels of <tt class="literal"><span class="pre">iTunes.app</span></tt>. This leads to
the following hefty command line which you should run in the
<tt class="literal"><span class="pre">SimpleComboBoxPlus</span></tt> directory:</p>
<pre class="literal-block">
% cd SimpleComboBoxPlus
% setenv FWPYTHON /Library/Frameworks/Python.framework/Versions/Current
% pythonw $FWPYTHON/lib/python2.3/plat-mac/gensuitemodule.py \
        --output iTunes --resource --creator hook \
        /Applications/iTunes.app/Contents/Resources/iTunes.rsrc
</pre>
<p>This assumes MacPython is installed in the standard place and <tt class="literal"><span class="pre">pythonw</span></tt>
is on your $PATH.</p>
</li>
<li><p class="first">Add the generated <tt class="literal"><span class="pre">iTunes</span></tt> package to your project: select the &quot;Resources&quot;,
and add <tt class="literal"><span class="pre">iTunes</span></tt>. Add it as a folder reference, not as a recursive group.</p>
</li>
<li><p class="first">Finally, add the code to <tt class="literal"><span class="pre">ITunesCommunication.py</span></tt> to actually communicate
with iTunes. We cop out and copy it from <tt class="literal"><span class="pre">src/ITunesCommunication_2.py</span></tt>.</p>
</li>
<li><p class="first">Build and run. If you press the button when iTunes is playing the Title and
Band names will be filled, otherwise they will be cleared. In a real application
you would probably put up a dialog in this case. Actually, in a real application
you would disable the &quot;Ask iTunes&quot; button unless iTunes was active. All that
is left as an exercise to the reader.</p>
</li>
</ol>
</div>
<?
    include "footer.inc";
?>