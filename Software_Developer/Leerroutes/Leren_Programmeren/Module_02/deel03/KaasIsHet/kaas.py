cheese_yellow = input("Take one of the below listed cheeses in mind and answer the question; Is the cheese yellow?\ncamembert, Mozzarella, Blue de Rochbaron, Foume d'Ambert, Parmigiano Reggiano, Goudse Kaas, Emmenthaler, Leerdammer.").lower()

def cheeseIs(variable, cheeseYes, CheeseNo):
    if variable == "yes":
        print(f"Your cheese is {cheeseYes}")
    elif variable == "no":
        print(f"Your cheese is {CheeseNo}")
    else:
        print("You can only answer using \"yes\" or \"no\".")

if cheese_yellow == "yes":
    cheese_holes = input("Does the cheese contain holes?")

    if cheese_holes == "yes":
        cheese_expensive = input("Is the cheese ridiculously expensive?")

        cheeseIs(cheese_expensive, "Emmenthaler", "Leerdammer")

    elif cheese_holes == "no":
        cheese_rock = input("Is the cheese hard as a rock?")

        cheeseIs(cheese_rock, "Parmigiano Reggiano", "Goudse Kaas")

    else:
        print("You can only answer using \"yes\" or \"no\".")

if cheese_yellow == "no":
    cheese_blue = input("Does the cheese contain blue mold?")

    if cheese_blue == "yes":
        cheese_crust = input("Does the cheese have a crust?")

        cheeseIs(cheese_crust, "Blue de Rochbaron", "Foume d'Ambert")

    elif cheese_blue == "no":
        cheese_crust = input("Does the cheese have a crust?")

        cheeseIs(cheese_crust, "Camembert", "Mozzarrella")

    else:
        print("You can only answer using \"yes\" or \"no\".")

