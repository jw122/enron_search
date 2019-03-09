# Go through the maildir. For each individual, save the content from all_contents
import os
import re
import json
import trie
import pickle

maildir = "test"

# TODO: pass in file as argument?

# A word map from word -> {author: [list of emails]}
words_map = {}
for filename in os.listdir(maildir):
    # Loop through all the individuals in the maildir
    person = filename
    person_dir = maildir + "/" + person
    print('Reading contents from {}\'s mailbox'.format(person))

    if "all_documents" not in os.listdir(person_dir):
        continue
    else:
        all_docs = person_dir + "/" + "all_documents"
        person_word_map = {}

        # Open the files in this person's "all_documents" folder
        for file in os.listdir(all_docs):
            filePath = all_docs + "/" + file
            with open(filePath) as f:
                contents = f.readlines()
                for line in contents:
                    words = line.split()
                    # TODO: can scan for delimiter to avoid words in email metadata
                    for w in words:
                        # Get rid of non alphanumeric characters
                        word = re.sub(r'\W+', '', w)
                        # Add the word and its author + email id to the map
                        if len(word) > 0:
                            if word not in person_word_map:
                                person_word_map[word] = [file]
                            elif file not in person_word_map[word]:
                                person_word_map[word].append(file)

                            if word not in words_map:
                                words_map[word] = [person]
                            elif person not in words_map[word]:
                                words_map[word].append(person)

        # print("person word map: ", person_word_map)
        with open('people/' + person, 'w') as f:
            json.dump(person_word_map, f)

# print("words map: ", words_map)
print ("creating trie from word map...")

# dump the map to disk
# with open('mail_map_small.json', 'w') as outfile:
#     json.dump(words_map, outfile)

# CREATE THE TRIE
email_trie = trie.Trie()

for word in words_map:
    email_trie.insert(word, words_map[word])

# save trie to disk
file_name = "email_trie"
# open the file for writing
fileObject = open(file_name,'wb')
print("email trie: ", email_trie)
pickle.dump(email_trie,fileObject)
fileObject.close()
