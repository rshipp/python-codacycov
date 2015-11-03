all: build test install

build:
	python setup.py build

install: build
	python setup.py develop

test: pep8 pyflakes
	python setup.py test

coverage:
	rm coverage.xml || true
	coverage run --source src/codacy/ setup.py test
	coverage xml
	python-codacy-coverage -r coverage.xml

# requires "pip install pep8"
pep8:
	@git ls-files | grep \\.py$ | xargs pep8

# requires "pip install pyflakes"
pyflakes:
	@export PYFLAKES_NODOCTEST=1 && \
		git ls-files | grep \\.py$ | xargs pyflakes

upload:
	python setup.py sdist bdist_wheel upload
