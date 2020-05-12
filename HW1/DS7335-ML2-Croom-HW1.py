#******************************************************************
# DS 7337 - Machine Learning 2
# Author: Brandon Croom
# Assignment: Homework 1
# Date: 5/13/2020
#******************************************************************

# Part 1:
# Fill in an explanation of the functions below and an example of how to use it

#Lists
#******************************************************************

# append() - the append method adds an element to a list
# example:
fruits = ['pear','kiwi','grapes']
fruits.append("apple")
print(fruits)

# extend() - the extend method adds the specified list items to the end of the current list
veggies = ['tomatoes','lettuce','beans']
fruits.extend(veggies)
print(fruits)

# index() - the index method returns the position in a list of the first 
# occurrence of the speficied value. In order to use the index method the value or integer must be
# supplied as an argument. Calling the index method without parameters results in a type error. The 
# sample code below will show this type error and denote that a parameter is missing 
print(fruits.index())

# index(value, integer) - the index method returns the position in a list of the first 
# occurrence of the speficied value. In order to use the index method the value or integer must be
# supplied as an argument. 
# The code below will look for the entry "Lettuce" in the list and return that the entry is at index 5
print(fruits.index('lettuce'))

# insert() - the insert method inserts the specified value at the index position specified
# In the example below we will insert "broccoli" at index value 5
fruits.insert(5,"broccoli")
# Show that broccoli has been inserted into the list
print(fruits)
# Confirm broccoli has been inserted at position 5 in the list
print(fruits.index("broccoli"))

# remove() - the remove method removes the first occurrence of the element with the value specified
# Since we don't like broccoli lets remove it from our list
fruits.remove("broccoli")
# Confirm brocolli has been removed from the list
print(fruits)

# pop() - the pop method removed an element from the list. When no position is specified at during 
# method execution the optional pos parameter is defaulted to -1, which will return the last item 
# in the list
# Using pop() on our fruits list will remove beans. We'll pop off beans into the popval variable 
# for confirmation
popval = fruits.pop()
print(popval)
print(fruits)

# pop(0) - the pop method removed an element from the list. Using zero as the pos paramter will pop 
# off the first item in the list
# Using pop(0) on our fruits list will remove pear from the list
popval = fruits.pop(0)
print(popval)
print(fruits)

# count() - the count method returns the number of elements in a list with the specified value
# Using count on our fruits list to look for kiwi should result in a count of 1 since there is only 1
# reference to kiwi in the list
print(fruits.count("kiwi"))

# reverse() - the reverse method reverses the order of the list making the last item the first and
# the first item the last
# Using the fruits list we'll print off the original list and then print off the reverse list
print(fruits)
fruits.reverse()
print(fruits)

# sort() the sort method sorts the data in the list. By default it will sort the list ascenting. 
# Optional parameters may be specified to change the sorting criteria or to specify a function for 
# other sorting criteria
# Using our fruit list we'll print off the original list and the print off the sorted list
print(fruits)
fruits.sort()
print(fruits)

# [1] + [1] - using the + operator on lists concatenates two lists and returns a new list. 
# Using the example [1] + [1] we would get a new list containing [1,1]
print([1] + [1])

# Using the example [1,3] + [2] we would get a new list containing [1,3,2]
print([1,3] + [2])

# [2] * [2] - using the * operator on lists repeats the list the speficied number of times.
# Using the example above, we're attempting to multiply two lists which results in an error. However, 
# we can modify that example a repeat the list twice
print([2] * 2) 

#Using another example we can repeat the list 5 times
print([1,4] * 5)

# [1,2][1:] - this provided statement we are indexing into the list [1,2] using the index operator [1:]
# This index operator tells us to index from position 1 to the end of the list. Index operators can be 
# used to slice lists or strings in various ways. In the case of the provided example we'll return 
# the value 2
print([1,2][1:])

# Using another example we can request the list from the beginning to position 4. This will return 
# [1,2,3,4] for the example
print([1,2,3,4,5,6,7,8][:4])

# [x for x in [2,3]] - this provided statement is a loop through a list. It will output all values in 
# the list. In this specific statment our result will be [2,3]
print([x for x in [2,3]])

# Using another example we can interate through a longer list. In thie example we'll get the values
# list contain 1-8
print([x for x in [1,2,3,4,5,6,7,8]])

# [x for x in [1,2] if x ==1] - this provided statement iterates through the items in the list and only
# returns a value if the value of x is equal to 1. 
print([x for x in [1,2] if x ==1])

# Using another example we can iterate through a longer list and look for a differnet value. 
# We'll return [6]
print([x for x in [1,2,3,4,5,6,7,8] if x == 6])

# [y*2 for x in [[1,2],[3,4]] for y in x] - this provided statement contains two loops. The outer 
# loop iterates through the specified lists. Each list value in the second loop is returned to the y
# variable and then multiplied by 2. This code results in a new list of [2,4,6,8], which is a combining
# of the two lists specified in the outer loop and those values multiplied by 2
print([y*2 for x in [[1,2],[3,4]] for y in x])

# Using another example we can iterate through other lists and multiply by 3
print([y*3 for x in [[3,6],[9,12]] for y in x])

#Tuples
#********************************************************************

# count() - This method returns the number of times a specified value appears in a tuple
#Using the following as an example, we'll build a tuple
fasttuple = ("ferrari","maserati","audi","ferrari","tesla","bugati")

#now let's count how many ferrari's we have in our tuple'
fcount = fasttuple.count("ferrari")

#we should have 2 ferraris
print(fcount)

# index() - This method finds the first occurence of the specified value and returngs the index. 
# If the value is not found the method does raise an exception

# Using the tuple above let's look for audi. It should be at index 2
print(fasttuple.index("audi"))

