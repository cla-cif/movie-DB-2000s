""" import libraries """
import pandas as pd

GSHEET_ID = "1MjifIi5MPPGBP3635xWTrpef3RWngXcWgKjnCsaoE6Y"
SHEET_NAME = "Data"
GSHEET_URL = f"https://docs.google.com/spreadsheets/d/{GSHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"  # noqa
df = pd.read_csv(GSHEET_URL)




# ORIGINAL CODE
def get_film_info():
    """
    applies to input .title() to match dataframe's entries case 
    search for matches in the Title column,
    if none found, display message and call welcome function.
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
    request_film = request_film.lower().title().rstrip()
    search = False
    for value in df['Title']:
        if request_film in value:
            search = True

    if search:
        film_data = df.loc[(df['Title'].str.contains(request_film))]
        print(f"""{Fore.YELLOW + Style.BRIGHT}
All you need to know about the film you were looking for:
{Style.RESET_ALL}{film_data}\n""")
        welcome()
    else:
        print(f"""{Fore.YELLOW + Style.BRIGHT}
This film is not present in the database{Style.RESET_ALL}\n""")
        welcome()