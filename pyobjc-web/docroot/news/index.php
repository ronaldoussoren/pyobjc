<?
$title = "News";
$cvs_author = 'Author: dmrrsn';
$cvs_date = 'Date: 2002/11/05 19:15:25';

$metatags = '';

include "header.inc";
?>
<span class="news_date">2002-11-12: </span><span class="news_headline">Initial release of web site</span><?php gray_line(); ?>
  <p>
For the first time ever, the PyObjC module has a real web site (the start of one anyway).  The implementation is largely a copy of the <a href="http://fink.sourceforge.net/">Fink project's excellent site.</a>.  The design and graphics were contributed by <a href="http://starship.python.net/crew/jwt/">Jim Tittsler</a>.  The content was compiled from many sources-- Jim's work, Fink, the PyObjC source trees and some original-- by <a href="http://radio.weblogs.com/0100490/">Bill Bumgarner</a>.
</p>
<span class="news_date">2002-10-13: </span><span class="news_headline">Interim release 0.7.0</span><?php gray_line(); ?>
  <p> On or about this date, an interim release of PyObjC was made available as a disk image that contained the binary module (compatible with Apple's build of Python included with OS X 10.2), a Project Builder project template for building Cocoa applications using Python, and a basic README.</p>
  <p>Version 0.7.0 represents a huge step forward over the previous version (0.6.1).  Of note, 0.7.0 vastly improved the inter-language messaging mechanism, the bridging of various classes, improved support for features specific to the Foundation and AppKit, support for the Address Book framework, and subclassing of Objective-C classes in Python.</p>
<span class="news_date">2002-01-30: </span><span class="news_headline">Release 0.6.1</span><?php gray_line(); ?>
<p>
Last release made that used a single dynamically loadable module named 'pyobjc'.
</p>
<?
include "footer.inc";
?>

