class Classifier:
    def __init__(self, question):
        self.question = question.lower()

    def classify(self):
        if self.question.startswith("what is") or "define" in self.question:
            return "definition"
        elif self.question.startswith("why") or "cause" in self.question:
            return "explanation"
        elif self.question.endswith("?"):
            return "fact"
        else:
            return "unknown"
