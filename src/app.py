from flask import Flask
from flask_restful import Api
from controller.Author import Author
from controller.AuthorList import AuthorList

app = Flask(__name__)
api = Api(app)

@app.route('/')
def home():
  return 'Hello World'

api.add_resource(AuthorList, '/api/author');
api.add_resource(Author, '/api/author/<id>');

app.run(port=5000, debug=True);
