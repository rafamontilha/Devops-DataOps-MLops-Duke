.PHONY: install test format lint run all

install:
	pip install --upgrade pip
	pip install -r requirements.txt

test:
	python -m pytest -vv --cov=app --cov-report=term-missing

format:
	black *.py

lint:
	pylint --disable=R,C *.py

run:
	python app.py

all: install lint format test
