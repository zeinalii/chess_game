SHELL := /bin/bash

venv: requirements.txt
	python3 -m venv venv && \
	source venv/bin/activate && \
	pip install -r requirements.txt