import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
from nltk import word_tokenize  
from nltk import sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer

def preprocessor(text):
    all_words = word_tokenize(text)
    #lowercase text
    lower_case_words = [w.lower() for w in all_words]
    words = [word for word in lower_case_words if word.isalpha()]
    #remove unwanted words
    remove_words_list = set(stopwords.words('english'))
    filtered_words = [w for w in words if not w in remove_words_list]
    filtered_words = [w for w in filtered_words if not w in "br"]
    #lemmatenize words
    lemmatized_words = [WordNetLemmatizer().lemmatize(w) for w in filtered_words]
    #steam words
    porter = SnowballStemmer('english')
    stemmed_words = [porter.stem(word) for word in lemmatized_words]
    final_text = ' '.join([str(word) for word in stemmed_words ])
    return final_text