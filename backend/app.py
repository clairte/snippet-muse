# backend entry point 

from flask import Flask 
from routes import upload_blueprint

# initiate flask application 
app = Flask(__name__)

# register blueprints
app.register_blueprint(upload_blueprint)

# test route 
@app.route('/')
def home(): 
    return "Server is running!"

if __name__ == '__main__':
    app.run(debug=True)


