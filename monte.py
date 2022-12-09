#******************************************************************************
# monte.py
#******************************************************************************
# Name: Tashrif Apon
#******************************************************************************
# Remarks (optional):
# To limit the character count, I realized adding positions to subtract from would reveal the position
# Using the != was another character limitizer instead of setting two ==
# Making the position an int relieved the character count and stress of switching between int and str

position = int(input('Queen of Hearts starts at position: '))
move1 = input('First Move: ')
move2 = input('Second Move: ')

if move1 == 'L' and position != 3:
    position = 3 - position

if move1 == 'R' and position != 1:
    position = 5 - position

if move2 == 'L' and position != 3:
    position = 3 - position

if move2 == 'R' and position != 1:
    position = 5 - position
    
print(position)
