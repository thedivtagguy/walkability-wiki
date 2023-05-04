import nltk
import re
from collections import Counter
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the document
with open(
    "D:/Data Projects/walkability/walkability-wiki/_book/bookdown-demo.tex", "r"
) as f:
    document = f.read()

# Remove LaTeX commands
document = re.sub(r"\\[a-zA-Z]+", "", document)

# Tokenize the document
tokens = nltk.word_tokenize(document)

# Remove stopwords
stopwords = set(stopwords.words("english"))
stopwords.update(["fig", "tab", "figure", "minipage"])
words = [token.lower() for token in tokens if token.lower() not in stopwords]

# Remove punctuation
words = [word for word in words if word.isalpha()]
# Remove duplicate words
new_words = []
for word in words:
    if word not in new_words:
        new_words.append(word)
print(new_words)

# Frequency analysis
freq_dist = nltk.FreqDist(words)
print("Frequency Analysis:")
for word, freq in freq_dist.most_common(10):
    print(f"{word}: {freq}")

# TF-IDF analysis
cleaned_doc = " ".join(words)
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(
    [cleaned_doc]
)  # Updated to use cleaned list of words
feature_names = tfidf.get_feature_names_out()
tfidf_scores = zip(feature_names, tfidf_matrix.toarray()[0])
tfidf_scores = sorted(tfidf_scores, key=lambda x: x[1], reverse=True)


# Print the top 30 important words based on TF-IDF scores
print("\nTop 30 Important Words Based on TF-IDF Scores:")
for word, score in tfidf_scores[:30]:
    print(f"{word}: {score:.4f}")
