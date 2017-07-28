from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class NewVisitorTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])


	def tearDown(self):
		self.browser.quit()


	def test_can_start_a_list_and_retrieve_it_later(self):
		self.browser.get(self.live_server_url)
		
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)
		
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

		todo_entry = 'Buy peacock feathers'
		inputbox.send_keys(todo_entry)
		inputbox.send_keys(Keys.ENTER)
		
		time.sleep(5)
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)
		
		time.sleep(5)
		self.check_for_row_in_list_table('1. Buy peacock feathers')
		self.check_for_row_in_list_table('2. Use peacock feathers to make a fly')

		# self.assertIn('1. Buy peacock feathers',  [row.text for row in rows])
		self.fail('Finish the test!')





