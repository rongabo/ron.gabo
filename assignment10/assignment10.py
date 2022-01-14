import json
import random
import string

import mysql
import mysql.connector
import requests
from flask import Flask, request, render_template, session, redirect, Blueprint, flash, Response

app = Flask(__name__)
app.secret_key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))

assignment10 = Blueprint(
    'assignment10',
    __name__,
    static_folder='static',
    static_url_path='/assignment10',
    template_folder='templates'
)


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='root',
                                         database='web_schema_ron')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        connection.commit()
        return_value = True
    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


@assignment10.route('/assignment10')
def exercise10():
    users = interact_db(query="select * from web_schema_ron.users", query_type='fetch')
    if session.get('messages'):
        x = session['messages']
        session.pop('messages')
        return render_template('assignment10.html', users=users, messages=x)
    else:
        return render_template('assignment10.html', users=users)


@assignment10.route('/insert', methods=['GET', 'POST'])
def insert():
    if request.method == 'POST':
        user_name = request.form['user_name']
        user_first_name = request.form['user_first_name']
        email = request.form['email']
        check_input = "SELECT user_name FROM web_schema_ron.users WHERE user_name='%s';" % user_name
        answer = interact_db(query=check_input, query_type='fetch')
        if len(answer) == 0:
            query = "insert into web_schema_ron.users(user_name, user_first_name , email)\
                            value ('%s', '%s', '%s');" % (user_name, user_first_name, email)
            interact_db(query=query, query_type='commit')
            flash('user added to data base ')
            return redirect('/assignment10')
        else:
            flash('already has a user with this userName. try another one')
            return redirect('/assignment10')
    return render_template('assignment10.html', req_method=request.method)


@assignment10.route('/update', methods=['GET', 'POST'])
def update():
    user_name = request.form['user_name']
    user_first_name = request.form['user_first_name']
    email = request.form['email']
    query = " UPDATE web_schema_ron.users SET user_first_name='%s', email='%s' WHERE user_name='%s';" % \
            (user_first_name, email, user_name)
    interact_db(query=query, query_type='commit')
    return redirect('/assignment10')


@assignment10.route('/delete', methods=['POST'])
def delete():
    user_name = request.form['user_name']
    check = "SELECT user_name FROM web_schema_ron.users WHERE user_name='%s';" % user_name
    answer = interact_db(query=check, query_type='fetch')
    if len(answer) > 0:
        query = "delete from web_schema_ron.users where user_name='%s';" % user_name
        interact_db(query=query, query_type='commit')
        flash('user deleted!  ')
        return redirect('/assignment10')
    else:
        flash('try another user name to delete.')
        return redirect('/assignment10')


@assignment10.route('/assignment11/users')
def users():
    users_ = interact_db(query="select * from web_schema_ron.users", query_type='fetch')
    return Response(json.dumps(users_), mimetype='application/json')


@assignment10.route('/req_frontend')
def req_frontend():
    return render_template('req_frontend.html')

<<<<<<< HEAD

@assignment10.route('/req_backend')
def req_backend():
    user = request.args.get('number')
    data = None
    if user:
        try:
            res = requests.get("https://reqres.in/api/users/%s" % user, verify=False)
            data = res.json()['data']
        except Exception as e:
            data = ''
    return render_template('req_backend.html', user_data=data)




@assignment10.route('/assignment12/restapi_users', defaults={'user_id': 1})
@assignment10.route('/assignment12/restapi_users/<int:user_id>')
def get_user_data(user_id):
    query = f'''
    SELECT * from users WHERE user_id={user_id}
    '''

    user_data = interact_db(query=query, query_type='fetch', named_tuple=None, dictionary=True)
    if not user_data:
        user_data = {'error': f'user  id {user_id}  not found'}
    return Response(json.dumps(user_data), mimetype='application/json')
=======

@assignment10.route('/req_backend')
def req_backend():
    user = request.args.get('number')
    data = None
    if user:
        try:
            res = requests.get("https://reqres.in/api/users/%s" % user, verify=False)
            data = res.json()['data']
        except Exception as e:
            data = ''
    return render_template('req_backend.html', user_data=data)
>>>>>>> 2c3a732187355a7d2553c04d258246758ace19ed
