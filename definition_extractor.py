import re
from base_extractor import BaseExtractor


class DefinitionExtractor(BaseExtractor):
    def extractSpan(self, question, sentence):
        sentence = sentence.lower()
        if re.search(r'\bis\s[^.]+', sentence):
            return re.search(r'\bis\s[^.]+', sentence).group(0)
        elif re.search(r'\bare\s[^.]+', sentence):
            return re.search(r'\bare\s[^.]+', sentence).group(0)
        elif re.search(r'\bmeans\s[^.]+', sentence):
            return re.search(r'\bmeans\s[^.]+', sentence).group(0)
        else:
            return sentence
