import requests #External library - https://docs.python-requests.org/en/latest/user/quickstart/#make-a-request
import json #https://docs.python.org/3/library/json.html
#Adam Sellwood
#https://jikan.docs.apiary.io/# - anime and manga

genre_dict = {
            'Action': 1, 'Adventure': 2, 'Cars': 3, 'Comedy': 4, 'Avante Garde': 5, 'Demons': 6, 'Mystery': 7, 'Drama': 8, 'Ecchi': 9,
            'Fantasy': 10, 'Game': 11, 'Historical': 13, 'Horror': 14, 'Kids': 15, 'Martial Arts': 17, 'Mecha': 18, 'Music': 19,
            'Parody': 20, 'Samurai': 21, 'Romance': 22, 'School': 23, 'Sci Fi': 24, 'Shoujo': 25, 'Girls Love': 26, 'Shounen': 27,
            'Boys Love': 28, 'Space': 29, 'Sports': 30, 'Super Power': 31, 'Vampire': 32, 'Harem': 35, 'Slice Of Life': 36,
            'Supernatural': 37, 'Military': 38, 'Police': 39, 'Psychological': 40, 'Suspense': 41, 'Seinen': 42, 'Josei': 43,
            'Award Winning': 46, 'Gourmet': 47, 'Work Life': 48
}

def anime_by_genre(genre):
    '''Data stored in dictionaires within a list.
    Function takes in a string as an arguement.'''
    result_list = []
    try:
        genreid = genre_dict[genre.title()]
    except (KeyError, AttributeError) as error: 
        '''https://stackoverflow.com/questions/6470428/catch-multiple-exceptions-in-one-line-except-block
        Showed me how to catch multiple exceptions in one line.'''
        return 'Sorry that is not a valid input.'
    response = requests.get(f"https://api.jikan.moe/v3/genre/anime/{genreid}").text
    response_dict = json.loads(response)
    animes_list = response_dict['anime']
    for info in animes_list:
        result_dict = {}
        result_dict['Title'] = info['title']
        result_dict['Url'] = info['url']
        result_dict['Episodes'] = info['episodes']
        result_dict['Score'] = info['score']
        result_dict['Producers'] = info['producers'][0]['name']
        result_dict['Image'] = info['image_url']
        result_dict['Synopsis'] = info['synopsis']
        result_list.append(result_dict)
    return result_list
    
def anime_trailers(title):
    '''Data stored in dictionaires within a list.
    Function takes in a string as an arguement.'''
    information = grab_anime_id(title)
    if isinstance(information, str):
        return information
    else:
        result_list = []
        response = requests.get(f'https://api.jikan.moe/v3/anime/{information}/videos').text
        response_dict = json.loads(response)
        try:
            animes_list = response_dict['promo']
        except KeyError:
            return f'Sorry I could not find any find any anime with the title "{title}".'
        for info in animes_list:
            result_dict = {}
            result_dict['Title'] = info['title']
            result_dict['Video'] = info['video_url']
            result_list.append(result_dict)
        return result_list

def anime_by_title(title):
    '''Data stored in dictionaires within a list.
    Function takes in a string as an arguement.'''
    result_list = []
    response = requests.get(f'https://api.jikan.moe/v3/search/anime?q={title}').text
    response_dict = json.loads(response)
    try:
        animes_list = response_dict['results']
    except KeyError:
        return f'Sorry I could not find any anime with the title "{title}".'
    for info in animes_list:
        result_dict = {}
        result_dict['Title'] = info['title']
        result_dict['Url'] = info['url']
        result_dict['Episodes'] = info['episodes']
        result_dict['score'] = info['score']
        result_dict['Image'] = info['image_url']
        result_list.append(result_dict)
    return result_list

def grab_anime_id(title):
    '''Returns an integer.
    Function takes in a string as an arguement.'''
    response = requests.get(f'https://api.jikan.moe/v3/search/anime?q={title}').text
    response_dict = json.loads(response)
    try:
        animes_list = response_dict['results']
    except KeyError:
        return f'Sorry I could not find any anime with the title "{title}".'
    malid = animes_list[0]['mal_id']
    return malid

def anime_recommendations(title):
    '''Data stored in dictionaires within a list.
    Function takes in a string as an arguement.'''
    information = grab_anime_id(title)
    if isinstance(information, str):
        return information
    else:
        result_list = []
        response = requests.get(f'https://api.jikan.moe/v3/anime/{information}/recommendations').text
        response_dict = json.loads(response)
        animes_list = response_dict['recommendations']
        for info in animes_list:
            result_dict = {}
            result_dict['Title'] = info['title']
            result_dict['Url'] = info['url']
            result_dict['rec_num'] = info['recommendation_count']
            result_dict['Image'] = info['image_url']
            result_list.append(result_dict)
        return result_list

