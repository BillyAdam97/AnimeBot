import requests #External Library - https://docs.python-requests.org/en/latest/user/quickstart/#make-a-request
import json #Standard Library - https://docs.python.org/3/library/json.html
#Adam Sellwood
#https://jikan.docs.apiary.io/# - anime and manga

genre_dict = {'Action': 1, 'Adventure': 2, 'Cars': 3, 'Comedy': 4, 'Avante Garde': 5, 'Demons': 6, 'Mystery': 7, 'Drama': 8, 'Ecchi': 9, 'Fantasy': 10,
            'Game': 11, 'Historical': 13, 'Horror': 14, 'Kids': 15, 'Martial Arts': 17, 'Mecha': 18, 'Music': 19, 'Parody': 20,
            'Samurai': 21, 'Romance': 22, 'School': 23, 'Sci Fi': 24, 'Shoujo': 25, 'Girls Love': 26, 'Shounen': 27, 'Boys Love': 28, 'Space': 29, 'Sports': 30,
            'Super Power': 31, 'Vampire': 32, 'Harem': 35, 'Slice Of Life': 36, 'Supernatural': 37, 'Military': 38, 'Police': 39, 'Psychological': 40,
            'Seinen': 41, 'Josei': 42, 'Doujinshi': 43, 'Gender Bender': 44, 'Suspense': 45,'Award Winning': 46, 'Gourmet': 47, 'Work Life': 48,
}

def manga_by_genre(genre):
    '''Data stored in dictionaires within a list.
    Function takes in a string as an arguement.'''
    result_list = []
    try:
        genreid = genre_dict[genre.title()]
    except (KeyError, AttributeError) as error:
        '''https://stackoverflow.com/questions/6470428/catch-multiple-exceptions-in-one-line-except-block
        Showed me how to catch multiple exceptions in one line.'''
        return 'Sorry that is not a valid input.'
    response = requests.get(f"https://api.jikan.moe/v3/genre/manga/{genreid}").text
    response_dict = json.loads(response)
    manga_list = response_dict['manga']
    for info in manga_list:
        result_dict = {}
        result_dict['Title'] = info['title']
        result_dict['Start Date'] = info['publishing_start']
        result_dict['Volumes'] = info['volumes']
        result_dict['Url'] = info['url']
        result_dict['Synopsis'] = info['synopsis']
        result_dict['Score'] = info['score']
        result_dict['Author'] = info['authors'][0]['name']
        result_dict['Image'] = info['image_url']
        result_list.append(result_dict)
    return result_list

def manga_by_title(title):
    '''Data stored in dictionaires within a list.
    Function takes in a string as an arguement.'''
    result_list = []
    response = requests.get(f"https://api.jikan.moe/v3/search/manga?q={title.lower()}").text
    response_dict = json.loads(response)
    try:
        manga_list = response_dict['results']
    except KeyError:
        return f'Sorry I could not find any manga with the title "{title}".'
    for info in manga_list:
        result_dict = {}
        result_dict['Title'] = info['title']
        result_dict['Start Date'] = info['start_date']
        result_dict['End Date'] = info['end_date']
        result_dict['Url'] = info['url']
        result_dict['Synopsis'] = info['synopsis']
        result_dict['Chapters'] = info['chapters']
        result_dict['Volumes'] = info['volumes']
        result_dict['Score'] = info['score']
        result_dict['Image'] = info['image_url']
        result_list.append(result_dict)
    return result_list

def grab_manga_id(title):
    '''Returns an integer.
    Function takes in a string as an arguement.'''
    response = requests.get(f'https://api.jikan.moe/v3/search/manga?q={title}').text
    response_dict = json.loads(response)
    try:
        manga_list = response_dict['results']
    except KeyError:
        return f'Sorry I could not find any manga with the title "{title}".'
    malid = manga_list[0]['mal_id']
    return malid

