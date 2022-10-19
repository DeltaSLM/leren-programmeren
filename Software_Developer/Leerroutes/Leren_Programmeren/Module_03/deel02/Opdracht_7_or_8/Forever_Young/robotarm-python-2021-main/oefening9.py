from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

blocks = 1
# Jouw python instructies zet je vanaf hier:
for i in range(4):
    for block in range(blocks):
        robotArm.grab()
        for i in range(5):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(5):
            robotArm.moveLeft()
    robotArm.moveRight()
    blocks += 1

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()