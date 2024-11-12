class RegexEngine:
    def __init__(self, pattern):
        self.tokens = self.scan(pattern)
    
    def scan(self, pattern):
        # Scanner// for the pattern input
        tokens = []
        i = 0
        while i < len(pattern):
            if pattern[i] in {'*', '+', '|', '(', ')', '.'}:
                tokens.append(pattern[i])
                i += 1
            elif pattern[i].isalpha():  #For single char
                tokens.append(pattern[i])
                i += 1
            else:
                raise ValueError(f"Unrecognized character: {pattern[i]}")
        return tokens

    def match(self, text):
        # Matching the input of the text
        return self.match_pattern(self.tokens, text)

    def match_pattern(self, tokens, text):
        # Recursive 
        if not tokens:
            return not text

        first_token = tokens[0]
        first_match = bool(text) and (first_token == text[0] or first_token == '.')

        if len(tokens) >= 2 and tokens[1] in "*+":
            if tokens[1] == '*':
                return (self.match_pattern(tokens[2:], text) or
                        first_match and self.match_pattern(tokens, text[1:]))
            elif tokens[1] == '+':
                return first_match and (self.match_pattern(tokens[2:], text[1:]) or
                                        self.match_pattern(tokens, text[1:]))
        elif len(tokens) >= 2 and tokens[1] == '|':
            return self.match_pattern(tokens[2:], text) or self.match_pattern(tokens[1:], text)
        else:
            return first_match and self.match_pattern(tokens[1:], text[1:])

# Test cases
engine = RegexEngine("A*B|C")
print(engine.match("AAAAAB"))  # t
print(engine.match("C"))       # t
print(engine.match("D"))       # f
