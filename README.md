# MasterMind

This simple terminal game allows people to play MasterMind, a logic game for children that came out in the 1970s. I learned this game as a kid when I was in primary school. This is a two player game where one player ('the codemaker') sets a color combination that the other player ('the codebreaker') must guess. To guess, the codebreaker simply enters a color code after which the codemaker provides feedback by placing key pegs of two different colors on the board. One color signals that the codebreaker has placed a color peg in the correct position while the other color signals that while the color peg is in the code, it is not in the correct position. With this feedback, the codebreaker will decypher the color code, but he loses if he does not manage to do it in the prescribed number of tries. The length of the code and the amount of tries available differed from edition to edition of this game, and in this computer version the player can set these parameters himself.

Take a look at the deployed website: <a href="https://pp3-mastermind.herokuapp.com/" target="_blank" rel="noopener">MasterMind</a>.

![Mastermind - The original game](/assets/readme-images/mastermind.jpg)
![Gameplay](/assets/readme-images/win.gif)

# Contents

* [**User Experience UX**](#user-experience-ux)
  * [User Stories](#user-stories)
  * [Design](#design) 
    * [Structure](#structure)
    * [Flowchart](#flowchart)
    * [Typography](#typography)
* [Features](#features)
  * [Existing Features](#existing-features)
    * [Explanations Screen](#game-explanations)
    * [Random Color Code Generation](#random-color-code-generation)
    * [Custom Difficulty Settings](#custom-difficulty-settings)
    * [Player Move Evaluation](#player-move-evaluation)
    * [Cheat Mode](#cheat-mode)
  * [Future Implementations](#future-implementations)
    * [Statistics](#statistics)
* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Python Modules Used](#python-modules-used)
  * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)
* [Testing](#testing)
  * [Testing User Stories](#testing-user-stories)
  * [Manual Testing](#manual-testing)
    * [Browser compatibility](#browser-compatibility)
    * [Python PEP8 Code Validation](#python-pep8-code-validation)
  * [Solved Bugs](#solved-bugs)
  * [Known Bugs](#known-bugs)
* [Deployment](#deployment)
  * [How to Deploy the Project on Heroku](#how-to-deploy-the-project-on-heroku)
  * [How to Fork the Repository on GitHub](#how-to-fork-the-repository-on-github)
  * [How to Clone the Repository on GitHub](#how-to-clone-the-repository-on-github)
* [Credits](#credits)
  * [Content](#content)
  * [Media](#media)
  * [Code](#code)
* [Acknowledgements](#acknowledgements)

# User Experience UX

## User Stories

  * As a user, I want to learn how the game works.

  * As a user, I want to play MasterMind in a difficulty setting fitting my skill level so that I won't feel frustrated while playing.

  * As a user, I want the game to help me visualize the board and colors of the pegs.

  [Back to top](<#contents>)

## Design

### Structure

  When the game starts, the player is shown a brief explanation of how the game works.
  After this, they can set their own difficulty level by setting the length of the code and the number of times they are allowed to guess before they lose. As experienced players will need about 5-7 tries to guess a code of 7 colors, the maximum amount of 10 tries gives beginners plenty of wiggling room. Shorter codes will generally require less tries.
  The player can then enter color codes to play. Colors have to be seperated with spaces, this information is always visible below the 'board'.
  After the player wins or loses, they are asked whether they want to play again. Choosing no will simply exit the game, but if players choose to play again, the game will loop back to setting the difficulty level.

### Flowchart

<br />
<details>
  <summary>Click to show flowchart</summary>

  #### ![Flowchart](/assets/readme-images/mastermind.drawio.png)
</details><br />


### Typography

  For the logo, I used the 'Big' Font available on [Patrick Gillespie](https://www.instagram.com/patorjk/)'s [Text to ASCII Art Generator](http://patorjk.com/software/taag/). It is easily readable and does not take up too much space.

  [Back to top](<#contents>)

# Features

## Existing Features

### Game Explanations

* The game starts with a short explanation of what it is and how it works.

  ![Explanations](/assets/readme-images/explanation.png)

  [Back to top](<#contents>)

### Random Color Code Generation

* The color code the player has to guess is generated randomly so that every game is different.

### Custom Difficulty Settings

  * The player can customize the difficulty of the game by setting the code length from 3-7 colors and the number of tries to a number between 4 and 10.

  ![Main Menu](/assets/readme-images/difficulty.png)

  [Back to top](<#contents>)

### Player Move Evaluation

  * Once the player enters his guesses the game automatically provides feedback by printing checkmarks, rhombi and Xs on the board.

### Cheat Mode

  * This was created mainly for testing purposes, but players can enter a cheat code (iseedeadpeople) to reveal the color code. In Warcraft III, this cheat code reveals the map.

  ![Cheat Mode](/assets/readme-images/cheatmode.png)

[Back to top](<#contents>)

## Future Implementations

### Statistics
  1970ies
  * Create statistics like 'x games won out of y attempts'.

[Back to top](<#contents>)

# Technologies Used

## Languages Used

  * Python

## Python Modules Used

  * [random](https://docs.python.org/3/library/random.html), for its choice function that I use to randomly generate the color codes
  * [os](https://docs.python.org/3/library/os.html), for its clear function that allows me to clear the screen
  * [time](https://docs.python.org/3/library/time.html), for its sleep function. This is used when error messages are displayed (e.g. invalid input) but also for dramatic effect when the player's guesses are evaluated

## Frameworks, Libraries & Programs Used

  * [Draw.io](https://draw.io) - To create a flowchart that illustrates the game's logic

  * [Git](https://git-scm.com/) - For version control

  * [GitHub](https://github.com) - To save and store my project files

  * [Heroku](https://heroku.com) - To deploy the project

  * [ScreenToGif](https://www.screentogif.com/) - To record gameplay for the documentation of this project

  * [Text ASCII Art Generator](https://patorjk.com/software/taag/#p=testall&h=3&f=Alpha&t=Mastermind) - For the logo displayed at the top of the board while playing

  [Back to top](<#contents>)

# Testing

## Testing user stories

  * As a user, I want to learn how the game works.

    -->  Users only need to read the explanation that's displayed when they start the game.

  * As a user, I want to play MasterMind in a difficulty setting fitting my skill level so that I won't feel frustrated while playing.

    -->  This is accomplished by setting code length and most of all by setting the number of allowed tries before the user loses. The game will always ask for these parameters at the start of every new game.

  * As a user, I want the game to help me visualize the board and colors of the pegs.

    --> This is done by printing a visual representation of the board to the terminal, with colored output where it makes things easier to read.

  [Back to top](<#contents>)

## Manual Testing

  * I play tested the game extensively. As this is a quite simple game, there are only a few places where problems can occur due to user input. 
  
  * In fact, there are only 5 places in the code where users are required to provide input, two of which are simple 'Press Enter to continue' messages where users may press other buttons, but this input is not assigned to anything or processed anywhere, so it will not result in errors:
  ```py
  input("Press Enter to continue...")
  ```

  * The other instances of user input were thoroughly tested. After fixing obvious issues (c.f. [Solved bugs](#solved-bugs)) I can no longer make the game crash or behave in any other way but the intended one.

    ![Input errors when settings game parameters](/assets/readme-images/input_validation.gif)

  * The game correctly triggers winning and losing behavior, no matter the code length or number of allowed tries.

  * Quitting game by entering 'quit' works as intended.

  * After starting a game, users can seperate the colors in their input with one or more spaces, just as intended.

  * Activating cheat mode works and shows the correct code.

  * Starting new games after winning or losing works.

  [Back to top](<#contents>)

### Browser compatibility

  * The deployed page was tested in Mozilla Firefox, Google Chrome, Microsoft Edge, Opera and Brave with no issues. Terminal output on Firefox appears to have a greenish tint in some places but it does not impact the functionality:

      ![Greenish output in Firefox](/assets/readme-images/firefox_greenish.png)

  [Back to top](<#contents>)

### Python PEP8 Code Validation

  * Tests using Code Institute's Linter did not show any issues:

    ![run.py](/assets/readme-images/run-linter.png)
    ![art.py](/assets/readme-images/art-linter.png)

  [Back to top](<#contents>)

## Solved Bugs

  * At an early stage of development the evaluation checkmarks, rhombi and 'X's weren't colored. When I eventually changed that, the game would not detect wins anymore because instead of
    ```py
    if playing_field[line_to_check]\
                      .count(f'{colored_text("???", "green")}') == \
                      len(code_to_guess):
    ``` 
    the code only checked for "???". Adding the f-string solved the problem.

  * There were a couple of issues when I wanted to add the possibility to start new games after winning or losing, before the game simply exited. A Code Institute tutor pointed out that I did not simply call main() at the end of my code and that had loops in place where main() could be called from two different points.
    \
  At that point the function that's now play_game() was my main() and there was more code at the root level. Renaming my main() to play_game(), wrapping the code that was not part of any functions into main() and only calling main() once, at the very end of the file, solved the problem.

  * There were multiple issues where the game would exit unexpectedly because I had not implemented good input validation. One example is when the game asks how long the generated code is supposed to be, it would throw value and type errors when the user would enter letters because the input is immediately processed by the int() function. This was solved with try and except:
    ```py
    try:
        code_length = int(input("How long do you want the color code "
                                "to be? (3-7) "))
        # try will catch input that's a string or multiple numbers, but not
        # numbers that are outside the specified range. This if-statement will.
        if code_length <= 2 or code_length >= 8:
            code_length = "error"
    except (TypeError, ValueError):
        code_length = "error"
    ```
    It later checks whether any of the input is equal to "error" and loops back if it is.

## Known Bugs

  * None.

[Back to top](<#contents>)

# Deployment

## How to Deploy the Project on Heroku

  1. Create a [Heroku](https://www.heroku.com/) account or sign into your existing account.
  2. On your Heroku dashboard, click the New button and then select 'Create new app'.\
    ![Creating a new app on Heroku dashboard](/assets/readme-images/create_new_app.png)

  3. Enter an app name, pick a region based on where you are in the world and then click 'Create app'.\
    ![Create New App Screen](/assets/readme-images/naming_the_app.png)

  4. On the 'Deploy' tab of your new project, connect your project to your Github account.\
    ![Connect Heroku project to Github](/assets/readme-images/connect_to_github.png)

  5. Now click the Settings tab and click the 'Reveal config vars' button.\
    ![Config Vars](/assets/readme-images/config_vars.png)

  6. Add a config var by entering PORT in the KEY field and 8000 in the VALUE field.\
    ![Setting 8000 PORT](/assets/readme-images/setting_8000_port.png)

  7. Scroll down to the Buildpacks section and click the 'Add buildpack' button.\
    ![Buildpacks section](/assets/readme-images/buildpacks_section.png)

  8. Add both the Python and Node.js buildpacks:\
    ![Click these to add buildpacks](/assets/readme-images/adding_buildpacks.png)

  9. It should look like this after you're done:\
    ![Added Buildpacks](/assets/readme-images/added_buildpacks.png)
  
  10. Back on the Deploy tab, scroll to the bottom and click 'Deploy Branch'. Optionally, you can also enable Automatic Deploys.
    ![Deploy the project](/assets/readme-images/deploy_project.png)


[Back to top](<#contents>)

## How to Fork the Repository on GitHub

1. In your browser, navigate to the [GitHub page of this project.](https://github.com/beckoningstranger/pp3-mastermind)
2. Click the 'Fork' button at the top right of the page. If you are not the owner of the project, it will not appear greyed out to you:

![Location of Fork button](assets/readme-images/howtofork.png)

[Back to top](<#contents>)

## How to Clone the Repository on GitHub

1. In your browser, navigate to the [GitHub page of this project.](https://github.com/beckoningstranger/pp3-mastermind)
2. Click the 'Code' button, make sure you have HTTPS selected and then click the button to copy the link to your clipboard as demonstrated in this GIF:

  ![How to Clone](assets/readme-images/howtoclone.png)

3. Open your IDE and either use the functionality it provides (many IDE offer buttons that help you clone repositories) and paste your link there to have your clone created or go to the terminal and type: 'git clone \[insert your link here\]'
4. Hit ENTER and wait for you local clone to be created.

[Back to top](<#contents>)

# Credits

## Content

  * All of the content was written by myself.

  * According to [the game's Wikipedia page](https://en.wikipedia.org/wiki/Mastermind_(board_game)) MasterMind was created by [Mordecai Meirowitz](https://en.wikipedia.org/wiki/Mordecai_Meirowitz).

## Media

  * The picture of the game used at the top of this README file was taken by user [ZeroOne](https://en.wikipedia.org/wiki/User:ZeroOne) over on Wikipedia. It is licensed under the [Creative Commons Attribution-Share Alike 2.0 Generic license](https://creativecommons.org/licenses/by-sa/2.0/deed.en). No changes to the image were made.

## Code

There were many times I searched the web for solutions to my problems. Here is where I actually took code and used it for this project: 
  
  * Trying to figure out how to output colored text in the terminal I looked at the colorama module. In the end I ran this code that I found [on Stackoverflow](https://stackoverflow.com/questions/61686780/python-colorama-print-all-colors)
    ```py
    from colorama import Fore
    from colorama import init as colorama_init
    colorama_init(autoreset=True)
    colors = dict(Fore.__dict__.items())
    print(colors)
    ```
    and simply wrote down all the ANSI codes that I wanted to use.

  * On [another Stackoverflow page](https://stackoverflow.com/questions/134934/display-number-with-leading-zeros) I learned how to print numbers with leading zeroes.

  * Creating the playing field, I iterate through a range of numbers in reverse order. Yet again, I found how to do that [on Stackoverflow](https://stackoverflow.com/questions/49539187/range-countdown-to-zero).

  * I wanted to print the solution and also what users entered in colored text, using my colored_text() function. The issue was that it would always cause a line break after every word. In an article on [stechies.com](https://www.stechies.com/python-print-without-newline/) I learned how to omit that linebreak.
  
  [Back to top](<#contents>)

# Acknowledgements

I would like to thank the following people

* Precious Ijege, my mentor, for providing feedback on my ideas and helping me create this project.

* Code Institute's tutors, who provided help when I needed it.

* My wife for proofreading my work.

[Back to top](<#contents>)