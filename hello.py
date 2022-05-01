# import flask library
from ensurepip import bootstrap
from imp import reload
from tkinter.tix import Tree
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

#initialise  object
app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config["PROPAGATE_EXCEPTIONS"] = False

# declare the decorator and view function
@app.errorhandler(400)
def page_not_found(e):
    return render_template('404.html'), 404
    
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<username>')
def user(username):    
    return render_template('user.html', username = username)

# start the webserver
if __name__ == '__main__':
    app.run(debug=True)