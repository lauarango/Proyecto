from  tkinter import *



fondo=Tk()
fondo.geometry("500x500") 
di=PhotoImage(file="hey.gif") #Imagen del menu 
##l= PhotoImage(file= "levels.gif") #Imagen de los niveles
juego_cargado=False 
nombre="" #nombre del jugador
principal= Canvas(fondo,width=500,height=500) #Ventana principal
principal.pack(fill="none")
principal.create_image(250,300,image=di,anchor='center')
niv=Toplevel(principal)
selector=PhotoImage(file="lev.gif")
screen_selector=Canvas(niv,width=500,height=500) #Ventana niveles
screen_selector.pack(fill="none")
screen_selector.create_image(250,300,image=selector,anchor='center')


def nombre_pl(ventana):
    global nombre
    ventana.deiconify()
    name_label.config(text=" " + s)
    nombre += s
    
def Salir(ventana):
    ventana.destroy()


def Mostrar(ventana):
    ventana.deiconify()


def Ejecutar(funcion):
    principal.after(200, funcion)


def Esconder(ventana):
    ventana.withdraw()

    
def NivelE():
    global level, levelff
    level=level
    levelff=levelff

    
def NivelM():
    global level, levelff
    level=level-50
    levelff=levelff-50

    
def NivelH():
    global level, levelff
    level=level-100
    levelff=levelff-100
menu=False

player=Entry(principal) #Para ingresar texto
player.place(x=170,y=300)
nom=player.get()
boton1=Button(principal,text="NEW GAME", command=lambda: Ejecutar(Mostrar(m))) #Jugar nueva partida
boton1.place(x=195,y=254)

boton2 = Button(principal, text=" EXIT GAME ", command=lambda: Ejecutar(exit(principal))) #Salir de todo
boton2= Button(principal, text=" EXIT GAME ", command=lambda: Ejecutar(exit(fondo)))
boton2.place(x=195,y=400)

boton3 = Button(principal, text=" SET LEVEL ", command=lambda: Ejecutar(Mostrar(niv))) #Elegir nivel de dificultad
boton3.place(x=195, y=350)


botonEasy=Button(niv,text="EASY", command=NivelE)
botonEasy=Button(niv,text="EASY", command=lambda: Ejecutar(Esconder(niv)))
botonEasy.place(x=110,y=350)

botonMedium=Button(niv,text="MEDIUM", command=NivelM)
botonMedium=Button(niv,text="MEDIUM", command=lambda: Ejecutar(Esconder(niv)))
botonMedium.place(x=210,y=350)

botonHard=Button(niv,text="HARD", command=NivelH)
botonHard=Button(niv,text="HARD", command=lambda: Ejecutar(Esconder(niv)))
botonHard.place(x=330,y=350)


"""Canvas del juego"""


m= Toplevel()
canvas = Canvas (m, width= "500", height= "500", bg= "black")
canvas.focus_set()
canvas.pack()

mario= canvas.create_polygon (82, 406, 82, 436, 112, 436, 112,406, fill ="orangered")
sc=canvas.create_polygon(332,34,332,59,358,59,358,34,fill="peachpuff")

Score= 0 #puntaje incial
Vidas=3 #Vidas inciales
puntuacion=canvas.create_text(300,20,  fill="white", text=("Score", Score),font=("Comic Sans", 20))
oneUps=canvas.create_text(200,20,fill="lightsalmon",text=("Ups",Vidas),font=("Comic Sans", 20))
levelff=600 #Nivel default solo para los fighterfly
level=200 #Nivel default

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
    poww=canvas.create_rectangle(240,260,266,280,fill="slateblue")
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
sc_Estado=False  #No volteada tortuga1 d
sc_morir=False #Tortuga1 no esta muerta 
sc_creada=True #Tortuga1 creada
sc2_Estado=False #No volteada tortuga2 d
sc2_morir=False #Tortuga2 no esta muerta
sc2_creada=False #Tortuga2 no creada
mario_Estado=False #Mario vivo
sc3_Estado=False #No volteada tortuga3 i
sc3_morir=False #Tortuga3 no esta muerta
sc3_creada=False  #Tortuga3 no creada
ff_Estado=False #No volteada ff
ff_morir=False #ff no esta muerta i
ff_creada=False #ff no creada
ff_salto=False #ff esta en el piso
scAd_Estado=False #No volteada tortugaAd d
scAd_morir=False #tortugaAd no muerta
scAd_creada=False #tortufaAd no creada
first=0 #Contador tortugaAd
ff2_Estado=False #No volteada ff2
ff2_morir=False #ff2 no esta muerta d
ff2_creada=False #ff2 no creada
ff2_salto=False #ff2 esta en el piso
scAd2_Estado=False #TortugaAd2 no volteada
scAd2_morir=False #TortugaAd2 viva 
scAd2_creada=False #TortugaAd2 no creada
first2=0 #Contador tortugaAd2



#Funcion del pow

def POW():
    global sc_Estado, sc,sc_creada,sc2_Estado, sc2, sc2_creada,sc3_Estado, sc3, sc3_creada,scAd, scAd_Estado,scAd_creada,  ff, ff_Estado,ff_creada, ff2, ff2_Estado,  ff2_creada,scAd2, scAd2_Estado, scAd2_creada
    if sc_creada==True and (canvas.coords(sc)[3]==139 or canvas.coords(sc)[3]==239 or canvas.coords(sc)[3]==339 or canvas.coords(sc)[3]==439):
        sc_Estado=True
        canvas.itemconfig(sc,fill='yellow')
        m.after(7000,Unflipped)
    if sc2_creada==True and (canvas.coords(sc2)[3]==139 or canvas.coords(sc2)[3]==239 or canvas.coords(sc2)[3]==339 or canvas.coords(sc2)[3]==439):
        sc2_Estado=True
        canvas.itemconfig(sc2,fill='yellow')
        m.after(7000,Unflipped)
    if sc3_creada==True and (canvas.coords(sc3)[3]==139 or canvas.coords(sc3)[3]==239 or canvas.coords(sc3)[3]==339 or canvas.coords(sc3)[3]==439):
        sc3_Estado=True
        canvas.itemconfig(sc3,fill='yellow')
        m.after(7000,Unflipped)
    if scAd_creada==True and (canvas.coords(scAd)[3]==139 or canvas.coords(scAd)[3]==239 or canvas.coords(scAd)[3]==339 or canvas.coords(scAd)[3]==439):
        scAd_Estado=True
        canvas.itemconfig(scAd,fill='yellow')
        m.after(7000,Unflipped)
    if scAd2_creada==True and (canvas.coords(scAd2)[3]==139 or canvas.coords(scAd2)[3]==239 or canvas.coords(scAd2)[3]==339 or canvas.coords(scAd2)[3]==439):
        scAd2_Estado=True
        canvas.itemconfig(scAd2,fill='yellow')
        m.after(7000,Unflipped)
    if ff_creada==True and (canvas.coords(ff)[3]==139 or canvas.coords(ff)[3]==239 or canvas.coords(ff)[3]==339 or canvas.coords(ff)[3]==439):
        ff_Estado=True
        canvas.itemconfig(ff,fill='yellow')
        m.after(7000,Unflipped)
    if ff2_creada==True and (canvas.coords(ff2)[3]==139 or canvas.coords(ff2)[3]==239 or canvas.coords(ff2)[3]==339 or canvas.coords(ff2)[3]==439):
        ff2_Estado=True
        canvas.itemconfig(ff2,fill='yellow')
        m.after(7000,Unflipped)

#Funcion para actualizar vidas

def Actualizar_vidas(): 
    global Vidas
    Vidas-=1
    canvas.itemconfig(oneUps, text=("Ups",Vidas))
    if Vidas==0:
        Mario_Estado=True
        sc_Estado=True
        sc2_Estado=True
        sc3_Estado=True
        scAd_Estado=True
        scAd2_Estado=True
        ff_Estado=True
        ff2_Estado=True
        mensaje=canvas.create_text(240,215,  fill="red", text="GAME OVER",font=("Comic Sans", 50))

#Funcion para desvoltear a un enemigo
    
def Unflipped():
    global sc_Estado, sc, sc_morir, sc2_Estado, sc2, sc2_morir, sc3_Estado, sc3, sc3_morir, scAd, scAd_Estado, scAd_morir, ff, ff_Estado, ff_morir, ff_creada, ff_salto, ff2, ff2_Estado, ff2_morir, ff2_creada, ff2_salto, scAd2, scAd2_Estado, scAd2_morir, first2, first
    if sc_Estado==True and sc_morir==False:
        canvas.itemconfig(sc,fill='peachpuff')
        sc_Estado=False
    elif sc2_Estado==True and sc2_morir==False:
        canvas.itemconfig(sc2,fill='peachpuff')
        sc2_Estado=False
    elif sc3_Estado==True and sc3_morir==False:
        canvas.itemconfig(sc3,fill='peachpuff')
        sc3_Estado=False
    elif scAd_Estado==True and scAd_morir==False:
        canvas.itemconfig(scAd,fill='salmon')
        scAd_Estado=False
        first=0
        m.after(1,shellcreeperAdvc)
    elif scAd2_Estado==True and scAd2_morir==False:
        canvas.itemconfig(scAd2,fill='salmon')
        scAd2_Estado=False
        first=0
        m.after(1,shellcreeperAdvc2)
    elif ff_Estado==True and ff_morir==False:
        canvas.itemconfig(ff,fill='cadetblue')
        ff_Estado=False
        ff_salto=False
        fighterfly()
    elif ff2_Estado==True and ff2_morir==False:
        canvas.itemconfig(ff2,fill='cadetblue')
        ff2_Estado=False
        ff2_salto=False
        fighterfly2()

