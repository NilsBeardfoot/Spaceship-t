# SPACESHIP/T - SHIPS in SPACE!
### Video Demo: <https://youtu.be/LrOVHRvcwkA>
### Required Libraries


```
pip install msvcrt
pip install random
pip install time
pip install date
```
## Description
### Abstract

This program.py is a mini-game using the command line tool as a graphical interface.

Press "W" "A" "S" "D" to fly a spaceship through asteroid infested space. Choose from existing ships or create your own in a .txt file. Use your blasters (your A's) by pressing 'L' to destroy asteroids in your path. If you collide with larger asteroids, shown as "#", your ship will be damaged and the part that was hit will be lost to space. If your entire ship is destroyed, or if you press 'Q' to exit, you will leave the game with your final results damage taken and score showing the points for shooting down asteroids.


### Files
This README.md file explains the funktion of the programm and shallow the python code behind it.
The requirements.txt file shows python librarys required.
The project.py file is the actual programm to execue idealy in VSC.
You can find five .txt files starting with "ship" containing spaceships to choose from.
test_project.py is here to test functions of project.py with pytest.


### Motivation
I have played a lot of games in my time and because of lack of usfull ideas for my CS50 Python final project I wanted to create my first game. I have created may "maps" in the Warcraft 3 editor 10 years back but no actual game. To keep it simple I used the simplest graphic interface there is, the commandline and started with a raster as screen and worked my self further from there.


### Full Description
This is a minigame written in Python using the command line tool as the graphical interface.
Be sure to install all the necessary libraries from requirement.py first.

The first thing to do is select a ship, choose the 'default' ship, select one of the five ship.txt files that come with the game by typing in the filename or create your own ship.txt first and select it like the others. If you choose to create your own ship, be sure not to use any '#', '.' or '|' in your ship, as these are used to animate asteroids and blaster shots; your 'A's will fire blasters.

*Method:
To do this the open function with read on the .txt file is used and take each character in a line as an element of a list, each line is a list and all line lists are concatenated into another list that makes up the ship.*


Then the game starts. The command line that displays the game is printed at 100 frames per second; image quality may vary depending on your hardware and software. Visual Studio Code worked well for me.

*Method:
The screen is a list for each row all combined in another list, creating a maneuverable grid with x and y coordinates. This screen is animated and then printed.


Every x seconds small asteroids are created, shown as '.' and moved, as well as large asteroids shown as '#' and move from top to bottom as well; the smaller ones are just for decoration, but the larger ones have more interaction.
The ship's position can be changed by pressing 'W', 'A', 'S', 'D', and the balster can be fired by pressing 'L'. If the ship collides with the large asteroids, or large asteroids collide with the ship, the ship will be damaged and the part that was damaged will be removed, the large asteroids will not be damaged though and will continue their path through the ship, damaging it even more if not destroyed or it is moved out of the way. The blasters on a ship are shown as A's, A's can fire a laser beam from bottom to top, destroying the first large asteroid in its path, this will add points to your score depending on the number of blasters on your ship has, more blasters equal less points.

*Method:
Every x seconds the last row in the screen (the lists in the list) will be cleared and every other, if not part of the ship or interface will be moved down one row by asigning each item in each row of the row below. In the top row, below the interface, new asteroids are randomly created.
The ship has a position marker at its top left corner, when a key is pressed this marker is moved, the ship is erased from the screen and re-created in its new position.
If a large asteroid is in the position that a part of the ship (individual sign), that is not empty, moves to, that part of the ship is removed and the damage counter goes up, same is true if a large asteroid moves to a position a part of the ship is in.
For the blasters it is similar. For each 'A' in the ship a laser of blaster shots "|" is fired from bottom to top until the first large asteroid is found, then the asteroid is removed and in the next frame any "|" is removed.*.


## Known bugs
Every collision function, moving asteroids, creating and removing blaster shots will occasionally cause an IndexError which, if simply ignored, the programm will still work as intended, but the source could not be found.

Some times when moving the ship in a position an asteroid just move the asteroid will be removed and not even dealing any damage.
