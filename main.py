# Applications using Tkinter

# 1. Import tkinter 
from tkinter import *

'''------------------------ Functions --------------------------''' 
# function to compute and display Multiplcation Table
def multiplication_table():
    txtTable_MT.delete("1.0", END)
    try:
        n = int(entNumber_MT.get())
    except ValueError:
        txtTable_MT.insert(END, 'Invalid input')
    
    for i in range(1,13):
        row = "{:3} x {:2} = {:3}\n".format(i, n, i * n)
        txtTable_MT.insert(END, row)

# function to calculate and display BMI
def calc_bmi():
    txtBMI_BMI.delete("1.0", END)
    try:
        weight = float(entWeight_BMI.get())
        height = float(entHeight_BMI.get())
    except ValueError:
        txtBMI_BMI.insert(END, 'Invalid input')
    
    if height > 5:
        txtBMI_BMI.insert(END, 'Invalid input')
    else:
        bmi = weight / (height ** 2)
        txtBMI_BMI.insert(END, round(bmi,2))

# function to calculate compound interest
def calc_CMPDINT():
    txtAmount_CMPDINT.delete('1.0', END)
    try:
        p = float(entPrincipal_CMPDINT.get())
        r = float(entInt_CMPDINT.get())
        n = float(entRate_CMPDINT.get())
        t = float(entTimes_CMPDINT.get())
    except ValueError:
        txtAmount_CMPDINT.insert(END, 'Invalid input')
    
    if r > 1:
        txtAmount_CMPDINT.delete('1.0', END)
        txtAmount_CMPDINT.insert(END, 'Invalid input')
    else:
        amount = p * ((1 + (r/n)) ** (n*t))
        txtAmount_CMPDINT.insert(END, round(amount,2)) 

# function to use caesar cipher (substitution cipher)
def caesar_cipher_SCCC():
    txtCipher_SCCC.delete('1.0', END)
    try:
        plaintext = str(entPlain_SCCC.get()).upper()
        pos_shift = int(entShift_SCCC.get())
    except ValueError:
        txtCipher_SCCC.insert(END, 'Invalid input')
    
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ciphertext = ''
    mistake = False
    
    for letter in plaintext:
        if letter not in alphabet:
            mistake = True
        else:
            key = ((alphabet.find(letter)) + pos_shift) % 26
            letter = alphabet[key]
            ciphertext += letter
    
    if mistake == True:
        txtCipher_SCCC.insert(END, 'Invalid input')
    else:
        txtCipher_SCCC.insert(END, ciphertext)

# function to show a frame
def raise_frame(frame):
    frame.tkraise()
''' ------------------------------------------------------------ '''

''' Main Window '''
# Create main window 
window = Tk()
window.title('Function Applications')
window.iconbitmap('c:/Personal Projects/Python/GUI Project/python.ico')
window.geometry('800x400')
''' ----------- '''


''' Frame 1 : Multiplcation Table  '''
frame1 = Frame(window, bg='light yellow', width=500, height=300)

# Add widgets
lblTitle_MT = Label(frame1, text="Multiplcation Table", bg="light yellow", font=('Lucida Calligraphy', 12))
lblNumber_MT = Label(frame1, text="Enter number", width=10)
entNumber_MT = Entry(frame1, width=29)
btnDisplay_MT = Button(frame1, text="Display table", width=10, command=multiplication_table)
txtTable_MT = Text(frame1, fg='blue', width=22, height=12)

# Organize (lay out) the widgets using place() manager
lblTitle_MT.place(x=20, y=10)
lblNumber_MT.place(x=20, y=50)
btnDisplay_MT.place(x=20, y=90)
entNumber_MT.place(x=120, y=50)
txtTable_MT.place(x=120, y=90)
''' ------------------------------ '''


''' Frame 2 : BMI Calculator  '''
frame2 = Frame(window, bg='light blue', width=500, height=300)

# Add widgets
lblTitle_BMI = Label(frame2, text="BMI Calculator", bg="light blue", font=('Lucida Calligraphy', 12))
lblWeight_BMI = Label(frame2, text="Weight (kg)", width=12)
lblHeight_BMI = Label(frame2, text="Height (m)", width=12)
entWeight_BMI = Entry(frame2, width=20)
entHeight_BMI = Entry(frame2, width=20)
lblBMI_BMI = Label(frame2, text="BMI", width=12)
txtBMI_BMI = Text(frame2, width=15, height=1, fg="blue")
btnCalculate_BMI = Button(frame2, text="Calculate", width=10, command=calc_bmi)

# Organize (lay out) the widgets using place() manager
lblTitle_BMI.place(x=20, y=10)     
lblWeight_BMI.place(x=20, y=50)
lblHeight_BMI.place(x=20, y=90)
lblBMI_BMI.place(x=20, y=130)
entWeight_BMI.place(x=120, y=50)
entHeight_BMI.place(x=120, y=90)
txtBMI_BMI.place(x=120, y=130)
btnCalculate_BMI.place(x=260, y=130)
''' ------------------------- '''


''' Frame 3 : Compound Interest Calculator '''
frame3 = Frame(window, bg='light green', width=500, height=300)

