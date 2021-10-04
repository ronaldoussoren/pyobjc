info:
	@echo "all               - build and develop"
	@echo "test              - build, develop and test"
	@echo "sanitize-test     - clean & test with sanitizers"
	@echo "clean             - remove build and dist"

all:
	python3 setup.py build_ext develop

test:
	python3 setup.py build_ext develop test --verbosity=3

# The complicated way of starting Python is needed to ensure the
# sanitizer library is actually loaded
# XXX: Calc DYLD_INSERT_LIBRARIES dynamicly as well
sanitize-test:
	rm -rf build dist
	env DYLD_INSERT_LIBRARIES=/Users/ronald/Applications/Xcode-beta.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/clang/13.0.0/lib/darwin/libclang_rt.asan_osx_dynamic.dylib CFLAGS="-fsanitize=address -fsanitize=undefined -fno-sanitize=vptr" $(shell python -c 'import sys; print(sys.base_prefix if hasattr(sys, "base_prefix") else sys.prefix)')/Resources/Python.app/Contents/MacOS/Python setup.py build_ext develop test --verbosity=3

clean:
	rm -rf build dist

.PHONY: info all test sanitize-test clean
