import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

gsheetid = "1MjifIi5MPPGBP3635xWTrpef3RWngXcWgKjnCsaoE6Y"
sheet_name ="Data"
gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheetid, sheet_name)
df = pd.read_csv(gsheet_url)

df_budget = df['Budget'].mean().astype(int)
#print('The average budget is', df_budget, '$' '\n')

df_score = df['IMDB Score'].mean().round(1)
#print('The average score got on IMDB is', df_score, '\n')

df_year = df.groupby('Year', sort=False)['Country'].count()
#print('number of movies producted per year\n', df_year, '\n')

df_score_country = df.groupby('Country', sort=False)['IMDB Score'].mean().round(1).sort_values(ascending=False)
#print('Countries with the highest IMDB Score\n', df_score_country, '\n')

df_language = df['Language'].value_counts().sort_values(ascending=False)
#print('Number of movies per language\n', df_language, '\n')

sort_by_highest_score = df[['Title', 'IMDB Score']].sort_values(by='IMDB Score', ascending=False)
#print('The best movies of the decade\n', sort_by_highest_score.head(10), '\n')

sort_by_lowest_score = df[['Title', 'IMDB Score']].sort_values(by='IMDB Score', ascending=True)
#print('The worst movies of the decade\n', sort_by_lowest_score.head(10), '\n')


test = df[df['Genres'].str.contains('Romance')].count()
print('Number or romance movies', test)
df["NewCol"] = np.where(df['Genres'].str.contains('Comedy'), 'test', '')
sort_genre = df[['Title', 'NewCol']]
#print(sort_genre)
