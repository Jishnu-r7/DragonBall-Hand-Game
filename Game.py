from tkinter import *
from tkinter import messagebox
from functools import partial
import random
from PIL import ImageTk,Image

#winning
def win():
    win=Tk()
    win.title("DRAGON BALLZ")
    win.geometry("1280x730+10+1")
    pla=Label(win,text="PLAYER",font=("Arial Black",50)).place(x=120,y=1)
    com=Label(win,text="COMPUTER",font=("Arial Black",50)).place(x=730,y=1)
    for i in range(0,100):
        line=Label(win,text="*").pack()
    global plwca
    global cowca
    plwca=Canvas(win,width=300,height=300)
    plwca.place(x=140,y=95)

    cowca=Canvas(win,width=300,height=300)
    cowca.place(x=800,y=95)

    photos()
    ent=Label(win,text="COMPUTER CHOSES:",font=("Aharoni",20)).place(x=750,y=400)
    cowshow=Label(win,text=comove,font=("Aharoni",20)).place(x=1010,y=400)
    plwshow=Label(win,text=plmove,font=("Aharoni",20)).place(x=210,y=400)
    plwpic()
    cowpic()
    
    messagebox.showinfo("You Won","CONGRATULATIONS.....YOU WON...YAYYYYY")


#losing
def lose():
    lose=Tk()
    lose.title("DRAGON BALLZ")
    lose.geometry("1280x730+10+1")
    pla=Label(lose,text="PLAYER",font=("Arial Black",50)).place(x=120,y=1)
    com=Label(lose,text="COMPUTER",font=("Arial Black",50)).place(x=730,y=1)
    
    for i in range(0,100):
        line=Label(lose,text="*").pack()
    global pllca
    global colca
    pllca=Canvas(lose,width=300,height=300)
    pllca.place(x=140,y=95)

    colca=Canvas(lose,width=300,height=300)
    colca.place(x=800,y=95)

    photos()
    ent=Label(lose,text="COMPUTER CHOSES:",font=("Aharoni",20)).place(x=750,y=400)
    cowshow=Label(lose,text=comove,font=("Aharoni",20)).place(x=1010,y=400)
    plwshow=Label(lose,text=plmove,font=("Aharoni",20)).place(x=210,y=400)
    pllpic()
    colpic()
    
    messagebox.showinfo("You Lose","Sorry....You Lost.....Better Luck Next Time")


#checking moves
def check():
    if plpow<0:
        if (plpow==copow) or (-plpow==copow):
            dra.destroy()
            game()
        elif -(plpow)<copow:
            dra.destroy()
            lose()
        elif -(plpow)>copow:
            dra.destroy()
            game()
    elif copow<0:
        if (plpow==copow) or (-copow==plpow):
            dra.destroy()
            game()
        elif -copow>plpow:
            dra.destroy()
            game()
        elif -copow<plpow:
            dra.destroy()
            win()
    elif(plpow>=0) and (copow>=0):
        if plpow>copow:
            dra.destroy()
            win()
        elif copow>plpow:
            dra.destroy()
            lose()
        elif plpow==copow:
            dra.destroy()
            game()


#moves
def charge(add):
    global plmove
    global plpow
    global plcha
    plmove="CHARGE"
    plpow=0
    comp()
    plcha+=1
    check()
def firef():
    global plmove
    global plcha
    global plpow
    plmove="FIREBALL(1)"
    plpow=1
    comp()
    plcha-=1
    check()
def thun():
    global plmove
    global plcha
    global plpow
    plmove="THUNDER PUNCH(2)"
    plpow=2
    comp()
    plcha-=2
    check()
def torn():
    global plmove
    global plcha
    global plpow
    plmove="TORNADO(3)"
    plpow=3
    comp()
    plcha-=3
    check()
def megpun():
    global plmove
    global plcha
    global plpow
    plmove="MEGA PUNCH(5)"
    plpow=5
    comp()
    plcha-=5
    check()
def slas():
    global plmove
    global plcha
    global plpow
    plmove="SLASH(6)"
    plpow=6
    comp()
    plcha-=6
    check()
def doubsl():
    global plmove
    global plcha
    global plpow
    plmove="DOUBLE SLASH(7)"
    plpow=7
    comp()
    plcha-=7
    check()
def kamih():
    global plmove
    global plcha
    global plpow
    plmove="KAMEHAMIHA(10)"
    plpow=10
    comp()
    plcha-=10
    check()
