import re
from base_extractor import BaseExtractor


class ExplanationExtractor(BaseExtractor):
    def extractSpan(self, question, sentence):
        sentence = sentence.lower()
        if re.search(r'\bbecause\s[^.]+', sentence):
            return re.search(r'\bbecause\s[^.]+', sentence).group(0)
        elif re.search(r'\bdue to\s[^.]+', sentence):
            return re.search(r'\bdue to\s[^.]+', sentence).group(0)
        elif re.search(r'\bas a result\s[^.]+', sentence):
            return re.search(r'\bas a result\s[^.]+', sentence).group(0)
        else:
            return sentence
