test:
	pytest -v

test/coverage:
	pytest --cov --cov-report html && open htmlcov/index.html