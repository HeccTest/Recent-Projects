# Kai Lun He
# August 10, 2022
# tested using python 3.10.6 on a windows 11 machine

# initial thoughts / outline: iterate through the file and make a list of movies star names and their number of appearances
# if the movie star is not on our list, append them and give them a count of 1. if they are on the list add 1.
# once our list is complete, iterate through the list looking for names with more than 2 movies, each instance found will need to iterate through json file again to average scores
# then print (maybe improve this once working for better efficiency).

import json
from collections import Counter

f = open("data.json", "r")
data = json.load(f)

starList = [] # a list containing the names of the movie stars, names can be duplicate (the number of times a name appears indicates the number of movies they were in)
for i in data:
    movieCast = i['stars'].split(", ") # splits all the actors from one movie into a list
    for j in movieCast: # iterate through each actor / actress , can technically just do (j in range 4), but not every movie will have only 4 actors / actresses
        starList.append(j) # make a big list of names, may contain many duplicates


starList = [item for items, c in Counter(starList).most_common() for item in [items] * c] 
# sorting the list by number of occurences (online solution, not my own. Ideally bypass this with a different implementation altogether)


while(len(starList) > 1): # do until our list is emptied out
    movieRating = 0
    starName = starList[len(starList) - 1] # get the last name (least common) in the list (will be removed once processed, should be a unique name each iteration)
    if(starList.count(starName) >= 2): # if the star appears in more than 2 movies, we will consider them
        for i in data: # iterate through json file again (not ideal)
            if(starName in i['stars']): # get the rating for movies the actor / actress is in
                movieRating += float(i['rating'])
        print("Star Name: ", starName, "\t\t\t| Movies: ", starList.count(starName), "\t| AVG Rating: ", "%0.2f" % (movieRating / starList.count(starName))) # formatting
    for i in range(starList.count(starName)): # unconditionally remove all instances of the current starName from our list
        starList.remove(starName)


# this implementation is rather crude and inefficient. Ideally I would have gotten 2d lists working, but I am a little unsure of how to do so in python.