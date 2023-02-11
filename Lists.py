# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line


# Write a function alphabetical_order that takes one argument: a list of strings that represent film names. 
# It returns a list of the same films in alphabetical order.

movies_name = [
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
"Memoirs of a Geisha"
]

def alphabetical_order(movies_name):
    return sorted(movies_name)

print (alphabetical_order(movies_name))

# Write a function won_golden_globe that takes a film name and 
# returns True or False based on whether or not this movie won a Golden Globe.
# gold globe prices "Jaws", "Star Wars", "E.T.", "Memoirs of a Geisha".

def won_golden_globe(movies_name):
    if ("Jaws").lower() in movies_name.lower():
        return True
    if "Star Wars".lower() in movies_name.lower():
        return True
    if "E.T.".lower() in movies_name.lower():
        return True
    if  "Memoirs of a Geisha".lower() in movies_name.lower():
        return True
    else:
        return False

print (won_golden_globe("jaws"))

# Write a function remove_toto_albums that takes a list of strings, 
# removes Joseph's Toto albums from it and returns the tidy list.

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

def remove_toto_albums (mixed_with_toto_albums):
    if "Fahrenheit" in mixed_with_toto_albums:
        mixed_with_toto_albums.remove("Fahrenheit")
    if "The Seventh One" in mixed_with_toto_albums:
        mixed_with_toto_albums.remove("The Seventh One")
    if "Toto XX" in mixed_with_toto_albums:
        mixed_with_toto_albums.remove("Toto XX")
    if "Falling in Between" in mixed_with_toto_albums:
        mixed_with_toto_albums.remove("Falling in Between")
    if "Toto XIV" in mixed_with_toto_albums:
        mixed_with_toto_albums.remove("Toto XIV")
    if "Old Is New" in mixed_with_toto_albums:
        mixed_with_toto_albums.remove("Old Is New")
        return mixed_with_toto_albums
    else: 
        "Wrong input"

print(remove_toto_albums(mixed_with_toto_albums))