# build a dictionary from tuples
# First lets define a new tuple for direction
directiontuple = [("North","N"),("East","E"),("South","S"),("West","W")]

# let's define a quick function to do the conversion
def ConvertTupToDict(theTuple, theDict):
    theDict = dict(theTuple)
    return theDict

# define an empty dictionary
dictionary = {}

# Print out the dictionary. We should get the following result
# ['North':'N', 'East':'E', 'South':'S', 'West':'W']
print(ConvertTupToDict(directiontuple,dictionary))

# unpack tuples - unpacking a tuple lets us get to individual values easier
# Let's upack our fast tuple from above
(car1,car2,car3,car4,car5,car6) = fasttuple

# print the original tuple
print(fasttuple)

# print the upacked values:
print(car1," ",car2," ",car3," ",car4," ",car5," ",car6)

#Dicts
#********************************************************************************

# a_dict = {'I hate':'you', 'You should':’leave’} - The provided statement here defines a dictionary. 
# A dictionary has key-value pairs. Dictionaries are unordered, changeable and indexed. 
# Dictionaries are define with curly braces
a_dict = {'I hate':'you', 'You should':'leave'}
print(a_dict)

# Another example of a dictionary is:
b_dict = {'North':'N', 'East': 'E', 'South':'S', 'West':'W'}
print(b_dict)

# values() - this method returns a view object that contains all of the values of the dictionary, 
# not the keys, in a list.
# Using b_dict from above we'll get the values and print them
direct_vals = b_dict.values()

print(direct_vals)

# keys() - this method returns a view object that contains all of the keys of the dictionary, 
# not their values, in a list
# Using b_dict from above we'll get the keys and print them
direct_keys = b_dict.keys()

print(direct_keys)

# items() - this method returns a view object that contains the key-value pairs from the dictionary. 
# These values are returned as a list of tuples
# Using b_dict from above we'll get the values and print them
direct_items = b_dict.items()

print(direct_items)

# has_key() - this method was originally in earlier versions of python, it is no longer in python 3. 
# The intent of this method is to provide a boolen value to determine if a key exists in a dictionary.
# The replacement for this function in Python 3 is the 'in' operator.
# Below is what sample code would look like. Since it's invalid it's commented out as in Python 3 
# dictionaries no longer have this attribute 

#print(b_dict.has_key("North"))

# 'never' in a_dict - this provided statement is the Python 3 approved method of determining if a key
# is in a dictionary or not. It will return a true/false result based on finding the ke
#Using b_dict from above we'll look for an existing key and a non existing key
print('North' in b_dict)
print('NorthEast' in b_dict)

# del a_dict['me'] - the provided statement demonstrates a way to inplace delete a key. 
# If an attempt is made to delete a non-existent key than an exception is raised
# Using b_dict from above we'll delete the North key

# Show the initial dictionary
print(b_dict)
# Delete the key
del b_dict['North']
# Show the deleted key
print (b_dict)

# a_dict.clear() - the clear() method removes all elements from the dictionary
# Using b_dict we'll clear out the dictionary

# Show the initial dictionary
print(b_dict)
# Clear the dictionary
b_dict.clear()
# Show the deleted key
print (b_dict)

# Sets
#*******************************************************************************

#Define some sets to get started
setA = {"banana", "apple", "pear", "grape","kiwi"}
setB = {"lettuce","tomato","cucumber","broccoli","onion"}

# add() - The add method adds the specified element to the set. If the element already exists is 
# does not get added
# Using setA above let's add orange and apple. We'll add apple to show no duplication
print(setA)
setA.add("orange")
print(setA)
setA.add("apple")
print(setA)

# clear() - The clear method removes all elements from the set
# Using setA above print out the set, clear it then show it's cleared
print(setA)
setA.clear()
print(setA)

# rebuild setA for later use
setA = {"banana", "apple", "pear", "grape","kiwi"}

# copy() - The copy method copies the set into a new variable
# Using setA we'll copy into a new set, then print both sets to show they're the same
setACopy = setA.copy()
print(setA)
print(setACopy)

# difference() - The difference method returns a new set containing the difference between two 
# or more sets.
# Define a new set to show difference
setC = {"apple","amazon","best buy"}

diffVals = setA.difference(setC)
# set should contain kiwi, pear, banana and grape. Apple is common between both sets
print(diffVals)

# difference_update() - The difference method updates the existing set to remove elements that exist
# in both sets
# Using setA and setC 
setA.difference_update(setC)
# set should contain kiwi, pear, banana and grape. Apple is common between both sets and is removed
print(setA)

# reset setA back to the original
setA = setACopy.copy()

# discard() - The discard method removes a specified items from the set
# Using setA, remove apple
setA.discard("apple")
print(setA)

# reset setA back to the original
setA = setACopy.copy()

# intersection() - The intersection method returns a new set that contains only items that are the same in
# two or more 
# Define a new set to show intersection
setC = {"apple","amazon","best buy"}

#Determine the intersection of setA and setC
intersect = setA.intersection(setC)

#The result should be apple, since it exists in both setA and setC
print(intersect)

# intersection_update() - The intersection method updates the existing set to contain only items that exist in 
# all set specified
# Define a new set to show intersection
setC = {"apple","amazon","best buy"}

#Determine the intersection of setA and setC
setA.intersection_update(setC)

#The result should be apple, since it exists in both setA and setC
print(setA)

# reset setA back to the original
setA = setACopy.copy()

# isdisjoint() - The isdisjoint method returns a boolean value of True if none of the items are present 
# in both sets, otherwise false is returned

# Using setA, setB and setC let's test disjointedness
# This should result in false
print(setA.isdisjoint(setC))
# this should result in true
print(setA.isdisjoint(setB))
# this should result in true
print(setB.isdisjoint(setC))

# issubset() - The issubset method returns true if all items in the set exist in the specified set, 
# otherwise false is returned
# Define a new set
setD = {"cucumber","onion"}

