""" import libraries """
import pandas as pd
from colorama import Fore, Style


GSHEET_ID = "1MjifIi5MPPGBP3635xWTrpef3RWngXcWgKjnCsaoE6Y"
SHEET_NAME = "Data"
GSHEET_URL = f"https://docs.google.com/spreadsheets/d/{GSHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"  # noqa
df = pd.read_csv(GSHEET_URL)

"""
ORIGINAL CODE
    search = False
    for value in df.values:
        for item in value:
            if request_genre in str(item):
                search = True

"""
def get_film_genres():
    """
    applies to input same dataframe's entries case
    nested loop to search for matches in the df and Genres column,
    display output or message, calls welcome function after.
    if more than 10 matches found, displays a random .sample() of them.
    """
    print(
        Fore.BLUE + Style.BRIGHT +
        """\n    Search by one or more genres, separated by a space.
    If there are many hits (Comedy has 850+ !),
    only 10 random results will be displayed.""")
    request_genre = input(Style.RESET_ALL + '\nType a genre: ')
    request_genre = request_genre.lower().title()
    search = False
    for value in df['Genres']:
        if request_genre in value:
            search = True

    if search:
        mask = df['Genres'].str.contains(request_genre)
        film_genre = df.loc[mask,
                            ['Title',
                             'Genres',
                             'Director',
                             'Actor1',
                             'Actor2',
                             'Actor3',
                             'IMDB Score']]
        if mask.sum() > 10:
            film_genre = film_genre.sample(n=10)
        print(
            'All the films of the genre you were looking for:\n',
            film_genre,
            '\n')
    else:
        print('The genre is not present in the database.')
get_film_genres()