#Funcion para que mario muera

def Morir():
    global mario_Estado, mario, sal
    if mario_Estado==True and canvas.coords(mario)[3]<=536:
        canvas.move(mario,0,10)
        canvas.update()
        m.after(1,Morir)
    m.after(4000,InvocarMario)


#Funcion para que los enemigos mueran

def Matar():
    global sc, sc_Estado,sc_morir,sc2, sc2_Estado,sc2_morir, sc_creada, sc2_creada, sc3, sc3_Estado, sc3_morir, sc3_creada, scAd, scAd_Estado, scAd_morir, scAd_creada, ff, ff_Estado, ff_morir, ff_creada, ff2, ff2_Estado, ff2_morir,ff2_creada, ff2_salto, scAd2, scAd2_Estado, scAd2_morir, scAd2_creada
    if sc_Estado==True and sc_morir==True and sc_creada==True:
        canvas.delete(sc)
        sc_creada=False
        m.after(1,Actualizar_puntos)
        m.after(3000,invocarTortuga)
    if sc2_Estado==True and sc2_morir==True and sc2_creada==True:
        sc2_creada=False
        canvas.delete(sc2)
        m.after(1,Actualizar_puntos)
        m.after(3000,invocarTortuga)
    if sc3_Estado==True and sc3_morir==True and sc3_creada==True:
        sc3_creada=False
        canvas.delete(sc3)
        m.after(1,Actualizar_puntos)
        m.after(3000,invocarTortuga2)
    if scAd_Estado==True and scAd_morir==True and scAd_creada==True:
        scAd_creada=False
        canvas.delete(scAd)
        m.after(1,Actualizar_puntos)
        m.after(3000,invocarTortuga)
    if scAd2_Estado==True and scAd2_morir==True and scAd2_creada==True:
        scAd2_creada=False
        canvas.delete(scAd2)
        m.after(1,Actualizar_puntos)
        m.after(3000,invocarTortuga2)
    if ff_Estado==True and ff_morir==True and ff_creada==True:
        ff_creada=False
        canvas.delete(ff)
        m.after(1,Actualizar_puntos)
        m.after(3000,invocarTortuga2)
    if ff2_Estado==True and ff2_morir==True and ff2_creada==True:
        ff2_creada=False
        canvas.delete(ff2)
        m.after(1,Actualizar_puntos)
        m.after(3000,invocarTortuga)
        
#Funcion para crear enemigos de la derecha
        
def invocarTortuga():
    global sc, sc_Estado,sc_morir,sc2, sc2_Estado,sc2_morir, sc_creada, sc2_creada, scAd_Estado, scAd, scAd_morir, scAd_creada, first, ff2, ff2_Estado, ff2_morir, ff2_creada, ff2_salto
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
    if scAd_creada==False:
        scAd_morir=False
        scAd_Estado=False
        scAd=canvas.create_polygon(332,34,332,59,358,59,358,34,fill="salmon")
        scAd_creada=True
        first=0
        m.after(1,shellcreeperAdvc)
    if ff2_creada==False:
        ff2_morir=False
        ff2_Estado=False
        ff2=canvas.create_polygon(332,34,332,59,358,59,358,34,fill="cadetblue")
        ff2_creada=True
        m.after(1,fighterfly2)

#Funcion para crear enemigos d ela izquierda

def invocarTortuga2():
    global sc3_Estado,sc3_morir,sc3, sc3_creada, ff, ff_Estado, ff_salto,ff_morir, ff_creada, scAd2, scAd2_morir, scAd2_creada, first2
    if sc3_creada==False:
        sc3_morir=False
        sc3_Estado=False
        sc3=canvas.create_polygon(142,34,142,59,167,59,167,34,fill="peachpuff")
        sc3_creada=True
    if scAd2_creada==False:
        scAd2_morir=False
        scAd2_Estado=False
        scAd2=canvas.create_polygon(142,34,142,59,167,59,167,34,fill="salmon")
        scAd2_creada=True
        first2=0
        m.after(1,shellcreeperAdvc2)
    if ff_creada==False:
        ff_morir=False
        ff_Estado=False
        ff=canvas.create_polygon(142,34,142,59,167,59,167,34,fill="cadetblue")
        ff_creada=True
        ff_salto=False
        m.after(1,fighterfly)


#Funcion para revivir a mario

def InvocarMario():
    global mario, mario_Estado
    if mario_Estado==True:
        m.after(1,Actualizar_vidas)
        if Vidas>0:
            mario= canvas.create_polygon (82, 406, 82, 436, 112, 436, 112,406, fill ="orangered")
            mario_Estado=False



            
