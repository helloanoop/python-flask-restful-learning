from flask_restful import Resource

class AuthorList(Resource):
  def get(self):
    return {'message': 'GET Route was invoked'}

  def post(self):
    return {'message': 'POST Route was invoked'}
