from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

# Must come after db initialization, as it uses that
from models import Patient, Question

@app.route('/patient', methods=['POST', 'GET'])
def patient():
    if request.method == 'POST':
        return create_patient()
    elif request.method == 'GET':
        return get_patient()


@app.route('/patient/<patient_id>', methods=['PUT', 'DELETE'])
def patient_with_id(patient_id):
    if request.method == 'PUT':
        return update_patient(patient_id)
    elif request.method == 'DELETE':
        return delete_patient(patient_id)


def create_patient():
    return None


def get_patient():
    return None


def update_patient(patient_id):
    return None


def delete_patient(patient_id):
    return None


if __name__ == '__main__':
    app.run()
