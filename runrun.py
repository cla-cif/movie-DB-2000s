""" import libraries """
from os import system, name
from time import sleep
import pyfiglet
import pandas as pd
from colorama import Fore, Style

GSHEET_ID = "1MjifIi5MPPGBP3635xWTrpef3RWngXcWgKjnCsaoE6Y"
SHEET_NAME = "Data"
GSHEET_URL = f"https://docs.google.com/spreadsheets/d/{GSHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"  # noqa
df = pd.read_csv(GSHEET_URL)


def get_film_info():
    """
    applies to input .title() to match dataframe's entries case
    search for matches in the dfcopy of Title column,
    if none found, encodes entries to match search for extend ASCII chars,
    if none found, display message. else display output.
    """
    print(
        Fore.WHITE + Style.BRIGHT +
        """\n    Search by full or partial title,
    type the words divided by a space.
    Characters from a foreign alpabet will be matched as well
    (type amelie to match Amélie)
    In case of multiple matches,
    the results will be restricted to the first 10 elements""")
    request_film = input(f"{Fore.BLUE + Style.BRIGHT}"
                         f"\nType a title: {Style.RESET_ALL}")
    request_film = request_film.lower().title().strip().str
    print('this is the input', request_film)
    search = False
    df_copy = df.copy(deep=True)
    print(df_copy['Title'].str.lower)
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
get_film_info()

