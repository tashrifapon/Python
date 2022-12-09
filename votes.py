#******************************************************************************
# votes.py
#******************************************************************************
# Name: Tashrif Apon
#******************************************************************************
# Remarks (optional):
# I could've done so line by line by taking character count of names and spaces; wouldn't really work for a file with different count per line
#
# For my workspace added my scrap notebook to the same folder/directory

result = open('result.txt','r')
readresult = result.read()
l_r = readresult.split()
#print(l_r)
result.close() # important

Frank = 0
David = 0
Evan = 0
George = 0
Alice = 0

for i in range(len(l_r)):
    spot = i - 5*(i//5) # don't need int for //
    points = 5 - spot # was going to do if stmnts -> not necessary
    if l_r[i] == 'Frank': # can I make Frank as a str be used as a var name -> can I unstringify a str?
        Frank += points
    elif l_r[i] == 'David':
        David += points
    elif l_r[i] == 'Evan':
        Evan += points
    elif l_r[i] == 'George':
        George += points
    elif l_r[i] == 'Alice':
        Alice += points
        
wanted = input('Whose points do you want to see?')
if wanted == 'Frank': 
    print(f'Frank has {Frank} points.')
elif wanted == 'David':
    print(f'David has {David} points.')
elif wanted == 'Evan':
    print(f'Evan has {Evan} points.')
elif wanted == 'George':
    print(f'George has {George} points.')
elif wanted == 'Alice':
    print(f'Alice has {Alice} points.')

winner = []
winner.append(Frank) # can I not append multiple inputs/stuff/crct_trmnlgy ?
winner.append(David)
winner.append(Evan)
winner.append(George)
winner.append(Alice)

whomst = max(winner) # so glad for this

if whomst == Frank:
    mayor = 'Frank'
elif whomst == David:
    mayor = 'David'
elif whomst == Evan:
    mayor = 'Evan'    
elif whomst == George:
    mayor = 'George'    
elif whomst == Alice:
    mayor = 'Alice'

print(f'The mayor is {mayor}.')

# I feel like there is probably a way to get the answer without having to write the names multiple times over
# my strat would depend on the answer to my q about unstr a str