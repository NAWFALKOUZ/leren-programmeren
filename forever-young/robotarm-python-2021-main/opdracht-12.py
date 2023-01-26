from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 2
        
for i in range(9,0,-1):
    robotArm.grab()
    if robotArm.scan() != "red":
        robotArm.drop() 
        robotArm.moveRight()
    else:
        for c in range(i):
            robotArm.moveRight()
        robotArm.drop()
        for c in range(i-1):
            robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()