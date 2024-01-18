# TRAIN YOUR LITHUANIAN VOCABULARY
#### Video Demo: https://youtu.be/mss_APF75G4
#### Description:
Final project for CS50's Programming with Python.

Program TRAIN YOUR LITHUANIAN VOCABULARY is a game for training Lithuanian nouns (level A1-A2).

The game has 2 levels.

On the first level a user gets a random pair of Lithuanian noun and English translation. The user just answers 'y' or 'n' depending on whether she or he considers the pair to be correct or not correct.

On the second level a user gets a random Lithuanian noun and should type translation into English.

At any level the user chooses the number of questions for the round herself / himself and gets her / his score at the end of the round.

#### Technologies and libraries
Project is created with python 3 and uses libraries *random* and *csv*.

#### Functions
Program has 4 functions:
* **get_level()** (gets level 1 or 2 from the user)
* **get_quest_number()** (gets number of questions for the round from the user)
* **function_level_1** (handles user answers on the first level)
* **function_level_2** (handles user answers on the second level)

#### Structure
Project consists of:
* *project.py* (main project file)
* *project.csv* (database for nouns)
* *test_project.py* (for unit tests)
* *README.md*

#### Features
* Program is based on a database of mine consisting of 593 basic Lithuanian nouns.
    - For the second level program randomly chooses any number of nouns from the entire database.
    - For the first level program extracts a random sample of 5 pairs from the database. The number of 5 was chosen through trial: with bigger number of nouns the game loses its meaning (the answer almost always would be 'n').
* If user's input is not valid, program always re-prompts for a valid input.

#### Contact
Anzhalika Dubasava, anzhalikad@gmail.com

Linkedin: https://www.linkedin.com/in/adubasava/
