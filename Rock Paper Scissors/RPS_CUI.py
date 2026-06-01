import random
import os
sc = 0
su = 0
d=0
g=0
r=0
def clr():
    input("Press Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')
while True:
    try:
        u = int(input('''Enter your choice 
            1.rock
            2.paper
            3.scissors 
            4.score
            5.how to play 
            6.documentation
            7.exit:\n'''))
    except ValueError:
        print("Invalid input. Please enter a number.")
        clr()
        continue
    if u == 7:
        print("Thanks for playing!")
        break
    elif u == 6:
        print("""
=========================
ROCK PAPER SCISSORS
DOCUMENTATION
=========================

OVERVIEW
--------
Rock Paper Scissors is a menu-driven command-line game developed using Python. The game allows a player to compete against the computer in a series of rounds while maintaining a running score throughout the session.

The computer generates its moves randomly, ensuring fairness and unpredictability in gameplay. The application is designed to demonstrate fundamental programming concepts including user input handling, conditional logic, loops, functions, randomization, score management, and exception handling.

--------------------------------------------------

FEATURES
--------
The game includes the following features:

• Interactive Menu-Driven Interface
• Rock, Paper, Scissors Gameplay
• Random Computer Move Generation
• Real-Time Score Tracking
• Built-In Documentation
• Input Validation
• Exception Handling
• Cross-Platform Console Support
• Continuous Gameplay Until Exit

--------------------------------------------------

GAME MECHANICS
--------------
The game operates using the traditional Rock Paper Scissors rule set.

Available Moves:

• Rock
• Paper
• Scissors

Result Determination:

• Rock defeats Scissors
• Paper defeats Rock
• Scissors defeats Paper

If both participants select the same move, the round is declared a tie.

The computer's move is generated randomly for every round using Python's random module.

--------------------------------------------------

MENU STRUCTURE
--------------
The application consists of the following menu options:

1. Rock
2. Paper
3. Scissors
4. Score
5. Documentation / How To
6. Exit

Each option performs a specific task and allows the user to navigate through the application efficiently.

--------------------------------------------------

SCORE MANAGEMENT
----------------
The application maintains two independent score counters:

• Player Score
• Computer Score

After every completed round:

• A player victory increases the player score.
• A computer victory increases the computer score.
• Tie rounds do not affect either score.

Scores remain available throughout the current execution of the program.

--------------------------------------------------

INPUT VALIDATION
----------------
The application validates user input before processing.

Validation ensures that:

• Only valid menu selections are accepted.
• Non-numeric input does not cause program failure.
• Invalid choices are rejected gracefully.

Whenever invalid input is detected, the user receives a clear error message and is prompted to try again.

--------------------------------------------------

EXCEPTION HANDLING
------------------
The application includes exception handling mechanisms to improve reliability and user experience.

Handled Exceptions:

1. ValueError

Occurs when a user enters data that cannot be converted into an integer.

Examples include:

• Letters
• Symbols
• Empty input

When detected, the program displays an error message and safely returns control to the user.

--------------------------------------------------

ERROR RECOVERY
--------------
The game is designed to continue operating after invalid input.

Error recovery mechanisms ensure that:

• The application does not terminate unexpectedly.
• Users can correct mistakes without restarting the game.
• Menu navigation remains uninterrupted.

--------------------------------------------------

PROGRAM STRUCTURE
-----------------
The application is organized into several components.

Modules Used:

• random
• os

random Module:
Used to generate computer choices randomly.

os Module:
Used to clear the console screen and improve interface readability.

Function Used:

clr()

Purpose:
Provides a pause mechanism and clears the terminal screen after each operation.

Main Game Loop:
Controls gameplay, score management, menu navigation, and user interaction.

--------------------------------------------------

CURRENT LIMITATIONS
-------------------
The current version has the following limitations:

• Scores are not saved after the program closes.
• Match history is not stored.
• Multiplayer mode is not available.
• No graphical user interface is provided.
• Statistics beyond scores are not tracked.

--------------------------------------------------

FUTURE ENHANCEMENTS
-------------------
Potential improvements include:

• Best-of-Three Mode
• Best-of-Five Mode
• Match Statistics
• Win Percentage Tracking
• Score Saving Using Files
• Match History Storage
• Difficulty Levels
• Multiplayer Support
• Graphical User Interface (GUI)
• Online Gameplay Functionality

--------------------------------------------------

LEARNING OUTCOMES
-----------------
This project demonstrates practical implementation of:

• Variables and Data Types
• Conditional Statements
• Loops
• Functions
• Exception Handling
• Input Validation
• Random Number Generation
• Menu-Driven Programming
• Score Management
• Modular Program Design
• Cross-Platform Console Operations

--------------------------------------------------

DEVELOPER INFORMATION
---------------------

Developer Name : Aaron Shibu Mammen

Course         : Bachelor of Engineering (B.E.)

Branch         : Computer Science and Engineering (CSE)

Year           : First Year

GitHub         : aaroninplayz

--------------------------------------------------

AREAS OF INTEREST
-----------------

• Programming
• Software Development
• User Interface (UI) Design
• User Experience (UX) Design
• Artificial Intelligence (AI)
• Machine Learning
• Data Science
• Automation
• Cybersecurity
• Web Development
• Application Development
• Software Engineering
• Problem Solving
• Open Source Development
• Computer Science Fundamentals

--------------------------------------------------

PROJECT INFORMATION
-------------------

Project Name   : Rock Paper Scissors

Version        : 1.0

Language       : Python 3

Modules Used   : random, os

Project Type   : Command-Line Game

--------------------------------------------------

ABOUT THE DEVELOPER
-------------------
Aaron Shibu Mammen is a First-Year Bachelor of Engineering (B.E.) student specializing in Computer Science and Engineering (CSE).

This project was developed as part of the learning journey in programming and software development. It demonstrates the practical application of Python fundamentals including variables, loops, conditionals, functions, exception handling, randomization, and modular programming principles.

The project reflects an interest in building reliable, user-friendly software while strengthening foundational programming skills and problem-solving abilities.

--------------------------------------------------

VERSION INFORMATION
-------------------

Application Name : Rock Paper Scissors

Version          : 1.0

Language         : Python 3

Modules Used     : random, os

Platform Support : Windows, Linux, macOS

--------------------------------------------------

END OF DOCUMENTATION
--------------------------------------------------
""")
        clr()
        continue
    elif u == 5:
        print("""
=========================
HOW TO PLAY
=========================

WELCOME
-------
Welcome to Rock Paper Scissors, a classic game where you compete against the computer. The computer randomly selects a move each round, and the winner is determined according to the standard rules of the game.

GAME RULES
----------
The game consists of three possible moves:

1. Rock
2. Paper
3. Scissors

Winning Conditions:

• Rock defeats Scissors
• Paper defeats Rock
• Scissors defeats Paper

If both the player and the computer choose the same move, the round ends in a tie.

--------------------------------------------------

PLAYING THE GAME
----------------

Step 1:
Launch the program.

Step 2:
Select one of the following options from the main menu:

1. Rock
2. Paper
3. Scissors
4. Score
5. how to  play
6. documentation
7. Exit

Step 3:
Enter the corresponding number for your desired action.

Step 4:
The computer will automatically generate a random move.

Step 5:
The result of the round will be displayed.

Possible outcomes include:

• You Win
• Computer Wins
• Tie

Step 6:
Scores are automatically updated after every round.

--------------------------------------------------

VIEWING SCORES
--------------
Select Option 4 from the Main Menu to view the current scores.

The score section displays:

• Player Score
• Computer Score

Scores remain active until the program is closed.

--------------------------------------------------

DOCUMENTATION
-------------
Select Option 5 to view the game's documentation and usage guide.

--------------------------------------------------

EXITING THE GAME
----------------
Select Option 6 from the Main Menu.

The program will display a farewell message and terminate safely.

--------------------------------------------------

TIPS
----
• Think strategically rather than choosing randomly.
• Observe patterns in your own choices.
• Use the score tracker to monitor performance.
• Continue playing multiple rounds to improve results.

--------------------------------------------------

END OF HOW TO PLAY
--------------------------------------------------
""")
        clr()
        continue
    elif u == 4:
        print("====================")
        print("CURRENT STATISTICS")
        print("====================")
        print()
        print(f"Player Wins     : {su}")
        print(f"Computer Wins   : {sc}")
        print(f"Ties            : {d}")
        print(f"Games Played    : {g}")

        if g > 0:
            winrate = (su / g) * 100
        else:
            winrate = 0

        print()
        print(f"Win Rate        : {winrate:.2f}%")
        print()
        print("====================")
        clr()
        continue
    elif u == 1:
        u = 'rock'
        r=1
    elif u == 2:
        u = 'paper' 
        r=1
    elif u == 3:
        u = 'scissors'
        r=1
    elif u==420:
        print("Congratulations! You found the secret option!")
        r=int(input("Enter a number the number of times the geame to play on auto play: "))
        clr()

    else:
        print("Invalid choice. Please try again.")
        clr()
        continue  
    y=u
    x=False
    while r>0:
        if y==420:
            u= random.choice(['rock', 'paper', 'scissors'])
            x=True
        c= random.choice(['rock', 'paper', 'scissors'])
        print(f"You chose: {u}")
        print(f"Computer chose: {c}")

        if u == c:
            print("It's a tie!")
            d+=1
        elif (u == 'rock' and c == 'scissors') or (u == 'paper' and c == 'rock') or (u == 'scissors' and c == 'paper'):
            print("You win!")
            su+=1
        else:
            print("Computer wins!")
            sc+=1
        print(f"Your score: {su}")
        print(f"Computer's score: {sc}")
        g+=1
        if x!=True:
            clr()
        else:
            print(f"Round {g} completed.")
            os.system('cls' if os.name == 'nt' else 'clear')

        r-=1
    
    