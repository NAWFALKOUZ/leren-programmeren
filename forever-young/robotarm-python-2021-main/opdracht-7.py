from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 2

for x in range(5):
    for z in range(6):
        robotArm.moveRight()
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
    if x != 4:
        robotArm.moveRight()
        robotArm.moveRight()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()