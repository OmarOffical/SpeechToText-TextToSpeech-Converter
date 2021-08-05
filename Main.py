import subprocess 
import Func



print("Hi This is Speech To Text/Text To Speech Converter")
print("What Do you Want ?")
print("1-Speech To Text")
print("2-Text To Speech ")
x=input()

if x=="1" :
    print("What Do You Want ?")
    print("1-Record audio")
    print("2-Choose File from device ")
    y=input()
    if y=="1":
        #Z Variable is to specify How many seconds does the user wants the Program to Run
        print("Please Enter How many seconds do You want To Record")
        z=input()

        #I used subprocess Function to allow the user to choose How many Seconds Does He wants
        subprocess.call("python transcribe.py -t {}".format(z),shell=True) 
    elif y=="2" :
        Func.AudioFromDevice()
    else:
        print("not a valid input please Try again")


elif x=="2" :
    print("What Do You Want ?")
    print("1-Write text")
    print("2-Choose File from device ")
    y=input()
    if y=="1":
        print('\nPlease Enter The Text That you want :')
        Text=input()
        Func.TxtToSpeech(Text)

    elif y=="2":
        Func.TxtFileFromDevice()
    else:
        print("not a valid input please Try again")

else: 
    print("not a valid input please Try again")















