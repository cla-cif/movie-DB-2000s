![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome to the 2000s Movie Database, the dataset contains 2100 films released between 2000 and 2009. Data points include title, genre, year, language and country of production, content rating, duration, aspect ratio, director, cast, budget, box office, number of reviews (by critics and users) and IMDB score. 

The Heroku-based command line interface (CLI) allows the user to browse the dataset and retrieve statistics, rankings and specific information.
The instructions are extremely simply written and require only a minimum of interaction to achieve the desired result.
[SOURCE](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset)

[Here is the live version](https://movie-db-2000s.herokuapp.com/)

## How to use
The user is welcomed by a large title and a short welcome message explaining how to use the app. 
The app has two tasks: display processed data and perform queries. 
The app is based on an iterative process that the user can interrupt at any time when prompted for input. 
On the first iteration, the user is asked the question, "What do you want to do today, get data or search?"
Depending on whether they answer "data" or "search", they'll be prompted for further choices that will lead to the desired output. 
Each answer (input) from the user is verified. If the check fails, the user is prompted to provide a suitable input.
After each output, the user is returned to the beginning and can choose to perform a new search or retrieve data.

### Data option
Users are offered ten options with pre-calculated statistics and rankings to choose from.
        1:  The average budget, score and duration of this films'decade.
        2:  Number of films in each language.
        3:  Number of films produced each year.
        4:  The most prolific directors of the decade and their scores.
        5:  Top 10 countries that produced films with the highest IMDB score.
        6:  The 10 best films of the decade.
        7:  The 10 worst films of the decade.
        8:  The most profitable films in terms of return of investment.
        9:  Top 10 box-office flops: the most unprofitable films.
        10  The content ratings and their average IMDB Score.
After the choice is validated and the output displayed, the user is asked whether he wants to retrieve the data again or perform a search.

### Search option
Users can search the dataset by title, genre, actor and director. 
Matching is also possible with partial text but limited to 10 results due to Heroku constraints, so a targeted entry will yield accurate results. 
Searching by title is the only query that returns all available information (genre, year, language and country of production, content rating, duration, aspect ratio, director, cast, budget, box office, number of reviews and IMDB score). 
The other options, which are likely to find multiple matches, display only the most relevant information (title, genre, director, cast and IMDB score) to improve readability given the aforementioned Heroku constraints.

## Features
The app is intuitive, the istructions are clear and simple, only a minimal interaction is required from the user to achieve the result. 
The text displayed on the black backgroun of Heroku's CLI is highly readable and bright. Four colours (blue, yellow, red, white) are chosen consistently to differenciate istructions, features, error messages and output. 
The input is case insensitive, but the output is consistently presented with "title" case (First letter is capital). 
The code is iterative to allow the users multiple searches wihtout restart the program. 
The user can quit at any time by typing "exit". The CLI will be cleared after three seconds. The program can be run again by clicking the "Run Program"

### Existing Features

### Future Features

## Data Model 

## Testing

### Bugs (Solved / Remaining)

### Validator

## Deployment

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Credits

## Creating the Heroku app


## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!
