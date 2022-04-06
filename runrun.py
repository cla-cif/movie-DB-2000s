import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
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
        print('All the movies of the actor you were looking for\n', actor_data, '\n')


    else:
        print('The actor is not present in the database')

get_actor()

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
        actor_data = df.loc[mask1 | mask2 | mask3, ['Title', 'Year', 'Genres', 'Actor1', 'Actor2', 'Actor3']]
        print('All the movies of the actor you were looking for\n', actor_data, '\n')
        print('Do you want to do a new search or find data?')
        welcome()

    else:
        print('The actor is not present in the database')
        print('Do you want to do a new search or find data?')
        welcome()


