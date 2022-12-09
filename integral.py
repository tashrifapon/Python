#******************************************************************************
# integral.py
#******************************************************************************
# Name: Tashrif Apon
#******************************************************************************
# Remarks (optional):
# https://www.derivative-calculator.net/ -> to find 4th derivative for error calculation
# https://www.youtube.com/watch?v=cmF4NpQYKH0 -> to find error tolerance
#
#https://www.google.com/searchq=calculating+integral+of+a+piecewise+function&rlz=1C5CHFA_enUS877US877&sxsrf=ALiCzsYq2XCKqF438fnLnfWtTPkIau4anA:1658637358732&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjy_8_U2ZD5AhUyjIkEHXnaAhUQ_AUoAnoECAIQBA&biw=1440&bih=789&dpr=2#imgrc=ZAMlArMt6e0awM -> to check piecewise integrals
#
#https://www.google.com/search?q=simpson%27s+rule&rlz=1C5CHFA_enUS877US877&oq=simpson%27s+rule&aqs=chrome..69i57j0i433i512j69i59j0i512l2j69i61j69i60j69i61.5554j0j7&sourceid=chrome&ie=UTF-8 -> kept on getting a big number, so I reread hw prompt -> is 3 in 'dx/3' part of Simpson's -> so I searched

import math
#**************************************************************************************************************************************
#inputs
a = float(input('What\'s the lower limit? '))
b = float(input('What\'s the upper limit? '))

decision = input('\nIf you want to use error tolerance, please enter \'YES\'.\nOtherwise, enter the N you want to use (must be even): ')
if decision == 'YES':
    print('\nIf you want to use test case, enter {0.0048476800363822087} for error tolerance')
    print('Your Answer should be the same for N = 6: (0.45123691)')
    e_tol = float(input('\nHow much error can you tolerate? (Do not include % sign)'))
else:
    N_put = float(decision)
#**************************************************************************************************************************************
#Finding error tolerance or what to put for N (if input)
def neg_f_dv(neg):
    return (math.pi**3)*(4*math.sin(math.pi*neg)+(math.pi*neg+math.pi)*math.cos(math.pi*neg))

def pos_f_dv(p):
    return -1*(math.pi**3)*(4*math.sin(math.pi*p)+(math.pi*p-math.pi)*math.cos(math.pi*p))

if a >= 0 and b > 0:
    #use pos
    k = pos_f_dv(b) - pos_f_dv(a)
elif a < 0 and b <= 0:
    #use neg
    k = neg_f_dv(b) - neg_f_dv(a)
elif a < 0 and b > 0:
    #use neg for a -> abs dv goes up and 0
    #use pos for b and 0 -> 
    k = (neg_f_dv(0) - neg_f_dv(a)) + (pos_f_dv(b) - pos_f_dv(0))
    
if k < 0:
    k *= -1 #b/c absolute value

    
N_put_tol = (k*(b-a)**5)/(180*(N_put**4))
if decision != 'YES':
    print(f'This calculation will have an error tolerance within {N_put_tol*100}%.') #thought it'd be a nice touch
    N = int(N_put) # int b/c it gave error in for loop (range doesn't take float)
else:
    n = (k*((b-a)**5)/(e_tol*180))**(1/4)
    # the if below gave an error when it was alone b/c n was not defined; n is var to set up N for the error tolerance condition
    if n/1 == int(n)/1: #here and a few more lines down to make sure N is even
        N = int(n)
    else:
        N = int(n+1)
        
if N % 2 != 0: #making it even (for error tolerance
    N += 1
#**************************************************************************************************************************************
#Setting up evaluating integral
dx = (b-a)/N 

def neg_func(x):
    return (1+x)*math.cos(math.pi*x)
def pos_func(x1):
    return (1-x1)*math.cos(math.pi*x1)

ans = 0
#start = a # later realized value of a in the forloop wouldn't change -> undesirable arithmetic -> ended up using a

#because of the decision (line 74) -> I elminated a second elif that considered a<0 and b>0

for calc in range(N+1): # +1 b/c simpson's adds N+1 terms
    
    if calc == 0 or calc == N:
        c = 1
    elif calc % 2 and calc != 0:
        c = 4 # swapped with number val 2 # confused as to why this worked b/c c = 4 only happens at non-start/end even indexes 
        # I thought it should've been the odd indexes -> please comment why
    else:
        c = 2 # same thing above -> swapped with number val 4
    
    if a >= 0: # had scenerio for b -> unnecessary + more if/elif statements
    #use pos
        ans += c*pos_func(a)
        a += dx
    elif a < 0:
    #use neg
        ans += c*neg_func(a)
        a += dx
    #print(ans) to check
#print(ans) to check

ans *= (dx/3)
print(f'\nAnswer: {ans:.8f}')

if decision == 'YES':
    print('Don\'t worry I did not code a print statement to spit out .45123691; I did print this statement though.')