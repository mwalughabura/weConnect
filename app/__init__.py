from flask import Flask

app = Flask(__name__)

from app import routes
from app.auth.routes import mod

app.register_blueprint(auth.routes.mod, url_prefix='/api/v1/auth')