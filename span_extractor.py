import re
from base_extractor import BaseExtractor


class SpanExtractor(BaseExtractor):
    def extractSpan(self, question, sentence):
        question = question.lower()
        sentence = sentence.lower()

        qkeywords = [w for w in re.findall(r'\b\w{3,}\b', question)]
        words = [w for w in re.findall(r'\b\w+\b', sentence)]

        matches = [w for w in words if w in qkeywords]

        if len(matches) == 0:
            return sentence

        first = words.index(matches[0])
        last = words.index(matches[-1])

        start = first - 2 if first - 2 >= 0 else 0
        end = last + 3 if last + 3 <= len(words) else len(words)

        span = [words[i] for i in range(start, end)]
        return ' '.join(span)
