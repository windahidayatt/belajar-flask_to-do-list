from flask import Flask

from .main.routes import main
from .extensions import mongo

def create_app():
    app = Flask(__name__)

    app.config['MONGO_URI'] = 'mongodb+srv://winda-1:winda123@cluster-win.3grdf.mongodb.net/to-do-list?retryWrites=true&w=majority'
    
    mongo.init_app(app)

    app.register_blueprint(main)
    return app