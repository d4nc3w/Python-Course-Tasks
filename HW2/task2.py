# Given the following text -> please generate a text with at least 100 words
# using the following analysis:
# 1. Count the occurrences of each word
# 2. Create a set of unique words
# 3. Create a list containg the lenghts of each word
# 4. Generate a list of words with a length greater than 5
# 5. Calculate average word length
# 6. Display the results of the analysis

text = "There should be some text I guess to check I will write some text myself There is some text then to check"
print(f"Analysis: ")
# (1)
wordCounter = {}
for word in text.split(" "):
    if word not in wordCounter:
        wordCounter[word] = 1
    else:
        wordCounter[word] += 1
print(f"Word counter: {wordCounter}")

# (2)
uniqueWords = []
for word in text.split(" "):
    if word not in uniqueWords:
        uniqueWords.append(word)
print(f"Unique words: {uniqueWords}")

# (3)
wordLengths = []
for word in text.split(" "):
    wordLengths.append(len(word))
print(f"Word lengths: {wordLengths}")

# (4)
longWords = []
for word in text.split(" "):
    if len(word) > 5:
        longWords.append(word)
print(f"Long words: {longWords}")

# (5)
averageWordLength = sum(wordLengths) / len(wordLengths)
print(f"Average word length: {averageWordLength}")
