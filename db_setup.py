import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine

Base = declarative_base()

class Subject(Base):
	__tablename__ = 'subject'
	id = Column(Integer, primary_key=True)
	dept_num = Column(String(3), nullable=False)
	name = Column(String(250), nullable=False)

	def __repr__(self):
		return "<Subject(name='%s', dept_num='%s')>" % (self.name, self.dept_num)

class Course(Base):
	__tablename__ = 'course'
	id = Column(Integer, primary_key=True)
	course_num = Column(String(3), nullable=False)
	course_name = Column(String(250), nullable=False)
	dept_id = Column(Integer, ForeignKey('subject.id'))
	subject = relationship("Subject", backref=backref('course',order_by=id))

	def __repr__(self):
		return "<Course(course_name='%s')>" % self.course_name

engine = create_engine('sqlite:///sqlalchemy_example.db')
Base.metadata.create_all(engine)
