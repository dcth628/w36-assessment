from flask import Flask
from .routes import simple
from .config import Configuration
from .models import db
from flask_migrate import Migrate

app = Flask(__name__)

app.config.from_object(Configuration)

app.register_blueprint(simple.bp)

db.init_app(app)

Migrate(app, db)
