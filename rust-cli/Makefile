
format:
	cargo fmt

lint:
	cargo clippy

run :
	cargo build
	cargo run -- extract
	cargo run -- load
	cargo run create --url "google.com" --player-id 123 --federation "USA" --former-fed "THA" --transfer-date "2004-02-01"
	cargo run read-latest
	cargo run update --id 1 --new-url "example.com"
	cargo run delete --id 1

check:
	cargo check

release:
	cargo build --release

all: check format lint test

test:
	cargo test
