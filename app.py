from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

url = 'http://sis.rutgers.edu/soc/'
level = 'U,G'
campus = 'NB'
params = {
	'campus': campus,
	'level': level,
}

@app.route('/')
def home():
	subjects = get_subjects('12015')
	return render_template('index.html', subjects=subjects)

@app.route('/list')
def list():
	dept = request.args['subj']
	courseNum = request.args['courseIndex']
	
	spring = '1'
	fall = '9'
	sems = []
	for i in range(2,5):
		year = '201' + str(i)
		spring_courses = get_courses(dept, spring + year)
		fall_courses = get_courses(dept, fall + year)
		sems.append(spring_courses)
		sems.append(fall_courses)

	#courses = get_courses(dept, '12015')
	return render_template('list.html', semesters=sems, courseNum=courseNum, l=len(sems))

def get_courses(subject, semester):
	subj = {
		'semester':semester,
		'subject': subject
	} 
	subj.update(params)
	resource = '/courses.json'
	
	r = requests.get(url + resource, params=subj, headers=headers())
	if r.status_code == requests.codes.ok:
		print "success!"
		print r.url
		return r.json()

	raise Exception('Invalid request %s: %s' % (r.status_code, r.text))	

def get_subjects(semester):	
	sem = {'semester':semester}
	sem.update(params)
	resource = '/subjects.json'

	r = requests.get(url + resource, params=sem, headers=headers())
	if r.status_code == requests.codes.ok:
		print "success!"
		print r.url
		return r.json()

	raise Exception('Invalid request %s: %s' % (r.status_code, r.text))

def headers():
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.60 Safari/537.1',
	}
	return headers


if __name__ == '__main__':
	app.run('0.0.0.0',port=4000,debug=True)
