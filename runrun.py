from time import sleep
from os import system, name
import pandas as pd
from colorama import Fore, Back, Style
import pyfiglet


gsheetid = "1MjifIi5MPPGBP3635xWTrpef3RWngXcWgKjnCsaoE6Y"
sheet_name = "Data"
gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(
    gsheetid, sheet_name)
df = pd.read_csv(gsheet_url)


"""
test = unicodedata2.normalize("NFD", "Skarsgård").encode('WINDOWS-1252', 'ignore')
print('it works as a single methond', test)
test2 = unicodedata2.normalize("NFD", "Zoë ").encode('ascii', 'ignore')
print('it works as a single methond', test2)
df['Actor3'] = (df['Actor3'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8'))
print(df['Actor3'])
"""


def get_actor():
    """
    df['Actor1'] = (df['Actor1'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8'))
    df['Actor2'] = (df['Actor2'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8'))
    df['Actor3'] = (df['Actor3'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8'))
    """
    request_actor = input("Enter an actor: ")
    request_actor = request_actor.lower().title()
    search = False
    for value in df.values:
        for item in value:
            if request_actor in str(item):
                search = True

    if search:
        mask1 = df['Cast'].str.contains(request_actor)
        actor_data = df.loc[mask1, ['Title', 'Year', 'Genres', 'Cast']]
        print(
            'All the movies of the actor you were looking for\n',
            actor_data,
            '\n')

    else:
        print('The actor is not present in the database')


def get_actor():
    """
    df['Actor1'] = (df['Actor1'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8'))
    df['Actor2'] = (df['Actor2'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8'))
    df['Actor3'] = (df['Actor3'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8'))
    """
    request_actor = input("Enter an actor: ")
    request_actor = request_actor.lower().title()
    search = False
    for value in df.values:
        for item in value:
            if request_actor in str(item):
                search = True

    if search:
        mask1 = df['Actor1'].str.contains(request_actor)
        mask2 = df['Actor2'].str.contains(request_actor)
        mask3 = df['Actor3'].str.contains(request_actor)
        actor_data = df.loc[mask1 | mask2 | mask3, [
            'Title', 'Year', 'Genres', 'Actor1', 'Actor2', 'Actor3']]
        print(
            'All the movies of the actor you were looking for\n',
            actor_data,
            '\n')
        print('Do you want to do a new search or find data?')
        welcome()

    else:
        print('The actor is not present in the database')
        print('Do you want to do a new search or find data?')
        welcome()


def average():
    df_avg_budget = df['Budget'].dropna().mean().astype(int)
    print(
        '\n'
        "The average cost to produce this decade's films is:",
        '{0:,}'.format(df_avg_budget),
        '$')
    df_avg_score = df['IMDB Score'].mean().round(1)
    print(
        "\nThe average score got by this decade's films on IMDB is:",
        df_avg_score)
    df_avg_duration = df['Duration'].mean().round(1)
    print(
        "\nThe average duration got by this decade's films on IMDB is:",
        df_avg_duration,'minutes\n')
    #print('\nDo you want to run a new search or find data?\n')
    #welcome()
#average()

def director_score():
    gb_director_score = df.groupby(
        'Director',
        sort=False,
        dropna=True)['IMDB Score'].mean().round(1).sort_values(
        ascending=False).reset_index()
    print(
        '\nDirectors which got the highest scores on IMDB Score: \n',
        gb_director_score.to_string(
            index=False))
    #print('\nDo you want to run a new search or find data?')
    #welcome()


dups_director = df.pivot_table(columns=['Director'], aggfunc='size').sort_values(ascending=False)
#print(dups_director)

new_df = df[['Director', 'IMDB Score']].copy()

new_df['Director Rank'] = new_df['Director'].rank(ascending=False, method ='average')
new_df['dups_director'] = new_df.pivot_table(columns=['Director'], aggfunc='size').sort_values(ascending=False)
#print(new_df)

test = df['Director'].value_counts()
print(test)

gb_director_score = df.groupby('Director').agg({'Title':'count', 'IMDB Score': 'sum'}).rename(columns={'Title':'Number of movies', 'IMDB Score': 'Total IMDB Score'}).sort_values(by=['Number of movies', 'Total IMDB Score'], ascending=False).reset_index()
gb_director_score['Average Score'] = (gb_director_score["Total IMDB Score"] / gb_director_score["Number of movies"]).round(2)
print(gb_director_score.head(20))