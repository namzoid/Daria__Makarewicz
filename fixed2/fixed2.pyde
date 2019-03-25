def setup(): 
    global krotkaKolorow
    krotkaKolorow = ((234,21,182),(201,227,101),(118,32,32))
    size(400, 400)
    frameRate(10)
    rectMode(CENTER)
    global x
    global y
    global z
    x = 0
    y = 200
    z = 0
    stroke(255,255,255)
    strokeWeight(1)
def draw():
    global krotkaKolorow
    global x
    global y
    global z
    background(89,147,139);
    rect(x,y,50,50)
    fill(*krotkaKolorow[z])
    z = (z + 1) % 3
    if x>=0 and x<= 200:
        x+= 2
        y+= 2
    if x >= 100 and x<= 200:
        x+= 2
        y+= 2
    if x>= 200 and x <= 300:
        x+= 2
        y-= 2
    if x>= 300 and x <= 400: 
        x+= 2
        y-= 2
    
        