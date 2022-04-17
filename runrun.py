""" import libraries """

import pandas as pd
from colorama import Fore, Style
import re


GSHEET_ID = "1MjifIi5MPPGBP3635xWTrpef3RWngXcWgKjnCsaoE6Y"
SHEET_NAME = "Data"
GSHEET_URL = f"https://docs.google.com/spreadsheets/d/{GSHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"  # noqa
df = pd.read_csv(GSHEET_URL)


def titlecase(user_input):
    """
    prevents .title() method to capitalize first letter after (' apostrophe)
    """
    return re.sub(
        r"[A-Za-z]+('[A-Za-z]+)?",
        lambda word: word.group(0).capitalize(),
        user_input)


def get_director():
    """
TEST TEST TEST
    """
    request_director = input(f"{Fore.BLUE + Style.BRIGHT}"
                             f"\nType a director: {Style.RESET_ALL}")
    request_director = request_director.strip().lower()
    search = False
    df_copy = df.copy(deep=True)
    df_copy['Director'] = df_copy['Director'].str.lower()

    for value in df_copy['Director']:
        if request_director in value:
            search = True

    if not search:
        df_copy['Director'] = (
            df_copy['Director'].str.normalize('NFKD').str.encode(
                'ascii', errors='ignore').str.decode('utf-8'))
        for value in df_copy['Director']:
            if request_director in value:
                search = True
    """
    if not search:
        user_input = titlecase(request_director)
        request_director = user_input
        for value in df_copy['Director']:
            for item in value:
                if request_director in str(item):
                    search = True

    if not search:
        df_copy['Director'] = df_copy['Director'].str.lower()
        request_director = request_director.lower()
        for value in df_copy['Director']:
            for item in value:
                if request_director in str(item):
                    search = True
    """
    if search:
        mask = df_copy['Director'].str.contains(request_director)
        director_data = df.loc[mask,
                               ['Title',
                                'Genres',
                                'Director',
                                'Actor1',
                                'Actor2',
                                'Actor3',
                                'IMDB Score']]
        print(f"""{Fore.YELLOW + Style.BRIGHT}
All the films from the director you were looking for:
{Style.RESET_ALL}{director_data}\n""")

    else:
        print(f"""{Fore.YELLOW + Style.BRIGHT}
This director is not present in the database{Style.RESET_ALL}\n""")

#get_director()


def get_actor():
    """
    WORK IN PROGRESS
    """
    request_actor = input(f"{Fore.BLUE + Style.BRIGHT}"
                          f"\nType an actor: {Style.RESET_ALL}")
    request_actor = request_actor.strip().lower()
    search = False
    df_copy = df.copy(deep=True)
    df_copy = df_copy.applymap(lambda s: s.lower() if isinstance(s, str) else s)
    for value in df_copy[['Actor1', 'Actor2', 'Actor3']].values:
        for item in value:
            if request_actor in str(item):
                search = True

    if not search:
        df_copy['Actor1'] = (
            df_copy['Actor1'].str.normalize('NFKD').str.encode(
                'ascii', errors='ignore').str.decode('utf-8'))
        df_copy['Actor2'] = (
            df_copy['Actor2'].str.normalize('NFKD').str.encode(
                'ascii', errors='ignore').str.decode('utf-8'))
        df_copy['Actor3'] = (
            df_copy['Actor3'].str.normalize('NFKD').str.encode(
                'ascii', errors='ignore').str.decode('utf-8'))
        for value in df_copy[['Actor1', 'Actor2', 'Actor3']].values:
            for item in value:
                if request_actor in str(item):
                    search = True
    """
    if not search:
        user_input = titlecase(request_actor)
        request_actor = user_input
        print('requested actor in titlecase', request_actor)
        for value in df_copy[['Actor1', 'Actor2', 'Actor3']].values:
            for item in value:
                if request_actor in str(item):
                    search = True

    if not search:
        request_actor = request_actor.lower()
        print('requested actor in lower', request_actor)
        df_copy = df_copy.applymap(
            lambda s: s.lower() if isinstance(
                s, str) else s)
        df_lower = df_lower.applymap(lambda s: s.lower() if type(s) == str else s)
        for value in df_copy.values:
            if request_actor in value:
                search = True
    """
    if search:
        mask1 = df_copy['Actor1'].str.contains(request_actor)
        mask2 = df_copy['Actor2'].str.contains(request_actor)
        mask3 = df_copy['Actor3'].str.contains(request_actor)
        actor_data = df.loc[mask1 | mask2 | mask3, [
            'Title', 'Genres', 'Director', 'Actor1', 'Actor2', 'Actor3',
            'IMDB Score']]
        print(f"""{Fore.YELLOW + Style.BRIGHT}
All the movies of the actor you were looking for:
{Style.RESET_ALL}{actor_data}\n""")

    else:
        print(f"""{Fore.YELLOW + Style.BRIGHT}
This actor is not present in the database{Style.RESET_ALL}\n""")
get_actor()
