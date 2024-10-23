install:
	python3 -m venv venv
	venv/bin/pip3 install --upgrade pip &&\
		venv/bin/pip3  install -r requirements.txt

format:
	venv/bin/black mylib/*.py

lint:
	venv/bin/ruff check mylib/*.py

container-lint:
	venv/bin/docker run --rm -i hadolint/hadolint < Dockerfile

run :
	venv/bin/python3 main.py

package :
	venv/bin/python3 setup.py sdist
	venv/bin/pip3 install ./dist/chess_transfer-1.0.0.tar.gz

run :
	venv/bin/python3 main.py extract
	venv/bin/python3 main.py transform
	venv/bin/python3 main.py load
	venv/bin/python3 main.py query

all: install lint format package run
