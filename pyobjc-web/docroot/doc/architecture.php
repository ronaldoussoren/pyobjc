<?
    $title = "PyObjC Architecture";
    $cvs_author = '$Author: ronaldoussoren $';
    $cvs_date = '$Date: 2004/02/02 15:23:01 $';

    include "header.inc";
?>
<table class="docinfo" frame="void" rules="none">
<col class="docinfo-name" />
<col class="docinfo-content" />
<tbody valign="top">
<tr><th class="docinfo-name">Author:</th>
<td>Ronald Oussoren</td></tr>
</tbody>
</table>
<div class="section" id="introduction">
<h1><a name="introduction">Introduction</a></h1>
<p>XXX: This documented is outdated and incomplete.</p>
<p>This document gives a (brief) description of how the PyObjc package is 
structured.</p>
</div>
<div class="section" id="objective-c-classes-and-objects">
<h1><a name="objective-c-classes-and-objects">Objective-C classes and objects</a></h1>
<p>Objective-C classes are represented directly as python classes. This allows
us to implement subclassing of Objective-C classes with the full power that
new-style classes provide.</p>
<p>There is one problem with this though, PyTypeObject does not have space to
store additional information, and is a variable-sized object. This means that
subclasses of PyType_Type cannot add instance variables. We solve this by
storing the additional information in a dictionary indexed by the PyTypeObjects
that represent Objective-C classes.</p>
<p>Objective-C objects are represented by proxy objects that are instances of
the classes descriped above.</p>
<p>TODO: work out how we'll implement subclasses objects and describe here.</p>
</div>
<div class="section" id="methods-and-instance-variables">
<h1><a name="methods-and-instance-variables">Methods and instance variables</a></h1>
<p>Methods and instance variables are represented as 'descriptor' objects that
are attributes of the PyTypeObject describing a class. This way it is possible
to use the normal python introspection mechanisms to explore an objective-C
object/class.</p>
<p>There is also a mechanism to call methods that are not part of the advertised
interface of a class. This is needed to support classes like NSProxy that 
forward method invocations to other objects.</p>
</div>
</div>
<?
    include "footer.inc";
?>