# determine if setD is a subset of setB or setA
# this should result in true
print(setD.issubset(setB))
# this should result in false
print(setD.issubset(setA))

# issuperset() - The issuperset method returns true is all items in the set exist in the original set, 
# otherwise false is returned

# determine if setB is a superset of setD or setC
# this should return true
print(setB.issuperset(setD))
# this should return false
print(setB.issuperset(setC))

# pop() - The pop method removes a random items from the set and returns that value
#Using setC, print out the original set, pop of a value then display the set and popped value.
print(setC)
popval = setC.pop()
print(setC)
print(popval)

# remove() - The remove method removes the specified element from the set. If the element does not
# exist the method will raise an error unlike the discard methot
# Using setA remove apple - show the initial set, remove apple then show the update
print(setA)
setA.remove("apple")
print(setA)

#rebuild setA
setA = setACopy.copy()

# symmetric_difference() - The semmetric_difference method returns a new set that contains all items
# from both sets but not those items that are present in both sets.
# Using setA and setC, print both sets, find the symmetric difference then print it
print(setA)
print(setC)
symdiff = setA.symmetric_difference(setC)
print(symdiff)

# symmetric_difference_update() - The semmetric_difference method returns a updated set that contains all items
# from both sets but not those items that are present in both sets.
# Using setA and setC, print both sets, find the symmetric difference then print it
print(setA)
print(setC)
setA.symmetric_difference(setC)
print(setA)

#rebuild setA
setA = setACopy.copy()

# union() - The union method returns a new set that contains all items from an original set 
# and all sets specified. Multiple sets can be unioned together
# Using setA, setB and setC let's union those together
print(setA.union(setB,setC))
# print setA to show it is unchanged
print(setA)

# update() - The update method updates the specified set by adding items from another set
# Using setA and setB let's update the two
# show the original setA
print(setA)
# add setB into set A
setA.update(setB)
# show the additions to setA
print(setA)

# Strings
#*************************************************************************************
#Define a few text strings
str1 = "welcome to machine learning 2"
str2 = "This Homework is Really Long"
str3 = "THIS IS AN UPPERCASE STRING"

#Get the list of functions
dir(str1)

# capitalize() - The capitalize method returns a string where the first character is uppercase.
# Using str1 above, print the original, capitalize it, and print the updated string
print(str1)
newstr1 = str1.capitalize()
print(newstr1)

# casefold() - The casefold method returns a string where all characters are lowercase. It is 
# similar to the lower method but will convert more characters
# Using str2 above, print the original, casefold it, and print the updated string
print(str2)
newstr2 = str2.casefold()
print(newstr2)

# center() - The center method will align the string using a specified character (default space) 
# as the fill character
# Using str1, fill 50 spaces with asteriks(*)
fillstr1 = str1.center(50,"*")
print(fillstr1)

# count() - The count() method returns a specified value appears in the string
# Using str 1, count the number of times 'learning' is in the string (should be 1 time)
countstr1 = str1.count("learning")
print(countstr1)

# encode() - The encode() method encodes the string using the specified encoding type. The default 
# encoding is UTF-8
# Using str1, encode and print the encoded string
encodestr1 = str1.encode()
print(encodestr1)

# endswith() - The endswith() method returns true if the string ends with the specified value, 
# or false if not
# Using str1, check for a period, should return false
endsstr1 = str1.endswith(".")
print(endsstr1)

# expandtabs() - The expandtabs() method sets the tab size to the specified number of whitespaces
# Define a new string with tabs
str3 = "H\te\tl\tp"
print(str3)
etabsstr3 = str3.expandtabs(2)
print(etabsstr3)

# find() - The find() method finds the first occurrence of the specified value. 
# It returns -1 if the value is not found and does not raise an exception like the index method
# Using str1, find machine, it should start at index 11
findstr1 = str1.find("machine")
print(findstr1)

# format() - The format() method formats the specified values nd inseters them into the string's 
# placeholder
# Define a new string with formatting placeholder
str4 = "The Low Low price of ${price:.2f}"
print(str4.format(price=9.99))

# index() - The index() method is similar to the find() method in that is finds the first occurrence
# of the specified value. It will raise an exception if the value is not found and does not return a 
# -1 as find does in this case
findstr1 = str1.index("machine")
print(findstr1)

# isalnum() - The isalnum() method returns true if all characters are alphanumeric
# Using str1, determine if the string is alphanumeric, should return false due to spaces
alphastr = str1.isalnum()
print(alphastr)

# isalpha() - The isalpha() method returns true is all characters are in the alphabet (a-z). Spaces
# and punctuation will result in false as will numeric values
# Using str1, determine if the string is alphanumeric, should return false due to spaces
alphastr = str1.isalpha()
print(alphastr)

# isdecimal() - The isdecimal() method returns true if all characters in the string are decimals
# Using str1, determine if the string is decimal, should return false
decimalstr = str1.isdecimal()
print(decimalstr)

# isdigit() - The isdigit() method returns true if all characters in the string are digits
# Using str1, determine if the string is digit, should return false
digitstr = str1.isdigit()
print(digitstr)

# isidentifier() - The isidentifier() method returns true if the string matches the valid identifier
# construct of only alphanumeric letters or underscores
# Using str1, determine if the string is identifier, should return false
identstr = str1.isidentifier()
print(identstr)

# islower() - The islower() method returns true if the string is all lowercase
# Using str1, determine if the string is digit, should return true
lowerstr = str1.islower()
print(lowerstr)

# isnumeric() - The isnumeric() method returns true if all characters are numeric
# Using str1, determine if the string is digit, should return false
numstr = str1.isnumeric()
print(numstr)

