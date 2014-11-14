from flask.ext.wtf import Form
from wtforms import StringField, SelectField, DateTimeField
from wtforms.validators import DataRequired
from app import app, models 

	
class pillForm(Form):
	tube = StringField('tube', validators=[DataRequired()])
	name = StringField('pname', validators=[DataRequired()])
	dose = StringField('dose', validators=[DataRequired()])
	load = StringField('load', validators=[DataRequired()])

class prescriptionForm(Form):
	patient = StringField('patient', validators=[DataRequired()])
	rfid = SelectField('rfid', validators=[DataRequired()], choices=[('1','1'),('2','2')])

class addPillsForm(Form):
	perscriptions = SelectField('perscripts', choices = [])
	pills = SelectField('pills', choices =[])
	time = DateTimeField('times', validators=[DataRequired()], format ='%H:%M')

	def loadSpinners(self):
		pill = models.Pill.query.all()
		perscripts = models.Prescription.query.all()
		self.perscriptions.choices = [(p.id, p.patient) for p in perscripts]
		self.pills.choices = [(p.id, p.name) for p in pill]


