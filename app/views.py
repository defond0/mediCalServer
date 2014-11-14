from flask import render_template, flash, redirect
from app import app, models
from .forms import pillForm, prescriptionForm, addPillsForm
@app.route('/')

@app.route('/index')
def index():
	pills = models.Pill.query.all()
	prescriptions = models.Prescription.query.all()
	return render_template("index.html", pills= pills , prescriptions = prescriptions)

@app.route('/newpill', methods=['GET','POST'])
def newPill():
	form = pillForm()
	if form.validate_on_submit():
		flash('Creating Pill "%s", tube %s' %
               (form.name.data, str(form.tube.data)))
		models.Pill.createPill(form.tube.data, form.name.data, form.dose.data, form.tube.data)
	return render_template('newPill.html', form=form)

@app.route('/newprescription', methods=['GET','POST'])
def newPrescription():
	form = prescriptionForm()
	if form.validate_on_submit():
	 	flash('Creating Prescription for "%s"' %
	 		(form.patient.data))
	 	models.Prescription.createPrescription(form.patient.data, form.rfid.data)
	return render_template('newPrescription.html', form=form)

@app.route('/addpills', methods=['GET','POST'])
def addPills():
	form = addPillsForm()
	form.loadSpinners()
	if form.validate_on_submit():
		flash('Adding pill "%s" to perscription %s' %
			(form.pills.data, form.perscriptions.data))
		models.PPjoin.createPrescription(form.pills.data, form.prescriptions.data, form.times.data)
	return render_template('addPills.html', form=form)