# isprintable() - The isprintable() method returns true if all the characters are printable. CRLF are
# considered non-printable and return false
# Using str1, determine if the string is digit, should return true
printstr = str1.isprintable()
print(printstr)

# isspace() - The isspace() method returns true is all characters in the string are whitespace characters
# Using str1, determine if the string is digit, should return false
print(str1.isspace())

# istitle() - The istitle() method returns true if all words in a text start with an uppercase letter and the
# remainder of the word are lowercase letters
# Using str1, determine if the string is digit, should return false
print(str1.istitle())

# isupper() - The isupper() method returns true if all the characters in the string are uppercase
# Using str1, determine if the string is digit, should return false. Test with an uppercase string 
# for true, using str3
print(str1.isupper())
print(str3.isupper())

# join() - The join() method joins all items in a tuple into in a string separated by a specified 
# hash character
# Define a tuple, and then join based on the "#" character, print out the result
newTuple = ("Apple","Annie","Pretzels")
result = "#".join(newTuple)
print("#".join(newTuple))

# ljust() - The ljust() method returns a left justified version of the string. 
# The length of the returned string is a required parameter. The fill character may also be specified, 
# if it is not specified a space is used
# Using str1, determine if the string is digit, display left justified string and fill 
# remaining spaces with a hash mark "#"
print(str1.ljust(len(str1) + 10,"#"))

# lower() - The lower() method returns a string that is all lowercase
# Using str3 display the string in lowercase
print(str3.lower())

# lstrip() - The lstrip() method returns a left trimmed version of the string
# Define a new string with spacing on both the left and right. The result should be a left trimmed string
print("     A New String     ".lstrip())

# partition() - The partition() method takes a search word as a parameter. It returns a three part tuple
# The tuple contains: everything before the match, the match, and everything after the match
# Using str2, find "Homework" and return the tuple of ("This", "Homework", "is Really Long")
print(str2.partition("Homework"))

# replace() - The replace() method takes three parameters the "oldvalue" (what's being replaced),
# the "newvalue" (the value for replacement), and an optional count value for how many replacements 
# to perform. If no count value is specified only one replacement is performed
# Using str2, replace "Really" with "Extremely"
print(str2.replace("Really","Extremly"))

# rfind() - The rfind() method takes three parameters. A value to search for, an optional start position
# and an option end position. Defaults for the optional values are to start at the beginning of the string
# to the end of the string. If the search value is found the method returns the start position. If the
# search value is not found the method returns -1
# Using str2, find where Homework (position 5) and homework (-1) starts in the sentence
print(str2.rfind("Homework"))
print(str2.rfind("homework"))

# rindex() - The rindex() method takes three parameters. A value to search for, an optional start position
# and an option end position. Defaults for the optional values are to start at the beginning of the string
# to the end of the string. If the search value is found the method returns the start position. If the
# search value is not found the method raises an exception
# Using str2, find where Homework (position 5) starts in the sentence
print(str2.rindex("Homework"))

# rjust() - The rjust() method returns a right justified version of the string. As with ljust(), it has two
# parameters: length which is required and is the length of the returned string, character which is
# optional which fills in the missing spaces. This value default to space if not specified
# Using str2, right justify to 50 and fill in the remaining characters with '!'. Should result in the 
# string "!!!!!!!!!!!!!!!!!!!!!!This Homework is Really Long"
print(str2.rjust(50,"!"))

# rpartition() - The rpartition() method searchs for the last occurrence of a specfied string. It then
# returns a tuple that contains three elements: everything before the match, the match, everything 
# after the match
# Using str2, search for "is", returns a tuple of ('This Homework','is','Really Long')
print(str2.rpartition("is"))

# rsplit() - The rsplit() method splits the string at the specified separator and returns a list of
# occurrences. There is also a maxsplit, optional paramter, that can be used to specify how many splits
# to perform. The default is -1, which means "all occurrences"
# Using str2, split on " ", returns a list of ['This', 'Homework','is','Really', 'Long']
print(str2.rsplit(" "))

# rstrip() - The rstrip() method removes any trailing characters at the end of the string. The default,
# trailing character to look for is a space
# Define a new string with spacing on both the left and right. The result should be a 
# right trimmed string, "     A New String"
print("     A New String     ".rstrip())

# split() - The split() method splits the string into a list based on the specified character to split
# on. The method also contains a parameter that allows for the number of splits to perform. It defaults
# to -1, which is "all occurrences"
# Using str2, split on " ", returns a list of ['This', 'Homework','is','Really', 'Long']
print(str2.split(" "))

# splitlines() - The splitlines() method splits a string into a list. The string is split based on
# on line breaks
# Using str2 and str1, concatenate with a like break, then split. Results:
# ['welcome to machine learning 2','THIS IS AN UPPERCASE STRING']
strCombo = str1 + "\n" + str3
print(strCombo.splitlines())

# startswith() - The startswith() method returns true if the string starts with the specified value,
# otherwise False
# Using str2, see if the string starts with "welcome" (result is True) or "Welcome" (result is False)
print(str1.startswith("welcome"))
print(str1.startswith("Welcome"))

# strip() - The strip() method returns a string with all leading and trailing spaces trimmed. The
# character to remove is space, but other characters can be specified
# Define a new string with spacing on both the left and right. The result should be a 
# trimmed string, "A New String"
print("     A New String     ".strip())

# swapcase() - The swapcase() method returns a string where the case of the characters is swapped. 
# Uppercase characters become lowercase and lowercase characters become uppercase
# Using str1 and str2, show that str1, which is all lowercase, becomes uppercase and that str2, 
# which is mixed case , becomes mixed case
print(str1.swapcase())
print(str2.swapcase())

# title() - The title() method converts the first chatacter of each word in the string to upper case
# Using str1, which is all lowercase, we should see the case changed to title case. Using str2, 
# we should see no change as it is already in title case
print(str1.title())
print(str2.title())

