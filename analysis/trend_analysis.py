import pandas as pd
from collections import defaultdict
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'http\S+', '', text)  # Remove URLs
    text = re.sub(r'@\w+', '', text)  # Remove mentions
    text = re.sub(r'#\w+', '', text)  # Remove hashtags
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    return tokens

def analyze_trends(frames):
    trend_data = defaultdict(list)
    for frame in frames:
        content = frame.get('content', '')
        tokens = preprocess_text(content)
        for token in tokens:
            trend_data[token].append(frame['timestamp'])
    
    trend_df = pd.DataFrame([(key, len(values), values) for key, values in trend_data.items()],
                            columns=['keyword', 'count', 'timestamps'])
    trend_df = trend_df.sort_values(by='count', ascending=False)
    return trend_df
