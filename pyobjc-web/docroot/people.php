<?
$title = "Contributors";
$cvs_author = '$Author: ronaldoussoren $';
$cvs_date = '$Date: 2002/11/13 15:24:22 $';

include "header.inc";
?>
<p><b>Contributors:</b></p>
<p>
Many, many people have contributed to the PyObjC module in the recent months.  The mailing list should be parsed to complete this list.
<ul>
<li>Jack Jansen has provided constant technical assistance and direction based on his wealth of experience as the primary developer of the MacPython project.</li>
<li>Jim Tittsler provided a significant chunk of the look/feel of this web site, including the cool PyDog graphic.</li>
<li>The <a href="http://fink.sourceforge.net/">Fink Project</a> deserves a huge amount of credit.  Beyond providing a model for building this site, Fink represents an incredible base of knowledge to anyone working with various open source tools and OS X.
</ul>
</p>
<p><b>History:</b></p>
<p>Ronald Oussoren &lt;oussoren@cistron.nl&gt; rewrote most of the module in 2002.  Ronald made it possible to subclass Objective-C classes from Python and added nearly complete support for the Foundation, the AppKit and the AddressBook frameworks.</p>
<p></p>
<p>In the fall of 2002, Bill Bumgarner &lt;bbum@codefab.com&gt; added support for non-Framework builds of python.  Ronald and Bill subsequently added support for the Apple supplied build of Python.   Bill created the Project Builder template that allows for building standalone Cocoa applications that are implemented in Project Builder.</p>
<p></p>
<p>Steve Majewski &lt;sdm7g@minsky.med.virginia.edu&gt; and Bill Bumgarner &lt;bbum@codefab.com&gt; picked up Lele's work in early November, 2000. Steve significanlty improved compatibility with OS X.</p>
<p></p>
<p>
History prior to 2000 is a bit fuzzy.  Jeff Sickel contributed numerous patches and features over the years.
</p>
<p>Lele Gaifax built the original module which dates back to September 1996.  Lele's original list of contributors/motivators was as follows:</p>
<p></p>
<i><p>I should say "Grazie" to many persons that made this possible, but to some in particular:</p>
<p></p>
<p>Guido van Rossum <guido@CNRI.Reston.VA.US>:</p>
<p>  Long list of motivation omitted ;-)</p>
<p></p>
<p>Thomas Breuel <tmb@best.com>:</p>
<p>  He first inspired me with good ideas.</p>
<p></p>
<p>Ted Horst <ted_horst@il.us.swissbank.com>:</p>
<p>  His own ObjC module and kind comments helped me a lot.</p>
<p></p>
<p>Bill Bumgarner <bbum@friday.com>:</p>
<p>        He contribuited the standalone packaging setup, good comments and his own implementation of the Streams and Pasteboards support. He  maintained also several Python-related packages for NeXTSTEP: see <ftp://ftp.thoughtport.net/pub/next/lang> [long gone;  see http://www.friday.com/software/python/]</p>
<p></p>
<p>...and of course to the entire ObjC-SIG community.</p></i>
<p>
<a href="mailto:bbum@codefab.com">My (bbum's) memory</a> is far from perfect.  Please feel free to send corrections and updates to this list!  In particular, I believe that the objc module was shipped with the core python distribution at one point, but I can't find any information about that.
</p>
<p><?
include "footer.inc";
?>
