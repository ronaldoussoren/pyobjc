#!/bin/sh

set +e

for proj in  \
	altgraph \
	macholib \
	modulegraph \
	py2app \
	pyobjc-core \
	pyobjc-metadata \
	pyobjc-framework-Cocoa
do (
	echo $proj
	cd ${proj}
	rm -rf build
	python2.5 setup.py test
	python2.5 setup.py develop
); done

exit 0

(
   cd PyOpenGL-2.0.2.01
   /usr/bin/python2.5 setup.py install
)

for proj in `ls | grep ^pyobjc-framework`
do (
	echo $proj
	case ${proj} in 
	pyobjc-framework-Cocoa) : ;;
	*)
		cd ${proj}
		rm -rf build
		python2.5 setup.py test
		python2.5 setup.py develop
		;;
	esac
); done
