from flask import Flask, request,make_response,jsonify
from controller import user,notes

app = Flask(__name__)
app.config["SECRET_KEY"] = "THISISSECRETKEY"


# Register User
app.add_url_rule('/register', view_func=user.register, methods = ['POST'])


if __name__ == "__main__":
    app.run(
        debug=True
    )
