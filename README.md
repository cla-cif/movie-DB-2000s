![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome to the 2000s Movie Database, the database contains 2100 films cathegorised by title, genre, year, director, cast, number of reviews (from critics and users) and IMDB score. 

The user gets an insight from the movie archive such as statistics and Top 10 lists, ranking the films. Users can also search by title, genres, director and cast to get specific information or find titles. 

[Here is the live version](https://movie-db-2000s.herokuapp.com/)

## How to use
The user is welcomed by a large title and a brief welcome message wich explains how to use the app. 
The app has two purposes: to get data and to run queries. The users are hence asked the question "What do you want to do today, gett data or search?"
Based on their answer "data" or "search" they will be presented the relative "section" of the app. 

### Data

### Search

## Features

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
