from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:
rows = 9
while True:
    if rows == 0:
        break
    robotArm.grab()
    color = robotArm.scan()
    if color != "red":
        robotArm.drop()
        robotArm.moveRight()
        rows -= 1
    else:
        for i in range(rows):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(rows-1):
            robotArm.moveLeft()
        rows -= 1

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()