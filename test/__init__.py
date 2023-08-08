import requests
import re

#Use the API
response = requests.get("https://dinoipsum.com/api/?format=text&paragraphs=1&words=50")

#Extract the vocabulary
words = re.findall(r'\w+',response.text)

#Find the maximum and minimum string length
longest = max(words, key = len)
shortest = min(words, key = len)

#Create a list that holds the longest and shortest words
longest_ones = []
shortest_ones = []

#Go through the list of words and find the words that are as long as the longest or the shortest
for word in words:
    if len(word) == len(longest):
        longest_ones.append(word)
    if len(word) == len(shortest):
        shortest_ones.append(word)

#The output
print('longest ' + str(longest_ones) + ' shortest ' + str(shortest_ones))
for word in words:
    print(word + ' ' + str(len(word)))
