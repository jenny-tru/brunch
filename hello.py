from pip._vendor.distlib.compat import raw_input

print ("It's Brunch Time!! Let me help you find the perfect place!")
name = raw_input("Enter a zip code: ")
date = raw_input("What day would you like to search hours for? ")
color = raw_input("Do you want to also search for bottomless drink deals? ")

print (("We are searching for resturants near %s, on %s, and %s for drink deals.") % (name, date, color))