import random
import string

from flask import Flask, request, render_template, session, url_for, redirect
from assignment10.assignment10 import assignment10
app = Flask(__name__)
app.secret_key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
app.register_blueprint(assignment10)
users = [
    {'user_name': 'Ron', 'email': 'Ron@gmail.com', 'User Name': 'Ron1'},
    {'user_name': 'Eden', 'email': 'Eden@gmail.com', 'User Name': 'Eden1'},
    {'user_name': 'Dana', 'email': 'Dana@gmail.com', 'User Name': 'Dana1'},
    {'user_name': 'Romi', 'email': 'Romi@gmail.com', 'User Name': 'Romi1'},
    {'user_name': 'Dani', 'email': 'Shon@gmail.com', 'User Name': 'Dani1'},
]


@app.route('/assignment9', methods=["POST", "GET"])
def exercise9():
    if request.method == "POST":
        session["userName"] = request.form["userName"]
        return redirect(url_for('exercise9'))
    else:
        query_parameters = request.args
        userName = session.get('userName')
        if 'name' in query_parameters:
            name = query_parameters['name']
            if name == '':
                found_users = list(users)
            else:
                found_users = [user for user in users if user['user_name'] == name]
            return render_template('assignment9.html', users=found_users, userName=userName)
        return render_template('assignment9.html', userName=userName)


@app.route('/')
def my_home():
    return render_template('exercise2.html', userName=session.get('userName'))


@app.route('/homepage')
def homepage():
    return redirect(url_for('my_home'))


@app.route('/cv-grid')
def cv_grid():
    return render_template('CVgrid.html', userName=session.get('userName'))


@app.route('/cv')
def cv():
    return render_template('cv.html', userName=session.get('userName'))


@app.route('/form')
def form():
    return render_template('forms.html', userName=session.get('userName'))


@app.route('/home')
def home():
    return redirect('/')


@app.route('/assignment8')
def hobbies():
    return render_template('assignment8.html', userName=session.get('userName'))


@app.route('/hobbies/computer_game')
def computer_game():
    return render_template('computer_game.html', userName=session.get('userName'))


@app.route('/hobbies/Tv')
def Tv():
    return render_template('Tv.html', userName=session.get('userName'))


@app.route('/logout')
def logout():
    session['userName'] = None
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run()
