from flask import Flask, jsonify, request
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

# Must come after db initialization, as it uses that
from models import Patient, Question, Answer

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


@app.route('/question', methods=['POST', 'GET'])
def question():
    if request.method == 'POST':
        return create_question()
    elif request.method == 'GET':
        return get_question()


@app.route('/question/<question_id>', methods=['PUT', 'DELETE'])
def question_with_id(question_id):
    if request.method == 'PUT':
        return update_question(question_id)
    elif request.method == 'DELETE':
        return delete_question(question_id)


def create_question():
    # TODO(tavi) Error response if there's an issue.
    data = dict(request.json)
    conditional_on = None
    if Question.conditional_on.name in data:
        conditional_on = data[Question.conditional_on.name]
    question = Question(text=data[Question.text.name],
                        conditional_on=conditional_on)
    db.session.add(question)
    db.session.commit()
    return success_response()


def get_question():
    return None


def update_question(question_id):
    return None


def delete_question(question_id):
    return None


@app.route('/answer', methods=['POST', 'GET'])
def answer():
    if request.method == 'POST':
        return create_answer()
    elif request.method == 'GET':
        return get_answer()


@app.route('/answer/<answer_id>', methods=['PUT', 'DELETE'])
def answer_with_id(answer_id):
    if request.method == 'PUT':
        return update_answer(answer_id)
    elif request.method == 'DELETE':
        return delete_answer(answer_id)


def create_answer():
    # TODO(tavi) Error response if there's an issue.
    data = dict(request.json)
    answer = Answer(text=data[Answer.text.name],
                    question_id=data[Answer.question_id.name])
    db.session.add(answer)
    db.session.commit()
    return success_response()


def get_answer():
    return None


def update_answer(answer_id):
    return None


def delete_answer(answer_id):
    return None


def success_response():
    response = jsonify({'success': True})
    return response


def error_response(error, message):
    response = jsonify({'error': error, 'message': message})
    response.status_code = 400
    return response
