import tkinter
import random
r=1
colours = ['Red','Blue','Green','Pink','Black','Yellow','Orange','Purple','Brown']
score = 0
highscore=0
live=True
messageids=[]
timeleft = 30
gameoverid=None
wonid=None
countdown_id=None

def save_name():
    global name
    name = name_entry.get()
    print(f"Name saved: {name}") 
    name_window.destroy()

def restartGame():
    global messageids,countdown_id,timeleft,live,score,highscore
    if score>highscore:
        high_score.config(text = "High Score: " + str(score))
    timeleft=30
    live=True
    score=0
    if countdown_id is not None:
        root.after_cancel(countdown_id)
    countdown_id=None
    for i in messageids:
        canvas.delete(i)
    startGame()

def startGame(event=None):
    if timeleft == 30 :
        countdown()
    # run the function to choose the next colour
    nextColour()

# Function to choose and display the next colour.
def nextColour():
    global score,timeleft,messageids, live,r

    # if a game is currently in play
    if timeleft > 0:
        live=True
        # make the text entry box active.
        e.focus_set()

        if e.get().lower() == colours[r].lower():
            score += 1

        elif e.get()!="" and e.get().lower() != colours[1].lower() and score<=10:
            over=canvas.create_text(240, 50, text=f"{name}'s GAME OVER!!", fill="red", 
                                    font="Calibri 20 bold ")
            messageids.append(over)
            root.update_idletasks()
            root.update()
            timeleft=0
            live=False

        if score>10:
            won=canvas.create_text(150, 50, text=f"{name} WON!!", fill="green", font="Calibri 20 bold ")
            messageids.append(won)
            root.update_idletasks()
            root.update()

        e.delete(0, tkinter.END)

        # change the colour to type, by changing the text _and_ the colour to a random colour value
        r=random.randint(0,8)
        random.shuffle(colours)
        # if game not over
        if live:
            label.config(fg = str(colours[r]), text = str(colours[0]))
        
        # update the score.
            scoreLabel.config(text = "Score: " + str(score))
    



# Countdown timer function 


def countdown():

    global timeleft,countdown_id,score,live

    # if a game is in play
    if timeleft > 0:

        # decrement the timer.
        timeleft -= 1
        
        # update the time left label
        timeLabel.config(text = "Time left: "
                               + str(timeleft))
                               
        # run the function again after 1 second.
        #timeLabel.after(1000, countdown)
        countdown_id=root.after(1000,countdown)
    else:
        if score<=10:
            over=canvas.create_text(240, 50, text=f"{name}'s GAME OVER!!", fill="red", font="Calibri 20 bold")
            messageids.append(over)
            root.update_idletasks()
            root.update()
            timeleft=0
            live=False

# Create the name input window
name_window = tkinter.Tk()
name_window.title("Enter Your Name")
name_window.geometry("300x100")
name_window.configure(bg="#F37D2F")
# Label and entry for name input
name_label = tkinter.Label(name_window, text="Enter your name:")
name_label.pack(pady=5)

name_entry = tkinter.Entry(name_window)
name_entry.pack(pady=5)
name_entry.focus_set()

# Bind the Enter key to the save_name function
name_entry.bind('<Return>', save_name)

# Button to submit name and close window
submit_button = tkinter.Button(name_window, text="Submit", command=save_name,fg="black",background="cyan")
submit_button.pack(pady=5)
name_window.bind('<Return>', lambda event: save_name())

name_window.mainloop()

# Driver Code

# create a GUI window
root = tkinter.Tk()
root.title("COLORGAME BY SAM")
root.geometry("475x450")
root.configure(bg="#168F8F")
canvas =tkinter.Canvas(root, width=450, height=100, bd=0, highlightthickness=2, 
                       highlightbackground="black", bg="#6DECAC")
canvas.create_text(240, 20, text=f"SAMYAK's COLOUR GAME", fill="black", font="Calibri 14  bold")
canvas.pack(padx=10, pady=20)
# add an instructions label
instructions = tkinter.Label(root, text = f"Hey {name} ,type in the colour of the words, and not the word text!\n To WIN you have to cross the score of 10::",
                                      font = ('Helvetica', 12),fg="black",background="#6DECAC")
instructions.pack() 

scoreLabel = tkinter.Label(root, text = "Press enter to start:",font = ('Helvetica', 12,'bold')
                           ,fg="brown",background="#6DECAC")
scoreLabel.pack(padx=10,pady=5)

high_score=tkinter.Label(root, text = "High Score: 0",font = ('Helvetica', 12,'bold')
                           ,fg="brown",background="#6DECAC")
high_score.pack(padx=10)



timeLabel = tkinter.Label(root, text = "Time left: " +str(timeleft),fg="black"
                          , font = ('Helvetica', 12,'bold'),background="#6DECAC")   
timeLabel.pack(pady=5)

label = tkinter.Label(root, font = ('Helvetica', 60),background="white")
label.pack(pady=5)

# add a text entry box for typing in colours
e = tkinter.Entry(root)
e.pack()

# set focus on the entry box
e.focus_set()
restart_button=tkinter.Button(root,text="Restart",command=restartGame,fg="black",background="cyan")
restart_button.pack(padx=10,pady=10)
# run the 'startGame' function 
# when the enter key is pressed
root.bind('<Return>', startGame)
# start the GUI
root.mainloop()
