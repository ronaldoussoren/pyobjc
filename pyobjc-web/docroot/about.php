<?
$title = "About";
$cvs_author = '$Author: bbum $';
$cvs_date = '$Date: 2002/11/12 07:41:06 $';

include "header.inc";
?>


<h1>More About PyObjC</h1>

<h2>What is PyObjC?</h2>

<p>
The PyObjC project aims to provide a bridge between the Python and Objective-C programming languages.  The bridge is intended to be fully bidirectional, allowing the Objective-C programmer transparent access to Python based functionality and the Python programmer to take full advantage of the power provided by various Objective-C based toolkits.</p>
<p>
Currently, development of the bridge is primarily focused upon the <a href="http://www.apple.com/macosx/">Mac OS X</a> and <a href="http://www.opensource.apple.com/">Darwin</a> platforms.  Within this environment, PyObjC can be used to entirely replace Objective-C in the development of Cocoa based applications and Foundation based command line tools.</p>

<h2><i>For the Python developer:</i>Why use PyObjC?</h2>

<p>
PyObjC offers the python developer full access to the Objective-C APIs available on OS X (and, hopefully someday soon, GnuStep) including Foundation, AppKit, Address Book, Rendezvous, and NetInfo.  The Python developer can also take advantage of any ANSI-C or C++ based API by simply wrapping said API in an Objective-C wrapper and using the PyObjC to access the wrapper.  This is often considerably less work than is required to make the same API available directly via the Python embedding API.
</p>

<h2><i>For the Objective-C developer:</i>Why use PyObjC?</h2>

<p>
PyObjC can be pretty much used anywhere the developer might normally implement something in Objective-C.   This includes everything from a simple subclass of NSObject through to a custom window controller that acts as a NIB file's owner and contains all of the logic for a user interface (including acting as a data source for a table view or combo box).
</p>
<p>
This provides two distinct advantages to the developer.   First, the combination of Python and Cocoa (or for Foundation tools) offers an incredible degree of productivity.   The 'compile' part of the edit-compile-run loop can be nearly eliminated (currently, the 'run' part still exists, but reloading of classes on the fly is in the works).  Also, many common idioms can be expressed in Python with many fewer lines of code than the Objective-C coounterpart.</p>
<p>
Secondly, Objective-C based applications can take advantage of the vast selection of Python modules both included with the <a href="http://www.python.org/">standard python distribution</a> or <a href="http://www.vex.net/parnassus/">by third parties</a>.
</p>

<p>
<a href="index.php">Home</a> -
<a href="download/index.php">Download</a>
</p>


<?
include "footer.inc";
?>
