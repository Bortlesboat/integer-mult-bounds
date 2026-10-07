.PHONY: verify note fetch

verify:
	python3 scripts/certify.py
	python3 scripts/search_network.py
	python3 scripts/make_patch.py
	python3 -m unittest discover -s tests -v
	git apply --check --directory=upstream patches/frozen-154.patch
	git apply --check --directory=upstream patches/balanced-153.patch
	git apply --check --directory=upstream patches/same-network-129.patch
	git apply --check --directory=upstream patches/h46-111.patch
	git apply --check --directory=upstream patches/h46-109.patch
	git apply --check --directory=upstream patches/h46-108.patch
	git apply --check --directory=upstream patches/h46-rational.patch

note:
	mkdir -p artifacts
	tectonic --outdir artifacts notes/parameter-note.tex

fetch:
	python3 scripts/fetch_upstream.py
