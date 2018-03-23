from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField, TextAreaField, SelectField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired, Email, InputRequired


class UserProfileForm(FlaskForm):
    first_name  = StringField('First Name', validators=[DataRequired()], render_kw={"placeholder":"Jon"})
    last_name   = StringField('Last Name', validators=[DataRequired()], render_kw={"placeholder":"Snow"})
    gender      = SelectField('Gender',validators=[DataRequired()], choices = [("MALE", "Male"), ("FEMALE", "Female")])
    email       = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder":"jon@hbo.com"})
    location    = StringField('Location', validators=[DataRequired()], render_kw={"placeholder":"Kings Landing"})
    biography   = TextAreaField("Biography", validators=[DataRequired()])
    photo       = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg', 'gif'])])