from flask import Flask, jsonify  # Import Flask and jsonify for creating JSON responses
from flask_migrate import Migrate  # Import Migrate for database migrations
from models import db, House, Manager, Tenant  # Import database instance and models

# Create a Flask application instance
app = Flask(__name__)

# In this case, we're using SQLite and storing the database in a file named 'app.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

# Disable SQLAlchemy track modifications to avoid unnecessary overhead
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Flask-Migrate with the Flask app and the SQLAlchemy database instance
migrate = Migrate(app, db)

# Initialize the SQLAlchemy database instance with the Flask app
db.init_app(app)

# --- Routes ---

# Root route ('/')
@app.route('/')
def index():
    # Return a JSON response with a welcome message
    return jsonify({"message": "Welcome to the House Management API!"})

# Route to get all houses ('/houses')
@app.route('/houses', methods=['GET'])  # Only accept GET requests
def get_houses():
    # Query all houses from the database
    houses = House.query.all()
    # Convert each house object to a dictionary using to_dict() and create a list
    houses_list = [house.to_dict() for house in houses]
    # Return the list of house dictionaries as a JSON response
    return jsonify(houses_list)

# Route to get a specific house by ID ('/houses/<int:id>')
@app.route('/houses/<int:id>', methods=['GET'])  # Only accept GET requests
def get_house_by_id(id):
    # Query the house with the given ID from the database
    house = House.query.get(id)
    # Check if the house exists
    if house:
        # If the house exists, return it as a JSON response
        return jsonify(house.to_dict())
    else:
        # If the house doesn't exist, return a JSON error message and a 404 status code
        return jsonify({"error": "House not found"}), 404

# Route to get all managers ('/managers')
@app.route('/managers', methods=['GET'])  # Only accept GET requests
def get_managers():
    # Query all managers from the database
    managers = Manager.query.all()
    # Convert each manager object to a dictionary and create a list
    managers_list = [manager.to_dict() for manager in managers]
    # Return the list of manager dictionaries as a JSON response
    return jsonify(managers_list)

# Route to get a specific manager by ID ('/managers/<int:id>')
@app.route('/managers/<int:id>', methods=['GET']) # Only accept GET requests
def get_manager_by_id(id):
    # Query the manager with the given ID from the database
    manager = Manager.query.get(id)
    # Check if the manager exists
    if manager:
        # If the manager exists, return it as a JSON response
        return jsonify(manager.to_dict())
    else:
        # If the manager doesn't exist, return a JSON error message and a 404 status code
        return jsonify({"error": "Manager not found"}), 404

# Route to get all tenants ('/tenants')
@app.route('/tenants', methods=['GET']) # Only accept GET requests
def get_tenants():
    # Query all tenants from the database
    tenants = Tenant.query.all()
    # Convert each tenant object to a dictionary and create a list
    tenants_list = [tenant.to_dict() for tenant in tenants]
    # Return the list of tenant dictionaries as a JSON response
    return jsonify(tenants_list)

# Route to get a specific tenant by ID ('/tenants/<int:id>')
@app.route('/tenants/<int:id>', methods=['GET']) # Only accept GET requests
def get_tenant_by_id(id):
    # Query the tenant with the given ID from the database
    tenant = Tenant.query.get(id)
    # Check if the tenant exists
    if tenant:
        # If the tenant exists, return it as a JSON response
        return jsonify(tenant.to_dict())
    else:
        # If the tenant doesn't exist, return a JSON error message and a 404 status code
        return jsonify({"error": "Tenant not found"}), 404

# Route to get all managers of a specific house ('/houses/<int:house_id>/managers')
@app.route('/houses/<int:house_id>/managers', methods=['GET']) # Only accept GET requests
def get_house_managers(house_id):
    # Query the house with the given ID from the database
    house = House.query.get(house_id)
    # Check if the house exists
    if house:
        # If the house exists, get all managers associated with that house
        managers = [manager.to_dict() for manager in house.managers]
        # Return the list of manager dictionaries as a JSON response
        return jsonify(managers)
    else:
        # If the house doesn't exist, return a JSON error message and a 404 status code
        return jsonify({"error": "House not found"}), 404

# --- Main Execution ---

# Run the Flask app if this script is executed directly
if __name__ == '__main__':
    # Start the Flask development server on port 5555 with debug mode enabled
    app.run(port=5555, debug=True)
