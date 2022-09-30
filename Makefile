# simple makefile to run common commands

SRC_DIR:=./
VENV_BIN_DIR:="venv/bin"

VIRTUALENV:=$(shell which virtualenv)

REQUIREMENTS_DIR:=./
REQUIREMENTS_LOCAL:="$(REQUIREMENTS_DIR)requirements.txt"

PIP:="$(VENV_BIN_DIR)/pip"
FLAKE8:="$(VENV_BIN_DIR)/flake8"
#ISORT:="$(VENV_BIN_DIR)/isort"

CMD_FROM_VENV:=". $(VENV_BIN_DIR)/activate; which"
PYTHON="python"

hello:
	$(info $$var is [${PYTHON}])
	$(info $$var is [${REQUIREMENTS_LOCAL}])
	$(info $$var is [${VENV_BIN_DIR}])
	$(info $$var is [${SRC_DIR}])
	@echo "Hello, World!"

# DEVELOPMENT

define create-venv
virtualenv venv -p python3
endef

venv:
	@$(create-venv)
	@$(PIP) install -r $(REQUIREMENTS_LOCAL)

check: venv
	@$(FLAKE8)

# TESTING
test: venv
	@coverage run manage.py test
	@coverage html
#fix: venv
#	@$(ISORT) -rc src

#clean:
#	@rm -rf .cache
#	@rm -rf htmlcov coverage.xml .coverage
#	@find . -name *.pyc -delete
#	@find . -name db.sqlite3 -delete
#	@find . -type d -name __pycache__ -delete
#	@rm -rf venv
#	@rm -rf .tox

# TOOLS/SCRIPTS, Activate venv to run
makemigrations: venv
	@$(PYTHON) $(SRC_DIR)manage.py makemigrations

migrate: venv
	@$(PYTHON) $(SRC_DIR)manage.py migrate

superuser: venv
	@$(PYTHON) $(SRC_DIR)manage.py createsuperuser

# LOCAL

runlocal: venv
	@$(PYTHON) $(SRC_DIR)manage.py runserver
