class StackQ:
    def __init__(self):
        self.stack = []

    def push(self, question, answer):
        self.stack.append((question, answer))

    def last(self):
        return self.stack[-1] if len(self.stack) > 0 else (None, None)

    def history(self, n=5):
        start = max(0, len(self.stack) - n)
        return self.stack[start:]
