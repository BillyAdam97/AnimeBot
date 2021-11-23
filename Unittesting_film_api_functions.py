import unittest #https://docs.python.org/3/library/unittest.html
from film_and_tv_shows_api import *
#Adam Sellwood

class TestFilmApiFunctions(unittest.TestCase):

	def test_film_title(self):
		title_test = film_by_title('Venom')
		self.assertTrue(len(title_test)>0)
		self.assertEqual(type(title_test), list)

	def test_film_info(self):
		info_test = film_info(335983)
		self.assertEqual(info_test['Score'], 6.8)
		self.assertTrue(len(info_test)>0)
		self.assertEqual(type(info_test), dict)

	def test_popular_films(self):
		popular_test = popular_films()
		self.assertTrue(len(popular_test)>0)
		self.assertEqual(type(popular_test), list)

	def test_recommendations_film(self):
		recommendations_test = recommendations_film(24428)
		self.assertTrue(len(recommendations_test)>0)
		self.assertEqual(type(recommendations_test), list)

	def test_silmilar_films(self):
		similar_test = similar_films(24428)
		self.assertTrue(len(similar_test)>0)
		self.assertEqual(type(similar_test), list)

	def test_top_rated_films(self):
		top_rated_test = top_rated_films()
		self.assertTrue(len(top_rated_test)>0)
		self.assertEqual(type(top_rated_test), list)

if __name__ == '__main__':
	#https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/
	#Helped me to understand what __name__ == __main__ does.
	unittest.main()