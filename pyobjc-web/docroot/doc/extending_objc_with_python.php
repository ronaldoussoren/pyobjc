<?
    $title = "Tutorial - Adding Python code to an existing ObjC application";
    $cvs_author = '$Author: ronaldoussoren $';
    $cvs_date = '$Date: 2003/07/05 14:59:47 $';

    include "header.inc";
?>
<div class="document" id="tutorial-adding-python-code-to-an-existing-objc-application">
<p>In this tutorial we are going to take an existing ObjC application and
add Python and PyObjC to it. One of the reasons why you may want to do
this is because some things are much simpler in Python than in ObjC, mainly
due to the rich library Python has.</p>
<p>To follow the tutorial you need:</p>
<blockquote>
<ul class="simple">
<li>PyObjC 1.2</li>
<li>py2app 0.1.6 or later (included in the binary installer for PyObjC)</li>
<li>Python 2.3 or later (note: PyObjC is NOT compatible with MacPython-OS9)</li>
<li>Mac OS X 10.3 or later</li>
<li>Xcode Tools</li>
</ul>
</blockquote>
<p>If you do not have a <tt class="literal"><span class="pre">/Developer</span></tt> folder, then you do not have Xcode Tools
installed.  See <a class="reference" href="http://developer.apple.com/tools/download/">Getting the Xcode Tools</a>.</p>
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
$ cp -R /Developer/Examples/AppKit/SimpleComboBox SimpleComboBoxPlus
</pre>
</li>
</ol>
<blockquote>
From this point on, all shell commands take place from this
<tt class="literal"><span class="pre">SimpleComboBoxPlus</span></tt> folder.</blockquote>
<ol class="arabic" start="2">
<li><p class="first">Open it in Xcode, build it, and see what it does.</p>
</li>
<li><p class="first">Open <tt class="literal"><span class="pre">CDInfoDocument.nib</span></tt>. Select the Class View, <tt class="literal"><span class="pre">NSObject</span></tt>, subclass
as <tt class="literal"><span class="pre">ITunesCommunication</span></tt>. Give the class an <tt class="literal"><span class="pre">askITunes:</span></tt> action.
Instantiate the class as object <tt class="literal"><span class="pre">ITunesCommunication</span></tt>.  This wll be the
class that we write in Python.</p>
</li>
<li><p class="first">Go to the object view again, open the Window.</p>
</li>
<li><p class="first">Move the text box down a bit to make space, add a button &quot;ask iTunes&quot;.</p>
</li>
<li><p class="first">Connect this button to the <tt class="literal"><span class="pre">askITunes:</span></tt> action of the
<tt class="literal"><span class="pre">ITunesCommunication</span></tt> object.</p>
</li>
<li><dl class="first">
<dt>We now need to write the code implementing the <tt class="literal"><span class="pre">ITunesCommunication</span></tt></dt>
<dd><p class="first last">class.  As this tutorial is about using PyObjC in existing ObjC programs
and not about PyObjC itself, we are going to skip writing the code and
simply copy <tt class="literal"><span class="pre">src/ITunesCommunication_1.py</span></tt> to <tt class="literal"><span class="pre">ITunesCommunication.py</span></tt>.</p>
</dd>
</dl>
</li>
<li><p class="first">Now we need to create the build script for our plugin, create a file named
<tt class="literal"><span class="pre">setup.py</span></tt> with the following contents:</p>
<pre class="literal-block">
from distutils.core import setup
import py2app

setup(
    plugin = ['ITunesCommunication.py']
)   
</pre>
<p>You may also copy this file from <tt class="literal"><span class="pre">src/setup.py</span></tt>.</p>
</li>
<li><p class="first">Run the setup script to create a temporary plugin bundle for development:</p>
<pre class="literal-block">
    $ python setup.py py2app -A