# upper() - The upper() method converts a string to upper case
# Using str1 we should see the string go to all uppercase
print(str1.upper())

# zfill() - The zfill() method adds zeros to the beginning of the string based on the length specified
# to the method call.If the length is less than the string no filling is performed
# Using str1 zfill with 10 zeroes
print(str1.zfill(len(str1) + 10))

# from collections import Counter
#*******************************************************************************
# load the counter library
from collections import Counter

# initialize a counter object so we can run dir() on it to get methods
c = Counter(a=5,b=1,c=10)
fillCounter = Counter(['knights','dragons','castle'])
dir(c)

# clear() - The clear() method resets all counts in the counter. 
# It will remove all items from the counter object
# Use the fillCounter, defined above, to show the counts for all values, then clear the counts. 
# This should result in an empty counter object
print(fillCounter)
fillCounter.clear()
print(fillCounter)

#refill the counter for later
fillCounter = Counter(['knights','dragons','castle'])

# copy() - The copy method will create an independent copy of the counter 
# Use the fillCounter object, create a copy in fillCntr2 and show they are the same
fillCntr2 = fillCounter.copy()
print(fillCounter)
print(fillCntr2)

# elements() - The elements() method returns a list over the elements. Each element is repeated as 
# many times as its count. The returned list is ordered based on first occurrence. 
# Use the c counter object, display the elements in sorted order
print(sorted(c.elements()))

# fromkeys() - The fromkeys() method is currently not implemented for Counter objects, but is listed
# as it is part of the usual dictionary methods

# get() - The get() method returns the count of the specified value as it exists in the counter object
# Using fillCounter, display the counter value for "knights", this should be 1
print(fillCounter.get("knights"))

# items() - The items() method returns a listing of all of the items (keys and values) within the counter
# Using fillCounter, display the list of items,
# should return ([('knights',1),('dragons',1),('castle',1)])
print(fillCounter.items())

# keys() - The keys() method returns a listing of all of the keys within the counter
# Using fillCounter, display the list of keys, should return (['knights,'dragons,'castle])
print(fillCounter.keys())

# most_common() - The most_common() method returns the most common elements from the counter. The 
# method takes an optional parameter specifying the number of entries to return. If not specified it
# will return the sorted dictionary from most common to least common
# Using the c counter, display the most common items, Results in [('c', 10), ('a', 5), ('b', 1)]
print(c.most_common())

# subtract() - The subtract() method subtracts element counts. It does allow for negative subtraction
# Define new counters, subtract them and show the results. Should result in 
# ({'c': 24, 'a': 5, 'b': 3})
cnt1 = Counter(a=10,b=5,c=22)
cnt2 = Counter(a=5, b=2,c=-2)
cnt1.subtract(cnt2)
print(cnt1)

# update() - The update() method adds element counts
# Define new counters, update them and show the results. Should result in 
# ({'c': 20, 'a': 15, 'b': 7})
cnt1 = Counter(a=10,b=5,c=22)
cnt2 = Counter(a=5, b=2,c=-2)
cnt1.update(cnt2)
print(cnt1)

# values() - The values() method returns the values for a given counter
# Using fillCounter and cnt2 , display the values, fillCounter = ([1, 1, 1])
# cnt2 = ([5, 2, -2])
print(fillCounter.values())
print(cnt2.values())

# BONUS: from itertools import*
#****************************************************************************
# Itertools provides high speed tools for efficient looping. 
from itertools import*

# list the methods available in the package
dir(itertools)

# accumulate() - The accumulate() method is an iterator that returns sums or accumulated
# results of binary operators. It takes an iterable value as a required parameter, and an optional
# function specification to specific how to accumulate the sum. The default is to add, but other 
# operators or lambda functions may be provided. 
# Using the example below we'll define a dataset and return both an added list and a max value list
data = [5,6,7,20,8,9]
#add the list values, result is [5, 11, 18, 38, 46, 55]
print(list(accumulate(data)))

# find the max in the list values, result in [5, 6, 7, 20, 20, 20]
print(list(accumulate(data, max)))

# chain() - The chain() method returns from the first iterable list until all values are exhaused and then
# proceeds to the next iterable until all the iterables are exhausted. The result is a single sequence
# of all the values in the iterable
# Example below, results in ['S', 'M', 'U', 'M', 'S', 'D', 'S', 'R', 'o', 'c', 'k', 's']
print(list(chain("SMU","MSDS","Rocks")))

# combinations() - The combinations() method will return subsequences based on the parameter value r
# specified from the iterable. Combinations are emitted in lexicographical order and thus sorted lists
# will return sorted. If the input values are unique there will be no repeat combinations
# Example below, results in [('A', 'B'), ('A', 'E'), ('A', 'F'), ('B', 'E'), ('B', 'F'), ('E', 'F')]
print(list(combinations("ABEF",2)))

# combinations_with_replacement() - The combinations_with_replacement() method will return subsequences based on the parameter value r
# specified from the iterable. Combinations are emitted in lexicographical order and thus sorted lists
# will return sorted. This method allows for repeat combinations
# Example below, results in [('A', 'A'), ('A', 'B'), ('A', 'E'), ('A', 'F'), ('B', 'B'), ('B', 'E'), ('B', 'F'), ('E', 'E'), ('E', 'F'), ('F', 'F')]
print(list(combinations_with_replacement("ABEF",2)))

# compress() - The compress() method filters elements from the data parameter returning only those
# values that have a corresponding element in the selectors parameter that evaluates to true. The
# process stops when either the data or the selectors iterable has been exhausted
# Example below, results in ['H', 'E', 'L', 'L', 'O']
print(list(compress("HAEOLELAO",[1,0,1,0,1,0,1,0,1])))

