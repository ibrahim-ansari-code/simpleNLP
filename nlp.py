from preprocessing import Preprocessing
from classifier import Classifier
from keywords import Keywords
from similarity import Similarity
from stack_q import StackQ
from definition_extractor import DefinitionExtractor
from explanation_extractor import ExplanationExtractor
from span_extractor import SpanExtractor
from sentence_extractor import SentenceExtractor


class NLP:
    def __init__(self, text):
        self.raw_text = text
        self.pre = Preprocessing(text)

        self.cleaned = self.pre.cleanText()
        self.sentences = self.pre.segmentSentences()
        self.tokens = self.pre.tokenizer()

        self.stack = StackQ()
        self.keywords = Keywords(self.cleaned).keywords()
        self.similarity = Similarity(self.sentences)

    def chooseExtractor(self, q_type):
        if q_type == "definition":
            return DefinitionExtractor()
        elif q_type == "fact":
            return SpanExtractor()
        elif q_type == "explanation":
            return ExplanationExtractor()
        else:
            return SentenceExtractor()

    def handleQuestion(self, query):
        if query.lower() in ["explain this", "what does that mean"]:
            lastQ, lastAns = self.stack.last()
            print(f"[Follow-up detected — referring to: '{lastQ}']")
            query = f"Explain: {lastAns}"

        q_type = Classifier(query).classify()
        questionTokens = Preprocessing(query).tokenizer()

        sim_matches = self.similarity.findSimilar(
            query, boost_keywords=self.keywords, questionsTokens=questionTokens
        )
        extractor = self.chooseExtractor(q_type)

        answers = [(extractor.extractSpan(query, sent), score) for sent, score in sim_matches]

        best = answers[0][0] if len(answers) > 0 else "No answer found."
        self.stack.push(query, best)

        return q_type, answers, self.stack.history()
