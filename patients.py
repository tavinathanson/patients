from flask import Flask, jsonify, request
from flask.ext.sqlalchemy import SQLAlchemy
from flask.views import MethodView


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


# Must come after db initialization, as it uses that
from models import Patient, Question, Answer


class PatientAPI(MethodView):
    def get(self):
        return None

    
patient_view = PatientAPI.as_view('patient_api')
app.add_url_rule('/patient', view_func=patient_view)


class QuestionAPI(MethodView):
    def post(self):
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


question_view = QuestionAPI.as_view('question_api')
app.add_url_rule('/question', methods=['POST'], view_func=question_view)


class AnswerAPI(MethodView):
    def post(self):
        # TODO(tavi) Error response if there's an issue.
        data = dict(request.json)
        answer = Answer(text=data[Answer.text.name],
                        question_id=data[Answer.question_id.name])
        db.session.add(answer)
        db.session.commit()
        return success_response()


answer_view = AnswerAPI.as_view('answer_api')
app.add_url_rule('/answer', methods=['POST'], view_func=answer_view)


def success_response():
    response = jsonify({'success': True})
    return response


def error_response(error, message):
    response = jsonify({'error': error, 'message': message})
    response.status_code = 400
    return response
