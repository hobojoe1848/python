import os.path
if os.path.isfile("userattributes.txt") == True:        #Check to see userattributes file exists
    print("Welcome Back!")                              #If it exists, print Welcome Back Message        
else:
    configfile = open("userattributes.txt", "a")        #If userattributes doesn't exist, create new userattributes file
    print('Please enter normal hourly rate: ')

    normaltime = input()                                #Allow user to enter in base normal pay rate

    normaltime = float(normaltime)                      #Convert user input to float
    
    timeandhalf = normaltime * 1.5                      #Calculate time and a half and double time rates based on normal pay rate
    doubletime = normaltime * 2

    timeandhalf = round(timeandhalf, 4)                 #Round rates to 4 decimal places
    doubletime = round(doubletime, 4)
    
    print("Time and Half Rate: " + str(timeandhalf))    #Display over time rates
    print("Double Time Rate: " + str(doubletime))

    configfile.write(str(normaltime) + "\n");           #Write normal, time and half and double time amounts to userattributes file
    configfile.write(str(timeandhalf) + "\n");
    configfile.write(str(doubletime) + "\n");
    
    configfile.close()

configfile = open("userattributes.txt", "r")



configfile.close()

