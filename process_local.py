import argparse
import os
import re
import json
import trie
import pickle

# Takes in file as argument
parser = argparse.ArgumentParser(description='Process email data from a folder')
parser.add_argument('data_path',
                    help='Path containing email data')
args = parser.parse_args()
maildir = args.data_path
print("Loading email data from: ", maildir)

# A word map from word -> [authors]
words_map = {}
metadata = ['Message-ID:', 'Date:', 'From:', 'To:', 'cc:', 'Subject:', 'Mime-Version:', 'Content-Type:', 'Content-Transfer-Encoding:', 'X-From:', 'X-To:', 'X-cc:', 'X-bcc:', 'X-Folder:', 'X-Origin:', 'X-FileName:', '@', '________', '-----']
# Go through the maildir. For each individual, save the content from all_contents
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
            with open(filePath, encoding='utf-8', errors='ignore') as f:
                contents = f.readlines()
                for line in contents: # process line content
                    is_metadata = False
                    for m in metadata:
                        if m in line:
                            is_metadata = True
                    if is_metadata:
                        continue

                    words = line.split()
                    words = [w.lower() for w in words]

                    for w in words:
                        # Get rid of non alphabet characters
                        regex = re.compile('[^a-zA-Z]')
                        word = regex.sub('', w)

                        # Update person_word_map and words_map
                        if len(word) > 1:
                            if word not in person_word_map:
                                person_word_map[word] = [file]
                            elif file not in person_word_map[word]:
                                person_word_map[word].append(file)

                            if word not in words_map:
                                words_map[word] = [person]
                            elif person not in words_map[word]:
                                words_map[word].append(person)

        with open('people_small/' + person, 'w') as f:
            json.dump(person_word_map, f)

# CREATE THE TRIE
# email_trie = trie.Trie()
word_trie = trie.Trie()

for word in words_map:
    # email_trie.insert(word, words_map[word])
    word_trie.insert(word, None)

# save trie to disk
print("saving word map...")
with open('word_map_small.json', 'w') as f:
    json.dump(words_map, f)

# file_name = "email_trie_small.pkl"
# # open the file for writing
# fileObject = open(file_name,'wb')
# print("email trie: ", email_trie)
# pickle.dump(email_trie,fileObject,-1)
# fileObject.close()

print("saving word trie...")
file_name = "word_trie_small.pkl"
# open the file for writing
fileObject = open(file_name,'wb')
print("word trie: ", word_trie)
pickle.dump(word_trie,fileObject,-1)
fileObject.close()
