def setup():
    global krotkaKolorow
    krotkaKolorow = ((234,21,182),(201,227,101),(118,32,32), (0, 0, 0))
    global c
    c =('FFFFFFFF')
    background(89,147,139);
    size (400, 400)
    textSize (120)
    textAlign(CENTER)
    text("d", width/2-120, height/2)
    text("m", width/2+120, height/2)
def draw():
    if keyPressed == True:
        fill(0)
    global krotkaKolorow
    fill(*krotkaKolorow[1])
    if key == 'd':
        text("d", width/2-120, height/2)
    if key == 'm':
        text("m", width/2+120, height/2)
    else:
        fill(255)
    if mousePressed:
        fill(*krotkaKolorow[2])
        text('d',width/2-120, height/2)
        text('m', width/2+120, height/2)
    if keyCode==RIGHT:
            fill(*krotkaKolorow[0])
            text('m', width/2+120, height/2)
    if keyCode==LEFT:
         fill(*krotkaKolorow[0])
         text('d',width/2-120, height/2)
    if hex(get(mouseX,mouseY)) == c:
     fill(*krotkaKolorow[3])
     text('d',width/2-120, height/2)

    s = createShape()
    s.beginShape()
    s.fill(255, 184, 126)
    s.noStroke()
    s.vertex(0, height/3*2)
    s.vertex(0, height/3*2-50)
    s.vertex(50, height/3*2)
    s.vertex(50, height/3*2+50)
    s.vertex(50, height/3*2+50)
    s.vertex(150, height/7)
    s.vertex(50, height/3*2+50)
    s.vertex(width-100, height/3*2)
    s.endShape(CLOSE)
    shape(s, 25, 25)
