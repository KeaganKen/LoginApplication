# JOIN MY DISCORD! discord.gg/dVSVGgqv2Q
from tkinter import *
import mysql.connector






#Connects to the database
db = mysql.connector.connect(user="root", host="127.0.0.1", database="passwords")
mycursor = db.cursor(buffered=True)

#Fetches rows (Username and password)from the database so it can later compare them
mycursor.execute("SELECT username FROM login_details")

raw_username = mycursor.fetchall()

mycursor.execute("SELECT password FROM login_details")

raw_password = mycursor.fetchall()


#Tkinter GUI register window to Sign up which then writes the information to the database
def register_scr():

    #Setting up and configuring window
    global register_screen
    register_screen = Tk()
    register_screen.title("Create an Account")
    register_screen.geometry('300x250')
   
    #Basic Labels for the GUI
    Label(register_screen, text = 'Register!', font={'Calibri', 13}).pack()
    Label(register_screen, text='').pack()
    Label(register_screen, text='Username:').pack()

    #Fetches the text from the text box
    userentry = Entry(register_screen, width=20, bg="white") 
    userentry.pack()
    Label(register_screen, text='Password:').pack()
    passentry = Entry(register_screen, width=20, bg="white")
    passentry.pack()
    
    
    
    
    def register():
        entered_user=userentry.get()
        entered_pass=passentry.get()
        
        mycursor.execute("SELECT username FROM login_details")

        raw_username = mycursor.fetchall()
        if not 0 < len(entered_user) < 20:
            print("Username too short or too long")
        else:
            for user in raw_username:
                user = user[0]
                if user == entered_user:
                    print('Username Already Exists')
                    break
            else:
                    print("Account has been Registered!")
                    mycursor.execute("INSERT INTO login_details(username, password) VALUES (%s,%s)", (entered_user, entered_pass))
                    db.commit()
        
        
        


    Button(register_screen, text="Register", bg='#20bebe', fg='white', height=2, width=30, command=register).pack(pady=10)




#Tkinter GUI login window to login which then compares the information to the database
def login_screen():
    #Setting up and configuring window
    global window
    window = Tk()
    window.title("Login")
    window.geometry('300x250')

        
    #Labels for the GUI
    Label(window, text = 'Login', font={'Calibri', 13}).pack()
    Label(window, text='').pack()
    Label(window, text='Username:').pack()
    
    #Fetches text from Text Entry box
    userentry = Entry(window, width=20, bg="white") 
    userentry.pack()
    Label(window, text='Password:').pack()
    passentry = Entry(window, width=20, bg="white")
    passentry.pack()

    
    def click():
        entered_user=userentry.get()
        entered_pass=passentry.get()

        print("Entered Username: ", entered_user)
        print("Entered Password: ", entered_pass, "\n")
        mycursor.execute("SELECT username FROM login_details")
        raw_username = mycursor.fetchall()
        mycursor.execute("SELECT password FROM login_details")
        raw_password = mycursor.fetchall()
        
        for user, pw in zip(raw_username, raw_password):
            user = user[0]
            pw = pw[0]
            print("Database: ", user, pw)
            if user == entered_user and pw == entered_pass:
                print("Login Successful!")
                break
        else:
                print("Login Incorrect!")

    Button(window, text="Login", command=click, bg='#20bebe', fg='white', height=4, width=25) .pack(pady=10)
    window.mainloop()
    
       
    return userentry, passentry,




#Function to open another window via click of a button
def Close():
    login_screen()
    Tk.destroy()
    
#Main screen to choose if you wanna open a Register window or Login window
def option_screen():
    global screen
    screen = Tk()
    screen.title("Login or Register")
    screen.geometry('300x250')
    Label(text = 'Login or Register an Account!', font={'Calibri', 13}).pack()
    Button(screen, text="Login", bg='#20bebe', fg='white', height=2, width=30, command=Close).pack(pady=10)
    Button(screen, text="Register", bg='#20bebe', fg='white', height=2, width=30, command=register_scr) .pack(pady=10)
    screen.mainloop()



#Opens the option screen
option_screen()


