
format:
	cargo fmt

lint:
	cargo clippy

run :
	cargo build
	cargo run read-latest

check:
	cargo check

release:
	cargo build --release

all: check format lint test

test:
	cargo test