def spir():
    global plmove
    global plcha
    global plpow
    plmove="SPIRIT BOMB(12)"
    plpow=12
    comp()
    plcha-=12
    check()

def sh1():
    global plmove
    global plpow
    plmove="SHIELD(1)"
    plpow=-1
    comp()
    check()
def sh3():
    global plmove
    global plpow
    plmove="SHIELD(3)"
    plpow=-3
    comp()
    check()
def sh5():
    global plmove
    global plpow
    plmove="SHIELD(5)"
    plpow=-5
    comp()
    check()
def sh10():
    global plmove
    global plpow
    plmove="SHIELD(10)"
    plpow=-10
    comp()
    check()


#start
def game():
    global dra
    dra=Tk()
    dra.title("DRAGON BALLZ")
    dra.geometry("1280x730+10+1")

    global plca
    global coca
    plca=Canvas(dra,width=300,height=300)
    plca.place(x=140,y=95)

    coca=Canvas(dra,width=300,height=300)
    coca.place(x=800,y=95)
    photos()
    global mo
    mo=["SHIELD(1)","SHIELD(3)","SHIELD(5)","SHIELD(10)","CHARGE","FIREBALL(1)","THUNDER PUNCH(2)","TORNADO(3)","MEGA PUNCH(5)","SLASH(6)","DOUBLE SLASH(7)","KAMEHAMIHA(10)","SPIRIT BOMB(12)"]
    
    plpic()
    copic()
    
    for i in range(0,100):
        line=Label(dra,text="*").pack()

    pla=Label(dra,text="PLAYER",font=("Arial Black",50)).place(x=120,y=1)
    com=Label(dra,text="COMPUTER",font=("Arial Black",50)).place(x=730,y=1)

    shiel1=Button(dra,text="Shield(1)",command=sh1).place(x=10,y=350)
    sheil3=Button(dra,text="Shield(3)",command=sh3).place(x=10,y=400)
    sheil5=Button(dra,text="Shield(5)",command=sh5).place(x=10,y=450)
    sheil10=Button(dra,text="Shield(10)",command=sh10).place(x=10,y=500)

    char=Button(dra,text="Charge",font=(40),command=partial(charge,add)).place(x=200,y=450)
        
    lab=Label(dra,text=("YOUR CHARGE:%s"%plcha),font=("Aharoni",20)).place(x=160,y=500)
    
    if plcha<1:
        fire=Button(dra,text="Fireball(1)",state=DISABLED).place(x=500,y=350)
    else:
        fire=Button(dra,text="Fireball(1)",command=firef).place(x=500,y=350)
    if plcha<2:
        thpunch=Button(dra,text="Thunder punch(2)",state=DISABLED).place(x=500,y=400)
    else:
        thpunch=Button(dra,text="Thunder punch(2)",command=thun).place(x=500,y=400)
    if plcha<3:
        tor=Button(dra,text="Tornado(3)",state=DISABLED).place(x=500,y=450)
    else:
        tor=Button(dra,text="Tornado(3)",command=torn).place(x=500,y=450)
    if plcha<5:
        megapun=Button(dra,text="Mega punch(5)",state=DISABLED).place(x=500,y=500)
    else:
        megapun=Button(dra,text="Mega punch(5)",command=megpun).place(x=500,y=500)
    if plcha<6:
        slash=Button(dra,text="Slash(6)",state=DISABLED).place(x=500,y=550)
    else:
        slash=Button(dra,text="Slash(6)",command=slas).place(x=500,y=550)
    if plcha<7:
        doubslash=Button(dra,text="Double Slash(7)",state=DISABLED).place(x=500,y=600)
    else:
        doubslash=Button(dra,text="Double Slash(7)",command=doubsl).place(x=500,y=600)
    if plcha<10:
        kamehamiha=Button(dra,text="Kamehamiha(10)",state=DISABLED).place(x=500,y=650)
    else:
        kamehamiha=Button(dra,text="Kamehamiha(10)",command=kamih).place(x=500,y=650)
    if plcha<12:
        spiritbomb=Button(dra,text="Spirit Bomb(12)",state=DISABLED).place(x=500,y=700)
    else:
        spiritbomb=Button(dra,text="Spirit Bomb(12)",command=spir).place(x=500,y=700)
            
    ent=Label(dra,text="COMPUTER CHOSES:",font=("Aharoni",20)).place(x=650,y=400)
    coshow=Label(dra,text=comove,font=("Aharoni",20)).place(x=910,y=400)
    plshow=Label(dra,text=plmove,font=("Aharoni",20)).place(x=210,y=400)
    coch=Label(dra,text="COMPUTER CHARGE(S):",font=("Aharoni",20)).place(x=650,y=450)
    cochashow=Label(dra,text=cocha,font=("Aharoni",30)).place(x=950,y=440)
    dra.mainloop()

