# Makefile for automation
venv:
	python -m venv venv
	venv\Scripts\activate && pip install -r requirements.txt

# Run the tests using pytest
test:
	venv\Scripts\activate && pytest

# Install dependencies
install:
	venv\Scripts\activate && pip install -r requirements.txt

# Run main script
run:
	venv\Scripts\activate && python main.py

# Clean up __pycache__ and .pytest_cache
clean:
	del /s /q __pycache__ .pytest_cache