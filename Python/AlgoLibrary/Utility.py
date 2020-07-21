def splitText(text, tok_len) -> list: # text : 문자열(str), tok_len : 자를 길이(list)
    return [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
