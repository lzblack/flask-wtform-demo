from wtforms import Form, FloatField, validators, SelectField
from math import pi


class InputForm(Form):
    A = FloatField(
        label='amplitude (m)', default=1.0,
        validators=[validators.InputRequired()])
    b = SelectField(
        label='Award', choices=[('actor', 'Best Actor'), ('actress', 'Best Actress')], validators=[validators.InputRequired()])
    w = FloatField(
        label='frequency (1/s)', default=2 * pi,
        validators=[validators.InputRequired()])
    T = FloatField(
        label='time interval (s)', default=18,
        validators=[validators.InputRequired()])
