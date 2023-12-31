"""Main Code for Flask App"""

from flask import Flask
from flask_cors import CORS
from flaskr.songInterface import SongInterface
from flaskr.songInterfaceBlueprint import constructBlueprint
#export FLASK_APP=flaskr
#export FLASK_ENV=development
#python -m flask run
def create_app():
    app = Flask(__name__, instance_relative_config=True)
    cors = CORS(app)
    
    songInterface = SongInterface()
    bluePrint = constructBlueprint(songInterface)
    app.register_blueprint(bluePrint)
    
    return app