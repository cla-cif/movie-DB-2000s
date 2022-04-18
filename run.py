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

pd.set_option("display.max_rows", 10)
pd.set_option("display.min_rows", None)
pd.set_option("display.max_colwidth", None)
pd.set_option("display.max_columns", None)


# CLEAR


def clear():
    """
    clears the CLI and exit the program.
    can be called typing exit after every input prompt.
    """
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
    exit()

# HELP


def get_help():
    """
    it's called once on load
    calls help_text function
    calls validation function on user input
    """
    while True:
        help_input = input(
            Fore.BLUE +
            Style.BRIGHT + """
Type HELP to get instruction, EXIT to quit or press Enter to continue: """ +
            Style.RESET_ALL)
        help_input = help_input.lower().strip()

        if help_input.lower().strip() == "exit":
            print(Fore.YELLOW + Style.BRIGHT + 'Thank you!' + Fore.BLUE +
                  Style.BRIGHT + ' Goodbye!')
            sleep(3)
            clear()

        if validate_get_help(help_input):
            if help_input == 'help':
                help_text()
            elif help_input == "":
                welcome()
            break


def validate_get_help(help_choice):
    """
    raise error msg if input is not return key or help string.
    function is called by get_help function.
    """
    choices = ['help', '']
    try:
        if str(help_choice) in choices:
            return True
        else:
            raise ValueError
    except ValueError:
        print(
            Fore.RED +
            'Please provide a suitable choice' +
            Style.RESET_ALL)
        return False


def help_text():
    """
    provide descriptive text and info about the app
    can be called typing help after every input prompt.
    calls validation function on user input.
    """
    print(Style.BRIGHT + """
    The database is part of Kaggle's "The Movies Dataset"
    under CC0: Public Domain Licence.

    This app has two main sections DATA and SEARCH:
        DATA displays 10 options to choose from, showing pre-calculated data.
        SEARCH to find content by actor, title, director, genre.

    When prompted, type an answer from the available options and press Enter.
    In case of an invalid answer, the question is asked again.
    Lowercase and uppercase letters from your input are treated the same.

    Two specific commands can always be typed after each question:
        EXIT   clear the screen and quits the program.
        HELP   provides help and information. """ + Style.RESET_ALL)
    while True:
        help_text_input = input(Style.BRIGHT + Fore.BLUE + """
Press Enter to continue """ + Style.RESET_ALL)
        help_text_input = help_text_input.lower()

        if validate_help_text(help_text_input):
            if help_text_input == 'exit':
                print(Fore.YELLOW + Style.BRIGHT + 'Thank you!' + Fore.BLUE +
                      Style.BRIGHT + ' Goodbye!')
                sleep(3)
                clear()
            elif help_text_input == "":
                welcome()
            break


def validate_help_text(help_text_choice):
    """
    raise error msg if input is not return key or help or exit string.
    function is called by get help text function.
    """
    choices = ['exit', '']
    if str(help_text_choice) == 'help':
        print('Instructions are provided above')
    else:
        try:
            if str(help_text_choice) in choices:
                return True
            else:
                raise ValueError
        except ValueError:
            print(
                Fore.RED + 'Please provide a suitable choice\n' +
                Style.RESET_ALL)
        return False


# WELCOME!

def welcome():
    """
    accepts input strings data/search/exit.
    calls validation function on user input.
    function is called after every output.
    """
    while True:
        welcome_input = input(
            Fore.BLUE + Style.BRIGHT + """
Type SEARCH or DATA to explore the database: """ +
            Style.RESET_ALL)
        welcome_input = welcome_input.lower().strip()

        if welcome_input.lower().strip() == "exit":
            print(Fore.YELLOW + Style.BRIGHT + 'Thank you!' + Fore.BLUE +
                  Style.BRIGHT + ' Goodbye!')
            sleep(3)
            clear()
        elif welcome_input.lower().strip() == 'help':
            help_text()

        if validate_welcome(welcome_input):
            if welcome_input == 'search':
                search_choice()
            elif welcome_input == 'data':
                data_choice()
            break


def validate_welcome(welcome_choice):
    """
    raise error msg if input is not string and not within the options.
    function is called by welcome function.
    """
    choices = ['data', 'search']
    try:
        if str(welcome_choice) in choices:
            return True
        else:
            raise ValueError
    except ValueError:
        print(
            Fore.RED +
            'Please provide a suitable choice\n' +
            Style.RESET_ALL)
        return False


