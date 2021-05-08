from flask import Flask, request
from flask.globals import session

app = Flask(__name__)

@app.route('/')
def index():
  return 'Server Works!'
  
@app.route('/userData/',  methods=['GET'])
def say_hello():
  user_id = request.args.get("userId")
  session_id = request.args.get("sessionId") 
  
  return f'''<h1>Request Args| user_id: {user_id} | session_id: {session_id}</h1>'''



@app.route('/query-example')
def query_example():
    # if key doesn't exist, returns None
    language = request.args.get('language')

    return '''<h1>The language value is: {}</h1>'''.format(language)

    http://127.0.0.1:5000/query-example?language=Python