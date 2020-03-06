from tkinter import *
#from tkinter.ttk import *
from tkinter import messagebox

Position = 0


def cleartextboxes():
    FirstnameTextBox.configure(state='normal')
    FirstnameTextBox.delete('1.0','end')
    SurnameTextBox.configure(state='normal')
    SurnameTextBox.delete('1.0','end')
    DateOfBirthTextBox.configure(state='normal')
    DateOfBirthTextBox.delete('1.0','end')
    AgeTextBox.configure(state='normal')
    AgeTextBox.delete('1.0','end')
    default1.set('Choose an Option')
    DiscountTextBox.configure(state='normal')
    DiscountTextBox.delete('1.0','end')
    DiscountTextBox.configure(state='disabled')

def loadMembers():
    global Position
    global MemberList
    global NumberOfMembers

    with open("Members1.txt") as members:
        MemberList = members.read().splitlines()

    NumberOfMembers = len(MemberList)
    MemberRecords = str(MemberList[Position]).split(",")

    cleartextboxes()

    Firstname = FirstnameTextBox.insert('1.0',MemberRecords[0])
    Surname = SurnameTextBox.insert('1.0',MemberRecords[1])
    DateofBirth = DateOfBirthTextBox.insert('1.0',MemberRecords[2])
    Age = AgeTextBox.insert('1.0',MemberRecords[3])
    default1.set(MemberRecords[4])

    members.close()

def nextMember():
    global Position
    global MemberList
    global NumberOfMembers

    if NumberOfMembers == Position + 1:
        messagebox.showerror("Error Message","End of Database")
    else:
        Position = Position + 1

        MemberRecords = str(MemberList[Position]).split(",")

        cleartextboxes()

        Firstname = FirstnameTextBox.insert('1.0',MemberRecords[0])
        Surname = SurnameTextBox.insert('1.0',MemberRecords[1])
        DateofBirth = DateOfBirthTextBox.insert('1.0',MemberRecords[2])
        Age = AgeTextBox.insert('1.0',MemberRecords[3])
        default1.set(MemberRecords[4])

def previousMember():
    global Position
    global MemberList
    global NumberOfMembers

    if 0 == Position:
        messagebox.showerror("error Message","Start of Database")
    else:
        Position = Position - 1

        MemberRecords = str(MemberList[Position]).split(",")

        cleartextboxes()

        Firstname = FirstnameTextBox.insert('1.0',MemberRecords[0])
        Surname = SurnameTextBox.insert('1.0',MemberRecords[1])
        DateofBirth = DateOfBirthTextBox.insert('1.0',MemberRecords[2])
        Age = AgeTextBox.insert('1.0',MemberRecords[3])
        default1.set(MemberRecords[4])



def saveMember():
    global NumberOfMembers
    Firstname = FirstnameTextBox.get('1.0','end-1c')
    Surname = SurnameTextBox.get('1.0','end-1c')
    DateofBirth = DateOfBirthTextBox.get('1.0','end-1c')
    Age = AgeTextBox.get('1.0','end-1c')
    friends = default1.get()
    
    if NumberOfMembers >= 20:
        messagebox.showerror("Error Message","Max Amount of Members Reached")
    elif (Firstname == ""):
        messagebox.showerror("Error Message", "Firstname is blank")
    elif (Surname == ""):
        messagebox.showerror("Error Message", "Surname is blank")
    elif (DateofBirth == ""):
        messagebox.showerror("Error Message", "DateofBirth is blank")
    elif (Age == ""):
        messagebox.showerror("Error Message", "Age is blank")
    elif (friends == "Choose an Option"):
        messagebox.showerror("Error Message", "Select friend amount")
    else:
        MemberRecords = (Firstname + "," + Surname +"," + DateofBirth + "," + Age + "," + friends + "\n")
        Members = open("Members1.txt","a")
        Members.write(MemberRecords)
        Members.close()

        cleartextboxes()

def calculateDiscount(*args):
    if 'Choose an Option' == default1.get():
        return default1
    else:
        N2 = default1.get()
        # print(N2)
        Discount = 5*int(N2)
        # print(Discount)
        DiscountTextBox.configure(state='normal')
        DiscountTextBox.delete('1.0','end')
        DiscountTextBox.insert('1.0', f'-{Discount}%')
        DiscountTextBox.configure(state='disabled')

def hi():
    print('hi')

# def calculateCost(*args):
    
    

mywindow = Tk()
mywindow.grid()
mywindow.title('Members and Moneys')
#mywindow.configure(bg = 'light blue')
label = Label(mywindow, text='Members')
label.grid(row=0,column=0,columnspan=5)

FirstnameLabel = Label(mywindow,text='Firstname')
FirstnameLabel.grid(row=1,column=0,columnspan=1)
FirstnameTextBox = Text(mywindow,width=20,height=2)
FirstnameTextBox.grid(row=1,column=1,sticky='E')

SurnameLabel = Label(mywindow,text='Surname')
SurnameLabel.grid(row=2,column=0,columnspan=1)
SurnameTextBox = Text(mywindow,width=20,height=2)
SurnameTextBox.grid(row=2,column=1,sticky='E')

DateOfBirthLabel = Label(mywindow,text='DateofBirth')
DateOfBirthLabel.grid(row=3,column=0,columnspan=1)
DateOfBirthTextBox = Text(mywindow,width=20,height=2)
DateOfBirthTextBox.grid(row=3,column=1,sticky='E')

AgeLabel = Label(mywindow,text='Age')
AgeLabel.grid(row=4,column=0,columnspan=1)
AgeTextBox = Text(mywindow,width=20,height=2)
AgeTextBox.grid(row=4,column=1,sticky='E')

default1 = StringVar(mywindow)
choices = [ '0', '1','2','3','4']
default1.set('Choose an Option')
dropdownMenu = OptionMenu(mywindow, default1, *choices)
Label(mywindow, text="Choose amount of friends").grid(row = 5, column = 0)

dropdownMenu.grid(row = 5, column =1)

DiscountLabel = Label(mywindow,text='Discount')
DiscountLabel.grid(row=6,column=0,columnspan=1)
DiscountTextBox = Text(mywindow,width=20,height=2)
DiscountTextBox.grid(row=6,column=1,sticky='E')
DiscountTextBox.config(state=DISABLED)

default1.trace('w', calculateDiscount)

NewMemberButton = Button(mywindow,text='New Member', command=cleartextboxes)
NewMemberButton.grid(row=7,column=0,columnspan=1)
SaveMemberButton = Button(mywindow,text='Save Member', command=saveMember)
SaveMemberButton.grid(row=7,column=1,columnspan=1)
LoadMembersButton = Button(mywindow,text='Load Members', command=loadMembers)
LoadMembersButton.grid(row=8,column=1,columnspan=1)
PreviousMemberButton = Button(mywindow,text='Previous Member', command=previousMember)
PreviousMemberButton.grid(row=8,column=0,columnspan=1)
NextMemberButton = Button(mywindow,text='Next Member',command=nextMember)
NextMemberButton.grid(row=8,column=2,columnspan=1)



#def change_dropdown(*args):
     #friends = default1.get()
     #print( default1.get() )
     

#default1.trace('w', change_dropdown)


if __name__ == '__main__':
    mywindow.mainloop()
        


