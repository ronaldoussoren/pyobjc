.. module:: SensitiveContentAnalysis
   :platform: macOS 14+
   :synopsis: Bindings for the SensitiveContentAnalysis framework

API Notes: SensitiveContentAnalysis framework
=============================================

Apple documentation
-------------------

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/sensitivecontentanalysis?language=objc

These bindings are accessed through the ``SensitiveContentAnalysis`` package (that is, ``import SensitiveContentAnalysis``).

.. macosadded:: 14

API Notes
---------

* Using this framework requires the app to have the `com.apple.developer.sensitivecontentanalysis.client <https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.sensitivecontentanalysis.client?language=objc>`_ entitlement.
