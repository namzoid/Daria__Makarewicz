def setup(): 
    krotkaKolorow = ((234,21,182),(201,227,101),(118,32,32))
    size(400, 400)
    frameRate(30)
    rectMode(CENTER)
    global x
    global y
    x = 0
    y = 200
    stroke(255,255,255)
    strokeWeight(1) 
    fill(*krotkaKolorow[0])
def draw():
    krotkaKolorow = ((234,21,182),(201,227,101),(118,32,32))
    global x
    global y
    background(89,147,139);
    rect(x,y,50,50)
    if x>=0 and x<= 200:
        x+= 2
        y+= 2
    if x >= 100 and x<= 200:
        fill(*krotkaKolorow[0])
        x+= 2
        y+= 2
    if x>= 200 and x <= 300:
        fill(*krotkaKolorow[1])
        x+= 2
        y-= 2
    if x>= 300 and x <= 400: 
        fill(*krotkaKolorow[2])
        x+= 2
        y-= 2
    
        
