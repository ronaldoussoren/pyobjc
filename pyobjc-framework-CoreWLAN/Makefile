info:
	@echo "c-coverage        - clean & test with C level coverage"
	@echo "scan-build        - build with clang's static analyzer"

# Run the test suite while recording C-level coverage
c-coverage:
	rm -rf build
	mkdir -p build dist
	python -m pip install -U coverage
	env ARCHFLAGS="-arch arm64" CFLAGS="-DCOVERAGE --coverage -fprofile-arcs -ftest-coverage -O1" LDFLAGS="--coverage -fprofile-arcs -ftest-coverage -O1" python setup.py build_ext -j 4 --inplace
	lcov --directory .  --zerocounters
	-env PYOBJC_INTERACTIVE_TESTS=1 python -m coverage run --branch setup.py test -v
	if test -d Modules ;then lcov --rc lcov_branch_coverage=1 --rc "lcov_excl_br_line=LCOV_BR_EXCL_LINE|Py_VISIT|Py_CLEAR|NEW_EXC|NEW_STR|PyObjC_Assert|assert|PyObjC_END_WITH_GIL|PyObjCMethodSignature_Validate|PyMutex_Lock|PyMutex_Unlock|PyObjCErr_FromObjC|^[ ]*}\$$|^[ ]*} else \{\$$"  --rc "lcov_excl_line=LCOV_EXCL_LINE|^[ ]*} else \{\$$" --no-external --capture --directory . --output-file build/coverage.info; fi
	if test -d Modules; then genhtml --legend --branch-coverage --rc "lcov_excl_br_line=LCOV_BR_EXCL_LINE|Py_VISIT|Py_CLEAR|NEW_EXC|NEW_STR|PyObjC_Assert|assert|PyObjC_END_WITH_GIL|PyObjCMethodSignature_Validate|PyMutex_Lock|PyMutex_Unlock|PyObjCErr_FromObjC|^[ ]*}\$$|^[ ]*} else \{\$$" --rc "lcov_excl_line=LCOV_EXCL_LINE|^[ ]*} else {\$$" --legend build/coverage.info --output-directory dist/c-coverage; fi
	python -mcoverage html --omit='PyObjCTest/*,setup.py,pyobjc_setup.py,Lib/**/_metadata.py'
	python -mcoverage report --omit='PyObjCTest/*,setup.py,pyobjc_setup.py,Lib/**/_metadata.py' | grep -v `dirname $(PWD)`
	if test -d Modules; then open htmlcov/index.html dist/c-coverage/Modules/index-sort-l.html; else open htmlcov/index.html; fi

scan-build:
	test -d build || mkdir build
	env CFLAGS="-DPyObjC_DEBUG -DUSE_STATIC_ANALYZER -UNDEBUG -O2" scan-build -o build   \
	    --enable-checker nullability.NullPassedToNonnull \
	    --enable-checker nullability.NullReturnedFromNonnull \
	    --enable-checker nullability.NullableDereferenced \
	    --enable-checker nullability.NullablePassedToNonnull \
	    --enable-checker nullability.NullableReturnedFromNonnull \
	    --enable-checker security.insecureAPI.DeprecatedOrUnsafeBufferHandling \
	    --enable-checker security.insecureAPI.bcmp \
	    --enable-checker security.insecureAPI.bcopy \
	    --enable-checker security.insecureAPI.bzero \
	    --enable-checker security.insecureAPI.rand \
	    --enable-checker security.insecureAPI.strcpy \
	    --enable-checker optin.portability.UnixAPI \
	    --enable-checker valist.CopyToSelf \
	    --enable-checker valist.Uninitialized \
	    --enable-checker valist.Unterminated \
	    --enable-checker security \
	    python3 setup.py build_ext
	open build/scan-build*/index.html

.PHONY: info c-coverage
