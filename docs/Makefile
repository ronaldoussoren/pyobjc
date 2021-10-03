all:
	@echo "Usage:"
	@echo "  make html          # create html output"
	@echo "  make view          # show html output"
	@echo "  make linkcheck     # check links"

html:
	sphinx-build -b html -d _build/doctrees . _build/html

linkcheck:
	sphinx-build -b linkcheck -d _build/doctrees . _build/linkcheck

view:
	open _build/html/index.html

.PHONY: html view linkcheck
