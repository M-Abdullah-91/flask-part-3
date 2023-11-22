from flask import Flask, request,make_response,jsonify
from controller import user,notes,category

app = Flask(__name__)
app.config["SECRET_KEY"] = "THISISSECRETKEY"


# Register User
app.add_url_rule('/register', view_func=user.register, methods = ['POST'])

#login user
app.add_url_rule('/login', view_func=user.login, methods = ['POST'])


# create category
app.add_url_rule('/createnotes', view_func=notes.create_notes, methods = ['POST'])

# Assign notes category
app.add_url_rule('/assignnotescategory', view_func=notes.assign_note_category, methods = ['POST'])

# Get all notes
app.add_url_rule('/getallnotes', view_func=notes.view_notes, methods = ['GET'])

# create new category
app.add_url_rule('/createnewcategory', view_func=category.create_category, methods = ['POST'])

# Notes by category
app.add_url_rule('/getnotebycategory', view_func=notes.get_notes_by_category, methods = ['GET'])

if __name__ == "__main__":
    app.run(
        debug=True
    )
