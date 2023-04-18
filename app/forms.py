from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, TextAreaField, DateField, SelectField, BooleanField
from wtforms.validators import DataRequired

types = ["Other", "String", "Woodwind", "Brass", "Percussion"]

class NewInstrument(FlaskForm):
    date_bought = DateField('Date Bought', validators=[DataRequired()])
    nickname = StringField('Nickname', validators=[DataRequired()])
    year = IntegerField('Year')
    maker = StringField('Maker')
    type = SelectField(
        'Type',
        choices=types,
    )
    used = BooleanField('Used', validators=[DataRequired()])
    submit = SubmitField('Submit')
