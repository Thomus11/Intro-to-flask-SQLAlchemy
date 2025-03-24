from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

# Metadata for database naming conventions
metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
)

# SQLAlchemy instance for database interactions
db = SQLAlchemy(metadata=metadata)

# House model representing a house or apartment building
class House(db.Model, SerializerMixin):
    __tablename__ = "houses"

    id = Column(Integer, primary_key=True)  # Unique identifier for each house
    name = Column(String)  # Name of the house/building
    location = Column(String)  # Location of the house/building

    # Serialization rules to avoid circular references
    serialize_rules = ("-managers.house", "-tenants.house")

    # Relationship with Manager model (one-to-many)
    # A house can have multiple managers
    managers = relationship("Manager", back_populates="house")

    # Relationship with Tenant model (one-to-many)
    # A house can have multiple tenants
    tenants = relationship("Tenant", back_populates="house")

    def __repr__(self):
        return f"<House {self.id}, {self.name}, {self.location}>"

# Manager model representing a manager of a house
class Manager(db.Model, SerializerMixin):
    __tablename__ = "managers"

    id = Column(Integer, primary_key=True)  # Unique identifier for each manager
    name = Column(String)  # Name of the manager
    salary = Column(Float)  # Salary of the manager

    # Serialization rule to avoid circular reference
    serialize_rules = ("-house.managers",)

    # Foreign key referencing the house's id
    house_id = Column(Integer, ForeignKey("houses.id"))

    # Relationship with House model (many-to-one)
    # A manager belongs to one house
    house = relationship("House", back_populates="managers")

    def __repr__(self):
        return f"<Manager {self.id}, {self.name}, {self.salary}>"

# Tenant model representing a tenant living in a house
class Tenant(db.Model, SerializerMixin):
    __tablename__ = "tenants"

    id = Column(Integer, primary_key=True)  # Unique identifier for each tenant
    name = Column(String)  # Name of the tenant
    rent = Column(Float)  # Rent paid by the tenant

    # Serialization rule to avoid circular reference
    serialize_rules = ("-house.tenants",)

    # Foreign key referencing the house's id
    house_id = Column(Integer, ForeignKey("houses.id"))

    # Relationship with House model (many-to-one)
    # A tenant belongs to one house
    house = relationship("House", back_populates="tenants")

    def __repr__(self):
        return f"<Tenant {self.id}, {self.name}, {self.rent}>"

# Detailed Explanation:

# 1. Database Setup:
#    - `metadata = MetaData(...)`: Configures naming conventions for foreign keys, improving readability and maintainability of the database schema.
#    - `db = SQLAlchemy(metadata=metadata)`: Creates a SQLAlchemy instance, which handles all database operations.

# 2. Models:
#    - `House`, `Manager`, `Tenant`: These classes define the database tables and their columns.
#    - `__tablename__`: Specifies the name of the table in the database.
#    - `Column`: Defines a column in the table, specifying its data type (Integer, String, Float), primary key, and foreign key relationships.

# 3. Relationships:
#    - `relationship()`: Defines relationships between models.
#    - `back_populates`: Creates a bidirectional relationship, allowing you to access related objects from both sides.
#    - `House` has one-to-many relationships with `Manager` and `Tenant`: A house can have multiple managers and tenants.
#    - `Manager` and `Tenant` have many-to-one relationships with `House`: A manager or tenant belongs to one house.
#    - **Use Case:** These relationships allow you to easily navigate and access related data. For example, you can get all managers of a house by accessing `house.managers`, or get the house a manager works at by accessing `manager.house`.

# 4. Foreign Keys:
#    - `ForeignKey`: Establishes a link between tables, ensuring data integrity.
#    - `house_id` in `Manager` and `Tenant` models references the `id` of the `House` model.

# 5. Serialization:
#    - `SerializerMixin`: Simplifies converting model objects to dictionaries or JSON.
#    - `serialize_rules`: Prevents circular references during serialization.
#    - **Use Case:** When you want to return data from your API, you need to convert database objects to JSON. `SerializerMixin` makes this easy.
#    - Circular references happen when object A contains object B, and object B contains object A, and this loops. The rules prevent this.
#    - Example: if we serialize a house, and it contains managers, and we do not use the rule, each manager would contain the house it belongs to, which then contains the managers, and so on.

# 6. Association Proxy:
#    - The `association_proxy` import is included in the code, but is not used.
#    - **Use Case:** Association proxies are used when you want to access a property of a related object directly through the parent object.
#    - For example, if you wanted to access a tenant's name directly through the house object, you could use an association proxy.
#    - Because we are using direct relationships, and serialize rules, we do not need association proxies.

# 7. `__repr__`:
#    - Provides a string representation of the model objects, useful for debugging and logging.
