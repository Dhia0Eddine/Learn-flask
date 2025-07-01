# Importing necessary modules from Flask
from flask import Flask, request, jsonify

# Importing the database instance and model from models.py
from models import db, Venue

# Configuration settings (like DB URL) from config.py
from config import Config

# Create a new Flask app instance
app = Flask(__name__)

# Load settings from Config class
app.config.from_object(Config)

# Initialize the database with the Flask app
db.init_app(app)

# -------------------------------
# Route: Home endpoint
# Method: GET
# URL: /
# Purpose: Just a simple route to test if the app is running
@app.route("/")
def home():
    return "Venue API is running!"

# -------------------------------
# Route: Create a new venue
# Method: POST
# URL: /venues
@app.route("/venues", methods=["POST"])
def create_venue():
    # Parse the incoming JSON data
    data = request.get_json()

    # Create a new Venue instance using the data
    venue = Venue(
        name=data.get("name"),           # Required
        location=data.get("location"),   # Optional
        capacity=data.get("capacity")    # Optional
    )

    # Add the new venue to the DB session and commit (save it)
    db.session.add(venue)
    db.session.commit()

    # Return the serialized venue with HTTP 201 Created
    return jsonify(venue.serialize()), 201

# -------------------------------
# Route: Get all venues
# Method: GET
# URL: /venues
@app.route("/venues", methods=["GET"])
def get_venues():
    # Query all venues from the DB
    venues = Venue.query.all()

    # Return a list of serialized venues (Python objects converted to JSON)
    return jsonify([v.serialize() for v in venues]), 200

# -------------------------------
# Route: Get a single venue by ID
# Method: GET
# URL: /venues/<venue_id>
@app.route("/venues/<int:venue_id>", methods=["GET"])
def get_venue(venue_id):
    # Fetch venue by ID or return 404 if not found
    venue = Venue.query.get_or_404(venue_id)

    # Return serialized venue
    return jsonify(venue.serialize()), 200

# -------------------------------
# Route: Update a venue
# Method: PUT
# URL: /venues/<venue_id>
@app.route("/venues/<int:venue_id>", methods=["PUT"])
def update_venue(venue_id):
    # Fetch the existing venue by ID
    venue = Venue.query.get_or_404(venue_id)

    # Get incoming data
    data = request.get_json()

    # Update only the fields that are provided (partial update)
    venue.name = data.get("name", venue.name)
    venue.location = data.get("location", venue.location)
    venue.capacity = data.get("capacity", venue.capacity)

    # Save changes
    db.session.commit()

    # Return the updated venue
    return jsonify(venue.serialize()), 200

# -------------------------------
# Route: Delete a venue
# Method: DELETE
# URL: /venues/<venue_id>
@app.route("/venues/<int:venue_id>", methods=["DELETE"])
def delete_venue(venue_id):
    # Get the venue or return 404
    venue = Venue.query.get_or_404(venue_id)

    # Delete from DB and commit
    db.session.delete(venue)
    db.session.commit()

    # Return success message with 204 (no content)
    return jsonify({"message": "Venue deleted"}), 204

if __name__ == "__main__":
    with app.app_context():
        db.create_all() 
    app.run(debug=True)
