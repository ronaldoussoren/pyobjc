all:
	@echo "Usage:"
	@echo "  make html     # create html output"
	@echo "  make view     # show html output"

html:
	sphinx-build -b html -d _build/doctrees . _build/html

view:
	open _build/html/index.html

.PHONY: html view
