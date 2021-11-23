import unittest #https://docs.python.org/3/library/unittest.html
from manga_api import *
#Adam Sellwood

class TestMangaApiFunctions(unittest.TestCase):

	def test_manga_genre(self):
		genre_test = manga_by_genre('action')
		self.assertEqual(manga_by_genre(20), 'Sorry that is not a valid input.')
		self.assertTrue(len(genre_test)>0)
		self.assertTrue(genre_test[0]['Image'])

	def test_manga_title(self):
		title_test = manga_by_title('naruto')
		self.assertEqual(manga_by_title(' '), 'Sorry I could not find any manga with the title " ".')
		self.assertTrue(len(title_test)>0)
		self.assertTrue(title_test[0]['Image'])

	def test_manga_recommendations(self):
		recommendation_test = manga_recommendations('naruto')
		self.assertTrue(len(recommendation_test)>0)
		self.assertEqual(manga_recommendations(' '), 'Sorry I could not find any manga with the title " ".')
		self.assertTrue(recommendation_test[0]['Image'])

	def test_manga_mangalist_by_user(self):
		mangalist_test = mangalist_by_user('PimmySwift', 'Reading')
		self.assertEqual(mangalist_test[0], 'Hinamatsuri')
		self.assertTrue(len(mangalist_by_user('PimmySwift', 'Completed'))>0)
		self.assertEqual(mangalist_by_user(' ', 'Reading'), 'Sorry I can not find this profile.')

	def test_top_manga(self):
		top_test = search_top_manga()
		self.assertTrue(len(top_test)>0)
		self.assertTrue(top_test[0]['Image'])

	def test_characters_in_manga(self):
		characters_test = characters_in_manga('naruto')
		self.assertEqual(characters_test[3]['Name'], 'Uzumaki, Naruto')
		self.assertTrue(len(characters_test)>0)
		self.assertTrue(characters_test[0]['Image'])
		self.assertEqual(characters_in_manga(' '), 'Sorry I could not find any manga with the title " ".')

	def test_top_characters_in_manga(self):
		top_characters_test = top_rated_character_manga()
		self.assertTrue(len(top_characters_test)>0)
		self.assertTrue(top_characters_test[0]['Image'])

if __name__ == '__main__':
	#https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/
	#Helped me to understand what __name__ == __main__ does.
	unittest.main()