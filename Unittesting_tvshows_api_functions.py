import unittest #https://docs.python.org/3/library/unittest.html
from film_and_tv_shows_api import *
#Adam Sellwood

class TestTVApiFunctions(unittest.TestCase):

	def test_show_by_title(self):
		title_test = show_by_title('The Big Bang Theory')
		self.assertEqual(title_test[0]['Title'], 'The Big Bang Theory')
		self.assertTrue(len(title_test)>0)
		self.assertEqual(type(title_test), list)

	def test_popular_shows(self):
		popular_test = popular_shows()
		self.assertTrue(len(popular_test)>0)
		self.assertEqual(type(popular_test), list)

	def test_top_rated_shows(self):
		top_rated_test = top_rated_shows()
		self.assertTrue(len(top_rated_test)>0)
		self.assertEqual(type(top_rated_test), list)

	def test_recommendations_shows(self):
		recommendations_test = recommendations_shows(1418)
		self.assertTrue(len(recommendations_test)>0)
		self.assertEqual(type(recommendations_test), list)

	def test_similar_shows(self):
		similar_test = similar_shows(1100)
		self.assertTrue(len(similar_test)>0)
		self.assertEqual(type(similar_test), list)

	def test_show_providers(self):
		providers_test = show_providers(1421, 'United Kingdom')
		self.assertEqual(providers_test['flatrate'][0], 'Netflix')
		self.assertEqual(providers_test['buy'][0], 'Apple iTunes')
		self.assertTrue(len(providers_test)>0)
		self.assertEqual(type(providers_test), dict)


if __name__ == '__main__':
	#https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/
	#Helped me to understand what __name__ == __main__ does.
	unittest.main()