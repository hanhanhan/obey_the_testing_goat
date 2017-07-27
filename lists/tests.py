from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from lists.views import home_page
from lists.models import Item
from django.template.loader import render_to_string


class HomePageTest(TestCase):

	def test_home_page_returns_correct_html(self):
		response = self.client.get('/')
		html = response.content.decode('utf8')
		self.assertTrue(html.startswith('<html>'))
		self.assertIn('<title>To-Do Lists</title>', html)
		self.assertTrue(html.endswith('</html>'))
		self.assertTemplateUsed(response, 'home.html')


	def test_uses_home_template(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'home.html')


	def test_can_save_a_POST_request(self):
		response = self.client.post('/', data={'item_text': 'A new list item'})
		self.assertIn('A new list item', response.content.decode())
		self.assertTemplateUsed(response, 'home.html')


class ItemModelTest(TestCase):


	def test_saving_and_retrieving_items(self):
		first_item = Item()
		first_item.text = 'The first ever list item'
		first_item.save()

		second_item = Item()
		second_item.text = 'The second item.'
		second_item.save()

		saved_items = Items.objects.all()
		self.assertEqual(saved_items.count(), 2)

		self.assertEqual(first_item, saved_items[0])
		self.assertEqual(second_item, saved_items[1])
