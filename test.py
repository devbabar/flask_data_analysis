from main_app import app
import unittest

class FlaskTestCase(unittest.TestCase):

	#Ensure setup correctly
	def test_index_route(self):
		tester = app.test_client(self)
		response = tester.get('/', content_type = 'html/text')
		self.assertEqual(response.status_code, 200)

	def test_regular_search_route(self):
		tester = app.test_client(self)
		response = tester.post('/regular_search', data=dict(location="Arroyo Grande"), follow_redirects=True)
		self.assertIn(b'Arroyo Grande',response.data)

	# Using invalid location and response should be "Sorry No Result Found"
	def test_advance_search_route(self):
		tester = app.test_client(self)
		response = tester.post('/search', data=dict(location="Grande", bedrooms=3), follow_redirects=True)
		self.assertIn(b'Sorry No Result Found',response.data)

if __name__ == '__main__':
	unittest.main()
