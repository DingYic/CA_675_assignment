# !/user/bin/env python

# libraries required to calculate tf idf and perform other operations
import sys
import numpy as np
from nltk.tokenize import word_tokenize
import warnings

warnings.filterwarnings('ignore')

# read the input that is printed by the mapper
dataFrame = sys.stdin

# declaring two variables to store the information to calculate tf idf score
sentences = []
words = []

# iterating through the data frame to pass input to the word tokenizer and identify the word
for sent in dataFrame:
    sec = [word.lower for word in word_tokenize(sent) if word.isAlpha()]
    # append sentence from the data frame to the sentences variable
    sentences.append(sec)
    for w in sec:
        # append words from the sentences to the words variable
        words.append(w)

# convert the output of words to a set format to remove duplicate values
words = set(words)
# find the total number of records in the data frame
totalDocs = len(dataFrame)

wordIndex = {}
# iterate the words
for i, word in enumerate(words):
    # create a word index
    wordIndex[word] = i

wordCount = []
countDict = {}
# iterate the words
for word in words:
    # create a dictionary of words
    countDict[word] = 0
for sentence in sentences:
    for word in sentence:
        # update the occurrence of the word in the sentence
        countDict[word] += 1

# update the word count dictionary
wordCount = countDict


# method to calculate term frequency
def termFrequencyValue(document, a):
    # calculate the length of the document
    n = len(document)
    # calculate the occurrences of the word in the document
    occ = len([token for token in document if token == a])
    # divide the occurrences by the length of the document which will result in the tf value
    return occ / n


# method to calculate inverse document frequency
def inverseDocumentFrequencyValue(x):
    # try block to identify word from the word count dictionary
    try:
        oc = wordCount[x] + 1
    # if exception is thrown assign the value to 0
    except:
        oc = 0
    # use numpy library with the function log to return idf
    return np.log(totalDocs / oc)


# method to calculate tf and idf
def calculateTfIdf(s):
    # define a vector using numpy function 0
    vector = np.zeros((len(words),))
    # iterate the sentence for words in the sentence
    for y in s:
        # y is the word and s is the sentence passed
        # pass sentence and the word as input
        tf = termFrequencyValue(s, y)
        # pass word as an input
        idf = inverseDocumentFrequencyValue(y)
        # create a tf idf vector for the word present in the word index
        vector[wordIndex[y]] = tf * idf
    return vector


# defining an output vector
vectors = []
# iterate the sentences and add the values to the vector
for sentence in sentences:
    vectors.append(calculateTfIdf(sentence))

# print vector output
print(vectors)