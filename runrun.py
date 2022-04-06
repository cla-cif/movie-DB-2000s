import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import unicodedata2
from colorama import Fore, Back, Style
import pyfiglet


gsheetid = "1MjifIi5MPPGBP3635xWTrpef3RWngXcWgKjnCsaoE6Y"
sheet_name = "Data"
gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(
    gsheetid, sheet_name)
df = pd.read_csv(gsheet_url)


"""
test = unicodedata2.normalize("NFD", "Skarsgård").encode('WINDOWS-1252', 'ignore')
print('it works as a single methond', test)

test2 = unicodedata2.normalize("NFD", "Zoë ").encode('ascii', 'ignore')
print('it works as a single methond', test2)

df['Actor3'] = (df['Actor3'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8'))
print(df['Actor3'])
"""

def budget():
    df_budget = df['Budget'].mean().astype(int)
    print('The average budget is', df_budget, '$' '\n')
budget()

print("""there are""",
      df['Title'].count(),
      """movies""")


df_rating_score = df.groupby('Content Rating', sort=False)['IMDB Score'].mean().round(1).sort_values(ascending=False)
df_rating_score.filter(df['Content Rating'] =='Unrated')
print('groupby Content first\n', df_rating_score)

"""
df['Content Rating'] = df[df['Content Rating'] != 'Unrated']
df_rating_score = df.groupby('Content Rating', sort=False)['IMDB Score'].mean().round(1).sort_values(ascending=False)
#print(df_rating_score)

grouped = df.groupby('Content Rating')['IMDB Score'].mean().round(1).sort_values(ascending=False)
grouped.filter(lambda x: x['Content Rating']=='Unrated')
#(grouped)
"""