def plpic():
    global plca
    if plmove==mo[0]:
        plca.create_image(20, 20, anchor=NW, image=shield1pic)
    elif plmove==mo[1]:
        plca.create_image(20, 20, anchor=NW, image=shield3pic)
    elif plmove==mo[2]:
        plca.create_image(20, 20, anchor=NW, image=shield5pic)
    elif plmove==mo[3]:
        plca.create_image(20, 20, anchor=NW, image=shield10pic)
    elif plmove==mo[4]:
        plca.create_image(20, 20, anchor=NW, image=chargepic)
    elif plmove==mo[5]:
        plca.create_image(20, 20, anchor=NW, image=fireball)
    elif plmove==mo[6]:
        plca.create_image(20, 20, anchor=NW, image=thunderpun)
    elif plmove==mo[7]:
        plca.create_image(20, 20, anchor=NW, image=tornado)
    elif plmove==mo[8]:
        plca.create_image(20, 20, anchor=NW, image=megapunch)
    elif plmove==mo[9]:
        plca.create_image(20, 20, anchor=NW, image=slashpic)
    elif plmove==mo[10]:
        plca.create_image(20, 20, anchor=NW, image=doubleslashpic)
    elif plmove==mo[11]:
        plca.create_image(20, 20, anchor=NW, image=kamehamihapic)
    elif plmove==mo[12]:
        plca.create_image(20, 20, anchor=NW, image=spiritbombpic)

def plwpic():
    if plmove==mo[0]:
        plwca.create_image(20, 20, anchor=NW, image=shield1pic)
    elif plmove==mo[1]:
        plwca.create_image(20, 20, anchor=NW, image=shield3pic)
    elif plmove==mo[2]:
        plwca.create_image(20, 20, anchor=NW, image=shield5pic)
    elif plmove==mo[3]:
        plwca.create_image(20, 20, anchor=NW, image=shield10pic)
    elif plmove==mo[4]:
        plwca.create_image(20, 20, anchor=NW, image=chargepic)
    elif plmove==mo[5]:
        plwca.create_image(20, 20, anchor=NW, image=fireball)
    elif plmove==mo[6]:
        plwca.create_image(20, 20, anchor=NW, image=thunderpun)
    elif plmove==mo[7]:
        plwca.create_image(20, 20, anchor=NW, image=tornado)
    elif plmove==mo[8]:
        plwca.create_image(20, 20, anchor=NW, image=megapunch)
    elif plmove==mo[9]:
        plwca.create_image(20, 20, anchor=NW, image=slashpic)
    elif plmove==mo[10]:
        plwca.create_image(20, 20, anchor=NW, image=doubleslashpic)
    elif plmove==mo[11]:
        plwca.create_image(20, 20, anchor=NW, image=kamehamihapic)
    elif plmove==mo[12]:
        plwca.create_image(20, 20, anchor=NW, image=spiritbombpic)

def pllpic():
    if plmove==mo[0]:
        pllca.create_image(20, 20, anchor=NW, image=shield1pic)
    elif plmove==mo[1]:
        pllca.create_image(20, 20, anchor=NW, image=shield3pic)
    elif plmove==mo[2]:
        pllca.create_image(20, 20, anchor=NW, image=shield5pic)
    elif plmove==mo[3]:
        pllca.create_image(20, 20, anchor=NW, image=shield10pic)
    elif plmove==mo[4]:
        pllca.create_image(20, 20, anchor=NW, image=chargepic)
    elif plmove==mo[5]:
        pllca.create_image(20, 20, anchor=NW, image=fireball)
    elif plmove==mo[6]:
        pllca.create_image(20, 20, anchor=NW, image=thunderpun)
    elif plmove==mo[7]:
        pllca.create_image(20, 20, anchor=NW, image=tornado)
    elif plmove==mo[8]:
        pllca.create_image(20, 20, anchor=NW, image=megapunch)
    elif plmove==mo[9]:
        pllca.create_image(20, 20, anchor=NW, image=slashpic)
    elif plmove==mo[10]:
        pllca.create_image(20, 20, anchor=NW, image=doubleslashpic)
    elif plmove==mo[11]:
        pllca.create_image(20, 20, anchor=NW, image=kamehamihapic)
    elif plmove==mo[12]:
        pllca.create_image(20, 20, anchor=NW, image=spiritbombpic)