# DATA OPTION

# DATA AT A GLANCE ()


def average():
    """
    applies .mean() method to calculate average on int values.
    rounds the result to one decimal.
    """
    avg_budget = df['Budget'].dropna().mean().astype(int)
    print(f"\nThe average cost to produce this decade's films is: "
          f"{Style.BRIGHT + Fore.YELLOW}{avg_budget:,} ${Style.RESET_ALL}")

    avg_score = df['IMDB Score'].mean().round(1)
    print(f"\nThe average score got by this decade's films on IMDB is: "
          f"{Style.BRIGHT + Fore.YELLOW}{avg_score} points{Style.RESET_ALL}")

    avg_duration = df['Duration'].mean().round(1)
    print(f"\nThe average duration got by this decade's films on IMDB is: "
          f"{Style.BRIGHT + Fore.YELLOW}{avg_duration}"
          f" minutes{Style.RESET_ALL}")
    welcome()


def language():
    """
    group by language and counts occurrencies for each language.
    number are in descending order. first column works as index.
    """
    gb_language = df.groupby('Language')['Country'].size().sort_values(
        ascending=False).reset_index(name='Count')
    print(f"""{Fore.YELLOW + Style.BRIGHT}
Number of films in each language:
{Style.RESET_ALL}{gb_language.to_string(index=False)}\n""")
    welcome()
    welcome()


def year():
    """
    group by year and counts how many movies for each year.
    years are in ascending order. first column works as index.
    """
    gb_year = df.groupby(
        'Year',
        sort=False)['Country'].size().reset_index(
        name='Count')
    print(f"""{Fore.YELLOW + Style.BRIGHT}
Number of films produced each year:
{Style.RESET_ALL}{gb_year.to_string(index=False)}\n""")
    welcome()


# DATA RANKINGS

def director_score():
    """
    use .agg() operation to pass .count() and .sum()
    counts the number of movies for each director.
    sum the IMDB score of the movies from each director.
    renames columns, sort the values in descending order.
    calculates average score and create a new column.
    """
    gb_director_score = df.groupby('Director').agg(
        {
            'Title': 'count',
            'IMDB Score': 'sum'}).rename(
        columns={
            'Title': 'Number of movies',
            'IMDB Score': 'Total IMDB Score'}).sort_values(
        by=[
            'Number of movies',
            'Total IMDB Score'],
        ascending=False).reset_index()
    gb_director_score['Average Score'] = (
        gb_director_score["Total IMDB Score"] /
        gb_director_score["Number of movies"]).round(2)
    print(f"""{Fore.YELLOW + Style.BRIGHT}
The average score of the most prolific directors:
{Style.RESET_ALL}{gb_director_score.head(10).to_string(index=False)}\n""")
    welcome()


def score_country():
    """
    group by country, calculates average score for each.
    scores are in descending order. first column works as index.
    """
    gb_score_country = df.groupby(
        'Country', sort=False)['IMDB Score'].mean().round(1).sort_values(
        ascending=False).reset_index()
    print(f"""{Fore.YELLOW + Style.BRIGHT}
Top 10 countries whose films have the highest IMDB score:
{Style.RESET_ALL}{gb_score_country.head(10).to_string(index=False)}\n""")
    welcome()


def highest_score():
    """
    .sort() in descending order the scores and relative titles.
    scores are in descending order. first column works as index.
    """
    sort_highest_score = df[['Title', 'IMDB Score']
                            ].sort_values(by='IMDB Score', ascending=False)
    print(f"""{Fore.YELLOW + Style.BRIGHT}
The best ten films of the decade according to IMDB:
{Style.RESET_ALL}{sort_highest_score.head(10).to_string(index=False)}\n""")
    welcome()


def lowest_score():
    """
    .sort() in ascending order the scores and relative titles.
    scores are in ascending order. first column works as index.
    """
    sort_lowest_score = df[['Title', 'IMDB Score']
                           ].sort_values(by='IMDB Score', ascending=True)
    print(f"""{Fore.YELLOW + Style.BRIGHT}
The worst ten films of the decade according to IMDB:
{Style.RESET_ALL}{sort_lowest_score.head(10).to_string(index=False)}\n""")
    welcome()


