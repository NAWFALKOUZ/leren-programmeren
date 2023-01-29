from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 2
        
for x in range(9,0,-1):
    robotArm.grab()
    if robotArm.scan() != "red":
        robotArm.drop() 
        robotArm.moveRight()
    else:
        for y in range(x):
            robotArm.moveRight()
        robotArm.drop()
        for z in range(x-1):
            robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()