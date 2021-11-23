import discord
from Tier1_Functions import *
from anime_api import *
from manga_api import *
from dan_notes import *
import random

Token = 'OTAzNzI2NDY3MDI2OTI3Njk2.YXxK3A.1bxRjU9Pe6ehzMdqGX-09-hsIyM'

client = discord.Client()

###################################################################################################################################
#Adam Sellwood
def embed(anime, anime_url, episodes, score, producers, image, description):
    '''Function takes in values from API results as arguments.'''
    result = discord.Embed(title=str(anime), url=str(anime_url), provider=  str(producers), image=str(image), description=str(description), color=discord.Color.blue())
    result.add_field(name='Episodes', value=str(episodes), inline=True)
    result.add_field(name='Score', value=str(score), inline=True)
    result.add_field(name='Producers', value=str(producers), inline=True)
    result.set_thumbnail(url=str(image))
    return result
#Embedding within a dicord bot - https://python.plainenglish.io/send-an-embed-with-a-discord-bot-in-python-61d34c711046
#########################################################################################################################################

def trailerobtainer(anime):
    a = anime_trailers(anime)
    a = a[0]['Video']
    if 'embed' in a:
        a = a.replace("embed", "watch")
        b = a.find('?')
        a = a[:b]
    return a


def personality_of_bot():
    personality_num = random.randint(1,2)
    return personality_num

personality_num = personality_of_bot()

@client.event
async def on_ready():
    print(f'We have logged on as {client.user}')

@client.event
async def on_message(message):
    if message.channel.name == 'anime-bot':
        if message.author == client.user: # Bot cannot respond to itself
            return

        if message.content:
            user_input, last_response = get_response(message.content, personality_num)

            if last_response == 'rec_trigger':
                main, sub_type, sub_id = bigask_evaluate(user_input)
                outcome = [main[0], sub_type[0], sub_id[0]]
                if 'anime' in outcome and 'genre' in outcome:
                    a = anime_by_genre(outcome[2])
                    length = len(a)
                    num = random.randint(0, length)
                    a = a[num]
                    b = trailerobtainer(a['Title'])
                    var = embed(a['Title'], a['Url'], a['Episodes'], a['Score'], a['Producers'], a['Image'], a['Synopsis'])
                    await message.channel.send(embed=var)
                    await message.channel.send(b)

                elif 'manga' in outcome and 'genre' in outcome:
                    a = manga_by_genre(outcome[2])
                    length = len(a)
                    num = random.randint(0, length)
                    a = a[num]
                    var = embed(a['Title'], a['Url'], a['Volumes'], a['Score'], a['Author'], a['Image'], a['Synopsis'])
                    await message.channel.send(embed=var)

            elif last_response == 'rate_trigger':
                main, sub_type, sub_id = bigask_evaluate(user_input)
                outcome = [main[0], sub_type[0], sub_id[0]]
                if 'anime' in outcome and 'genre' in outcome:
                    a = anime_by_genre(outcome[2])
                    top_genre_list = sort_by_genre(a)
                    top_genre_list = top_genre_list[:5]
                    for item in top_genre_list:
                        var = embed(item['Title'], item['Url'], item['Episodes'], item['Score'], item['Producers'], item['Image'], item['Synopsis'])
                        b = trailerobtainer(item['Title'])
                        await message.channel.send(embed=var)
                        await message.channel.send(b)

                elif 'manga' in outcome and 'genre' in outcome:
                    a = manga_by_genre(outcome[2])
                    top_genre_list = sort_by_genre(a)
                    top_genre_list = top_genre_list[:5]
                    for item in top_genre_list:
                        var = embed(item['Title'], item['Url'], item['Volumes'], item['Score'], item['Author'], item['Image'], item['Synopsis'])

                        await message.channel.send(embed=var)

            else:
                await message.channel.send(last_response)


client.run(Token)