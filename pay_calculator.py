import os
import sys

#Define Initial Global Variables#

total_OT = 0

#Let's define the functions that will be used by the main menu.


def TimeandHalfEntry():
  print('\n')
 
  while True:
    try:
      timeandhalfhours = float(input('How many hours of time and a half did you work?: '))
      break
    except ValueError:
      print('Invalid entry. Please enter a number. \n')

  totaltimeandhalf = round((timeandhalfhours * timeandhalfrate), 2)

  print(str(totaltimeandhalf) + '\n')

  global total_OT
  total_OT = round((total_OT + totaltimeandhalf), 2)

###########################


def DoubleTimeEntry():

  print('\n')
 
  while True:
    try:
      double_time_hours = float(input('How many hours of double time did you work?: '))
      break
    except ValueError:
      print('Invalid entry. Please enter a number. \n')

  totaldoubletime = round((double_time_hours * doubletimerate), 2)

  print(str(totaldoubletime) + '\n')

  global total_OT
  total_OT = round((total_OT + totaldoubletime), 2)


#########################


def DoubleTimeandHalfEntry():

  print('\n')
 
  while True:
    try:
      double_time_and_half_hours = float(input('How many hours of double time and a half did you work?: '))
      break
    except ValueError:
      print('Invalid entry. Please enter a number. \n')

  total_double_time_and_half = round((double_time_and_half_hours * doubletimeandhalfrate), 2)

  print(str(total_double_time_and_half) + '\n')

  global total_OT
  total_OT = round((total_OT + total_double_time_and_half), 2)


#########################


def PrintTotal():

  global total_OT
  
  print('\n')
  
  print('Current Total Overtime Earned = $' + str(total_OT) + '. \n')


###########################






##Start the User Attributes Collection##


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

        
    timeandhalfrate = round((normaltimerate * 1.5), 4)                      #Calculate time and a half and double time rates based on normal pay rate and rounds to 4 decimal places
    doubletimerate = round((normaltimerate * 2), 4)
    doubletimeandhalfrate = round((normaltimerate * 2.5), 4)
    
    print('Time and Half Rate: ' + str(timeandhalfrate))    #Display over time rates
    print('Double Time Rate: ' + str(doubletimerate))
    print('Double Time and Half Rate: ' + str(doubletimeandhalfrate) + '\n')

    configfile.write(str(normaltimerate) + '\n');           #Write normal, time and half and double time amounts to userattributes file
    configfile.write(str(timeandhalfrate) + '\n');
    configfile.write(str(doubletimerate) + '\n');
    configfile.write(str(doubletimeandhalfrate) + '\n');
    
    configfile.close()                                  #close off the userattributes file (configfile variable).



  


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
  print('(4) Quit')
  print('\n')
  print('**Current Total Overtime Earned = $' + str(total_OT) + '.**')
  print('\n')

  try:
    OTchoice = int(input('Enter Choice: '))
  except ValueError:
    print('Invalid character. Please enter a number. \n')
    continue

  if OTchoice == 1:
    TimeandHalfEntry()
  elif OTchoice == 2:
    DoubleTimeEntry()
  elif OTchoice == 3:
    DoubleTimeandHalfEntry()
  elif OTchoice == 4:
    break
  else:
    print('Invalid number. Please try again. \n')

  input('Press Enter... \n')
  
    
      

configfile.close()

