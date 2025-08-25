from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class Similarity:
    def __init__(self, sentences, top_n=3):
        self.sentences = sentences
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix = self.vectorizer.fit_transform(sentences)
        self.top_n = top_n

    def findSimilar(self, query, boost_keywords=None, questionsTokens=None):
        questionVector = self.vectorizer.transform([query])
        scoreArray = cosine_similarity(questionVector, self.tfidf_matrix).flatten()

        if boost_keywords is None:
            boost_keywords = []
        if questionsTokens is None:
            questionsTokens = []

        for i, sentence in enumerate(self.sentences):
            keywordCount = sum(1 for kw in boost_keywords if kw.lower() in sentence.lower())
            tokenMatches = sum(1 for t in questionsTokens if t.lower() in sentence.lower())
            scoreArray[i] += 0.05 * keywordCount + 0.03 * tokenMatches

        ranked = [(self.sentences[i], scoreArray[i]) for i in range(len(scoreArray))]

        for i in range(len(ranked)):
            for j in range(0, len(ranked) - i - 1):
                if ranked[j][1] < ranked[j + 1][1]:
                    ranked[j], ranked[j + 1] = ranked[j + 1], ranked[j]

        return ranked[:self.top_n]
