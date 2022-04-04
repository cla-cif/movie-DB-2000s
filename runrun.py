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