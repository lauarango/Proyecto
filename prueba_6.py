from  tkinter import *
import time

m= Tk ()
canvas = Canvas (m, width= "500", height= "500", bg= "black")
canvas.focus_set()
canvas.pack()
##f=tkinter.PhotoImage(file='cjndsk.gif')
##h=canvas.create_image(3,6,image=f)dddd
mario= canvas.create_polygon (82, 406, 82, 436, 112, 436, 112,406, fill ="orangered")
sc=canvas.create_polygon(332,34,332,59,358,59,358,34,fill="peachpuff")
#sidestepper=canvas.create_polygon()
#slipice=canvas.create_polygon()
#figtherfly=canvas.create.polygon()

"""Interfaz grafica"""
def tubos():
    #tubo izquierdo abajo
    cuadrado = canvas.create_polygon(0,369,0,430,80,430,80,369,fill="green")
    cuadrado = canvas.create_polygon(0,410,0,428,80,428,80,410,fill="darkgreen")
    cuadrado = canvas.create_polygon(0,375,0,383,80,383,80,375,fill="white")
    cuadrado = canvas.create_polygon(65,365,65,435,80,435,80,365,fill="limegreen")
    cuadrado = canvas.create_polygon(65,405,65,423,80,423,80,405,fill="darkgreen")
    cuadrado = canvas.create_polygon(65,371,65,379,80,379,80,371,fill="white")
    #tubo derecho abajo
    cuadrado = canvas.create_polygon(420,369,420,430,500,430,500,369,fill="green")
    cuadrado = canvas.create_polygon(420,410,420,428,500,428,500,410,fill="darkgreen")
    cuadrado = canvas.create_polygon(420,375,420,383,500,383,500,375,fill="white")
    cuadrado = canvas.create_polygon(420,365,420,435,435,435,435,365,fill="limegreen")
    cuadrado = canvas.create_polygon(420,405,420,423,435,423,435,405,fill="darkgreen")
    cuadrado = canvas.create_polygon(420,371,420,379,435,379,435,371,fill="white")
    
    #tubo izquierdo arriba
    #estructura inicial
    cuadrado = canvas.create_polygon(0,76,0,137,80,137,80,76,fill="green")
    cuadrado = canvas.create_polygon(55,46,55,137,110,137,110,46,fill="green")
    cuadrado = canvas.create_polygon(55,16,55,77,140,77,140,16,fill="green")

    #sombra de la estructura inicial
    
    cuadrado = canvas.create_polygon(0,117,0,135,91,135,91,117,fill="darkgreen")
    cuadrado = canvas.create_polygon(83,65,83,135,101,135,101,65,fill="darkgreen")
    cuadrado = canvas.create_polygon(83,60,83,75,140,75,140,60,fill="darkgreen")

    #iluminacion
    cuadrado = canvas.create_polygon(0,85,0,95,73,95,73,85,fill="white")
    cuadrado = canvas.create_polygon(63,33,63,95,73,95,73,33,fill="white")
    cuadrado = canvas.create_polygon(63,28,63,38,140,38,140,28,fill="white")

    #correas de la tuberia
    cuadrado = canvas.create_polygon(125,12,125,81,140,81,140,12,fill="limegreen")
    cuadrado = canvas.create_polygon(35,74,35,139,50,139,50,74,fill="limegreen")
    
    #sombras de las correas
    cuadrado = canvas.create_polygon(35,111,35,130,50,130,50,111,fill="darkgreen")
    cuadrado = canvas.create_polygon(125,56,125,71,140,71,140,56,fill="darkgreen")

    #tubo derecho arriba
    #estructura inicial
    cuadrado = canvas.create_polygon(500,76,500,137,420,137,420,76,fill="green")
    cuadrado = canvas.create_polygon(445,137,445,46,390,46,390,137,fill="green")
    cuadrado = canvas.create_polygon(445,16,445,77,360,77,360,16,fill="green")

    #sombra de la estructura inicial
    
    cuadrado = canvas.create_polygon(500,117,500,135,409,135,409,117,fill="darkgreen")
    cuadrado = canvas.create_polygon(417,65,417,135,399,135,399,65,fill="darkgreen")
    cuadrado = canvas.create_polygon(417,60,417,75,360,75,360,60,fill="darkgreen")

    #iluminacion
    cuadrado = canvas.create_polygon(500,85,500,95,427,95,427,85,fill="white")
    cuadrado = canvas.create_polygon(437,33,437,95,427,95,427,33,fill="white")
    cuadrado = canvas.create_polygon(437,28,437,38,360,38,360,28,fill="white")
    
    #correas de la tuberia
    cuadrado = canvas.create_polygon(375,12,375,81,360,81,360,12,fill="limegreen")
    cuadrado = canvas.create_polygon(465,74,465,139,450,139,450,74,fill="limegreen")
    
    #sombras de las correas
    cuadrado = canvas.create_polygon(465,111,465,130,450,130,450,111,fill="darkgreen")
    cuadrado = canvas.create_polygon(375,56,375,71,360,71,360,56,fill="darkgreen")

###piso
##cuadrado1=canvas.create_polygon(0, 436, 0, 500, 500, 500, 500, 436, fill="firebrick")
##
##def bloques():
##    #bloques1
##    cuadrado2=canvas.create_polygon(0,340,0,360,180,360,180,340,fill="cyan")
##    cuadrado3=canvas.create_polygon(500,340,500,360,320,360,320,340,fill="cyan")
##    #bloques2
##    cuadrado4=canvas.create_polygon(0,250,0,270,60,270,60,250,fill="cyan")
##    cuadrado5=canvas.create_polygon(130,240,130,260,370,260,370,240,fill="cyan")
##    cuadrado6=canvas.create_polygon(440,250,440,270,500,270,500,250,fill="cyan")
##    #bloques3
##    cuadrado7=canvas.create_polygon(0,140,0,160,194,160,194,140,fill="cyan")
##    cuadrado8=canvas.create_polygon(306,140,306,160,500,160,500,140,fill="cyan")
    
#piso
##cuadrado1=canvas.create_polygon(0, 436, 0, 500, 99, 500, 99, 436, fill="firebrick")
##cuadrado11=canvas.create_polygon(102, 436, 102, 500, 199, 500, 199, 436, fill="brown")
##cuadrado1=canvas.create_polygon(202, 436, 202, 500, 299, 500, 299, 436, fill="firebrick")
##cuadrado11=canvas.create_polygon(302, 436, 302, 500, 399, 500, 399, 436, fill="brown")
##cuadrado1=canvas.create_polygon(402, 436, 402, 500, 500, 500, 500, 436, fill="firebrick")
cuadrado1=canvas.create_polygon(0, 436, 0, 500, 500, 500, 500, 436, fill="firebrick")


