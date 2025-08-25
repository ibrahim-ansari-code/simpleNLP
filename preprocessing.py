class Preprocessing:
    def __init__(self, text):
        self.raw_text = text

    def cleanText(self):
        lowered = self.raw_text.lower()
        noPunctuation = "".join([c if c.isalnum() or c.isspace() else " " for c in lowered])
        single_spaced = ""
        prev = ""
        for c in noPunctuation:
            if not (c == " " and prev == " "):
                single_spaced += c
            prev = c
        return single_spaced.strip()

    def segmentSentences(self):
        result, current = [], ""
        for ch in self.raw_text:
            current += ch
            if ch in ".!?":
                result.append(current.strip())
                current = ""
        if current.strip():
            result.append(current.strip())
        return [s for s in result if s]

    def tokenizer(self):
        cleaned = self.cleanText()
        tokens, word = [], ""
        for c in cleaned:
            if c.isalnum():
                word += c
            else:
                if word:
                    tokens.append(word)
                    word = ""
        if word:
            tokens.append(word)
        return tokens
