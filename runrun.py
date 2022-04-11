""" import libraries """
import pandas as pd


GSHEET_ID = "1MjifIi5MPPGBP3635xWTrpef3RWngXcWgKjnCsaoE6Y"
SHEET_NAME = "Data"
GSHEET_URL = f"https://docs.google.com/spreadsheets/d/{GSHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"  # noqa
df = pd.read_csv(GSHEET_URL)

"""
ORIGINAL CODE
    search = False
    for value in df.values:
        for item in value:
            if request_genre in str(item):
                search = True

"""
