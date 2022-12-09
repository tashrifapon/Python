#******************************************************************************
# goldbach.py
#******************************************************************************
# Name: Tashrif Apon
#******************************************************************************
# Remarks (optional):
# all non prime factors: 2 and/or 3; dont forget perfect squares of prime numbers; use modulo # this was b4 I started the code
# ended up not worrying about perfect squares of prime number -> mod was useful and used (not in all the senses I thought)
#
###############################################################################
#
# Test code for is_prime()
#
################################################################################
def is_prime(x):
    if x == 1:
        return False
    elif x == 2:
        return True
    else:
        blah = 0 # has to be within the def
        for i in range(2,x): # x won't be counted -> blah won't be wrongly affected
            if x%i == 0:
                blah += 1  # the moment a factor other than x or 1
        if blah >= 1:
            return False # had this at true and everything beside first two cases messed up
        else:
            return True

def decompose(x):
    l_of_prime = []
    fin_lis = []
    for i in range(2,x):
        if is_prime(i) == True:
            l_of_prime.append(i)
    for val in l_of_prime:
        if x-val in l_of_prime:
            fin_lis.append(val)
            fin_lis.append(x-val)
            break
    return fin_lis

for ans in range(4,801,2):
    frst = decompose(ans)[0]
    scnd = decompose(ans)[1]
    print(f'{ans} = {frst} + {scnd}')