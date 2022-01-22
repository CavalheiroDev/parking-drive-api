start_project:
	python manage.py migrate
	python manage.py runserver

test:
	python manage.py test

create_super_user:
	docker exec -it parking-api python manage.py createsuperuser