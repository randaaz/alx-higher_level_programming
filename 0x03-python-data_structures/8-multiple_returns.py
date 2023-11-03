#!/usr/bin/python3
def multiple_returns(sentence):
    Length = len(sentence)
    return (Length, sentence[0] if len(sentence) > 0 else None)
