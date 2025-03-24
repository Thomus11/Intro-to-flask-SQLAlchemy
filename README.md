## Setup

Fork and clone the lab repo.

Run `pipenv install` and `pipenv shell` .

```console
$ pipenv install
$ pipenv shell
```

Change into the `server` directory:

```console
$ cd server
```

pipenv install flask flask-migrate flask-sqlalchemy Werkzeug Faker

 flask db init
 flask db migrate -m "initial migration"
 flask db upgrade head
 python seed.py

 flask shell

>>> from models import House, Manager, Tenant

>>> houses = House.query.all()
>>> managers = Manager.query.all()
>>> tenants = Tenant.query.all()

>>> for house in houses:
...     print(house.address)
...
>>> for manager in managers:
...     print(manager.name)
...
>>> for tenant in tenants:
...     print(tenant.name)
...


Get All Houses (/houses):

Go to http://127.0.0.1:5555/houses.

Get All Managers (/managers):

Go to http://127.0.0.1:5555/managers.

Get All Tenants (/tenants):

Go to http://127.0.0.1:5555/tenants.

Get All House Managers (/house_managers):

http://127.0.0.1:5555/houses/<house_id>/managers

Get All House Tenants (/house_tenants):

http://127.0.0.1:5555/houses/<house_id>/tenants
