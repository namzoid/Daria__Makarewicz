add_library('sound')

def setup():
    size(350, 400)
    global sf
    sf = SoundFile(this, "meow.wav")
    global id_photo
    id_photo = loadImage("photo.jpg")
    global c
    c =('FFFEFCFD')
def draw():
    global id_photo
    image(id_photo, 0, 0, 350, 400)
    print(hex(get(mouseX, mouseY)))
    strokeWeight(5)
    line(216, 231, 259, 220)
    line(228, 241, 262, 243)
    line(229, 256, 255, 268)
    line(122, 250, 94, 276)
    line(112, 240, 85, 244)
    line(81, 221, 121, 229)
    line(48, 108, 40, 23)
    line(40, 23, 87, 64)
    line(225, 69, 288, 17)
    line(288, 17, 274, 105)
    if mousePressed:
        ellipse(121, 194, 50, 50)
        ellipse(220, 191, 50, 50)
        line(146, 193, 195, 193)
        line(96, 195, 52, 189)
        line(246, 190, 283, 176)
    if keyCode==RIGHT:
            ellipse(121, 194, 6, 6)
    if keyCode==LEFT:
            ellipse(220, 191, 6, 6)
    if hex(get(mouseX,mouseY)) == c:
            text('zdjecie jest dowodowe',115, 363)
def mouseClicked():
    sf.play()