def copic():
    global coca
    if comove==mo[0]:
        coca.create_image(20, 20, anchor=NW, image=shield1pic)
    elif comove==mo[1]:
        coca.create_image(20, 20, anchor=NW, image=shield3pic)
    elif comove==mo[2]:
        coca.create_image(20, 20, anchor=NW, image=shield5pic)
    elif comove==mo[3]:
        coca.create_image(20, 20, anchor=NW, image=shield10pic)
    elif comove==mo[4]:
        coca.create_image(20, 20, anchor=NW, image=chargepic)
    elif comove==mo[5]:
        coca.create_image(20, 20, anchor=NW, image=fireball)
    elif comove==mo[6]:
        coca.create_image(20, 20, anchor=NW, image=thunderpun)
    elif comove==mo[7]:
        coca.create_image(20, 20, anchor=NW, image=tornado)
    elif comove==mo[8]:
        coca.create_image(20, 20, anchor=NW, image=megapunch)
    elif comove==mo[9]:
        coca.create_image(20, 20, anchor=NW, image=slashpic)
    elif comove==mo[10]:
        coca.create_image(20, 20, anchor=NW, image=doubleslashpic)
    elif comove==mo[11]:
        coca.create_image(20, 20, anchor=NW, image=kamehamihapic)
    elif comove==mo[12]:
        coca.create_image(20, 20, anchor=NW, image=spiritbombpic)

def cowpic():
    if comove==mo[0]:
        cowca.create_image(20, 20, anchor=NW, image=shield1pic)
    elif comove==mo[1]:
        cowca.create_image(20, 20, anchor=NW, image=shield3pic)
    elif comove==mo[2]:
        cowca.create_image(20, 20, anchor=NW, image=shield5pic)
    elif comove==mo[3]:
        cowca.create_image(20, 20, anchor=NW, image=shield10pic)
    elif comove==mo[4]:
        cowca.create_image(20, 20, anchor=NW, image=chargepic)
    elif comove==mo[5]:
        cowca.create_image(20, 20, anchor=NW, image=fireball)
    elif comove==mo[6]:
        cowca.create_image(20, 20, anchor=NW, image=thunderpun)
    elif comove==mo[7]:
        cowca.create_image(20, 20, anchor=NW, image=tornado)
    elif comove==mo[8]:
        cowca.create_image(20, 20, anchor=NW, image=megapunch)
    elif comove==mo[9]:
        cowca.create_image(20, 20, anchor=NW, image=slashpic)
    elif comove==mo[10]:
        cowca.create_image(20, 20, anchor=NW, image=doubleslashpic)
    elif comove==mo[11]:
        cowca.create_image(20, 20, anchor=NW, image=kamehamihapic)
    elif comove==mo[12]:
        cowca.create_image(20, 20, anchor=NW, image=spiritbombpic)

def colpic():
    if comove==mo[0]:
        colca.create_image(20, 20, anchor=NW, image=shield1pic)
    elif comove==mo[1]:
        colca.create_image(20, 20, anchor=NW, image=shield3pic)
    elif comove==mo[2]:
        colca.create_image(20, 20, anchor=NW, image=shield5pic)
    elif comove==mo[3]:
        colca.create_image(20, 20, anchor=NW, image=shield10pic)
    elif comove==mo[4]:
        colca.create_image(20, 20, anchor=NW, image=chargepic)
    elif comove==mo[5]:
        colca.create_image(20, 20, anchor=NW, image=fireball)
    elif comove==mo[6]:
        colca.create_image(20, 20, anchor=NW, image=thunderpun)
    elif comove==mo[7]:
        colca.create_image(20, 20, anchor=NW, image=tornado)
    elif comove==mo[8]:
        colca.create_image(20, 20, anchor=NW, image=megapunch)
    elif comove==mo[9]:
        colca.create_image(20, 20, anchor=NW, image=slashpic)
    elif comove==mo[10]:
        colca.create_image(20, 20, anchor=NW, image=doubleslashpic)
    elif comove==mo[11]:
        colca.create_image(20, 20, anchor=NW, image=kamehamihapic)
    elif comove==mo[12]:
        colca.create_image(20, 20, anchor=NW, image=spiritbombpic)

