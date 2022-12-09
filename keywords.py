#******************************************************************************
# keywords.py
#******************************************************************************
# Name: Tashrif Apon
#******************************************************************************
# Overall notes (not to replace inline comments):
# Some silly mistakes
# Used w3schools lists, dictionaries
# other websites were used but I didn't put them in b/c I redid and tried many other (some similar maybe same) methods for the meat of this code

filenames = ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt', '6.txt', '7.txt', '8.txt', '9.txt', '10.txt']

terms_ = {} # inside -> allows new dict for each file -> more computing(?) -> easier

wrd = input('Enter a word: ')
print() # looks nicer

for f in filenames: #dictionary
    #print(f)
    
    #terms = {} # I tried it on the outside but it kept returning 10.txt; tried again; All Praise and Thanks are due to Allaah alone
    
    a = open(f, 'r') # close
    b = a.read() # kept getting _ioTXT -> https://stackoverflow.com/questions/38744244/glob-error-io-textiowrapper-name-mode-r-encoding-cp1252-reading-tex
    # it was silly
    c = b.split()
    a.close() # remembered
    
    # try using range; recall on f via index
    for w in c:
        # l = [] was here
        if w not in terms_:
            terms_[w] = [f]
        else:
            terms_[w].append(f) # game changer # kept on using l = [] and appending that with f; I set terms[w] equal to that
            # it refreshes every "w" and "f" but the changes to terms_ were already made
    
    #print(terms_) checks
    
#print(terms_) #checking


####CLEAN UP####
terms = terms_.copy() # does this change terms? b/c I wntd to print('How many times your wrd is in file') using terms_

for v in terms:
    for t in terms[v]: # this treats it like a list and not a range
        # b/c I didn't get error after .remove()
        while terms[v].count(t) > 1:
            terms[v].remove(t) # initially an if stmnt -> then a for loop until every is gone then add one back
            # or could've stopped at 1 count (?); Alhamdulillaah, Allaah gave me the idea of using a while loop
            
#print(terms) checking

if wrd in terms: # finally
    if len(terms[wrd]) > 1:
        print(f'Your word, "{wrd}," is in these files: {terms[wrd]}')
    else:
        print(f'Your word, "{wrd}" is in this file: {terms[wrd]}')
else:
    print(f'Your word, "{wrd}," is not any of the files.')
    
    
####Challenge####

#for i in range(len(filenames)):
    #if i <= len(filenames) - 2:
        #a = open(filenames[i], 'r') # close
        #b = a.read() 
        #c = b.split()
        #a.close()
        
        #counter = 0
        
        #for i_o in range(1,i+1):
            #a1 = open(filenames[i+i_0], 'r') # close
            #b1 = a1.read()
            #c1 = b1.split()
            #a1.close()
            
            #counter =
            
#gtg might come back to it ltr







