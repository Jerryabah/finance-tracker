from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FloatField, SelectField, TextAreaField, DateField
from wtforms.validators import DataRequired, Email, Length, NumberRange, EqualTo
from datetime import date

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(), 
        Length(min=4, max=20, message="Username must be between 4 and 20 characters")
    ])
    email = StringField('Email', validators=[
        DataRequired(), 
        Email(message="Please enter a valid email address")
    ])
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=6, message="Password must be at least 6 characters long")
    ])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(),
        EqualTo('password', message="Passwords must match")
    ])

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class TransactionForm(FlaskForm):
    amount = FloatField('Amount', validators=[
        DataRequired(),
        NumberRange(min=0.01, message="Amount must be greater than 0")
    ])
    description = StringField('Description', validators=[
        DataRequired(),
        Length(max=200, message="Description cannot exceed 200 characters")
    ])
    transaction_type = SelectField('Type', choices=[
        ('expense', 'Expense'),
        ('income', 'Income')
    ], validators=[DataRequired()])
    category_id = SelectField('Category', coerce=int, validators=[DataRequired()])
    date = DateField('Date', validators=[DataRequired()], default=date.today)
    
    def __init__(self, *args, **kwargs):
        super(TransactionForm, self).__init__(*args, **kwargs)
        # Categories will be populated dynamically in the route

class CategoryForm(FlaskForm):
    name = StringField('Category Name', validators=[
        DataRequired(),
        Length(max=50, message="Category name cannot exceed 50 characters")
    ])
    description = TextAreaField('Description', validators=[
        Length(max=200, message="Description cannot exceed 200 characters")
    ])