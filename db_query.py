from db_setup import Subject, Course, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///sqlalchemy_example.db')
Base.metadata.bind = engine

DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

print session.query(Subject).all()

first = session.query(Subject).first()
print first.name
print first.dept_num

print session.query(Course).all()
first = session.query(Course).first()
print first.course_name
print first.subject
