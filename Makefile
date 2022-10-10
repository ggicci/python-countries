default: build

.PHONY: build
build:
	pdm build

.PHONY: build/verbose
build/verbose:
	pdm build -v

.PHONY: test
test:
	pytest -v

.PHONY: test/coverage
test/coverage:
	pytest --cov --cov-report html && firefox htmlcov/index.html &>/dev/null
