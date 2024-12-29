from flask_sqlalchemy import SQLAlchemy
from .settings import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST

database_name = DB_NAME
database_user = DB_USER
database_password = DB_PASSWORD
database_host = DB_HOST
database_path = 'postgresql://{}:{}@{}/{}?sslmode=require'.format(database_user, database_password, database_host, database_name)

db = SQLAlchemy()

def setup_db(app):
    if not hasattr(app, 'extensions') or 'sqlalchemy' not in app.extensions:
        app.config["SQLALCHEMY_DATABASE_URI"] = database_path
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        db.app = app
        db.init_app(app)
        with app.app_context():
            db.create_all()

movie_actor_association = db.Table(
    'movie_actor',
    db.Column('movie_id', db.Integer, db.ForeignKey('movies.id'), primary_key=True),
    db.Column('actor_id', db.Integer, db.ForeignKey('actors.id'), primary_key=True)
)

class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    release_date = db.Column(db.Date, nullable=False)
    actors = db.relationship('Actor', secondary=movie_actor_association, back_populates='movies')

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def rollback(self):
        db.session.rollback()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()
        
    def get_data(self):
        return {
            'id': self.id,
            'title': self.title,
            'releaseDate': self.release_date,
        }

class Actor(db.Model):
    __tablename__ = 'actors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    movies = db.relationship('Movie', secondary=movie_actor_association, back_populates='actors')

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def rollback(self):
        db.session.rollback()

    def get_data(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }