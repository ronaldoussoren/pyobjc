<?
    $title = "GNUstep support in PyObjC";
    $cvs_author = '$Author: ronaldoussoren $';
    $cvs_date = '$Date: 2004/02/02 15:23:01 $';

    include "header.inc";
?>
<div class="document" id="gnustep-support-in-pyobjc">
<h1 class="title">GNUstep support in PyObjC</h1>
<p>PyObjC has limited support for GNUstep, the 'objc' and 'Foundation' packages
build and pass some, but by far not all, unittests. More work is needed to
make the GNUstep port as stable as the MacOS X &quot;port&quot;.</p>
<p>The GNUstep port was primarily developed on Linux i86 (specifically 
the Debian testing distribution), using python 2.3.2,  gcc 3.3.2 and 
gnustep-base 1.7.3-1. The code in setup.py works for this configuration,
but probably not for other configurations.</p>
<div class="section" id="todo">
<h1><a name="todo">TODO</a></h1>
<ul class="simple">
<li>Fix bugs found using the unittests</li>
<li>Port the AppKit wrappers</li>
<li>Extract more CFLAGS and LDFLAGS information from the GNUstep build system,
instead of hard-coding the information</li>
</ul>
</div>
</div>
<?
    include "footer.inc";
?>