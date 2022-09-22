cheese_yellow = input("Take one of the below listed cheeses in mind and answer the question; Is the cheese yellow?\ncamembert, Mozzarella, Blue de Rochbaron, Foume d'Ambert, Parmigiano Reggiano, Goudse Kaas, Emmenthaler, Leerdammer.").lower()

if cheese_yellow == "yes":
    cheese_holes = input("Does the cheese contain holes?").lower()

    if cheese_holes == "yes":
        cheese_expensive = input("Is the cheese ridiculously expensive?").lower()

        if cheese_expensive == "yes":
            print("Your cheese is Emmenthaler")
        elif cheese_expensive == "no":
            print("Your cheese is Leerdammer")
        else:
            print("You can only answer using \"yes\" or \"no\".")

    elif cheese_holes == "no":
        cheese_rock = input("Is the cheese hard as a rock?").lower()

        if cheese_rock == "yes":
            print("Your cheese is Parmigiano Reggiano")
        elif cheese_rock == "no":
            print("Your cheese is Goudse kaas")
        else:
            print("You can only answer using \"yes\" or \"no\".")
    else:
        print("You can only answer using \"yes\" or \"no\".")

if cheese_yellow == "no":
    cheese_blue = input("Does the cheese contain blue mold?").lower()

    if cheese_blue == "yes":
        cheese_crust = input("Does the cheese have a crust?").lower()

        if cheese_crust == "yes":
            print("Your cheese is Blue de Rochbaron")
        elif cheese_crust == "no":
            print("Your cheese is Floume d'Ambert")
        else:
            print("You can only answer using \"yes\" or \"no\".")

    elif cheese_blue == "no":
        cheese_crust = input("Does the cheese have a crust?")

        if cheese_crust == "yes":
            print("Your cheese is Camembert")
        elif cheese_crust == "no":
            print("Your cheese is Mozzarrella")
        else:
            print("You can only answer using \"yes\" or \"no\".")

    else:
        print("You can only answer using \"yes\" or \"no\".")

