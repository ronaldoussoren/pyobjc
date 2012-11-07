====================================================
API Description for :mod:`PyObjCTools.FndCategories`
====================================================

.. module:: PyObjCTools.FndCategories
   :synopsis: Useful categories on classes from Foundation


Introduction
------------

The module :mod:`PyObjCTools.FndCategories` defines a number of categories on
classes from the *Foundation* framework. These categories introduce
new methods that aren't present in that framework.

To use these new methods use the following code somewhere in your program::

  .. sourcecode:: python

       import PyObjCTools.FndCategories


Additional methods on :class:`NSAffineTransform`
-------------------------------------------------

.. class:: NSAffineTransform

   .. method:: rotateByDegrees_atPoint_(angle, point)

      This is simular to ``rotateByDegrees_`` but rotates around ``point`` instead
      of the origin.

   .. method:: rotateByRadians_atPoint_(angle, point)

      This is simular to ``rotateByRadians_`` but rotates around ``point`` instead
      of the origin.
