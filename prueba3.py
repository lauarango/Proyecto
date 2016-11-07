from  tkinter import *
import time

m= Tk ()
canvas = Canvas (m, width= "500", height= "500", bg= "black")
canvas.focus_set()
canvas.pack()
mario= canvas.create_polygon (82, 406, 82, 436, 112, 436, 112,406, fill ="orangered")
sc=canvas.create_polygon(332,34,332,59,358,59,358,34,fill="peachpuff")
#sidestepper=canvas.create_polygon()
#slipice=canvas.create_polygon()
#figtherfly=canvas.create.polygon()

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

#piso
cuadrado1=canvas.create_polygon(0, 436, 0, 500, 500, 500, 500, 436, fill="firebrick")

def bloques():
    #bloques1
    cuadrado2=canvas.create_polygon(0,340,0,360,180,360,180,340,fill="cyan")
    cuadrado3=canvas.create_polygon(500,340,500,360,320,360,320,340,fill="cyan")
    #bloques2
    cuadrado4=canvas.create_polygon(0,240,0,260,60,260,60,240,fill="cyan")
    cuadrado5=canvas.create_polygon(130,240,130,260,370,260,370,240,fill="cyan")
    cuadrado6=canvas.create_polygon(440,240,440,260,500,260,500,240,fill="cyan")
    #bloques3
    cuadrado7=canvas.create_polygon(0,140,0,160,180,160,180,140,fill="cyan")
    cuadrado8=canvas.create_polygon(320,140,320,160,500,160,500,140,fill="cyan")

#Graficas
bloques()
tubos()

sal=False
state=[0,0,0]
y=canvas.coords(mario)[1]-120

def salto():
    global sal, y
    #1mer piso
    if sal==True and canvas.coords(mario)[1] >= y and ((canvas.coords(mario)[1]>366) or (canvas.coords(mario)[0]>180 and canvas.coords(mario)[6]<320)) and canvas.coords(mario)[1]>266:
        canvas.move(mario,0,-5)
        canvas.update()
        m.after(10,salto())
    #2do piso
    elif sal==True and canvas.coords(mario)[1] >=y and canvas.coords(mario)[3]<=336 and ((canvas.coords(mario)[1]>266) or ((canvas.coords(mario)[0]>60 and canvas.coords(mario)[6]<130)or(canvas.coords(mario)[0]>370 and canvas.coords(mario)[6]<440))) and canvas.coords(mario)[1]>166:
        canvas.move(mario,0,-5)
        canvas.update()
        m.after(10,salto())
    #3er piso
    elif sal==True and canvas.coords(mario)[1] >= y and canvas.coords(mario)[3]<=266 and ((canvas.coords(mario)[1]>166) or (canvas.coords(mario)[0]>180 and canvas.coords(mario)[6]<320)):
        canvas.move(mario,0,-5)
        canvas.update()
        m.after(10,salto())
    #4to piso
    elif sal==True and canvas.coords(mario)[1] >= y and canvas.coords(mario)[3] <=136 and canvas.coords(mario)[1]>66:
        canvas.move(mario,0,-5)
        canvas.update()
        m.after(10,salto())





    sal=False
    #1mer piso - b1
    if sal== False and canvas.coords(mario)[3]<436:
        #2do piso
        if sal==False and canvas.coords(mario)[3]==336 and(canvas.coords(mario)[0]<180 or canvas.coords(mario)[6]>320):
            y=canvas.coords(mario)[1]-120
            return None
        #3er piso
        if sal==False and canvas.coords(mario)[3]==236 and(canvas.coords(mario)[0]<60 or (canvas.coords(mario)[6]>130 and canvas.coords(mario)[0]<370) or (canvas.coords(mario)[6]>440)):
            y=canvas.coords(mario)[1]-120
            return None
        #4to piso
        if sal==False and canvas.coords(mario)[3]==136 and(canvas.coords(mario)[0]<180 or canvas.coords(mario)[6]>320):
            y=canvas.coords(mario)[1]-120
            return None
        
        canvas.move(mario,0,5)
        canvas.update()
        m.after(10,salto())
    elif sal == False and canvas.coords(mario)[1]>406:
        y=canvas.coords(mario)[1]-120


def salto1():
    global sal, y
    #1mer piso 
    if sal == True and canvas.coords(mario)[1] >= y and ((canvas.coords(mario)[1]>366) or (canvas.coords(mario)[0]>180 and canvas.coords(mario)[6]<320)) and canvas.coords(mario)[1]>266:
        canvas.move(mario,-1,-5)
        canvas.update()
        m.after(10,salto1())
    #2do piso 
    elif sal== True and canvas.coords(mario)[1]>=y and canvas.coords(mario)[3]<=336 and((canvas.coords(mario)[1]>266)or((canvas.coords(mario)[0]>60 and canvas.coords(mario)[6]<130)or(canvas.coords(mario)[0]>370 and canvas.coords(mario)[6]<440))) and canvas.coords(mario)[1]>166:
        canvas.move(mario,-1,-5)
        canvas.update()
        m.after(10,salto1())
    #3er piso
    elif sal==True and canvas.coords(mario)[1] >= y and canvas.coords(mario)[3]<=266 and ((canvas.coords(mario)[1]>166) or (canvas.coords(mario)[0]>180 and canvas.coords(mario)[6]<320)):
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
    if sal==False and canvas.coords(mario)[3]<436:
        #b2
        if sal==False and canvas.coords(mario)[3]==336 and canvas.coords(mario)[0]<180:
            y=canvas.coords(mario)[1]-120
            return None
        #b3
        elif sal==False and canvas.coords(mario)[3]==336 and canvas.coords(mario)[6]>320:
            y=canvas.coords(mario)[1]-120
            return None
        #b4
        elif sal==False and canvas.coords(mario)[3]==236 and canvas.coords(mario)[0]<60:
            y=canvas.coords(mario)[1]-120
            return None
        #b5
        elif sal==False and canvas.coords(mario)[3]==236 and (canvas.coords(mario)[6]>130 and canvas.coords(mario)[0]<370):
            y=canvas.coords(mario)[1]-120
            return None
        #b6
        elif sal==False and canvas.coords(mario)[3]==236 and canvas.coords(mario)[6]>440:
            y=canvas.coords(mario)[1]-120
            return None
        #b7
        elif sal==False and canvas.coords(mario)[3]==136 and canvas.coords(mario)[2]<180:
            y=canvas.coords(mario)[1]-120
            return None
        #b8
        elif sal==False and canvas.coords(mario)[3]==136 and canvas.coords(mario)[4]>320:
            y=canvas.coords(mario)[1]-120
            return None 
        
        canvas.move(mario,-1,5)
        canvas.update()
        m.after(10,salto1())
    elif sal == False and canvas.coords(mario)[1]>406:
        y=canvas.coords(mario)[1]-120


