1) run `docker-compose up -d`
2) after docker starts, set all privilege to folder redis/data,
example ubuntu: `sudo chmod -R a+rwx redis`/
3) then restart celery and redis container, run `docker restart celery redis`
4) open web container `docker exec -it web bash`
5) run migrations in web container `python manage.py migrate`
6) open in browser [http://0.0.0.0:8000](http://0.0.0.0:8000)

**Addition Info**

users api [http://0.0.0.0:8000/api/v1/customers](http://0.0.0.0:8000/api/v1/customers)

filter url example = `http://0.0.0.0:8000/api/v1/customers?registration_date=12/05/2018`

in case celery didn't work, comment celery and redis services in `docker-compose.yml`,
and change function call in directory `core/views/customer.py` in `CustomersUploadCSVFile` view 
line `create_customer.delay(file.read().decode())` to `create_customer(file.read().decode())`