"""Movimiento de los enemigos"""
def shellcreeper():
    global sc, sc_Estado, sc_morir, mario, mario_Estado, Vidas
    if Vidas>0:
        if sc_Estado==False and sc_morir==False:

            if mario_Estado==False and sc_Estado==False:
                #1mer piso
                if ((canvas.coords(mario)[3]<=440 and canvas.coords(mario)[1]>340) and (canvas.coords(sc)[3]<=440 and canvas.coords(sc)[1]>340)) and ((canvas.coords(mario)[4]>=canvas.coords(sc)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(sc)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(sc)[3])<=5:
                    mario_Estado=True
                    m.after(1,Morir)
                #2do piso sin tuberias
                elif ((canvas.coords(mario)[3]<=340 and canvas.coords(mario)[1]>240) and (canvas.coords(sc)[3]<=340 and canvas.coords(sc)[1]>240)) and ((canvas.coords(mario)[4]>=canvas.coords(sc)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(sc)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(sc)[3])<=5:
                    mario_Estado=True
                    m.after(1,Morir)
                #4to piso
                elif ((canvas.coords(mario)[3]<=240 and canvas.coords(mario)[1]>140) and (canvas.coords(sc)[3]<=240 and canvas.coords(sc)[1]>140))and ((canvas.coords(mario)[4]>=canvas.coords(sc)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(sc)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(sc)[3])<=5:
                    mario_Estado=True
                    m.after(1,Morir)
                #5to piso
                elif canvas.coords(mario)[3]<=140 and canvas.coords(sc)[3]<=140 and ((canvas.coords(mario)[4]>=canvas.coords(sc)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(sc)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(sc)[3])<=5:
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
        m.after(level,shellcreeper) #Recursion


def shellcreeper2():
    global sc2_Estado, sc2_morir, sc2_creada, sc2,mario, mario_Estado, Vidas
    if Vidas>0:
        if sc2_creada==False:
            m.after(3000,invocarTortuga)
            m.after(100, shellcreeper2)
        elif sc2_creada==True:

            if mario_Estado==False and sc2_Estado==False:
                #1mer piso
                if ((canvas.coords(mario)[3]<=440 and canvas.coords(mario)[1]>340) and (canvas.coords(sc2)[3]<=440 and canvas.coords(sc2)[1]>340)) and ((canvas.coords(mario)[4]>=canvas.coords(sc2)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(sc2)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(sc2)[3])<=5:
                    mario_Estado=True
                    m.after(1,Morir)
                #2do piso sin tuberias
                elif ((canvas.coords(mario)[3]<=340 and canvas.coords(mario)[1]>240) and (canvas.coords(sc2)[3]<=340 and canvas.coords(sc2)[1]>240)) and ((canvas.coords(mario)[4]>=canvas.coords(sc2)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(sc2)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(sc2)[3])<=5:
                    mario_Estado=True
                    m.after(1,Morir)
                #4to piso
                elif ((canvas.coords(mario)[3]<=240 and canvas.coords(mario)[1]>140) and (canvas.coords(sc2)[3]<=240 and canvas.coords(sc2)[1]>140))and ((canvas.coords(mario)[4]>=canvas.coords(sc2)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(sc2)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(sc2)[3])<=5:
                    mario_Estado=True
                    m.after(1,Morir)
                #5to piso
                elif canvas.coords(mario)[3]<=140 and canvas.coords(sc2)[3]<=140 and ((canvas.coords(mario)[4]>=canvas.coords(sc2)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(sc2)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(sc2)[3])<=5:
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
                canvas.move(sc2,-7,0)
            #pantalla continua
            if sc2_Estado==False and sc2_morir==False and canvas.coords(sc2)[0]<0:
                canvas.move(sc2, 500,0)
            #Meterse en las tuberias
            if sc2_Estado==False and sc2_morir==False and canvas.coords(sc2)[2]<=80 and canvas.coords(sc2)[3]>360:
                canvas.delete(sc2)
                sc2=canvas.create_polygon(332,34,332,59,358,59,358,34,fill="peachpuff")
            m.after(level,shellcreeper2) #Recursion
        


def shellcreeper3():
    
    global sc3_Estado, sc3_morir, sc3_creada, sc3,mario, mario_Estado, Vidas
    if Vidas>0:
        if sc3_creada==False:
            m.after(3000,invocarTortuga2)
            m.after(100, shellcreeper3)
        elif sc3_creada==True:

            if mario_Estado==False and sc3_Estado==False:
                #1mer piso
                if ((canvas.coords(mario)[3]<=440 and canvas.coords(mario)[1]>340) and (canvas.coords(sc3)[3]<=440 and canvas.coords(sc3)[1]>340)) and ((canvas.coords(mario)[4]>=canvas.coords(sc3)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(sc3)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(sc3)[3])<=5:
                    mario_Estado=True
                    m.after(1,Morir)
                #2do piso sin tuberias
                elif ((canvas.coords(mario)[3]<=340 and canvas.coords(mario)[1]>240) and (canvas.coords(sc3)[3]<=340 and canvas.coords(sc3)[1]>240)) and ((canvas.coords(mario)[4]>=canvas.coords(sc3)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(sc3)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(sc3)[3])<=5:
                    mario_Estado=True
                    m.after(1,Morir)
                #4to piso
                elif ((canvas.coords(mario)[3]<=240 and canvas.coords(mario)[1]>140) and (canvas.coords(sc3)[3]<=240 and canvas.coords(sc3)[1]>140))and ((canvas.coords(mario)[4]>=canvas.coords(sc3)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(sc3)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(sc3)[3])<=5:
                    mario_Estado=True
                    m.after(1,Morir)
                #5to piso
                elif canvas.coords(mario)[3]<=140 and canvas.coords(sc3)[3]<=140 and ((canvas.coords(mario)[4]>=canvas.coords(sc3)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(sc3)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(sc3)[3])<=5:
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
            if sc3_Estado==False and sc3_morir==False and canvas.coords(sc3)[4]>=420 and canvas.coords(sc3)[3]>360:
                canvas.delete(sc3)
                sc3=canvas.create_polygon(142,34,142,59,167,59,167,34,fill="peachpuff")
            m.after(level,shellcreeper3) #Recursion

def shellcreeperAdvc():
    global scAd_Estado, scAd_morir, scAd_creada, scAd,mario, mario_Estado, Vidas
    if Vidas>0:
        if scAd_creada==False:
            m.after(3000,invocarTortuga)
        elif scAd_creada==True:
            if mario_Estado==False and scAd_Estado==False:
                #1mer piso
                if ((canvas.coords(mario)[3]<=440 and canvas.coords(mario)[1]>340) and (canvas.coords(scAd)[3]<=440 and canvas.coords(scAd)[1]>340)) and ((canvas.coords(mario)[4]>=canvas.coords(scAd)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(scAd)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(scAd)[3])<=5:
                    mario_Estado=True
                    m.after(1,Morir)
                #2do piso sin tuberias
                elif ((canvas.coords(mario)[3]<=340 and canvas.coords(mario)[1]>240) and (canvas.coords(scAd)[3]<=340 and canvas.coords(scAd)[1]>240)) and ((canvas.coords(mario)[4]>=canvas.coords(scAd)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(scAd)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(scAd)[3])<=5:
                    mario_Estado=True
                    m.after(1,Morir)
                #4to piso
                elif ((canvas.coords(mario)[3]<=240 and canvas.coords(mario)[1]>140) and (canvas.coords(scAd)[3]<=240 and canvas.coords(scAd)[1]>140))and ((canvas.coords(mario)[4]>=canvas.coords(scAd)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(scAd)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(scAd)[3])<=5:
                    mario_Estado=True
                    m.after(1,Morir)
                #5to piso
                elif canvas.coords(mario)[3]<=140 and canvas.coords(scAd)[3]<=140 and ((canvas.coords(mario)[4]>=canvas.coords(scAd)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(scAd)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(scAd)[3])<=5:
                    mario_Estado=True
                    m.after(1,Morir)
            if scAd_Estado==False and scAd_morir==False: 
                #caidas
                if scAd_Estado==False and canvas.coords(scAd)[3]<136 or ((canvas.coords(scAd)[4]<306 and canvas.coords(scAd)[2]>194) and canvas.coords(scAd)[3]<236) or ((canvas.coords(scAd)[2]>60 and canvas.coords(scAd)[4]<130) and canvas.coords(scAd)[3]<336) or ((canvas.coords(scAd)[4]<320 and canvas.coords(scAd)[2]>180)and canvas.coords(scAd)[3]<434 and canvas.coords(scAd)[3]>=336):
                    
                    canvas.move(scAd,0,5)
                    canvas.update()
                    m.after(40,shellcreeperAdvc)
                    return None
                
                #avanzar
                if scAd_Estado==False and scAd_morir==False:
                    canvas.move(scAd,-6,0)
                #pantalla continua
                if scAd_Estado==False and scAd_morir==False and canvas.coords(scAd)[0]<0:
                    canvas.move(scAd, 500,0)
                #Meterse en las tuberias
                if scAd_Estado==False and scAd_morir==False and canvas.coords(scAd)[2]<=80 and canvas.coords(scAd)[3]>360:
                    canvas.delete(scAd)
                    scAd=canvas.create_polygon(332,34,332,59,358,59,358,34,fill="salmon")
                    first=0
                m.after(level,shellcreeperAdvc) #Recursion

def shellcreeperAdvc2():
    global scAd2_Estado, scAd2_morir, scAd2_creada, scAd2,mario, mario_Estado, Vidas
    if Vidas>0:
        if scAd2_creada==False:
            m.after(3000,invocarTortuga2)
        elif scAd2_creada==True:
            if mario_Estado==False and scAd2_Estado==False:
                #1mer piso
                if ((canvas.coords(mario)[3]<=440 and canvas.coords(mario)[1]>340) and (canvas.coords(scAd2)[3]<=440 and canvas.coords(scAd2)[1]>340)) and ((canvas.coords(mario)[4]>=canvas.coords(scAd2)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(scAd2)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(scAd2)[3])<=5:
                    mario_Estado=True
                    m.after(1,Morir)
                #2do piso sin tuberias
                elif ((canvas.coords(mario)[3]<=340 and canvas.coords(mario)[1]>240) and (canvas.coords(scAd2)[3]<=340 and canvas.coords(scAd2)[1]>240)) and ((canvas.coords(mario)[4]>=canvas.coords(scAd2)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(scAd2)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(scAd2)[3])<=5:
                    mario_Estado=True
                    m.after(1,Morir)
                #4to piso
                elif ((canvas.coords(mario)[3]<=240 and canvas.coords(mario)[1]>140) and (canvas.coords(scAd2)[3]<=240 and canvas.coords(scAd2)[1]>140))and ((canvas.coords(mario)[4]>=canvas.coords(scAd2)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(scAd2)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(scAd2)[3])<=5:
                    mario_Estado=True
                    m.after(1,Morir)
                #5to piso
                elif canvas.coords(mario)[3]<=140 and canvas.coords(scAd2)[3]<=140 and ((canvas.coords(mario)[4]>=canvas.coords(scAd2)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(scAd2)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(scAd2)[3])<=5:
                    mario_Estado=True
                    m.after(1,Morir)

            if scAd2_Estado==False and scAd2_morir==False:
                #caidas
                if scAd2_Estado==False and canvas.coords(scAd2)[3]<136 or ((canvas.coords(scAd2)[4]<306 and canvas.coords(scAd2)[2]>194) and canvas.coords(scAd2)[3]<236) or ((canvas.coords(scAd2)[2]>370 and canvas.coords(scAd2)[4]<440) and canvas.coords(scAd2)[3]<336) or ((canvas.coords(scAd2)[4]<320 and canvas.coords(scAd2)[2]>180)and canvas.coords(scAd2)[3]<434 and canvas.coords(scAd2)[3]>=336):
                    
                    canvas.move(scAd2,0,5)
                    canvas.update()
                    m.after(40,shellcreeperAdvc2)
                    return None
                
                #avanzar
                if scAd2_Estado==False and scAd2_morir==False:
                    canvas.move(scAd2,6,0)
                #pantalla continua
                if scAd2_Estado==False and scAd2_morir==False and canvas.coords(scAd2)[0]>500:
                    canvas.move(scAd2, -500,0)
                #Meterse en las tuberias
                if scAd2_Estado==False and scAd2_morir==False and canvas.coords(scAd2)[6]>=420 and canvas.coords(scAd2)[3]>360:
                    canvas.delete(scAd2)
                    scAd2=canvas.create_polygon(142,34,142,59,167,59,167,34,fill="salmon")
                    first2=0
                m.after(level,shellcreeperAdvc2) #Recursion



def fighterfly():
    global ff_salto, ff, ff_Estado, ff_morir, mario, mario_Estado, Vidas
    if Vidas>0:
        if ff_creada==False:
            m.after(3000,invocarTortuga2)
        elif ff_creada==True:
            if mario_Estado==False and ff_Estado==False:
                #1mer piso
                if ((canvas.coords(mario)[3]<=440 and canvas.coords(mario)[1]>340) and (canvas.coords(ff)[3]<=440 and canvas.coords(ff)[1]>340)) and ((canvas.coords(mario)[4]>=canvas.coords(ff)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(ff)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(ff)[3])<=5:
                    mario_Estado=True
                    m.after(1,Morir)
                #2do piso 
                elif ((canvas.coords(mario)[3]<=340 and canvas.coords(mario)[1]>240) and (canvas.coords(ff)[3]<=340 and canvas.coords(ff)[1]>240)) and ((canvas.coords(mario)[4]>=canvas.coords(ff)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(ff)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(ff)[3])<=5:
                    mario_Estado=True
                    m.after(1,Morir)
                #4to piso
                elif ((canvas.coords(mario)[3]<=240 and canvas.coords(mario)[1]>140) and (canvas.coords(ff)[3]<=240 and canvas.coords(ff)[1]>140))and ((canvas.coords(mario)[4]>=canvas.coords(ff)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(ff)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(ff)[3])<=5:
                    mario_Estado=True
                    m.after(1,Morir)
                #5to piso
                elif canvas.coords(mario)[3]<=140 and canvas.coords(ff)[3]<=140 and ((canvas.coords(mario)[4]>=canvas.coords(ff)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(ff)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(ff)[3])<=5:
                    mario_Estado=True
                    m.after(1,Morir)

            if ff_Estado==False and ff_morir==False:

                if ff_salto==False and canvas.coords(ff)[3]==139:
                    canvas.move(ff,4,-40)

                elif ff_salto==False and canvas.coords(ff)[3]==239:      
                    canvas.move(ff,4,-40)

                elif ff_salto==False and canvas.coords(ff)[3]==339:
                    canvas.move(ff,4,-40)

                elif ff_salto==False and canvas.coords(ff)[3]==439:
                    canvas.move(ff,4,-40)

                ff_salto=True
                
                if ff_salto==True and canvas.coords(ff)[3]==99:
                    canvas.move(ff,4,10)
                    ff_salto=False
                elif ff_salto==True and canvas.coords(ff)[3]==199:      
                    canvas.move(ff,4,10)
                    ff_salto=False
                elif ff_salto==True and canvas.coords(ff)[3]==209:
                    canvas.move(ff,4,30)
                    ff_salto=False       
                elif ff_salto==True and canvas.coords(ff)[3]==299:
                    canvas.move(ff,4,10)
                    ff_salto=False
                elif ff_salto==True and canvas.coords(ff)[3]==309:
                    canvas.move(ff,4,30)
                    ff_salto=False  
                elif ff_salto==True and canvas.coords(ff)[3]==399:
                    canvas.move(ff,4,10)
                    ff_salto=False
                elif ff_salto==True and canvas.coords(ff)[3]==409:
                    canvas.move(ff,4,30)
                    ff_salto=False
                else:
                    ff_salto=False


                #pantalla continua
                if canvas.coords(ff)[0]>500:
                    canvas.move(ff,-500,0)
                #Meterse en las tuberias
                if canvas.coords(ff)[4]>=420 and canvas.coords(ff)[3]>360:
                    canvas.delete(ff)
                    ff=canvas.create_polygon(142,34,142,59,167,59,167,34,fill="cadetblue")
                m.after(10,freefall)
                m.after(levelff,fighterfly)

def fighterfly2():
    global ff2_salto, ff2, ff2_Estado, ff2_morir, mario, mario_Estado, Vidas
    if Vidas>0:

        if ff2_creada==False:
            m.after(3000,invocarTortuga)
        elif ff2_creada==True:
            if mario_Estado==False and ff2_Estado==False:
                #1mer piso
                if ((canvas.coords(mario)[3]<=440 and canvas.coords(mario)[1]>340) and (canvas.coords(ff2)[3]<=440 and canvas.coords(ff2)[1]>340)) and ((canvas.coords(mario)[4]>=canvas.coords(ff2)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(ff2)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(ff2)[3])<=5:
                    mario_Estado=True
                    m.after(1,Morir)
                #2do piso 
                elif ((canvas.coords(mario)[3]<=340 and canvas.coords(mario)[1]>240) and (canvas.coords(ff2)[3]<=340 and canvas.coords(ff2)[1]>240)) and ((canvas.coords(mario)[4]>=canvas.coords(ff2)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(ff2)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(ff2)[3])<=5:
                    mario_Estado=True
                    m.after(1,Morir)
                #4to piso
                elif ((canvas.coords(mario)[3]<=240 and canvas.coords(mario)[1]>140) and (canvas.coords(ff2)[3]<=240 and canvas.coords(ff2)[1]>140))and ((canvas.coords(mario)[4]>=canvas.coords(ff2)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(ff2)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(ff2)[3])<=5:
                    mario_Estado=True
                    m.after(1,Morir)
                #5to piso
                elif canvas.coords(mario)[3]<=140 and canvas.coords(ff2)[3]<=140 and ((canvas.coords(mario)[4]>=canvas.coords(ff2)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(ff2)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(ff2)[3])<=5:
                    mario_Estado=True
                    m.after(1,Morir)
                    
            if ff2_Estado==False and ff2_morir==False:
            
                if ff2_salto==False and canvas.coords(ff2)[3]==139:
                    canvas.move(ff2,-4,-40)

                elif ff2_salto==False and canvas.coords(ff2)[3]==239:      
                    canvas.move(ff2,-4,-40)

                elif ff2_salto==False and canvas.coords(ff2)[3]==339:
                    canvas.move(ff2,-4,-40)

                elif ff2_salto==False and canvas.coords(ff2)[3]==439:
                    canvas.move(ff2,-4,-40)

                ff2_salto=True
                
                if ff2_salto==True and canvas.coords(ff2)[3]==99:
                    canvas.move(ff2,-4,10)
                    ff2_salto=False
                elif ff2_salto==True and canvas.coords(ff2)[3]==199:      
                    canvas.move(ff2,-4,10)
                    ff2_salto=False
                elif ff2_salto==True and canvas.coords(ff2)[3]==209:
                    canvas.move(ff2,-4,30)
                    ff2_salto=False       
                elif ff2_salto==True and canvas.coords(ff2)[3]==299:
                    canvas.move(ff2,-4,10)
                    ff2_salto=False
                elif ff2_salto==True and canvas.coords(ff2)[3]==309:
                    canvas.move(ff2,-4,30)
                    ff2_salto=False  
                elif ff2_salto==True and canvas.coords(ff2)[3]==399:
                    canvas.move(ff2,-4,10)
                    ff2_salto=False
                elif ff2_salto==True and canvas.coords(ff2)[3]==409:
                    canvas.move(ff2,-4,30)
                    ff2_salto=False
                else:
                    ff2_salto=False


                #pantalla continua
                if ff2_Estado==False and ff2_morir==False and canvas.coords(ff2)[0]<0:
                    canvas.move(ff2, 500,0)
                #Meterse en las tuberias
                if ff2_Estado==False and ff2_morir==False and canvas.coords(ff2)[2]<=80 and canvas.coords(ff2)[3]>360:
                    canvas.delete(ff2)
                    ff2=canvas.create_polygon(332,34,332,59,358,59,358,34,fill="cadetblue")
                m.after(10,freefall)
                m.after(levelff,fighterfly2) #Recursion
    
            
    



"""Variables para movimiento de mario"""
sal=False
state=[0,0,0]
y=canvas.coords(mario)[1]-120

"""saltos"""

#Funcion para salto recto

def salto():
    global sal, y, sc, sc_Estado,sc_morir, sc_creada, sc2, sc2_Estado, mario_Estado, sc2_morir, sc2_creada,sc3,sc3_Estado, sc3_morir,sc3_creada, scAd, scAd_Estado, scAd_morir, scAd_creada, first, ff, ff_Estado, ff_morir, ff_creada, ff2, ff2_Estado, ff2_morir, ff2_creada, ff2_salto, scAd2, scAd2_Estado, scAd2_morir, scAd2_creada, first2
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
                    
            if sc3_Estado==False and sc3_morir==False and sc3_creada==True:
                xsc3=canvas.find_overlapping(canvas.coords(sc3)[0]+3, canvas.coords(sc3)[1]+49, canvas.coords(sc3)[4]+3, canvas.coords(sc3)[5]+33)
                if ((canvas.coords(sc3)[0] >= 83 and canvas.coords(sc3)[0] < 180 and canvas.coords(mario)[0]<180) or (canvas.coords(sc3)[6]<=417 and canvas.coords(sc3)[6]>320 and canvas.coords(mario)[6]>320)) and canvas.coords(mario)[1]>366 and  sc3_Estado==False and sc3_morir==False and len(xsc3) >=1 and canvas.coords(sc3)[3]==339:
                    sc3_Estado=True
                    canvas.itemconfig(sc3,fill='yellow')
                    m.after(5000,Unflipped)
                    
            if scAd_Estado==False and scAd_morir==False and scAd_creada==True:
                xscAd=canvas.find_overlapping(canvas.coords(scAd)[0]+3, canvas.coords(scAd)[1]+49, canvas.coords(scAd)[4]+3, canvas.coords(scAd)[5]+33)
                if ((canvas.coords(scAd)[0] >= 83 and canvas.coords(scAd)[0] < 180 and canvas.coords(mario)[0]<180) or (canvas.coords(scAd)[6]<=417 and canvas.coords(scAd)[6]>320 and canvas.coords(mario)[6]>320)) and canvas.coords(mario)[1]>366 and  scAd_Estado==False and scAd_morir==False and len(xscAd) >=1 and canvas.coords(scAd)[3]==339:
                    first+=1
                    if first==2:
                        scAd_Estado=True
                        canvas.itemconfig(scAd,fill='yellow')
                        m.after(5000,Unflipped)

            if scAd2_Estado==False and scAd2_morir==False and scAd2_creada==True:
                xscAd2=canvas.find_overlapping(canvas.coords(scAd2)[0]+3, canvas.coords(scAd2)[1]+49, canvas.coords(scAd2)[4]+3, canvas.coords(scAd2)[5]+33)
                if ((canvas.coords(scAd2)[0] >= 83 and canvas.coords(scAd2)[0] < 180 and canvas.coords(mario)[0]<180) or (canvas.coords(scAd2)[6]<=417 and canvas.coords(scAd2)[6]>320 and canvas.coords(mario)[6]>320)) and canvas.coords(mario)[1]>366 and  scAd_Estado==False and scAd2_morir==False and len(xscAd2) >=1 and canvas.coords(scAd2)[3]==339:
                    first2+=1
                    if first2==2:
                        scAd2_Estado=True
                        canvas.itemconfig(scAd2,fill='yellow')
                        m.after(5000,Unflipped)

            if ff_Estado==False and ff_morir==False and ff_creada==True:
                xff=canvas.find_overlapping(canvas.coords(ff)[0]+3, canvas.coords(ff)[1]+49, canvas.coords(ff)[4]+3, canvas.coords(ff)[5]+33)
                if ((canvas.coords(ff)[0] >= 83 and canvas.coords(ff)[0] < 180 and canvas.coords(mario)[0]<180) or (canvas.coords(ff)[6]<=417 and canvas.coords(ff)[6]>320 and canvas.coords(mario)[6]>320)) and canvas.coords(mario)[1]>366 and  ff_Estado==False and ff_morir==False and len(xff) >=1 and canvas.coords(ff)[3]==339:
                    ff_Estado=True
                    canvas.itemconfig(ff,fill='yellow')
                    m.after(5000,Unflipped)

            if ff2_Estado==False and ff2_morir==False and ff2_creada==True:
                xff2=canvas.find_overlapping(canvas.coords(ff2)[0]+3, canvas.coords(ff2)[1]+49, canvas.coords(ff2)[4]+3, canvas.coords(ff2)[5]+33)
                if ((canvas.coords(ff2)[0] >= 83 and canvas.coords(ff2)[0] < 180 and canvas.coords(mario)[0]<180) or (canvas.coords(ff2)[6]<=417 and canvas.coords(ff2)[6]>320 and canvas.coords(mario)[6]>320)) and canvas.coords(mario)[1]>366 and  ff2_Estado==False and ff2_morir==False and len(xff2) >=1 and canvas.coords(ff2)[3]==339:
                    ff2_Estado=True
                    canvas.itemconfig(ff2,fill='yellow')
                    m.after(5000,Unflipped)

            if canvas.coords(mario)[1]==y and (canvas.coords(mario)[4]>=238 and canvas.coords(mario)[2]<=282):
                m.after(1,POW)
            
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
                    
            if sc3_Estado==False and sc3_morir==False and sc3_creada==True:
                xsc3=canvas.find_overlapping(canvas.coords(sc3)[0]+3, canvas.coords(sc3)[1]+49, canvas.coords(sc3)[4]+3, canvas.coords(sc3)[5]+33)
                if len(xsc3)>=1 and sc3_Estado==False and sc3_morir==False and canvas.coords(sc3)[6]>=130 and canvas.coords(sc3)[6]<=370 and canvas.coords(mario)[3]<=336 and canvas.coords(mario)[1]>=266 and canvas.coords(sc3)[3]==239:
                    sc3_Estado=True
                    canvas.itemconfig(sc3,fill='yellow')
                    m.after(5000,Unflipped)
                    
            if scAd_Estado==False and scAd_morir==False and scAd_creada==True:
                xscAd=canvas.find_overlapping(canvas.coords(scAd)[0]+3, canvas.coords(scAd)[1]+49, canvas.coords(scAd)[4]+3, canvas.coords(scAd)[5]+33)
                if len(xscAd)>=1 and scAd_Estado==False and scAd_morir==False and canvas.coords(scAd)[6]>=130 and canvas.coords(scAd)[6]<=370 and canvas.coords(mario)[3]<=336 and canvas.coords(mario)[1]>=266 and canvas.coords(scAd)[3]==239:
                    first+=1
                    if first==2:
                        scAd_Estado=True
                        canvas.itemconfig(scAd,fill='yellow')
                        m.after(5000,Unflipped)

            if scAd2_Estado==False and scAd2_morir==False and scAd2_creada==True:
                xscAd2=canvas.find_overlapping(canvas.coords(scAd2)[0]+3, canvas.coords(scAd2)[1]+49, canvas.coords(scAd2)[4]+3, canvas.coords(scAd2)[5]+33)
                if len(xscAd2)>=1 and scAd2_Estado==False and scAd2_morir==False and canvas.coords(scAd2)[6]>=130 and canvas.coords(scAd2)[6]<=370 and canvas.coords(mario)[3]<=336 and canvas.coords(mario)[1]>=266 and canvas.coords(scAd2)[3]==239:
                    first2+=1
                    if first2==2:
                        scAd2_Estado=True
                        canvas.itemconfig(scAd2,fill='yellow')
                        m.after(5000,Unflipped)

            if ff_Estado==False and ff_morir==False and ff_creada==True:
                xff=canvas.find_overlapping(canvas.coords(ff)[0]+3, canvas.coords(ff)[1]+49, canvas.coords(ff)[4]+3, canvas.coords(ff)[5]+33)
                if len(xff)>=1 and ff_Estado==False and ff_morir==False and canvas.coords(ff)[6]>=130 and canvas.coords(ff)[6]<=370 and canvas.coords(mario)[3]<=336 and canvas.coords(mario)[1]>=266 and canvas.coords(ff)[3]==239:
                    ff_Estado=True
                    canvas.itemconfig(ff,fill='yellow')
                    m.after(5000,Unflipped)

            if ff2_Estado==False and ff2_morir==False and ff2_creada==True:
                xff2=canvas.find_overlapping(canvas.coords(ff2)[0]+3, canvas.coords(ff2)[1]+49, canvas.coords(ff2)[4]+3, canvas.coords(ff2)[5]+33)
                if len(xff2)>=1 and ff2_Estado==False and ff2_morir==False and canvas.coords(ff2)[6]>=130 and canvas.coords(ff2)[6]<=370 and canvas.coords(mario)[3]<=336 and canvas.coords(mario)[1]>=266 and canvas.coords(ff2)[3]==239:
                    ff2_Estado=True
                    canvas.itemconfig(ff2,fill='yellow')
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
                    
            if sc3_Estado==False and sc3_morir==False and sc3_creada==True:
                xsc3=canvas.find_overlapping(canvas.coords(sc3)[0]+3, canvas.coords(sc3)[1]+49, canvas.coords(sc3)[4]+3, canvas.coords(sc3)[5]+33)
                if ((canvas.coords(sc3)[0] <= 194 and canvas.coords(mario)[0]<=194) or (canvas.coords(sc3)[6]>=306 and canvas.coords(mario)[6]>=306)) and canvas.coords(mario)[3]<236 and canvas.coords(sc3)[3]==139 and len(xsc3)>=1 and sc3_Estado==False and sc3_morir==False:
                    sc3_Estado=True
                    canvas.itemconfig(sc3,fill='yellow')
                    m.after(5000,Unflipped)
                    
            if scAd_Estado==False and scAd_morir==False and scAd_creada==True:
                xscAd=canvas.find_overlapping(canvas.coords(scAd)[0]+3, canvas.coords(scAd)[1]+49, canvas.coords(scAd)[4]+3, canvas.coords(scAd)[5]+33)
                if ((canvas.coords(scAd)[0] <= 194 and canvas.coords(mario)[0]<=194) or (canvas.coords(scAd)[6]>=306 and canvas.coords(mario)[6]>=306)) and canvas.coords(mario)[3]<236 and canvas.coords(scAd)[3]==139 and len(xscAd)>=1 and scAd_Estado==False and scAd_morir==False:
                    first+=1
                    if first==2:
                        scAd_Estado=True
                        canvas.itemconfig(scAd,fill='yellow')
                        m.after(5000,Unflipped)

            if scAd2_Estado==False and scAd2_morir==False and scAd2_creada==True:
                xscAd2=canvas.find_overlapping(canvas.coords(scAd2)[0]+3, canvas.coords(scAd2)[1]+49, canvas.coords(scAd2)[4]+3, canvas.coords(scAd2)[5]+33)
                if ((canvas.coords(scAd2)[0] <= 194 and canvas.coords(mario)[0]<=194) or (canvas.coords(scAd2)[6]>=306 and canvas.coords(mario)[6]>=306)) and canvas.coords(mario)[3]<236 and canvas.coords(scAd2)[3]==139 and len(xscAd2)>=1 and scAd2_Estado==False and scAd2_morir==False:
                    first2+=1
                    if first2==2:
                        scAd2_Estado=True
                        canvas.itemconfig(scAd2,fill='yellow')
                        m.after(5000,Unflipped)


            if ff_Estado==False and ff_morir==False and ff_creada==True:
                xff=canvas.find_overlapping(canvas.coords(ff)[0]+3, canvas.coords(ff)[1]+49, canvas.coords(ff)[4]+3, canvas.coords(ff)[5]+33)
                if ((canvas.coords(ff)[0] <= 194 and canvas.coords(mario)[0]<=194) or (canvas.coords(ff)[6]>=306 and canvas.coords(mario)[6]>=306)) and canvas.coords(mario)[3]<236 and canvas.coords(ff)[3]==139 and len(xff)>=1 and ff_Estado==False and ff_morir==False:
                    ff_Estado=True
                    canvas.itemconfig(ff,fill='yellow')
                    m.after(5000,Unflipped)

            if ff2_Estado==False and ff2_morir==False and ff2_creada==True:
                xff2=canvas.find_overlapping(canvas.coords(ff2)[0]+3, canvas.coords(ff2)[1]+49, canvas.coords(ff2)[4]+3, canvas.coords(ff2)[5]+33)
                if ((canvas.coords(ff2)[0] <= 194 and canvas.coords(mario)[0]<=194) or (canvas.coords(ff2)[6]>=306 and canvas.coords(mario)[6]>=306)) and canvas.coords(mario)[3]<236 and canvas.coords(ff2)[3]==139 and len(xff2)>=1 and ff2_Estado==False and ff2_morir==False:
                    ff2_Estado=True
                    canvas.itemconfig(ff2,fill='yellow')
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

#Funcion para salto parabolico izquierda

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

#Funcion para salto parabolico derecha

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
        
        
#Funcion gravedad
            
def freefall():
    global sal,y, mario_Estado,ff, ff_creada, ff_Estado, ff_morir, ff2, ff2_Estado, ff2_morir, ff2_creada
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
            
    if ff_Estado==False and ff_morir==False and ff_creada==True:
        #caer 
        if canvas.coords(ff)[3]>=59 and canvas.coords(ff)[3]<139:
            canvas.move(ff,0,5)
            canvas.update()
            m.after(10,freefall())
        #caer 4to piso
        elif canvas.coords(ff)[2]>194 and canvas.coords(ff)[4]<306 and canvas.coords(ff)[3]<239 and canvas.coords(ff)[1]>=0:
            canvas.move(ff,0,5)
            canvas.update()
            m.after(10,freefall())
        #caer 3er piso
        elif canvas.coords(ff)[2]>370 and canvas.coords(ff)[4]<440 and canvas.coords(ff)[3]<339 and canvas.coords(ff)[3]>=234:
            canvas.move(ff,0,5)
            canvas.update()
            m.after(10,freefall())
        #caer 2do piso
        elif canvas.coords(ff)[2]>180 and canvas.coords(ff)[4]<320 and canvas.coords(ff)[3]<439 and canvas.coords(ff)[3]>=334:
            canvas.move(ff,0,5)
            canvas.update()
            m.after(10,freefall())
    
    if ff2_Estado==False and ff2_morir==False and ff2_creada==True:
        #caer 
        if canvas.coords(ff2)[3]>=59 and canvas.coords(ff2)[3]<139:
            canvas.move(ff2,0,5)
            canvas.update()
            m.after(10,freefall())
        #caer 4to piso
        elif canvas.coords(ff2)[2]>194 and canvas.coords(ff2)[4]<306 and canvas.coords(ff2)[3]<239 and canvas.coords(ff2)[1]>=0:
            canvas.move(ff2,0,5)
            canvas.update()
            m.after(10,freefall())
        #caer 3er piso
        elif canvas.coords(ff2)[2]>60 and canvas.coords(ff2)[4]<130 and canvas.coords(ff2)[3]<339 and canvas.coords(ff2)[3]>=234:
            canvas.move(ff2,0,5)
            canvas.update()
            m.after(10,freefall())
        #caer 2do piso
        elif canvas.coords(ff2)[2]>180 and canvas.coords(ff2)[4]<320 and canvas.coords(ff2)[3]<439 and canvas.coords(ff2)[3]>=334:
            canvas.move(ff2,0,5)
            canvas.update()
            m.after(10,freefall())
        

"""Control de teclas y menu"""
def pressed (event):
    global sal,state, y, sc, sc2, sc_Estado, sc2_Estado, sc_morir, sc2_morir, mario, mario_Estado, sc2_creada, sc_creada, sc3, sc3_Estado, sc3_morir, sc3_creada, scAd, scAd_Estado,scAd_morir,scAd_creada, ff, ff_Estado, ff_morir, ff_creada, ff2, ff2_Estado, ff2_morir, ff2_creada, scAd2, scAd2_Estado, scAd2_morir, scAd2_creada
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

                #matar en segundo piso
                if ((canvas.coords(mario)[3]<=340 and canvas.coords(mario)[1]>240) and (canvas.coords(sc)[3]<=340 and canvas.coords(sc)[1]>240)) and ((canvas.coords(mario)[4]>=canvas.coords(sc)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(sc)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(sc)[3])<=5:
                    sc_morir=True
                    m.after(1,Matar)
                #matar en tercer piso medio
                elif ((canvas.coords(mario)[3]<=240 and canvas.coords(mario)[1]>140) and (canvas.coords(sc)[3]<=240 and canvas.coords(sc2)[1]>140))and ((canvas.coords(mario)[4]>=canvas.coords(sc)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(sc)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(sc)[3])<=5:
                    sc_morir=True
                    m.after(1,Matar)
                #matar en cuarto piso
                elif canvas.coords(mario)[3]<=140 and canvas.coords(sc)[3]<=140 and ((canvas.coords(mario)[4]>=canvas.coords(sc)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(sc)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(sc)[3])<=5:
                    sc_morir=True
                    m.after(1,Matar)
                    
            if sc2_morir==False and sc2_creada==True and sc2_Estado==True:

                #matar en segundo piso
                if ((canvas.coords(mario)[3]<=340 and canvas.coords(mario)[1]>240) and (canvas.coords(sc2)[3]<=340 and canvas.coords(sc2)[1]>240)) and ((canvas.coords(mario)[4]>=canvas.coords(sc2)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(sc2)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(sc2)[3])<=5:
                    sc2_morir=True
                    m.after(1,Matar)
                #matar en tercer piso medio
                elif ((canvas.coords(mario)[3]<=240 and canvas.coords(mario)[1]>140) and (canvas.coords(sc2)[3]<=240 and canvas.coords(sc2)[1]>140))and ((canvas.coords(mario)[4]>=canvas.coords(sc2)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(sc2)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(sc2)[3])<=5:
                    sc2_morir=True
                    m.after(1,Matar)
                #matar en cuarto piso
                elif canvas.coords(mario)[3]<=140 and canvas.coords(sc2)[3]<=140 and ((canvas.coords(mario)[4]>=canvas.coords(sc2)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(sc2)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(sc2)[3])<=5:
                    sc2_morir=True
                    m.after(1,Matar)

            if sc3_morir==False and sc3_creada==True and sc3_Estado==True:

                #matar en segundo piso
                if ((canvas.coords(mario)[3]<=340 and canvas.coords(mario)[1]>240) and (canvas.coords(sc3)[3]<=340 and canvas.coords(sc3)[1]>240)) and ((canvas.coords(mario)[4]>=canvas.coords(sc3)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(sc3)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(sc3)[3])<=5:
                    sc3_morir=True
                    m.after(1,Matar)
                #matar en tercer piso medio
                elif ((canvas.coords(mario)[3]<=240 and canvas.coords(mario)[1]>140) and (canvas.coords(sc3)[3]<=240 and canvas.coords(sc3)[1]>140))and ((canvas.coords(mario)[4]>=canvas.coords(sc3)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(sc3)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(sc3)[3])<=5:
                    sc3_morir=True
                    m.after(1,Matar)
                #matar en cuarto piso
                elif canvas.coords(mario)[3]<=140 and canvas.coords(sc3)[3]<=140 and ((canvas.coords(mario)[4]>=canvas.coords(sc3)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(sc3)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(sc3)[3])<=5:
                    sc3_morir=True
                    m.after(1,Matar)

                    
            if scAd_morir==False and scAd_creada==True and scAd_Estado==True:

                #matar en segundo piso
                if ((canvas.coords(mario)[3]<=340 and canvas.coords(mario)[1]>240) and (canvas.coords(scAd)[3]<=340 and canvas.coords(scAd)[1]>240)) and ((canvas.coords(mario)[4]>=canvas.coords(scAd)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(scAd)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(scAd)[3])<=5:
                    scAd_morir=True
                    m.after(1,Matar)
                #matar en tercer piso medio
                elif ((canvas.coords(mario)[3]<=240 and canvas.coords(mario)[1]>140) and (canvas.coords(scAd)[3]<=240 and canvas.coords(scAd)[1]>140))and ((canvas.coords(mario)[4]>=canvas.coords(scAd)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(scAd)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(scAd)[3])<=5:
                    scAd_morir=True
                    m.after(1,Matar)
                #matar en cuarto piso
                elif canvas.coords(mario)[3]<=140 and canvas.coords(scAd)[3]<=140 and ((canvas.coords(mario)[4]>=canvas.coords(scAd)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(scAd)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(scAd)[3])<=5:
                    scAd_morir=True
                    m.after(1,Matar)

            if scAd2_morir==False and scAd2_creada==True and scAd2_Estado==True:

                #matar en segundo piso
                if ((canvas.coords(mario)[3]<=340 and canvas.coords(mario)[1]>240) and (canvas.coords(scAd2)[3]<=340 and canvas.coords(scAd2)[1]>240)) and ((canvas.coords(mario)[4]>=canvas.coords(scAd2)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(scAd2)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(scAd2)[3])<=5:
                    scAd2_morir=True
                    m.after(1,Matar)
                #matar en tercer piso medio
                elif ((canvas.coords(mario)[3]<=240 and canvas.coords(mario)[1]>140) and (canvas.coords(scAd2)[3]<=240 and canvas.coords(scAd2)[1]>140))and ((canvas.coords(mario)[4]>=canvas.coords(scAd2)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(scAd2)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(scAd2)[3])<=5:
                    scAd2_morir=True
                    m.after(1,Matar)
                #matar en cuarto piso
                elif canvas.coords(mario)[3]<=140 and canvas.coords(scAd2)[3]<=140 and ((canvas.coords(mario)[4]>=canvas.coords(scAd2)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(scAd2)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(scAd2)[3])<=5:
                    scAd2_morir=True
                    m.after(1,Matar)

            if ff_morir==False and ff_creada==True and ff_Estado==True:

                #matar en segundo piso
                if ((canvas.coords(mario)[3]<=340 and canvas.coords(mario)[1]>240) and (canvas.coords(ff)[3]<=340 and canvas.coords(ff)[1]>240)) and ((canvas.coords(mario)[4]>=canvas.coords(ff)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(ff)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(ff)[3])<=5:
                    ff_morir=True
                    m.after(1,Matar)
                #matar en tercer piso medio
                elif ((canvas.coords(mario)[3]<=240 and canvas.coords(mario)[1]>140) and (canvas.coords(ff)[3]<=240 and canvas.coords(ff)[1]>140))and ((canvas.coords(mario)[4]>=canvas.coords(ff)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(ff)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(ff)[3])<=5:
                    ff_morir=True
                    m.after(1,Matar)
                #matar en cuarto piso
                elif canvas.coords(mario)[3]<=140 and canvas.coords(ff)[3]<=140 and ((canvas.coords(mario)[4]>=canvas.coords(ff)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(ff)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(ff)[3])<=5:
                    ff_morir=True
                    m.after(1,Matar)

            if ff2_morir==False and ff2_creada==True and ff2_Estado==True:

                #matar en segundo piso
                if ((canvas.coords(mario)[3]<=340 and canvas.coords(mario)[1]>240) and (canvas.coords(ff2)[3]<=340 and canvas.coords(ff2)[1]>240)) and ((canvas.coords(mario)[4]>=canvas.coords(ff2)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(ff2)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(ff2)[3])<=5:
                    ff2_morir=True
                    m.after(1,Matar)
                #matar en tercer piso medio
                elif ((canvas.coords(mario)[3]<=240 and canvas.coords(mario)[1]>140) and (canvas.coords(ff2)[3]<=240 and canvas.coords(ff2)[1]>140))and ((canvas.coords(mario)[4]>=canvas.coords(ff2)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(ff2)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(ff2)[3])<=5:
                    ff2_morir=True
                    m.after(1,Matar)
                #matar en cuarto piso
                elif canvas.coords(mario)[3]<=140 and canvas.coords(ff2)[3]<=140 and ((canvas.coords(mario)[4]>=canvas.coords(ff2)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(ff2)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(ff2)[3])<=5:
                    ff2_morir=True
                    m.after(1,Matar)

                    
                
        elif (tecla == "'d'" or tecla == "'D'"):
            state[2]=True
            canvas.move(mario,10,0)


            if sc_morir==False and sc_Estado==True and sc_creada==True:

                #matar en segundo piso
                if ((canvas.coords(mario)[3]<=340 and canvas.coords(mario)[1]>240) and (canvas.coords(sc)[3]<=340 and canvas.coords(sc)[1]>240)) and ((canvas.coords(mario)[4]>=canvas.coords(sc)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(sc)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(sc)[3])<=5:
                    sc_morir=True
                    m.after(1,Matar)
                #matar en tercer piso medio
                elif ((canvas.coords(mario)[3]<=240 and canvas.coords(mario)[1]>140) and (canvas.coords(sc)[3]<=240 and canvas.coords(sc2)[1]>140))and ((canvas.coords(mario)[4]>=canvas.coords(sc)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(sc)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(sc)[3])<=5:
                    sc_morir=True
                    m.after(1,Matar)
                #matar en cuarto piso
                elif canvas.coords(mario)[3]<=140 and canvas.coords(sc)[3]<=140 and ((canvas.coords(mario)[4]>=canvas.coords(sc)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(sc)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(sc)[3])<=5:
                    sc_morir=True
                    m.after(1,Matar)
                    
            if sc2_morir==False and sc2_creada==True and sc2_Estado==True:

                #matar en segundo piso
                if ((canvas.coords(mario)[3]<=340 and canvas.coords(mario)[1]>240) and (canvas.coords(sc2)[3]<=340 and canvas.coords(sc2)[1]>240)) and ((canvas.coords(mario)[4]>=canvas.coords(sc2)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(sc2)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(sc2)[3])<=5:
                    sc2_morir=True
                    m.after(1,Matar)
                #matar en tercer piso medio
                elif ((canvas.coords(mario)[3]<=240 and canvas.coords(mario)[1]>140) and (canvas.coords(sc2)[3]<=240 and canvas.coords(sc2)[1]>140))and ((canvas.coords(mario)[4]>=canvas.coords(sc2)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(sc2)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(sc2)[3])<=5:
                    sc2_morir=True
                    m.after(1,Matar)
                #matar en cuarto piso
                elif canvas.coords(mario)[3]<=140 and canvas.coords(sc2)[3]<=140 and ((canvas.coords(mario)[4]>=canvas.coords(sc2)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(sc2)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(sc2)[3])<=5:
                    sc2_morir=True
                    m.after(1,Matar)

            if sc3_morir==False and sc3_creada==True and sc3_Estado==True:

                #matar en segundo piso
                if ((canvas.coords(mario)[3]<=340 and canvas.coords(mario)[1]>240) and (canvas.coords(sc3)[3]<=340 and canvas.coords(sc3)[1]>240)) and ((canvas.coords(mario)[4]>=canvas.coords(sc3)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(sc3)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(sc3)[3])<=5:
                    sc3_morir=True
                    m.after(1,Matar)
                #matar en tercer piso medio
                elif ((canvas.coords(mario)[3]<=240 and canvas.coords(mario)[1]>140) and (canvas.coords(sc3)[3]<=240 and canvas.coords(sc3)[1]>140))and ((canvas.coords(mario)[4]>=canvas.coords(sc3)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(sc3)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(sc3)[3])<=5:
                    sc3_morir=True
                    m.after(1,Matar)
                #matar en cuarto piso
                elif canvas.coords(mario)[3]<=140 and canvas.coords(sc3)[3]<=140 and ((canvas.coords(mario)[4]>=canvas.coords(sc3)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(sc3)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(sc3)[3])<=5:
                    sc3_morir=True
                    m.after(1,Matar)

                    
            if scAd_morir==False and scAd_creada==True and scAd_Estado==True:

                #matar en segundo piso
                if ((canvas.coords(mario)[3]<=340 and canvas.coords(mario)[1]>240) and (canvas.coords(scAd)[3]<=340 and canvas.coords(scAd)[1]>240)) and ((canvas.coords(mario)[4]>=canvas.coords(scAd)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(scAd)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(scAd)[3])<=5:
                    scAd_morir=True
                    m.after(1,Matar)
                #matar en tercer piso medio
                elif ((canvas.coords(mario)[3]<=240 and canvas.coords(mario)[1]>140) and (canvas.coords(scAd)[3]<=240 and canvas.coords(scAd)[1]>140))and ((canvas.coords(mario)[4]>=canvas.coords(scAd)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(scAd)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(scAd)[3])<=5:
                    scAd_morir=True
                    m.after(1,Matar)
                #matar en cuarto piso
                elif canvas.coords(mario)[3]<=140 and canvas.coords(scAd)[3]<=140 and ((canvas.coords(mario)[4]>=canvas.coords(scAd)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(scAd)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(scAd)[3])<=5:
                    scAd_morir=True
                    m.after(1,Matar)

            if scAd2_morir==False and scAd2_creada==True and scAd2_Estado==True:

                #matar en segundo piso
                if ((canvas.coords(mario)[3]<=340 and canvas.coords(mario)[1]>240) and (canvas.coords(scAd2)[3]<=340 and canvas.coords(scAd2)[1]>240)) and ((canvas.coords(mario)[4]>=canvas.coords(scAd2)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(scAd2)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(scAd2)[3])<=5:
                    scAd2_morir=True
                    m.after(1,Matar)
                #matar en tercer piso medio
                elif ((canvas.coords(mario)[3]<=240 and canvas.coords(mario)[1]>140) and (canvas.coords(scAd2)[3]<=240 and canvas.coords(scAd2)[1]>140))and ((canvas.coords(mario)[4]>=canvas.coords(scAd2)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(scAd2)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(scAd2)[3])<=5:
                    scAd2_morir=True
                    m.after(1,Matar)
                #matar en cuarto piso
                elif canvas.coords(mario)[3]<=140 and canvas.coords(scAd2)[3]<=140 and ((canvas.coords(mario)[4]>=canvas.coords(scAd2)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(scAd2)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(scAd2)[3])<=5:
                    scAd2_morir=True
                    m.after(1,Matar)

            if ff_morir==False and ff_creada==True and ff_Estado==True:

                #matar en segundo piso
                if ((canvas.coords(mario)[3]<=340 and canvas.coords(mario)[1]>240) and (canvas.coords(ff)[3]<=340 and canvas.coords(ff)[1]>240)) and ((canvas.coords(mario)[4]>=canvas.coords(ff)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(ff)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(ff)[3])<=5:
                    ff_morir=True
                    m.after(1,Matar)
                #matar en tercer piso medio
                elif ((canvas.coords(mario)[3]<=240 and canvas.coords(mario)[1]>140) and (canvas.coords(ff)[3]<=240 and canvas.coords(ff)[1]>140))and ((canvas.coords(mario)[4]>=canvas.coords(ff)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(ff)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(ff)[3])<=5:
                    ff_morir=True
                    m.after(1,Matar)
                #matar en cuarto piso
                elif canvas.coords(mario)[3]<=140 and canvas.coords(ff)[3]<=140 and ((canvas.coords(mario)[4]>=canvas.coords(ff)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(ff)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(ff)[3])<=5:
                    ff_morir=True
                    m.after(1,Matar)

            if ff2_morir==False and ff2_creada==True and ff2_Estado==True:

                #matar en segundo piso
                if ((canvas.coords(mario)[3]<=340 and canvas.coords(mario)[1]>240) and (canvas.coords(ff2)[3]<=340 and canvas.coords(ff2)[1]>240)) and ((canvas.coords(mario)[4]>=canvas.coords(ff2)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(ff2)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(ff2)[3])<=5:
                    ff2_morir=True
                    m.after(1,Matar)
                #matar en tercer piso medio
                elif ((canvas.coords(mario)[3]<=240 and canvas.coords(mario)[1]>140) and (canvas.coords(ff2)[3]<=240 and canvas.coords(ff2)[1]>140))and ((canvas.coords(mario)[4]>=canvas.coords(ff2)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(ff2)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(ff2)[3])<=5:
                    ff2_morir=True
                    m.after(1,Matar)
                #matar en cuarto piso
                elif canvas.coords(mario)[3]<=140 and canvas.coords(ff2)[3]<=140 and ((canvas.coords(mario)[4]>=canvas.coords(ff2)[2]-4) and (canvas.coords(mario)[2]<=canvas.coords(ff2)[4]+4)) and (canvas.coords(mario)[1]-canvas.coords(ff2)[3])<=5:
                    ff2_morir=True
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
def llamar():
#    canvas.after(200,shellcreeper) #Esperar para ejecutar esta funcion
    canvas.after(1000,shellcreeper2) #Esperar para ejecutar esta funcion
    canvas.after(1000,shellcreeper3) #Esperar para ejecutar esta funcion
    canvas.after(3000,shellcreeperAdvc) #Esperar para ejecutar esta funcion
    canvas.after(3000,shellcreeperAdvc2) #Esperar para ejecutar esta funcion
    canvas.after(3500,fighterfly) #Esperar para ejecutar esta funcion
    canvas.after(3500,fighterfly2) #Esperar para ejecutar esta funcion

llamar()
if sc_creada==True and sc2_creada==True and sc3_creada==True and scAd_creada==True and scAd2_creada==True and ff_creada==True and ff2_creada==True:
    a=(canvas.coords(sc)[0],canvas.coords(sc)[1],canvas.coords(sc)[2],canvas.coords(sc)[3],canvas.coords(sc)[4],canvas.coords(sc)[5],canvas.coords(sc)[6],canvas.coords(sc)[7])
    b=(canvas.coords(sc2)[0],canvas.coords(sc2)[1],canvas.coords(sc2)[2],canvas.coords(sc2)[3],canvas.coords(sc2)[4],canvas.coords(sc2)[5],canvas.coords(sc2)[6],canvas.coords(sc2)[7])
    c=(canvas.coords(sc3)[0],canvas.coords(sc3)[1],canvas.coords(sc3)[2],canvas.coords(sc3)[3],canvas.coords(sc3)[4],canvas.coords(sc3)[5],canvas.coords(sc3)[6],canvas.coords(sc3)[7])
    d=(canvas.coords(scAd)[0],canvas.coords(scAd)[1],canvas.coords(scAd)[2],canvas.coords(scAd)[3],canvas.coords(scAd)[4],canvas.coords(scAd)[5],canvas.coords(scAd)[6],canvas.coords(scAd)[7])
    e=(canvas.coords(scAd)[0],canvas.coords(scAd)[1],canvas.coords(scAd)[2],canvas.coords(scAd)[3],canvas.coords(scAd)[4],canvas.coords(scAd)[5],canvas.coords(scAd)[6],canvas.coords(scAd)[7])
    f=(canvas.coords(ff)[0],canvas.coords(ff)[1],canvas.coords(ff)[2],canvas.coords(ff)[3],canvas.coords(ff)[4],canvas.coords(ff)[5],canvas.coords(ff)[6],canvas.coords(ff)[7])
    g=(canvas.coords(ff2)[0],canvas.coords(ff2)[1],canvas.coords(ff2)[2],canvas.coords(ff2)[3],canvas.coords(ff2)[4],canvas.coords(ff2)[5],canvas.coords(ff2)[6],canvas.coords(ff2)[7])
    h=(canvas.coords(mario)[0],canvas.coords(mario)[1],canvas.coords(mario)[2],canvas.coords(mario)[3],canvas.coords(mario)[4],canvas.coords(mario)[5],canvas.coords(mario)[6],canvas.coords(mario)[7])

def GuardarPartida():
    global lifes, score, the_name
    name = "Partida Guardada"
    partida = open(name+".txt", "w")
    jugador = str(nombre)
    puntos = str(Score)
    scpos=str(a)
    sc2pos=str(b)
    sc3pos=str(c)
    scAdpos=str(d)
    ffpos=(e)
    ff2pos=(f)
    mariopos=str(g)
    vidas = str(vidas)
    partida.write(jugador + '\n')
    partida.write(puntos + '\n')
    partida.write(life + '\n')
    partida.write(scpos + '\n')
    partida.write(sc2pos + '\n')
    partida.write(sc3pos + '\n')
    partida.write(scAdpos + '\n')
    partida.close()
    
def Cargar():
    global Score, vidas
    titulo = "MarioBros"
    game_name= open(titulo+".txt", "r")
    reading = titulo.readline()
    score = titulo.readline()
    vidas = titulo.readline()

def Actualizar_puntos(): 
    global Score
    Score+=1
    canvas.itemconfig(puntuacion, text=("Score",Score))
    




for char in ["w","a","d"]:
    canvas.bind("<KeyPress-%s>" % char, pressed)
    canvas.bind("<KeyRelease-%s>" % char, released)

principal.focus_set()
principal.pack
m.withdraw()
niv.withdraw()

fondo.mainloop()




