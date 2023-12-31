install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py

lint:
	pylint --disable=R,C operations.py

test:
	python -m pytest -vv --cov=operations test_operations.py

all: install lint test format