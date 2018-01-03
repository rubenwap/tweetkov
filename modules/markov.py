
import markovify

def make_sentence(corpus):
    text_model = markovify.Text(corpus)
    return text_model.make_short_sentence(140)
