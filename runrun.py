import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import unicodedata2

gsheetid = "1MjifIi5MPPGBP3635xWTrpef3RWngXcWgKjnCsaoE6Y"
sheet_name = "Data"
gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(
    gsheetid, sheet_name)
df = pd.read_csv(gsheet_url)

def get_actor():
    request_actor = input("Enter an actor: ")
    request_actor = request_actor.lower().title()
    if request_actor in df[['Actor1', 'Actor2', 'Actor3']]:
        mask1 = df['Actor1'].str.contains(request_actor)
        mask2 = df['Actor2'].str.contains(request_actor)
        mask3 = df['Actor3'].str.contains(request_actor)
        actor_data = df.loc[mask1 | mask2 | mask3, ['Title', 'Year', 'Genres', 'Director']]
        print('All the movies of the actor you were looking for\n', actor_data, '\n')
    else:
        print('The actor is not present in the database')
get_actor()