all: run

clean:
	rm -rf venv && rm -rf *.egg-info && rm -rf dist && rm -rf *.log*

venv:
	#virtualenv --python=python3 venv && venv/bin/python setup.py develop
	virtualenv --python=python3 venv && venv/bin/pip install --editable .

run: venv
	FLASK_APP=fsr_lister FSR_LISTER_SETTINGS=../settings.cfg venv/bin/flask run

test: venv
	FSR_LISTER_SETTINGS=../settings.cfg venv/bin/python -m unittest discover -s tests

sdist: venv test
	venv/bin/python setup.py sdist
