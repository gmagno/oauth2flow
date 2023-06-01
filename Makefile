
SHELL := /bin/bash


.PHONY: run
run:
	lt --local-host 127.0.0.1 --port 9000 --subdomain oauth2flow &
	python -m oauth2flow.main

.PHONY: clean
clean:
	find . \( -name __pycache__ -o -name "*.pyc" -o -name .pytest_cache -o -name .mypy_cache \) -exec rm -rf {} +
