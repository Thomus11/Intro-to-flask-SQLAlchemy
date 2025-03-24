
#!/usr/bin/env python3

from app import app
from models import db, House, Manager, Tenant

with app.app_context():

    Tenant.query.delete()
    Manager.query.delete()
    House.query.delete()

    house1 = House(name="Sunny Apartments", location="Uptown")
    house2 = House(name="Riverside Villas", location="Downtown")
    house3 = House(name="Mountain View Homes", location="Suburbia")
    db.session.add_all([house1, house2, house3])
    db.session.commit()

    manager1 = Manager(name="Alice Johnson", salary=60000, house=house1)
    manager2 = Manager(name="Bob Williams", salary=75000, house=house2)
    manager3 = Manager(name="Charlie Brown", salary=55000, house=house3)
    db.session.add_all([manager1, manager2, manager3])
    db.session.commit()

    tenant1 = Tenant(name="David Lee", rent=1200, house=house1)
    tenant2 = Tenant(name="Eve Davis", rent=1500, house=house1)
    tenant3 = Tenant(name="Frank Miller", rent=1800, house=house2)
    tenant4 = Tenant(name="Grace Wilson", rent=2000, house=house2)
    tenant5 = Tenant(name="Henry Moore", rent=1300, house=house3)
    db.session.add_all([tenant1, tenant2, tenant3, tenant4, tenant5])
    db.session.commit()