# count() - The count() method returns evenly spaced values beginning with the start parameter and
# increasing based on the step parameter specified
# Example below, results equivalent to 1 2 3 4 5
count(5,1) 

# cycle() - The cycle() method returns elements from the iterable, saving a copy of each. Once the 
# initial iterable is exhausted, the method returns elements from the saved copy, repeating indefinitely
# Example below, results equivalent to 'B C D B C D B C D...'
cycle('BCD')

# permutations() - The permutations() method returns the permutations based on the length specified
# to the optional parameter r. If r is not specified the method returns all possible full-length permutations
# Example below, results in [('B', 'A'), ('B', 'A'), ('B', 'D'), ('B', 'F'), ('A', 'B'), ('A', 'A'),
#  ('A', 'D'), ('A', 'F'), ('A', 'B'), ('A', 'A'), ('A', 'D'), ('A', 'F'), ('D', 'B'), ('D', 'A'), 
# ('D', 'A'), ('D', 'F'), ('F', 'B'), ('F', 'A'), ('F', 'A'), ('F', 'D')]
print(list(permutations("BAADF",2)))


# Part 2 - Question 1
# ***************************************************************************
# Using the flower_orders definition below answer the following questions:
# 1. Build a counter object and and use counter and confirm they have the same values.
# 2. Count how many objects have color W in them.
# 3. Make histogram of colors
# 4. Rank the tuples of color pairs regardless of how many colors in order.
# 5. Rank the triples of color pairs regardless of how many colors in order.
# 6. Make dictionary of where keys are a color and values are what colors go with it
# 7. Make a graph showing the probability of having an edge between two colors based on how
#    often they co-occur. (a numpy square matrix)
# 8. Make 10 business questions related to the questions we asked above.

flower_orders=[ 'W/R/B' , 'W/R/B' , 'W/R/B' , 'W/R/B' , 'W/R/B' , 'W/R/B' , 'W/R/B' , 
               'W/R/B' , 'W/R/B' , 'W/R/B' , 'W/R/B' , 'W/R/B' , 'W/R/B' , 'W/R/B' , 'W/R/B' , 
               'W/R/B' , 'W/R/B', 'W/R/B' , 'W/R/B' , 'W/R/B' , 'W/R/B' , 'W/R/B' , 'W/R/B' , 
               'W/R/B' , 'W/R/B' , 'W/R/B' , 'W/R/B' , 'W/R/B' , 'W/R/B' , 'W/R/B' , 'W/R' , 
               'W/R' , 'W/R' , 'W/R' , 'W/R' , 'W/R' , 'W/R' , 'W/R' , 'W/R' , 'W/R' , 'W/R' , 
               'W/R' , 'W/R' , 'W/R' , 'W/R' , 'W/R' , 'R/V/Y' , 'R/V/Y' , 'R/V/Y' ,
               'R/V/Y' , 'R/V/Y' , 'R/V/Y' , 'R/V/Y' , 'R/V/Y' , 'R/V/Y' , 'R/V/Y' , 'W/R/V' , 
               'W/R/V' , 'W/R/V' , 'W/R/V' , 'W/R/V' , 'W/R/V' , 'W/R/V' , 'W/R/V' , 'W/R/V' , 
               'W/R/V' , 'W/N/R/V' , 'W/N/R/V' , 'W/N/R/V' , 'W/N/R/V' , 'W/N/R/V' , 'W/N/R/V' , 
               'W/N/R/V' , 'W/N/R/V' , 'W/R/B/Y', 'W/R/B/Y' , 'W/R/B/Y' , 'W/R/B/Y' , 'W/R/B/Y' ,
               'W/R/B/Y' , 'B/Y' , 'B/Y' , 'B/Y' , 'B/Y' ,'B/Y' , 'R/B/Y' , 'R/B/Y' , 'R/B/Y' , 
               'R/B/Y' , 'R/B/Y' , 'W/N/R/B/V/Y' , 'W/N/R/B/V/Y' , 'W/N/R/B/V/Y' , 'W/N/R/B/V/Y' , 
               'W/N/R/B/V/Y' , 'W/G' , 'W/G' , 'W/G' , 'W/G' , 'R/Y' , 'R/Y' , 'R/Y' , 'R/Y' ,
               'N/R/V/Y' , 'N/R/V/Y' , 'N/R/V/Y' , 'N/R/V/Y' , 'W/R/B/V' , 'W/R/B/V' , 'W/R/B/V' , 
               'W/R/B/V' , 'W/N/R/V/Y' , 'W/N/R/V/Y' , 'W/N/R/V/Y' , 'W/N/R/V/Y' , 'N/R/Y' ,
               'N/R/Y' , 'N/R/Y' , 'W/V/O' , 'W/V/O' , 'W/V/O' , 'W/N/R/Y' , 'W/N/R/Y' , 'W/N/R/Y' , 
               'R/B/V/Y' , 'R/B/V/Y' , 'R/B/V/Y' , 'W/R/V/Y' , 'W/R/V/Y' , 'W/R/V/Y' , 'W/R/B/V/Y' , 
               'W/R/B/V/Y' , 'W/R/B/V/Y' , 'W/N/R/B/Y' , 'W/N/R/B/Y' , 'W/N/R/B/Y' , 'R/G' , 'R/G' , 
               'B/V/Y' , 'B/V/Y' , 'N/B/Y' , 'N/B/Y' , 'W/B/Y' , 'W/B/Y' , 'W/N/B' , 'W/N/B' , 
               'W/N/R' , 'W/N/R' , 'W/N/B/Y' , 'W/N/B/Y' , 'W/B/V/Y' , 'W/B/V/Y' , 
               'W/N/R/B/V/Y/G/M' , 'W/N/R/B/V/Y/G/M' , 'B/R', 'N/R' , 'V/Y' , 'V' , 'N/R/V' , 
               'N/V/Y' , 'R/B/O' , 'W/B/V' , 'W/V/Y' , 'W/N/R/B' , 'W/N/R/O' , 'W/N/R/G' ,
               'W/N/V/Y' , 'W/N/Y/M' , 'N/R/B/Y' , 'N/B/V/Y' , 'R/V/Y/O' , 'W/B/V/M' ,
               'W/B/V/O' , 'N/R/B/Y/M' , 'N/R/V/O/M' , 'W/N/R/Y/G' , 'N/R/B/V/Y' , 'W/R/B/V/Y/P' ,
                'W/N/R/B/Y/G' , 'W/N/R/B/V/O/M' , 'W/N/R/B/V/Y/M' , 'W/N/B/V/Y/G/M' , 'W/N/B/V/V/Y/P' ]

