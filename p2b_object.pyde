# I am instancing my Android Object twice on this scence
from androidobject import *
time = 0   # use time to move objects from one frame to the next
def setup():
    size (800, 800, P3D)
    perspective (60 * PI / 180, 1, 0.1, 1000)  # 60 degree field of view
    
    global f
    f = createFont("Arial",20)
    #frameRate(480)

def draw():
    print(frameCount)
    global time
    time += 0.01

    camera (0, -30, 400, 0, 0, 0, 0,  1, 0)  # position the virtual camera
    if (frameCount < 300):
        camera (0, -30, 400 - frameCount, 0, 0, 0, 0,  1, 0)  # position the virtual camera
        #cameraProfile(4)
    elif(frameCount >= 300 and frameCount < 380):
        camera ( - (frameCount - 300), -30, 100, 0, 0, 0, 0,  1, 0)
        if (frameCount > 340):
            camera ( - (frameCount - 300), -30, 100 - (frameCount - 340), 0, 0, 0, 0,  1, 0)
    elif(frameCount >= 380 and frameCount < 480):
        camera ( - (380 - 300), -30, 100 - (380 - 340), 0, 0, 0, 0,  1, 0)
    elif ( frameCount >= 480 and frameCount < 500):
        cameraProfile(1)  # position the virtual camera
    elif(frameCount >= 500 and frameCount < 690):
        cameraProfile(2)
    elif(frameCount >= 690 and frameCount < 720):
        cameraProfile(1)
    elif(frameCount >= 720 and frameCount < 760):
        camera(-80 + (frameCount - 720)/2, -30, 60 - (frameCount - 720)/2, 0, 0, 0, 0,  1, 0)
        print("X Axis", 60 - (frameCount - 720)/2)
    elif(frameCount >= 760 and frameCount < 780):
        cameraProfile(3)
    elif(frameCount >= 780 and frameCount < 880):
        cameraProfile(4)
    elif(frameCount >= 880 and frameCount < 2000):
        cameraProfile(1)
    elif(frameCount >=2000):
        camera (-80 + (frameCount - 2000), -30, 100 - 40, 0, 0, 0, 0,  1, 0)
    background (255, 255, 255)  # clear screen and set background to white
    if(frameCount > 570):
        background((frameCount/10 - 550/10) * 2, (frameCount/3 - 400/3), (frameCount/3 - 500/3) / 2)

    global f
    textFont(f,8) 
    fill(255,0,0)
    if(frameCount>430 and frameCount < 500):
        text("Give me your droids",-30,-30,-10)
    fill(0,255,0)
    if(frameCount>500 and frameCount < 590):
        pushMatrix()
        rotateY(PI/2)
        text("Dance battle?",-30,-30,-40)
        popMatrix()
    fill(255,0,0)
    if(frameCount > 690 and frameCount < 900):
        text("ur just a baby?!",-30,-30,-10)
    fill(255,255,0)
    if(frameCount > 1300 and frameCount < 1600):
        text("when did it all go sour?",-30,-30,-10)
    if (frameCount > 1500):
        background(((1500/10 - 550/10) * 2) - (frameCount-1500), (frameCount/3 - 400/3) - (frameCount-1500), ((1500/3 - 500/3) / 2) - (frameCount-1500))
    # create a directional light source
    #ambientLight(50, 50, 50);
    #lightSpecular(255, 255, 255)
    directionalLight (100, 100, 100, -0.3, 0.5, -1)
    pointLight(200,200,200, 35, 40, 36);
    #spotLight(10, 10, 10, 0, -20, -40, -1, 0, 0, PI/2, 1);
    rotateX(PI)
    rotateY(PI)
   #rotateY(time)
    #rotateZ(time/4)
    #rotateZ(time/6)
    noStroke()
    specular (180, 180, 180)
    shininess (15.0)
    pushMatrix()
    translate(-60,0,0)
    if(frameCount < 390):
        translate(frameCount / 10.0,0,0)
    else:
        translate(390/10.0,0,0)
    rotateY(PI/2)
    android(True)
    popMatrix()
    pushMatrix()
    translate(60,0,0)
    if(frameCount < 390):
        translate(-frameCount / 10.0,0,0)
    else:
        translate(-390/10.0,0,0)
    rotateY(3*PI/2)
    if (frameCount > 880 and frameCount < 1080):
        scale(1- (.01*(frameCount - 880)/2),1- (.01*(frameCount - 880)/2), 1- (.01*(frameCount - 880)/2))
    elif(frameCount>= 1080):
        scale(1- (.01*(1080 - 880)/2),1- (.01*(1080 - 880)/2), 1- (.01*(1080 - 880)/2))
    android(False)
    popMatrix()
    pushMatrix()
    translate(210,-18,-30)
    rotateX(PI/2)
    fill(255,255,255)
    if (frameCount > 1500):
        fill(255 - (frameCount-1500), 255 - (frameCount-1500), 255 - (frameCount-1500))
    for num in range(0,23):
        translate(-20.5,0,0)
        rect(20,20,20,20)
    popMatrix()
# cylinder with radius = 1, z range in [-1,1]

def cameraProfile(num):
    if (num == 1):
        camera (-(380 - 300), -30, 100 - 40, 0, 0, 0, 0,  1, 0)
    elif (num == 2):
        camera ((380 - 300), -30, 100 - 40, 0, 0, 0, 0,  1, 0)
    elif (num == 3):
        camera (-61, -30, 41, 0, 0, 0, 0,  1, 0)
    elif (num == 4):
        camera (-(40), -30, -20, 0, 0, 0, 0,  1, 0)