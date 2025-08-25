from sklearn.feature_extraction.text import TfidfVectorizer


class Keywords:
    def __init__(self, text, max=10):
        self.text = text
        self.max = max

    def keywords(self):
        vectorizer = TfidfVectorizer()
        tfidfMatrix = vectorizer.fit_transform([self.text])
        tfidfArray = tfidfMatrix.toarray()[0]
        featureNames = vectorizer.get_feature_names_out()

        pairs = [(featureNames[i], tfidfArray[i]) for i in range(len(tfidfArray))]

        for i in range(len(pairs)):
            for j in range(0, len(pairs) - i - 1):
                if pairs[j][1] < pairs[j + 1][1]:
                    pairs[j], pairs[j + 1] = pairs[j + 1], pairs[j]

        return [pairs[i][0] for i in range(min(self.max, len(pairs)))]
