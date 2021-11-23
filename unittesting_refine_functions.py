import unittest 
from jareds_notepad import *
#Hoi Yuen Unit testing
class TestAnimeRefine(unittest.TestCase):

	def test_anime_genre_function(self): 
		func_test = func_anime_genre('action', 'Title') # Storing the imported function as a varibale to make it efficient when running the test 
		self.assertEqual(func_test[0],'Shingeki no Kyojin') # Using self.assertTrue to see if the manga title is in the list 

	def test_anime_title_function(self): # Function name states anime to clealy state the difference of manga and anime functions
		func_test2 = func_anime_title('naruto', 'Title', 'score')
		self.assertEqual(func_test2[0],'Naruto: Shippuuden')
		self.assertEqual(func_test2[2],'The Last: Naruto the Movie')
		
	def test_anime_reccomendation_function(self):
		func_test3 = func_anime_recommendation('One Punch Man', 'Title') # Function tests if one anime is inputted, does the function recommend a similar one
		self.assertEqual(func_test3[0], 'Mob Psycho Mini')

	def test_anime_top_function(self):
		func_test4 = func_top_anime('Title', 'Rank')
		self.assertEqual(func_test4[0], 'Fullmetal Alchemist: Brotherhood', 1) # Using the self.assertEqual to see if the anime title is in the correct order for top ranking

	def test_anime_character_function(self):
		func_test5 = func_character_in_anime('One Piece', 'Name')
		self.assertEqual(func_test5[0], 'El Drago')

	def test_anime_top_rated_character(self):
		func_test6 = func_top_rated_character_anime('Title')
		self.assertEqual(func_test6[0], 'Lamperouge, Lelouch')

if __name__ == '__main__':
	unittest.main()

