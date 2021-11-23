import requests #External Library - https://docs.python-requests.org/en/latest/user/quickstart/#make-a-request
import json #Standard Library - https://docs.python.org/3/library/json.html
#Adam Sellwood
#https://www.themoviedb.org/documentation/api - api documentation

key = '2adfa4110449009d9f572ac362e8be05'

countries = {
	'Argentina': 'AR', 'Austria': 'AT', 'Australia': 'AU', 'Belgium': 'BE', 'Brazil': 'BR', 'Canada': 'CA', 'Switzerland': 'CH', 'Czech Republic': 'CZ',
	'Germany': 'DE', 'Denmark': 'DK', 'Estonia': 'EE', 'Spain': 'ES', 'Finland': 'FI', 'France': 'FR', 'United Kingdom': 'GB', 'Hungary': 'HU',
	'Indonesia': 'ID', 'Ireland': 'IE', 'India': 'IN', 'Italy': 'IT', 'Japan': 'JP', 'South Korea': 'KR', 'Lithuania': 'LT', 'Mexico': 'MX', 'Netherlands': 'NL',
	'Norway': 'NO', 'New Zealand': 'NZ', 'Philippines': 'PH', 'Poland': 'PL', 'Portugal': 'PL', 'Russia': 'RU', 'Sweden': 'SE', 'Turkey': 'TR', 'United States of America': 'US',
	'South Africa': 'ZA'
}

def film_by_title(title):
	'''Stored in list of dictionaries.
	Function takes in a string as an arguement.'''
	response = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key={key}&language=en-US&query={title}').text
	response_dict = json.loads(response)
	film_list = response_dict['results']
	result_list = []
	for info in film_list:
		result_dict = {}
		result_dict['Title'] = info['original_title']
		result_dict['Release Date'] = info['release_date']
		result_dict['id'] = info['id']
		result_dict['Score'] = info['vote_average']
		result_list.append(result_dict)
	return result_list

def film_info(idnum):
	'''Stored in a dictionary.
	Function takes in an integer as an arguement.'''
	response = requests.get(f'https://api.themoviedb.org/3/movie/{idnum}?api_key={key}&language=en-US').text
	response_dict = json.loads(response)
	result_list = []
	genres_list = []
	info_dict = {}
	info_dict['Synopsis'] = response_dict['overview']
	for info in response_dict['genres']:
		genres_list.append(info['name'])
	info_dict['Genres'] = genres_list
	info_dict['Release Date'] = response_dict['release_date']
	info_dict['Budget'] = response_dict['budget']
	info_dict['Revenue'] = response_dict['revenue']
	info_dict['Score'] = response_dict['vote_average']
	return info_dict

def popular_films():
	'''Data stored in dictionaires within a list.
	No arguements required.'''
	response = requests.get(f'https://api.themoviedb.org/3/movie/popular?api_key={key}&language=en-US').text
	response_dict = json.loads(response)
	film_list = response_dict['results']
	result_list = []
	for info in film_list:
		result_dict = {}
		result_dict['Title'] = info['original_title']
		result_dict['Score'] = info['vote_average']
		result_dict['id'] = info['id']
		result_list.append(result_dict)
	return result_list

def recommendations_film(idnum):
	'''Data stored in a list.
	Function takes in an integer as an arguement.'''
	response = requests.get(f'https://api.themoviedb.org/3/movie/{idnum}/recommendations?api_key={key}&language=en-US').text
	response_dict = json.loads(response)
	recommended = response_dict['results']
	result_list = []
	for info in recommended:
		result_list.append(info['title'])
	return result_list

def similar_films(idnum):
	'''Data stored in dictionaires within a list.
	Function takes in an integer as an arguement.'''
	response = requests.get(f'https://api.themoviedb.org/3/movie/{idnum}/similar?api_key={key}&language=en-US').text
	response_dict = json.loads(response)
	similar = response_dict['results']
	result_list = []
	for info in similar:
		result_dict = {}
		result_dict['Title'] = info['title']
		result_dict['id'] = info['id']
		result_dict['Score'] = info['vote_average']
		result_dict['Synopsis'] = info['overview']
		result_list.append(result_dict)
	return result_list

