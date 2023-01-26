from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3

x = 8

robotArm.grab()
for x in range(4):
    for y in range(x):
        robotArm.moveRight()   
    robotArm.drop()
    x = x - 1
    for z in range(x):
        robotArm.moveLeft()
    if x < 3:
        robotArm.grab()
    x = x - 1

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()