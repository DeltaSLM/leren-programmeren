#firstAnswer = print("Please provide the first letter of your first name").lower()
firstanswer = input("Please provide the letter of your first name").lower()
#secondAnswer = input("Please provide the first letter of your last name").lower()
secondAnswer = input("Please provide the letter of your last name").lower()


firstLetters = [
    "a": "cute",
    "b": "handsome",
    "c": "lovely",
    "d": "fancy",
    "e": "wholesome",
    "f": "beautiful",
    "g": "sexy",
    "h": "amazing",
    "i": "smart",
    "j": "cool",
    "k": "sweet",
    "l": "caring",
    "m": "awesome",
    "n": "fantastic",
    "o": "cold",
    "p": "dark",
    "q": "aggressive",
    "r": "ugly",
    "s": "stupid",
    "t": "idiotic",
    "u": "bitchy",
    "v": "slutty",
    "w": "edgy",
    "x": "emo",
    "y": "lame",
    "z": "lazy"
}

secondLetters == {
    "a": "goblin"
    "b": "alien"
    "c": "ghoul"
    "d": "ghost"
    "e": "Fairy"
    "f": "lame human"
    "g": "wolf"
    "h": "car"
    "i": "hedgehog"
    "j": "Griffin"
    "k": "Kraken"
    "l": "Godzilla"
    "m": "Harambe"
    "n": "Tree"
    "o": "Witch"
    "p": "Wench"
    "q": "Frog"
    "r": "Dragon"
    "s": "Rexouium"
    "t": "plant"
    "u": "horse"
    "v": "Bigfoot"
    "w": "Smallfoot"
    "x": "Loch ness"
    "y": "Dwarf"
    "z": "Banshee"
}

print("Your title is:")
print("firstLetters(firstanswer) + " " + secondLetters[secondAnswer]")
