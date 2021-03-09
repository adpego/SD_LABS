# countingWords: Counts the total number of words in different text files or text entries.
def countingWords(text):
    return len(text.split())

# wordCount: Counts the number of occurrences of each word in a text file.
def wordCount(text):
    counts = dict()
    words = text.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return str(counts)

# do_request: do a request
def do_request(URL):
    return requests.get(URL).text