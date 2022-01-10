from typing_extensions import Required
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video  is required", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video")
video_put_args.add_argument("likes", type=int, help="Likes of the video")

videos = {}

class Videos(Resource):
    def get(self, video_id):
        if video_id not in videos:
            abort(404, message="Id is not valid")
        return videos[video_id]
    def put(self, video_id):
        if video_id in videos:
            abort(409, "video already exists")
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 200
    def delete(self, video_id):
        if video_id not in videos:
            abort(404, message="Id is not valid")
        del videos[video_id]
        return "", 204


api.add_resource(Videos, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)