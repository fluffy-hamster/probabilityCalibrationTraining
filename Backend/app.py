from flask import Flask, request, Response
from typing import Dict

from Backend.HelperFunctions import get_questions, generate_probabilities, plot_user_data
#from Backend.SessionUser import SessionUser
from Backend.Question import Question
from Backend.Database.DatabaseAPI import DatabaseApi

DOCUMENTATION = """

# Grab a question: 
Example Query:
    http://127.0.0.1:5000/questions/?numberOfQuestions=1

"""

app = Flask(__name__)

@app.route('/')
def index():
  return 'Backend Running! For help about the Api, navagitate to <url>/help/'

@app.route('/help/',  methods=['GET'])
def get_help_text():
  return DOCUMENTATION
  
@app.route('/questions/',  methods=['GET'])
def fetch_questions():
  number_of_questions = int(request.args.get("numberOfQuestions", -1))
  
  question_response = get_questions(number_of_questions)
  if question_response is None:
    return Response("Failed to get Questions", status=500)

  questions: Dict[int, Question] = {i: Question(v) for i, v in enumerate(question_response)}
  question = questions[0]

  return f"<h2>QUESTION 1: {question.question}</h2>" + "\n".join([f"\t{i+1}: {question.awnser_list[i]}" for i in range(len(question.awnser_list))])


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