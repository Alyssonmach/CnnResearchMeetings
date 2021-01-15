from ex120_word_counts import count_words

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']

for filename in filenames:
    filename = 'content_n_exceptions/files/'.__add__(filename)
    count_words(filename)