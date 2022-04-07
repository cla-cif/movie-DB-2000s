from os import system, name
from time import sleep
import pyfiglet
import pandas as pd
from colorama import Fore, Style

GSHEET_ID = "1MjifIi5MPPGBP3635xWTrpef3RWngXcWgKjnCsaoE6Y"
SHEET_NAME = "Data"
GSHEET_URL = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(
    GSHEET_ID, SHEET_NAME)
df = pd.read_csv(GSHEET_URL)

pd.set_option("display.max_rows", 25)
pd.set_option("display.min_rows", None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_columns', None)


# CLEAR


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
    exit()

# WELCOME!


def welcome():
    while True:
        welcome_input = input(Style.RESET_ALL + "Please type data or search: ")
        welcome_input = welcome_input.lower()

        if welcome_input.lower() == "exit":
            print(Fore.CYAN + Style.BRIGHT + 'Thank you! Goodbye!')
            sleep(3)
            clear()

        if validate_welcome(welcome_input):
            print('All right!\n')
            if welcome_input == 'search':
                search_choice()
            elif welcome_input == 'data':
                data_choice()
            break


def validate_welcome(welcome_choice):
    welcome_choices = ['data', 'search']
    try:
        if str(welcome_choice) in welcome_choices:
            return True
        else:
            raise ValueError
    except ValueError:
        print(Fore.RED + 'Please provide a suitable choice\n')
        return False


# DATA SECTION

# DATA AT A GLANCE


def budget():
    df_budget = df['Budget'].dropna().mean().astype(int)
    print(
        '\n'
        "The average cost to produce this decade's films is:",
        '{0:,}'.format(df_budget),
        '$'
        '\n')
    print('\nDo you want to run a new search or find data?\n')
    welcome()


def score():
    df_score = df['IMDB Score'].mean().round(1)
    print(
        "\nThe average score got by this decade's films on IMDB is:",
        df_score,
        '\n')
    print('\nDo you want to run a new search or find data?\n')
    welcome()


def language():
    df_language = df.groupby('Language')['Country'].size().sort_values(
        ascending=False).reset_index(name='Count')
    print('\nNumber of films in each language:\n',
          df_language.to_string(index=False), '\n')
    print('\nDo you want to run a new search or find data?\n')
    welcome()


def year():
    df_year = df.groupby(
        'Year',
        sort=False)['Country'].size().reset_index(
        name='Count')
    print('\nNumber of films produced each year:\n',
          df_year.to_string(index=False), '\n')
    print('\nDo you want to run a new search or find data?\n')
    welcome()


# RANKINGS


def score_country():
    df_score_country = df.groupby(
        'Country', sort=False)['IMDB Score'].mean().round(1).sort_values(
        ascending=False).reset_index()
    print(
        '\nTop ten countries that produced films with the highest IMDB score:',
        df_score_country.head(10).to_string(
            index=False),
        '\n')
    print('\nDo you want to run a new search or find data?')
    welcome()


def highest_score():
    sort_highest_score = df[['Title', 'IMDB Score']
                            ].sort_values(by='IMDB Score', ascending=False)
    print('\nThe best ten films of the decade according to IMDB:\n',
          sort_highest_score.head(10).to_string(index=False), '\n')
    print('\nDo you want to run a new search or find data?')
    welcome()


def lowest_score():
    sort_lowest_score = df[['Title', 'IMDB Score']
                           ].sort_values(by='IMDB Score', ascending=True)
    print('\nThe worst ten films of the decade according to IMDB:\n',
          sort_lowest_score.head(10).to_string(index=False), '\n')
    print('\nDo you want to run a new search or find data?')
    welcome()


def roi():
    df['ROI'] = (df["Gross Earnings"] / df["Budget"] * 100).round(2)
    sort_mostroi = df[['Title', 'ROI']].sort_values(
        by='ROI', ascending=False).dropna()
    print('\nThe most profitable films of the decade:\n',
          sort_mostroi.head(10).to_string(index=False), '\n')
    print('\nDo you want to run a new search or find data?')
    welcome()


def profit():
    df['Profit'] = (
        df['Gross Earnings'] -
        df['Budget']).dropna().astype(int).apply(
        lambda x: f'{x:,}')
    sort_leastprofitable = df[['Title', 'Profit']
                              ].sort_values(by='Profit', ascending=True)
    print(
        '\nTop 10 box-office flop:\n',
        sort_leastprofitable.head(10).to_string(
            index=False),
        '\n')
    print('\nDo you want to run a new search or find data?')
    welcome()


def rating_score():
    gb_rating_score = df.groupby(
        'Content Rating',
        sort=False,
        dropna=True)['IMDB Score'].mean().round(1).sort_values(
        ascending=False).reset_index()
    print(
        '\nThe content ratings and their average IMDB Score: \n',
        gb_rating_score.to_string(
            index=False))
    print('\nDo you want to run a new search or find data?')
    welcome()


def data_choice():
    while True:
        print('Chose one of the following numbers:')
        print("""
        1:  The average budget spent on films.
        2:  The average score according to IMDB.
        3:  Number of films in each language.
        4:  Number of films produced each year.
        5:  Top ten countries that produced films with the highest IMDB score.
        6:  The best ten films of the decade.
        7:  The worst ten films of the decade.
        8:  The most profitable films in terms of return of investment.
        9:  Top 10 box-office flops: the most unprofitable films.
        10  The content ratings and their average IMDB Score.\n""")
        user_input = input("Type the number:  ")
        if user_input.lower() == "exit":
            print(Fore.CYAN + Style.BRIGHT + 'Thank you! Goodbye!')
            sleep(3)
            clear()

        if validate_data_choice(user_input):
            if int(user_input) == 1:
                budget()
            if int(user_input) == 2:
                score()
            if int(user_input) == 3:
                language()
            if int(user_input) == 4:
                year()
            if int(user_input) == 5:
                score_country()
            if int(user_input) == 6:
                highest_score()
            if int(user_input) == 7:
                lowest_score()
            if int(user_input) == 8:
                roi()
            if int(user_input) == 9:
                profit()
            if int(user_input) == 10:
                rating_score()
            break

    return user_input


def validate_data_choice(data):
    try:
        int(data)
    except ValueError:
        print(Fore.RED + 'Please provide a number.\n')
    else:
        if 0 < int(data) < 11:
            return True
        else:
            print(Fore.RED + 'The number is out of range.\n')


# SEARCH


def get_film_info():
    request_film = input("\nType a title: ")
    request_film = request_film.lower().title()
    search = False
    for value in df.values:
        for item in value:
            if request_film in str(item):
                search = True

    if search:
        film_data = df.loc[(df['Title'].str.contains(request_film))]
        print(
            '\nAll you need to know about the film you were looking for:\n',
            film_data,
            '\n')
        print('\nDo you want to run a new search or find data?')
        welcome()
    else:
        print('The film is not present in the database.')
        print('\nDo you want to run a new search or find data?')
        welcome()


def get_film_genres():
    request_genre = input('\nType a genre: ')
    request_genre = request_genre.lower().title()
    search = False
    for value in df.values:
        for item in value:
            if request_genre in str(item):
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
        print(
            'All the films of the genre you were looking for:\n',
            film_genre,
            '\n')
        print('\nDo you want to run a new search or find data?')
        welcome()
    else:
        print('The genre is not present in the database.')
        print('\nDo you want to run a new search or find data?')
        welcome()


def get_actor():
    """
    df['Actor1'] = (df['Actor1'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8'))
    df['Actor2'] = (df['Actor2'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8'))
    df['Actor3'] = (df['Actor3'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8'))
    """
    request_actor = input('\nType an actor: ')
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
            'Title', 'Year', 'Genres', 'Actor1', 'Actor2', 'Actor3', 'IMDB Score']]
        print(
            'All the films of the actor you were looking for:\n',
            actor_data,
            '\n')
        print('\nDo you want to run a new search or find data?')
        welcome()

    else:
        print('The actor is not present in the database.')
        print('\nDo you want to run a new search or find data?')
        welcome()


