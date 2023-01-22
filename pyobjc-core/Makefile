info:
	@echo "all               - build and develop"
	@echo "test              - build, develop and test"
	@echo "sanitize-test     - clean & test with sanitizers"
	@echo "scan-build        - build with clang static analyzer"
	@echo "c-coverage        - clean & test with C level coverage"
	@echo "clean             - remove build and dist"

all:
	python3 setup.py build_ext develop

test:
	python3 setup.py build_ext develop test -v

# Build and test using various sanitizers.
#
# This needs a complicated way of starting to ensure that the
# sanitizer library is loaded.
sanitize-test:
	rm -rf build dist
	env ASAN_OPTIONS=allocator_may_return_null=1 DYLD_INSERT_LIBRARIES=$(shell echo `xcode-select -p`/Toolchains/XcodeDefault.xctoolchain/usr/lib/clang/*/lib/darwin/libclang_rt.asan_osx_dynamic.dylib) CFLAGS="-fsanitize=address -fsanitize=undefined -fno-sanitize=vptr" $(shell python -c 'import sys; print(sys.base_prefix if hasattr(sys, "base_prefix") else sys.prefix)')/Resources/Python.app/Contents/MacOS/Python setup.py build_ext develop test -v

clean:
	rm -rf build dist

# Run a build with clang's static analyzer.
scan-build:
	test -d build || mkdir build
	env CFLAGS="-DPyObjC_DEBUG -DUSE_STATIC_ANALYZER" scan-build -o build   \
            --enable-checker nullability.NullableDereferenced \
            --enable-checker nullability.NullablePassedToNonnull \
            --enable-checker nullability.NullableReturnedFromNonnull \
            --enable-checker security.insecureAPI.DeprecatedOrUnsafeBufferHandling \
            --enable-checker security.insecureAPI.bcmp \
            --enable-checker security.insecureAPI.bcopy \
            --enable-checker security.insecureAPI.bzero \
	    python3 setup.py build_ext -j 4
	open build/scan-build*/index.html

# Run the test suite while recording Python-level coverage
coverage:
	rm -rf build dist
	mkdir build dist
	python3 -mvenv build/cov-env
	build/cov-env/bin/python3 -mpip install -U wheel pip setuptools coverage
	build/cov-env/bin/python3 setup.py develop
	-build/cov-env/bin/python3 -mcoverage run --branch setup.py test -v
	build/cov-env/bin/python3 -mcoverage html --omit='PyObjCTest/*,setup.py'
	open htmlcov/index.html

# Run the test suite while recording C-level coverage
c-coverage:
	rm -rf build dist
	mkdir build dist
	python3 -mvenv build/cov-env
	env ARCHFLAGS="-arch arm64" CFLAGS="-DCOVERAGE --coverage -fprofile-arcs -ftest-coverage -O1" LDFLAGS="--coverage -fprofile-arcs -ftest-coverage -O1" build/cov-env/bin/python3 setup.py build_ext -j 4 develop
	lcov --directory .  --zerocounters
	-build/cov-env/bin/python3 setup.py test -v
	lcov --rc lcov_branch_coverage=1 --rc "lcov_excl_br_line=LCOV_BR_EXCL_LINE|Py_VISIT|Py_CLEAR|NEW_EXC|NEW_STR|PyObjC_Assert"  --no-external --capture --directory . --output-file build/coverage.info
	genhtml --legend --branch-coverage --rc "lcov_excl_br_line=LCOV_BR_EXCL_LINE|Py_VISIT|Py_CLEAR|NEW_EXC|NEW_STR|PyObjC_Assert" --legend build/coverage.info --output-directory dist/c-coverage # --rc "genhtml_med_limit=80" --rc "genhtml_hi_limit=95"
	open dist/c-coverage/index.html


# XXX: Maybe use this to run the tests to test both architectures, should lead to better coverage info:
#-arch -arm64 build/cov-env/bin/python3 setup.py test -v
#-arch -x86_64 build/cov-env/bin/python3 setup.py test -v


.PHONY: info all test sanitize-test clean scan-build c-coverage
