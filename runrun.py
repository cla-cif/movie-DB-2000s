""" import libraries """

import pandas as pd
from colorama import Fore, Style
import re


GSHEET_ID = "1MjifIi5MPPGBP3635xWTrpef3RWngXcWgKjnCsaoE6Y"
SHEET_NAME = "Data"
GSHEET_URL = f"https://docs.google.com/spreadsheets/d/{GSHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"  # noqa
df = pd.read_csv(GSHEET_URL)

def titlecase(s):
    """
    LET'S TRY
    """
    return re.sub(
        r"[A-Za-z]+('[A-Za-z]+)?",
        lambda word: word.group(0).capitalize(),
        s)
    """
    s = titlecase(request_actor)
    request_actor = s
    print('sstring', s)
    print('request actor', request_actor)
    """

def get_film_info():
    """
    THIS WORKS THIS WORKS THIS WORKS THIS WORKS THIS WORKS THIS WORKS THIS WORKS THIS WORKS THIS WORKS THIS WORKS THIS WORKS THIS WORKS
    """
    request_film = input(f"{Fore.BLUE + Style.BRIGHT}"
                         f"\nType a title: {Style.RESET_ALL}")
    request_film = request_film.lower().strip()
    search = False
    df_copy = df.copy(deep=True)
    df_copy['Title'] = df_copy['Title'].str.lower()
    for value in df_copy['Title']:
        if request_film in value:
            search = True
    if not search:
        df_copy['Title'] = (
            df_copy['Title'].str.normalize('NFKD').str.encode(
                'ascii', errors='ignore').str.decode('utf-8'))
        for value in df_copy['Title']:
            if request_film in value:
                search = True

    if search:
        film_data = df.loc[(df_copy['Title'].str.contains(request_film))]
        print(f"""{Fore.YELLOW + Style.BRIGHT}
All you need to know about the film you were looking for:
{Style.RESET_ALL}{film_data}\n""")

    else:
        print(f"""{Fore.YELLOW + Style.BRIGHT}
This film is not present in the database{Style.RESET_ALL}\n""")
#get_film_info()