def bloques():
    #bloques1
    cuadrado2=canvas.create_polygon(0,340,0,360,89,360,89,340,fill="Aquamarine")
    cuadrado22=canvas.create_polygon(92,340,92,360,180,360,180,340,fill='cyan')
    cuadrado3=canvas.create_polygon(500,340,500,360,411,360,411,340,fill="cyan")
    cuadrado33=canvas.create_polygon(408,340,408,360,320,360,320,340,fill="Aquamarine")
    #bloques2
    cuadrado4=canvas.create_polygon(0,250,0,270,29,270,29,250,fill="cyan")
    cuadrado44=canvas.create_polygon(32,250,32,270,60,270,60,250,fill="Aquamarine")
    cuadrado5=canvas.create_polygon(130,240,130,260,249,260,249,240,fill="cyan")
    cuadrado55=canvas.create_polygon(252,240,252,260,370,260,370,240,fill="Aquamarine")
    cuadrado6=canvas.create_polygon(440,250,440,270,469,270,469,250,fill="cyan")
    cuadrado66=canvas.create_polygon(472,250,472,270,500,270,500,250,fill="Aquamarine")
    #bloques3
    cuadrado7=canvas.create_polygon(0,140,0,160,96,160,96,140,fill="Aquamarine")
    cuadrado77=canvas.create_polygon(99,140,99,160,194,160,194,140,fill="cyan")
    cuadrado8=canvas.create_polygon(306,140,306,160,402,160,402,140,fill="Aquamarine")
    cuadrado88=canvas.create_polygon(405,140,405,160,500,160,500,140,fill="cyan")
    
#Graficas
bloques()
tubos()


#x=canvas.find_overlapping(x1, y1, x2, y2)
"""Estados de los enemigos """
sc_Estado=False  #No volteada tortuga1
sc_morir=False #Tortuga1 no esta muerta
sc_creada=True #Tortuga1 creada
sc2_Estado=False #No volteada tortuga2
sc2_morir=False #Tortuga2 no esta muerta
sc2_creada=False #Tortuga2 no creada
mario_Estado=False #Mario vivo
sc3_Estado=False #No volteada tortuga3
sc3_morir=False #Tortuga3 no esta muerta
sc3_creada=False  #Tortuga3 no creada
ff_Estado=False #No volteada ff
ff_morir=False #ff no esta muerta
ff_creada=False #ff no creada
ff_salto=True #ff esta en el piso



def Unflipped():
    global sc_Estado, sc, sc_morir, sc2_Estado, sc2, sc2_morir
    if sc_Estado==True and sc_morir==False:
        canvas.itemconfig(sc,fill='peachpuff')
        sc_Estado=False
    elif sc2_Estado==True and sc2_morir==False:
        canvas.itemconfig(sc2,fill='peachpuff')
        sc2_Estado=False

def Morir():
    global mario_Estado, mario, sal
    if mario_Estado==True and canvas.coords(mario)[3]<=536:
        canvas.move(mario,0,10)
        canvas.update()
        m.after(1,Morir)
    m.after(4000,InvocarMario)



def Matar():
    global sc, sc_Estado,sc_morir,sc2, sc2_Estado,sc2_morir, sc_creada, sc2_creada
    if sc_Estado==True and sc_morir==True and sc_creada==True:
        canvas.delete(sc)
        sc_creada=False
        m.after(3000,invocarTortuga)
    if sc2_Estado==True and sc2_morir==True and sc2_creada==True:
        sc2_creada=False
        canvas.delete(sc2)
        m.after(3000,invocarTortuga)
        
def invocarTortuga():
    global sc, sc_Estado,sc_morir,sc2, sc2_Estado,sc2_morir, sc_creada, sc2_creada
    if sc_morir==True and sc_creada==False:
        sc_morir=False
        sc_Estado=False
        sc=canvas.create_polygon(332,34,332,59,358,59,358,34,fill="peachpuff")
        sc_creada=True
    if sc2_creada==False:
        sc2_morir=False
        sc2_Estado=False
        sc2=canvas.create_polygon(332,34,332,59,358,59,358,34,fill="peachpuff")
        sc2_creada=True

def invocarTortuga2():
   global sc3_Estado,sc3_morir,sc3, sc3_creada
   if sc3_creada==False:
        sc3_morir=False
        sc3_Estado=False
        sc3=canvas.create_polygon(142,34,142,59,167,59,167,34,fill="peachpuff")
        sc3_creada=True


def InvocarMario():
    global mario, mario_Estado
    if mario_Estado==True:
        mario= canvas.create_polygon (82, 406, 82, 436, 112, 436, 112,406, fill ="orangered")
        mario_Estado=False

def Text():
    vidas=Label(m,text="HOLA MUNDO",fg="white",font=("Arial",30))
    vidas.pack(padx=250,pady=10)




