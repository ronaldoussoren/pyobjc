<?
    $title = "PyObjCTools: The PyObjC Toolbox";
    $cvs_author = '$Author: ronaldoussoren $';
    $cvs_date = '$Date: 2003/07/05 14:59:47 $';

    include "header.inc";
?>
<div class="document" id="pyobjctools-the-pyobjc-toolbox">
<p>The package <tt class="literal"><span class="pre">PyObjCTools</span></tt> contains a number of (basically unrelated) modules
with useful functionality. These have been placed inside a module to avoid
cluttering the global namespace.</p>
<p>The rest of this document provides documentation for these modules, but lets
start with a short overview.</p>
<ul class="simple">
<li><tt class="literal"><span class="pre">PyObjCTools.AppHelper</span></tt></li>
</ul>
<p>Utility functions for use with the <tt class="literal"><span class="pre">AppKit</span></tt> module.</p>
<ul class="simple">
<li><tt class="literal"><span class="pre">PyObjCTools.Conversion</span></tt></li>
</ul>
<p>Functions for converting between Cocoa and pure Python data structures.</p>
<ul class="simple">
<li><tt class="literal"><span class="pre">PyObjCTools.KeyValueCoding</span></tt></li>
</ul>
<p>A Python API for working with <a class="reference" href="http://developer.apple.com/documentation/Cocoa/Conceptual/KeyValueCoding/">Key-Value Coding</a>.</p>
<ul class="simple">
<li><tt class="literal"><span class="pre">PyObjCTools.NibClassBuilder</span></tt></li>
</ul>
<p>Module containing a magic super-class that can read information about the
actual super-class and implemented actions and outlets from a NIB file.</p>
<ul class="simple">
<li><tt class="literal"><span class="pre">PyObjCTools.MachSignals</span></tt></li>
</ul>
<p>Module to make it possible to integrate signal handling into the main
runloop.</p>
<ul class="simple">
<li><tt class="literal"><span class="pre">PyObjCTools.Debugging</span></tt></li>
</ul>
<p>Allows logging of NSException stack traces.  This module should only be used
during development.</p>
<ul class="simple">
<li><tt class="literal"><span class="pre">PyObjCTools.Signals</span></tt></li>
</ul>
<p>Module that tries to print useful information when the program gets a fatal
exception. This module should only be used during development.</p>
<div class="section" id="pyobjctools-apphelper">
<h1><a name="pyobjctools-apphelper"><tt class="literal"><span class="pre">PyObjCTools.AppHelper</span></tt></a></h1>
<p>This module exports two functions that are useful when working with the
<tt class="literal"><span class="pre">AppKit</span></tt> framework.</p>
<ul>
<li><p class="first"><tt class="literal"><span class="pre">endSheetMethod(method)</span> <span class="pre">-&gt;</span> <span class="pre">selector</span></tt></p>
<p>Convert a method to a form that is suitable to use as the delegate callback
for sheet methods.</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">runEventLoop(argv=None,</span> <span class="pre">unexpectedErrorAlert=unexpectedErrorAlert)</span> <span class="pre">-&gt;</span> <span class="pre">None</span></tt></p>
<p>Run the event loop using <tt class="literal"><span class="pre">NSApplicationMain</span></tt> and ask the user if we should
continue if an exception is caught.</p>
<p>This function doesn't return unless it throws an exception.</p>
</li>
</ul>
</div>
<div class="section" id="pyobjctools-conversiony">
<h1><a name="pyobjctools-conversiony"><tt class="literal"><span class="pre">PyObjCTools.Conversiony</span></tt></a></h1>
<p>Functions for converting between Cocoa and pure Python data structures.</p>
<ul>
<li><p class="first"><tt class="literal"><span class="pre">propertyListFromPythonCollection(pyCol,</span> <span class="pre">conversionHelper=None)</span> <span class="pre">-&gt;</span> <span class="pre">ocCol</span></tt></p>
<p>Convert a Python collection (dictionary, array, tuple, string) into an 
Objective-C collection.</p>
<p>If conversionHelper is defined, it must be a callable.  It will be called 
for any object encountered for which <tt class="literal"><span class="pre">propertyListFromPythonCollection()</span></tt>
cannot automatically convert the object.   The supplied helper function 
should convert the object and return the converted form.  If the conversion 
helper cannot convert the type, it should raise an exception or return None.</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">pythonCollectionFromPropertyList(ocCol,</span> <span class="pre">conversionHelper=None)</span> <span class="pre">-&gt;</span> <span class="pre">pyCol</span></tt></p>
<p>Converts a Foundation based collection-- a property list-- into a Python 
collection.  Like <tt class="literal"><span class="pre">propertyListFromPythonCollection()</span></tt>, <tt class="literal"><span class="pre">conversionHelper</span></tt>
is an optional callable that will be invoked any time an encountered object 
cannot be converted.</p>
</li>
</ul>
</div>
<div class="section" id="pyobjctools-keyvaluecoding">
<h1><a name="pyobjctools-keyvaluecoding"><tt class="literal"><span class="pre">PyObjCTools.KeyValueCoding</span></tt></a></h1>
<p>A module for working with Key-Value Coding in Python. Key-Value Coding is
explained <a class="reference" href="http://developer.apple.com/documentation/Cocoa/Conceptual/KeyValueCoding/">on the Apple website</a></p>
<p>This module provides a Python interface to some of that functionality. The
interface is modeled on the <tt class="literal"><span class="pre">getattr</span></tt> and <tt class="literal"><span class="pre">setattr</span></tt> functions.</p>
<ul>
<li><p class="first"><tt class="literal"><span class="pre">getKey(object,</span> <span class="pre">key)</span> <span class="pre">-&gt;</span> <span class="pre">value</span></tt></p>
<p>Find the value for <tt class="literal"><span class="pre">key</span></tt>. Raises <tt class="literal"><span class="pre">KeyError</span></tt> if the key is not a valid
attribute of the object.</p>
<p>To find the value of a key the following values are tried for a key named
<tt class="literal"><span class="pre">key</span></tt> (first match wins):</p>
<ul class="simple">
<li>the return value of <tt class="literal"><span class="pre">object.get_key()</span></tt></li>
<li>the return value of <tt class="literal"><span class="pre">object.getKey()</span></tt></li>
<li>the return value of <tt class="literal"><span class="pre">object._get_key()</span></tt></li>
<li>the return value of <tt class="literal"><span class="pre">object._getKey()</span></tt></li>
<li>the value of the attribute <tt class="literal"><span class="pre">key</span></tt>, or the value of <tt class="literal"><span class="pre">object.key()</span></tt> if
<tt class="literal"><span class="pre">object.key</span></tt> is a method.</li>
<li>the value of the attribute <tt class="literal"><span class="pre">_key</span></tt>, or the vale of <tt class="literal"><span class="pre">object._key()</span></tt> if
<tt class="literal"><span class="pre">object._key</span></tt> is a method.</li>
</ul>
</li>
<li><p class="first"><tt class="literal"><span class="pre">getKeyPath(object,</span> <span class="pre">keypath)</span> <span class="pre">-&gt;</span> <span class="pre">value</span></tt></p>
<p>Like <tt class="literal"><span class="pre">getKey</span></tt> but using a key path. The <tt class="literal"><span class="pre">keypath</span></tt> is a sequence of keys
separated by dots. It calls <tt class="literal"><span class="pre">getKey</span></tt> to follow the path and returns the
final value.</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">setKey(object,</span> <span class="pre">key,</span> <span class="pre">value)</span> <span class="pre">-&gt;</span> <span class="pre">None</span></tt></p>
<p>Set the value of <tt class="literal"><span class="pre">key</span></tt> to <tt class="literal"><span class="pre">value</span></tt>.</p>
<p>The following values are used for setting the value for a key named <tt class="literal"><span class="pre">key</span></tt>
(first match wins):</p>
<ul class="simple">
<li>Call <tt class="literal"><span class="pre">object.set_key(value)</span></tt></li>
<li>Call <tt class="literal"><span class="pre">object.setKey(value)</span></tt></li>
<li>Call <tt class="literal"><span class="pre">object._set_key(value)</span></tt></li>
<li>Call <tt class="literal"><span class="pre">object._setKey(value)</span></tt></li>
<li>Check if <tt class="literal"><span class="pre">_key</span></tt> is an attribute and if so, set its value</li>
<li>Try to set the attribute <tt class="literal"><span class="pre">key</span></tt>.</li>
</ul>
<p>Raises <tt class="literal"><span class="pre">KeyError</span></tt> if the key cannot be changed.</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">setKeyPath(object,</span> <span class="pre">keypath,</span> <span class="pre">value)</span> <span class="pre">-&gt;</span> <span class="pre">None</span></tt></p>
<p>The same as <tt class="literal"><span class="pre">setKey</span></tt>, but now using a key path. A key path is a sequence
of keys separated by dots. The <tt class="literal"><span class="pre">getKey</span></tt> function is used to traverse 
the path up to the last item, and then <tt class="literal"><span class="pre">setKey</span></tt> is used to change the value.</p>
</li>
</ul>
</div>
<div class="section" id="pyobjctools-nibclassbuilder">
<h1><a name="pyobjctools-nibclassbuilder">PyObjCTools.NibClassBuilder</a></h1>
<div class="section" id="extracting-class-definitions-from-nibs">
<h2><a name="extracting-class-definitions-from-nibs">Extracting class definitions from nibs</a></h2>
<p>The module maintains a global set of class definitions, extracted from
nibs. To add the classes from a nib to this set, use the <tt class="literal"><span class="pre">extractClasses()</span></tt>
function. It can be called in two ways:</p>
<ul>
<li><p class="first"><tt class="literal"><span class="pre">extractClasses(nibName,</span> <span class="pre">bundle=&lt;main-bundle&gt;)</span></tt></p>
<p>This finds the nib by name from a bundle. If no bundle
if given, the main bundle is searched.</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">extractClasses(path=pathToNib)</span></tt></p>
<p>This uses an explicit path to a nib.</p>
</li>
</ul>
<p><tt class="literal"><span class="pre">extractClasses()</span></tt> can be called multiple times for the same bundle: the
results are cached so no almost extra overhead is caused.</p>
</div>
<div class="section" id="using-the-class-definitions">
<h2><a name="using-the-class-definitions">Using the class definitions</a></h2>
<p>The module contains a &quot;magic&quot; base (super) class called <tt class="literal"><span class="pre">AutoBaseClass</span></tt>.
Subclassing <tt class="literal"><span class="pre">AutoBaseClass</span></tt> will invoke some magic that will look up the
proper base class in the class definitions extracted from the nib(s).
If you use multiple inheritance to use Cocoa's &quot;informal protocols&quot;,
you <em>must</em> list <tt class="literal"><span class="pre">AutoBaseClass</span></tt> as the first base class. For example:</p>
<pre class="literal-block">
class PyModel(AutoBaseClass, NSTableSource):
    ...
