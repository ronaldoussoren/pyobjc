
all: update-shared extension-format python-format

update-shared:
	development-support/update-shared-files

extension-format:
	clang-format -i --style=file --assume-filename='foo.m' $(shell find */Modules -name '*.[chm]')

python-format:
	ruff format

.PHONY: all extension-format python-format update-shared
