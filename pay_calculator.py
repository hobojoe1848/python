import os.path
if os.path.isfile("userattributes.txt") == True:
    print("Welcome Back!")
else:
    configfile = open("userattributes.txt", "a")
    print('Please enter normal hourly rate: ')

    normaltime = input()
    
    timeandhalf = float(normaltime) * 1.5
    doubletime = float(normaltime) * 2

    timeandhalf = round(timeandhalf, 4)
    doubletime = round(doubletime, 4)
    
    print("Time and Half Rate: " + str(timeandhalf))
    print("Double Time Rate: " + str(doubletime))

    configfile.write(normaltime + "\n");
    configfile.write(str(timeandhalf) + "\n");
    configfile.write(str(doubletime) + "\n");
    
    configfile.close()

configfile = open("userattributes.txt", "r")



configfile.close()

