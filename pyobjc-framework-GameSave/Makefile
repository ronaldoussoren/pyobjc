info:
	@echo "c-coverage        - clean & test with C level coverage"

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

dummy:
	rm -rf build
	python setup.py build_ext --inplace

.PHONY: info c-coverage
