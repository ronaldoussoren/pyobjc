<?
    $title = "Installation Instructions";
    $cvs_author = '$Author: ronaldoussoren $';
    $cvs_date = '$Date: 2003/07/05 14:59:47 $';

    include "header.inc";
?>
<h1 class="title">Installation Instructions</h1>
<!-- :authors: Bill Bumgarner, Ronald Oussoren, Bob Ippolito -->
<div class="section" id="building-the-package">
<h3><a name="building-the-package">Building the package</a></h3>
<p>PyObjC is built and installed using the distutils package included with Python
2.0 and beyond.  distutils provides a single interface for building and
packaging the PyObjC via a <tt class="docutils literal"><span class="pre">setup.py</span></tt> script. To see usage documentation
for <tt class="docutils literal"><span class="pre">setup.py</span></tt>, issue the <tt class="docutils literal"><span class="pre">--help</span></tt> command:</p>
<pre class="literal-block">
% python setup.py --help
</pre>
<p>To see an inventory of building and packaging commands, issue the
command:</p>
<pre class="literal-block">
% python setup.py --help-commands
</pre>
<p>The following command will build and open a binary installer for PyObjC,
py2app, tools, examples, and documentation:</p>
<pre class="literal-block">
% python setup.py bdist_mpkg --open
</pre>
<p>When multiple versions of Python are installed, the above examples
will use the default interpreter.  Unless you have changed your
<tt class="docutils literal"><span class="pre">PATH</span></tt> environment variable, this will be the Python interpreter
that ships with Mac OS X.  To use PyObjC with an alternate Python
interpreter, specify it explicitly or manipulate your <tt class="docutils literal"><span class="pre">PATH</span></tt>
such that the location of the Python interpreter comes before
<tt class="docutils literal"><span class="pre">/usr/bin</span></tt>.</p>
<p>Note that there is a known bug in Python 2.3.0 
(as shipped with Mac OS X 10.3), such that when another framework Python is 
installed it will not link extensions (such as PyObjC) properly, rendering
them unusable.  If you intend to build PyObjC for Python 2.3.0, first install
the <a class="reference" href="http://homepages.cwi.nl/~jack/macpython/beta.html">PantherPythonFix</a> package from <a class="reference" href="http;//pythonmac.org/packages/">pythonmac.org packages</a>.</p>
<p>If you have a previous version of PyObjC installed, you may see an exception
such as <tt class="docutils literal"><span class="pre">Wrong</span> <span class="pre">version</span> <span class="pre">of</span> <span class="pre">PyObjC</span> <span class="pre">C</span> <span class="pre">API</span></tt>.  If this happens, you should
delete any previous installation of PyObjC and the build folder in your
new sources and try again.  PyObjC will typically be installed to a folder
of the same name in <tt class="docutils literal"><span class="pre">/Library/Python/2.3</span></tt> or
<tt class="docutils literal"><span class="pre">/Library/Python/2.3/site-packages</span></tt>.</p>
<p>When using Mac OS X 10.2, you must install the WebKit SDK from the
<a class="reference" href="http://connect.apple.com">ADC website</a> in order to build or use
the WebKit wrapper.</p>
</div>
<div class="section" id="examples">
<h3><a name="examples">Examples</a></h3>
<p>The <a class="reference" href="Examples/00ReadMe.html">examples directory</a> contains a number of projects that demonstrate
various features of the PyObjC bridge. The scripts at the top level of
the <a class="reference" href="Examples/00ReadMe.html">examples directory</a> were mostly written to test a particular
feature of the bridge (or document a bug until a fix could be found).</p>
<p>CurrencyConverter and TableModel are both examples of standalone
Cocoa-Python applications.  To build and execute:</p>
<pre class="literal-block">
% cd TableModel
% python setup.py py2app
% open dist/TableModel.app
</pre>
<p>The preferred method for building the examples is to use a py2app-based
setup.py, as above.  Some examples may also have an Xcode (.xcode)
or Project Builder (.pbproj) project file, but these may be out of date.</p>
<p>All of the examples are always installed whether or not the target
operating system supports them.  If an example fails to run due to a
ImportError, it is likely that the example is intended for a newer
version of Mac OS X.</p>
</div>
<div class="section" id="project-templates">
<h3><a name="project-templates">Project Templates</a></h3>
<div class="section" id="xcode-on-mac-os-x-10-3">
<h4><a name="xcode-on-mac-os-x-10-3">Xcode on Mac OS X 10.3+</a></h4>
<p>The <tt class="docutils literal"><span class="pre">Xcode</span></tt> directory contains some file and project that make it easier to
work with Python and PyObjC when using <a class="reference" href="http://www.apple.com/xcode">Xcode</a>.</p>
<p>For documentation on these templates, see <a class="reference" href="Xcode-templates.html">Xcode-Templates.html</a></p>
<p>Normally these Xcode templates are installed with PyObjC by the package installer.
If doing development, you may copy or symlink them to the appropriate places in
<tt class="docutils literal"><span class="pre">/Library/Application</span> <span class="pre">Support/Apple/Developer</span> <span class="pre">Tools/</span></tt>.</p>
</div>
<div class="section" id="project-builder-on-mac-os-x-10-2">
<h4><a name="project-builder-on-mac-os-x-10-2">Project Builder on Mac OS X 10.2</a></h4>
<p>The Project Builder templates are out of date and unsupported.  You should
use py2app exclusively when developing on Mac OS X 10.2.</p>
<p>The <tt class="docutils literal"><span class="pre">ProjectBuilder</span> <span class="pre">Extras</span></tt> directory contains additional files that can
be used with Project Builder. The directory <tt class="docutils literal"><span class="pre">Specifications</span></tt> contains files
that enable syntax coloring for Python files in Project Builder.</p>
<p>The <tt class="docutils literal"><span class="pre">Project</span> <span class="pre">Templates</span></tt> directory contains project templates for
Project Builder.  These have to be copied to
<tt class="docutils literal"><span class="pre">/Developer/ProjectBuilder</span> <span class="pre">Extras/Project</span> <span class="pre">Templates/Application</span></tt> before
they are useable from Project Builder.</p>
<p>There are three templates available:</p>
<ul>
<li><p class="first">Cocoa-Python Application</p>
<p>A project created from this template is designed to implement standalone,
pure-Python, applications that are compatible with Apple's build of Python as
well as all other builds of python that support PyObjC.</p>
<p>When building the 'install' target, the resulting application wrapper will
include the PyObjC module and can be launched on any stock OS X 10.2 system
without requiring PyObjC to be preinstalled.</p>
</li>
<li><p class="first">Cocoa-Python-ObjC Application</p>
<p>A project created from this template includes an embedded framework project
into which all compiled (Objective-C) code can be placed.  Upon launch, 
the application automatically dynamically loads the embedded framework 
containing the compiled code.</p>
<p>Each Framework's Resources directory is automatically added to sys.path.</p>
</li>
<li><p class="first">Cocoa-Python Document-based Application</p>
<p>This template works like the Cocoa-Python Application template in that it
is compatible with the Apple build of Python.   It creates an application 
that uses Cocoa's Multiple Document Architecture in the same fashion as the
default Cocoa Document-based Application supplied with Project Builder.</p>
</li>
</ul>
<p>More information on project templates can be found in the Project
Builder documentation and/or release notes.</p>
</div>
</div>
</div>
<?
    include "footer.inc";
?>