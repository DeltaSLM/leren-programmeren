from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

# Jouw python instructies zet je vanaf hier:
segment = 8
right = 9

for x in range(5):
    robotArm.grab()
    for i in range(right):
        robotArm.moveRight()
    robotArm.drop()
    right -= 2
    for i in range(segment):
        robotArm.moveLeft()
    segment -= 2

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()