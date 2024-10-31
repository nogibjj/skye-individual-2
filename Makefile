install:
	python3 -m venv venv
	venv/bin/pip3 install --upgrade pip &&\
		venv/bin/pip3  install -r requirements.txt

format:
	venv/bin/black mylib/*.py
	rustfmt src/*.rs

lint:
	venv/bin/ruff check mylib/*.py
	cargo clippy

container-lint:
	venv/bin/docker run --rm -i hadolint/hadolint < Dockerfile

python-run :
	venv/bin/python3 main.py

rust-run :
	cargo build
	cargo run

package :
	venv/bin/python3 setup.py sdist
	venv/bin/pip3 install ./dist/chess_transfer-1.0.0.tar.gz

run :
	python-run
	rust-run

gen-readme :
	echo '''# Performance Comparison of Rust and Python Scripts\n This project is designed to compare the runtime and memory usage of Python and Rust implementations of a task. The project includes: \n 1. A Python script (src) for the task.\n 2. A Rust executable (mylib). \n 3. A comparison script (compare.sh) that runs both implementations, measuring and reporting runtime and memory usage.''' > README.md
	#chmod +x ./compare.sh
	./compare.sh "venv/bin/python3 main.py" "python_script"
	./compare.sh "cargo run" "rust_executable"
	cat readme.md.template >> README.md

run-cli :
	venv/bin/python3 main.py extract
	venv/bin/python3 main.py transform
	venv/bin/python3 main.py load
	venv/bin/python3 main.py query

all: install lint format python-run rust-run
