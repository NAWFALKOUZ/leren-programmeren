from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3

x = 1

while robotArm.grab():
    for y in range(x):
        robotArm.moveRight()
    robotArm.drop()
    for z in range(x):
        robotArm.moveLeft()
    x += 1



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()