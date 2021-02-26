# CountingWords: Counts the total number of words in different text files or text entries.
def countingWords(text):
    return len(text.split())

# WordCount: Counts the number of occurrences of each word in a text file.
def wordCount(text):
    counts = dict()
    words = text.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return str(counts)