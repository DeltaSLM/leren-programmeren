from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')
robotArm.speed = 5

# Jouw python instructies zet je vanaf hier:
robotArm.moveRight()

robotArm.grab()

for x in range(6):

    color = robotArm.scan()
    print(color)

    if color == "white":
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveRight()
        robotArm.grab()

    elif color == "red":
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
        robotArm.grab()

else:
    print("No more blocks")

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()