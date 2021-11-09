from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, ValidationError
from wtforms.validators import InputRequired, NumberRange

from app.models import User

class ResultForm(FlaskForm):
    player1 = StringField('Player1 username', validators=[InputRequired()])
    player1Score = IntegerField('Player1 score', validators=[InputRequired(), NumberRange(min=0, max=None)])

    player2 = StringField('Player2 username', validators=[InputRequired()])
    player2Score = IntegerField('Player2 score', validators=[InputRequired(), NumberRange(min=0, max=None)])

    submit = SubmitField('Submit')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Username already in use.')