def top_rated_films():
	'''Data stored in dictionaires within a list.
	No required arguements.'''
	response = requests.get(f'https://api.themoviedb.org/3/movie/top_rated?api_key={key}&language=en-US').text
	response_dict = json.loads(response)
	top_rated = response_dict['results']
	result_list = []
	for info in top_rated:
		result_dict = {}
		result_dict['Title'] = info['original_title']
		result_dict['id'] = info['id']
		result_dict['Score'] = info['vote_average']
		result_dict['Synopsis'] = info['overview']
		result_list.append(result_dict)
	return result_list

################################################################################################################################################################################################################################
################################################################################################################################################################################################################################

def show_by_title(title):
	'''Data stored in dictionaires within a list.
	Function takes in a string as an arguement.'''
	response = requests.get(f'https://api.themoviedb.org/3/search/tv?api_key={key}&language=en-US&query={title}').text
	response_dict = json.loads(response)
	shows_list = response_dict['results']
	result_list = []
	for info in shows_list:
		result_dict = {}
		result_dict['Title'] = info['name']
		result_dict['id'] = info['id']
		result_dict['Synopsis'] = info['overview']
		result_dict['Score'] = info['vote_average']
		result_list.append(result_dict)
	return result_list

def popular_shows():
	'''Data stored in dictionaires within a list.
	No arguements required.'''
	response = requests.get(f'https://api.themoviedb.org/3/tv/popular?api_key={key}&language=en-US').text
	response_dict = json.loads(response)
	shows_list = response_dict['results']
	result_list = []
	for info in shows_list:
		result_dict = {}
		result_dict['Title'] = info['name']
		result_dict['id'] = info['id']
		result_dict['Synopsis'] = info['overview']
		result_dict['Score'] = info['vote_average']
		result_list.append(result_dict)
	return result_list

def top_rated_shows():
	'''Data stored in dictionaires within a list.
	No arguements required.'''
	response = requests.get(f'https://api.themoviedb.org/3/tv/top_rated?api_key={key}&language=en-US').text
	response_dict = json.loads(response)
	shows_list = response_dict['results']
	result_list = []
	for info in shows_list:
		result_dict = {}
		result_dict['Title'] = info['name']
		result_dict['id'] = info['id']
		result_dict['Synopsis'] = info['overview']
		result_dict['Score'] = info['vote_average']
		result_list.append(result_dict)
	return result_list

def recommendations_shows(idnum):
	'''Data stored within a list.
	Function takes an integer as an arguement.'''
	response = requests.get(f'https://api.themoviedb.org/3/tv/{idnum}/recommendations?api_key={key}&language=en-US').text
	response_dict = json.loads(response)
	recommend = response_dict['results']
	result_list = []
	for info in recommend:
		result_list.append(info['name'])
	return result_list

def similar_shows(idnum):
	'''Data stored in dictionaires within a list.
	Function takes an integer as an arguement.'''
	response = requests.get(f'https://api.themoviedb.org/3/tv/{idnum}/similar?api_key={key}&language=en-US').text
	response_dict = json.loads(response)
	similar = response_dict['results']
	result_list = []
	for info in similar:
		result_dict = {}
		result_dict['Title'] = info['name']
		result_dict['id'] = info['id']
		result_dict['Synopsis'] = info['overview']
		result_dict['Score'] = info['vote_average']
		result_list.append(result_dict)
	return result_list

def show_providers(idnum, country):
	'''Data stored in lists within a dictionary.
	Function takes an integer and a string as an arguement.'''
	country_code = countries[country]
	response = requests.get(f'https://api.themoviedb.org/3/tv/{idnum}/watch/providers?api_key={key}').text
	response_dict = json.loads(response)
	providers = response_dict['results'][country_code]
	result_dict = {}
	buy_list = []
	flatrate_list = []
	for info in providers['flatrate']:
		flatrate_list.append(info['provider_name'])
	for info in providers['buy']:
		buy_list.append(info['provider_name'])
	result_dict['flatrate'] = flatrate_list
	result_dict['buy'] = buy_list
	return result_dict


	
