from app import app

@app.route('/')
@app.route('/index')
def hello():
    return {
        "message": "Hello Flask!"
    }