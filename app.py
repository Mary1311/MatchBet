from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)
app.config['Flask_ENV'] = 'development'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///match.db'
app.config['SECRET_KEY'] = 'anykey'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

@app.get('/')
def index():
    return render_template('index.html')

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(20), unique=True, nullable=False)
    telegram_id = db.Column(db.String)


class Tournament(db.Model):
    __tablename__ = 'tournaments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)


class Match(db.Model):
    __tablename__ = 'matches'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    start_datetime = db.Column(db.DateTime, nullable=False)
    team_1 = db.Column(db.String(20), unique=True, nullable=False)
    team_2 = db.Column(db.String(20), unique=True, nullable=False)
    team_1_score = db.Column(db.Integer, nullable=False)
    team_2_score = db.Column(db.Integer, nullable=False)


class Team(db.Model):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)


# class UserVoting(db.Model):
#     __tablename__ = 'votings'
#
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     team_1_score = db.Column(db.Integer, nullable=False)
#     team_2_score = db.Column(db.Integer, nullable=False)
#     match_id = db.Column(db.Integer, db.ForeignKey('matches.id'))


admin = Admin(app, name='Матчи', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session, name='Пользователь'))
admin.add_view(ModelView(Tournament, db.session, name='Турнир'))
admin.add_view(ModelView(Match, db.session, name='Матч'))
admin.add_view(ModelView(Team, db.session, name='Команда'))
# admin.add_view(ModelView(UserVoting, db.session, name='Голосование'))


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

