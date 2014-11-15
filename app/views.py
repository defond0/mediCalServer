from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, models
from .forms import pillForm, prescriptionForm, addPillsForm #, loginForm

@app.route('/')
@app.route('/index')
def index():
	pills = models.Pill.query.all()
	prescriptions = models.Prescription.query.all()
	joins = models.PPjoin.query.all()
	print joins 
	return render_template("index.html", pills= pills , prescriptions = prescriptions, joins= joins, title='Medical Pillar')

@app.route('/newpill', methods=['GET','POST'])
def newPill():
	form = pillForm()
	if form.validate_on_submit():
		print("fling")
		p = models.Pill.createPill(form.tube.data, form.name.data, form.dose.data, form.load.data)
		flash('Creating Pill "%s", in tube %s, of dose %s  with %s load' % (p.name, p.tube, p.dose, p.load))
	return render_template("newPill.html", form=form, title='Create Pill')


@app.route('/newprescription', methods=['GET','POST'])
def newPrescription():
	form = prescriptionForm()
	if form.validate_on_submit():
		print("ding")
		pr = models.Prescription.createPrescription(form.patient.data, form.rfid.data)
	 	flash('Creating Prescription for "%s" with rfid %s' %(pr.patient, pr.rfid))
	return render_template('newPrescription.html', form=form, title='Create Prescription')

@app.route('/addpills', methods=['GET','POST'])
def addPills():
	form = addPillsForm()
	print form.errors
	print form.pills.data
	print form.prescriptions.data
	print form.times.data
	# if form.validate_on_submit():
	print("ping")
	j=models.PPjoin.createJoin(form.pills.data, form.prescriptions.data, form.times.data)
	flash('Adding pill "%s" to perscription %s at time %s'  %(j.pillId, j.prescriptionId, j.times))
	return render_template('addPills.html', form=form, title='Add Pills to Perscriptions')

