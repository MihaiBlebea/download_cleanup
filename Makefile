venv-create:
	python3 -m venv virtualenv

venv-activate:
	source virtualenv/bin/activate

venv-deps:
	pip3 freeze > requirements.txt

venv-install:
	pip3 install -r requirements.txt