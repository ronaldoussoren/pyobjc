#!/bin/sh

set -o pipefail

echo "Misusage of LCOV_BR_EXCL_LINE:"
grep -n LCOV_BR_EXCL_LINE */Modules/objc/*.[hm] | grep -v -e 'if (' -e 'while (' -e '} else {' -e ': always non-empty' -e 'switch ('
xit1=$?
echo

echo "Misusage of LCOV_EXCL_LINE:"
grep -n LCOV_EXCL_LINE */Modules/objc/*.[hm] | grep -e 'if (' -e 'while (' -e '} else {' -e ': always non-empty' -e 'switch ('
xit2=$?
echo

exit $(expr 2 - $xit1 - $xit2)
