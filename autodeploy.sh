#!/bin/bash
set -ev

if [ ! -z "$TRAVIS_TAG" ]; then
	if [[ "$(python -V)" == *3.5* ]]; then
		python setup.py sdist bdist_wheel
		twine upload dist/*
		echo "Published version $TRAVIS_TAG to PyPi"
	else
		echo "No deployement to PyPi; Only deploying from Python 3.5"
	fi
else
	echo "Not a tag; not going to deploy"
fi