def manga_recommendations(title):
    '''Data stored in dictionaires within a list.
    Function takes in a string as an arguement.'''
    information = grab_manga_id(title)
    if isinstance(information, str):
        return information
    else:
        result_list = []
        response = requests.get(f"https://api.jikan.moe/v3/manga/{information}/recommendations").text
        response_dict = json.loads(response)
        manga_list = response_dict['recommendations']
        for info in manga_list:
            result_dict = {}
            result_dict['Title'] = info['title']
            result_dict['malid'] = info['mal_id']
            result_dict['Url'] = info['url']
            result_dict['rec_num'] = info['recommendation_count']
            result_dict['Image'] = info['image_url']
            result_list.append(result_dict)
    return result_list

def mangalist_by_user(user, search):
    '''Data stored in dictionaires within a list.
    Function takes in two strings as arguements.'''
    result_list = []
    search = search.title()
    try:
        if search == 'Reading':
            response = requests.get(f"https://api.jikan.moe/v3/user/{user}/mangalist/reading").text
            response_dict = json.loads(response)
            manga_list = response_dict['manga']
            for info in manga_list:
                result_list.append(info['title'])
        elif search == 'Completed':
            response = requests.get(f"https://api.jikan.moe/v3/user/{user}/mangalist/completed").text
            response_dict = json.loads(response)
            manga_list = response_dict['manga']
            for info in manga_list:
                result_list.append(info['title'])
        elif search == 'Onhold':
            response = requests.get(f"https://api.jikan.moe/v3/user/{user}/mangalist/onhold").text
            response_dict = json.loads(response)
            manga_list = response_dict['manga']
            for info in manga_list:
                result_list.append(info['title'])
        elif search == 'Dropped':
            response = requests.get(f"https://api.jikan.moe/v3/user/{user}/mangalist/dropped").text
            response_dict = json.loads(response)
            manga_list = response_dict['manga']
            for info in manga_list:
                result_list.append(info['title'])
        elif search == 'Plantoread':
            response = requests.get(f"https://api.jikan.moe/v3/user/{user}/mangalist/plantoread").text
            response_dict = json.loads(response)
            manga_list = response_dict['manga']
            for info in manga_list:
                result_list.append(info['title'])
        else:
            response = requests.get(f"https://api.jikan.moe/v3/user/{user}/mangalist/all").text
            response_dict = json.loads(response)
            manga_list = response_dict['manga']
            for info in manga_list:
                result_list.append(info['title'])
    except KeyError:
        return f'Sorry I can not find this profile.'
    return result_list

def search_top_manga():
    '''Data stored in dictionaires within a list.
    No arguements required.'''
    result_list = []
    response = requests.get(f'https://api.jikan.moe/v3/top/manga').text
    response_dict = json.loads(response)
    manga_list = response_dict['top']
    for info in manga_list:
        result_dict = {}
        result_dict['Title'] = info['title']
        result_dict['Url'] = info['url']
        result_dict['Volumes'] = info['volumes']
        result_dict['Score'] = info['score']
        result_dict['malid'] = info['mal_id']
        result_dict['Rank'] = info['rank']
        result_dict['Image'] = info['image_url']
        result_list.append(result_dict)
    return result_list

def characters_in_manga(title):
    '''Data stored in dictionaires within a list.
    Function takes in a string as an arugment.'''
    information = grab_manga_id(title)
    if isinstance(information, str):
        return information
    else:
        result_list = []
        response = requests.get(f'https://api.jikan.moe/v3/manga/{information}/characters').text
        response_dict = json.loads(response)
        characters_dict = response_dict['characters']
        for info in characters_dict:
            result_dict = {}
            result_dict['Name'] = info['name']
            result_dict['Role'] = info['role']
            result_dict['Url'] = info['url']
            result_dict['Image'] = info['image_url']
            result_list.append(result_dict)
        return result_list

def top_rated_character_manga():
    '''Data stored in dictionaires within a list.
    No arguements required.'''
    result_list = []
    response = requests.get(f'https://api.jikan.moe/v3/top/characters').text
    response_dict = json.loads(response)
    characters_dict = response_dict['top']
    for info in characters_dict:
        result_dict = {}
        result_dict['Title'] = info['title']
        result_dict['Image'] = info['image_url']
        list_of_manga = []
        for i in info['mangaography']:
            list_of_manga.append(i['name'])
        result_dict['Manga'] = list_of_manga
        result_list.append(result_dict)
    return result_list


