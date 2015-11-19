import os
import sys

refresh = False
if len(sys.argv) > 1: 
  refresh = True                      # if script is run with cli argument (any string) do the questioning again

if os.path.isfile("userattributes.txt") and not refresh:      #Check to see userattributes file exists (== True not needed) - if refresh chosen go to else
    print("Welcome Back!")                                    #If it exists, print Welcome Back Message        
else:

    # start creating the new userattributes file or reset values if refresh is chosen
    
    configfile = open("userattributes.txt", "w")              #If userattributes doesn't exist, create new userattributes file. Open it in variable configfile

    while True:
      try:                                                    # try is an error handling function. Try doing this, if an error occurs, go to the exception.
        normaltime = float(input('Please enter normal hourly rate: '))  #enter normal hourly pay rate
        break                                                 #break our of while loop
      except ValueError:
        print("Not a number, please try again")         #if anything other than an int is entered, error out.

    #normaltime = float(normaltime)                      #Convert user input to float
    
    timeandhalf = normaltime * 1.5                      #Calculate time and a half and double time rates based on normal pay rate
    doubletime = normaltime * 2

    timeandhalf = round(timeandhalf, 4)                 #Round rates to 4 decimal places
    doubletime = round(doubletime, 4)
    
    print("Time and Half Rate: " + str(timeandhalf))    #Display over time rates
    print("Double Time Rate: " + str(doubletime))

    configfile.write(str(normaltime) + "\n");           #Write normal, time and half and double time amounts to userattributes file
    configfile.write(str(timeandhalf) + "\n");
    configfile.write(str(doubletime) + "\n");
    
    configfile.close()                                  #close off the userattributes file (configfile variable).


#Now that the userattributes have been collected and stored, let's start the actual program

configfile = open("userattributes.txt", "r")            #open the userattributes file in variable "configfile".



configfile.close()

