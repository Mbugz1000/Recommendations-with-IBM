import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer

def clean_body(body):
    body = body.lower()
    punctuation_removed = re.sub(r"[^a-zA-Z0-9]", " ", body)
    tokenized = word_tokenize(punctuation_removed)
    no_stop_words = [word for word in tokenized if word not in stopwords.words('english')]

    lemmatizer = WordNetLemmatizer()
    clean_tokens = [lemmatizer.lemmatize(token).strip() for token in no_stop_words]
    
    return clean_tokens