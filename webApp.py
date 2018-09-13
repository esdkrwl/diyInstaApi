from flask import Flask, request
from flask_restful import Resource, Api
from diyInstaAPI import get_follower_count

app = Flask(__name__)
api = Api(app)


class InstaUser(Resource):
    def get(self, insta_user_name):
        follower_count = get_follower_count(insta_user_name)
        if follower_count == -1:
            return {"error": "username not found"}
        else:
            result = {'follower_count': follower_count}
            return result


api.add_resource(InstaUser, '/<insta_user_name>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
