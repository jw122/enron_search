from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/home')
def home():
	return render_template('home.html')

if __name__ == '__main__':
   app.run(debug=True)
