from flask import Flask, request
from typing import Dict

from backend.HelperFunctions import get_questions, generate_probabilities, plot_user_data
#from Backend.SessionUser import SessionUser
from backend.Question import Question
from backend.Database.DatabaseAPI import DatabaseApi


app = Flask(__name__)

@app.route('/')
def index():
  return 'Server Works!'
  
@app.route('/questions/',  methods=['GET'])
def get_questions():
  number_of_questions = int(request.args.get("numberOfQuestions", -1))
  
  response = get_questions(number_of_questions)
  if response is not None:
      questions: Dict[int, Question] = {i: Question(v) for i, v in enumerate(response)}


@app.route('/userData/',  methods=['GET'])
def say_hello():
  user_id = request.args.get("userId")
  session_id = request.args.get("sessionId") 
  
  return f'''<h1>Request Args| user_id: {user_id} | session_id: {session_id}</h1>'''


"""
https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask
@app.route('/query-example')
def query_example():
    # if key doesn't exist, returns None
    language = request.args.get('language')

    return '''<h1>The language value is: {}</h1>'''.format(language)

    http://127.0.0.1:5000/query-example?language=Python
"""