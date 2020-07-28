from flask_restful import Resource

class Author(Resource):
  def get(self, id):
    print(id);
    return {'message': 'GET Route was invoked'}

  def put(self, id):
    print(id);
    return {'message': 'PUT Route was invoked'}

  def delete(self, id):
    print(id);
    return {'message': 'DELETE Route was invoked'}
