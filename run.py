import pandas as pd

gsheetid = "1MjifIi5MPPGBP3635xWTrpef3RWngXcWgKjnCsaoE6Y"
sheet_name ="Data"
gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheetid, sheet_name)
df = pd.read_csv(gsheet_url)

by_year = df.groupby('Year', sort=False)['Country'].count()
#print('in these years have been producted\n', by_year)

print('the movies with score 8 or higher')
print(df[(df['IMDB Score'] > 8.0)])

