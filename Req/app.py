from flask import Flask, render_template, request

# TODO: create new Flask app
app = Flask(__name__)

users = [("ossama54@gmail.com", "mostafa", "147"), ("yomna7@gmailcom", "yomna", "789") ]


@app.route("/")
def main_page():
    # TODO: return index.html
    return render_template("index.html")


# TODO: Add route for sign up
@app.route("/form_SignUp")
def sign_up():
    # TODO: get user input from request
    email    = request.args['email']
    username = request.args['username']
    password = request.args['password']

    if not user_exists(email=email, username=username):
        users.append((email, username, password))
        return "<h2>New user has been created</h2>"
    else:
        return "<h2>This user already exists</h2>"


def user_exists(email, username):
    # TODO: check for user if exists, you can use an array as your records.
    for x in users:
        if (x[0] == email or x[1] == username):
            return True
    return False