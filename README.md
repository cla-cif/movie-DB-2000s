![Header](https://github.com/cla-cif/movie-DB-2000s/blob/main/screenshot/title.png)
#
Welcome to the 2000s Movie Database, the dataset contains 2100 films released between 2000 and 2009. Data points include title, genre, year, language and country of production, content rating, duration, aspect ratio, director, cast, budget, box office, number of reviews (by critics and users) and IMDB score. 

The Heroku-based command line interface (CLI) allows the user to browse the dataset and retrieve statistics, rankings and specific information.
The instructions are extremely simply written and require only a minimum of interaction to achieve the desired result.

[Here is the live version](https://movie-db-2000s.herokuapp.com/)

## Content
 [How it's done](#How-it's-done)<br>
 [How it works](#How-it-works)<br>
 [Features](#Features)<br>
 [Testing](#Testing)<br>
 [Technologies](#Technologies-used)<br>
 [Deployment](#Deployment)<br>
 [Credits](#Credits)<br>

## How it's done
### How I developed this project: my story told through the Design Thinking Process

This project is inspired to the five Stages of Design Thinking and its further development will stricly follow the same [principles](https://canvas.unl.edu/courses/73802/pages/5-stages-of-design-thinking?module_item_id=1968000). 

### Define
> I'm a film __blogger__. I want to write about what ingredients make a film successful, and I want to do this by analysing film-related data from the last few decades. I also want to be able to __explore and query__ my database whenever I write an article. But __I don't know how to get meaningful information__ from my database.

__I turned this problem into an opportunity.__ <br>
I tried to understand why this problem is important to the blogger by getting to the heart of the matter and developing a targeted solution from there, keeping this question in mind: _"What solves the problem according to the blogger's needs and goals?"_ I shared the blogger's vision and hit their needs right where they needed to be addressed. <br>
To do this, I researched film blogs and conducted interviews that led to the creation of a potential user persona.

### Empathise
_This program has been coded thinking at the potential needs of film bloggers in their thirties/forties with moderate to low IT skills who want to gain insights into their personalised film database and tell their followers about it._

__Let us call our blogger Nastya.__

- She wants to set up her database on her own with information about films that is relevant to her.
- The database should be hosted on a software Nastya is familiar with. 
- She wants to gain insight into this data through an "old-fashioned" and easy-to-use interface. 
- Nastya wants a developer to code a program to elaborate the data and turn it into the information she is looking for and can access through the interface. 
- She has followers to whom she needs to deliver content, so it is important that the developer doesn't break this chain of expectations. Therefore, she is keen to find a developer with whom she can establish a close working relationship.

### Ideate
The brainstorming phase followed by research, challenges and discussions lead to the integration of the following tools to find a solution to the stated problem. 
- [Python](https://docs.python.org/3/) and its libraries are ideal for working with small dataframes.
- The Heroku-based app provides an easy-to-use solution with an old-fashioned interface. (What is [Heroku](https://en.wikipedia.org/wiki/Heroku))
- [Google Sheets](https://en.wikipedia.org/wiki/Google_Sheets) can be shared, are intuitive and easy to edit.
- [GitHub](https://en.wikipedia.org/wiki/GitHub) is the go to solution for software development.

### Prototype
And that is how I arrived at the [current prototype](https://movie-db-2000s.herokuapp.com/). It is a scaled-down version of the main idea with a demo of the potential features: <br> SEARCH the database by keywords and get pre-calculated DATA. 
- The functions have been developed with the user's goal in mind and designed so that the user does not get lost when using the programme. 
- The prompts are obvious, short and direct, but a HELP option is always available. 

Other important points are:
  - the consistency of the prompts in colour and language, 
  - the constant availability of information and functions, 
  - the creation of a recursive architecture to avoid dead ends, 
  - the handling of invalid inputs and the avoidance of unexpected behaviour. 

>My personal challenge was to put myself in the shoes of the user: What is clear, obvious and self-evident to the developer may not be to the user.

### Test
I brought together people who matched the _persona_ aka our film blogger Nastya, wich have different IT abilities. <br>
I presented the prototype to them and asked them to comment and raise questions while using the app. <br>
I listened to their comments, observed their reactions, took notes and showed my appreciation for their feedback. 
>I then used their feedback to go to-and-fro the Design Thinking stages.

### The guiding principles
This app, created with Heroku, offers simple functions but is well structured to facilitate further development, expansion of the dataset and troubleshooting. 

I believe that in development, work is better than rework. _Adding_ features according to the client's and team's inputs is __more efficient and time-wise__ than _Removing_ programme features that the developer has spent time on but the client doesn't actually need.

My goal is to meet the clients' needs by taking their suggestions and frequently keeping in touch with them through chat, emails and video calls. 
This way I can make timely and frequent adjustments and fix problems as they arise. I believe in offering a __tailor-made solution__ that __adds value__ to the client. 

My promise to the client is that I'll take care of all phases of development while striving for improvement. The client is on board with the developer through the _plan > design > develop > test > release > review_ cicrle. I'm highly motivated to develop this project and want to assemble a team of goal-oriented, autonomous and empowered programmers.

Read more about the guiding principles of [Agile Development](https://www.agilealliance.org/agile101/)

## How it works
![Welcome](https://github.com/cla-cif/movie-DB-2000s/blob/main/screenshot/welcome.png)
- The user is welcomed by a large title and a short welcome message presenting the dataframe (database) and its main features. 
- The app has two main features: display processed data and perform queries.
- Side features are HELP and EXIT which can be invoked at any point by typing the desired feature after any question. 
- The first time the app is launched, the user is offered the choice to get HELP, EXIT the program or press the Enter key to continue (especially in case the user is already familiar with the app and wants skip the HELP section)
- Throgh a series of questions, the user is lead to the desired output. 
- Each answer (input) from the user is verified. If the check fails, the user is prompted to provide a suitable input.
![Error](https://github.com/cla-cif/movie-DB-2000s/blob/main/screenshot/error.png)
- After each result (output), the user is returned to the main question and can chose again how to explore the database (SEARCH/DATA).
![After output](https://github.com/cla-cif/movie-DB-2000s/blob/main/screenshot/after-output.png)
- The app wont terminate unless the user types exit, closes the window or refreshes the page.

### Flowchart

A flowchart of the program's main process was created with [Lucid.app](https://lucid.app/documents).
![Flowchart](https://github.com/cla-cif/movie-DB-2000s/blob/main/screenshot/flowchart.png)

### Data option
![Data Option](https://github.com/cla-cif/movie-DB-2000s/blob/main/screenshot/data.png)
The option is available by typing __data__ in response to this question _Type SEARCH or DATA to explore the database:_ which will be asked after each output.
Users are offered ten options with pre-calculated statistics and rankings to choose from.
1.  The average budget, score and duration of this films'decade.
2.  Number of films in each language.
3.  Number of films produced each year.
4.  The most prolific directors of the decade and their scores.
5.  Top 10 countries that produced films with the highest IMDB score.
6.  The 10 best films of the decade.
7.  The 10 worst films of the decade.
8.  The most profitable films in terms of return of investment.
9.  Top 10 box-office flops: the most unprofitable films.
10.  The content ratings and their average IMDB Score. <br>

After the choice is validated and the output displayed, the user is asked whether he wants to retrieve the data again or perform a search.

### Search option
![Search Option](https://github.com/cla-cif/movie-DB-2000s/blob/main/screenshot/search.png)
The option is available by typing __search__ in response to this question _Type SEARCH or DATA to explore the database:_ which will be asked after each output.
- Users can search the dataset by title, genre, actor and director. 
- Matching is also possible with partial text but limited to 10 results due to Heroku's terminal constraints (80 characters by 24 rows), so a targeted entry will yield accurate results. 
- Searching by title is the only query that returns all available information (genre, year, language and country of production, content rating, duration, aspect ratio, director, cast, budget, box office, number of reviews and IMDB score). 
- The other options, which are likely to find multiple matches, display only the most relevant information (title, genre, director, cast and IMDB score) to improve readability given the aforementioned Heroku's terminal limitations mentioned above.

### Exit option
![Exit Option](https://github.com/cla-cif/movie-DB-2000s/blob/main/screenshot/exit.png)
The exit option can be called by typing __exit__ after each prompt. The function prints the message _Thank you! Goodbye!_ clear the screen and causes the program to quit after 3 seconds. 

### Help option
![Help Option](https://github.com/cla-cif/movie-DB-2000s/blob/main/screenshot/help.png)
The help option can be called by typing __help__ after each prompt. The function provides basic information about the dataframe and instructions about how to explore the program.

## Features
All functions have a general purpose and can be applied to a similar dataset or, for this particular project, allow the current dataset to be extended with minimal further implementation.

### Existing Features
- The app is intuitive, the instructions are clear and simple, requiring minimal interaction from the user to achieve the result. 
- The text displayed on the black background of Heroku's CLI is legible and bright. The four colours (blue, yellow, red, white) are chosen consistently to differentiate instructions, messages, errors and outputs. 
- Input isn't case-sensitive, but output is consistently presented with the first letter capitalised. 
- The code is iterative so that users can perform multiple searches without restarting the program. 
- From the Heroku app link, the program can be restarted any time by clicking the red "Run Program" button on the Heroku app page. 

### Future Features
Some potential features include:
- Searches possible with two or more options at the same time (e.g.: search by genre AND actor, search by actor AND director). 
- A collection of films from the 90s and 10s to be added to the dataset.
- Additional statistics and lists. 
- Deployment with [Jupyter Lab](https://jupyter.org/) to create meaningful istograms, distributions and charts.

> Future features will be based on the users' requests and consequent necessities.

## Testing
I manually tested this project throughout the development process by doing the following:
 - I ran the code through the PEP8 linter.
 - Given invalid input and checked the logical and visual consistency of the error messages.
 - Entered substrings, extended ASCII characters, lower and upper case letters. 
 - Checked how many lines to display for better readability. 
 - Tested colours and their consistnecy for better readability.
 
 > By using it, the user will test the program and will be asked to provide feedback

### Issues
  The program has so far proven to be free of arithmetic, syntax, resource, multi-threading and interfacing bugs. 
  The program operates correctly and doesn't terminate abnormally. 
  The following logical errors provided undesired output. While the output was consitent with the input, a much broader result was desired. 

#### Fixed
_Matching is not possible with a partial string. e.g. the title must be complete, actor/director must searched by full name in order to display the desired result._ 
 - Implementation of a nested loop to work efficiently with a multi-dimensional data structure like this dataset. If the substring provided by the user was matched by iterating through the spreadsheet and its columns (this dataset is a list that contains other lists), boolean variable returns true and the output displayed. 

_Extended ASCII characters (character code 128-255) present in some names couldn't be matched providing printable ASCII characters (character code 128-255)._ 
 - The dataframe is parsed twice (looking for printable and extended ASCII chars) before informing the user that no matches were found. To match extended ASCII, the normalize method is applied to the dataframe. 
[Example of the output](https://github.com/cla-cif/movie-DB-2000s/blob/main/screenshot/normalize-bugfix.png)

#### Remaining
The terminal constraints don't allow to display large results and graphs.

### Validator
- PEP8: no errors were returned from the [PEP8 validator](http://pep8online.com/). 

## Technologies used
The project is coded with Python and relies on [pandas 1.4.2:](https://pypi.org/project/pandas/) to analyse data.

### Languages used

-   [Python](https://docs.python.org/3/)

### Frameworks, Libraries & Programs Used

- [pandas 1.4.2:](https://pypi.org/project/pandas/) which was installed along with [seaborn 0.11.2](https://pypi.org/project/seaborn/)
- [colorama 0.4.4](https://pypi.org/project/colorama/)
- [pyfiglet 0.8.post1](https://pypi.org/project/pyfiglet/)
- [pycodestyle 2.8.0](https://pypi.org/project/pycodestyle/)
--
- The dataset is a [Google Sheet](https://www.google.com/sheets/about/) file. A copy of the dataset is [available](https://github.com/cla-cif/movie-DB-2000s/blob/main/movie-DB-2000s.xlsx) in this repository. 

## Deployment
The project is coded and hosted on GitHub and deployed with [Heroku](https://www.heroku.com/). 

### Creating the Heroku app 
The steps needed to deploy this projects are as follows:

1. Create a `requirement.txt` file in GitHub, for Heroku to read, listing the dependancies the program needs in order to run.
2. `push` the recent changes to GitHub and go to your [Heroku account page](https://id.heroku.com/login) to create and deploy the app running the project. 
3. Chose "CREATE NEW APP", give it a unique name, and select a geographical region. 
4. From the _Settings_ tab, configure the environment variables (_config var_ section).
5. Copy/paste the `CREDS.json` file, if the project has credentials, in the `VALUE` field, type `CREDS` in the corresponding KEY box, click the "ADD" button.
6. Create another config var, set `PORT` as KEY and assign it the VALUE `8000`.
7. Add two buildpacks from the _Settings_ tab. The ordering is as follows:
   `heroku/python`
   `heroku/nodejs`
8. From the _Deployment_ tab, chose GitHub as deployment method, connect to GitHub and select the project's repository. 
9. Click to "Enable Automatic Deploys " or chose to "Deploy Branch" from the _Manual Deploy_ section. 
10. Wait for the logs to run while the dependencies are installed and the app is being built.
11. The mock terminal is then ready and accessible from a link similar to `https://your-projects-name.herokuapp.com/`

### Forking the Repository

By forking this GitHub Repository you make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository. The steps to fork the repository are as follows:
1. Locate this [GitHub Repository](https://github.com/cla-cif/movie-DB-2000s) of this project and log into your GitHub account. 
2. Click on the "Fork" button, on the top right of the page, just above the _Settings_. 
3. Decide where to fork the repository (your account for instance)
4. You now have a copy of the original repository in your GitHub account.

### Making a local clone

Cloning a repository pulls down a full copy of all the repository data that GitHub.com has at that point in time, including all versions of every file and folder for the project. The steps to clone a repository are as follows:
1. Locate this [GitHub Repository](https://github.com/cla-cif/movie-DB-2000s) of this project and log into your GitHub account. 
2. Click on the "Code" button, on the top right of the page, next to the green "Gitpod" button. 
3. Chose one of the available options: Clone with HTTPS, Open with Git Hub desktop, Download ZIP. 
4. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
5. Open Git Bash. [How to download and install](https://phoenixnap.com/kb/how-to-install-git-windows).
6. Chose the location where you want the repository to be created. 
7. Type:
    ```
    $ git clone https://github.com/cla-cif/movie-DB-2000s.git
    ```
8. Press Enter, the following lines will appear and your repository is now created.
    ```
   Cloning into 'movie-DB-2000s'...
    remote: Enumerating objects: 257, done.
    remote: Counting objects: 100% (257/257), done.
    remote: Compressing objects: 100% (182/182), done.
    remote: Total 257 (delta 157), reused 158 (delta 72), pack-reused 0Receiving obj
    Receiving objects:  81% (209/257)
    Receiving objects: 100% (257/257), 54.76 KiB | 549.00 KiB/s, done.
    Resolving deltas: 100% (157/157), done.
    ```
9. Click [here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) for a more detailed explaination. 
    
## Credits

-  All content written by developer Claudia Cifaldi - [cla-cif](https://github.com/cla-cif) on GitHub. 
-  The template used for this project belongs to CodeInstitute - [GitHub](https://github.com/Code-Institute-Submissions) and [website](https://codeinstitute.net/global/).
- The dataset is part of Kaggle's ["The Movies Dataset"](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset) under CC0: Public Domain Licence. 

##
[Here is the live version](https://movie-db-2000s.herokuapp.com/)
##
[Link to top](#)
