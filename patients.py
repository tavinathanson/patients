from flask import Flask, jsonify, request
from flask.ext.sqlalchemy import SQLAlchemy
from flask.views import MethodView


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


# Must come after db initialization, as it uses that
from models import Patient, Question, Answer


def register_api(view, endpoint, url, pk='id', pk_type='int'):
    view_func = view.as_view(endpoint)
    app.add_url_rule(url, defaults={pk: None},
                     view_func=view_func, methods=['GET'])
    app.add_url_rule(url, view_func=view_func, methods=['POST'])
    app.add_url_rule('%s<%s:%s>' % (url, pk_type, pk),
                     view_func=view_func,
                     methods=['GET', 'PUT', 'DELETE'])


class PatientAPI(MethodView):
    def get(self):
        return None


register_api(PatientAPI, 'patient_api', '/patient')


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


register_api(QuestionAPI, 'question_api', '/question')


class AnswerAPI(MethodView):
    def post(self):
        # TODO(tavi) Error response if there's an issue.
        data = dict(request.json)
        answer = Answer(text=data[Answer.text.name],
                        question_id=data[Answer.question_id.name])
        db.session.add(answer)
        db.session.commit()
        return success_response()


register_api(AnswerAPI, 'answer_api', '/answer')


def success_response():
    response = jsonify({'success': True})
    return response


def error_response(error, message):
    response = jsonify({'error': error, 'message': message})
    response.status_code = 400
    return response
