start_project:
	python manage.py migrate
	python manage.py runserver 0.0.0.0:8000

test:
	docker exec -it parking-api python manage.py test

create_super_user:
	docker exec -it parking-api python manage.py createsuperuser