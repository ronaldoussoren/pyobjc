#!/bin/sh

echo "Misusage of LCOV_BR_EXCL_LINE:"
grep LCOV_BR_EXCL_LINE Modules/objc/*.[hm] | grep -v -e 'if (' -e 'while (' -e '} else {' -e ': always non-empty' -e 'switch ('
echo

echo "Misusage of LCOV_EXCL_LINE:"
grep LCOV_EXCL_LINE Modules/objc/*.[hm] | grep -e 'if (' -e 'while (' -e '} else {' -e ': always non-empty' -e 'switch ('
echo