# Add widgets
lblTitle_CMPDINT = Label(frame3, text='Compound Interest Calculator', bg='light green', font=('Lucida Calligraphy', 12))
lblPrincipal_CMPDINT = Label(frame3, text='Principal Amount ($)', width=30)
lblInt_CMPDINT = Label(frame3, text='Annual Interest Rate (decimal)', width=30)
lblRate_CMPDINT = Label(frame3, text='Number of times compounded per year', width=30)
lblTimes_CMPDINT = Label(frame3, text='Number of years to be compounded', width=30)
lblAmount_CMPDINT = Label(frame3, text='Final amount ($)', width=30)
entPrincipal_CMPDINT = Entry(frame3, width=20)
entInt_CMPDINT = Entry(frame3, width=20)
entRate_CMPDINT = Entry(frame3, width=20)
entTimes_CMPDINT = Entry(frame3, width=20)
txtAmount_CMPDINT = Text(frame3, width=15, height=1, fg='blue')
btnCalculate_CMPDINT = Button(frame3, text='Calculate', width=10, command=calc_CMPDINT)

# Organize (lay out) the widgets using place() manager
lblTitle_CMPDINT.place(x=20, y=10)
lblPrincipal_CMPDINT.place(x=20, y=50)
lblInt_CMPDINT.place(x=20, y=90)
lblRate_CMPDINT.place(x=20, y=130)
lblTimes_CMPDINT.place(x=20, y=170)
lblAmount_CMPDINT.place(x=20, y=210)
entPrincipal_CMPDINT.place(x=250, y=50)
entInt_CMPDINT.place(x=250, y=90)
entRate_CMPDINT.place(x=250, y=130)
entTimes_CMPDINT.place(x=250, y=170)
txtAmount_CMPDINT.place(x=250, y=210)
btnCalculate_CMPDINT.place(x=390, y=210)
''' -------------------------------------- '''


''' Frame 4 : Caesar Cipher '''
frame4 = Frame(window, bg='pale violet red', width=500, height=300)

# Add widgets
lblTitle_SCCC = Label(frame4, text='Caesar Cipher', bg='pale violet red', font=('Lucida Calligraphy', 12))
lblPlain_SCCC = Label(frame4, text='Plaintext', width=25)
lblShift_SCCC = Label(frame4, text='Number of positions to shift', width=25)
entPlain_SCCC = Entry(frame4, width=20)
entShift_SCCC = Entry(frame4, width=20)
txtCipher_SCCC = Text(frame4, width=15, height=1, fg='blue')
btnDisplay_SCCC = Button(frame4, text='Display Ciphertext', width=25, command=caesar_cipher_SCCC)

# Organize (lay out) the widgets using place() manager
lblTitle_SCCC.place(x=20, y=10)
lblPlain_SCCC.place(x=20, y=50)
lblShift_SCCC.place(x=20, y=90)
entPlain_SCCC.place(x=220, y=50)
entShift_SCCC.place(x=220, y=90)
txtCipher_SCCC.place(x=220, y=130)
btnDisplay_SCCC.place(x=20, y=130)
''' ---------------------- '''


''' Main window '''
# Menu framing
frmMenu = Frame(window, bg='light grey', width=300, height=300)
lblMenu = Label(frmMenu, text='Main Menu', width=9, fg='blue', bg='light grey', font=('Lucida Calligraphy', 12))
lblMenu.place(x=20, y=10)
frameMenu = Frame(window, bg='grey', width=500, height=300)
lblMenu1 = Label(frameMenu, text='Welcome! Click on a function to get started.', width=30, bg='light grey', font=('Lucida Calligraphy', 12))
lblMenu1.place(x=70, y=20)
creatorLabel = Label(window, text='Created by Roseller Armirola', width=32, bg='light grey', fg='black')
creatorLabel.place(x=20, y=300)
versionLabel = Label(window, text='v2.0', width=10, fg='black') # Change after every update
versionLabel.place(x=700, y=325)

# Menu navigation buttons
btn1 = Button(frmMenu, text='Multiplcation Table', width=25, fg='blue', command=lambda:raise_frame(frame1))
btn1.place(x=20, y=50)
btn2 = Button(frmMenu, text='BMI Calculator', width=25, fg='blue', command=lambda:raise_frame(frame2))
btn2.place(x=20, y=90)
btn3 = Button(frmMenu, text='Compound Interest Calculator', width=25, fg='blue', command=lambda:raise_frame(frame3))
btn3.place(x=20, y=130)
btn4 = Button(frmMenu, text='Caesar Cipher', width=25, fg='blue', command=lambda:raise_frame(frame4))
btn4.place(x=20, y=170)

# Menu layout
frmMenu.place(x=20, y=20)
frameMenu.place(x=250, y=20)
frame1.place(x=250, y=20)
frame2.place(x=250, y=20)
frame3.place(x=250, y=20)
frame4.place(x=250, y=20)

raise_frame(frameMenu)
''' ----------- '''


window.mainloop()

''' Future Changelogs (notes)
- Import functions from week 4 weekly exercises
'''