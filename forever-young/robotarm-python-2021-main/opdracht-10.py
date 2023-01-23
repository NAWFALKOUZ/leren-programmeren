from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3

x = 9
for a in range(5):
    robotArm.grab()
    for b in range(x):
        robotArm.moveRight()
    x -= 1
    robotArm.drop()
    for c in range(x):
        robotArm.moveLeft()
    x -= 1


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()