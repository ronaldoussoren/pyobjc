<?
    $title = "GNUstep support in PyObjC";
    $cvs_author = '$Author: ronaldoussoren $';
    $cvs_date = '$Date: 2004/04/12 09:22:46 $';

    include "header.inc";
?>
<div class="document" id="gnustep-support-in-pyobjc">
<h1 class="title">GNUstep support in PyObjC</h1>
<p>PyObjC has limited support for GNUstep, the 'objc' and 'Foundation' packages
build and pass some, but by far not all, unittests. More work is needed to
make the GNUstep port as stable as the MacOS X &quot;port&quot;.</p>
<p>The GNUstep port was primarily developed on Linux i86 (specifically 
the Debian testing distribution), using python 2.3.3,  gcc 3.3.2 and 
gnustep-base1 1.9.0-1. The code in setup.py works for this configuration,
but probably not for other configurations.</p>
<p>GNUstep support is <em>very</em> fragile, in some versions of the the selectors for
new classes should be strings, in others they should be SEL objects (as you
would expect). We also use undocumented private functions to initialize new
classes.</p>
<div class="section" id="todo">
<h1><a name="todo">TODO</a></h1>
<ul>
<li><p class="first">Fix the odd bug...</p>
<p>I currently get the following text when importing objc:</p>
<pre class="literal-block">
Unable to retrieve information about SIGPIPE
</pre>
<p>This text is not printed by PyObjC and I haven't been able to find who
does print that text...</p>
</li>
<li><p class="first">Fix bugs found using the unittests</p>
<p>runPyObjCTests finds some problems that disapear when those tests are run
seperately...</p>
</li>
<li><p class="first">Port the AppKit wrappers</p>
</li>
<li><p class="first">Extract more CFLAGS and LDFLAGS information from the GNUstep build system,
instead of hard-coding the information</p>
</li>
</ul>
</div>
</div>
<?
    include "footer.inc";
?>