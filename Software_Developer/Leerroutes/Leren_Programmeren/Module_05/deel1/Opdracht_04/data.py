def people() -> {}:
    ages = {}
    looping = True
    while looping:
        while not (person := input("Provide the person's name or type stop to stop: ")).isalpha():
            print("Letters only, no spaces.")

        if person.lower() == "stop":
            return ages

        if person not in ages.keys():
            while not (age := input(f"What is the age of {person}? (type stop to stop)")).isdigit():
                if age.lower() == "stop":
                    return ages
                else:
                    print("The age please, this is usually a max 3-digit number.")

            ages[person] = age
        else:
            print("This person is already in the list, try again.")

age = people()

for x in age:
    print(f"{x} is {age[x]} jaar")