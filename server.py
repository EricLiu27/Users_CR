from flask import Flask, render_template, redirect, request
# import the class from friend.py
from user_model import User

app = Flask(__name__)

@app.route("/")
@app.route('/users')
def all_users():
    all_users = User.get_all()
    return render_template("read.html", all_users=all_users)


@app.route('/users/new')
def new_user():
    return render_template('create.html')
            

@app.route('/users/create', methods=['POST'])
def create_user():
    print('request form', request.form)
    User.create(request.form)
    
    return redirect('/users')
    
if __name__ == "__main__":
    app.run(debug=True)
