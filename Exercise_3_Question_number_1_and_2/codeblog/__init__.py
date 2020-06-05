from flask import Flask
from codeblog.config import Configdetails
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow



app = Flask(__name__)
app.config.from_object(Configdetails)

db = SQLAlchemy(app)
ma = Marshmallow(app)
# engine = create_engine('sqlite:///:memory:')


from codeblog.main.routes import main
app.register_blueprint(main)


