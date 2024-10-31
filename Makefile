
format:
	cargo fmt

lint:
	cargo clippy

run :
	cargo build
	cargo run

check:
	cargo check

release:
	cargo build --release

all: check build format lint test

test:
	cargo test
