from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from lists.views import home_page
from django.template.loader import render_to_string


class HomePageTest(TestCase):


	def test_home_page_returns_correct_html(self):
		response = self.client.get('/')
		html = response.content.decode('utf8')
		self.assertTrue(html.startswith('<html>'))
		self.assertIn('<title>To-Do Lists</title>', html)
		self.assertTrue(html.endswith('</html>'))
		# django test - same as function below
		self.assertTemplateUsed(response, 'home.html')

	# this version of test doesn't work with csrf token
	# def test_home_page_returns_correct_html_page(self):
	# 	request = HttpRequest()
	# 	response = home_page(request)
	# 	html = response.content.decode('utf8')
	# 	expected_html = render_to_string('home.html')
	# 	self.assertEqual(html, expected_html)


	def test_uses_home_template(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'home.html')


	def test_can_save_a_POST_request(self):
		response = self.client.post('/', data={'item_text': 'A new list item'})
		self.assertIn('A new list item', response.content.decode())
		self.assertTemplateUsed(response, 'home.html')

