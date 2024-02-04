
import random
from tkinter import *

global quiz0
global quiz1
quiz0 = [
    {
        "word" : "ALPHANSO",
        "hint" : "A famous variety of mango"
        
    },
    {
        "word" : "GRATITUDE",
        "hint" : "An expression of thankfulness"
    },
    {
        "word" : "MENDELEEVIUM",
        "hint" : "An element named after the scientist Dmitri Mendeleev"
    },
    {
        "word" : "HOLLYWOOD",
        "hint" : "Film Industry of the west"
    },
     {
        "word" : "PENINSULA",
        "hint" : "A landmass covered by water on three sides"
    },
    {
        "word" : "SNITCH",
        "hint" : "Complaining about someone to some authority behind their back"
    },
    {
        "word" : "CACOPHONY",
        "hint" : "A harsh, discordant mixture of sounds"
    },
    {
        "word" : "EPITOME",
        "hint" : "A perfect example, embodiment of any quality"
    },
    {
        "word" : "SUBCONTINENT",
        "hint" : "A large distinguishable part of a continent"
    },
    {
        "word" : "AESTHETIC",
        "hint" : "Concerned with beauty or the appreciation of beauty"
    },
    {
        "word" : "HALLELUJAH",
        "hint" : "Uttered in worship or as an expression of rejoicing"
    },
    {
        "word" : "SUPERSTITION",
        "hint" : "A widely held but irrational belief in supernatural influences"
    }, 
    {
        "word" : "DIFFERENTIATION",
        "hint" : "The process by which cells acquire specialized features"
    }, 
    {
        "word" : "CIRCUMSTANCE",
        "hint" : "A fact or condition connected with or relevant to an event or action"
    }, 
    {
        "word" : "SUBTLE",
        "hint" : "So delicate or precise as to be difficult to analyse or describe"
    }, 
    {
        "word" : "OSTENTATIOUS",
        "hint" : "Characterized by pretentious or showy display"
    },

]
quiz1 = []
global chances
global qword
global hint
global word
global score
global quiz
global q
score = 0 
chances = 5

if len(quiz0) > len(quiz1) :
        quiz = quiz0
        q = quiz1
else:
        quiz = quiz1
        q = quiz0

    
def gameSetup():
    global gamewindow
    global b1
    global canvas1
    global canvas0

    gamewindow = Tk()
    gamewindow.title("Word Guessing Game")
    gamewindow.geometry('600x500')

    canvas1 = Canvas(gamewindow,width=600,height=500,bg="lightpink")
    canvas1.pack(fill="both", expand=False)
    
    canvas1.create_text(300, 65, text="WORD GUESSING GAME", font=(("Comic Sans MS",30,"bold")),fill="#aa3366")
    canvas1.create_text(300, 185, text="How to play:", font=(("Comic Sans MS",17,"underline bold")),fill="#ffffff")
    canvas1.create_text(300, 260, text="Rearrange the jumble and make a guess \nbased on the hints provided and score a\npoint on every correct answer !!", font=(("Comic Sans MS",17,"bold")),fill="#ffffff")

    b1 = Button(gamewindow,text="START",font=(("Comic Sans MS",20,"bold")),command=game,width=8,height=1,bg="#aa3355",bd=3,fg="#ffffff")
    b1.place(x=220,y=390)

    gamewindow.resizable(False,False)
    gamewindow.mainloop()

    

def game():
    b1.destroy()
    canvas1.destroy()
    global canvas2
    global canvas3
    global chances
    global e1
    global word
    global item
    global score
   
    canvas2 = Canvas(gamewindow,width=600,height=500,bg="lightpink")
    canvas2.pack()
    canvas2.create_text(300, 65, text="WORD GUESSING GAME", font=(("Comic Sans MS",30,"bold")),fill="#aa3366")
    
    if chances :

        item = random.choice(quiz)
        word = item["word"]
        hint = item["hint"]
        qword = ''.join(random.sample(word,len(word)))

    
        canvas2.create_text(300,220,text=qword,font=(("Comic Sans MS",40,"bold")),fill = "#aa3355")
        canvas2.create_text(300,270,text="Hint: "+hint,font=(("Comic Sans MS",12,"bold")),fill = "#ffffff")

        canvas2.create_text(470,130,text="Score: "+str(score),font=(("Comic Sans MS",20,"bold")),fill = "#ffffff")
        canvas2.create_text(120,130,text="Chances: "+str(chances),font=(("Comic Sans MS",20,"bold")),fill = "#ffffff")

        
        e1 = Entry(gamewindow,width=20,justify="center",font=(("Comic Sans MS",18,"bold")),bd=5,bg="#ffffff")
        e1.place(x=130,y=300)
    
        b2 = Button(gamewindow,text="ENTER",font=(("Comic Sans MS",20,"bold")),command=newg,width=8,height=1,bg="#aa3355",bd=3,fg="#ffffff")
        b2.place(x=220,y=390)
        chances -= 1
    else:

        if score == 5 :
            msg="CONGRATULATIONS!! YOU WON"
        elif score == 4 or score == 3 :
            msg="Good job!! Almost there..."
        elif score<3 and score>0 :
            msg="Better luck next time...."
        elif score == 0:
            msg="YOU LOSE!!"

        
        canvas3.destroy()
        canvas2.create_text(300,220,text="SCORE: "+str(score)+"/5",font=(("Comic Sans MS",60,"bold")),fill = "#ffffff")
        canvas2.create_text(300,300,text=msg,font=(("Comic Sans MS",25,"bold")),fill = "#aa3355")
       
       
        b4 = Button(gamewindow,text="RESTART",font=(("Comic Sans MS",20,"bold")),command=rstgame,width=9,height=1,bg="#aa3355",bd=3,fg="#ffffff")
        b4.place(x=220,y=390)


def newg():
    global canvas3
    global e1
    global word
    global item
    ans = e1.get()
    global score
    
    canvas2.destroy()
    canvas3 = Canvas(gamewindow,height=590,width=600,background="lightpink")
    canvas3.pack()
    canvas3.create_text(300, 65, text="WORD GUESSING GAME", font=(("Comic Sans MS",30,"bold")),fill="#aa3366")
    
    if ans.upper() == word:
        canvas3.create_text(300, 250, text="Correct Guess!!", font=(("Comic Sans MS",50,"bold")),fill="#aa3366")
        score+= 1
        
    else:
        canvas3.create_text(300, 250, text="Wrong Guess!!", font=(("Comic Sans MS",50,"bold")),fill="#aa3366")

    quiz.remove(item)
    q.append(item) 

    canvas3.create_text(470,130,text="Score: "+str(score),font=(("Comic Sans MS",20,"bold")),fill = "#ffffff")
    canvas3.create_text(120,130,text="Chances: "+str(chances),font=(("Comic Sans MS",20,"bold")),fill = "#ffffff")

    b3 = Button(gamewindow,text="NEXT",font=(("Comic Sans MS",20,"bold")),command=nextg,width=8,height=1,bg="#aa3355",bd=3,fg="#ffffff")
    b3.place(x=220,y=390)
    

def nextg():
    global canvas3
    canvas3.destroy()
    game()


def rstgame():
    global score
    global chances
    global canvas2
    global q
    global quiz
    global quiz0
    global quiz1
    
    score = 0
    chances = 5
    gamewindow.destroy()
    if len(quiz0) > len(quiz1) :
        quiz = quiz0
        q = quiz1
    else:
        quiz = quiz1
        q = quiz0

    gameSetup()

gameSetup()



  
       

    