"""Movimiento de los enemigos"""
def shellcreeper():
    global sc, sc_Estado, sc_morir, mario, mario_Estado
    if sc_Estado==False and sc_morir==False:
        bb=canvas.find_overlapping(canvas.coords(sc)[0],canvas.coords(sc)[1],canvas.coords(sc)[4],canvas.coords(sc)[5])
        if mario_Estado==False and sc_Estado==False:
            #1mer piso
            if ((canvas.coords(mario)[3]<=440 and canvas.coords(mario)[1]>340) and (canvas.coords(sc)[3]<=440 and canvas.coords(sc)[1]>340)) and ((canvas.coords(mario)[4]==canvas.coords(sc)[2]) or (canvas.coords(mario)[2]<=(canvas.coords(sc)[4]-1))) and len(bb)>1:
                mario_Estado=True
                m.after(1,Morir)
        #2do piso tuberias
            elif ((canvas.coords(mario)[3]<=340 and canvas.coords(mario)[1]>240) and (canvas.coords(sc)[3]<=340 and canvas.coords(sc)[1]>240)) and ((canvas.coords(mario)[4]==canvas.coords(sc)[2]) or (canvas.coords(mario)[2]<=(canvas.coords(sc)[4]-1))) and  len(bb)>1:
                mario_Estado=True
                m.after(1,Morir)
        #4to piso
            elif ((canvas.coords(mario)[3]<=240 and canvas.coords(mario)[1]>140) and (canvas.coords(sc)[3]<=240 and canvas.coords(sc)[1]>140)) and ((canvas.coords(mario)[4]==canvas.coords(sc)[2]) or (canvas.coords(mario)[2]<=(canvas.coords(sc)[4]-1))) and len(bb)>1:
                mario_Estado=True
                m.after(1,Morir)
        #5to piso
            elif canvas.coords(mario)[3]<=140 and canvas.coords(sc)[3]<=140 and ((canvas.coords(mario)[4]==canvas.coords(sc)[2]) or (canvas.coords(mario)[2]<=(canvas.coords(sc)[4]-1))) and len(bb)>1:
                mario_Estado=True
                m.after(1,Morir)

        #caidas
        if sc_Estado==False and canvas.coords(sc)[3]<136 or ((canvas.coords(sc)[4]<306 and canvas.coords(sc)[2]>194) and canvas.coords(sc)[3]<236) or ((canvas.coords(sc)[2]>60 and canvas.coords(sc)[4]<130) and canvas.coords(sc)[3]<336) or ((canvas.coords(sc)[4]<320 and canvas.coords(sc)[2]>180)and canvas.coords(sc)[3]<434 and canvas.coords(sc)[3]>=336):
                canvas.move(sc,0,5)
                canvas.update()
                m.after(40,shellcreeper)
                return None
        
        #avanzar
        if sc_Estado==False and sc_morir==False:
            canvas.move(sc,-5,0)
        #pantalla continua
        if sc_Estado==False and sc_morir==False and canvas.coords(sc)[0]<0:
            canvas.move(sc, 500,0)
        #Meterse en las tuberias
        if sc_Estado==False and sc_morir==False and canvas.coords(sc)[2]<=80 and canvas.coords(sc)[3]>360:
            canvas.delete(sc)
            sc=canvas.create_polygon(332,34,332,59,358,59,358,34,fill="peachpuff")
    m.after(100,shellcreeper) #Recursion

#(((((canvas.coords(mario)[1])-(canvas.coords(sc2)[5]))**2)<=1) or ((((canvas.coords(mario)[5])-(canvas.coords(sc2)[1]))**2)<=1))
    #and (canvas.coords(sc2)[0]<=440 and canvas.coords(sc2)[1]>340)) and ((((canvas.coords(mario)[6])-(canvas.coords(sc2)[0]))<=(-5)) or (((canvas.coords(mario)[0])-(canvas.coords(sc2)[6]))<=(-5)) or (((canvas.coords(mario)[1])-(canvas.coords(sc2)[5]))<=(-5)) or (((canvas.coords(mario)[5])-(canvas.coords(sc2)[1]))<=(-5)))
#(canvas.coords(mario)[4]==canvas.coords(sc2)[2])
#(canvas.coords(mario)[2]==(canvas.coords(sc2)[4]-1))

def shellcreeper2():
    global sc2_Estado, sc2_morir, sc2_creada, sc2,mario, mario_Estado
    if sc2_creada==False:
        m.after(3000,invocarTortuga)
        m.after(100, shellcreeper2)
    elif sc2_creada==True:
        b=canvas.find_overlapping(canvas.coords(sc2)[0],canvas.coords(sc2)[1],canvas.coords(sc2)[4],canvas.coords(sc2)[5])
        if mario_Estado==False and sc2_Estado==False:
            #1mer piso
            if ((canvas.coords(mario)[3]<=440 and canvas.coords(mario)[1]>340) and (canvas.coords(sc2)[3]<=440 and canvas.coords(sc2)[1]>340)) and ((canvas.coords(mario)[4]==canvas.coords(sc2)[2]) or (canvas.coords(mario)[2]<=(canvas.coords(sc2)[4]-1))) and len(b)>1:
                mario_Estado=True
                m.after(1,Morir)
            #2do piso sin tuberias
            elif ((canvas.coords(mario)[3]<=340 and canvas.coords(mario)[1]>240) and (canvas.coords(sc2)[3]<=340 and canvas.coords(sc2)[1]>240)) and ((canvas.coords(mario)[4]==canvas.coords(sc2)[2]) or (canvas.coords(mario)[2]<=(canvas.coords(sc2)[4]-1))) and  len(b)>1:
                print(sc2_Estado)
                print(sc2_morir)
                mario_Estado=True
                m.after(1,Morir)
            #4to piso
            elif ((canvas.coords(mario)[3]<=240 and canvas.coords(mario)[1]>140) and (canvas.coords(sc2)[3]<=240 and canvas.coords(sc2)[1]>140)) and ((canvas.coords(mario)[4]==canvas.coords(sc2)[2]) or (canvas.coords(mario)[2]<=(canvas.coords(sc2)[4]-1))) and len(b)>1:
                mario_Estado=True
                m.after(1,Morir)
            #5to piso
            elif canvas.coords(mario)[3]<=140 and canvas.coords(sc2)[3]<=140 and ((canvas.coords(mario)[4]==canvas.coords(sc2)[2]) or (canvas.coords(mario)[2]<=(canvas.coords(sc2)[4]-1))) and len(b)>1:
                mario_Estado=True
                m.after(1,Morir)
                
        
        #caidas
        if sc2_Estado==False and canvas.coords(sc2)[3]<136 or ((canvas.coords(sc2)[4]<306 and canvas.coords(sc2)[2]>194) and canvas.coords(sc2)[3]<236) or ((canvas.coords(sc2)[2]>60 and canvas.coords(sc2)[4]<130) and canvas.coords(sc2)[3]<336) or ((canvas.coords(sc2)[4]<320 and canvas.coords(sc2)[2]>180)and canvas.coords(sc2)[3]<434 and canvas.coords(sc2)[3]>=336):
            
            canvas.move(sc2,0,5)
            canvas.update()
            m.after(40,shellcreeper2)
            return None
        
        #avanzar
        if sc2_Estado==False and sc2_morir==False:
            canvas.move(sc2,-3,0)
        #pantalla continua
        if sc2_Estado==False and sc2_morir==False and canvas.coords(sc2)[0]<0:
            canvas.move(sc2, 500,0)
        #Meterse en las tuberias
        if sc2_Estado==False and sc2_morir==False and canvas.coords(sc2)[2]<=80 and canvas.coords(sc2)[3]>360:
            canvas.delete(sc2)
            sc2=canvas.create_polygon(332,34,332,59,358,59,358,34,fill="peachpuff")
        m.after(100,shellcreeper2) #Recursion
        


