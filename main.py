
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('exercise2.html')


@app.route('/homepage')
def homepage():
    return redirect(url_for('my_home'))

@app.route('/cv-grid')
def cv_grid():
    return render_template('CVgrid.html')


@app.route('/cv')
def cv():
    return render_template('cv.html')

@app.route('/form')
def form():
    return render_template('forms.html')

@app.route('/home')
def home():
    return redirect('/')

@app.route('/assignment8')
def hobbies():
    return render_template('assignment8.html')
@app.route('/hobbies/computer_game')
def computer_game():
    return render_template('computer_game.html')

@app.route('/hobbies/Tv')
def Tv():
    return render_template('Tv.html')


if __name__ == '__main__':
    app.run()