# 1. Build a counter object and and use counter and confirm they have the same values.
# Print off the total number of flower orders:
print(len(flower_orders))
# convert the flower_orders list to set and then back to a list. This will give us unique orders
unique_orders = list(set(flower_orders))
# the length of the unique_orders list should provide us with a count
unique_order_count = len(unique_orders)

# test to see if the orders list is the same between the counter object and the
# unique_orders list. Be sure to sort to ensure matching is correct. 
if list(Counter(flower_orders).keys()).sort() == unique_orders.sort():
    print("Unique Orders Match")
else:
    print("No Match")

# test to see if the number of entries between the counter object and the 
# unique_orders list are the same. We'll use a similar if/else test. Both should have 59 entries
if len(Counter(flower_orders).values()) == unique_order_count:
    print("Unique Order Counts Match: ", unique_order_count)
else:
    print("No Match. Collection Count: ",len(Counter(flower_orders).values()),
           " Unique Order List: ", unique_order_count)

# 2. Count how many objects have color W in them.
# set the counter variable
i = 0

# loop through the elements checking to see if "W" is in the item
# increment the iterator. Once complete print out the result. Should be 130
for item in Counter(flower_orders).elements():
    if "W" in item:
        i += 1
print("Elements with W: ", i)

# 3. Make histogram/bar plot of colors
import matplotlib.pyplot as plt

# plot top 10 unique order values based on the counter mappings
top_ten = Counter(flower_orders).most_common(10)
plt.bar(*zip(*top_ten)) 
plt.title("Top Ten Ordering Combinations")
plt.xlabel("Ordering Combination")
plt.ylabel("Count")
plt.show()

# now do a histogram/bar plot of individual colors
# define a dictionary to hold the results
colordict = {}
# loop through the counter, splitting each item into it's individual color parts
# if the color part already exists in the dictionary update the count value otherwise
# add it to the dictionary. 
for item in Counter(flower_orders).elements():
    colors = item.split("/")
    
    for color in colors:
        if color in colordict:
            colordict[color] = colordict.get(color) + 1
        else:
            colordict[color] = 1
        
#plot the individual colors
plt.bar(colordict.keys(), colordict.values())
plt.title("Individual Colors Counts")
plt.xlabel("Color Value")
plt.ylabel("Count")
plt.show()

# 4. Rank the tuples of color pairs regardless of how many colors in order.
# Reading this question it looks as simple as providing the unique color sets by the number ot times 
# they occur. We can use the counter.most_common() function to easily display this
Counter(flower_orders).most_common()

# 5. Rank the triples of color pairs regardless of how many colors in order.
from itertools import combinations
rankdict = {}

#define a method to pull out the pair combinations from the individual orders
def findPairs(lst):
    return [pair for pair in combinations(lst,2)]

# loop through the counter elements, remove the "/", find the pairs, build a dictionary of rankings
for item in Counter(flower_orders).elements():
    colors = item.replace("/","")
    pairs = findPairs(colors)
    
    for pair in pairs:
        if pair in rankdict:
            rankdict[pair] = rankdict.get(pair) + 1
        else:
            rankdict[pair] = 1   
  
# print out the rankings           
print(rankdict)

#plot the values
plt.bar(rankdict.keys(), rankdict.values()) 

# 6. Make dictionary of where keys are a color and values are what colors go with it
# setup the intial color dictionary
colorDict = {}

# define a function to get the color based on the value. Realize it's building the dictionary twice
# given the data, but in a real situation this method could be easier to update
def getColor(flower_color):
    switcher={"W" : "White", 
              "R" : "Red", 
              "B" : "Blue", 
              "V" : "Violet", 
              "Y" : "Yellow",
              "N" : "Indigo",
              "G" : "Green",
              "O" : "Orange",
              "M" : "Maroon",
              "P" : "Purple"}
    
    return switcher.get(flower_color,"Invalid Color")

# Iterate through our elements to get all the possible color values and assigning the color"
for item in Counter(flower_orders).elements():
    colors = item.split("/")
    
    for color in colors:
        
        colorDict[color] = getColor(color)

# print out the dictionary so we know the final outcome
print(colorDict)

# 7. Make a graph showing the probability of having an edge between two colors based on how
#    often they co-occur. (a numpy square matrix)
import numpy as np
import string

#build out the mapping array and probability array for the probability calculations
arraySize = 0
arraySize = len(colorDict)
mapArray = np.zeros((arraySize,arraySize))
probArray = np.zeros((arraySize,arraySize))


for item in Counter(flower_orders).elements():
    colors = item.replace("/","")
    
    for i in range(len(colors)-1):
        x = list(colorDict.keys()).index(colors[i])
        y = list(colorDict.keys()).index(colors[i+1])
        mapArray[x,y] = mapArray[x,y] + 1
        
# initialize the counter array
counter = mapArray.sum(axis=1)

#cycle through the main array and calculate our probabilities
i = 0

