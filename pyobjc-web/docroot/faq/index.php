<?
$title = "F.A.Q.";
$cvs_author = '$Author: ronaldoussoren $';
$cvs_date = '$Date: 2003/03/15 15:38:05 $';

include "header.inc";
?>

<i>A FAQ would be nice, too.  There has to be a way to automatically generate this based on some more usefully structured text/data.  <b>Links at left are broken pending something useful.</b></i>

<DL>
<DT><B>I use an <code>NSTableView</code> and my program crashes, what's up?</B></DT>
<DT>
Your table model should be a subclass of another ObjC class, <B>and</B> of 
<code>AppKit.NSTableDataSource</code>. This is necessary to enable the bridge
to deduce the correct method signatures for your methods.
<P>The same is true of other data-models and informal protocols: You must 
multiple-inherit from NSObject (or a subclass of that class) and the 
corresponding protocol pseudo-class.
</DT>
</DL>
<?
include "footer.inc";
?>

