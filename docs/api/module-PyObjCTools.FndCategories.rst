====================================================
API Description for :mod:`PyObjCTools.FndCategories`
====================================================

.. module:: PyObjCTools.FndCategories
   :synopsis: Useful categories on classes from Foundation


Introduction
------------

The module :mod:`PyObjCTools.FndCategories` defines a number of categories on
classes from the :mod:`Foundation` framework. These categories introduce
new methods that aren't present in that framework.

To use these new methods use the following code somewhere in your program:

.. sourcecode:: python

   import PyObjCTools.FndCategories


Additional methods on :class:`NSAffineTransform <Foundation.NSAffineTransform>`
-------------------------------------------------

.. class:: Foundation.NSAffineTransform

   .. method:: rotateByDegrees_atPoint_(angle, point)

      This is similar to :meth:`rotateByDegrees_ <Foundation.NSAffineTransform.rotateByDegrees_>` but rotates around *point* instead
      of the origin.

      :param float angle: Angle the transform should be rotated by.
      :param CGPoint point: Point the transform should be rotated around.

   .. method:: rotateByRadians_atPoint_(angle, point)

      This is similar to :meth:`rotateByRadians_ <Foundation.NSAffineTransform.rotateByRadians_>` but rotates around *point* instead
      of the origin.

      :param float angle: Angle the transform should be rotated by.
      :param CGPoint point: Point the transform should be rotated around.
