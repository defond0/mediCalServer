from app import db

class Pill(db.Model):
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

class Prescription(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	patient = db.Column(db.String(64), index = True)
	rfid = db.Column(db.LargeBinary)
	
	@staticmethod
	def createPrescription(patient, rfid):
		rfids={'1':bytes([0x1A, 0xE2, 0x41,0xD9]),'2':bytes([0x04, 0x92, 0x6E, 0x7A, 0x7A, 0x31, 0x80])}
		p = Prescription(patient=patient,rfid = rfids[rfid])
		db.session.add(p)
		db.session.commit()		



class PPjoin(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	pillId = db.Column(db.Integer, db.ForeignKey('prescription.id'))
	prescriptioinId = db.Column(db.Integer, db.ForeignKey('prescription.id'))
	times = db.Column(db.String(120), index = True)

	@staticmethod
	def createJoin(pillid, perscriptionId, times):
		j = PPjoin(pillid=pillid, perscriptionId=perscriptionId, times=times)
		db.session.add(j)
		db.session.commit()

	
