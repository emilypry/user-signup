from flask import Flask, request, redirect, render_template
app = Flask(__name__)
app.config['DEBUG'] = True      # displays runtime errors in the browser, too


@app.route('/error', methods=['POST'])
def get_errors():
    username = request.form['user']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    e1=''
    e2=''
    e3=''
    e4=''
    error = False

    if username == '' or username.count(' ')>0 or len(username)<3 or len(username)>20:
        e1 = "That's not a valid username"
        error = True
    if password == '' or password.count(' ')>0 or len(password)<3 or len(password)>20:
        e2 = "That's not a valid password"
        error = True  
    if verify != password:
        e3 = "Passwords don't match"
        error = True
    if email.count('@')!=1 or email.count('.')!=1 or email.count(' ')>0 or len(email)<3 or len(email)>20:
        e4 = "That's not a valid email"
        error = True

    if error==True:
        return render_template('main.html', username=username, email = email, e1=e1, e2=e2, e3=e3, e4=e4)
    if error==False:
        return render_template('welcome.html', username=username)


@app.route('/')
def index():
    return render_template('main.html')

app.run()