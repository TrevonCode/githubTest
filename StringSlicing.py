# slicing = create a substring by extracting elements from another string
#               indexing[] or slice()
#               [start:stop:step]

# example below is for slicing. Important things to know is that you can
# leave blank certain things. Python will assume it's the beginning or end.
# in the below if you leave the start of first name blank it will start at the
# beginning of the name, same for last.

#name = "Trey Hennessey"

#first_name = name[:3]
#last_name = name[5:]
#funky_name = name[::3]
#reversed_name = name[::-1]


#print(last_name)

#   Example of slicing
#   Takes out http:// and .com from the websites

website = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4)

print(website[slice])
print(website2[slice])