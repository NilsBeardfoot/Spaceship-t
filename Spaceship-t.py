import msvcrt
import random
import time
from datetime import date



# Screen size
_height = 18
_width = 151 # needs to be odd
dmg = 0
rows = []
errorcount = 0

# Standard ship 
ship_shape_1 = ["A", " "," "," ", " " ," " ," " ," ", "A"]
ship_shape_2 = ["\\", "\\", "_", "_", "A" ,"_","_" ,"/", "/"]
ship_shape_3 = [" "," ", "\\" ,"I", "X" ,"I","/" , " ", " "]
ship = [ship_shape_1, ship_shape_2, ship_shape_3]


# Set ship starting position of the top left corner of the ship
ship_position_y = int(_height - len(ship) - 3)
ship_position_x = int((_width - len(ship[0])) / 2)

score = 0
score_multiplicator = 10
blaster = "A"
blaster_shot = "|"
meteor_small = "."
meteor_large = "#"


_meteor_timer_1 = 0
_meteor_timer_2 = -100

def main():
     global ship, ship_position_x, ship_position_y, _meteor_timer_1, _meteor_timer_2, meteor_large, meteor_small, blaster, blaster_shot, score_multiplicator

     # CS50 Requirement
     print()
     print("Project Title:         SPACESHIP/T - SHIPS in SPACE!")
     print("Todays date:           " + str(date.today()))
     print()

     ###################
     # Start Menue ---->
     ###################
     print()
     print("Welcome to >>> SPACESHIP/T - SHIPS in SPACE! <<<")    
     print()
     print("Select your spaceship from existing ones, write 'default' for the standart one or exit the programm to create your own one in a txt file first.")
     print("If you create your own ship, do NOT use any of these in them >", meteor_large, meteor_small, blaster_shot, "<, >", blaster, "<'s are your blasters, more blasters give less points.")
     while True:
          try:
               file = input("What's the file name of your ship? ")
               if file == "default":
                    pass  # take defailt ship
               else:
                    ship = read_ship(file) #Select ship/file
          except FileNotFoundError: # if file name is wrong, cycle back
               pass
          else:
               ship_check = []
               for i in ship:
                    for j in i:
                         ship_check.append(j)   
               if meteor_large not in ship_check and meteor_small not in ship_check and blaster_shot not in ship_check:
                    print()
                    for i in ship:
                         print(*i, sep="")
                    print()
                    yes = input("Is this the ship you want? [Y/N] ").lower()
                    if yes == "y":
                         break
               else:
                    print("There is a >", meteor_large, meteor_small, blaster_shot, "< in the ship")

     print("There are small meteors >", meteor_small, "< that deal no damage and can be ignored.")   
     print("There are big meteors >", meteor_large, "< that deal damage your ship when they collide.")   
     print("Use 'L' to fire your blasters, use 'W', 'A', 'S', 'D' to navigate, use 'Q' to quit.")   
     print()
     print("This will be a bumpy ride, are you ready?")           
     input("PRESS ANY ENTER ")
     ###################
     # End Menu <----
     ###################

     # Interface in first row
     first_row = [dmg, " Dmg / Score: ", score, "  W, A, S, D = Move, L = Fire, Q = Quit"]
     rows.append(first_row)

     # other rows
     for _ in range(_height):
          new_row = [" "] * (_width+2)  # Create empty space
          rows.append(new_row)

     # Position ship in starting position
     position_ship(ship_position_x, ship_position_y, ship)

     # Start screen
     print_screen(rows)

     # This loop keeps the whole game running, with 100 fps it prints the current screen (rows)
     while True:
          time.sleep(0.01)

          score_multiplicator = 10
          for i in range(len(ship)):
               for j in ship[i]:
                    if j == blaster:
                         score_multiplicator -= 1



          vanish_blaster(blaster_shot)
          _meteor_timer_2 += 1
          _meteor_timer_1 += 1
          #print(_meteor_timer_1)
          if _meteor_timer_1 == 2:
               move_meteor(meteor_small)
               create_meteor(meteor_small)
               _meteor_timer_1 = 0

          if _meteor_timer_2 == 30:
               create_meteor(meteor_large, 6)
               move_meteor(meteor_large)
               _meteor_timer_2 = 0

          if msvcrt.kbhit():  # Check for pressed keys
               key = msvcrt.getch().decode("utf-8").lower()

               if key == 'a' and ship_position_x != 1: # key needs to be pressed and not on edge of screen 
                    move(ship, ship_position_x, ship_position_y, -1, 0) 
                    ship_position_x -= 1
               elif key == 'd' and ship_position_x != _width - len(ship[0]) - 1: # key needs to be pressed and not on edge of screen 
                    move(ship, ship_position_x, ship_position_y, 1, 0)
                    ship_position_x += 1
               elif key == 'w' and ship_position_y != 2: # key needs to be pressed and not on edge of screen 
                    move(ship, ship_position_x, ship_position_y, 0, -1) 
                    ship_position_y -= 1
               elif key == 's' and ship_position_y != _height - len(ship) - 1: # key needs to be pressed and not on edge of screen 
                    move(ship, ship_position_x, ship_position_y, 0, 1)
                    ship_position_y += 1  
               elif key == 'l':
                    blast(ship, blaster, blaster_shot, ship_position_x, ship_position_y)               
               elif key == 'q':
                    print("You quit.")
                    #print("Errors: ", errorcount)
                    print("Score: ", score)
                    print("Damage taken: ", dmg)
                    break  # Break with 'q' to exit

          print_screen(rows) 
  

          # When ship is only whitespace exit game
          count = 0
          for i_idx, i in enumerate(ship): 
               if all(element == " " for element in ship[i_idx]):
                    count += 1
          if count == len(ship):
               print("Your ship has been destroyed!")
               #print("Errors: ", errorcount)
               print("Score: ", score)
               print("Damage taken: ", dmg)
               break  


