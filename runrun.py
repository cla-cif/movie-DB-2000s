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
    LET'S TRY
    """
    return re.sub(
        r"[A-Za-z]+('[A-Za-z]+)?",
        lambda word: word.group(0).capitalize(),
        user_input)
    
"""
s = titlecase(request_actor)
request_actor = s
print('sstring', s)
print('request actor', request_actor)
"""

def get_actor():
    """
    WORK IN PROGRESS
    """

    request_actor = input(f"{Fore.BLUE + Style.BRIGHT}"
                          f"\nType an actor: {Style.RESET_ALL}")
    request_actor = request_actor.lower().title().strip()
    search = False
    df_copy = df.copy(deep=True)
    for value in df_copy[['Actor1', 'Actor2', 'Actor3']].values:
        for item in value:
            if request_actor in str(item):
                search = True

    if not search:
        user_input = titlecase(request_actor)
        request_actor = user_input
        for value in df_copy[['Actor1', 'Actor2', 'Actor3']].values:
            for item in value:
                if request_actor in str(item):
                    search = True
                else: 
                    continue

    if not search:
        request_actor = request_actor.lower()
        df_lower = df_copy[['Actor1', 'Actor2', 'Actor3']]
        df_lower = df_lower.applymap(lambda s:s.lower() if type(s) == str else s)
        for item in value:
            if request_actor in str(item):
                search = True
            else: 
                continue

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

    if search:
        mask1 = df_copy['Actor1'].str.contains(request_actor)
        mask2 = df_copy['Actor2'].str.contains(request_actor)
        mask3 = df_copy['Actor3'].str.contains(request_actor)
        actor_data = df_copy.loc[mask1 | mask2 | mask3, [
            'Title', 'Genres', 'Director', 'Actor1', 'Actor2', 'Actor3',
            'IMDB Score']]
        print(f"""{Fore.YELLOW + Style.BRIGHT}
All the movies of the actor you were looking for:
{Style.RESET_ALL}{actor_data}\n""")

    else:
        print(f"""{Fore.YELLOW + Style.BRIGHT}
This actor is not present in the database{Style.RESET_ALL}\n""")
get_actor()


#df_copy = df.copy(deep=True)
#my_df = df_copy[['Actor1', 'Actor2', 'Actor3']]
#my_df = my_df.applymap(lambda s: s.lower() if type(s) == str else s)
#print(my_df)

