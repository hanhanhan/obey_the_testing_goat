from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from lists.views import home_page
from django.template.loader import render_to_string


class HomePageTest(TestCase):

	# can remove, implicitly tested
	# def test_root_url_resolves_to_home_page(self):
	# 	found = resolve('/')
	# 	self.assertEqual(found.func, home_page)

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		html = response.content.decode('utf8')
		self.assertTrue(html.startswith('<html>'))
		self.assertIn('<title>To-Do Lists</title>', html)
		self.assertTrue(html.endswith('</html>'))
		# django test - same as function below
		self.assertTemplateUsed(response, 'home.html')

	def test_home_page_returns_correct_html_page(self):
		request = HttpRequest()
		response = home_page(request)
		html = response.content.decode('utf8')
		expected_html = render_to_string('home.html')
		self.assertEqual(html, expected_html)





