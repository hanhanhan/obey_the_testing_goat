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
		submitted_new_item = 'A new list item'
		response = self.client.post('/', data={'item_text': submitted_new_item})
		
		self.assertEqual(Item.objects.count(), 1)
		new_item = Item.objects.first()
		self.assertEqual(new_item.text, submitted_new_item)


	def test_redirects_after_POST(self):
		submitted_new_item = 'A new list item'
		response = self.client.post('/', data={'item_text': submitted_new_item})	
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/')		


	def test_only_saves_nonempty_items(self):
		self.client.get('/')
		self.assertEqual(Item.objects.count(), 0)


	def test_displays_all_list_items(self):
		# setup
		Item.objects.create(text = 'itemey 1')
		Item.objects.create(text = 'itemey 2')
		# call code being tested
		response = self.client.get('/')
		# test
		# doesn't work other way around! assert 1st argument in 2nd.
		self.assertIn('itemey 1', response.content.decode(), )
		self.assertIn('itemey 2', response.content.decode(), )


class ItemModelTest(TestCase):


	def test_saving_and_retrieving_items(self):
		first_item = Item()
		first_item.text = 'The first ever list item'
		first_item.save()

		second_item = Item()
		second_item.text = 'The second item.'
		second_item.save()

		saved_items = Item.objects.all()
		self.assertEqual(saved_items.count(), 2)

		self.assertEqual(first_item, saved_items[0])
		self.assertEqual(second_item, saved_items[1])
