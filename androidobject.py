def cylinder(sides = 64):
    # first endcap
    
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, -1)
    endShape(CLOSE)
    
    # second endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, 1)
    endShape(CLOSE)
    
    # sides
    x1 = 1
    y1 = 0
    for i in range(sides):
        theta = (i + 1) * 2 * PI / sides
        x2 = cos(theta)
        y2 = sin(theta)
        beginShape()
        normal (x1, y1, 0)
        vertex (x1, y1, 1)
        vertex (x1, y1, -1)
        normal (x2, y2, 0)
        vertex (x2, y2, -1)
        vertex (x2, y2, 1)
        endShape(CLOSE)
        x1 = x2
        y1 = y2
    
def body(whichObject, sides = 64): 
    cylinder()
def face(whichObject, sides = 64):
    if (frameCount > 690 and whichObject == True):
        fill(frameCount - 690, 0,0)
    if (frameCount >= 1100 and frameCount < 1500 and whichObject == True):
        fill(255, frameCount - 1100, 0)
    if (frameCount >= 1500):
        fill(255 - (frameCount-1500), 255 - (frameCount-1500), 255 - (frameCount-1500))
    sphere(10)
    pushMatrix()
    translate(0,0,9)
    scale(0.06,0.06,0.06)
    #rotateX(PI/2);
    rotateZ(PI/3);
    triangularPyramid()
    popMatrix()

def triangularPyramid(sides = 64):
    #translate(400, 400, 0)
    #stroke(0,0,0)
    fill(188,27,57)
    beginShape()
    vertex(-100, -100, -100);
    vertex( 100, -100, -100);
    vertex(   0,    0,  100);
    endShape(CLOSE)
    fill(231,207,0)
    beginShape()
    vertex( 100, -100, -100);
    vertex( 100,  100, -100);
    vertex(   0,    0,  100);
    endShape(CLOSE)
    fill(188,27,57)

    beginShape()
    vertex( 100, 100, -100);
    vertex(-100, 100, -100);
    vertex(   0,   0,  100);
    endShape(CLOSE)
    fill(231,207,0)

    beginShape()
    vertex(-100,  100, -100);
    vertex(-100, -100, -100);
    vertex(   0,    0,  100);
    endShape(CLOSE)
def legs(whichObject, sides = 64):
    if (frameCount > 690 and whichObject == True):
        fill(frameCount - 690, 0,0)
    if (frameCount >= 1100 and frameCount < 1500 and whichObject == True):
        fill(255, frameCount - 1100, 0)
    if (frameCount >= 1500):
        fill(255 - (frameCount-1500), 255 - (frameCount-1500), 255 - (frameCount-1500))

    pushMatrix()
    if(frameCount < 390):
        rotateX((0.5)*sin((frameCount/15.0)))
    if(frameCount > 590 and frameCount < 690 and whichObject != True):
        rotateY(-(2)*cos((frameCount/5.0)))

    translate(05,-11,0)
    scale(2,6,2)
    rotateX(PI/2)
    cylinder()
    popMatrix()
    pushMatrix()
    if(frameCount < 390):
        rotateX(-(0.5)*sin((frameCount/15.0)))
    if(frameCount > 590 and frameCount < 690 and whichObject != True):
        rotateY(-(2)*cos((frameCount/5.0)))
    translate(-5,-11,0)
    scale(2,6,2)
    rotateX(PI/2)
    cylinder()
    popMatrix()
def antennas(whichObject, sides = 64):
    
    if (frameCount > 690 and whichObject == True):
        fill(frameCount - 690, 0,0)
    if (frameCount >= 1100 and frameCount < 1500 and whichObject == True):
        fill(255, frameCount - 1100, 0)
    if (frameCount >= 1500):
        fill(255 - (frameCount-1500), 255 - (frameCount-1500), 255 - (frameCount-1500))

    pushMatrix()
    if(frameCount > 590 and frameCount < 690 and whichObject != True):
        rotateZ((-(0.1)*cos((frameCount/2.0))))
    translate(7,18,0)
    rotateZ(3*PI/4)
    scale(2,2,2)
    rotateX(PI/2)
    cylinder()
    popMatrix()
    pushMatrix()
    if(frameCount > 590 and frameCount < 690 and whichObject != True):
        rotateZ((-(0.1)*cos((frameCount/2.0))))
    translate(8.0,19,-0.0)
    sphere(2.1)
    popMatrix()
    pushMatrix()
    translate(-7,18,0)
    rotateZ(PI/4)
    scale(2,2,2)
    rotateX(PI/2)
    cylinder()
    popMatrix()
    pushMatrix()
    translate(-8.0,19,-0.0)
    sphere(2.1)
    popMatrix()
