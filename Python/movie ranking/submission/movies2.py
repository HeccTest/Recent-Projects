# Kai Lun He
# August 10, 2022
# tested using python 3.10.6 on a windows 11 machine

# revision 2. Goal: better efficiency through use of psudo multidimentional lists

import json

f = open("data.json", "r")
data = json.load(f)

starNames = [] # a list containing the names of the movie stars, names cannot be duplicates. Any time an actor / actress stars in more than one movie their movieCount will increment by one instead.
movieCount = [] # a list containing the number of movies an actor / actress has been in. the index will match that of starNames 
# (ie. if Tom Holland is index 0 of starNames, index 0 of movieCount is how many movies Tom Holland has been in)
movieRatings = [] # same as movieCount, but for summative rating. Average will be found by movieRatings[i] / movieCount[i]

for i in data:
    movieCast = i['stars'].split(", ") # splits all the actors from one movie into a list
    rating = float(i['rating']) # get the rating, casted to a float
    for j in movieCast: # iterate through each actor / actress , can technically just do (j in range 4), but not every movie will have only 4 actors / actresses
        if (j in starNames): # if this star is already in my list (change the values of my list, rather than simply appending to them)
            starIndex = starNames.index(j) # find the index of the star's name so I could alter their movie count and cumulative movie rating
            movieCount[starIndex] = (movieCount[starIndex] + 1) # increment the number of movies the star has been in by 1
            movieRatings[starIndex] = (movieRatings[starIndex] + rating)
        else: # if star not in list yet
            starNames.append(j)
            movieCount.append(1)
            movieRatings.append(rating)

maxMovieCount = 0
for i in range(len(movieCount)): # get the star with the most movies. Used to determine how many times I need to run the print statement
    maxMovieCount = max(maxMovieCount, movieCount[i])

for i in range(1, maxMovieCount): # iterate from 1 to maxMovieCount. Used to print stars with the least number of movies in to the the stars with most movies in
    for j in range(len(movieCount)): # iterate through the movieCount of stars (will have to do this maxMovieCount - 2 times. Not ideal but better than reading the json file a bunch)
        if(movieCount[j] == i + 1):
            print("Star Name: ", starNames[j], "\t\t| Movies: ", movieCount[j], "\t| AVG Rating: ", "%0.2f" % (movieRatings[j] / movieCount[j])) # formatting