# Load in the ship from another file.
def read_ship(filename):
    with open(filename, 'r') as file: # Open file in read mode
        ship_lines = file.readlines() # Read all lines of the file

    ship = []
    for line in ship_lines: 

        characters_list = [] #new list for each row
        for char in line:
            # Add to the characters list, ignore newline characters
            if char != '\n':
                characters_list.append(char)
        ship.append(characters_list) # Add the characters list to the ship
    return ship


# Creates a line of meteors underneath the first line (the interface with Dmg Score etc.).
def create_meteor(meteor, x=20):  
     _meteor_chance = [" "] * x # x = the number is the chance for NO meteor
     _meteor_chance.append(meteor) # and add one meteor
     for i in range(len(rows[1])):
          rows[1][int(i)] = random.choice(_meteor_chance)  

# Moves the meteors from top to bottom, if the ship is in the way of the meteor the ship gets damaged.
def move_meteor(meteor):
     global rows, _height, _meteor_chance, ship, ship_position_x, ship_position_y, meteor_large, meteor_small, errorcount, dmg, score_multiplicator
     for i_idx, i in reversed(list(enumerate(rows))):
          for j_idx, j in enumerate(i): #select all list items/pixels
               if j != " " and i_idx >= 1 and j == meteor: # only replace when space is not empty and not the interface row
                    if i_idx == _height-1: # delet last row that "moves out of the screen"
                         rows[int(i_idx)][int(j_idx)] = " "
                    else: # All other rows but interface and last row
                         if ship_position_x <= int(j_idx) <= (ship_position_x + len(ship[0])) and ship_position_y <= int(i_idx) <= ship_position_y + len(ship):
                              # if new meteor position is in the ship remove ship part and reduce hp
                              try:
                                   if ship[int(i_idx - ship_position_y)][int(j_idx - ship_position_x)] != " ":
                                        ship[int(i_idx - ship_position_y)][int(j_idx - ship_position_x)] = " "
                                        dmg += 10
                                        rows[0][0] = dmg
                              except IndexError:
                                   #print(i_idx, ship_position_y, int(i_idx - ship_position_y), " // ", j_idx, ship_position_x, int(j_idx - ship_position_x), " // ", _height)
                                   errorcount +=1
                                   pass
                                   #sys.exit()
                                 
                         if meteor == meteor_small and rows[int(i_idx + 1)][int(j_idx)] != " ":
                              rows[int(i_idx)][int(j_idx)] = " "
                         else:
                              rows[int(i_idx + 1)][int(j_idx)] = j
                              rows[int(i_idx)][int(j_idx)] = " "

      
# Moves the ship based on position and key pressed to direct it.
def move(ship, ship_position_x, ship_position_y, direction_x, direction_y):
     vanish_ship(ship_position_x, ship_position_y, ship)      
     position_ship(ship_position_x + direction_x, ship_position_y + direction_y, ship) 

# Brings the ship in an new position.
def position_ship(x, y, ship):
     global rows, meteor_small, dmg
     for i_idx, i in enumerate(ship):
          for j_idx, j in enumerate(i):
               if j != " ":  # only replace when ship space is not empty
                    if rows[int(y + i_idx)][int(x + j_idx)] != " " and rows[int(y + i_idx)][int(x + j_idx)] != meteor_small:
                         dmg += 10
                         rows[0][0] = dmg
                         ship[i_idx][j_idx] = " "
                    else: 
                         rows[int(y + i_idx)][int(x + j_idx)] = j

# To reposition the ship in a new place you also need to remove the ship on its current position and this is what happens here.
def vanish_ship(x, y, ship):
     global rows
     for i_idx, i in enumerate(ship):
          for j_idx, j in enumerate(i):
               if j != " ":  # only replace when ship space is not empty
                    rows[int(y + i_idx)][int(x + j_idx)] = " "

# Fire the blasters from your "A"s.
def blast(ship, blaster, blaster_shot, ship_position_x, ship_position_y):
     global rows, meteor_large, score, errorcount, score_multiplicator
     
     for i_idx, i in enumerate(ship):
          for j_idx, j in enumerate(ship[i_idx]):
               if j == blaster:
                    for k in range(ship_position_y):
                        
                         try:
                              if rows[int(i_idx + ship_position_y-k-1)][int(j_idx + ship_position_x)] != meteor_large:
                                   rows[int(i_idx + ship_position_y-k-1)][int(j_idx + ship_position_x)] = blaster_shot
                              else:
                                   rows[int(i_idx + ship_position_y-k-1)][int(j_idx + ship_position_x)] = " "
                                   score += score_multiplicator
                                   rows[0][2] = score
                                   break
                         except IndexError:
                              pass
                              errorcount +=1

# Removes the blaster shots
def vanish_blaster(blaster_shot):
     global rows, errorcount
     for i_idx, i in enumerate(rows):
          for j_idx, j in enumerate(rows[i_idx]):
               try:
                    if rows[i_idx][j_idx] == blaster_shot:
                         rows[int(i_idx)][int(j_idx)] = " "  
               except IndexError:
                    pass
                    errorcount +=1

#Probably the most important but very simpel function, this prints the creat every x seconds to create the illusion of movement.
def print_screen(rows):
     for list in rows:
        print(*list, sep='')




if __name__ == "__main__":
     main()

  