def shellcreeper3():
    
    global sc3_Estado, sc3_morir, sc3_creada, sc3,mario, mario_Estado
    
    if sc3_creada==False:
        m.after(3000,invocarTortuga2)
        m.after(100, shellcreeper3)
    elif sc3_creada==True:
        d=canvas.find_overlapping(canvas.coords(sc3)[0],canvas.coords(sc3)[1],canvas.coords(sc3)[4],canvas.coords(sc3)[5])
        if mario_Estado==False and sc3_Estado==False:
            #1mer piso
            if ((canvas.coords(mario)[3]<=440 and canvas.coords(mario)[1]>340) and (canvas.coords(sc3)[3]<=440 and canvas.coords(sc3)[1]>340)) and ((canvas.coords(mario)[4]==canvas.coords(sc3)[2]) or (canvas.coords(mario)[2]==(canvas.coords(sc3)[4]-1)) or (canvas.coords(mario)[2]==(canvas.coords(sc3)[4]-6)) or (canvas.coords(mario)[2]==(canvas.coords(sc3)[4]-10)) or (canvas.coords(mario)[2]==(canvas.coords(sc3)[4]-4))) and len(d)>1:
                mario_Estado=True
                m.after(1,Morir)
            #2do piso
            elif ((canvas.coords(mario)[3]<=340 and canvas.coords(mario)[1]>240) and (canvas.coords(sc3)[3]<=340 and canvas.coords(sc3)[1]>240)) and ((canvas.coords(mario)[4]==canvas.coords(sc3)[2]) or (canvas.coords(mario)[2]==(canvas.coords(sc3)[4]-1)) or (canvas.coords(mario)[2]==(canvas.coords(sc3)[4]-6)) or (canvas.coords(mario)[2]==(canvas.coords(sc3)[4]-10)) or (canvas.coords(mario)[2]==(canvas.coords(sc3)[4]-4))) and  len(d)>1:
                mario_Estado=True
                m.after(1,Morir)
            #4to piso
            elif ((canvas.coords(mario)[3]<=240 and canvas.coords(mario)[1]>140) and (canvas.coords(sc3)[3]<=240 and canvas.coords(sc3)[1]>140)) and ((canvas.coords(mario)[4]==canvas.coords(sc3)[2]) or (canvas.coords(mario)[2]==(canvas.coords(sc3)[4]-1)) or (canvas.coords(mario)[2]==(canvas.coords(sc3)[4]-6)) or (canvas.coords(mario)[2]==(canvas.coords(sc3)[4]-10)) or (canvas.coords(mario)[2]==(canvas.coords(sc3)[4]-4))) and len(d)>1:
                mario_Estado=True
                m.after(1,Morir)
            #5to piso
            elif canvas.coords(mario)[3]<=140 and canvas.coords(sc3)[3]<=140 and ((canvas.coords(mario)[4]==canvas.coords(sc3)[2]) or (canvas.coords(mario)[2]==(canvas.coords(sc3)[4]-1)) or (canvas.coords(mario)[2]==(canvas.coords(sc3)[4]-6)) or (canvas.coords(mario)[2]==(canvas.coords(sc3)[4]-10)) or (canvas.coords(mario)[2]==(canvas.coords(sc3)[4]-4))) and len(d)>1:
                mario_Estado=True
                m.after(1,Morir)
        
        #caidas
        if sc3_Estado==False and canvas.coords(sc3)[3]<136 or ((canvas.coords(sc3)[4]<306 and canvas.coords(sc3)[2]>194) and canvas.coords(sc3)[3]<236) or ((canvas.coords(sc3)[2]>370 and canvas.coords(sc3)[4]<440) and canvas.coords(sc3)[3]<336) or ((canvas.coords(sc3)[4]<320 and canvas.coords(sc3)[2]>180)and canvas.coords(sc3)[3]<434 and canvas.coords(sc3)[3]>=336):
            
            canvas.move(sc3,0,5)
            canvas.update()
            m.after(40,shellcreeper3)
            return None
        
        #avanzar
        if sc3_Estado==False and sc3_morir==False:
            canvas.move(sc3,7,0)
        #pantalla continua
        if sc3_Estado==False and sc3_morir==False and canvas.coords(sc3)[0]>500:
            canvas.move(sc3,-500,0)
        #Meterse en las tuberias
        if sc3_Estado==False and sc3_morir==False and canvas.coords(sc3)[2]>420 and canvas.coords(sc3)[3]>360:
            canvas.delete(sc3)
            sc3=canvas.create_polygon(142,34,142,59,167,59,167,34,fill="peachpuff")
        m.after(100,shellcreeper3) #Recursion


def fighterfly():
    global ff,ff_salto
        
    ff=canvas.create_polygon(142,34,142,59,167,59,167,34,fill="peachpuff")
    if canvas.coords(ff)[3]<=139 and canvas.coords(ff)[1]>90 and ff_salto==True:
        canvas.move(ff,1,-3)
        m.after(10,fighterfly)
    elif canvas.coords(ff)[3]<239 and canvas.coords(ff)[1]>190 and ff_salto==True: 
        canvas.move(ff,1,-3)
        m.after(10,fighterfly)
    elif canvas.coords(ff)[3]<339 and canvas.coords(ff)[1]>290 and ff_salto==True: 
        canvas.move(ff,1,-3)
        m.after(10,fighterfly)
    elif canvas.coords(ff)[3]<439 and canvas.coords(ff)[1]>390 and ff_salto==True: 
        canvas.move(ff,1,-3)
        m.after(10,fighterfly)

        
    ff_salto=False
    
    if canvas.coords(ff)[3]<139 and canvas.coords(ff)[1]>90:
        canvas.move(ff,1,3)
        ff_salto=True
        m.after(10,fighterfly)
    elif canvas.coords(ff)[3]<239 and canvas.coords(ff)[1]>190: 
        canvas.move(ff,1,3)
        ff_salto=True
        m.after(10,fighterfly)
    elif canvas.coords(ff)[3]<339 and canvas.coords(ff)[1]>290: 
        canvas.move(ff,1,3)
        ff_salto=True
        m.after(10,fighterfly)
    elif canvas.coords(ff)[3]<439 and canvas.coords(ff)[1]>390: 
        canvas.move(ff,1,3)
        ff_salto=True
        m.after(10,fighterfly)
        

    if canvas.coords(ff)[2]>=180 and canvas.coords(ff)[4]<=320 and canvas.coords(ff)[3]<439 and canvas.coords(ff)[1]>266:
        canvas.move(ff,0,3)
        canvas.update()
        m.after(10,fighterfly)
    #caer desde el 3er piso
    elif canvas.coords(ff)[2]>=370 and canvas.coords(ff)[4]<=440 and canvas.coords(ff)[3]<339 and canvas.coords(ff)[1]>166:
        canvas.move(ff,0,3)
        canvas.update()
        m.after(10,fighterfly)
    #caer desde el 4to piso
    elif canvas.coords(ff)[2]>=194 and canvas.coords(ff)[4]<=306 and canvas.coords(ff)[3]<239 and canvas.coords(ff)[1]>66:
        canvas.move(ff,0,3)
        canvas.update()
        m.after(10,fighterfly)
    elif canvas.coords(ff)[1]>=34 and canvas.coords(ff)[3]<139:
        canvas.move(ff,0,3)
        canvas.update()
        m.after(10,fighterfly)
