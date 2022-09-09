x = 255
y = 270
velY = 0
gravedad = 0.2

def Flappy():
    global x,y
    l = 5
    background(24, 247, 244)
    #rect(300,300,1,1) 1px en el centro
    #rect(300,300,5,5)
    #x -> 17 cuadros
    #y -> 12 cuadros
    #17*5 = 85
    #12*5 = 60
    #Fila 1
    fill(0)
    stroke(0)
    rect(x+l*6,y,l*6,l)
    #Fila 2
    rect(x+l*4,y+l,l*2,l)
    rect(x+l*9,y+l,l*1,l)
    rect(x+l*12,y+l,l*1,l)
    #Fila 3
    rect(x+l*3,y+l*2,l,l)
    rect(x+l*8,y+l*2,l,l*3)
    rect(x+l*13,y+l*2,l,l)
    #Fila 4
    rect(x+l*2,y+l*3,l,l)
    rect(x+l*12,y+l*3,l,l*2)
    rect(x+l*14,y+l*3,l,l*3)
    #Fila 5
    rect(x+l,y+l*4,l,l*3)
    #Fila 6
    rect(x+l*9,y+l*5,l,l)
    #Fila 7
    rect(x+l*2,y+l*6,l*4,l)
    rect(x+l*10,y+l*6,l*6,l)
    #Fila 8
    rect(x,y+l*7,l,l*3)
    rect(x+l*6,y+l*7,l,l)
    rect(x+l*9,y+l*7,l,l)
    rect(x+l*16,y+l*7,l,l)
    #Fila 9
    rect(x+l*5,y+l*8,l,l)
    rect(x+l*8,y+l*8,l,l)
    rect(x+l*10,y+l*8,l*6,l)
    #Fila 10
    rect(x+l*4,y+l*9,l,l)
    rect(x+l*9,y+l*9,l,l)
    rect(x+l*15,y+l*9,l,l)
    #Fila 11
    rect(x+l,y+l*10,l*4,l)
    rect(x+l*10,y+l*10,l*5,l)
    #Fila 12
    rect(x+l*5,y+l*11,l*5,l)
    #Color naranja
    #Fila 11
    fill(224, 153, 49)
    stroke(224, 153, 49)
    rect(x+l*5,y+l*10,l*5,l)
    #Fila 10
    rect(x+l*5,y+l*9,l*4,l)
    #Fila 9
    rect(x+l*6,y+l*8,l*2,l)
    #Color pico
    fill(224, 80, 49)
    stroke(224, 80, 49)
    rect(x+l*10,y+l*9,l*5,l)
    rect(x+l*9,y+l*8,l,l)
    rect(x+l*10,y+l*7,l*6,l)
    #Color ala
    fill(249, 247, 202)
    stroke(249, 247, 202)
    rect(x+l,y+l*8,l*2,l*2)
    rect(x+l*2,y+l*7,l*3,l*2)
    #Color amarillo
    fill(212,191,38)
    stroke(212,191,38)
    rect(x+l,y+l*7,l,l)
    rect(x+l*5,y+l*7,l,l)
    rect(x+l*7,y+l*7,l*2,l)
    rect(x+l*3,y+l*9,l,l)
    rect(x+l*6,y+l*6,l*4,l)
    #JUAN
    #color fila 2
    stroke(227,236,190)
    fill(227,236,190)
    rect(x+l*6,y+l,l*3,l)
    stroke(237,253,221)
    fill(237,253,221)
    rect(x+l*10,y+l,l*2,l*4)
    #color fila 3
    stroke(227,236,190)
    fill(227,236,190)
    rect(x+l*4,y+l*2,l*2,l)
    stroke(212,191,38)
    fill(212,191,38)
    rect(x+l*6,y+l*2,l*2,l)
    stroke(237,253,221)
    fill(237,253,221)
    rect(x+l*9,y+l*2,l,l)
    rect(x+l*12,y+l*2,l,l)
    #color fila 4
    stroke(227,236,190)
    fill(227,236,190)
    rect(x+l*3,y+l*3,l,l)
    stroke(201,191,38)
    fill(212,191,38)
    rect(x+l*4,y+l*3,l*4,l)
    fill(201,193,193)
    stroke(201,193,193)
    rect(x+l*9,y+l*3,l,l*2)
    stroke(237,253,221)
    fill(237,253,221)
    rect(x+l*13,y+l*3,l,l*3)
    #color fila 5
    stroke(212,191,38)
    fill(212,191,38)
    rect(x+l*2,y+l*4,l*6,l)
    #color fila 6
    rect(x+l*2,y+l*5,l*7,l)
    fill(201,193,193)
    stroke(201,193,193)
    rect(x+l*10,y+l*5,l,l)
    stroke(237,253,221)
    fill(237,253,221)
    rect(x+l*11,y+l*5,l*2,l)

def setup():
    size(600,600)
    
def draw():
    global x,y, velY, gravedad
    Flappy()
    velY += gravedad
    y += velY
    if y >= 600:
        y = 0
        
def mousePressed():
    global y, velY, gravedad
    velY = -5
    
    
    
