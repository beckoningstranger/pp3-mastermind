# MasterMind

This simple terminal game allows people to play MasterMind, a logic game for children that came out in the 1970ies. I learned this game as a kid when I was in primary school. This is a two player game where one player ('the codemaker') sets a color combination that the other player ('the codebreaker') must guess. To guess, the codebreaker simply enters a color code after which the codemaker provides feedback by placing key pegs of two different colors on the board. One color signals that the codebreaker has placed a color peg in the correct position while the other color signals that while the color peg is in the code, it's not in the correct position. With this feedback, the codebreaker will decypher the color code, but he loses if the does not manage to do it in the prescribed number of tries. The length of the code and the amount of tries available differed from edition to edition of this game, and in this computer version the player can set these parameters himself.

Take a look at the deployed website: <a href="https://pp3-mastermind.herokuapp.com/" target="_blank" rel="noopener">MasterMind</a>.

![Mastermind - The original game](/assets/readme-images/mastermind.jpg)
![Mastermind in the terminal](/assets/readme-images/mastermind_terminal.png)

# Contents

* [**User Experience UX**](#user-experience-ux)
  * [User Stories](#user-stories)
  * [Design](#design) 
    * [Structure](#site-structure)
    * [Typography](#typography)
* [Features](#features)
  * [Existing Features](#existing-features)
    * [Random Color Code Generation](#random-color-code-generation)
    * [Main Menu](#main-menu)
    * [Difficulty Menu](#difficulty-menu)
    * [Customize Difficulty Settings Menu](#customize-difficulty-settings-menu)
    * [How to Play Section](#how-to-play-section)
    * [Settings Menu](#settings-menu)
    * [Playing Field](#playing-field)
    * [Future Implementations](#future-implementations)
      * [Reveal zero squares automatically](#reveal-zero-squares-automatically)
      * [Leaderboards](#leaderboards)
      * [Statistics](#statistics)
  * [Accessibility](#accessibility)
* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)
* [Testing](#testing)
* [Deployment](#deployment)
  * [How to Deploy the Project on GitHub Pages](#how-to-deploy-the-project-on-github-pages)
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
  After this, they can set his own difficulty level by setting the length of the code and the number of times they are allowed to guess before they lose. As experienced players will need about 5-7 tries to guess a code of 7 colors, the maximum amount of 10 tries gives beginners plenty of wiggling room. Shorter codes will generally require less tries.
  The player can then enter color codes to play. Colors have to be seperated with spaces, this information is always visible below the 'board'.
  After the player wins or loses, they are asked whether they want to play again. Choosing no will simply exit the game, but if players choose to play again the game loops back to setting the difficulty level.

  [Back to top](<#contents>)

### Typography

  For the logo, I used the 'Big' Font available on [Patrick Gillespie](https://www.instagram.com/patorjk/)'s [Text to ASCII Art Generator](http://patorjk.com/software/taag/). It's easily readable and does not take up too much space.

  [Back to top](<#contents>)

# Features

## Existing Features

### Game Explanations

* The game starts with a short explanation of what it is and how it works.



### Random Color Code Generation

* The color code the player has to guess is generated randomly so that every game is different.

### Custom Difficulty Settings

  * The player can customize the difficulty of the game by setting the code length from 3-7 colors and the number of tries to a number between 4 and 10.

  ![Main Menu](/assets/readme-images/main_menu.jpg)

[Back to top](<#contents>)

### Difficulty Menu

  * In this menu users can pick the difficulty level of their choice, navigate to the customize difficulty settings menu or go back to the main menu.

    ![Difficulty Menu](/assets/readme-images/difficulty_menu.jpg)

  * On viewports with less than 1024px width, the hard and custom difficulty options are hidden. Hard would definitely break the layout and custom options have a high chance of doing that as well, as narrow viewports can't handle more than 8 columns of squares. Beginners will be satisfied with the lower difficulty levels.

    ![Difficulty Menu with hidden options](/assets/readme-images/diff_options_hidden.jpg)

  [Back to top](<#contents>)  

### Customize Difficulty Settings Menu

  * Here users can customize the playing field by adjusting the parameters of its height and width. 
  * They can also configure the number of mines that will be in the playing field.
  * After they are done, they can start the game by clicking the 'Start Playing' button.
  * If they would rather pick one of the pre-defined settings, they can go back to the main menu and restart from there.

  ![Customize Difficulty Settings Page](/assets/readme-images/custom_difficulty.jpg)

  [Back to top](<#contents>)

### How To Play Section

  * Here users can learn what Minesweeper is and how to play the game.

  * The two clickable buttons at the top of the playing field are also briefly explained. They are the only elements that are not completely straightforward.

  * At the bottom of the page users can also see what it looks like to win and lose a game.

  ![How To Play Section](/assets/readme-images/how_to_play.jpg)

  [Back to top](<#contents>)

### Settings Menu

  * Here users can activate Desktop Mode, which just prevents the playing field from being resized with respect to their viewport. Users who know the game from the olden days might want to prefer the squares never to vary in size. This is deactivated by default because the resizing feature is essential on mobile devices.
  * Users can also pick a different background color that they might prefer to the standard greyish blue.

  ![Settings Menu](/assets/readme-images/settings_menu.jpg)

  [Back to top](<#contents>)

### Playing Field
  
  * On the playing field there is a circle arrow at the top left. By clicking it, users can quickly restart their games. This is essential because clicking a mine and losing in the process is such a frequent part of the game.
  * The timer starts counting as soon as a game is started. It only stops once the player either loses or wins.
  * The ^\_^ emoji indicates that the game is still going on. It temporarily changes to O\_O when the player is clicking a mine, which conveys a certain tension as every click is potentially the end of the game. Once players lose, it changes to X\_X indicating that the player is dead and to d^\_^b when they win to indicate a double thumbs up, acknowledging the player's feat. All of this was heavily inspired by the original game that had a graphical emoji with similar expressions.
  * The mines counter shows the number of mines players have left to find. Every time a player marks a square as mined by right-clicking or long-pressing it, the counter goes down. As in the original game, it is not a clear indicator of whether the marked squares really contain mines, it does not perform a check. It simply serves as an indicator of the player's progress and can help with decisions late in the game when the player can evaluate how many mines there are in the last remaining squares. This can be helpful.
  * The off button allows players to navigate back to the main menu.
  * Every square on the playing field has a hover effect and an active effect for more feedback.
  * The numbers that players reveal by clicking or tapping squares are color-coded to help players make faster decisions.
  * When a game is lost, the background of the playing field will turn red, when the player wins, it turns green. This is different from the original game but gives additional feedback.
  * When the game ends, all mines are revealed as their squares will show in black.

  ![Playing Field: Easy Difficulty](/assets/readme-images/easy_difficulty.jpg)
  ![Players wins](/assets/readme-images/win.jpg)
  ![Players loses](/assets/readme-images/lose.jpg)

  [Back to top](<#contents>)

## Future Implementations

### Reveal zero squares automatically

  *  When you click a square that does not border on any mined squares (zero square), the game should automatically reveal all adjacent squares and do the same if it finds any more zero squares in the process. This would mimick the original game's behavior.

### Leaderboards

  * Record times and player names for won games in leaderboards for the standard difficulty levels.

### Statistics
  
  * Create statistics like 'x games won out of x attempts' or 'percentage of revealed squares before losing'.

[Back to top](<#contents>)

## Accessibility

I have tried to keep the website as accessible as possible by using semantic HTML elements, providing adequate contrast for fonts, using the alt attribute for images, the title attribute for links, etc. To further ensure that the site is accessible, I ran tests with the Web Accessibility Evaluation Tool (WAVE) and also used a Chrome browser extension called Web Disability Simulator. More on this in [Testing](#testing).

[Back to top](<#contents>)

# Technologies Used

## Languages Used

  * HTML5
  * CSS3
  * Javascript

## Frameworks, Libraries & Programs Used

  * [Git](https://git-scm.com/) - For version control

  * [GitHub](https://github.com) - To save and store my project files

  * [Google Fonts](https://fonts.google.com/) - To find and import fonts

  * [CloudConvert](https://cloudconvert.com/) - To convert PNG images to WebP images and GIF to WebM animations

  * [Colordot](https://color.hailpixel.com/) - To create the color palette above

  * [Favicon.io](https://favicon.io/) - To create a favicon

  * [Font Awesome](https://fontawesome.com/) - For the Restart and Off Button icons

  * [Google Dev Tools](https://developer.chrome.com/docs/devtools/) - To work out bugs, troubleshoot and test features and play around with property values and to test the website using the Lighthouse Test

  * [Compressor.io](https://compressor.io) - To compress images

  * [GIMP](https://gimp.org) - To resize and convert images

  * [ScreenToGif](https://www.screentogif.com/) - To record gameplay for the How to Play section and animations for the documentation of this project

  * [Text ASCII Art Generator](https://patorjk.com/software/taag/#p=testall&h=3&f=Alpha&t=Mastermind)

  * [Am I Responsive?](https://ui.dev/amiresponsive) - To showcase the website on all of the images used in this documentation file

  * [WAVE Web Accessibility Evaluation Tool](https://wave.webaim.org/) - To further ensure accessibility for all users

  [Back to top](<#contents>)

# Testing

  Please go [here](TESTING.md) for information about the testing that went into this project.

[Back to top](<#contents>)

# Deployment

## How to Deploy the Project on GitHub Pages

1. In your browser, navigate to the [GitHub page of this project.](https://github.com/beckoningstranger/pp2-mines)
![Image of the repository's website](assets/readme-images/howtodeploy.jpg)
2. Click on the 'Settings' button in the top menu
3. Select the 'Pages' section in the side bar on the left
4. Under 'Source' select 'Deploy from a branch'
5. Select the 'main' branch
6. Click 'Save'
7. After about a minute, when you come back to the page, you will see the message 'Your site is live ...' with a link you can simply click.

[Back to top](<#contents>)

## How to Fork the Repository on GitHub

1. In your browser, navigate to the [GitHub page of this project.](https://github.com/beckoningstranger/pp2-mines)
2. Click the 'Fork' button at the top right of the page. If you are not the owner of the project, it will not appear greyed out to you:

![Location of Fork button](assets/readme-images/forkbutton.jpg)

[Back to top](<#contents>)

## How to Clone the Repository on GitHub

1. In your browser, navigate to the [GitHub page of this project.](https://github.com/beckoningstranger/pp2-mines)
2. Click the 'Code' button, make sure you have HTTPS selected and then click the button to copy the link to your clipboard as demonstrated in this GIF:

  ![How to Clone](assets/readme-images/howtoclone.jpg)

3. Open your IDE and either use the functionality it provides (many IDE offer buttons that help you clone repositories) and paste your link there to have your clone created or go to the terminal and type: 'git clone \[insert your link here\]'
4. Hit ENTER and wait for you local clone to be created.

[Back to top](<#contents>)

# Credits

## Content

  * All of the content was written by myself.

  * The game principle is of course not my own and according to [the Minesweeper Wikipedia page](https://en.wikipedia.org/wiki/Microsoft_Minesweeper) its origin is unclear.

## Media

  * For my favicon, I used [this free picture](https://pixabay.com/illustrations/bomb-explode-detonate-explosion-1602109/) by [95C](https://pixabay.com/users/95c-484762/).

## Code

  * As this was my first Javascript project, there were many first times here, where I searched the web for solutions to my problems. Here is where I actually took code and used it for this project: 
    
    * When I was looking for a way to disable the event triggers for the playing field to stop players from playing on after losing, I finally found the possibility to use an abort signal. I learned this reading the [MDN addEventListener page](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener) and adapted their code.

    * When I was looking for a good way to resize the playing field specifically for a user's viewport, I learned how to get the needed values by reading [ryanve's answer on this Stackoverflow page](https://stackoverflow.com/questions/1248081/how-to-get-the-browser-viewport-dimensions).

    * Implementing a long press to enable users to mark squares as mines was harder than expected, but with [the answers on this Stackoverflow page](https://stackoverflow.com/questions/6139225/how-to-detect-a-long-touch-pressure-with-javascript-for-android-and-iphone) I could make it work.

    * [This article by Tulusibrahim](https://medium.com/geekculture/creating-counter-with-javascript-4b1c60892c45) helped me greatly to create my own timer.

    * To save the settings the website uses cookies. As I had no prior knowledge of how this is done, I used the information in [W3School's article](https://www.w3schools.com/js/js_cookies.asp) on the subject from which I took one function without altering it.
  
  [Back to top](<#contents>)

# Acknowledgements

I would like to thank the following people

* Precious Ijege, my mentor, for providing feedback on my ideas and helping me create this project.

* My daughter for being interested in this project and learning how to play the game.

* My wife for proofreading my work.

[Back to top](<#contents>)