#fighterfly()

"""Variables para movimiento de mario"""
sal=False
state=[0,0,0]
y=canvas.coords(mario)[1]-120

"""saltos"""
def salto():
    global sal, y, sc, sc_Estado, sc2, sc2_Estado, mario_Estado
    if mario_Estado==False:
        #1mer piso
        if sal==True and canvas.coords(mario)[1] >= y and ((canvas.coords(mario)[1]>366) or (canvas.coords(mario)[0]>180 and canvas.coords(mario)[6]<320)) and canvas.coords(mario)[1]>266:
            #Evalua si voltea algo
            #2do piso
            if sc_Estado==False and sc_morir==False:
                x=canvas.find_overlapping(canvas.coords(sc)[0]+3, canvas.coords(sc)[1]+49, canvas.coords(sc)[4]+3, canvas.coords(sc)[5]+33)
                if ((canvas.coords(sc)[0] >= 83 and canvas.coords(sc)[0] < 180 and canvas.coords(mario)[0]<180) or (canvas.coords(sc)[6]<=417 and canvas.coords(sc)[6]>320 and canvas.coords(mario)[6]>320)) and canvas.coords(mario)[1]>366 and  sc_Estado==False and sc_morir==False and len(x) >=1 and canvas.coords(sc)[3]==339:
                    sc_Estado=True
                    canvas.itemconfig(sc,fill='yellow')
                    m.after(5000,Unflipped)
            if sc2_Estado==False and sc2_morir==False and sc2_creada==True:
                xsc2=canvas.find_overlapping(canvas.coords(sc2)[0]+3, canvas.coords(sc2)[1]+49, canvas.coords(sc2)[4]+3, canvas.coords(sc2)[5]+33)
                if ((canvas.coords(sc2)[0] >= 83 and canvas.coords(sc2)[0] < 180 and canvas.coords(mario)[0]<180) or (canvas.coords(sc2)[6]<=417 and canvas.coords(sc2)[6]>320 and canvas.coords(mario)[6]>320)) and canvas.coords(mario)[1]>366 and  sc2_Estado==False and sc2_morir==False and len(xsc2) >=1 and canvas.coords(sc2)[3]==339:
                    sc2_Estado=True
                    canvas.itemconfig(sc2,fill='yellow')
                    m.after(5000,Unflipped)
            canvas.move(mario,0,-5)
            canvas.update()
            m.after(10,salto())
        #2do piso medio
        elif sal==True and canvas.coords(mario)[1] >= y and canvas.coords(mario)[3] <=336 and canvas.coords(mario)[1]>166 and (canvas.coords(mario)[0]>60 and canvas.coords(mario)[6]<440)and((canvas.coords(mario)[1]>266) or ((canvas.coords(mario)[0]>60 and canvas.coords(mario)[6]<130)or(canvas.coords(mario)[0]>370 and canvas.coords(mario)[6]<440))):
            #Evalua si voltea algo
            #3er piso
            if sc_Estado==False and sc_morir==False:
                x=canvas.find_overlapping(canvas.coords(sc)[0]+3, canvas.coords(sc)[1]+49, canvas.coords(sc)[4]+3, canvas.coords(sc)[5]+33)
                if len(x)>=1 and sc_Estado==False and sc_morir==False and canvas.coords(sc)[6]>=130 and canvas.coords(sc)[6]<=370 and canvas.coords(mario)[3]<=336 and canvas.coords(mario)[1]>=266 and canvas.coords(sc)[3]==239:
                    sc_Estado=True
                    canvas.itemconfig(sc,fill='yellow')
                    m.after(5000,Unflipped)
            if sc2_Estado==False and sc2_morir==False and sc2_creada==True:
                xsc2=canvas.find_overlapping(canvas.coords(sc2)[0]+3, canvas.coords(sc2)[1]+49, canvas.coords(sc2)[4]+3, canvas.coords(sc2)[5]+33)
                if len(xsc2)>=1 and sc2_Estado==False and sc2_morir==False and canvas.coords(sc2)[6]>=130 and canvas.coords(sc2)[6]<=370 and canvas.coords(mario)[3]<=336 and canvas.coords(mario)[1]>=266 and canvas.coords(sc2)[3]==239:
                    sc2_Estado=True
                    canvas.itemconfig(sc2,fill='yellow')
                    m.after(5000,Unflipped)
            canvas.move(mario,0,-5)
            canvas.update()
            m.after(10,salto())
        #2do piso lados
        elif sal==True and canvas.coords(mario)[1]>=y and canvas.coords(mario)[3] <=336 and canvas.coords(mario)[1]>276 and (canvas.coords(mario)[0]<60 or canvas.coords(mario)[6]>440):
            canvas.move(mario,0,-5)
            canvas.update()
            m.after(10,salto())
        #3er piso
        elif sal==True and canvas.coords(mario)[1]>=y and canvas.coords(mario)[3]<=266 and ((canvas.coords(mario)[1]>166)or(canvas.coords(mario)[0]>194 and canvas.coords(mario)[6]<306)):
            #Evalua si voltea algo
            #4to piso
            if sc_Estado==False and sc_morir==False:
                x=canvas.find_overlapping(canvas.coords(sc)[0]+3, canvas.coords(sc)[1]+49, canvas.coords(sc)[4]+3, canvas.coords(sc)[5]+33)
                if ((canvas.coords(sc)[0] <= 194 and canvas.coords(mario)[0]<=194) or (canvas.coords(sc)[6]>=306 and canvas.coords(mario)[6]>=306)) and canvas.coords(mario)[3]<236 and canvas.coords(sc)[3]==139 and len(x)>=1 and sc_Estado==False and sc_morir==False:
                    sc_Estado=True
                    canvas.itemconfig(sc,fill='yellow')
                    m.after(5000,Unflipped)
            if sc2_Estado==False and sc2_morir==False and sc2_creada==True:
                xsc2=canvas.find_overlapping(canvas.coords(sc2)[0]+3, canvas.coords(sc2)[1]+49, canvas.coords(sc2)[4]+3, canvas.coords(sc2)[5]+33)
                if ((canvas.coords(sc2)[0] <= 194 and canvas.coords(mario)[0]<=194) or (canvas.coords(sc2)[6]>=306 and canvas.coords(mario)[6]>=306)) and canvas.coords(mario)[3]<236 and canvas.coords(sc2)[3]==139 and len(xsc2)>=1 and sc2_Estado==False and sc2_morir==False:
                    sc2_Estado=True
                    canvas.itemconfig(sc2,fill='yellow')
                    m.after(5000,Unflipped)
            canvas.move(mario,0,-5)
            canvas.update()
            m.after(10,salto())
        #4to piso
        elif sal==True and canvas.coords(mario)[1] >= y and canvas.coords(mario)[3] <=136 and canvas.coords(mario)[1]>66:
            canvas.move(mario,0,-5)
            canvas.update()
            m.after(10,salto())
            
        
        
            


        #Caer despues del salto
        sal=False
        #1mer piso - b1
        if sal== False and (canvas.coords(mario)[3]<436 or mario_Estado==True):
            #2do piso
            if sal==False and canvas.coords(mario)[3]==336 and(canvas.coords(mario)[0]<180 or canvas.coords(mario)[6]>320):
                y=canvas.coords(mario)[1]-120
                return None
            #3er piso medio
            if sal==False and (canvas.coords(mario)[6]>130 and canvas.coords(mario)[0]<370) and canvas.coords(mario)[3]==236:
                y=canvas.coords(mario)[1]-120
                return None
            #3r piso lados
            if sal==False and (canvas.coords(mario)[0]<60 or canvas.coords(mario)[6]>440) and canvas.coords(mario)[3]==246:
                y=canvas.coords(mario)[1]-120
                return None 
            #4to piso
            if sal==False and canvas.coords(mario)[3]==136 and (canvas.coords(mario)[0]<194 or canvas.coords(mario)[6]>306):
                y=canvas.coords(mario)[1]-120
                return None
            
            canvas.move(mario,0,5)
            canvas.update()
            m.after(10,salto())
        elif sal == False and canvas.coords(mario)[1]>406:
            y=canvas.coords(mario)[1]-120


