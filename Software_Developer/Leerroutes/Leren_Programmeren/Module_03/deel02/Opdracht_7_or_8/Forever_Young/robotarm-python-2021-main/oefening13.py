from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:
rows = 1

while True:
    robotArm.grab()
    block = robotArm.scan()
    print(block)
    if block == "":
        break
    for i in range(rows):
        robotArm.moveRight()
    robotArm.drop()
    for i in range(rows):
        robotArm.moveLeft()
    rows += 1

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()