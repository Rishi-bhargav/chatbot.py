import random
from tkinter import *
root = Tk()
root.title('Chat Bot')
root.configure(bg='teal')
root.geometry('1000x850')
root.resizable(False,False)
scroll_bar = Scrollbar(root)    
  
scroll_bar.pack( side = RIGHT,fill = Y )
txt=Text(root)
txt.configure(bg='white',fg='blue',font=('Times New Roman',14,'italic'),yscrollcommand= scroll_bar.set,height=30)




def send():
    send="You :"+ e.get()
    txt.insert(END,"\n "+send)

    if(e.get()=="hii")or(e.get()=="hello") or (e.get()=="what's up") or (e.get()=="greetings"):
        greeting1=['hey !' ,'hi !','hello','Hi there','I am glad! you are talking to me']
        txt.insert(END,"\n"+"Bot : "+random.choice(greeting1))

    elif(e.get()=="how are you?")or(e.get()=="how's it going?") or (e.get()=="how do you do?"):
        greeting2=['good ! what about you?','I am good and you ?','fine, thankyou']
        txt.insert(END,"\n"+"Bot : "+random.choice(greeting2))

    elif(e.get()=="I am also fine")or(e.get()=="fine") or (e.get()=="good"):
        greeting0=['How may i help you?','what can i do for you ?']
        txt.insert(END,"\n"+"Bot : "+random.choice(greeting0))
    elif(e.get()=="I am also good") or (e.get()=='good') or (e.get()=="fine") or (e.get()=="great"):
        greetings=['how can i help you?','what can i do for you?']
        txt.insert(END,"\n"+"Bot : "+random.choice(greetings))
    elif(e.get()=="good morning") or (e.get()=='morning'):
        greeting3=['good morning','morning ! have a great day','good day']
        txt.insert(END,"\n"+"Bot : "+random.choice(greeting3))
    elif(e.get()=="good night") or (e.get()=='night'):
        greeting4=['good night','night ! have a good sleep']
        txt.insert(END,"\n"+"Bot : "+random.choice(greeting4))
    elif(e.get()=="good evening"):
        greeting5=['good evening']
        txt.insert(END,"\n"+"Bot : "+random.choice(greeting5))
    elif(e.get()=="good afternoon") or (e.get()=='afternoon'):
        greeting6=['good afternoon','afternoon']
        txt.insert(END,"\n"+"Bot : "+random.choice(greeting6))
    elif(e.get()=="what is your name?") or (e.get()=="who are you?"):
        intro=['My name is baby bot.','I am baby bot.','baby bot.']
        txt.insert(END,"\n"+"Bot : "+random.choice(intro))
    elif(e.get()=="what can you do?"):
        origin=['I am a chat bot, we can chat','chatting']
        txt.insert(END,"\n"+"Bot : "+random.choice(origin))
    elif(e.get()=="namaste") or (e.get()=="namaskaar"):
        origin=['namaste','namaskaar']
        txt.insert(END,"\n"+"Bot : "+random.choice(origin))
    elif(e.get()=="bye") or (e.get()=='goodbye') or (e.get()=="see you") :
        greetings=['bye','goodbye','see you','have a great day']
        txt.insert(END,"\n"+"Bot : "+random.choice(greetings))
    elif(e.get()=="Are you human"):
        origin=['No']
        txt.insert(END,"\n"+"Bot : "+random.choice(origin))
    elif(e.get()=="Do you have a hobby?"):
        origin=['YES,talking','Yes,replying']
        txt.insert(END,"\n"+"Bot : "+random.choice(origin))
    elif(e.get()=="Say anything"):
        origin=['You are nice person','great meeting you','You are awesome','I think you are great!']
    elif(e.get()=="Tell me some facts") or (e.get()=="Some more"):
        origin=['Competitive art used to be in the Olympics. ...','The majority of your brain is fat. ...','Oranges are not naturally occurring fruits.']   
        txt.insert(END,"\n"+"Bot : "+random.choice(origin))
    elif(e.get()=="Do you know other chatbots"):
        origin=['TGIFridays','AccuWeather','Fandango']
        txt.insert(END,"\n"+"Bot : "+random.choice(origin))
    else:
        txt.insert(END,"\n"+ "Bot : Sorry,still learning about it. ")
    e.delete(0,END)
    
txt.pack()
scroll_bar.config(command=txt.yview)

def clear():
    txt.delete('1.0',END)
e=Entry(root,width=20,font=('Times New Roman',16,'bold'),fg='black')
e.place(x=600,y=700)
send=Button(root,width=7,text='Send',bg='white',fg='black',command=send,font=('Times New Roman',14))
send.place(x=600,y=750)
clear=Button(root,width=7,text='Clear',bg='white',fg='black',command=clear,font=('Times New Roman',14))
clear.place(x=750,y=750)

root.mainloop()