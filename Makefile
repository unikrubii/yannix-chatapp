ENV = .env

run:
	@pipenv run python app/manage.py runserver

setup: $(ENV)
	@pip install --upgrade pip
	@pip install pipenv
	@pipenv install -r requirements.txt
	@pipenv run python app/manage.py migrate

test:
	@pipenv run python app/manage.py test chatapp

$(ENV): 
	echo "DB_NAME=postgres\nDB_USER=postgres\nDB_PASSWORD=postgres\
	\nDB_HOST=localhost\nDB_PORT=5432" > .env

.PHONY: run setup test
