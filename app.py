from flask import Flask, render_template, request, jsonify
import json
import argparse
import trie
import search_local
import pickle

app = Flask(__name__)

'''
Initializing the trie and word map, which power the search functionality
'''

# load word trie
word_trie_fp = open('word_trie.pkl','rb')
word_trie = pickle.load(word_trie_fp)
print("Word trie loaded: ", word_trie)
# load word map
with open('word_map.json') as f:
    word_map = json.load(f)
print("Word map loaded")

'''
Templates & User interactions
'''
@app.route('/', methods=['GET', 'POST'])
@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/get_completions')
def get_completions():
	try:
		q = request.args.get('search_term', 0, type=str)
		# Use the trie (prefix tree) to find completions
		res = word_trie.getChildren(q)[:10]
		return jsonify(result=res)

	except Exception as e:
		return str(e)


if __name__ == '__main__':
   app.run(debug=True)
