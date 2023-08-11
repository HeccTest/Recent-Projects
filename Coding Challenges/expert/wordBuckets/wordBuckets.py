"""
Project

    Write a function that divides a phrase into word buckets, with each bucket containing n or fewer characters. Only include full words inside each bucket.

Examples

    split_into_buckets("she sells sea shells by the sea", 10)
    ➞ ["she sells", "sea shells", "by the sea"]

    split_into_buckets("the mouse jumped over the cheese", 7)
    ➞ ["the", "mouse", "jumped", "over", "the", "cheese"]

    split_into_buckets("fairy dust coated the air", 20)
    ➞ ["fairy dust coated", "the air"]

    split_into_buckets("a b c d e", 2)
    ➞ ["a", "b", "c", "d", "e"]

Notes

    - Spaces count as one character.
    - Trim beginning and end spaces for each word bucket (see final example).
    - If buckets are too small to hold a single word, return an empty list: []
    - The final goal isn't to return just the words with a length equal (or lower) to the given n, but to return the entire given phrase bucketized (if possible). So, for the specific case of "by" the only word with a proper length, the phrase can't be bucketized, and the returned list has to be empty.
    LINK: https://edabit.com/challenge/grorumaEjyFDmZQCx

Thoughts

    - if at least one word cannot be held, the entire bucket fails, and simply return empty list.
    - order seems to matter, so I will simply linearly iterate through the phrase

"""

def split_into_buckets(phrase, n):
	returnList = []
	currBucket = ""
	bucketCount = 0

	wordList = phrase.split()
	i = 0
	while(i <= len(wordList)):
		if(i == len(wordList)):
			returnList.append(currBucket)
			return(returnList)
		if(bucketCount == 0):
			if(len(wordList[i]) <= n):
				currBucket += wordList[i]
				bucketCount += len(wordList[i])
			else: # empty bucket, that cannot hold a word
				return([])
		else:
			if(len(wordList[i]) + bucketCount + 1 <= n):
				currBucket += " " + wordList[i]
				bucketCount += len(wordList[i]) + 1
			else:
				returnList.append(currBucket)
				currBucket = ""
				bucketCount = 0
				i -= 1
		i += 1
		

# Complete and tested Aug. 11, 2023. See test_wordBuckets.py for test cases.