def roi():
    """
    calculate return of investment, displays values and relative title
    values displayed in descending order with relative title
    delete the ROI series after display
    """
    df['ROI'] = (df["Gross Earnings"] / df["Budget"] * 100).round(2)
    sort_highest_roi = df[['Title', 'ROI']].sort_values(
        by='ROI', ascending=False).dropna()
    print(f"""{Fore.YELLOW + Style.BRIGHT}
The most profitable films of the decade:
{Style.RESET_ALL}{sort_highest_roi.head(10).to_string(index=False)}\n""")
    df.drop(['ROI'], axis=1, inplace=True)
    welcome()


def profit():
    """
    calculate profit in new column, displays thousands separated by comma
    values displayed in ascending order with relative title
    delete the profit series after display
    """
    df['Profit'] = (
        df['Gross Earnings'] -
        df['Budget']).dropna().astype(int).apply(
        lambda x: f'{x:,}')
    sort_least_profitable = df[['Title', 'Profit']
                               ].sort_values(by='Profit', ascending=True)
    print(f"""{Fore.YELLOW + Style.BRIGHT}
Top 10 box-office flop:
{Style.RESET_ALL}{sort_least_profitable.head(10).to_string(index=False)}\n""")
    df.drop(['Profit'], axis=1, inplace=True)
    welcome()


def rating_score():
    """
    group by content rating calculate the average score for each cathegory
    scores are in descending order. first column works as index.
    """
    gb_rating_score = df.groupby(
        'Content Rating',
        sort=False,
        dropna=True)['IMDB Score'].mean().round(1).sort_values(
        ascending=False).reset_index()
    print(f"""{Fore.YELLOW + Style.BRIGHT}
The content ratings and their average IMDB Score:
{Style.RESET_ALL}{gb_rating_score.to_string(index=False)}\n""")
    welcome()


def data_choice():
    """
    accepts input strings exit/help or integer within range of options.
    calls validation function on user input.
    calls functions relative to the user's choice.
    """
    while True:
        print(Style.BRIGHT +
              Fore.BLUE + '\nChose one of the following numbers:')
        print(Style.BRIGHT + Fore.WHITE + """
        1:  The average budget, score and duration of this decade's films.
        2:  Number of films in each language.
        3:  Number of films produced each year.
        4:  The most prolific directors of the decade and their scores.
        5:  Top 10 countries that produced films with the highest IMDB score.
        6:  The 10 best films of the decade.
        7:  The 10 worst films of the decade.
        8:  The most profitable films in terms of return of investment.
        9:  Top 10 box-office flops: the most unprofitable films.
        10  The content ratings and their average IMDB Scores.\n""")
        user_input = input(
            Fore.BLUE +
            Style.BRIGHT +
            "Type the number:  " +
            Style.RESET_ALL)
        if user_input.lower().strip() == "exit":
            print(Fore.YELLOW + Style.BRIGHT + 'Thank you!' + Fore.BLUE +
                  Style.BRIGHT + ' Goodbye!')
            sleep(3)
            clear()
        elif user_input.lower().strip() == 'help':
            help_text()

        if validate_data_choice(user_input):
            if int(user_input) == 1:
                average()
            if int(user_input) == 2:
                language()
            if int(user_input) == 3:
                year()
            if int(user_input) == 4:
                director_score()
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
    """
    raise error msg if input is not int and not within the options.
    function is called by data_choice function.
    """
    try:
        int(data)
    except ValueError:
        print(Fore.RED + 'Please provide a number.\n' + Style.RESET_ALL)
    else:
        if 0 < int(data) < 11:
            return True
        else:
            print(Fore.RED + 'The number is out of range.\n' + Style.RESET_ALL)


# SEARCH OPTION


def get_film_info():
    """
    applies .lower() to input and copy of df for accurate comparison
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
    request_film = request_film.lower().strip()
    df_copy = df.copy(deep=True)
    df_copy['Title'] = df_copy['Title'].str.lower()
    search = False
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
        welcome()
    else:
        print(f"""{Fore.YELLOW + Style.BRIGHT}
