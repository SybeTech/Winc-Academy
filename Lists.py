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

alphabetical_order = sorted(movies_name)
print (alphabetical_order)

# Write a function won_golden_globe that takes a film name and 
# returns True or False based on whether or not this movie won a Golden Globe.

gold_globe_price = [
"Jaws",
"Star Wars",
"E.T.",
"Memoirs of a Geisha"
]

def won_golden_globe(movies_name):
    if movies_name in gold_globe_price:
        return True
    else:
        return False

print (won_golden_globe("Memoirs of a Geisha"))

# Write a function remove_toto_albums that takes a list of strings, 
# removes Joseph's Toto albums from it and returns the tidy list.

remove_toto_albums= [
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

remove_toto_albums.remove("Fahrenheit")
remove_toto_albums.remove("The Seventh One")
remove_toto_albums.remove("Toto XX")
remove_toto_albums.remove("Falling in Between")
remove_toto_albums.remove("Toto XIV")
remove_toto_albums.remove("Old Is New")
print (remove_toto_albums)
