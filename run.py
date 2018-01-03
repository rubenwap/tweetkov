from flask import Flask, render_template, Response
from modules import twitter
from modules import markov
import json

app = Flask(__name__, static_url_path='/static')


@app.route("/")
def start_page():
    return render_template('index.html')


@app.route("/user/<string:handle>")
def generate_tweet(handle):
    corpus = twitter.download_tweets(handle)
    return Response(json.dumps({"user": handle, "tweetkov": markov.make_sentence(corpus)}), mimetype='application/json')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
