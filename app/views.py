from flask import Flask, render_template, flash, redirect, session, url_for, request, g, json, jsonify
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, models
from .forms import pillForm, prescriptionForm, addPillsForm #, loginForm

@app.route('/')
@app.route('/index')
def index():
	pills = models.Pill.query.all()
	prescriptions = models.Prescription.query.all()
	joins = models.PPjoin.query.all()
	return render_template("index.html", pills= pills , prescriptions = prescriptions, joins= joins, title='Medical Pillar')

@app.route('/newpill', methods=['GET','POST'])
def newPill():
	form = pillForm()
	if form.validate_on_submit():
		p = models.Pill.createPill(form.tube.data, form.name.data, form.dose.data, form.load.data)
		flash('Creating Pill "%s", in tube %s, of dose %s  with %s load' % (p.name, p.tube, p.dose, p.load))
	return render_template("newPill.html", form=form, title='Create Pill')

@app.route('/newprescription', methods=['GET','POST'])
def newPrescription():
	form = prescriptionForm()
	request.content_type
	if form.validate_on_submit():
		pr = models.Prescription.createPrescription(form.patient.data, form.rfid.data)
	 	flash('Creating Prescription for "%s" with rfid %s' %(pr.patient, pr.rfid))
	return render_template('newPrescription.html', form=form, title='Create Prescription')

@app.route('/addpills', methods=['GET','POST'])
def addPills():
	form = addPillsForm()
	j=models.PPjoin.createJoin(form.pills.data, form.prescriptions.data, form.times.data)
	flash('Adding pill "%s" to prescription %s at time %s'  %(j.pillId, j.prescriptionId, j.times))
	return render_template('addPills.html', form=form, title='Add Pills to Perscriptions')

@app.route('/api/getallpills', methods=['GET','POST'])
def apiGetAllPills():
	pills = models.Pill.query.all()		
	return jsonify(pill_list=[ p.serialize for p in pills])

@app.route('/api/getallprescriptions', methods=['GET','POST'])
def apiGetAllPrescriptions():
	prescriptions = models.Prescription.query.all()		
	return jsonify(prescription_list=[ p.serialize for p in prescriptions])

@app.route('/api/getalljoins', methods=['GET','POST'])
def apiGetAllJoins():
	joins = models.PPjoin.query.all()		
	return jsonify(join_list=[ j.serialize for j in joins])

@app.route('/api/newpill', methods=['GET','POST'])
def apiNewPill():
	args = request.args
	p = models.Pill.createPill(args['tube'],args['name'],args['dose'],args['load'])
	return jsonify(new_pill_list=[p.serialize])

@app.route('/api/newprescription', methods=['GET','POST'])
def apiNewPrescription():
	args = request.args
	p = models.Prescription.createPrescription(args['patient'],args['rfid'])
	return jsonify(new_prescription_list=[p.serialize])

@app.route('/api/newjoin', methods=['GET','POST'])
def apiNewJoin():
	args = request.args
	j = models.PPjoin.createJoin(args['pillId'],args['prescriptionId'],args['times'])
	return jsonify(new_join_list=[j.serialize])

@app.route('/api/deletepill', methods=['GET','POST'])
def apiDeletePill():
	args = request.args
	deleted_pills = models.Pill.deletePill(args['id'])
	return jsonify(deleted_pills_list=[p.serialize for p in deleted_pills])

@app.route('/api/deleteprescription', methods=['GET','POST'])
def apiDeletePrescription():
	args = request.args
	deleted_prescriptions = models.Prescription.deletePrescription(args['id'])
	return jsonify(deleted_prescriptions_list=[p.serialize for p in deleted_prescriptions])

@app.route('/api/deletejoin', methods=['GET','POST'])
def apiDeletejoin():
	args = request.args
	deleted_joins = models.PPjoin.deleteJoin(args['id'])
	return jsonify(deleted_join_list=[p.serialize for p in deleted_joins])
