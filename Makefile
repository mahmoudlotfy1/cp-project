run:
	python mainfile.py
test:
	pytest
venv:
	python -m venv venv
	venv\Scripts\activate && pip install -r requirements.txt
install:
	pip install -r requirements.txt
clean:
	del /q *.pyc
	del /q __pycache__\*