This film is not present in the database{Style.RESET_ALL}\n""")
        welcome()


def get_film_genres():
    """
    applies .lower() to input and copy of df for accurate comparison
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
    request_genre = request_genre.strip()
    df_copy = df.copy(deep=True)
    df_copy['Genres'] = df_copy['Genres'].str.lower()
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
            film_genre = film_genre.sample(n=10, replace=True)
        print(f"""{Fore.YELLOW + Style.BRIGHT}
All the films of the genre you were looking for:
{Style.RESET_ALL}{film_genre}\n""")
        welcome()
    else:
        print(f"""{Fore.YELLOW + Style.BRIGHT}
This genre is not present in the database{Style.RESET_ALL}\n""")
        welcome()


def get_actor():
    """
    applies .lower() to input and copy of df for accurate comparison
    nested loop to search for matches in the df and actors' 3 columns,
    if none found, encodes entries to match search for extend ASCII chars,
    if none found, display message. else display output.
    """
    print(
        Fore.WHITE + Style.BRIGHT +
        """\n    Search by full or partial name.
    Type the words divided by a space.
    Characters from a foreign alpabet will be matched as well
    (type skarsgard to match Skarsgård)
    but please be aware that names like Zoë/Zoe, Chloë/Chloe are different.
    In case of multiple matches, the results
    will be restricted to the first 10 elements,""" + Style.RESET_ALL)
    request_actor = input(f"{Fore.BLUE + Style.BRIGHT}"
                          f"\nType an actor: {Style.RESET_ALL}")
    request_actor = request_actor.strip().lower()
    df_copy = df.copy(deep=True)
    df_copy = df_copy.applymap(
        lambda s: s.lower() if isinstance(
            s, str) else s)
    search = False
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
        welcome()
    else:
        print(f"""{Fore.YELLOW + Style.BRIGHT}
This actor is not present in the database{Style.RESET_ALL}\n""")
        welcome()


def get_director():
    """
    applies .lower() to input and copy of df for accurate comparison
    search for matches in the dfcopy of Director column,
    if none found, encodes entries to match search for extend ASCII chars,
    if none found, display message. else display output.
    """
    print(
        Fore.WHITE + Style.BRIGHT +
        """\n    Search by full or partial name.
    Type the words divided by a space.
    Characters from a foreign alpabet will be matched as well
    (type inarritu to match Iñárritu)
    but please be aware that names like Zoë/Zoe, Chloë/Chloe are different.
    In case of multiple matches,
    the results will be restricted to the first 10 elements""")
    request_director = input(f"{Fore.BLUE + Style.BRIGHT}"
                             f"\nType a director: {Style.RESET_ALL}")
    request_director = request_director.lower().strip()
    df_copy = df.copy(deep=True)
    df_copy['Director'] = df_copy['Director'].str.lower()
    search = False
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
        welcome()

    else:
        print(f"""{Fore.YELLOW + Style.BRIGHT}
This director is not present in the database{Style.RESET_ALL}\n""")
        welcome()


def search_choice():
    """
    accepts input strings exit/help or string within range of options.
    calls validation function on user input.
    calls functions relative to the user's choice.
    """
    while True:
        user_input = input(
            Style.BRIGHT +
            Fore.BLUE +
            "\nType your search criteria - ACTOR, GENRE, DIRECTOR, TITLE: " +
            Style.RESET_ALL)
        user_input = user_input.lower().strip()
        if user_input.lower().strip() == "exit":
            print(Fore.YELLOW + Style.BRIGHT + 'Thank you!' + Fore.BLUE +
                  Style.BRIGHT + ' Goodbye!')
            sleep(3)
            clear()
        elif user_input.lower().strip() == 'help':
            help_text()

        if validate_search_choice(user_input):
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
    """
    raise error msg if input is not int and not within the options.
    function is called by search_choice function.
    """
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
    """
    calls the input functions,
    displays header when program first runs.
    """
    get_help()
    data_choice()
    search_choice()


title = pyfiglet.figlet_format(" Movie DB 2000s", font="slant")
print(Fore.YELLOW + Style.BRIGHT + title)
print(Style.BRIGHT + Fore.YELLOW + """
    Welcome to the 2000s Movie Database! """ + Style.BRIGHT + Fore.WHITE + """
    The database contains""", df['Title'].count(), """films released between 2000 and 2009.
    Information include title, genre, year, language and country of production,
    content rating, duration, aspect ratio, director, cast, budget
    box office revenue, number of reviews and IMDB score.""" +
      Fore.YELLOW + Style.BRIGHT + """
    Get statistics, the top 10 lists or search by criteria.\n""")

main()
