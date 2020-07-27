from flask import Flask
from flask_restful import Api
from Author import Author

app = Flask(__name__)
api = Api(app)

@app.route('/')
def home():
  return 'Hello World'

api.add_resource(Author, '/api/author');

app.run(port=5000, debug=True);
