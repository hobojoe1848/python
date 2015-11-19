import os
import sys

refresh = False
if len(sys.argv) > 1: 
  refresh = True # if called with cli arg (any string) do the questioning again

if os.path.isfile("userattributes.txt") and not refresh:        #Check to see userattributes file exists (== True not needed) - if refresh go to else
    print("Welcome Back!")                              #If it exists, print Welcome Back Message        
else:
    # new file or refresh
    configfile = open("userattributes.txt", "w")        #If userattributes doesn't exist, create new userattributes file

    while True:
      try:
        normaltime = int(raw_input('Please enter normal hourly rate: '))
        break
      except ValueError:
        print "Not a number, please try again"

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

