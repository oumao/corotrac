from flask_login import UserMixin
from coroapp import db


class User(db.Model, UserMixin):

	__tablename__ = 'user'

	id = db.Column(db.Integer, primary_key=True)
	first = db.Column(db.String(80), nullable=False)
	last = db.Column(db.String(80), nullable=False)
	email = db.Column(db.String(80), unique=True, nullable=False)
	password = db.Column(db.String(80), nullable=False)
	is_admin = db.Column(db.Boolean, default=False)

	__mapper_args__= {
		'polymorphic_on': is_admin,
		'polymorphic_identity' : 'user'

	}


	def __repr__(self):
		return "<User: {0}, {1}, {2}>"
				.format(self.first, self.last, self.email)

class Doctor(User, db.Model):
	 
	__mapper_args__ = {
		'polymorphic_identity' : 'doctor'
	}
	s_num = db.Column(db.String(20), nullable=False)
	special = db.Column(db.String(50))

	def __repr__(self):
		return "<Doctor: {0}, {1}>"
				.format(self.s_num, self.special)

	

	
class Patient(db.Model):

	__tablename__ = 'patient'

	id = db.Column(db.Integer, primary_key=True)
	first = db.Column(db.String(80), nullable=False)
	last = db.Column(db.String(80), nullable=False)
	age = db.Column(db.Integer, nullable=False)
	marriage = db.Column(db.String, nullable=False)
	next_kin = db.Column(db.String(80), nullable=False)
	kin_tel = db.Column(db.Integer, nullable=False)
	kin_rship = db.Column(db.String(20), nullable=False)
	natid = db.Column(db.Integer, nullable=False, unique=True)
	phone = db.Column(db.Integer, nullable=False)
	reside = db.Column(db.String(80), nullable=False)
	sub_county = db.Column(db.String(80), nullable=False)
	facil_id = db.Column(db.Integer, db.ForeignKey('Facility.mfl'))

	def __repr__(self):
		return "<Patient: {}, {}, {}, {}, {},\
						{}, {}, {}, {}, {}, {}>"
				.format(self.first, self.last, self.age,
				self.marriage, self.next_kin, self.kin_tel,
				self.kin_rship, self.natid, self.phone,
				self.reside, self.sub_county)


class Facility(db.Model):

	__tablename__ = 'facility'

	mfl = db.Column(db.Integer, primary_key=True)
	facil_name = db.Column(db.String(100), nullable=False)
	location = db.Column(db.String(100), nullable=False)
	patient = db.Relationship('Patient', backref='patient', lazy=True)


class Case(db.Model):

	""" This table contains the information about covid 19 """

	__tablename__ = 'case'

	id = db.Column(db.Integer, primary_key=True)
	date = db.Column(db.date, nullable=False)
	is_screened = db.Column(db.Boolean, nullable=False)
	conf_pos = db.Column(db.Boolean, nullable=False)  # confirmed positive

	__mapper_args__ = {
		'polymorphic_on' : conf_pos,
		'polymorphic_identity' : 'case' 
	}


class UnderCondition(Case, db.Model):

	""" This table contains the information about underlying condition"""

	__tablename__ = 'undercondition'

	__mapper_args__ = {
		'polymorphic_identity' = 'undercondition'
	}
	

