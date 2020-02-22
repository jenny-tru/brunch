from pip._vendor.distlib.compat import raw_input

print ('hello world')
name = raw_input("What is your name? ")
date = raw_input("What is today's date? ")
color = raw_input("What is your favorite color? ")

print (("Hello %s, today's date is %s, and your favorite color is %s.") % (name, date, color))