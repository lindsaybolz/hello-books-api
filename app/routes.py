from flask import Blueprint

hello_world_bp = Blueprint("hello_world", __name__)

@hello_world_bp.route("/hello_world", methods=["GET"])
def say_hello():
    response = "Hello World!"
    return response, 200