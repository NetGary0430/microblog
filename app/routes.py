from app import app


# the @app.route is a decorator which modifies the function that follows it.
# common pattern:  use them to register functions as callbacks for certain events

@app.route('/')
@app.route('/index')

def index():
    return "Hello, World!"
