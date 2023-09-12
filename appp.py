from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from sqlalchemy import String

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/database_name'
db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.String(4), primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Create the database table if it doesn't exist
db.create_all()

@app.route('/api', methods=['POST'])
def create_person():
    try:
        data = request.json
        name = data.get('name')

        if not name or not isinstance(name, str):
            return jsonify({'error': 'Invalid input for "name"'}), 400

        person = Person(name=name)
        db.session.add(person)
        db.session.commit()

        return jsonify({'message': 'Person created successfully'}), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Person with the same name already exists'}), 400

@app.route('/api/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def person_by_id(user_id):
    person = Person.query.get_or_404(user_id)

    if request.method == 'GET':
        return jsonify({'name': person.name})

    if request.method == 'PUT':
        try:
            data = request.json
            new_name = data.get('name')

            if not new_name or not isinstance(new_name, str):
                return jsonify({'error': 'Invalid input for "name"'}), 400

            person.name = new_name
            db.session.commit()

            return jsonify({'message': 'Person updated successfully'})

        except IntegrityError:
            db.session.rollback()
            return jsonify({'error': 'Person with the same name already exists'}), 400

    if request.method == 'DELETE':
        db.session.delete(person)
        db.session.commit()
        return jsonify({'message': 'Person deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
