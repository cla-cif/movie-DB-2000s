import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

gsheetid = "1MjifIi5MPPGBP3635xWTrpef3RWngXcWgKjnCsaoE6Y"
sheet_name = "Data"
gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(
    gsheetid, sheet_name)
df = pd.read_csv(gsheet_url)

"""
DATA AT A GLANCE
"""
df_budget = df['Budget'].mean().astype(int)
#print('The average budget is', df_budget, '$' '\n')

df_score = df['IMDB Score'].mean().round(1)
#print('The average score got on IMDB is', df_score, '\n')

df_language = df['Language'].value_counts().sort_values(ascending=False)
#print('Number of movies per language\n', df_language, '\n')

df_year = df.groupby('Year', sort=False)['Country'].count()
#print('number of movies producted per year\n', df_year, '\n')

"""
RANKINGS
"""

df_score_country = df.groupby('Country', sort=False)[
    'IMDB Score'].mean().round(1).sort_values(ascending=False)
#print('Countries with the highest IMDB Score\n', df_score_country, '\n')

sort_highest_score = df[['Title', 'IMDB Score']
                        ].sort_values(by='IMDB Score', ascending=False)
#print('The best movies of the decade\n', sort_by_highest_score.head(10), '\n')

sort_lowest_score = df[['Title', 'IMDB Score']
                       ].sort_values(by='IMDB Score', ascending=True)
#print('The worst movies of the decade\n', sort_by_lowest_score.head(10), '\n')

# I'VE CREATED A FUNCTION FOR THIS
gb_specific_genre = df.groupby(['Title', 'IMDB Score'])['Genres'].apply(
    lambda x: x[x.str.contains('War', case=False)])
#print('All the War movies\n', gb_specific_genre, '\n')

df['ROI'] = (df["Gross Earnings"] / df["Budget"] * 100).round(2)
sort_mostroi = df[['Title', 'ROI']].sort_values(
    by='ROI', ascending=False).dropna()
#print('The most profitable movies of the decade\n', sort_mostroi, '\n')

df['Profit'] = (df['Gross Earnings'] - df['Budget']
                ).dropna().astype(int).apply(lambda x: f'{x:,}')
sort_leastprofitable = df[['Title', 'Profit']
                          ].sort_values(by='Profit', ascending=True)
#print('Top 10 box-office flop\n', sort_leastprofitable.head(10), '\n')


"""
SINGLE QUERIES
"""

"""
def get_movie_info():
    request_movie = input("Enter a Title: ")
    if request_movie in df.values:
       movie_data = df.loc[(df['Title'].str.contains(request_movie, case=False))]
       print('All you need to know about the movie you were looking for\n', movie_data, '\n')
    else:
        print('The movie is not present in the database')
get_movie_info()
"""
"""
def get_movie_genres():
    request_genre = input("Enter a genre: ")
    if request_genre in df.values:
       movie_genre = df.loc[(df['Genres'].str.contains(request_genre))],
       print('All the movies of the genre you were looking for\n', movie_genre, '\n')
    else:
        print('The genre is not present in the database')
get_movie_genres()
"""

"""
def get_actor():
    request_actor = input("Enter an actor: ")
    if request_actor in df.values:
       actor_data = df.loc[(df['Cast'].str.contains(request_actor))],
       print('All the movies of the actor you were looking for\n', actor_data, '\n')
    else:
        print('The actor is not present in the database')
get_actor()
"""

"""
def get_director():
    request_director = input("Enter a director: ")
    if request_director in df.values:
       director_data = df.loc[(df['Director'].str.contains(request_director))],
       print('All the movies from the director you were looking for\n', director_data, '\n')
    else:
        print('The director is not present in the database')
get_director()
"""

def query_choice():
    while True:
        user_input = input(
            "Do you want to search by actor, genre, director or title?: ")

        if validate_query_choice(user_input):
            print("Data is valid!")
            break
    return user_input
query_choice()

def validate_query_choice(choice):
    choices = ['director', 'actor', 'genre', 'title']
    try:
        if str(choice) in choices:
            return True
        else:
            print('please provide a suitable input\n')


#DATA QUERIES

"""
def get_input():
    while True:
        user_input = input("Enter a number: ")

        if validate(user_input):
            print("Data is valid!")
            break
    return user_input


def validate(data):
    try:
        val = int(data)
    except ValueError:
        print('please provide a number\n') 
    else:
        if 0 < int(data) < 11:
            return True
        else:
            print('not in range\n')


def main():
    get_input()

print("Welcome to the 2000s Movie database\n")
print("Please provide a number between one and ten")

main()
"""
