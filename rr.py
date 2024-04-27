from tkinter import *
from PIL import Image, ImageTk
from random import randint

#main window
root = Tk() 
root.title('rock- scissor - paper')
root.configure(bg='black')

#picture 
rock_img = ImageTk.PhotoImage(Image.open('rocking.png'))
scissor_image = ImageTk.PhotoImage(Image.open("scissoring.png"))
paper_img = ImageTk.PhotoImage(Image.open("papering.png"))
rockuser_img = ImageTk.PhotoImage(Image.open('rocking.png'))
scissoruser_image = ImageTk.PhotoImage(Image.open("scissoring.png"))
paperuser_img = ImageTk.PhotoImage(Image.open("papering.png"))

#insert picture 
user_label = Label(root, image=scissor_image, bg='yellow')
comp_label = Label(root, image=scissoruser_image, bg='yellow')
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

#scores 
playerScore = Label(root, text=0, bg='black', fg='pink')
computerScore = Label(root, text=0, bg='black', fg='cyan')
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)

#indicator
user_indicator = Label(root, font=50, text="USER", bg='black', fg='yellow')
computer_indicator = Label(root, font=50, text="COMPUTER", bg='black', fg='yellow')
computer_indicator.grid(row=0, column=3)
user_indicator.grid(row=0, column=1)

#messages 
msg = Label(root, font=50, bg='black', fg="pink")
msg.grid(row=3, column=2)

#update message 
def updateMessage(x):
    msg['text'] = x

#update user score 
def updateuserscore():
    score = int(playerScore['text'])
    score += 1
    playerScore['text'] = str(score)

#update computer score
def updatecomputerscore():
    score = int(computerScore['text'])
    score += 1
    computerScore['text'] = str(score)

# check winner 
def checkwin(player, computer):
    if player == computer:
        updateMessage("It's a tie")
    elif player == "rock":
        if computer == 'paper':
            updateMessage('Computer Wins!\t\nYou lose!')
            updatecomputerscore()
        else:
            updateMessage("You Win!\t\nComputer loses!")
            updateuserscore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage('Computer Wins!\t\nYou lose!')
            updatecomputerscore()
        else:
            updateMessage("You Win!\t\nComputer loses!")
            updateuserscore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage('Computer Wins!\t\nYou lose!')
            updatecomputerscore()
        else:
            updateMessage("You Win!\t\nComputer loses!")
            updateuserscore()
    else:
        pass

#update_choices
choices = ['rock', 'paper', "scissor"]
def update_choice(x):
    #for computer 
    computerchoice = choices[randint(0,2)]
    if computerchoice == 'rock':
        comp_label.configure(image=rock_img)
    elif computerchoice == 'paper':
        comp_label.configure(image=paper_img)
    else:
        comp_label.configure(image=scissor_image)
    #for user 
    if x == 'rock':
        user_label.configure(image=rockuser_img)
    elif x == 'paper':
        user_label.configure(image=paperuser_img)
    else:
        user_label.configure(image=scissor_image)    

    checkwin(x, computerchoice)

#button
rock = Button(root, width=20, height=2, text='Rock', bg="black", fg="pink", command=lambda: update_choice('rock'))
paper = Button(root, width=20, height=2, text='Paper', bg='black', fg='cyan', command=lambda: update_choice('paper'))
scissor = Button(root, width=20, height=2, text='Scissor', bg='black', fg='yellow', command=lambda: update_choice('scissor'))

rock.grid(row=2, column=1)
paper.grid(row=2, column=2)
scissor.grid(row=2, column=3)

#main
root.mainloop()