def comp():
    global cocha
    if cocha==0 and plcha<=1:
        co=["CHARGE"]
    elif plcha<=1:
        co=["CHARGE","SHIELD(1)"]
    elif plcha<=3:
        co=["CHARGE","SHIELD(3)"]
    elif plcha<=5:
        co=["CHARGE","SHIELD(5)"]
    elif plcha <=12:
        co=["CHARGE","SHIELD(10)"]
    if cocha>=12:
        co.extend(["SPIRIT BOMB(12)"])
    elif cocha>=10:
        co.extend(["FIREBALL(1)","THUNDER PUNCH(2)","SLASH(6)","DOUBLE SLASH(7)","KAMEHAMIHA(10)"])
    elif cocha>7:
        co.extend(["FIREBALL(1)","THUNDER PUNCH(2)","TORNADO(3)","SLASH(6)","DOUBLE SLASH(7)"])
    elif cocha>=6:
        co.extend(["FIREBALL(1)","THUNDER PUNCH(2)","MEGA PUNCH(5)","SLASH(6)"])
    elif cocha>=5:
        co.extend(["FIREBALL(1)","THUNDER PUNCH(2)","MEGA PUNCH(5)"])
    elif cocha>=3:
        co.extend(["FIREBALL(1)","THUNDER PUNCH(2)","TORNADO(3)"])
    elif cocha>=2:
        co.extend(["FIREBALL(1)","THUNDER PUNCH(2)"])
    elif cocha>=1:
        co.append("FIREBALL(1)")
    step=random.randint(0,len(co)-1)
    global comove
    comove=co[step]
    global copow
    if comove=="SHIELD(1)":
        copow=-1
    elif comove=="SHIELD(3)":
        copow=-3
    elif comove=="SHIELD(5)":
        copow=-5
    elif comove=="SHIELD(10)":
        copow=-10
    elif comove=="CHARGE":
        cocha+=1
        copow=0
        copho=Label(dra,image=chargepic)
        copho.place(x=540,y=80)
    elif comove=="FIREBALL(1)":
        copow=1
        cocha-=1
    elif comove=="THUNDER PUNCH(2)":
        copow=2
        cocha-=2
    elif comove=="TORNADO(3)":
        copow=3
        cocha-=3
    elif comove=="MEGA PUNCH(5)":
        copow=5
        cocha-=5
    elif comove=="SLASH(6)":
        copow=6
        cocha-=6
    elif comove=="DOUBLE SLASH(7)":
        copow=7
        cocha-=7
    elif comove=="KAMEHAMIHA(10)":
        copow=10
        cocha-=10
    elif comove=="SPIRIT BOMB(12)":
        copow=12
        cocha-=12
def photos():
    global fireball
    global thunderpun
    global tornado
    global megapunch
    global slashpic
    global doubleslashpic
    global kamehamihapic
    global spiritbombpic
    global shield1pic
    global shield3pic
    global shield5pic
    global shield10pic
    global chargepic
    fireball=ImageTk.PhotoImage(Image.open("fireball.jpg"))
    thunderpun=ImageTk.PhotoImage(Image.open("thunderpunch.jpg"))
    tornado=ImageTk.PhotoImage(Image.open("tornado.jpg"))
    megapunch=ImageTk.PhotoImage(Image.open("megapunch.jpg"))
    slashpic=ImageTk.PhotoImage(Image.open("slash.png"))
    doubleslashpic=ImageTk.PhotoImage(Image.open("images.png"))
    kamehamihapic=ImageTk.PhotoImage(Image.open("kamehamiha.jpg"))
    spiritbombpic=ImageTk.PhotoImage(Image.open("spiritbomb.jpg"))
    shield1pic=ImageTk.PhotoImage(Image.open("shield1.jpg"))
    shield3pic=ImageTk.PhotoImage(Image.open("shield3.jpg"))
    shield5pic=ImageTk.PhotoImage(Image.open("shield5.jpg"))
    shield10pic=ImageTk.PhotoImage(Image.open("shield10.jpg"))
    chargepic=ImageTk.PhotoImage(Image.open("charge.png"))



cocha=0
plcha=0
add=1
comove=""
plmove=""

game()


