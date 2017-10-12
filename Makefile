excludes = \*~ \*.pyc .cache/\* test_\* __pycache__/\*

.PHONY: test
test:
	nosetests --with-cov --cov warrior_buddy

.PHONY: bandit
bandit:
	bandit -r warrior_buddy/
