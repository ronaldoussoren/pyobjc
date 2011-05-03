default:
	@echo "Usage:"
	@echo " - build: Create test frameworks"
	@echo " - test:  Build PyObjC and run tests"
	@echo
	@echo "WARNING: 'test' doesn't automaticly 'build'"
	@echo

build:
	python3	build_frameworks.py

test:
	python3 run_tests.py

.PHONY: default build test clean
