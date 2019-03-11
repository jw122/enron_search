import os
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import json
import argparse
import trie
import search
import pickle

# from models import Word

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Word(db.Model):
    __tablename__ = 'words'

    id = db.Column(db.Integer, primary_key=True)
    term = db.Column(db.String())
    people = db.Column(db.String())

    def __init__(self, term, people):
        self.term = term
        self.people = people

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'term': self.term,
            'people': self.people
        }

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

@app.route('/search')
def search():
    try:
        keyword = request.args.get('term', 0, type=str)
        if keyword in word_map:
            return jsonify(result=word_map[keyword])
    except Exception as e:
        return str(e)

@app.route("/get/<id_>")
def get_by_id(id_):
    try:
        word=Word.query.filter_by(id=id_).first()
        return jsonify(word.serialize())
    except Exception as e:
	    return(str(e))

@app.route("/get_term/<term_>")
def get_by_term(term_):
    try:
        word=Word.query.filter(Word.term==term_).first()
        return jsonify(word.serialize())
    except Exception as e:
	    return(str(e))

# WIP: Storing into postgres in a loop
def add_word(file_path):
    print("in add word!")
    with open(file_path,'r') as f:
        word_map = json.load(f)
        for w in word_map:
            authors = word_map[w]
            # stringify authors, store into db
            term=w
            people=json.dumps(authors)
            print("adding term to postgres: ", term)
            try:
                word=Word(
                    term=term,
                    people=people
                )
                db.session.add(word)

                print("Word {} added. id={}".format(term, word.id))
                return "Word {} added. id={}".format(term, word.id)
            except Exception as e:
                print("could not add: ", str(e))
                return(str(e))
    db.session.commit()
if __name__ == '__main__':
   app.run(debug=True)
   # add_word('word_map_small.json')
