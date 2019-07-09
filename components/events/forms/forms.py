from flask_wtf import FlaskForm
from wtforms import ValidationError
from wtforms.fields import StringField, PasswordField, SubmitField, TextAreaField, IntegerField, FloatField, RadioField
from wtforms.fields.html5 import DateField
from wtforms.validators import InputRequired, NumberRange
from models.ticketbox import Event

class CreateEventForm(FlaskForm):
    title = StringField('Title', validators = [InputRequired()])
    location = StringField('Location', validators = [InputRequired()])
    description = TextAreaField("Description", validators = [InputRequired()])
    starting_date = DateField('Starting Date')
    image_url = StringField('Image URL', validators = [InputRequired()])
    ticket_name = StringField('Ticket Name', validators = [InputRequired()])
    quantity = IntegerField('Quantity',validators = [NumberRange(min=1, max=10000)])
    submit = SubmitField('Create')


class EditEventForm(FlaskForm):
    title = StringField('Title', validators = [InputRequired()])
    location = StringField('Location', validators = [InputRequired()])
    description = TextAreaField("Description", validators = [InputRequired()])
    starting_date = DateField('Starting Date', format('%Y-%m-%d'))
    image_url = StringField('Image URL', validators = [InputRequired()])
    price = FloatField('Price', validators = [InputRequired()])
    submit = SubmitField('Update')
    
class PurchaseForm(FlaskForm):
    quantity = IntegerField('Quantity',validators = [NumberRange(min=0, max=100)])
    payment_method = RadioField('Gender', choices = [('visa','Visa'),('MasterCard','masterCard'), ('cash', 'Cash')])
    submit = SubmitField('Buy Now')


