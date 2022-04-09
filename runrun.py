import pandas as pd


gsheetid = "1MjifIi5MPPGBP3635xWTrpef3RWngXcWgKjnCsaoE6Y"
sheet_name = "Data"
gsheet_url = """https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}""".format( # noqa
    gsheetid, sheet_name)
df = pd.read_csv(gsheet_url)


def get_actor():

    request_actor = input("Enter an actor: ")
    request_actor = request_actor.lower().title()
    search = False
    for value in df.values:
        for item in value:
            if request_actor in str(item):
                search = True

    if not search:
        df['Actor1'] = (
            df['Actor1'].str.normalize('NFKD').str.encode(
                'ascii', errors='ignore').str.decode('utf-8'))
        df['Actor2'] = (
            df['Actor2'].str.normalize('NFKD').str.encode(
                'ascii', errors='ignore').str.decode('utf-8'))
        df['Actor3'] = (
            df['Actor3'].str.normalize('NFKD').str.encode(
                'ascii', errors='ignore').str.decode('utf-8'))
        for value in df.values:
            for item in value:
                if request_actor in str(item):
                    search = True

    if search:
        mask1 = df['Actor1'].str.contains(request_actor)
        mask2 = df['Actor2'].str.contains(request_actor)
        mask3 = df['Actor3'].str.contains(request_actor)
        actor_data = df.loc[mask1 | mask2 | mask3, [
            'Title', 'Genres', 'Director', 'Actor1', 'Actor2', 'Actor3',
            'IMDB Score']]
        print(
            'All the movies of the actor you were looking for\n',
            actor_data,
            '\n')
    else:
        print('The actor is not present in the database')
        print('\nDo you want to run a new search or find data?')


def get_director():
    request_director = input('\nType a director: ')
    request_director = request_director.lower().title()
    search = False
    for value in df.values:
        for item in value:
            if request_director in str(item):
                search = True
    if not search:
        df['Director'] = (
            df['Director'].str.normalize('NFKD').str.encode(
                'ascii', errors='ignore').str.decode('utf-8'))
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

    else:
        print('The director is not present in the database.\n')
        print('\nDo you want to run a new search or find data?')