</pre>
</div>
<div class="section" id="the-nibinfo-class">
<h2><a name="the-nibinfo-class">The <tt class="literal"><span class="pre">NibInfo</span></tt> class</a></h2>
<p>The parsing of nibs and collecting the class definition is done by the
<tt class="literal"><span class="pre">NibInfo</span></tt> class. You normally don't use it directly, but it's here if you
have special needs.</p>
</div>
<div class="section" id="the-command-line-tool">
<h2><a name="the-command-line-tool">The command line tool</a></h2>
<p>When run from the command line, this module invokes a simple command
line program, which you feed paths to nibs. This will print a Python
template for all classes defined in the nib(s). For more documentation,
see the commandline_doc variable, or simply run the program without
arguments. It also contains a simple test program.</p>
</div>
</div>
<div class="section" id="pyobjctools-signals">
<h1><a name="pyobjctools-signals">PyObjCTools.Signals</a></h1>
<p>This module provides two functions that can be useful while investigating
random crashes of a PyObjC program. These crashes are often caused by 
Objective-C style weak references or incorrectly implemented protocols.</p>
<ul>
<li><p class="first"><tt class="literal"><span class="pre">dumpStackOnFatalSignal()</span></tt></p>
<p>This function will install signal handlers that print a stack trace and
then re-raise the signal.</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">resetFatalSignals()</span></tt></p>
<p>Restores the signal handlers to the state they had before the call to
dumpStackOnFatalSignal.</p>
</li>
</ul>
<p>This module is not designed to provide fine grained control over signal 
handling. Nor is it intended to be terribly robust. It may give useful
information when your program gets unexpected signals, but it might just
as easily cause a crash when such a signal gets in.</p>
</div>
</div>
<?
    include "footer.inc";
?>