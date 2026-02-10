from flask import Flask

app = Flask(__name__)

# Static route
@app.route("/")
def hello(): # functions like these are called view functions
    return {"message": "Hello world!"}
    # return '<h1>Hello World!</h1>'
    
# Dynamic route
@app.route('/user/<name>')
def user(name):
    return f"User {name}"
    
@app.route('/user/<int:id>')
def id(id):
    return f"Number {id}"

if __name__ == "__main__":
    app.run(debug=True)