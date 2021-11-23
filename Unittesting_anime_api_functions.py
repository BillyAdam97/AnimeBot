import unittest #https://docs.python.org/3/library/unittest.html
from anime_api import *
#Adam Sellwood

class TestAnimeApiFunctions(unittest.TestCase):

	def test_anime_genre(self):
		genre_test = anime_by_genre('action')
		self.assertEqual(anime_by_genre(11), 'Sorry that is not a valid input.')
		self.assertTrue(len(genre_test)>0)
		self.assertTrue(genre_test[0]['Image'])

	def test_anime_title(self):
		title_test = anime_by_title('naruto')
		self.assertEqual(anime_by_title(' '), 'Sorry I could not find any anime with the title " ".')
		self.assertTrue(len(title_test)>0)
		self.assertTrue(title_test[0]['Image'])

	def test_anime_recommendations(self):
		recommendations_test = anime_recommendations('naruto')
		self.assertEqual(anime_recommendations(' '), 'Sorry I could not find any anime with the title " ".')
		self.assertTrue(len(recommendations_test)>0)
		self.assertTrue(recommendations_test[0]['Image'])

	def test_anime_animelist_by_user(self):
		animelist_test = animelist_by_user('PimmySwift', 'Watching')
		self.assertEqual(animelist_test[0], 'Boku wa Tomodachi ga Sukunai')
		self.assertTrue(len(animelist_by_user('PimmySwift', 'Dropped'))>0)
		self.assertEqual(animelist_by_user(' ', 'Watching'), 'Sorry I can not find this profile.')

	def test_anime_by_season(self):
		self.assertEqual(anime_by_season(1000, 'summer'), 'You must enter a year between 1917 and 2021.')
		self.assertEqual(anime_by_season(1919, 'summer'), 'There was no anime released in this season that year.')
		self.assertTrue(len(anime_by_season(2020, 'summer'))>0)

	def test_top_anime(self):
		top_test = search_top_anime()
		self.assertEqual(top_test[0]['Title'], 'Fullmetal Alchemist: Brotherhood')
		self.assertTrue(len(top_test)>0)
		self.assertTrue(top_test[0]['Image'])

	def test_characters_in_anime(self):
		characters_test = characters_in_anime('naruto')
		self.assertTrue(len(characters_test)>0)
		self.assertEqual(characters_in_anime(' '), 'Sorry I could not find any anime with the title " ".')
		self.assertTrue(characters_test[0]['Image'])

	def test_top_characters_in_anime(self):
		top_characters_test = top_rated_character_anime()
		self.assertTrue(len(top_characters_test)>0)
		self.assertTrue(top_characters_test[0]['Image'])

if __name__ == '__main__':
	#https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/
	#Helped me to understand what __name__ == __main__ does.
	unittest.main()