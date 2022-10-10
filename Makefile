default: build

.PHONY: build
build:
	pdm build

test:
	pytest -v

test/coverage:
	pytest --cov --cov-report html && firefox htmlcov/index.html &>/dev/null