for row in mapArray:
    j = 0
    
    for cell in row:
        #check to make sure we don't try to divide by zero
        if counter[i] != 0:
            probVal = cell / counter[i]
        
        #check to make sure we have a real value
        if np.isnan(probVal):
            probVal = 0
            
        probArray[i,j] = probVal
        j +=1
    
    i += 1    
    
#Plot the data
for line in mapArray:
    plt.plot(line)
plt.xlabel("Color")
plt.ylabel("Probability")
plt.title("Transition Probabilities from color to color")
plt.show()  
    

# 8. Make 10 business questions related to the questions we asked above.
# - What are the total number of orders placed? A: 183
# - What are the number of distinct orders? A: 59
# - How many orders have white flowers? A: 130
# - What percentage of the total orders have white flowers?  A: approximately 71%
# - What is the most common order combination? A: White/Red/Blue at 30 orders
# - What color pairing occur most frequently? A: White/Red at 107
# - What color pairing had the lowest frequency of occurrence? A: Violet/Violet at 1
# - How many individual colors of flowers should be stocked? A: 10
# - What is the least common indivdual color? A: P (Purple)
# - What are the top ten ordering combinations? A: [('W/R/B', 30), ('W/R', 16), ('R/V/Y', 10), ('W/R/V', 10), 
# ('W/N/R/V', 8), ('W/R/B/Y', 6), ('B/Y', 5), ('R/B/Y', 5), ('W/N/R/B/V/Y', 5), ('W/G', 4)]

# Part 2 - Question 2
# ***************************************************************************
# Using the dead_men_tell_tales definition below answer the following questions:
# 1. Join everything
# 2. Remove spaces
# 3. Occurrence probabilities for letters
# 4. Tell me transition probabilities for every letter pairs
# 5. Make a 26x26 graph of 4. in numpy
# optional
# 6. plot graph of transition probabilities from letter to letter

dead_men_tell_tales = [ 'Four score and seven years ago our fathers brought forth on this' ,
                        'continent a new nation, conceived in liberty and dedicated to the' ,
                        'proposition that all men are created equal. Now we are engaged in' ,
                        'a great civil war, testing whether that nation or any nation so' ,
                        'conceived and so dedicated can long endure. We are met on a great' ,
                        'battlefield of that war. We have come to dedicate a portion of' ,
                        'that field as a final resting-place for those who here gave their' ,
                        'lives that that nation might live. It is altogether fitting and' ,
                        'proper that we should do this. But in a larger sense, we cannot' ,
                        'dedicate, we cannot consecrate, we cannot hallow this ground.' ,
                        'The brave men, living and dead who struggled here have consecrated' ,
                        'it far above our poor power to add or detract. The world will' ,
                        'little note nor long remember what we say here, but it can never' ,
                        'forget what they did here. It is for us the living rather to be' ,
                        'dedicated here to the unfinished work which they who fought here' ,
                        'have thus far so nobly advanced. It is rather for us to be here' ,
                        'dedicated to the great task remaining before us--that from these' ,
                        'honored dead we take increased devotion to that cause for which' ,
                        'they gave the last full measure of devotion--that we here highly' ,
                        'resolve that these dead shall not have died in vain, that this' ,
                        'nation under God shall have a new birth of freedom, and that' ,
                        'government of the people, by the people, for the people shall' ,
                        'not perish from the earth.' ]

# 1. Join everything
strVal = ""

#loop through the tuple and build out a single string value
for item in dead_men_tell_tales:
    strVal = strVal + item

print(strVal)

# 2. Remove spaces
noSpaceStr = strVal.replace(" ","")
print(noSpaceStr)

# 3. Occurrence probabilities for letters
# Assuming here that we're looking for letter frequency
count = Counter(noSpaceStr)

#print the total counter output
print(count)

#look for a specific count result. Use e, result is 165
print("Count of e in string is : " + str(count["e"]))

# 4. Tell me transition probabilities for every letter pairs
#lets clean the noSpacesStr to make it lowercase and remove all punctuation markers
newStr = noSpaceStr.lower()
newStr = "".join(let for let in newStr if let.isalpha())

import numpy as np
import string
# create a 26 x 26 numpy array of zeros
array1 = np.zeros((26,26))

# initialize the array looking at character by character mappings
for i in range(len(newStr)-1):
    #get the position in the alphabet of the current character and the next character
    #then plug into the array
    x = string.ascii_lowercase.index(newStr[i])
    y = string.ascii_lowercase.index(newStr[i+1])
    array1[x,y] = array1[x,y] + 1

#initialize the counter array
counter = array1.sum(axis=1)

 # create a 26 x 26 numpy array of zeros
probArray = np.zeros((26,26)) 

#cycle through the main array and calculate our probabilities
i = 0

for row in array1:
    j = 0
    
    for cell in row:
        #check to make sure we don't try to divide by zero
        if counter[i] != 0:
            probVal = cell / counter[i]
        
        #check to make sure we have a real value
        if np.isnan(probVal):
            probVal = 0
            
        probArray[i,j] = probVal
        j +=1
    
    i += 1

# 5. Make a 26x26 graph of 4. in numpy
# As part of the calculations for number 4 above the numpy array probArray was created
# We'll print the shape (26x26) to show that it meets the requirements. 
print(probArray.shape)

# optional
# 6. plot graph of transition probabilities from letter to letter
for line in probArray:
    plt.plot(line)
plt.xlabel("Alphabetical Letter (0=a...25=z)")
plt.ylabel("Probability")
plt.title("Transition Probabilities from letter to letter")
plt.show()

# 7. Flatten a nested list
# build out a nested list
nestedList = ['aa', ['c',['fff','ggg'], 'e', 'h'],'vv','nn']

# native python (no additional libraries)
flattened_list = [y for x in nestedList for y in x]
print(flattened_list)

# using itertools
import itertools
flattened_list2 = list(itertools.chain(*nestedList))
print(flattened_list2)