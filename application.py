from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///people.db'
db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, name):
        self.name = name

with app.app_context():  # Create an application context
    db.create_all()  # Create the database tables

@app.route('/api', methods=['POST'])
def create_person():
    data = request.get_json()
    name = data.get('name')
    if not name or not isinstance(name, str):
        return jsonify({'error': 'Invalid input for "name"'}), 400

    try:
        person = Person(name)
        db.session.add(person)
        db.session.commit()
        response_data = {
            'id': person.id,  
            'message': 'Person created successfully'
        }
        return jsonify(response_data), 201
        #return jsonify({'message': 'Person created successfully'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'message': 'Duplicate entry. Person already exists'}), 409

@app.route('/api', methods=['GET'])
def get_people():
    people = Person.query.all()
    result = [{'id': person.id, 'name': person.name} for person in people]
    return jsonify(result), 200

@app.route('/api/<int:user_id>', methods=['GET'])
def get_person(user_id):
    person = Person.query.get(user_id)
    if not person:
        return jsonify({'message': 'Person not found'}), 404
    return jsonify({'id': person.id, 'name': person.name}), 200

@app.route('/api/<int:user_id>', methods=['PUT', 'PATCH'])
def update_person(user_id):
    person = Person.query.get(user_id)
    if not person:
        return jsonify({'message': 'Person not found'}), 404
    
    data = request.get_json()
    name = data.get('name')
    if not name:
        return jsonify({'message': 'Name is required'}), 400

    person.name = name
    db.session.commit()
    return jsonify({'message': 'Person updated successfully'}), 200

@app.route('/api/<int:user_id>', methods=['DELETE'])
def delete_person(user_id):
    person = Person.query.get(user_id)
    if not person:
        return jsonify({'message': 'Person not found'}), 404
    
    db.session.delete(person)
    db.session.commit()
    return jsonify({'message': 'Person deleted successfully'}), 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
