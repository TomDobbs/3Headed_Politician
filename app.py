from flask import Flask, request, render_template
from chain_builder import get_sentence
import cPickle as pickle
from itertools import count

app = Flask(__name__)
app.debug = True

with open('f_dict.pkl') as f:
    f_dict = pickle.load(f)

with open('r_dict.pkl') as f:
    r_dict = pickle.load(f)

with open('count.pkl') as f:
    counter = count(pickle.load(f))

# Main page
@app.route('/')
def index():
    return render_template("index.html")

# Home Page
@app.route('/api/v0')
def get_statement():
    word = request.args['q']
    sentence = get_sentence(word, f_dict, r_dict, randomness = 1)
    page = sentence
    return page

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
