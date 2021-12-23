import phone as phone
from flask import Flask, request, render_template, session, url_for, redirect
import random
import string

app = Flask(__name__)
app.secret_key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))

users = {'user1': {'name': 'Ron', 'email': 'Ron@gmail.com', 'User Name': 'Ron1'},
         'user2': {'name': 'Eden', 'email': 'Eden@gmail.com', 'User Name': 'Eden1'},
         'user3': {'name': 'Dana', 'email': 'Dana@gmail.com', 'User Name': 'Dana1'},
         'user4': {'name': 'Romi', 'email': 'Romi@gmail.com', 'User Name': 'Romi1'},
         'user5': {'name': 'Dani', 'email': 'Shon@gmail.com', 'User Name': 'Dani1'}}

@app.route('/assignment9', methods=["POST", "GET"])
def exercise9():
    if request.method == "POST":
        session["userName"] = request.form.get("userName")

        return redirect(url_for('exercise9'))
    else:
        query_parameters = request.args
        userName = session.get('userName')
        if 'name' in query_parameters:
            name = query_parameters['name']
            if name == '':
                return render_template('assignment9.html', users=list(users.values()), userName=userName)
            else:
                found_user = []
                for user_data in users.values():
                    if user_data['name'] == name:
                        found_user.append(user_data)
                return render_template('assignment9.html', users=found_user, userName=userName)
        return render_template('assignment9.html', userName=userName)


@app.route('/')

def my_home():
    userName = session.get('userName')
    return render_template('exercise2.html', userName=userName)


@app.route('/homepage')
def homepage():
    return redirect(url_for('my_home'))

@app.route('/cv-grid')
def cv_grid():
    userName = session.get('userName')
    return render_template('CVgrid.html', userName=userName)


@app.route('/cv')
def cv():
    userName = session.get('userName')
    return render_template('cv.html', userName=userName)

@app.route('/form')
def form():
    userName = session.get('userName')
    return render_template('forms.html', userName=userName)

@app.route('/home')
def home():
    return redirect('/')

@app.route('/assignment8')
def hobbies():
    userName = session.get('userName')
    return render_template('assignment8.html', userName=userName)
@app.route('/hobbies/computer_game')
def computer_game():
    userName = session.get('userName')
    return render_template('computer_game.html', userName=userName)

@app.route('/hobbies/Tv')
def Tv():
    userName = session.get('userName')
    return render_template('Tv.html', userName=userName)

@app.route('/logout')
def logout():
    session['userName'] = None
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run()