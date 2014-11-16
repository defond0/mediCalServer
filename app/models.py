from app import db


class Pill(db.Model):
	__tablename__="pill"
	id = db.Column(db.Integer, primary_key = True)
	tube = db.Column(db.String(64), index = True)
	name = db.Column(db.String(64), index = True)
	dose = db.Column(db.String(64), index = True)
	load = db.Column(db.String(64), index = True)

	@staticmethod
	def createPill(tube, name, dose, load):
		p = Pill(tube=tube,name=name,dose= dose, load=load)
		db.session.add(p)
		db.session.commit()
		return p

	@staticmethod
	def deletePill(id):
		pills = Pill.query.filter_by(id=id).all()
		for p in pills:
			db.session.delete(p)
		db.session.commit()
		return pills 

	@property
	def serialize(self):
		return {
           'id': self.id,
           'tube': self.tube,
           'name': self.name,
           'dose': self.dose,
           'load': self.load
       }	
	

class Prescription(db.Model):
	__tablename__="prescription"
	id = db.Column(db.Integer, primary_key = True)
	patient = db.Column(db.String(64), index = True)
	rfid = db.Column(db.LargeBinary)
	
	@staticmethod
	def createPrescription(patient, rfid):
		rfids={'1':bytes([0x1A, 0xE2, 0x41,0xD9]),'2':bytes([0x04, 0x92, 0x6E, 0x7A, 0x7A, 0x31, 0x80])}
		p = Prescription(patient=patient,rfid = rfids[rfid])
		db.session.add(p)
		db.session.commit()
		return p

	@staticmethod
	def deletePrescription(id):
		prescriptions = Prescription.query.filter_by(id=id).all()
		for p in prescriptions:
			db.session.delete(p)
		db.session.commit()
		return prescriptions  

	@property
	def serialize(self):
		return {
           'id': self.id,
           'patient': self.patient,
           'rfid': self.rfid
       }	

class PPjoin(db.Model):
	__tablename__="join"
	id = db.Column(db.Integer, primary_key = True)
	pillId = db.Column(db.Integer, db.ForeignKey('prescription.id'))
	prescriptionId = db.Column(db.Integer, db.ForeignKey('prescription.id'))
	times = db.Column(db.String(120), index = True)

	@staticmethod
	def createJoin(pillId, prescriptionId, times ):
		j = PPjoin(pillId=pillId, prescriptionId=prescriptionId, times=times)
		db.session.add(j)
		db.session.commit()
		return j

	@staticmethod
	def deleteJoin(id):
		joins = PPjoin.query.filter_by(id=id).all()
		for j in joins:
			db.session.delete(j)
		db.session.commit()
		return joins  

	@property
	def serialize(self):
		return {
           'id': self.id,
           'pillId': self.pillId,
           'prescriptionId': self.prescriptionId,
           'times': self.times
       }	
	 


