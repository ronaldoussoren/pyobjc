"import Quartz" or "import CoreGraphics"
========================================

There are currently two sets of bindings for the CoreGraphics API
of macOS

* "import CoreGraphics"

  Apple ships a module named CoreGraphics that provides bindings
  for a large subset of the CoreGraphics API. These bindings provide
  a fairly Object-Oriented API, but are only available when you
  use Apple distribution of Python ("/usr/bin/python")

* "import Quartz"

  PyObjC also provides bindings to the CoreGraphics frameworks, and does
  this through the "Quartz" package. This binds almost all of CoreGraphics
  (and the rest of Quartz), but does only provide a classic function-based
  API.

  The PyObjC bindings are available for all Python versions and macOS
  releases supported by PyObjC.
