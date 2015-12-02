import os
import sys

refresh = False
if len(sys.argv) > 1: 
  refresh = True                      # if script is run with cli argument (any string) do the questioning again

if os.path.isfile('userattributes.txt') and not refresh:      #Check to see userattributes file exists (== True not needed) - if refresh chosen go to else
    print('Welcome Back!')                                    #If it exists, print Welcome Back Message
    
else:

    # start creating the new userattributes file or reset values if refresh is chosen
    
    configfile = open('userattributes.txt', 'w')              #If userattributes doesn't exist, create new userattributes file. Open it in variable configfile

    while True:
      try:                                                    # try is an error handling function. Try doing this, if an error occurs, go to the exception.
        normaltimerate = float(input('Please enter normal hourly rate: '))  #enter normal hourly pay rate
        break                                                 #break our of while loop
      except ValueError:
        print('Not a number, please try again')         #if anything other than an int is entered, error out.

        
    timeandhalfrate = normaltimerate * 1.5                      #Calculate time and a half and double time rates based on normal pay rate
    doubletimerate = normaltimerate * 2
    doubletimeandhalfrate = normaltimerate * 2.5

    timeandhalfrate = round(timeandhalfrate, 4)                 #Round rates to 4 decimal places
    doubletimerate = round(doubletimerate, 4)
    doubletimeandhalfrate = round(doubletimeandhalfrate, 4)
    
    print('Time and Half Rate: ' + str(timeandhalfrate))    #Display over time rates
    print('Double Time Rate: ' + str(doubletimerate))
    print('Double Time and Half Rate: ' + str(doubletimeandhalfrate))

    configfile.write(str(normaltimerate) + '\n');           #Write normal, time and half and double time amounts to userattributes file
    configfile.write(str(timeandhalfrate) + '\n');
    configfile.write(str(doubletimerate) + '\n');
    configfile.write(str(doubletimeandhalfrate) + '\n');
    
    configfile.close()                                  #close off the userattributes file (configfile variable).


#Let's define the functions that will be used by the main menu.


def TimeandHalfEntry():
  print('\n')
 
  while True:
    try:
      timeandhalfhours = float(input('How many hours of time and a half did you work? '))
      break
    except ValueError:
      print('Invalid entry. Please enter a number. \n')

  totaltimeandhalf = timeandhalfhours * timeandhalfrate

  print(str(totaltimeandhalf) + '\n')
  


###########################



def PrintTotal():
  print('\n')
  
  print(str(total) + '\n')

  input('Press any key to return to main menu...')
  


#Now that the userattributes have been collected and stored, let's start the actual program

configfile = open('userattributes.txt', 'r')            #open the userattributes file in variable "configfile".

normaltimerate = float(configfile.readline())           #read line 1 from the configfile and assign that line as a float to normaltimerate variable
timeandhalfrate = float(configfile.readline())          #read line 2 and assign
doubletimerate = float(configfile.readline())           #read line 3 and assign
doubletimeandhalfrate = float(configfile.readline())    #read line 4 and assign


while True:
  print('What rate of Over Time would you like to enter? (Enter the number)')
  print('(1) Time and a Half (' + str(timeandhalfrate) + ').')
  print('(2) Double Time (' + str(doubletimerate) + ').')
  print('(3) Double Time and a Half (' + str(doubletimeandhalfrate) + ').')
  print('(4) View Current Total Earned.')
  print('\n')

  try:
    OTchoice = int(input('Enter Choice: '))
  except ValueError:
    print('Invalid character. Please enter a number. \n')
    continue

  if OTchoice == 1:
    TimeandHalfEntry()
  elif OTchoice == 2:
    print('Placeholder for 2')
  elif OTchoice == 3:
    print('Placeholder for 3')
  elif OTchoice == 4:
    PrintTotal()
  else:
    print('Invalid number. Please try again. \n')
  
    
      

configfile.close()