def salto1():
    global sal, y, mario_Estado
    if mario_Estado==False:
        #1mer piso 
        if sal == True and canvas.coords(mario)[1] >= y and ((canvas.coords(mario)[1]>366) or (canvas.coords(mario)[0]>180 and canvas.coords(mario)[6]<320)) and canvas.coords(mario)[1]>266:
            canvas.move(mario,-1,-5)
            canvas.update()
            m.after(10,salto1())
        #2do piso medio
        elif sal==True and canvas.coords(mario)[1] >= y and canvas.coords(mario)[3] <=336 and canvas.coords(mario)[1]>166 and (canvas.coords(mario)[0]>60 and canvas.coords(mario)[6]<440)and((canvas.coords(mario)[1]>266) or ((canvas.coords(mario)[0]>60 and canvas.coords(mario)[6]<130)or(canvas.coords(mario)[0]>370 and canvas.coords(mario)[6]<440))):
            canvas.move(mario,-1,-5)
            canvas.update()
            m.after(10,salto1())
        #2do piso lados
        elif sal==True and canvas.coords(mario)[1]>=y and canvas.coords(mario)[3] <=336 and canvas.coords(mario)[1]>276 and (canvas.coords(mario)[0]<60 or canvas.coords(mario)[6]>440):
            canvas.move(mario,-1,-5)
            canvas.update()
            m.after(10,salto1())
        #3er piso
        elif sal==True and canvas.coords(mario)[1]>=y and canvas.coords(mario)[3]<=266 and ((canvas.coords(mario)[1]>166)or(canvas.coords(mario)[0]>194 and canvas.coords(mario)[6]<306)):
            canvas.move(mario,-1,-5)
            canvas.update()
            m.after(10,salto1())

        #4to piso
        elif sal==True and canvas.coords(mario)[1] >= y and canvas.coords(mario)[3] <=136 and canvas.coords(mario)[1]>66:
            canvas.move(mario,-1,-5)
            canvas.update()
            m.after(10,salto1())
        




        sal=False
        #1mer piso - b1
        if sal==False and (canvas.coords(mario)[3]<436 or mario_Estado==True):
            #b2
            if sal==False and canvas.coords(mario)[3]==336 and canvas.coords(mario)[0]<180:
                y=canvas.coords(mario)[1]-120
                return None
            #b3
            elif sal==False and canvas.coords(mario)[3]==336 and canvas.coords(mario)[6]>320:
                y=canvas.coords(mario)[1]-120
                return None
            #b4
            elif sal==False and canvas.coords(mario)[3]==246 and canvas.coords(mario)[0]<60:
                y=canvas.coords(mario)[1]-120
                return None
            #b5
            elif sal==False and canvas.coords(mario)[3]==236 and (canvas.coords(mario)[6]>130 and canvas.coords(mario)[0]<370):
                y=canvas.coords(mario)[1]-120
                return None
            #b6
            elif sal==False and canvas.coords(mario)[3]==246 and canvas.coords(mario)[6]>440:
                y=canvas.coords(mario)[1]-120
                return None
            #b7
            elif sal==False and canvas.coords(mario)[3]==136 and canvas.coords(mario)[0]<194:
                y=canvas.coords(mario)[1]-120
                return None
            #b8
            elif sal==False and canvas.coords(mario)[3]==136 and canvas.coords(mario)[6]>306:
                y=canvas.coords(mario)[1]-120
                return None 
            
            canvas.move(mario,-1,5)
            canvas.update()
            m.after(10,salto1())
        elif sal == False and canvas.coords(mario)[1]>406:
            y=canvas.coords(mario)[1]-120