Note that we use the ``-A`` argument to create an alias plugin bundle at
``dist/ITunesCommunication.py``.  Alias bundles contain an alias to the
main script (``ITunesCommunication.py``) and symlinks to the data files
(none in this case).  This allows us to keep working on the source files
without having to rebuild the application.  This alias bundle is similar
to a ZeroLink executable in Xcode - it is for DEVELOPMENT ONLY, and will
not work on other machines.
</pre>
</li>
<li><p class="first">Add <tt class="literal"><span class="pre">dist/ITunesCommunication.plugin</span></tt> to the Resources folder in your
Xcode project.  You can do this by ctrl-clicking the Resources folder
and choosing &quot;Add Existing Files...&quot;.</p>
</li>
<li><p class="first">Open <tt class="literal"><span class="pre">main.m</span></tt>, it is in the &quot;Other Sources&quot; folder in your Xcode
project, and change the main(...) function to the following:</p>
<pre class="literal-block">
int main(int argc, const char *argv[]) {
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
    NSString *pluginPath = [[NSBundle mainBundle]
                                pathForResource:&#64;&quot;ITunesCommunication&quot;
                                         ofType:&#64;&quot;plugin&quot;];
    NSBundle *pluginBundle = [NSBundle bundleWithPath:pluginPath];
    [pluginBundle load];
    [pool release];
    return NSApplicationMain(argc, argv);
}
</pre>
<p>You may also copy a full main.m from <tt class="literal"><span class="pre">src/main.m</span></tt>.  This code ensures
that our ITunesCommunication plugin is loaded before the nib
files.</p>
</li>
<li><p class="first">Build and run. When you press the &quot;Ask iTunes&quot; the &quot;CD Title&quot; and
&quot;Band Name&quot; fields will be filled with one of the best albums of the last
few years :-)</p>
</li>
<li><p class="first">Now we need to make the program talk to iTunes. The current MacPython
interface to the Open Scripting Architecture requires an extra step when
compared to AppleScript: you need to manually generate a Python package
that wraps all the AppleScript terminology for an application. To make
matters more complicated iTunes is one of those special cases where the
standard way to generate this package (start the application, ask it for
its terminology) does not work, so we have to actually look into the
bowels of <tt class="literal"><span class="pre">iTunes.app</span></tt>. This leads to the following hefty command line
which you should run in the <tt class="literal"><span class="pre">SimpleComboBoxPlus</span></tt> directory:</p>
<pre class="literal-block">
$ cd SimpleComboBoxPlus
$ pythonw -c &quot;from gensuitemodule import main;main()&quot; \
    --output iTunes --creator hook --resource \
    /Applications/iTunes.app/Contents/Resources/iTunes.rsrc
</pre>
</li>
<li><p class="first">Finally, add the code to <tt class="literal"><span class="pre">ITunesCommunication.py</span></tt> to actually communicate
with iTunes. We cop out and copy it from <tt class="literal"><span class="pre">src/ITunesCommunication_2.py</span></tt>.</p>
</li>
<li><p class="first">Build and run. If you press the button when iTunes is playing the Title
and Band names will be filled, otherwise they will be cleared. In a real
application you would disable the &quot;Ask iTunes&quot; button unless iTunes was
active. All that is left as an exercise to the reader.</p>
</li>
<li><p class="first">To make this application redistributable, perform the following commands
to make the plugin redistributable:</p>
<pre class="literal-block">
$ rm -rf dist
$ python setup.py py2app
</pre>
<p>Then, from Xcode, clean your project (shift-cmd-K), switch to Deployment
mode, and rebuild.</p>
</li>
</ol>
<div class="section" id="a-minor-variation">
<h1><a name="a-minor-variation">A minor variation</a></h1>
<p>There a several projects that improve upon the built-in AppleScript support
(or to be more precise &quot;application scripting support&quot;). One of those is
<a class="reference" href="http://freespace.virgin.net/hamish.sanderson/appscript.html">AppScript</a>.</p>
<p>When you have this module installed you can replace the contents of
<tt class="literal"><span class="pre">ITunesCommuncation.py</span></tt> with <tt class="literal"><span class="pre">src/ITunesCommunication_AppScript.py</span></tt>,
and you can skip step 13 entirely.</p>
</div>
</div>
<?
    include "footer.inc";
?>