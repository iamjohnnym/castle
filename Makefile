excludes = \*~ \*.pyc .cache/\* test_\* __pycache__/\*

.PHONY: test
test:
	nosetests --with-cov --cov castle

.PHONY: bandit
bandit:
	bandit -r castle/