def hands(whichObject, sides = 64):
    pushMatrix()
    if(frameCount > 390 and frameCount < 430 and ! whichObject):
        rotateX(1.5*sin((frameCount-390) / 20.0))
    elif (frameCount >= 430 and ! whichObject):
        rotateX(1.5*sin((430-390) / 20.0))
    elif(frameCount >= 790 and frameCount < 830 and whichObject != True):
        rotateX(1.5*sin((frameCount-390) / 20.0))    
    if(frameCount >= 830 and frameCount < 860 and whichObject == True):
        translate(0,frameCount - 830,0)
    elif(frameCount >=860 and frameCount < 880 and whichObject == True):
        translate(0,860 - 830,0)
    elif(frameCount > 880 and frameCount < 920 and whichObject == True):
        translate(0,0,(frameCount-880) / 2)
    elif(frameCount >=900 and whichObject == True):
        translate(0,0,(920-880)/2)
    if(frameCount > 590 and frameCount < 690 and whichObject != True):
        rotateY((0.5)*cos((frameCount/5.0)))
    translate(10,5,0)

    scale(2,7,2)
    rotateX(PI/2)
    if(whichObject != True):
        fill(78,255,108)
    if (frameCount >= 1500):
        fill(255 - (frameCount-1500), 255 - (frameCount-1500),0)

    cylinder()
    popMatrix()
    pushMatrix()
    translate(-10,5,0)
    scale(2,7,2)
    rotateX(PI/2)
    if (frameCount >=864 and whichObject != True):
        fill(255,0,0)

    cylinder()
    popMatrix()
def eyes(whichObject,sides = 64):
    fill(255,255,255)
    if (frameCount > 690 and whichObject == True):
        fill(frameCount - 690, 0,0)
    if(frameCount > 590 and frameCount < 690 and whichObject != True):
        rotateY(-(2)*cos((frameCount/5.0)))
    if (frameCount >= 1100 and frameCount < 1500 and whichObject == True):
        fill(255, frameCount - 1100, 0)
    if (frameCount >= 1500):
        fill(255 - (frameCount-1500), 255 - (frameCount-1500), 255 - (frameCount-1500))

    pushMatrix()
    translate(6,14,6)
    scale(1.5,1.5,0.5)
    rotateX(-PI/16)
    #rotateX(-PI/8)
    rotateY(PI/8)
    cylinder()
    popMatrix()
    pushMatrix()
    translate(-6,14,6)
    scale(1.5,1.5,0.5)
    rotateX(-PI/16)
    rotateY(-PI/8)
    cylinder()
    popMatrix()
    
def android(whichObject):
    fill (78,255,108)
    if (frameCount > 690 and frameCount < 1100 and whichObject == True):
        fill((frameCount - 690)/2, 27-(frameCount - 690),57-(frameCount - 690))
    elif (frameCount >= 1100 and frameCount < 1500 and whichObject == True):
        fill(255, frameCount - 1100, 0)
    if (frameCount >= 1500):
        fill(255 - (frameCount-1500), 255 - (frameCount-1500), 255 - (frameCount-1500))
        
    pushMatrix()
    translate (0, 0, 0)
    rotateX (80)
    scale (10, 10, 10)
    body(whichObject)
    popMatrix()
    pushMatrix()
    rotateX (80)
    #scale (10, 10, 10)
    translate(00, 0, 10)
    face(whichObject)
    popMatrix()
    fill (75,208,45)
    pushMatrix()
    #rotateX((0.5)*sin((frameCount/10.0)))
    legs(whichObject)
    popMatrix()
    pushMatrix()
    antennas(whichObject)
    popMatrix()
    pushMatrix()
    hands(whichObject)
    popMatrix()
    pushMatrix()
    eyes(whichObject)
    popMatrix()