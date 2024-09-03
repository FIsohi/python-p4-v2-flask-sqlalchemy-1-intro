# server/app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize Flask application
app = Flask(__name__)

# Configure database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy and Flask-Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define a model class
class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)

# Define routes (for demonstration purposes)
@app.route('/')
def index():
    return "Welcome to the Pet Database!"

@app.route('/create-pet/<name>/<species>')
def create_pet(name, species):
    pet = Pet(name=name, species=species)
    db.session.add(pet)
    db.session.commit()
    return f"Pet {name} of species {species} created!"

@app.route('/pets')
def list_pets():
    pets = Pet.query.all()
    return '<br>'.join([f"{pet.id}: {pet.name} ({pet.species})" for pet in pets])

if __name__ == '__main__':
    app.run(port=5555, debug=True)
