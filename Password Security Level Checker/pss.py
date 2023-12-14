# This Password Security Level Checker Created By Dr.Nick_Z

# Library

# Gui Library
from tkinter import*
pass_label=Tk()

# Strings For Containing Symbols...

Small_Alpha=tuple("abcdefghijklmnopqrstuvwxyz")
Letter_Aplha=tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
Integer_Number=tuple("1234567890")
Symbol_Define=tuple("`~!@#$%^&*()[]_-+=}|{:;'<,>./?")



# Function For Who Check Password Security Level
# We Created 4 security Level There ( 1. Low , 2. Medium , 3. Strong , 4. Highly Recommended )
def Password_Security_Level_Checker():

    ps=txt.get()

    # Four Security Level
    
    # Condition For Low Level 
    # 1. (Password Lenght More Than 10)
    # 2. (Second Contion Is The Password Contain Only One Kind Of Symbol , Example ('abcdefghijkl','ABCDEFGHIJKLMNOP'))

    # Condition For Medium Level
    # 1. (Lenght More Than 10)
    # 2. (Contain Two Type Of Symbol , Example ('ABCdefGHijklmnop'))
    # 3. (Symbol Must Be Two Different In Lenght Two..)
    
    # Condition For Strong Level
    # 1. (Lenght More Than 10)
    # 2. (Contain Three Type Of Symbol , Example ('ABCabc12301'))
    # 3. (Symbol Must Be Two Different In Lenght Two..)

    # Condition For Highly Recommended
    # 1. (Lenght More Than 10)
    # 2. (Contain Four Type Of Symbol , Example ('ABCabc12301!@#'))
    # 3. (Symbol Must Be Two Different In Lenght Two..)

    # Local Variable For Some Logic Building
    # Logic Given Following Below With Description

    Ps_Security_Level_Checker=[]
    Small_Alpha_level=0
    Letter_Aplha_level=0
    Integer_Number_level=0
    Symbol_Define_level=0
    Security_Final_Level=0

    # Checking Security Level Of Password
    # Frist It Check Lenght Of Password If Password Lenght More Than Or Equal To 10 
    if (len(ps)>=10):


        # Than In For Loop Getting All Character Of Password
        for i in ps:

            # Frist Nested For Loop
            # This Find Small Alphabet In Password
            for j in Small_Alpha:
                if (i==j):
                    # If Small Alphabet Found In Password It Set +1 In Given Variable 
                    Small_Alpha_level+=1


            # Second Nested For Loop
            # This Find Capital Alphabet In Password
            for k in Letter_Aplha:
                if (i==k):
                    # If Capital Alphabet Found In Password It Set +1 In Given Variable 
                    Letter_Aplha_level+=1


            # Third Nested For Loop
            # This Find Number (0 to 9 ) In Password
            for h in Integer_Number:
                if (i==h):
                    # If Number Found In Password It Set +1 In Given Variable 
                    Integer_Number_level+=1


            # Fourth Nested For Loop
            # This Find Symbol Like (!@#$) In Password
            for u in Symbol_Define:
                if (i==u):
                    # If Symbol Found In Password It Set +1 In Given Variable 
                    Symbol_Define_level+=1


            # If Every Given Variable Get +2 I Will Add Sum Of All


    # For Lenght Of Password Less Than 10        
    if (len(ps)<=10 and len(ps)>=6):
        Security_Final_Level+=2
            
            


    # If Sum Will Be 2 I Will Give OutPut As Low Level
    if (Small_Alpha_level>=2):
        Security_Final_Level+=2
    

    # If Sum Will Be 4 I Will Give OutPut As Medium Level
    if (Letter_Aplha_level>=2):
        Security_Final_Level+=2


    # If Sum Will Be 6 I Will Give OutPut As Strong Level
    if (Integer_Number_level>=2):
        Security_Final_Level+=2
    

    # If Sum Will Be 8 I Will Give OutPut As Highly Recommended Level
    if (Symbol_Define_level>=2):
        Security_Final_Level+=2

    
    # Seting Security Level Of Password

    # Low Level
    if (Security_Final_Level==2):
        Ps_Security_Level_Checker.append("Low Level")

    # Medium Lvel
    if (Security_Final_Level==4):
        Ps_Security_Level_Checker.append("Medium Level")

    # Strong Level
    if (Security_Final_Level==6):
        Ps_Security_Level_Checker.append("Strong Level")

    # Highly Recommended Level
    if (Security_Final_Level==8):
        Ps_Security_Level_Checker.append("Highly Recommended")
    
    # Delete Text In Entry Field
    txt.delete(0,END)
    txt.insert(0,Ps_Security_Level_Checker)

    # Print Level In Console
    print(Ps_Security_Level_Checker)
    


# GeoMetry Of Gui
pass_label.geometry("450x550+150+70")
pass_label.minsize(450,550)
pass_label.maxsize(450,550)

# Font For Words In Frame
font=("verdana",16,"bold")
txt_font=("verdana",22,"bold")


# Frame In Opened Windows
pass_frame=Frame(pass_label)
pass_frame.pack(side=TOP)


# Top String Label
Str_words=Label(pass_frame,text="Password Security Level Checker",font=font)
Str_words.pack(side=TOP,pady=21)

# Title For Windows
pass_label.title("Password Security Level Checker")

# Text Area For Entring Text
txt=Entry(pass_frame,font=txt_font,relief="ridge",justify=RIGHT)
txt.pack(side=TOP,pady=45)

# Button For Excute Command
btn=Button(pass_frame,font=font,text="Check Level",relief="ridge",command=Password_Security_Level_Checker)
btn.pack(side=TOP,pady=45)


# End Of Gui
pass_label.mainloop()

        





