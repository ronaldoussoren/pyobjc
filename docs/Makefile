all:
	@echo "Usage:"
	@echo "  make html          # create html output"
	@echo "  make view          # show html output"
	@echo "  make linkcheck     # check links"

html: _build/venv
	_build/venv/bin/sphinx-build -b html -d _build/doctrees . _build/html

linkcheck: _build/venv
	_build/venv/bin/sphinx-build -b linkcheck -d _build/doctrees . _build/linkcheck

view:
	open _build/html/index.html

_build/venv: requirements.txt
	mkdir -p _build
	rm -rf _build/venv
	python3.11 -m venv _build/venv
	_build/venv/bin/python -m pip install -r requirements.txt

.PHONY: html view linkcheck
