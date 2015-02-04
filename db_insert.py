from app import get_subjects, get_courses
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Subject, Course, Base

engine = create_engine('sqlite:///sqlalchemy_example.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

subjList = get_subjects('12015')

for subj in subjList:
	new_subj = Subject(id=subj['code'], dept_num=subj['code'], name=subj['description'])
	session.add(new_subj)

courseList = get_courses('198', '12015')

for course in courseList:
	sub = None
	for sub_search in session.query(Subject).\
			filter(Subject.dept_num=='198'):
		sub = sub_search
	new_course = Course(id=course['courseNumber'], course_num=course['courseNumber'], course_name=course['title'], dept_id='198', subject=sub)
	
session.commit()	

