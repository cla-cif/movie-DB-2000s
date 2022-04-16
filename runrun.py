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


def get_film_genres():
    """
    applies to input .title() to match dataframe's entries case
    search for matches in the Genres column,
    display output or message, calls welcome function after.
    if more than 10 matches found, displays a random .sample() of them.
    """
    print(
        Fore.WHITE + Style.BRIGHT +
        """\n    Search by one or more genres,
    type the words divided by a space.
    In case of multiple matches ('Comedy' has 850+ !),
    only 10 random results will be displayed.""")
    request_genre = input(f"{Fore.BLUE + Style.BRIGHT}"
                          f"\nType a genre: {Style.RESET_ALL}")
    request_genre = request_genre.lower().title().strip()
    search = False
    df_copy = df.copy(deep=True)
    df_copy.dropna().astype(str)
    for value in df_copy['Genres']:
        if request_genre in value:
            search = True
    if search:
        mask = df_copy['Genres'].str.contains(request_genre)
        film_genre = df_copy.loc[mask,
                                 ['Title',
                                  'Genres',
                                  'Director',
                                  'Actor1',
                                  'Actor2',
                                  'Actor3',
                                  'IMDB Score']]
        if mask.sum() > 10:
            film_genre = film_genre.sample(n=10, replace=True)
        print(f"""{Fore.YELLOW + Style.BRIGHT}
All the films of the genre you were looking for:
{Style.RESET_ALL}{film_genre}\n""")

    else:
        print(f"""{Fore.YELLOW + Style.BRIGHT}
This genre is not present in the database{Style.RESET_ALL}\n""")


get_film_genres()
