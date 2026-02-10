from flask import Flask

"""
It creates an instance of the Flask class,
Which will be your  WSGI(Web Server Gateway Interface)
"""

app=Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to my flask course this is the best way you can learn. This should be an amazing course."

@app.route('/index')
def index():
    return "phunch gye index pe ek nayi jagah same area me"


if __name__=="__main__":
    app.run(debug=True)