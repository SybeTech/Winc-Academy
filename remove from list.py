mixed_with_toto_albums= [
"The Towering Inferno",
"Jaws", 
"Midway", 
"Star Wars", 
"Close Encounters of the Third Kind",
"Superman ",
"Indiana Jones", 
"E.T.", 
"Born on the Fourth of July",
"Always",
"Presumed Innocent",
"Memoirs of a Geisha",
"Fahrenheit",
"The Seventh One",
"Toto XX",
"Falling in Between",
"Toto XIV",
"Old Is New"
]

list_toto_albums = [
"Fahrenheit",
"The Seventh One",
"Toto XX",
"Falling in Between",
"Toto XIV",
"Old Is New"
]

def remove_toto_albums(list_toto_albums):
    if "Fahrenheit" in mixed_with_toto_albums:
        mixed_with_toto_albums.remove("Fahrenheit")
    elif "The Seventh One" in mixed_with_toto_albums:
        mixed_with_toto_albums.remove("The Seventh One")
    elif "Toto XX" in mixed_with_toto_albums:
        mixed_with_toto_albums.remove("Toto XX")
    elif "Falling in Between" in mixed_with_toto_albums:
        mixed_with_toto_albums.remove("Falling in Between")
    elif "Toto XIV" in mixed_with_toto_albums:
        mixed_with_toto_albums.remove("Toto XIV")
    elif "Old Is New" in mixed_with_toto_albums:
        mixed_with_toto_albums.remove("Old Is New")
    else: 
        return "Wrong value"

# "Fahrenheit", "The Seventh One","Toto XX","Falling in Between","Toto XIV","Old Is New"

print (remove_toto_albums("Fahrenheit"))
