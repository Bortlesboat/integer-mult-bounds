.PHONY: verify note audit-note fetch

verify:
	python3 scripts/certify.py
	python3 scripts/search_network.py
	python3 scripts/make_patch.py
	python3 scripts/nonadjacent.py
	python3 scripts/make_nonadjacent_patch.py
	python3 -m unittest discover -s tests -v
	git apply --check --directory=upstream patches/frozen-154.patch
	git apply --check --directory=upstream patches/balanced-153.patch
	git apply --check --directory=upstream patches/same-network-129.patch
	git apply --check --directory=upstream patches/h46-111.patch
	git apply --check --directory=upstream patches/h46-109.patch
	git apply --check --directory=upstream patches/h46-108.patch
	git apply --check --directory=upstream patches/h46-rational.patch
	git apply --check --directory=upstream patches/nonadjacent-layout.patch
	git apply --check --directory=upstream patches/frozen-nonadjacent-107.patch
	git apply --check --directory=upstream patches/h46-nonadjacent-78.patch

note:
	mkdir -p artifacts
	tectonic --outdir artifacts notes/parameter-note.tex

audit-note:
	mkdir -p artifacts
	tectonic --outdir artifacts notes/nonadjacent-axis-note.tex

fetch:
	python3 scripts/fetch_upstream.py