def salto2():
    global sal, y, mario_Estado
    if mario_Estado==False:
        #1mer piso
        if sal==True and mario_Estado==False and canvas.coords(mario)[1] >= y and ((canvas.coords(mario)[1]>366)or(canvas.coords(mario)[0]>180 and canvas.coords(mario)[6]<320)) and canvas.coords(mario)[1]>266:
            canvas.move(mario,1,-5)
            canvas.update()
            m.after(10,salto2())
        #2do piso medio
        elif sal==True and canvas.coords(mario)[1] >= y and canvas.coords(mario)[3] <=336 and canvas.coords(mario)[1]>166 and (canvas.coords(mario)[0]>60 and canvas.coords(mario)[6]<440)and((canvas.coords(mario)[1]>266) or ((canvas.coords(mario)[0]>60 and canvas.coords(mario)[6]<130)or(canvas.coords(mario)[0]>370 and canvas.coords(mario)[6]<440))):
            canvas.move(mario,1,-5)
            canvas.update()
            m.after(10,salto2())
        #2do piso lados
        elif sal==True and canvas.coords(mario)[1]>=y and canvas.coords(mario)[3] <=336 and canvas.coords(mario)[1]>276 and (canvas.coords(mario)[0]<60 or canvas.coords(mario)[6]>440):
            canvas.move(mario,1,-5)
            canvas.update()
            m.after(10,salto2())
        #3er piso
        elif sal==True and canvas.coords(mario)[1]>=y and canvas.coords(mario)[3]<=266 and ((canvas.coords(mario)[1]>166)or(canvas.coords(mario)[0]>194 and canvas.coords(mario)[6]<306)):
            canvas.move(mario,1,-5)
            canvas.update()
            m.after(10,salto2())

        elif sal==True and canvas.coords(mario)[1] >= y and canvas.coords(mario)[3] <=136 and canvas.coords(mario)[1]>66:
            canvas.move(mario,1,-5)
            canvas.update()
            m.after(10,salto2())


            

        sal=False

        #1mer piso - b1
        if sal==False and (canvas.coords(mario)[3]<436 or mario_Estado==True):
            #b2
            if sal==False and canvas.coords(mario)[3]==336 and canvas.coords(mario)[0]<180:
                y=canvas.coords(mario)[1]-120
                return None
            #b3
            elif sal==False and canvas.coords(mario)[3]==336 and canvas.coords(mario)[6]>320:
                y=canvas.coords(mario)[1]-120
                return None
            #b4
            elif sal==False and canvas.coords(mario)[3]==246 and canvas.coords(mario)[0]<60:
                y=canvas.coords(mario)[1]-120
                return None
            #b5
            elif sal==False and canvas.coords(mario)[3]==236 and (canvas.coords(mario)[6]>130 and canvas.coords(mario)[0]<370):
                y=canvas.coords(mario)[1]-120
                return None
            #b6
            elif sal==False and canvas.coords(mario)[3]==246 and canvas.coords(mario)[6]>440:
                y=canvas.coords(mario)[1]-120
                return None
            #b7
            elif sal==False and canvas.coords(mario)[3]==136 and canvas.coords(mario)[0]<194:
                y=canvas.coords(mario)[1]-120
                return None
            #b8
            elif sal==False and canvas.coords(mario)[3]==136 and canvas.coords(mario)[6]>306:
                y=canvas.coords(mario)[1]-120
                return None
            canvas.move(mario,1,5)
            canvas.update()
            m.after(10,salto2())
        elif sal == False and canvas.coords(mario)[1]>406:
            y=canvas.coords(mario)[1]-120
        
        
#Funcion para las caidas de mario       
def freefall():
    global sal,y, mario_Estado
    #caer desde el 2do piso
    if mario_Estado==False:
        if sal==False and canvas.coords(mario)[2]>180 and canvas.coords(mario)[4]<320 and canvas.coords(mario)[3]<436 and canvas.coords(mario)[1]>=y and canvas.coords(mario)[1]>266:
            canvas.move(mario,0,5)
            canvas.update()
            m.after(10,freefall())
        #caer desde el 3er piso
        elif sal==False and canvas.coords(mario)[1]>=y  and ((canvas.coords(mario)[2]>60 and canvas.coords(mario)[4]<130) or (canvas.coords(mario)[2]>370 and canvas.coords(mario)[4]<440)) and canvas.coords(mario)[3]<336:
            canvas.move(mario,0,5)
            canvas.update()
            m.after(10,freefall())
        #caer desde el 4to piso
        elif sal==False and canvas.coords(mario)[1]>=y and canvas.coords(mario)[2]>194 and canvas.coords(mario)[4]<306 and canvas.coords(mario)[3]<236:
            canvas.move(mario,0,5)
            canvas.update()
            m.after(10,freefall())
        

