from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Set up a connection between a Flask application and a SQLAlchemy database."""

    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """This models a pet potentially available for adoption"""

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False, unique=True)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    is_available = db.Column(db.Boolean, nullable=False, default=True)
