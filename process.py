# Go through the maildir. For each individual, save the content from all_contents
import os
import re
import json

maildir = "test"

# TODO: pass in file as argument

words_map = {}
for filename in os.listdir(maildir):

    person = filename
    person_dir = maildir + "/" + person
    print("reading contents in this person's mailbox: " + person)

    if "all_documents" not in os.listdir(person_dir):
        continue
    else:
        all_docs = person_dir + "/" + "all_documents"

        for file in os.listdir(all_docs):
            filePath = all_docs + "/" + file
            with open(filePath) as f:
                contents = f.readlines()
                for line in contents:
                    words = line.split()
                    for w in words:
                        word = re.sub(r'\W+', '', w)
                        if len(word) > 0:
                            if word not in words_map:
                                words_map[word] = {person: [file]}
                            else:
                                if person not in words_map[word]:
                                    words_map[word][person] = [file]
                                if file not in words_map[word][person]:
                                    words_map[word][person].append(file)

print ("exporting map...")

# dump the map to disk
with open('mail_map.json', 'w') as outfile:
    json.dump(words_map, outfile)
