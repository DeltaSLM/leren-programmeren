answer = 50
addition = 51
toprint = "50"
while answer < 1000:
    answer += addition #1
    toprint += "+" + str(addition) # 2
    print(toprint, "=", answer) # 3
    addition += 1 # 4