<?
/* $Id: footer.inc,v 1.3 2004/02/02 15:23:01 ronaldoussoren Exp $ */
?>

</td></tr>

<? /* end content table */ ?>
</table>
</td></tr>



<? /* horizontal stripe */ ?>
<tr><td class="layout" height="3" style="background-image:url(<? print $root ?>img/top-line2.gif)">
</td></tr>

<? /* copyright-and-footer row of top-level table */ ?>
<tr valign="middle" align="left">
<td bgcolor="#eeeeee" align="center" width="120"
    style="background-image:url(<? print $root ?>img/stripes.gif)">
  <a href="<? print $root ?>legal.php" style="text-decoration:none;color:black;font-size:10pt;">
    Copyright&nbsp;&copy;&nbsp;2003, 2004 The&nbsp;PyObjC&nbsp;Project
  </a>
</td>
<td class="layout">

<? /* footer table */ ?>
<table border="0" cellpadding="0" cellspacing="0" width="100%">
<tr><td>&nbsp;</td></tr>
<tr><td width="100%">
<div class="footer" align="center"><?
if ($dyndate == 1) {
  print "Generated dynamically";
  $date = 0;
} elseif ($dyndate) {
  print "Database last updated on ";
  $date = $dyndate;
} else {
  print 'Last changed by <a href="mailto:'.$author.'ATusersDOTsourceforgeDOTnet">'.$author.'</a> on ';
}
if ($date)
  print gmstrftime("%a, %b %d %Y, %R GMT", $date);
?></div>
</td></tr>
<tr><td height="7" class="layout">
 <img src="<? print $root ?>img/shim.gif" width="1" height="7" border="0" alt="">
</td></tr>
</table>

</td>
</tr>

<? /* horizontal stripe */ ?>
<tr><td class="layout" colspan="2" height="3" style="background-image:url(<? print $root ?>img/top-line2.gif)">
</td></tr>

</table>


</body>
</html>
