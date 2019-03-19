def setup():
    krotkaKolorow = ((234,21,182),(201,227,101),(118,32,32))
    rectMode(CENTER)
    size(400,400)
    global x 
    global y 
    x = -25
    y = 165
    stroke(255,255,255)
    strokeWeight(1)
    fill(*krotkaKolorow[0])
def draw():
    krotkaKolorow = ((234,21,182),(201,227,101),(118,32,32))
    global x
    global y
    background(89,147,139);
    rect(x, y, 70, 70)
    if x<199:
         x+=1
         y+=1
    if x==199:
        fill(*krotkaKolorow[1])
        x+= 0
        y+= -1
    if y==-5:
        fill(*krotkaKolorow[2])
        x+=-1
        y+= 0
        