def animelist_by_user(user, search):
    '''Data stored in a list.
    Function takes two strings as arguements.'''
    result_list = []
    search = search.title()
    try:
        if search == 'Watching':
            response = requests.get(f'https://api.jikan.moe/v3/user/{user}/animelist/watching').text
            response_dict = json.loads(response)
            animes_list = response_dict['anime']
            for info in animes_list:
                result_list.append(info['title'])
        elif search == 'Completed':
            response = requests.get(f'https://api.jikan.moe/v3/user/{user}/animelist/completed').text
            response_dict = json.loads(response)
            animes_list = response_dict['anime']
            for info in animes_list:
                result_list.append(info['title'])
        elif search == 'Onhold':
            response = requests.get(f'https://api.jikan.moe/v3/user/{user}/animelist/onhold').text
            response_dict = json.loads(response)
            animes_list = response_dict['anime']
            for info in animes_list:
                result_list.append(info['title'])
        elif search == 'Dropped':
            response = requests.get(f'https://api.jikan.moe/v3/user/{user}/animelist/dropped').text
            response_dict = json.loads(response)
            animes_list = response_dict['anime']
            for info in animes_list:
                result_list.append(info['title'])
        elif search == 'Plantowatch':
            response = requests.get(f'https://api.jikan.moe/v3/user/{user}/animelist/plantowatch').text
            response_dict = json.loads(response)
            animes_list = response_dict['anime']
            for info in animes_list:
                result_list.append(info['title'])
        else:
            response = requests.get(f'https://api.jikan.moe/v3/user/{user}/animelist/all').text
            response_dict = json.loads(response)
            animes_list = response_dict['anime']
            for info in animes_list:
                result_list.append(info['title'])
    except KeyError:
        return f'Sorry I can not find this profile.'
    return result_list

def anime_by_season(year, season):
    '''Data stored in list.
    Function takes in an integer for year and a string for season.'''
    result_list = []
    if year not in range(1917,2022):
        return f'You must enter a year between 1917 and 2021.'
    response = requests.get(f'https://api.jikan.moe/v3/season/{year}/{season}').text
    response_dict = json.loads(response)
    animes_list = response_dict['anime']
    if len(animes_list) == 0:
        return 'There was no anime released in this season that year.'
    for a in animes_list:
        result_list.append(a['title'])
    return result_list

def search_top_anime():
    '''Data stored in dictionaires within a list.
    No arguement required.'''
    result_list = []
    response = requests.get(f'https://api.jikan.moe/v3/top/anime').text
    response_dict = json.loads(response)
    animes_list = response_dict['top']
    for info in animes_list:
        result_dict = {}
        result_dict['Title'] = info['title']
        result_dict['Url'] = info['url']
        result_dict['Episodes'] = info['episodes']
        result_dict['Score'] = info['score']
        result_dict['Rank'] = info['rank']
        result_dict['Image'] = info['image_url']
        result_list.append(result_dict)
    return result_list

def characters_in_anime(title):
    '''Data stored in dictionaires within a list.
    Function takes a string as an arguement.'''
    information = grab_anime_id(title)
    if isinstance(information, str):
        return information
    else:
        result_list = []
        response = requests.get(f'https://api.jikan.moe/v3/anime/{information}/characters_staff').text
        response_dict = json.loads(response)
        characters_list = response_dict['characters']
        for info in characters_list:
            result_dict = {}
            result_dict['Name'] = info['name']
            result_dict['Role'] = info['role']
            result_dict['Url'] = info['url']
            result_dict['Image'] = info['image_url']
            result_list.append(result_dict)
        return result_list

def top_rated_character_anime():
    '''Data stored in dictionaires within a list.
    No arguements required.'''
    result_list = []
    response = requests.get(f'https://api.jikan.moe/v3/top/characters').text
    response_dict = json.loads(response)
    characters_list = response_dict['top']
    for info in characters_list:
        result_dict = {}
        result_dict['Title'] = info['title']
        result_dict['Image'] = info['image_url']
        list_of_anime = []
        for i in info['animeography']:
            list_of_anime.append(i['name'])
        result_dict['Anime'] = list_of_anime
        result_list.append(result_dict)
    return result_list


