all: build test install

build:
	python setup.py build

install: build
	python setup.py develop

test: pep8 pyflakes

# requires "pip install pep8"
pep8:
	@git ls-files | grep \\.py$ | xargs pep8

# requires "pip install pyflakes"
pyflakes:
	@export PYFLAKES_NODOCTEST=1 && \
		git ls-files | grep \\.py$ | xargs pyflakes

upload:
	python setup.py sdist bdist_wheel upload
