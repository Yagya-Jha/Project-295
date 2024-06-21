from controller import Robot, Keyboard, Motion

timestep=32

robot= Robot()
keyboard = Keyboard()
keyboard.enable(timestep)

wave = Motion('../../motions/wave.motion')
   
def printMessages():
    print('press up to wave')
    print("***I tried incorporating other Motion files as well but they were not made for this robot but were instead made for the Nao robot so they didn't work on this robot***")

key = -1

printMessages()

while robot.step(timestep) != -1:

    key = keyboard.getKey()  
    
    if key == Keyboard.UP:
        wave.play()
   