"""Control de teclas y menu"""
def pressed (event):
    global sal,state, y, sc, sc2, sc_Estado, sc2_Estado, sc_morir, sc2_morir, mario, mario_Estado, sc2_creada, sc_creada
    tecla= repr (event.char)
    if mario_Estado==False:
        if (tecla == "'w'" or tecla== "'W'"):
            sal=True
            state[0]=True
            if state[1]==True:
                salto1()
            elif state[2]==True:

                salto2()
            elif (state[1]== False and state[2]==False):
                salto()
        elif(tecla=="'a'"or tecla == "'A'"):
            canvas.move(mario,-10,0)
            state[1]=True

            if sc_morir==False and sc_Estado==True and sc_creada==True:
                k=canvas.find_overlapping(canvas.coords(sc)[0], canvas.coords(sc)[1],canvas.coords(sc)[4], canvas.coords(sc)[5])
                #matar en segundo piso
                if ((canvas.coords(mario)[3]<=340 and canvas.coords(mario)[1]>240) and (canvas.coords(sc)[3]<=340 and canvas.coords(sc)[1]>240)) and ((canvas.coords(mario)[4]==canvas.coords(sc)[2]) or (canvas.coords(mario)[2]<=(canvas.coords(sc)[4]-1))) and  len(k)>1:
                    sc_morir=True
                    m.after(1,Matar)
                #matar en tercer piso medio
                elif ((canvas.coords(mario)[3]<=240 and canvas.coords(mario)[1]>140) and (canvas.coords(sc)[3]<=240 and canvas.coords(sc)[1]>140)) and ((canvas.coords(mario)[4]==canvas.coords(sc)[2]) or (canvas.coords(mario)[2]<=(canvas.coords(sc)[4]-1))) and len(k)>1:
                    sc_morir=True
                    m.after(1,Matar)
                #matar en cuarto piso
                elif canvas.coords(mario)[3]<=140 and canvas.coords(sc)[3]<=140 and ((canvas.coords(mario)[4]==canvas.coords(sc)[2]) or (canvas.coords(mario)[2]<=(canvas.coords(sc)[4]-1))) and len(k)>1:
                    sc_morir=True
                    m.after(1,Matar)
                    
            if sc2_morir==False and sc2_creada==True and sc2_Estado==True:
                hey=canvas.find_overlapping(canvas.coords(sc2)[0], canvas.coords(sc2)[1],canvas.coords(sc2)[4], canvas.coords(sc2)[5])
                #matar en segundo piso
                if ((canvas.coords(mario)[3]<=340 and canvas.coords(mario)[1]>240) and (canvas.coords(sc2)[3]<=340 and canvas.coords(sc2)[1]>240)) and ((canvas.coords(mario)[4]==canvas.coords(sc2)[2]) or (canvas.coords(mario)[2]<=(canvas.coords(sc2)[4]-1))) and  len(hey)>1:
                    sc2_morir=True
                    m.after(1,Matar)
                #matar en tercer piso medio
                elif ((canvas.coords(mario)[3]<=240 and canvas.coords(mario)[1]>140) and (canvas.coords(sc2)[3]<=240 and canvas.coords(sc2)[1]>140)) and ((canvas.coords(mario)[4]==canvas.coords(sc2)[2]) or (canvas.coords(mario)[2]<=(canvas.coords(sc2)[4]-1))) and len(hey)>1:
                    sc2_morir=True
                    m.after(1,Matar)
                #matar en cuarto piso
                elif canvas.coords(mario)[3]<=140 and canvas.coords(sc2)[3]<=140 and ((canvas.coords(mario)[4]==canvas.coords(sc2)[2]) or (canvas.coords(mario)[2]<=(canvas.coords(sc2)[4]-1))) and len(hey)>1:
                    sc2_morir=True
                    m.after(1,Matar)
                
                
        elif (tecla == "'d'" or tecla == "'D'"):
            state[2]=True
            canvas.move(mario,10,0)

            if sc_morir==False and sc_creada==True:
                k=canvas.find_overlapping(canvas.coords(sc)[0], canvas.coords(sc)[1],canvas.coords(sc)[4], canvas.coords(sc)[5])
                #matar en segundo piso
                if ((canvas.coords(mario)[3]<=340 and canvas.coords(mario)[1]>240) and (canvas.coords(sc)[3]<=340 and canvas.coords(sc)[1]>240)) and ((canvas.coords(mario)[4]==canvas.coords(sc)[2]) or (canvas.coords(mario)[2]<=(canvas.coords(sc)[4]-1))) and  len(k)>1:
                    sc_morir=True
                    m.after(1,Matar)
                #matar en tercer piso medio
                elif ((canvas.coords(mario)[3]<=240 and canvas.coords(mario)[1]>140) and (canvas.coords(sc)[3]<=240 and canvas.coords(sc)[1]>140)) and ((canvas.coords(mario)[4]==canvas.coords(sc)[2]) or (canvas.coords(mario)[2]<=(canvas.coords(sc)[4]-1))) and len(k)>1:
                    sc_morir=True
                    m.after(1,Matar)
                #matar en cuarto piso
                elif canvas.coords(mario)[3]<=140 and canvas.coords(sc)[3]<=140 and ((canvas.coords(mario)[4]==canvas.coords(sc)[2]) or (canvas.coords(mario)[2]<=(canvas.coords(sc)[4]-1))) and len(k)>1:
                    sc_morir=True
                    m.after(1,Matar)

            if sc2_morir==False and sc2_creada==True:
                hey=canvas.find_overlapping(canvas.coords(sc2)[0], canvas.coords(sc2)[1],canvas.coords(sc2)[4], canvas.coords(sc2)[5])
                #matar en segundo piso
                if ((canvas.coords(mario)[3]<=340 and canvas.coords(mario)[1]>240) and (canvas.coords(sc2)[3]<=340 and canvas.coords(sc2)[1]>240)) and ((canvas.coords(mario)[4]==canvas.coords(sc2)[2]) or (canvas.coords(mario)[2]<=(canvas.coords(sc2)[4]-1))) and  len(hey)>1:
                    sc2_morir=True
                    m.after(1,Matar)
                #matar en tercer piso medio
                elif ((canvas.coords(mario)[3]<=240 and canvas.coords(mario)[1]>140) and (canvas.coords(sc2)[3]<=240 and canvas.coords(sc2)[1]>140)) and ((canvas.coords(mario)[4]==canvas.coords(sc2)[2]) or (canvas.coords(mario)[2]<=(canvas.coords(sc2)[4]-1))) and len(hey)>1:
                    sc2_morir=True
                    m.after(1,Matar)
                #matar en cuarto piso
                elif canvas.coords(mario)[3]<=140 and canvas.coords(sc2)[3]<=140 and ((canvas.coords(mario)[4]==canvas.coords(sc2)[2]) or (canvas.coords(mario)[2]<=(canvas.coords(sc2)[4]-1))) and len(hey)>1:
                    sc2_morir=True
                    m.after(1,Matar)
            
        if canvas.coords(mario)[0]<0:
            canvas.move(mario, 500,0)
        if canvas.coords(mario)[6]>500:
            canvas.move(mario,-500,0)
        freefall()

    


def released(event):
    global sal, state
    tecla= repr (event.char)
    if (tecla=="'w'"):
        state[0]= False
    elif(tecla=="'a'"):
        state[1]= False
    elif(tecla=="'d'"):
        state[2]= False


#Menu
##canvas.after(200,shellcreeper) #Esperar para ejecutar esta funcion
##canvas.after(2000,shellcreeper2) #Esperar para ejecutar esta funcion
##canvas.after(2000,shellcreeper3) #Esperar para ejecutar esta funcion
#Text()



fondo= PhotoImage(file= "MARIOU.gif")
fond= canvas.create_image(250,300,image=fondo)


def arriba(event):
    """
    """
    canvas.move(selector,0,-86)
def abajo (event):
    """
    """
    canvas.move(selector,0,86)

menu=False
def tecla(event):
    """
    """
    global menu, selector
    teclaa=repr(event.char)
    if (teclaa=="'x'" and menu== False and canvas.coords(selector)[1]==198):
        menu= True
        canvas.delete(fond,selector)
        canvas.after(200,shellcreeper) #Esperar para ejecutar esta funcion
        canvas.after(2000,shellcreeper2) #Esperar para ejecutar esta funcion
        canvas.after(2000,shellcreeper3) #Esperar para ejecutar esta funcion


canvas.bind('<x>',tecla)       
        
selector=canvas.create_rectangle(90,198,100,208, fill="blue")

canvas.bind('<Up>',arriba)
canvas.bind('<Down>',abajo)
        


for char in ["w","a","d"]:
    canvas.bind("<KeyPress-%s>" % char, pressed)
    canvas.bind("<KeyRelease-%s>" % char, released)

canvas.focus_set()
canvas.pack
m.mainloop()




