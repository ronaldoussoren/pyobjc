<?
    $title = "Installation Instructions";
    $cvs_author = '$Author: ronaldoussoren $';
    $cvs_date = '$Date: 2003/02/12 20:43:00 $';

    include "header.inc";
?>
<div class="document" id="installation-instructions">
<h1 class="title">Installation Instructions</h1>
<!-- :author: Bill Bumgarner -->
<div class="section" id="building-the-module">
<h1><a name="building-the-module">Building the Module</a></h1>
<p>The module uses the distutils package included with Python 2.0 and
beyond.   This package provides a single interface for building and
packaging the module.   To see usage documentation for the module,
issue the <tt class="literal"><span class="pre">--help</span></tt> command:</p>
<pre class="literal-block">
% python setup.py --help
</pre>
<p>To see an inventory of building and packaging commands, issue the
command:</p>
<pre class="literal-block">
% python setup.py --help-commands
</pre>
<p>The following command will build and install the pyobjc module:</p>
<pre class="literal-block">
% python setup.py install
</pre>
<p>The setup.py system can also be used to create source and binary
distribution archives automatically.</p>
<p>Use <tt class="literal"><span class="pre">sudo</span></tt> to install the pyobjc module into a the Apple supplied
python's site-packages directory on OS X 10.2 and greater:</p>
<p>% sudo python setup.py install</p>
<p>If you have multiple versions of python installed on your system, the
above will only install pyobjc for whatever version of python is the
default on the command line.   Make sure you are installing python
against the correct version of python.</p>
</div>
<div class="section" id="examples">
<h1><a name="examples">Examples</a></h1>
<p>The examples directory contains a number of projects that demonstrate
various features of the PyObjC bridge. The scripts at the top level of
the examples directory were mostly written to test a particular
feature of the bridge (or document a bug until a fix could be found).</p>
<p>CurrencyConverter and TableModel are both examples of standalone
Cocoa-Python applications.  To build and execute:</p>
<pre class="literal-block">
% cd TableModel
% python buildapp.py build
</pre>
<p>The WebServicesTool and TableModel2 are both examples of Cocoa-Python
applications created via the Cocoa-Python project template found in
the <tt class="literal"><span class="pre">Project</span> <span class="pre">Templates</span></tt> directory.  Use Project Builder to build the
applications.</p>
</div>
<div class="section" id="project-templates">
<h1><a name="project-templates">Project Templates</a></h1>
<p>The <tt class="literal"><span class="pre">Project</span> <span class="pre">Templates</span></tt> directory contains project templates for
project builder.  Currently, there is one project builder template;  a
Cocoa-Python Application project template.   When installed, this adds
a project to Project Builder's project menu that allows new Cocoa
applications implemented entirely in Python to be created from within
Project Builder (in the same fashion as any other project).</p>
<p>To install, simply copy the project template into the Project Builder
project templates directory (or create a symlink).</p>
<p>More information on project templates can be found in the Project
Builder documentation and/or release notes.</p>
</div>
</div>
<?
    include "footer.inc";
?>