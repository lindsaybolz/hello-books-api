from flask import Blueprint

hello_world_bp = Blueprint("hello_world", __name__)

@hello_world_bp.route("/hello_world", methods=["GET"])
def say_hello():
    response = "Hello World!"
    return response, 200

@hello_world_bp.route("/hello/JSON", methods=["GET"])
def say_hello_json():
    response = {
        "name": "Ada Lovelace",
        "message": "Hello!",
        "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
    }
    return response, 200