def salto2():
    global sal, y
    #1mer piso
    if sal==True and canvas.coords(mario)[1] >= y and ((canvas.coords(mario)[1]>366)or(canvas.coords(mario)[0]>180 and canvas.coords(mario)[6]<320)) and canvas.coords(mario)[1]>266:
        canvas.move(mario,1,-5)
        canvas.update()
        m.after(10,salto2())
    #2do piso
    elif sal== True and canvas.coords(mario)[1]>=y and canvas.coords(mario)[3]<=336 and((canvas.coords(mario)[1]>266)or((canvas.coords(mario)[0]>60 and canvas.coords(mario)[6]<130)or(canvas.coords(mario)[0]>370 and canvas.coords(mario)[6]<440))) and canvas.coords(mario)[1]>166:
        canvas.move(mario,1,-5)
        canvas.update()
        m.after(10,salto2())
    #3er piso
    elif sal==True and canvas.coords(mario)[1] >= y and canvas.coords(mario)[3]<=266 and ((canvas.coords(mario)[1]>166) or (canvas.coords(mario)[0]>180 and canvas.coords(mario)[6]<320)):
        canvas.move(mario,1,-5)
        canvas.update()
        m.after(10,salto2())
    elif sal==True and canvas.coords(mario)[1] >= y and canvas.coords(mario)[3] <=136 and canvas.coords(mario)[1]>66:
        canvas.move(mario,1,-5)
        canvas.update()
        m.after(10,salto2())


        

    sal=False

    #1mer piso - b1
    if sal==False and canvas.coords(mario)[3]<436:
        #b2
        if sal==False and canvas.coords(mario)[3]==336 and canvas.coords(mario)[0]<180:
            y=canvas.coords(mario)[1]-120
            return None
        #b3
        elif sal==False and canvas.coords(mario)[3]==336 and canvas.coords(mario)[6]>320:
            y=canvas.coords(mario)[1]-120
            return None
        #b4
        elif sal==False and canvas.coords(mario)[3]==236 and canvas.coords(mario)[0]<60:
            y=canvas.coords(mario)[1]-120
            return None
        #b5
        elif sal==False and canvas.coords(mario)[3]==236 and (canvas.coords(mario)[6]>130 and canvas.coords(mario)[0]<370):
            y=canvas.coords(mario)[1]-120
            return None
        #b6
        elif sal==False and canvas.coords(mario)[3]==236 and canvas.coords(mario)[6]>440:
            y=canvas.coords(mario)[1]-120
            return None
        #b7
        elif sal==False and canvas.coords(mario)[3]==136 and canvas.coords(mario)[2]<180:
            y=canvas.coords(mario)[1]-120
            return None
        #b8
        elif sal==False and canvas.coords(mario)[3]==136 and canvas.coords(mario)[4]>320:
            y=canvas.coords(mario)[1]-120
            return None 
        canvas.move(mario,1,5)
        canvas.update()
        m.after(10,salto2())
    elif sal == False and canvas.coords(mario)[1]>406:
        y=canvas.coords(mario)[1]-120
        
        
        
def freefall():
    global sal,y
    #caer desde el 2do piso
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
    elif sal==False and canvas.coords(mario)[1]>=y and canvas.coords(mario)[2]>180 and canvas.coords(mario)[4]<320 and canvas.coords(mario)[3]<236:
        canvas.move(mario,0,5)
        canvas.update()
        m.after(10,freefall())       



def pressed (event):
    global sal,state, y 
    tecla= repr (event.char)
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
    elif (tecla == "'d'" or tecla == "'D'"):
        state[2]=True
        canvas.move(mario,20,0)
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

#Movimeinto de los enemigos
def shellcreeper():
    #caidas
    if canvas.coords(sc)[3]<136 or ((canvas.coords(sc)[4]<320 and canvas.coords(sc)[2]>180) and canvas.coords(sc)[3]<236) or ((canvas.coords(sc)[2]>60 and canvas.coords(sc)[4]<130) and canvas.coords(sc)[3]<336):
        canvas.move(sc,0,5)
        canvas.update()
        m.after(10,shellcreeper())
    #avanzar
    canvas.move(sc,-1,0)
    canvas.update()
    m.after(20,shellcreeper())
        
#shellcreeper()
        

for char in ["w","a","d"]:
    canvas.bind("<KeyPress-%s>" % char, pressed)
    canvas.bind("<KeyRelease-%s>" % char, released)


m.mainloop()