def get_director():
    request_director = input('\nType a director: ')
    request_director = request_director.lower().title()
    search = False
    for value in df.values:
        for item in value:
            if request_director in str(item):
                search = True

    if search:
        mask = df['Director'].str.contains(request_director)
        director_data = df.loc[mask,
                               ['Title',
                                'Genres',
                                'Director',
                                'Actor1',
                                'Actor2',
                                'Actor3',
                                'IMDB Score']]
        print(
            'All the films from the director you were looking for:\n',
            director_data,
            '\n')
        print('\nDo you want to run a new search or find data?')
        welcome()

    else:
        print('The director is not present in the database.\n')
        print('\nDo you want to run a new search or find data?')
        welcome()


def search_choice():
    while True:
        user_input = input(
            "Do you want to search by actor, genre, director or title? ")
        user_input = user_input.lower()
        if user_input.lower() == "exit":
            print(Fore.CYAN + Style.BRIGHT + 'Thank you! Goodbye!')
            sleep(3)
            clear()

        if validate_search_choice(user_input):
            print("All right!")
            if user_input == 'director':
                get_director()
            elif user_input == 'actor':
                get_actor()
            elif user_input == 'genre':
                get_film_genres()
            elif user_input == 'title':
                get_film_info()
            break
    return user_input


def validate_search_choice(choice):
    choices = ['director', 'actor', 'genre', 'title']
    try:
        if str(choice) in choices:
            return True
        else:
            raise ValueError
    except ValueError:
        print(Fore.RED + 'Please provide a suitable choice.\n')
        return False


# MAIN


def main():
    welcome()
    data_choice()
    search_choice()


title = pyfiglet.figlet_format("Movie DB 2000s", font="slant")
print(Fore.YELLOW + Style.BRIGHT + title)
print(Fore.CYAN + Style.BRIGHT + """
Welcome to the 2000s Movie Database,
the database contains""", df['Title'].count(), """films cathegorised by
title, genre, year, director, and leading actors,
number of reviews (from critics and users) and IMDB score.\n""" + Fore.YELLOW + Style.BRIGHT + """
Get statistics, the top 10 lists or search by film.\n""" + Style.RESET_ALL + """
To quit, type exit after a question | To run, type and hit enter\n""" + Style.BRIGHT + """
What do you want to do today, get data or search?\n""")

main()
