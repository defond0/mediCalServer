from flask.ext.wtf import Form
from wtforms import StringField, SelectField, DateTimeField
from wtforms.validators import DataRequired
from app import app, models 

class SelectPrescriptions(SelectField):
	def __init__(self, *args, **kwargs):
		super(SelectPrescriptions, self).__init__(*args, **kwargs)
		self.choices=[(prescription.id,prescription.patient)for prescription in models.Prescription.query.all()] 

class SelectPills(SelectField):
	def __init__(self, *args, **kwargs):
		super(SelectPills, self).__init__(*args, **kwargs)
		self.choices=[(pill.id,pill.name)for pill in models.Pill.query.all()] 
	
class pillForm(Form):
	tube = StringField('tube', validators=[DataRequired()])
	name = StringField('pname', validators=[DataRequired()])
	dose = StringField('dose', validators=[DataRequired()])
	load = StringField('load', validators=[DataRequired()])


class prescriptionForm(Form):
	patient = StringField('patient', validators=[DataRequired()])
	rfid = SelectField('rfid', validators=[DataRequired()], choices=[('1','1'),('2','2')])

class addPillsForm(Form):
	prescriptions = SelectPrescriptions('prescriptions', validators=[DataRequired()])
	pills = SelectPills('pills', validators=[DataRequired()])
	times = StringField('times', validators=[DataRequired()])

	

