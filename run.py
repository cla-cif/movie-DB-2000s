import pandas as pd

pd.set_option("display.max_rows", 20)

gsheetid = "1MjifIi5MPPGBP3635xWTrpef3RWngXcWgKjnCsaoE6Y"
sheet_name = "Data"
gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(
    gsheetid, sheet_name)
df = pd.read_csv(gsheet_url)

"""
WELCOME!
"""

def welcome():
    while True:
        welcome_input = input("Please type data or search: ")
        welcome_input = welcome_input.lower()

        if validate_welcome(welcome_input):
            print("All right!")
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
        print('please provide a suitable choice\n')
        return False

"""
DATA
"""


"""
DATA AT A GLANCE
"""

def budget():
    df_budget = df['Budget'].mean().astype(int)
    print('The average budget is', df_budget, '$' '\n')
    print('Do you want to do a new search or find data?')
    welcome()


def score():
    df_score = df['IMDB Score'].mean().round(1)
    print('The average score got on IMDB is', df_score, '\n')
    print('Do you want to do a new search or find data?')
    welcome()


def language():
    df_language = df['Language'].value_counts().sort_values(ascending=False)
    print('Number of movies per language\n', df_language, '\n')
    print('Do you want to do a new search or find data?')
    welcome()


def year():
    df_year = df.groupby('Year', sort=False)['Country'].count()
    print('number of movies producted per year\n', df_year, '\n')
    print('Do you want to do a new search or find data?')
    welcome()

"""
RANKINGS
"""

def score_country():
    df_score_country = df.groupby('Country', sort=False)[
        'IMDB Score'].mean().round(1).sort_values(ascending=False)
    print('Countries with the highest IMDB Score\n', df_score_country, '\n')
    print('Do you want to do a new search or find data?')
    welcome()


def highest_score():
    sort_highest_score = df[['Title', 'IMDB Score']].sort_values(by='IMDB Score', ascending=False)
    print('The best movies of the decade\n', sort_highest_score.head(10), '\n')
    print('Do you want to do a new search or find data?')
    welcome()


def lowest_score():
    sort_lowest_score = df[['Title', 'IMDB Score']
                       ].sort_values(by='IMDB Score', ascending=True)
    print('The worst movies of the decade\n', sort_lowest_score.head(10), '\n')
    print('Do you want to do a new search or find data?')
    welcome()


def roi():
    df['ROI'] = (df["Gross Earnings"] / df["Budget"] * 100).round(2)
    sort_mostroi = df[['Title', 'ROI']].sort_values(
        by='ROI', ascending=False).dropna()
    print('The most profitable movies of the decade\n', sort_mostroi, '\n')
    print('Do you want to do a new search or find data?')
    welcome()


def profit():
    df['Profit'] = (df['Gross Earnings'] - df['Budget']).dropna().astype(int).apply(lambda x: f'{x:,}')
    sort_leastprofitable = df[['Title', 'Profit']].sort_values(by='Profit', ascending=True)
    print('Top 10 box-office flop\n', sort_leastprofitable.head(10), '\n')
    print('Do you want to do a new search or find data?')
    welcome()


def data_choice():
    while True:
        user_input = input("Enter a number: ")

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
                print('function not defined yet')
            break
              
    return user_input


def validate_data_choice(data):
    try:
        int(data)
    except ValueError:
        print('please provide a number\n')
    else:
        if 0 < int(data) < 11:
            return True
        else:
            print('not in range\n')


"""
SEARCH  
"""


def get_movie_info():
    request_movie = input("Enter a Title: ")
    request_movie = request_movie.lower().title()
    search = False
    for value in df.values:
        for item in value:
            if request_movie in str(item):
                search = True

    if search:
        movie_data = df.loc[(df['Title'].str.contains(request_movie))]
        print('All you need to know about the movie you were looking for\n', movie_data, '\n')
        print('Do you want to do a new search or find data?')
        welcome()
    else:
        print('The movie is not present in the database')
        print('Do you want to do a new search or find data?')
        welcome()


def get_movie_genres():
    request_genre = input("Enter a genre: ")
    request_genre = request_genre.lower().title()
    search = False
    for value in df.values:
        for item in value:
            if request_genre in str(item):
                search = True

    if search:
        mask = df['Genres'].str.contains(request_genre)
        movie_genre = df.loc[mask, ['Title', 'Year', 'Director', 'Actor1', 'Actor2', 'Actor3']]
        print('All the movies of the genre you were looking for\n', movie_genre, '\n')
        print('Do you want to do a new search or find data?')
        welcome()
    else:
        print('The genre is not present in the database')
        print('Do you want to do a new search or find data?')
        welcome()


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
        actor_data = df.loc[mask1 | mask2 | mask3, ['Title', 'Year', 'Genres', 'Director', 'Actor1', 'Actor2', 'Actor3']]
        print('All the movies of the actor you were looking for\n', actor_data, '\n')
        print('Do you want to do a new search or find data?')
        welcome()

    else:
        print('The actor is not present in the database')
        print('Do you want to do a new search or find data?')
        welcome()


def get_director():
    request_director = input("Enter a director: ")
    request_director = request_director.lower().title()
    search = False
    for value in df.values:
        for item in value:
            if request_director in str(item):
                search = True
    
    if search:
        mask = df['Director'].str.contains(request_director)
        director_data = df.loc[mask, ['Title', 'Year', 'Genres', 'Actor1', 'Actor2', 'Actor3']]
        print('All the movies from the director you were looking for\n', director_data, '\n')
        print('Do you want to do a new search or find data?')
        welcome()

    else:
        print('The director is not present in the database\n')
        print('Do you want to do a new search or find data?\n')
        welcome()


def search_choice():
    while True:
        user_input = input(
            "Do you want to search by actor, genre, director or title? ")
        user_input = user_input.lower()
        if validate_search_choice(user_input):
            print("All right!")
            if user_input == 'director':
                get_director()
            elif user_input == 'actor':
                get_actor()
            elif user_input == 'genre':
                get_movie_genres()
            elif user_input == 'title':
                get_movie_info()
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
        print('please provide a suitable choice\n')
        return False


def main():
    welcome()
    data_choice()
    search_choice()

print("Welcome to the 2000s Movie database\n")
print("What do you want to do today, get data or search?\n")

main()
