import requests

class SoC:
	def __init__(self,semester):
		self.url = 'http://sis.rutgers.edu/soc'
		campus = 'NB'
		level = 'U,G'
		self.params = {
			'campus': campus,
			'semester': semester,
			'level': level
		}
		
		self.headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.60 Safari/537.1',
        	}
		
	def query(self,resource, params):
		params.update(self.params)
		
		r = requests.get(self.url + resource, params=params, headers=self.headers)
		if r.status_code == requests.codes.ok:
			print "Success!"
			print r.url
			return r.json

		raise Exception('Invalid request %s: %s' % (r.status_code, r.text))

	def get_subjects(self, **kwargs):
		return self.query('/subjects.json', params=kwargs)

	def get_courses(self,subject):
		return self.query('/courses.json', params={'subject': subject})

if __name__ == '__main__':
	soc = SoC()
	print soc.get_courses(subject=198)
	import pdb; pdb.set_trace()
